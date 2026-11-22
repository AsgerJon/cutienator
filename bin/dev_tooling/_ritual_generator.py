"""RitualGenerator writes the ritual file of one Qt class, and the rows
file that goes with it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import collections
import json
import os
import re
import textwrap
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree, QtPart

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Rituals = Tuple[Record, ...]
  Records = Tuple[Record, ...]
  Reasons = Tuple[Tuple[str, str], ...]
  Rows = Dict[str, Tuple[str, ...]]


class RitualGenerator:
  """
  Writes the ritual file of one Qt class: one ritual for each function
  of the class whose types it can pass. Beside it goes the rows file,
  which says for Python what each ritual takes and gives. This is the
  generator side of the tooling; 'RitualTester' is the side that
  verifies what it wrote.

    generator = RitualGenerator()
    generator.setDependencyTree(tree)
    generator.setClassName('QObject')
    generator.setWorkFolder('/some/folder')
    generator.write()            # writes '/some/folder/q_object.cpp'
                                 # and '/some/folder/q_object.json'
    generator.getWritten()       # the rituals in that file
    generator.getNotWritten()    # the other functions, with reasons

  Terms
  -----

  - A ritual is one function of ours that Python can call, and that
    calls one Qt function. It is named 'ritual' followed by the
    compiler's own name for that Qt function.
  - A ritual file is a C++ file holding rituals.
  - To pass a type is to hand a value of it from Python to C++, or
    back.
  - A row says, for one ritual, what comes back from it and then what
    goes into it, one word each. 'cutienator.occult.Rituals' reads the
    rows to know how to call each ritual.
  - A value class is a class C++ can copy, as 'QSize'. C++ hands such
    an object around as a copy, where it hands a 'QObject' around by
    its address.

  You provide
  -----------

  - 'setDependencyTree': the tree of the parts of Qt, which knows the
    classes, the enums and the records. Required.
  - 'setClassName': the class to write rituals for. Required.
  - 'setWorkFolder': an existing folder for the ritual file. Required
    before 'write' only.

  Types it can pass
  -----------------

  - Nothing: a function giving back 'void'.
  - Numbers: 'bool' and the numbers built into C++, as 'int' and
    'double', also under a second name, as 'qsizetype', and taken to
    be read only, as 'const bool' and 'const int &'.
  - A number the function may change, taken as 'int &' or 'int *'.
    The ritual takes the address of the number and hands Qt the number
    there. Giving one back is not written.
  - Text as C has it: 'const char *'.
  - The texts a program was started with, 'char **'. The ritual takes
    the address of the first and hands it on. Giving such back is not
    written.
  - Enums, as 'Qt::TimerType'.
  - Flags: the type Qt names for the combinations of a flags enum, as
    'Qt::WindowFlags', which C++ reads as 'QFlags<Qt::WindowType>'. The
    ritual takes and gives the number of the combination as an 'int'.
  - Addresses of objects: 'QThread *' and 'const QObject *', for every
    class of the tree.
  - Values: 'QSize', 'const QSize' and 'const QSize &', for every class
    of the tree C++ can copy. The ritual takes the address of one and
    hands Qt the object there, which Qt copies if it keeps it. For one
    given back, the ritual makes a copy with 'new' and gives its
    address: that copy is known to nobody else, and whoever called the
    ritual has to remove it.
  - Text: Qt's 'QString' in each of those three spellings, and the two
    classes that look at text held elsewhere, 'QStringView' and
    'QAnyStringView'. It is passed as a value of 'QString', and its
    word in the row is 'text', so Python passes a plain 'str'.

  The words of a row
  ------------------

  - 'nothing': the ritual gives nothing back.
  - 'address': the address of an object, a value class included; of
    a number the function may change; or of the first of the texts a
    program was started with.
  - 'text': the address of a 'QString' that is made from a 'str' for
    the call, or read into a 'str' after it.
  - 'chars': text as C has it, 'const char *'.
  - A number goes by the name C++ has for it, as 'int', 'bool' and
    'long long'. An enum goes by the number type it is kept as.
  - Flags go as 'int'. Qt keeps the combinations of a flags enum in a
    number as wide as an 'int', with a sign on one system and without
    on another, so the ritual hands the 32 bits over as an 'int' on
    every system.
  - 'size_t': the number type of that name, which is not the same
    type built into C++ on every system.

  What to expect
  --------------

  - Every function the header declares for the class is accounted for:
    it is in 'getWritten', or in 'getNotWritten' with the reason.
    Nothing is passed over silently. Functions the compiler makes up
    itself are no part of the header and are not counted.
  - One function the compiler makes up gets a ritual all the same: the
    destructor of a class C++ can copy that declares none, as 'QSize'.
    Python removes its copy of such an object by that ritual.
  - A function is not written when it takes or gives a type that is
    not in the list above, when it is private or protected, when Qt
    forbids it, when it is a signal, or when it is a template.
  - A function giving back 'QString &', the object itself to be changed
    further, is not written: a copy would not be that object.
  - A number that ends as 'long' on this system, under a name that
    says no width, as 'GLintptr', is not written either. 'long' is 64
    bits wide on Linux and macOS and 32 on Windows, and the row would
    be right on one of them only.
  - The ritual file pulls in the header file of every value class its
    rituals copy, since a copy needs the whole class.
  - The getters decide and write nothing. Only 'write' touches a file,
    and it replaces the ritual file and the rows file whole.
  - Whether what was written is right is not checked here. That is the
    job of 'RitualTester'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _splitFunctionType(functionType: str) -> Tuple[str, str, List[str]]:
    """
    Takes apart the type the compiler writes for a function.

    Parameters
    ----------

    functionType : str
      As 'QObject *() const': what it gives, what it takes between
      brackets, and then words such as 'const'.

    Returns
    -------

    Tuple[str, str, List[str]]
      What the function gives, as 'QObject *'; what stands between the
      brackets; and the words after them.

    Raises
    ------

    ValueError
      The text has no pair of brackets holding what the function takes.
    """
    #  The compiler may write 'noexcept(true)' where the header says
    #  'noexcept' with a condition. It is the word 'noexcept' here.
    marker = functionType.rfind(' noexcept(')
    if marker >= 0 and functionType.endswith(')'):
      inside = functionType[marker + len(' noexcept('):-1]
      if inside.count('(') == inside.count(')'):
        functionType = '%s noexcept' % functionType[:marker]
    close = functionType.rfind(')')
    depth, start = 0, -1
    for index in range(close, -1, -1):
      if functionType[index] == ')':
        depth += 1
      elif functionType[index] == '(':
        depth -= 1
        if depth == 0:
          start = index
          break
    if close < 0 or start < 0:
      infoSpec = """Expected the type of a function, as 'int (int)', but
      received '%s'."""
      raise ValueError(' '.join((infoSpec % functionType).split()))
    given = functionType[:start].strip()
    taken = functionType[start + 1:close]
    return given, taken, functionType[close + 1:].split()

  @staticmethod
  def _joinType(cppType: str, name: str) -> str:
    """Writes a type and a name the way C++ does, as 'QObject *parent'."""
    if not name:
      return cppType
    if cppType.endswith(('*', '&')):
      return '%s%s' % (cppType, name)
    return '%s %s' % (cppType, name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The numbers built into C++, as the compiler writes them.
  __number_types__ = (
      'bool', 'char', 'signed char', 'unsigned char', 'short',
      'unsigned short', 'int', 'unsigned int', 'long', 'unsigned long',
      'long long', 'unsigned long long', 'float', 'double',
  )

  #  The names a header writes 'long' itself by. A number that ends as
  #  'long' under any other name is as wide as its system makes it.
  __long_names__ = ('long', 'unsigned long', 'ulong')

  #  The names that end as 'long' on Linux and macOS and as another type
  #  on Windows, each with the word it goes by in a row.
  __size_names__ = {'size_t': 'size_t', 'std::size_t': 'size_t'}

  #  The class of Qt that is text, and the classes of Qt that look at
  #  text held elsewhere. A ritual takes a 'QString' for each of them.
  __text_name__ = 'QString'
  #  The operators that change the object they are called on and give
  #  that very object back, as 'a += b'.
  __in_place_operators__ = (
      'operator+=', 'operator-=', 'operator*=', 'operator/=',
      'operator%=', 'operator&=', 'operator|=', 'operator^=',
      'operator<<=', 'operator>>=',
  )
  __view_names__ = ('QAnyStringView', 'QStringView')

  #  How C++ reads the type of the combinations of a flags enum, as
  #  'QFlags<Qt::WindowType>', with the enum in the brackets. The same
  #  type taken to be read only, as 'const QFlags<Qt::WindowType> &',
  #  crosses the same way.
  __flags_pattern__ = re.compile(
      r'(?:const )?QFlags<([A-Za-z_]\w*(?:::[A-Za-z_]\w*)*)>(?: &)?')

  #  The number types Qt keeps such combinations in a number as wide as
  #  an 'int' for: every number type of an enum that is no wider.
  __flags_enum_types__ = (
      'bool', 'char', 'signed char', 'unsigned char', 'short',
      'unsigned short', 'int', 'unsigned int',
  )

  #  What the compiler calls each kind of function of a class.
  __function_kinds__ = dict(
      CXXConstructorDecl='constructor', CXXDestructorDecl='destructor',
      CXXMethodDecl='method', CXXConversionDecl='method',
  )

  #  A name as C++ writes it inside a type, as 'QMetaObject::Connection'.
  __name_pattern__ = re.compile(r'[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*')

  #  The two functions through which a class says how 'new' and 'delete'
  #  work for it. A class forbidding one of them cannot be made, or
  #  removed, by a ritual.
  __making_functions__ = dict(
      constructor='operator new', destructor='operator delete',
  )

  #  Fallback Variables

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __class_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]
  #  The classes that get a C++ class of ours, through which Python can
  #  take a function over, or None for every class that has such a
  #  function. It is set while the way is tried on a few classes.
  __cute_class_limit__ = None  # type: Optional[Tuple[str, ...]]
  #  The functions C++ looks up in the object that are Qt's own
  #  workings, and are never taken over.
  __qt_own_virtuals__ = ('metaObject', 'qt_metacast', 'qt_metacall')
  __overridable_functions__ = None  # type: Optional[Records]
  #  What '_isHiddenType' found for each type asked about so far, and
  #  the generators '_getOther' made, each kept for the tree they
  #  belong to: both are asked for thousands of times.
  __hidden_types__ = dict()  # type: Dict[Tuple[int, str], bool]
  #  The record of each class read so far. The tree reads a record anew
  #  at every asking, and the work on the functions Python can take
  #  over asks for the same ones over and over.
  __class_records__ = dict()  # type: Dict[Tuple[int, str], Record]
  __has_cute_class__ = None  # type: Optional[bool]
  __other_generators__ = dict()  # type: Dict[Tuple[int, str], Any]
  __written_rituals__ = None  # type: Optional[Rituals]
  __unwritten_functions__ = None  # type: Optional[Reasons]
  __known_names__ = None  # type: Optional[FrozenSet[str]]
  __offered_names__ = None  # type: Optional[FrozenSet[str]]
  __type_tables__ = None  # type: Optional[Record]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getDependencyTree(self) -> DependencyTree:
    """
    Gives the dependency tree the generator works from.

    Provided by you, through 'setDependencyTree'. Nothing fills it in
    for you.

    Raises
    ------

    MissingVariable
      'setDependencyTree' has not been called.
    """
    if self.__dependency_tree__ is None:
      raise MissingVariable(self, '__dependency_tree__', DependencyTree)
    return self.__dependency_tree__

  def getClassName(self) -> str:
    """
    Gives the class the generator writes rituals for, as 'QObject'.

    Provided by you, through 'setClassName'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setClassName' has not been called.
    """
    if self.__class_name__ is None:
      raise MissingVariable(self, '__class_name__', str)
    return self.__class_name__

  def getWorkFolder(self) -> str:
    """
    Gives the folder the ritual file is written to.

    Provided by you, through 'setWorkFolder'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setWorkFolder' has not been called.
    """
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getQtPart(self) -> QtPart:
    """
    Gives the part of Qt the class belongs to.

    Found for you, by the dependency tree.

    Raises
    ------

    LookupError
      The tree has no class of the name you set.
    """
    return self.getDependencyTree().getQtPart(self.getClassName())

  def getFileStem(self) -> str:
    """
    Gives the name of the ritual file without its ending: the name of
    the class in small letters, with an underscore before each word.

    Found for you. 'QObject' gives 'q_object', and
    'QMetaObject::Connection' gives 'q_meta_object__connection'.
    """
    stem = []
    for letter in self.getClassName().replace('::', '__'):
      if letter.isupper() and stem and stem[-1] != '_':
        stem.append('_')
      stem.append(letter.lower())
    return ''.join(stem)

  def getRitualFile(self) -> str:
    """
    Gives the full path of the ritual file, as
    '/some/folder/q_object.cpp'.

    Found for you, from the work folder and the name of the class.
    Having the path does not mean the file is there; 'write' makes it.
    """
    name = '%s.cpp' % self.getFileStem()
    return os.path.join(self.getWorkFolder(), name)

  def getRowsFile(self) -> str:
    """
    Gives the full path of the rows file, as
    '/some/folder/q_object.json': the ritual file with another ending.

    Found for you, from the work folder and the name of the class.
    Having the path does not mean the file is there; 'write' makes it.
    """
    name = '%s.json' % self.getFileStem()
    return os.path.join(self.getWorkFolder(), name)

  def _createPlan(self, ) -> None:
    """Decides, for each function of the class, whether it is written."""
    tree = self.getDependencyTree()
    className = self.getClassName()
    record = tree.getClassRecord(className)
    summary = self.getQtPart().getClassSummary(className)
    signals = {signal['name'] for signal in summary.get('signals', ())}
    abstract = record.get('definitionData', dict()).get('isAbstract', False)
    barred = self._findBarred(record)
    written, unwritten = [], []  # type: List[Record], List[Tuple[str, str]]
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    for member in record.get('inner', ()):
      kind = member.get('kind')
      if kind == 'AccessSpecDecl':
        access = member['access']
        continue
      if member.get('isImplicit'):
        continue
      if kind == 'FunctionTemplateDecl':
        infoSpec = """a template: a pattern and no single function"""
        unwritten.append((self._showTemplate(member), infoSpec))
        continue
      if kind == 'FriendDecl':
        #  A function Qt writes inside the class with 'friend' in front
        #  belongs to no object: it takes everything it works on as
        #  arguments. Qt writes most operators that way, as
        #  'operator+(const QPoint &p1, const QPoint &p2)', and those
        #  are taken. The other friends are helpers of Qt's own.
        for friend in member.get('inner', ()):
          if not isinstance(friend, dict) or friend.get('isImplicit'):
            continue
          if friend.get('kind') != 'FunctionDecl':
            continue
          if not friend.get('name', '').startswith('operator'):
            continue
          plan = self._planFunction(friend, friend=True)
          reason = self._findReason(plan, friend, 'public', (), False, ())
          owner = self._findFriendOwner(friend, plan)
          if not reason and owner != className:
            #  Two classes may each declare one and the same operator, as
            #  'QVector4D * QMatrix4x4'. It is one function of C++, so it
            #  gets one ritual, with the class that stands first in it.
            infoSpec = """written with the class '%s', which declares it
            as well and stands first in it"""
            reason = ' '.join((infoSpec % owner).split())
          if reason:
            unwritten.append((plan['function'], reason))
          else:
            written.append(plan)
        continue
      if kind not in self.__function_kinds__:
        continue
      plan = self._planFunction(member)
      reason = self._findReason(
          plan, member, access, signals, abstract, barred,
      )
      if reason:
        unwritten.append((plan['function'], reason))
      else:
        written.append(plan)
    if className in self._getTypeTables()['copyable']:
      declared = [m.get('kind') for m in record.get('inner', ())
                  if not m.get('isImplicit')]
      if 'CXXDestructorDecl' not in declared:
        written.append(self._planOwnDestructor())
    #  A class built on more than one class gets, for each class after
    #  the first, the ritual that gives where that part of an object is.
    for baseName in self.getFurtherBases():
      written.append(self._planCast(baseName))
    #  A class with a C++ class of ours gets the ritual that hands a
    #  Python function over, and one for each function of its own that
    #  runs just that function.
    if self.hasCuteClass():
      written.append(self._planTake())
    limit = self.__cute_class_limit__
    if limit is None or className in limit:
      written.extend(self._planOwn())
    self.__written_rituals__ = (*written,)
    self.__unwritten_functions__ = (*unwritten,)

  def getCuteClassName(self) -> str:
    """Gives the name of the C++ class of ours that is built on the
    class of Qt, as 'CuteQWidget'. Python never sees it."""
    return 'Cute%s' % self.getClassName().replace('::', '_')

  def _getOther(self, className: str) -> RitualGenerator:
    """Gives a generator for another class of the same tree."""
    if className == self.getClassName():
      return self
    key = (id(self.getDependencyTree()), className)
    try:
      return self.__other_generators__[key]
    except KeyError:
      other = type(self)()
      other.setDependencyTree(self.getDependencyTree())
      other.setClassName(className)
      #  It only works out plans and never writes a file, so it needs
      #  no folder.
      self.__other_generators__[key] = other
      return other

  def _readRecord(self, className: str) -> Record:
    """Gives the record of a class as the tree has it, read once."""
    tree = self.getDependencyTree()
    key = (id(tree), className)
    try:
      return self.__class_records__[key]
    except KeyError:
      record = tree.getClassRecord(className)
      self.__class_records__[key] = record
      return record

  def _findVirtuals(self) -> List[Record]:
    """
    Gives every function of the class that C++ looks up in the object
    when it is called, its own and those of the classes it is built
    on. Qt calls such a function itself, and a class built on this one
    can put a function of its own in its place.

    Returns
    -------

    List[Record]
      For each 'name'; 'nearest': where the function Qt runs for an
      object of this class is declared, as 'owner', 'member', 'access',
      'final' and 'pure'; and 'root': the same for the class that first
      declared it.
    """
    tree, className = self.getDependencyTree(), self.getClassName()
    chain = (className, *reversed(tree.getAncestors(className)))
    groups = dict()  # type: Dict[Tuple[str, str], List[Record]]
    for owner in chain:
      record = self._readRecord(owner)
      access = 'private' if record.get('tagUsed') == 'class' else 'public'
      for member in record.get('inner', ()):
        kind = member.get('kind')
        if kind == 'AccessSpecDecl':
          access = member['access']
          continue
        if kind != 'CXXMethodDecl' or member.get('isImplicit'):
          continue
        if member.get('storageClass') == 'static':
          continue
        marks = [
            child.get('kind') for child in member.get('inner', ())
            if isinstance(child, dict)
        ]
        looked = True if member.get('virtual') else False
        if 'OverrideAttr' in marks or 'FinalAttr' in marks:
          looked = True
        #  One function is known by its name, what it takes and whether
        #  it leaves the object as it is. What it gives is left out: a
        #  class may declare it anew giving a class built on what the
        #  first one gave.
        _, taken, words = self._splitFunctionType(member['type']['qualType'])
        shape = '%s|%s' % (taken, 'const' if 'const' in words else '')
        groups.setdefault((member['name'], shape), []).append(dict(
            owner=owner, member=member, access=access, virtual=looked,
            final='FinalAttr' in marks,
            pure=True if member.get('pure') else False,
        ))
    virtuals = []  # type: List[Record]
    for name, declared in self._joinSpelledApart(chain, groups):
      if any(entry['virtual'] for entry in declared):
        virtuals.append(
            dict(name=name, nearest=declared[0], root=declared[-1]))
    return virtuals

  def _joinSpelledApart(self, chain: Any, groups: Any) -> List[Any]:
    """
    Joins the declarations of one function that two classes spell
    apart. A class may shorten the name of a type a class it is built
    on declares: 'QIODevice::open(QIODeviceBase::OpenMode)' is
    'QBuffer::open(OpenMode)' in QBuffer, and both are one function.

    Parameters
    ----------

    chain : Any
      The class and the classes it is built on, the nearest first.

    groups : Any
      The declarations gathered by name and by what the function takes
      as its class spells it, each list the nearest first.

    Returns
    -------

    List[Any]
      For each function its name and its declarations, the nearest
      first. Only a name with more than one group is spelled out in
      full, which is where two spellings of one function can be.
    """
    counts = collections.Counter(name for name, _ in groups)
    joined = collections.OrderedDict()  # type: Dict[Any, List[Record]]
    for (name, shape), declared in groups.items():
      if counts[name] < 2:
        joined[name, shape] = declared
        continue
      for entry in declared:
        other = self._getOther(entry['owner'])
        spelled = [
            other._spellOutside(child['type']['qualType'])
            for child in entry['member'].get('inner', ())
            if isinstance(child, dict) and child.get('kind') == 'ParmVarDecl'
        ]
        full = '%s|%s' % (', '.join(spelled), shape.rpartition('|')[2])
        joined.setdefault((name, full), []).append(entry)
    out = []  # type: List[Any]
    for (name, _), declared in joined.items():
      declared.sort(key=lambda entry: chain.index(entry['owner']))
      out.append((name, declared))
    return out

  def _planCallback(self, plan: Record) -> Optional[Record]:
    """
    Says how a function Qt calls is handed on to Python: what C++ hands
    the Python function and what it takes back.

    Returns
    -------

    Optional[Record]
      None when something of it cannot be handed over yet. Else
      'cTakes': the C++ types handed over after the object; 'cPassed':
      what is handed over; 'takes': for Python, the word of each
      ('address', 'int', ...) with what it is ('address' of a class,
      'value' of a class, 'number', 'enum' of an enum, 'flags' of an
      enum, 'text'); 'cGives', 'gives' and 'given': the same for what
      comes back.
    """
    cTakes, cPassed, takes = [], [], []
    for argument in plan['arguments']:
      passing, written = argument['passing'], argument['written']
      name, kind = argument['name'], passing['kind']
      if kind == 'address':
        pointed = written.replace('const ', '').replace('*', '').strip()
        cTakes.append(written)
        cPassed.append(name)
        takes.append(('address', 'address', pointed))
      elif kind == 'value':
        cTakes.append('const %s *' % passing['className'])
        cPassed.append('&%s' % name)
        takes.append(('address', 'value', passing['className']))
      elif kind == 'number':
        cTakes.append(self._stripReadOnly(written))
        cPassed.append(name)
        takes.append((passing['word'], 'number', ''))
      elif kind == 'enum':
        cTakes.append('int')
        cPassed.append('static_cast<int>(%s)' % name)
        takes.append(('int', 'enum', written))
      elif kind == 'flags' and passing['word']:
        #  The number of the combination is handed over, and Python
        #  makes the combination of it again.
        enumName = passing['className'][len('QFlags<'):-1]
        cTakes.append('int')
        cPassed.append('static_cast<int>(%s.toInt())' % name)
        takes.append(('int', 'flags', enumName))
      elif kind == 'text':
        #  The address of Qt's own text is handed over, and Python reads
        #  the letters off it.
        cTakes.append('const %s *' % passing['className'])
        cPassed.append('&%s' % name)
        takes.append(('address', 'text', ''))
      else:
        return None
    giving = plan['giving']
    kind, written = giving['kind'], giving['written']
    if kind == 'nothing':
      cGives, gives, given = 'void', ('nothing', 'nothing', ''), ''
    elif kind == 'number':
      cGives = self._stripReadOnly(written)
      gives, given = (giving['word'], 'number', ''), 'given'
    elif kind == 'enum':
      cGives, gives = 'int', ('int', 'enum', written)
      given = 'static_cast<%s>(given)' % written
    elif kind == 'flags' and giving['word']:
      enumName = giving['className'][len('QFlags<'):-1]
      cGives, gives = 'int', ('int', 'flags', enumName)
      given = '%s::fromInt(given)' % giving['className']
    elif kind == 'text' and '&' not in written:
      #  Python makes a text of Qt for what it gives, and the C++ class
      #  of ours copies it and removes it; see '_writeOverride'. A
      #  function that gives the text it keeps, as 'const QString &',
      #  cannot give one made for the call.
      cGives = '%s *' % giving['className']
      gives, given = ('address', 'text', ''), '*given'
    elif kind == 'value':
      cGives = 'const %s *' % giving['className']
      gives, given = ('address', 'value', giving['className']), '*given'
    elif kind == 'address':
      pointed = written.replace('const ', '').replace('*', '').strip()
      cGives, gives = 'void *', ('address', 'address', pointed)
      given = 'static_cast<%s>(given)' % written
    else:
      return None
    return dict(
        cTakes=(*cTakes,), cPassed=(*cPassed,), takes=(*takes,),
        cGives=cGives, gives=gives, given=given,
    )

  def getOverridable(self) -> Records:
    """
    Gives the functions of the class that Python can take over: those
    C++ looks up in the object, the class's own and inherited, that a
    class built on this one may replace and whose arguments can be
    handed to Python.

    Decided for you. Each is the plan of the function as the nearest
    class declares it, with 'key': the compiler's name of the function
    where it was first declared, by which Python names it to C++;
    'owner': the class whose function Qt runs when Python takes nothing
    over; 'rootOwner': the class that first declared it; 'access';
    'pure': whether Qt has no function of its own for it; and what
    '_planCallback' gives.
    """
    if self.__overridable_functions__ is not None:
      return self.__overridable_functions__
    found = []  # type: List[Record]
    for virtual in self._findVirtuals():
      nearest, root = virtual['nearest'], virtual['root']
      name = virtual['name']
      if name in self.__qt_own_virtuals__ or name.startswith('operator'):
        continue
      if nearest['access'] == 'private' or nearest['final']:
        continue
      if 'mangledName' not in root['member']:
        continue
      if nearest['member'].get('explicitlyDeleted'):
        #  Qt forbids the function in the nearest class.
        continue
      other = self._getOther(nearest['owner'])
      plan = other._planFunction(nearest['member'])
      if plan['unknownTypes'] or plan['unsureNumbers'] or plan['variadic']:
        continue
      if '&&' in plan['words'] or '&' in plan['words']:
        continue
      shape = self._planCallback(plan)
      if shape is None:
        continue
      named = [a['written'] for a in plan['arguments']]
      named.append(plan['giving']['written'])
      if any(self._isHiddenType(typeName) for typeName in named):
        #  A type Qt keeps for classes built on its class cannot be
        #  named by a ritual, which stands outside every class.
        continue
      found.append(dict(
          plan, key=root['member']['mangledName'], owner=nearest['owner'],
          rootOwner=root['owner'], access=nearest['access'],
          pure=nearest['pure'], **shape))
    self.__overridable_functions__ = (*found,)
    return self.__overridable_functions__

  def getDeclaredVirtuals(self) -> Records:
    """
    Gives every function Qt calls itself that the class is the first
    to declare and that a class built on it may put its own in the
    place of, whether or not Python can take it over.

    Decided for you. The class generator needs it to name, in the
    class file, the functions that cannot be handed to Python yet: a
    class of a program that writes one of those anew is refused, where
    Qt would otherwise never call what it wrote.

    Returns
    -------

    Records
      For each function its 'name', and 'written': the function as Qt
      declares it, as 'void QWidget::paintEvent(QPaintEvent *)'.
    """
    found = []  # type: List[Record]
    className = self.getClassName()
    for virtual in self._findVirtuals():
      nearest, root = virtual['nearest'], virtual['root']
      name = virtual['name']
      if root['owner'] != className:
        continue
      if name in self.__qt_own_virtuals__ or name.startswith('operator'):
        continue
      if nearest['access'] == 'private' or nearest['final']:
        continue
      functionType = root['member']['type']['qualType']
      gives, taken, words = self._splitFunctionType(functionType)
      space = '' if gives.endswith(('*', '&')) else ' '
      written = '%s%s%s::%s(%s)' % (gives, space, className, name, taken)
      found.append(dict(name=name, written=' '.join([written, *words])))
    return (*found,)

  def _isHiddenType(self, typeName: str) -> bool:
    """Says whether a type is one Qt writes inside a class and keeps
    for that class and the classes built on it, as the enum
    'QAbstractSlider::SliderChange'."""
    plain = typeName.replace('const ', '').replace('&', '')
    plain = plain.replace('*', '').strip()
    owner, _, own = plain.rpartition('::')
    if not owner:
      return False
    key = (id(self.getDependencyTree()), plain)
    try:
      return self.__hidden_types__[key]
    except KeyError:
      hidden = self._findHiddenType(owner, own)
      self.__hidden_types__[key] = hidden
      return hidden

  def _findHiddenType(self, owner: str, own: str) -> bool:
    """Does the looking for '_isHiddenType', which keeps the answer."""
    try:
      record = self._readRecord(owner)
    except (ValueError, LookupError):
      #  Written in a namespace, as 'Qt::FocusPolicy', or in no class
      #  the tree knows: nothing keeps it from being named.
      return False
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    for member in record.get('inner', ()):
      if member.get('kind') == 'AccessSpecDecl':
        access = member['access']
      elif member.get('name') == own and 'Decl' in member.get('kind', ''):
        return access != 'public'
    return False

  def hasCuteClass(self) -> bool:
    """
    Says whether the class gets a C++ class of ours built on it. Every
    object Python makes of the class is then of that C++ class, in
    which each function of 'getOverridable' asks Python first, when
    Python has handed a function over for it.
    """
    if self.__has_cute_class__ is None:
      self.__has_cute_class__ = self._findCuteClass()
    return self.__has_cute_class__

  def _findCuteClass(self) -> bool:
    """Does the looking for 'hasCuteClass', which keeps the answer."""
    limit = self.__cute_class_limit__
    if limit is not None and self.getClassName() not in limit:
      return False
    record = self._readRecord(self.getClassName())
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    for child in record.get('inner', ()):
      if not isinstance(child, dict):
        continue
      kind = child.get('kind')
      if kind == 'AccessSpecDecl':
        access = child['access']
      elif kind == 'FinalAttr':
        #  Qt forbids building a class on this one.
        return False
      elif kind == 'CXXDestructorDecl' and access == 'private':
        #  Only Qt may remove one, so no class can be built on it.
        return False
    return True if self.getOverridable() else False

  def _writeCuteClass(self) -> str:
    """
    Gives the C++ text of the class of ours built on the class of Qt.

    It holds, for each function of 'getOverridable', a place for the
    Python function handed over and the function Qt calls: that one
    asks the Python function when there is one, and runs Qt's own when
    there is none or when Python says it did not take the call.
    """
    className, cuteName = self.getClassName(), self.getCuteClassName()
    functions = self.getOverridable()
    lines = [
        '//  A %s that Python can take functions over in. Every %s' % (
            className, className),
        '//  Python makes is one. Each function below asks the Python',
        '//  function handed over for it, and runs Qt\'s own without one.',
    ]
    for index, function in enumerate(functions):
      handed = ['const void *', *function['cTakes'], 'int *']
      lines.append('typedef %s (*%sCall%d)(%s);' % (
          function['cGives'], cuteName, index, ', '.join(handed)))
    lines.append('class %s : public %s {' % (cuteName, className))
    lines.append('public:')
    lines.append('  using %s::%s;' % (className, className.split('::')[-1]))
    if className in self._getTypeTables()['copyable']:
      #  A copy of an object of Qt is an object of ours as well.
      lines.append('  %s(const %s &other) : %s(other) {}' % (
          cuteName, className, className))
    lines.append('  void *taken[%d] = {};' % len(functions))
    lines.append('')
    lines.append('  bool take(const char *key, void *call) {')
    for index, function in enumerate(functions):
      lines.append('    if (!std::strcmp(key, "%s")) {' % function['key'])
      lines.append('      taken[%d] = call;' % index)
      lines.append('      return true;')
      lines.append('    }')
    lines.append('    return false;')
    lines.append('  }')
    for index, function in enumerate(functions):
      lines.append('')
      lines.extend(self._writeOverride(index, function))
    lines.append('};')
    return '\n'.join(lines)

  def _writeOverride(self, index: int, function: Record) -> List[str]:
    """Gives the lines of one function of the C++ class of ours."""
    cuteName, name = self.getCuteClassName(), function['name']
    giving, words = function['giving'], function['words']
    arguments = function['arguments']
    shown = ', '.join(
        self._joinType(a['written'], a['name']) for a in arguments)
    tail = ''.join(' %s' % w for w in ('const', 'noexcept') if w in words)
    head = self._joinType(giving['written'], '%s(%s)' % (name, shown))
    lines = textwrap.wrap(
        function['function'], 75, initial_indent='  //  ',
        subsequent_indent='  //      ')
    whole = '  %s%s override {' % (head, tail)
    if len(whole) <= 77:
      lines.append(whole)
    else:
      lines.append('  %s' % self._joinType(giving['written'], '%s(' % name))
      for place, argument in enumerate(arguments):
        end = ')%s override {' % tail if place == len(arguments) - 1 else ','
        lines.append('      %s%s' % (
            self._joinType(argument['written'], argument['name']), end))
    callName = '%sCall%d' % (cuteName, index)
    passed = ', '.join(['this', *function['cPassed'], '&handled'])
    nothing = function['cGives'] == 'void'
    lines.append('    if (taken[%d]) {' % index)
    lines.append('      int handled = 0;')
    lines.append('      %s call = reinterpret_cast<%s>(taken[%d]);' % (
        callName, callName, index))
    if nothing:
      lines.append('      call(%s);' % passed)
      lines.append('      if (handled) return;')
    else:
      lines.append(
          '      %s given = call(%s);' % (function['cGives'], passed))
      test = 'handled'
      if function['given'] == '*given':
        test = 'handled && given'
      if function['gives'][1] == 'text':
        #  The text was made for this call alone, so it is removed here.
        lines.append('      if (%s) {' % test)
        lines.append('        %s back(*given);' % giving['className'])
        lines.append('        delete given;')
        lines.append('        return back;')
        lines.append('      }')
      else:
        lines.append('      if (%s) return %s;' % (test, function['given']))
    lines.append('    }')
    names = ', '.join(a['name'] for a in arguments)
    if not function['pure']:
      own = '%s::%s(%s);' % (function['owner'], name, names)
      lines.append('    %s%s' % ('' if nothing else 'return ', own))
    elif not nothing:
      #  Qt has no function of its own here. Without an answer from
      #  Python, what the type is made of from nothing goes back.
      lines.append('    return {};')
    lines.append('  }')
    return lines

  def _planTake(self) -> Record:
    """Works out the ritual that hands a Python function over to an
    object of the C++ class of ours, for one of its functions."""
    className, cuteName = self.getClassName(), self.getCuteClassName()
    plan = dict(
        ritualName='ritual_take_%s' % className.replace('::', '_'),
        function='a Python function taken by a %s, for the function '
                 'named by the key' % cuteName,
        kind='take', gives='bool',
        takes=(('self', '%s *' % className), ('key', 'const char *'),
               ('call', 'void *')),
        row=('bool', 'address', 'chars', 'address'), needs=(),
        unknownTypes=(), unsureNumbers=(), words=(), variadic=False,
        name='', arguments=(), giving=None, inPlace=False,
    )
    body = ['  return static_cast<%s *>(self)->take(key, call);' % cuteName]
    plan['text'] = self._writeRitual(plan, body)
    return plan

  def _planOwn(self) -> List[Record]:
    """
    Works out, for each function of 'getOverridable' the class declares
    itself, the ritual that runs just that function of Qt and no other:
    'self->QWidget::sizeHint()'. The cute function calls it for an
    object of ours, where the ordinary call would come back to Python.
    """
    className = self.getClassName()
    plans = []  # type: List[Record]
    #  The names the class also has a function of that only Qt itself
    #  may call. A function of such a name that a class built on this
    #  one may call cannot be reached apart from the other one.
    record = self._readRecord(className)
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    closed = set()  # type: Set[str]
    for member in record.get('inner', ()):
      if member.get('kind') == 'AccessSpecDecl':
        access = member['access']
      elif member.get('kind') == 'CXXMethodDecl' and access == 'private':
        closed.add(member.get('name'))
    for function in self.getOverridable():
      if function['owner'] != className or function['pure']:
        continue
      if function['access'] == 'protected' and function['name'] in closed:
        continue
      for member in self._findOwnMembers(function['name']):
        if member.get('mangledName') != function['ritualName'][6:]:
          continue
        hidden = function['access'] == 'protected'
        plan = self._planFunction(member, own=True, hidden=hidden)
        plan['kind'], plan['key'] = 'own', function['key']
        plan['access'] = function['access']
        plans.append(plan)
    return plans

  def _findOwnMembers(self, name: str) -> List[Record]:
    """Gives the functions of a name the class declares itself."""
    record = self._readRecord(self.getClassName())
    return [
        member for member in record.get('inner', ())
        if member.get('kind') == 'CXXMethodDecl'
        and member.get('name') == name
    ]

  def _writeOwnClass(self, plans: List[Record]) -> str:
    """Gives the C++ text of the class through which a ritual reaches
    the functions of Qt that only a class built on it may call."""
    className = self.getClassName()
    ownName = 'Own%s' % className.replace('::', '_')
    names = []  # type: List[str]
    for plan in plans:
      if plan['access'] == 'protected' and plan['name'] not in names:
        names.append(plan['name'])
    if not names:
      return ''
    lines = [
        '//  Only a class built on %s may call these functions of it.' % (
            className,),
        '//  This one is, and makes them free for the rituals to call.',
        'struct %s : %s {' % (ownName, className),
    ]
    lines.extend('  using %s::%s;' % (className, name) for name in names)
    lines.append('};')
    return '\n'.join(lines)

  def _findFriendOwner(self, friend: Record, plan: Record) -> str:
    """
    Gives the class an operator written with 'friend' gets its ritual
    with: of the classes that declare it in their body, the one that
    stands first among its arguments. For an operator no other class
    declares, that is this class.
    """
    className, tree = self.getClassName(), self.getDependencyTree()
    compilerName = friend.get('mangledName', None)
    if compilerName is None:
      return className
    for argument in plan['arguments']:
      otherName = argument['passing'].get('className', None)
      if argument['passing'].get('kind') != 'value' or otherName is None:
        continue
      if otherName == className:
        return className
      try:
        record = self._readRecord(otherName)
      except (ValueError, LookupError):
        continue
      for member in record.get('inner', ()):
        if member.get('kind') != 'FriendDecl':
          continue
        for declared in member.get('inner', ()):
          if not isinstance(declared, dict):
            continue
          if declared.get('mangledName', None) == compilerName:
            return otherName
    return className

  def getWritten(self, **kwargs) -> Rituals:
    """
    Gives the rituals of the class: one for each function the generator
    writes, in the order the header declares the functions.

    Decided for you, at the first call, from the record of the class,
    and kept. Nothing is written to a file by this. You pass nothing;
    the keyword is for the method's own use.

    Returns
    -------

    Rituals
      A 'Tuple[Dict[str, Any], ...]'. Each ritual says:
      'ritualName': its name, as 'ritual_ZNK7QObject6parentEv'.
      'function': the Qt function it calls, as C++ writes it.
      'kind': 'constructor', 'destructor', 'method', 'static method',
      'friend' for an operator Qt writes with 'friend' in the class, or
      'cast' for a ritual of 'getFurtherBases'.
      'gives': the type the ritual gives back, as C++ writes it.
      'takes': what the ritual takes, in order, each as a name and a
      type. For a ritual on an object the first is 'self', the address
      of the object.
      'row': the row of the ritual: the word for what it gives, then
      one word for each thing it takes.
      'needs': the value classes the ritual copies.
      'text': the C++ text of the ritual.
      'name': the name of the Qt function, as 'parent'.
      'arguments': what the Qt function takes, in order, each saying
      its 'name', its type as 'written' in the header with every name
      in full, how it is passed ('passing', as '_findPassing' gives
      it), and 'default': what the compiler wrote down for the value
      Qt fills in when the argument is left out, or None.
      'giving': how what the Qt function gives is passed, with the
      type as 'written'. It is None for a constructor and a destructor.

    Raises
    ------

    MissingVariable
      'setDependencyTree' or 'setClassName' has not been called.

    LookupError
      The tree has no class of that name.
    """
    if self.__written_rituals__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      self._createPlan()
      return self.getWritten(_recursion=True)
    return self.__written_rituals__

  def getNotWritten(self) -> Reasons:
    """
    Gives the functions of the class that get no ritual, each with the
    reason, in the order the header declares them.

    Decided for you, together with 'getWritten'.

    Returns
    -------

    Reasons
      A 'Tuple[Tuple[str, str], ...]': the function as C++ writes it,
      and the reason in words.
    """
    self.getWritten()
    return self.__unwritten_functions__

  def getRitualNames(self) -> Tuple[str, ...]:
    """Gives the name of every ritual of the class, in order."""
    return (*(ritual['ritualName'] for ritual in self.getWritten()),)

  def _getHeading(self) -> str:
    """Says who wrote a file, from what, and that it is written anew."""
    qtPart = self.getQtPart()
    headerPath = self.getDependencyTree().getHeaderPath(self.getClassName())
    relative = os.path.relpath(headerPath, qtPart.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.RitualGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, qtPart.getQtVersion())
    return ' '.join(info.split())

  def getRitualText(self) -> str:
    """
    Gives the whole text of the ritual file, without writing it.

    Written for you from 'getWritten': a heading, the lines pulling in
    the header file of the class, as 'QtPart.getIncludeLines' gives
    them, the same for each value class a ritual copies, and then each
    ritual under the Qt function it calls.
    """
    tree = self.getDependencyTree()
    className = self.getClassName()
    heading = textwrap.wrap(self._getHeading(), 73)
    blocks = ['\n'.join('//  %s' % line for line in heading)]
    needed = [className]
    for ritual in self.getWritten():
      needed.extend(n for n in ritual['needs'] if n not in needed)
    if self.hasCuteClass():
      #  The C++ class of ours holds the functions of the classes this
      #  one is built on as well, and a value one of them takes or
      #  gives has to be known in full here.
      for function in self.getOverridable():
        needed.extend(n for n in function['needs'] if n not in needed)
    includeLines = []  # type: List[str]
    for name in needed:
      lines = tree.getQtPart(name).getIncludeLines(tree.getHeaderPath(name))
      for line in lines.split('\n'):
        if line.strip() and line not in includeLines:
          includeLines.append(line)
    owned = [r for r in self.getWritten() if r['kind'] == 'own']
    if self.hasCuteClass():
      includeLines.append('#include <cstring>')
    blocks[0] = '%s\n%s' % (blocks[0], '\n'.join(includeLines))
    ownClass = self._writeOwnClass(owned)
    if ownClass:
      blocks.append(ownClass)
    if self.hasCuteClass():
      blocks.append(self._writeCuteClass())
    blocks.extend(ritual['text'] for ritual in self.getWritten())
    return '%s\n' % '\n\n'.join(blocks)

  def getRows(self) -> Rows:
    """
    Gives the row of every ritual of the class, under the name of the
    ritual, in the order of 'getWritten'.

    Decided for you, together with 'getWritten'.

    Returns
    -------

    Rows
      A 'Dict[str, Tuple[str, ...]]'. For
      'ritual_ZN7QObject12blockSignalsEb' it holds
      ('bool', 'address', 'bool'): a 'bool' comes back, and the address
      of the object and a 'bool' go in.
    """
    return {
        ritual['ritualName']: ritual['row'] for ritual in self.getWritten()
    }

  def getRowsText(self) -> str:
    """
    Gives the whole text of the rows file, without writing it.

    Written for you from 'getRows', as JSON: under 'about' the heading
    of the ritual file, and under 'rows' each ritual with its row.
    """
    about = textwrap.wrap(self._getHeading(), 66)
    lines = ['{', '  "about": [']
    lines.extend(
        '    %s%s' % (json.dumps(line), ',' if line is not about[-1] else '')
        for line in about
    )
    lines.extend(('  ],', '  "rows": {'))
    rows = [*self.getRows().items()]
    for index, (ritualName, row) in enumerate(rows):
      end = '' if index == len(rows) - 1 else ','
      words = ', '.join(json.dumps(word) for word in row)
      whole = '    %s: [%s]%s' % (json.dumps(ritualName), words, end)
      if len(whole) <= 77:
        lines.append(whole)
        continue
      lines.append('    %s: [' % json.dumps(ritualName))
      #  The words are put on lines one by one. A word may hold a space,
      #  as 'unsigned int', and must not be broken there.
      packed = '     '
      for position, word in enumerate(row):
        piece = json.dumps(word)
        if position < len(row) - 1:
          piece = '%s,' % piece
        if len(packed) + 1 + len(piece) > 77 and packed.strip():
          lines.append(packed)
          packed = '     '
        packed = '%s %s' % (packed, piece)
      lines.append(packed)
      lines.append('    ]%s' % end)
    lines.extend(('  }', '}'))
    return '%s\n' % '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setDependencyTree(self, dependencyTree: DependencyTree) -> None:
    """
    Tells the generator which dependency tree to work from.

    Required. Calling it again forgets what was decided before.

    Parameters
    ----------

    dependencyTree : DependencyTree
      A tree with its parts set. One tree serves every generator.

    Raises
    ------

    TypeException
      'dependencyTree' is not a 'DependencyTree'.
    """
    if not isinstance(dependencyTree, DependencyTree):
      raise TypeException('dependencyTree', dependencyTree, DependencyTree)
    self.__dependency_tree__ = dependencyTree
    self.__written_rituals__ = None
    self.__unwritten_functions__ = None
    self.__overridable_functions__ = None
    self.__has_cute_class__ = None
    self.__known_names__ = None
    self.__offered_names__ = None
    self.__type_tables__ = None

  def setClassName(self, className: str) -> None:
    """
    Tells the generator which class to write rituals for.

    Required. Calling it again forgets what was decided before.

    Parameters
    ----------

    className : str
      The class by the name the dependency tree has it under, as
      'QObject' or 'QMetaObject::Connection'.

    Raises
    ------

    TypeException
      'className' is not text.
    """
    if not isinstance(className, str):
      raise TypeException('className', className, str)
    self.__class_name__ = className
    self.__written_rituals__ = None
    self.__unwritten_functions__ = None
    self.__overridable_functions__ = None
    self.__has_cute_class__ = None

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Tells the generator where to write the ritual file.

    Required before 'write' and 'getRitualFile'. Calling it again
    replaces the folder given before.

    Parameters
    ----------

    workFolder : str
      The path of a folder that exists. A path may be relative to where
      Python was started; it is kept in full.

    Raises
    ------

    TypeException
      'workFolder' is not text.

    FileNotFoundError
      There is no folder at the path.
    """
    if not isinstance(workFolder, str):
      raise TypeException('workFolder', workFolder, str)
    workFolder = os.path.abspath(workFolder)
    if not os.path.isdir(workFolder):
      infoSpec = """There is no folder at '%s'."""
      raise FileNotFoundError(infoSpec % workFolder)
    self.__work_folder__ = workFolder

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says which class this is for and which setters are still due."""
    clsName = type(self).__name__
    unset = [
        setter for setter, value in (
            ('setDependencyTree', self.__dependency_tree__),
            ('setClassName', self.__class_name__),
        ) if value is None
    ]
    if unset:
      infoSpec = """<%s still waiting for: %s>"""
      return infoSpec % (clsName, ', '.join(unset))
    return "<%s of the class '%s'>" % (clsName, self.__class_name__)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _getTypeTables(self, **kwargs) -> Record:
    """
    Gives what the dependency tree knows of types, each asked of it
    once: 'aliases', every second name for a type; 'enums' and
    'classes', the names of those; 'enumTypes', the number type an enum
    is kept as; 'copyable', the classes C++ can copy. Kept after the
    first call.
    """
    if self.__type_tables__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      tree = self.getDependencyTree()
      self.__type_tables__ = dict(
          aliases=tree.getAliasTypes(),
          enums=frozenset(tree.getEnumNames()),
          classes=frozenset(tree.getClassNames()),
          enumTypes=tree.getEnumTypes(),
          copyable=tree.getCopyableNames(),
      )
      return self._getTypeTables(_recursion=True)
    return self.__type_tables__

  def _followAliases(self, cppType: str) -> str:
    """Gives the type a name stands for, through every second name."""
    aliases = self._getTypeTables()['aliases']
    seen = set()  # type: Set[str]
    while cppType in aliases and cppType not in seen:
      seen.add(cppType)
      cppType = aliases[cppType]
    return cppType

  def _findNumberWord(self, written: str, plain: str) -> str:
    """
    Gives the word a number goes by in a row, or '' when no word is
    right on every system.

    Parameters
    ----------

    written : str
      The type as the header writes it, as 'qsizetype' or 'size_t'.

    plain : str
      The number type built into C++ that it ends as on this system, as
      'long long' or 'unsigned long'.

    Returns
    -------

    str
      'plain' for every type but 'long' and 'unsigned long'. Those two
      are 64 bits wide on Linux and macOS and 32 on Windows, so they
      are given only when the header writes 'long' itself. A name known
      to follow the system, as 'size_t', gives its own word. Any other
      name gives ''.
    """
    if plain not in ('long', 'unsigned long'):
      return plain
    if written.startswith('const '):
      written = written[6:]
    if written in self.__long_names__:
      return plain
    return self.__size_names__.get(written, '')

  def _findValueName(self, cppType: str) -> str:
    """
    Gives the class a type hands around as a value: 'QSize' for
    'QSize', 'const QSize' and 'const QSize &'. Gives '' for any other
    type, as 'QSize &' and 'QSize *', and for a class C++ cannot copy.
    """
    if cppType.endswith(' &'):
      if not cppType.startswith('const '):
        return ''
      cppType = cppType[:-2]
    if cppType.startswith('const '):
      cppType = cppType[6:]
    cppType = self._followAliases(cppType)
    if cppType in self._getTypeTables()['copyable']:
      return cppType
    return ''

  @staticmethod
  def _stripReadOnly(cppType: str) -> str:
    """Gives 'int' for 'int', 'const int' and 'const int &'."""
    if cppType.startswith('const '):
      cppType = cppType[6:]
      if cppType.endswith(' &'):
        cppType = cppType[:-2]
    return cppType

  def _findReadOnlyNumber(self, plain: str) -> str:
    """
    Gives the number type built into C++ that a type hands around as a
    copy: 'int' for 'int', 'const int' and 'const int &'. Gives '' for
    any other type, as 'int &', which the function may change.
    """
    number = self._followAliases(self._stripReadOnly(plain))
    if number in self.__number_types__:
      return number
    return ''

  def _findFlagsEnum(self, plain: str) -> str:
    """
    Gives the flags enum whose combinations a type holds:
    'Qt::WindowType' for 'QFlags<Qt::WindowType>', also when the type
    is taken to be read only, as 'const QFlags<Qt::WindowType> &'. Gives
    '' for any other type, and for an enum the dependency tree does not
    know.
    """
    match = self.__flags_pattern__.fullmatch(plain)
    if match is None:
      return ''
    enumName = match.group(1)
    if enumName in self._getTypeTables()['enums']:
      return enumName
    return ''

  def _findPassing(self, written: str, plain: str) -> Optional[Record]:
    """
    Says how a type is passed between Python and C++.

    Parameters
    ----------

    written : str
      The type as the header writes it, with every name in full.

    plain : str
      The same type as the compiler reads it, second names followed.

    Returns
    -------

    Optional[Record]
      None for a type that cannot be passed yet. Else a record saying:
      'kind': 'nothing', 'number', 'chars', 'enum', 'flags', 'address',
      'value', 'text', 'view', 'number address' or 'texts address'.
      'word': its word in the row. It is '' for a number that has no
      word that is right on every system.
      'className': for 'value', 'text' and 'view', the class; for
      'flags', the type as C++ reads it, as 'QFlags<Qt::WindowType>';
      for 'number' and 'number address', the number type built into
      C++, as 'int'.
      'pointed': for 'number address', whether the header writes the
      address itself, as 'int *', and not the number, as 'int &'.
    """
    tables = self._getTypeTables()
    plain = self._followAliases(plain)
    if plain == 'void':
      return dict(kind='nothing', word='nothing')
    readOnly = self._findReadOnlyNumber(plain)
    if readOnly:
      word = self._findNumberWord(self._stripReadOnly(written), readOnly)
      return dict(kind='number', word=word, className=readOnly)
    if plain == 'const char *':
      return dict(kind='chars', word='chars')
    if plain == 'char **':
      return dict(kind='texts address', word='address')
    if plain[-2:] in (' &', ' *'):
      changed = self._followAliases(plain[:-2])
      if changed in self.__number_types__ and changed != 'char':
        #  The number has to be as wide on every system as its name
        #  says, or the address would be read wrongly on one of them.
        word = self._findNumberWord(written[:-2].strip(), changed)
        return dict(
            kind='number address', word='address' if word else '',
            className=changed, pointed=plain.endswith(' *'),
        )
    if plain in tables['enums']:
      fixedWritten, fixedPlain = tables['enumTypes'].get(plain, ('int',) * 2)
      fixedPlain = self._followAliases(fixedPlain)
      if fixedPlain not in self.__number_types__:
        return None
      word = self._findNumberWord(fixedWritten, fixedPlain)
      return dict(kind='enum', word=word)
    flagsEnum = self._findFlagsEnum(plain)
    if flagsEnum:
      fixedPlain = tables['enumTypes'].get(flagsEnum, ('int',) * 2)[1]
      fixedPlain = self._followAliases(fixedPlain)
      #  Qt keeps the combinations of a wider enum in a wider number,
      #  which no 'int' holds.
      word = 'int' if fixedPlain in self.__flags_enum_types__ else ''
      flagsType = 'QFlags<%s>' % flagsEnum
      return dict(kind='flags', word=word, className=flagsType)
    if plain.endswith(' *'):
      pointed = plain[:-2]
      if pointed.startswith('const '):
        pointed = pointed[6:]
      if pointed in tables['classes']:
        return dict(kind='address', word='address')
      return None
    valueName = self._findValueName(plain)
    if not valueName:
      return None
    if valueName == self.__text_name__:
      return dict(kind='text', word='text', className=valueName)
    if valueName in self.__view_names__:
      return dict(kind='view', word='text', className=valueName)
    return dict(kind='value', word='address', className=valueName)

  def _getKnownNames(self, **kwargs) -> FrozenSet[str]:
    """
    Gives the full name of every class, enum and second name for a type
    the dependency tree knows, as 'QAccessible::Id'. Kept after the
    first call.
    """
    if self.__known_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      tree = self.getDependencyTree()
      self.__known_names__ = frozenset((
          *tree.getClassNames(), *tree.getEnumNames(),
          *tree.getAliasTypes(),
      ))
      return self._getKnownNames(_recursion=True)
    return self.__known_names__

  def _getOfferedNames(self, **kwargs) -> FrozenSet[str]:
    """
    Gives the name of everything the Qt shared objects of the parts of
    the dependency tree offer, each as the compiler names it. Kept
    after the first call.
    """
    if self.__offered_names__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      offered = set()  # type: Set[str]
      for qtPart in self.getDependencyTree().getQtParts():
        offered.update(qtPart.getOfferedNames())
      self.__offered_names__ = frozenset(offered)
      return self._getOfferedNames(_recursion=True)
    return self.__offered_names__

  def _canBeCalled(self, member: Record) -> bool:
    """
    Says whether a ritual calling this function could ever run.

    A function can be called when its code is somewhere: in a header,
    so the ritual gets a copy of it, or in a Qt shared object, which
    then offers it by name. A virtual function is found through the
    object it is called on and needs neither. Qt's headers declare a
    few functions that are nowhere, as
    'QEvent::qt_check_for_QGADGET_macro()'. One ritual calling such a
    function keeps the whole shared object of rituals from being opened.

    Parameters
    ----------

    member : Record
      What the compiler wrote down about the function, with its own name
      for it under 'mangledName'.
    """
    tree = self.getDependencyTree()
    name = member['mangledName']
    if member.get('virtual') or tree.hasBody(member):
      return True
    if name in tree.getDefinedNames():
      return True
    return True if name in self._getOfferedNames() else False

  def _spellOutside(self, cppType: str) -> str:
    """
    Writes a type the way it has to be written outside the class.

    Inside a class a header may shorten the name of anything the class
    declares itself, or a class it is built on declares: the second
    name 'Id' in 'QAccessible' is 'QAccessible::Id' anywhere else. A
    ritual stands outside every class, so it needs the full name.

    Parameters
    ----------

    cppType : str
      A type as the header of the class writes it, as 'Id' or
      'const Connection &'.

    Returns
    -------

    str
      The same type with every shortened name written in full. A name
      the dependency tree does not know inside the class, or inside a
      class it is built on, is left as it is.
    """
    known = self._getKnownNames()
    className = self.getClassName()
    tree = self.getDependencyTree()
    scopes = [className, *tree.getAncestors(className)]

    def spell(match: Any) -> str:
      name = match.group(0)
      for scope in scopes:
        while scope:
          fullName = '%s::%s' % (scope, name)
          if fullName in known:
            return fullName
          scope = scope.rpartition('::')[0]
      return name

    return self.__name_pattern__.sub(spell, cppType)

  def _findBarred(self, record: Record) -> Set[str]:
    """
    Gives which of 'operator new' and 'operator delete' the class
    declares and keeps from others: forbidden outright, or private or
    protected. A class doing so cannot be made with 'new', or removed
    with 'delete', by anyone but itself.
    """
    barred = set()  # type: Set[str]
    access = 'private' if record.get('tagUsed') == 'class' else 'public'
    for member in record.get('inner', ()):
      if member.get('kind') == 'AccessSpecDecl':
        access = member['access']
        continue
      if member.get('name') not in self.__making_functions__.values():
        continue
      if member.get('explicitlyDeleted') or access != 'public':
        barred.add(member['name'])
    return barred

  def _showTemplate(self, member: Record) -> str:
    """Names a template of the class, as 'QObject::findChild'."""
    return '%s::%s' % (self.getClassName(), member.get('name', ''))

  def _planFunction(self, member: Record, **kwargs) -> Record:
    """
    Works out the ritual of one function of the class, whether or not
    it can be written: its name, what it takes and gives, its row and
    its text. The keyword 'friend=True' says the function is one Qt
    writes inside the class with 'friend' in front, which belongs to
    no object and is called by its bare name.
    """
    className = self.getClassName()
    own, hidden = kwargs.get('own', False), kwargs.get('hidden', False)
    if kwargs.get('friend', False):
      kind = 'friend'
    else:
      kind = self.__function_kinds__[member['kind']]
    if kind == 'method' and member.get('storageClass') == 'static':
      kind = 'static method'
    functionType = member['type']['qualType']
    given, taken, words = self._splitFunctionType(functionType)
    #  The same type as the compiler reads it, second names followed.
    plainType = member['type'].get('desugaredQualType', functionType)
    plainGiven = self._splitFunctionType(plainType)[0]
    arguments = []
    for entry in member.get('inner', ()):
      if entry.get('kind') != 'ParmVarDecl':
        continue
      name = entry.get('name', '') or 'a%d' % len(arguments)
      if name == 'self':
        name = 'self_'
      cppType = entry['type']
      #  The compiler writes a type the class declares itself, as its
      #  enum 'Type', without the class in front. Whether the type can be
      #  passed is judged by its full name.
      plain = cppType.get('desugaredQualType', cppType['qualType'])
      plain = self._spellOutside(plain)
      default = None
      if 'init' in entry:
        #  What Qt fills in when the argument is left out. The compiler
        #  keeps it beside whatever else it notes of the argument.
        for child in entry.get('inner', ()):
          if isinstance(child, dict) and 'Attr' not in child.get('kind', ''):
            default = child
      arguments.append((name, cppType['qualType'], plain, default))
    shown = ', '.join(self._joinType(t, n) for n, t, _, _ in arguments)
    if kind == 'friend':
      shown = '%s(%s)' % (member['name'], shown)
    else:
      shown = '%s::%s(%s)' % (className, member['name'], shown)
    if kind in ('method', 'static method', 'friend'):
      shown = self._joinType(given, shown)
    if 'const' in words:
      shown = '%s const' % shown
    #  From here on the types are for the ritual, which stands outside
    #  the class and needs every name in full.
    given = self._spellOutside(given)
    unknown, unsure = [], []  # type: List[str], List[str]
    takes, passed, row, needs = [], [], [], []
    noted = []  # type: List[Record]
    for name, cppType, plain, default in arguments:
      written = self._spellOutside(cppType)
      passing = self._findPassing(written, plain)
      if passing is None:
        unknown.append(plain)
        passing = dict(kind='', word='')
      elif not passing['word']:
        unsure.append(written)
      noted.append(dict(
          name=name, written=written, plain=self._followAliases(plain),
          passing=passing, default=default,
      ))
      if passing['kind'] in ('value', 'text', 'view'):
        valueName = passing['className']
        needs.append(valueName)
        if passing['kind'] == 'view':
          #  A look at text is made from the text for the call.
          needs.append(self.__text_name__)
          takes.append((name, 'const %s *' % self.__text_name__))
          passed.append('%s(*%s)' % (valueName, name))
        else:
          takes.append((name, 'const %s *' % valueName))
          passed.append('*%s' % name)
      elif passing['kind'] == 'flags':
        #  The combination is made from its number for the call.
        takes.append((name, 'int'))
        passed.append('%s::fromInt(%s)' % (passing['className'], name))
      elif passing['kind'] == 'number address':
        #  Qt is handed the number at the address, which it may change.
        takes.append((name, '%s *' % written[:-2].strip()))
        passed.append(name if passing['pointed'] else '*%s' % name)
      elif passing['kind'] == 'number':
        #  A number taken to be read only is handed over as a copy.
        takes.append((name, self._stripReadOnly(written)))
        passed.append(name)
      else:
        takes.append((name, written))
        passed.append(name)
      row.append(passing['word'])
    opening, closing = '', ');'
    giving = None  # type: Optional[Record]
    inPlace = False
    if kind == 'constructor':
      given, gives = '%s *' % className, 'address'
      opening, called = 'return ', 'new %s' % className
      if self.hasCuteClass():
        #  Every object Python makes is of the C++ class of ours.
        called = 'new %s' % self.getCuteClassName()
    elif kind == 'destructor':
      given, gives = 'void', 'nothing'
      takes.insert(0, ('self', '%s *' % className))
      row.insert(0, 'address')
    else:
      ownName = member['name']
      if member['kind'] == 'CXXConversionDecl':
        #  A function that turns the object into another type is named
        #  after that type, and the header may shorten the name of the
        #  type as it may anywhere inside the class.
        ownName = 'operator %s' % self._spellOutside(plainGiven)
      if kind == 'friend':
        #  C++ finds it by what it is handed, so the bare name is called.
        called = ownName
      elif kind == 'static method':
        called = '%s::%s' % (className, ownName)
      else:
        const = 'const ' if 'const' in words else ''
        takes.insert(0, ('self', '%s%s *' % (const, className)))
        row.insert(0, 'address')
        called = 'self->%s' % ownName
        if own and hidden:
          #  Just this function of this class, which only a class built
          #  on it may call: reached through the class that is.
          through = 'Own%s' % className.replace('::', '_')
          called = 'static_cast<%s%s *>(self)->%s::%s' % (
              const, through, through, ownName)
        elif own:
          #  Just this function of this class, whatever the object is.
          called = 'self->%s::%s' % (className, ownName)
        ownType = '%s &' % className
        if ownName in self.__in_place_operators__ and given == ownType:
          #  'a += b' changes 'a' and gives 'a' itself back. The ritual
          #  gives nothing, and the cute function gives its object.
          given, plainGiven, inPlace = 'void', 'void', True
      giving = self._findPassing(given, self._spellOutside(plainGiven))
      if giving and giving['kind'] in ('number address', 'texts address'):
        #  The number itself, to be changed where it is, is not given
        #  back: its address would outlive nothing it is known by.
        giving = None
      if giving is None:
        unknown.append(given)
        giving = dict(kind='', word='')
      elif not giving['word']:
        unsure.append(given)
      gives = giving['word']
      giving = dict(giving, written=given)
      if giving['kind'] == 'number':
        given = self._stripReadOnly(given)
      if giving['kind'] in ('value', 'text', 'view'):
        #  The copy is made here, and its address is what goes back.
        valueName = giving['className']
        needs.append(valueName)
        if giving['kind'] == 'view':
          needs.append(self.__text_name__)
          valueName = self.__text_name__
          closing = ').toString());'
        else:
          closing = '));'
        given = '%s *' % valueName
        opening = 'return new %s(' % valueName
      elif giving['kind'] == 'flags':
        #  The number of the combination is what goes back.
        given = 'int'
        opening, closing = 'return static_cast<int>(', ').toInt());'
      elif giving['kind'] != 'nothing':
        opening = 'return '
    plan = dict(
        ritualName='ritual%s%s' % (
            '_own' if own else '', member.get('mangledName', '')),
        function=shown, kind=kind, gives=given, takes=(*takes,),
        row=(gives, *row), needs=(*dict.fromkeys(needs),),
        unknownTypes=(*dict.fromkeys(unknown),),
        unsureNumbers=(*dict.fromkeys(unsure),),
        words=(*words,), variadic='...' in taken,
        name=member['name'], arguments=(*noted,), giving=giving,
        inPlace=inPlace,
    )
    if kind == 'destructor':
      body = ['  delete self;']
    else:
      body = self._writeBody(opening, called, passed, closing)
    plan['text'] = self._writeRitual(plan, body)
    return plan

  def getFurtherBases(self) -> Names:
    """
    Gives the classes the class is built on after the first, in the
    order C++ names them, as 'QPaintDevice' for 'QWidget', which is
    built on 'QObject' and 'QPaintDevice'. It is empty for a class
    built on one class or on none.

    An object of such a class holds one part for each class it is built
    on. The part of the first class begins where the object begins. The
    part of a further class begins somewhere inside it, so a function
    of that class has to be handed another address than the object has.
    """
    tree, className = self.getDependencyTree(), self.getClassName()
    known = tree.getClassNames()
    parents = tree.getParents(className)
    return (*(p for p in parents[1:] if p in known),)

  def _planCast(self, baseName: str) -> Record:
    """
    Works out the ritual that gives where the part of an object is that
    belongs to a class it is built on after the first: it takes the
    address of the object and gives the address of that part, as C++
    itself works it out.

    It is no function of Qt, so it has a name of its own:
    'ritual_cast_QWidget_QPaintDevice'.
    """
    className = self.getClassName()
    plan = dict(
        ritualName='ritual_cast_%s_%s' % (
            className.replace('::', '_'), baseName.replace('::', '_')),
        function='%s as the %s it is built on' % (className, baseName),
        kind='cast', gives='%s *' % baseName,
        takes=(('self', '%s *' % className),),
        row=('address', 'address'), needs=(), unknownTypes=(),
        unsureNumbers=(), words=(), variadic=False,
        name='', arguments=(), giving=None, baseName=baseName,
    )
    body = ['  return static_cast<%s *>(self);' % baseName]
    plan['text'] = self._writeRitual(plan, body)
    return plan

  def _planOwnDestructor(self) -> Record:
    """
    Works out the ritual of the destructor of a class that declares
    none, which the compiler then writes itself.

    It is written for a class C++ can copy only. Python holds copies of
    such a class that nothing else knows of, and removes each by this
    ritual. The compiler's own name for a destructor is made of the
    words of the class name, each with its length in front, between
    '_ZN' and 'D1Ev': '_ZN5QSizeD1Ev' for 'QSize'.
    """
    className = self.getClassName()
    words = className.split('::')
    lengths = ''.join('%d%s' % (len(word), word) for word in words)
    plan = dict(
        ritualName='ritual_ZN%sD1Ev' % lengths,
        function='%s::~%s()' % (className, words[-1]),
        kind='destructor', gives='void',
        takes=(('self', '%s *' % className),),
        row=('nothing', 'address'), needs=(), unknownTypes=(),
        unsureNumbers=(), words=(), variadic=False,
        name='~%s' % words[-1], arguments=(), giving=None,
    )
    plan['text'] = self._writeRitual(plan, ['  delete self;'])
    return plan

  def _findReason(
      self,
      plan: Record,
      member: Record,
      access: str,
      signals: Any,
      abstract: bool,
      barred: Any,
  ) -> str:
    """
    Gives the reason a function gets no ritual, in words, or '' when
    nothing stands in the way of writing it.

    That Qt has marked a function as deprecated is no such reason. It
    gets its ritual like any other, and the compiler then passes on
    Qt's own notice of it, as 'Use territory() instead'. That notice
    is wanted: it is what a warning is for.
    """
    if member.get('explicitlyDeleted'):
      return 'forbidden: Qt declares it only to forbid its use'
    if access == 'private':
      return 'private: only Qt itself may call it'
    if access == 'protected':
      return 'protected: only a subclass may call it'
    if member['name'] in signals:
      return 'a signal'
    if plan['kind'] == 'constructor' and abstract:
      return 'the class is abstract, so C++ cannot make one'
    if self.__making_functions__.get(plan['kind']) in barred:
      if plan['kind'] == 'constructor':
        return "the class keeps 'new' to itself, so no ritual can make one"
      infoSpec = """the class keeps 'delete' to itself, so no ritual can
      remove one"""
      return ' '.join(infoSpec.split())
    if plan['variadic']:
      return 'takes any number of arguments'
    if '&&' in plan['words']:
      return 'can only be called on a value about to be thrown away'
    if 'mangledName' not in member:
      return 'the compiler gave it no name of its own'
    if not self._canBeCalled(member):
      infoSpec = """declared and nowhere to be found: no header has its
      code and no Qt shared object offers it"""
      return ' '.join(infoSpec.split())
    if plan['unknownTypes']:
      names = ', '.join(plan['unknownTypes'])
      return 'takes or gives a type that cannot be passed yet: %s' % names
    if plan['unsureNumbers']:
      infoSpec = """takes or gives a number that is not equally wide on
      every system: %s"""
      names = ', '.join(plan['unsureNumbers'])
      return ' '.join((infoSpec % names).split())
    return ''

  @staticmethod
  def _writeBody(
      opening: str,
      called: str,
      passed: List[str],
      closing: str,
  ) -> List[str]:
    """
    Gives the lines between the curly brackets of one ritual: the call
    of the Qt function. They are kept to 77 letters where the names
    allow it.

    Parameters
    ----------

    opening : str
      What stands before the call, as 'return ' or 'return new QSize('.

    called : str
      What is called, as 'self->expandedTo' or 'new QSize'.

    passed : List[str]
      What is passed on, in order, as '*otherSize'.

    closing : str
      What stands after the last thing passed on, as '));'.
    """
    whole = '  %s%s(%s%s' % (opening, called, ', '.join(passed), closing)
    if len(whole) <= 77:
      return [whole]
    lines, indent = [], '  '
    if opening.endswith('('):
      lines.append('%s%s' % (indent, opening))
      indent, opening = '      ', ''
    lines.append('%s%s%s(' % (indent, opening, called))
    if not passed:
      lines[-1] = '%s%s' % (lines[-1], closing)
      return lines
    for index, entry in enumerate(passed):
      end = closing if index == len(passed) - 1 else ','
      lines.append('%s    %s%s' % (indent, entry, end))
    return lines

  def _writeRitual(self, plan: Record, body: List[str]) -> str:
    """
    Gives the C++ text of one ritual, under the function it calls.

    Every ritual starts with the line 'extern "C" Q_DECL_EXPORT'. The
    first part gives it the plain name Python finds it by. The second is
    Qt's own mark for a function a shared object is to offer: Windows
    offers only what carries it, and on Linux and macOS it changes
    nothing.
    """
    lines = textwrap.wrap(
        plan['function'], 77, initial_indent='//  ',
        subsequent_indent='//      ',
    ) or ['//  ']
    takes = [self._joinType(t, n) for n, t in plan['takes']]
    named = self._joinType(plan['gives'], plan['ritualName'])
    lines.append('extern "C" Q_DECL_EXPORT')
    head = '%s(' % named
    whole = '%s%s) {' % (head, ', '.join(takes))
    if len(whole) <= 77:
      lines.append(whole)
    else:
      lines.append(head)
      for index, take in enumerate(takes):
        end = ') {' if index == len(takes) - 1 else ','
        lines.append('    %s%s' % (take, end))
      if not takes:
        lines[-1] = '%s) {' % head
    lines.extend(body)
    lines.append('}')
    return '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def write(self) -> str:
    """
    Writes the ritual file of the class into the work folder, and the
    rows file beside it, replacing those written before.

    Returns
    -------

    str
      The full path of the ritual file, which now exists. The rows file
      is at 'getRowsFile'.

    Raises
    ------

    MissingVariable
      One of the three setters has not been called.

    LookupError
      The tree has no class of that name.
    """
    ritualFile = self.getRitualFile()
    with open(ritualFile, 'w') as file:
      file.write(self.getRitualText())
    with open(self.getRowsFile(), 'w') as file:
      file.write(self.getRowsText())
    return ritualFile
