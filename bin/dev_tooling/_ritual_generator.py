"""RitualGenerator writes the ritual file of one Qt class, and the rows
file that goes with it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import collections
import json
import os
import platform
import re
import shutil
import subprocess
import tempfile
import textwrap
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.util import Finalize
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import (DependencyTree, HeaderFolder, HeaderReader, Machine,
               SourceReader)

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
    generator.setPartName('QtCore')
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
  - 'setPartName': the part of Qt the class is under, as 'QtCore'.
    Required. Every name the generator meets is seen from that part,
    as 'DependencyTree' has it: a class of QtGraphs names QtGraphs'
    own 'QBarSeries', not that of QtCharts.
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

  @staticmethod
  def _readCompilerText(text: str) -> Tuple[Dict[str, Set[str]], Set[str]]:
    """
    Reads the text the compiler writes of a file before it makes an
    object file of it, LLVM's IR, which 'clang++ -S -emit-llvm' gives.
    It is the same text on Linux, macOS and Windows, where the object
    files are not: the compiler's own name of each function, as
    '_ZNK7QObject6threadEv', stands in it as it is everywhere, without
    the '_' more that macOS puts in front in an object file.

    Parameters
    ----------

    text : str
      The text, as the compiler wrote it.

    Returns
    -------

    Tuple[Dict[str, Set[str]], Set[str]]
      For each name the file defines, a function, as a ritual, or a
      thing kept in memory, as a table of virtual functions, the names
      it leans on directly; and the names the file only declares, which
      must come from elsewhere.

    The text is read line by line:

      define ... @name(...) ... {   a function the file defines, up to
      }                             the line '}' alone
      declare ... @name(...)        a function from elsewhere
      @name = external global ...   a thing from elsewhere
      @name = ... constant ...      a thing the file defines, leaning
                                    on each name in the rest of the line

    The names of LLVM's own helpers, as 'llvm.memcpy.p0.p0.i64', are
    passed over: the compiler makes them into code of its own.
    """
    #  A name is '@' and the word, or '@' and a text between '"'.
    #  Another text between '"', as that of a 'char' array, may hold
    #  an '@' that is no name, and is passed over whole.
    token = re.compile(r'@"([^"]*)"|"[^"]*"|@([-\w$.]+)')
    escaped = re.compile(r'\\([0-9A-Fa-f]{2})')

    def namesIn(line: str) -> List[str]:
      """Gives each name the line holds, in the order they stand."""
      found = []  # type: List[str]
      for quoted, plain in token.findall(line):
        name = plain or escaped.sub(
            lambda match: chr(int(match.group(1), 16)), quoted)
        #  A leading '\\01' tells the compiler to write the name as it
        #  stands; the name is the rest.
        name = name.lstrip('\x01')
        if name and not name.startswith('llvm.'):
          found.append(name)
      return found

    leans = dict()  # type: Dict[str, Set[str]]
    declared = set()  # type: Set[str]
    inside = None  # type: Optional[str]
    for line in text.split('\n'):
      if inside is not None:
        if line == '}':
          inside = None
        else:
          leans[inside].update(namesIn(line))
        continue
      if line.startswith(('define ', 'declare ')):
        names = namesIn(line)
        if not names:
          continue
        if line.startswith('declare '):
          declared.add(names[0])
          continue
        leans.setdefault(names[0], set()).update(names[1:])
        if line.rstrip().endswith('{'):
          inside = names[0]
        continue
      if not line.startswith('@'):
        continue
      names = namesIn(line)
      if not names:
        continue
      #  The words between '=' and the kind of the thing say whether it
      #  is kept here or elsewhere.
      before = re.split(r' (?:global|constant|alias|ifunc) ', line, 1)[0]
      if re.search(r'= (?:\S+ )*(?:external|extern_weak)\b', before):
        declared.add(names[0])
        continue
      leans.setdefault(names[0], set()).update(names[1:])
    return leans, declared - set(leans)

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
  __part_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]
  #  The classes that get a C++ class of ours, through which Python can
  #  take a function over, or None for every class that has such a
  #  function. It is set while the way is tried on a few classes.
  __cute_class_limit__ = None  # type: Optional[Tuple[str, ...]]
  #  The functions C++ looks up in the object that are Qt's own
  #  workings, and are never taken over.
  __qt_own_virtuals__ = ('metaObject', 'qt_metacast', 'qt_metacall')
  __overridable_functions__ = None  # type: Optional[Records]
  #  Four things are asked for thousands of times and kept, each in a
  #  dict the tree gives for it, 'DependencyTree.getKept': what
  #  '_isHiddenType' found for each type; the generators '_getOther'
  #  made; the record of each class '_readRecord' read; and the kinds
  #  of list the functions of the tree hand around. The lock keeps two
  #  threads from both going through the tree for those kinds.
  __list_kinds_lock__ = threading.Lock()
  __has_cute_class__ = None  # type: Optional[bool]
  #  The code taken from Qt's source for the class, and the lines that
  #  pull in what that code needs; see '_settleSource'.
  __source_text__ = None  # type: Optional[str]
  __source_includes__ = None  # type: Optional[Tuple[str, ...]]
  #  The classes '_spellOutside' looks a shortened name up in, nearest
  #  first, the class of the generator first.
  __spelling_scopes__ = None  # type: Optional[List[str]]
  #  Classes whose header file the compiler showed has to come before
  #  that of the class, found by '_settleSource'.
  __pulled_first__ = ()  # type: Tuple[str, ...]
  #  The lines around lines pulling files in that stay with the ritual
  #  file: 'Build' puts only the lines under no '#if' into its common
  #  header, and nothing defines this name.
  __not_common_start__ = '#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER'
  __not_common_end__ = '#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER'
  __written_rituals__ = None  # type: Optional[Rituals]
  __unwritten_functions__ = None  # type: Optional[Reasons]
  #  The rituals of ours that stand for no function of the header by
  #  themselves, dropped by '_settleSource', with the reason; see
  #  'getNotWrittenExtras'. And the kinds of such rituals.
  __unwritten_extras__ = None  # type: Optional[List[Tuple[str, str]]]
  __ours_only__ = ('own', 'cast', 'take', 'list', 'map')
  __known_names__ = None  # type: Optional[FrozenSet[str]]
  #  How the names of the functions begin that Qt declares only for
  #  the compiler to check something, and writes no code for.
  __never_written__ = ('qt_check_for_',)
  #  How 'c++filt' writes the name of what the compiler makes for a
  #  class as a whole, and of what it makes around one function.
  #  An '#if' line of code taken from Qt's source that asks for a
  #  system, or for a processor; see '_findCopiedConditions'.
  __system_asked__ = re.compile(
      r'^[ \t]*#[ \t]*(?:if|ifdef|ifndef|elif)\b[^\n]*'
      r'\b(?:Q_OS_\w+|Q_CC_\w+|_WIN32|_WIN64|__APPLE__|__linux__|'
      r'__ANDROID__|__EMSCRIPTEN__)\b', re.M)
  __processor_asked__ = re.compile(
      r'^[ \t]*#[ \t]*(?:if|ifdef|ifndef|elif)\b[^\n]*'
      r'\bQ_PROCESSOR_\w+', re.M)
  __made_for_class__ = (
      'vtable for ', 'typeinfo name for ', 'typeinfo for ', 'VTT for ',
  )
  __made_for_function__ = (
      'non-virtual thunk to ', 'virtual thunk to ', 'guard variable for ',
  )
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

  def getPartName(self) -> str:
    """
    Gives the part of Qt the class is under, as 'QtCore'; every name the
    generator meets is seen from it.

    Provided by you, through 'setPartName'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setPartName' has not been called.
    """
    if self.__part_name__ is None:
      raise MissingVariable(self, '__part_name__', str)
    return self.__part_name__

  def _keyOf(self, className: str) -> Tuple[str, str]:
    """
    Gives the class a name stands for, seen from the part of the class
    of the generator, by its key, as ('QtCore', 'QObject').

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    tree = self.getDependencyTree()
    return tree.getClassKey(className, self.getPartName())

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

  def getHeaderReader(self) -> HeaderReader:
    """
    Gives the part of Qt the class belongs to.

    Found for you, by the dependency tree.

    Raises
    ------

    LookupError
      The tree has no class of the name you set.
    """
    return self.getDependencyTree().getHeaderReader(
        self.getClassName(), self.getPartName())

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
    className = self.getClassName()
    record = self._readRecord(className)
    #  Which functions are signals is read from the text of the header
    #  file: the compiler does not report it.
    signals = set()  # type: Set[str]
    for member in record.get('inner', ()):
      place = member.get('loc', dict())
      place = place.get('expansionLoc', place)
      headerPath, line = place.get('file'), place.get('line')
      if headerPath and line:
        if line in HeaderReader.getSignalLines(headerPath):
          signals.add(member.get('name'))
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
    #  A class some list of Qt holds gets the rituals of that list, and
    #  a class some map of Qt has for its values those of that map.
    written.extend(self._planLists())
    written.extend(self._planMaps())
    #  A function Qt's library has no name for gets its code from Qt's
    #  source, where that code can be taken.
    self._settleSource(written, unwritten)
    self.__written_rituals__ = (*written,)
    self.__unwritten_functions__ = (*unwritten,)

  def getCuteClassName(self) -> str:
    """Gives the name of the C++ class of ours that is built on the
    class of Qt, as 'CuteQWidget'. Python never sees it."""
    return 'Cute%s' % self.getClassName().replace('::', '_')

  def _getOther(self, className: str) -> RitualGenerator:
    """Gives a generator for another class of the same tree: the class
    the name stands for, seen from the part of this one."""
    if className == self.getClassName():
      return self
    return self._getGenerator(self._keyOf(className))

  def _getGenerator(self, classKey: Tuple[str, str]) -> RitualGenerator:
    """Gives a generator for a class of the same tree by its key, as
    ('QtCore', 'QObject'), made once for the tree."""
    if classKey == (self.getPartName(), self.getClassName()):
      return self
    kept = self.getDependencyTree().getKept('other generators')
    try:
      return kept[classKey]
    except KeyError:
      other = type(self)()
      other.setDependencyTree(self.getDependencyTree())
      other.setPartName(classKey[0])
      other.setClassName(classKey[1])
      #  It only works out plans and never writes a file, so it needs
      #  no folder.
      kept[classKey] = other
      return other

  def _readRecord(self, className: str) -> Record:
    """Gives the record of a class as the tree has it, read once: the
    class the name stands for, seen from the part of this one."""
    tree = self.getDependencyTree()
    kept = tree.getKept('class records')
    classKey = self._keyOf(className)
    try:
      return kept[classKey]
    except KeyError:
      record = tree.getClassRecord(classKey[1], classKey[0])
      kept[classKey] = record
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
    ancestors = tree.getAncestors(className, self.getPartName())
    chain = (className, *(name for _, name in reversed(ancestors)))
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
      if nearest['final']:
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
      #  Where Qt declares the function under an '#if', what is written
      #  for it here stands under the same: every '#if' around it in
      #  the class that declares it first and in the nearest one.
      conditions = self._findConditions(root['member'])
      for condition in self._findConditions(nearest['member']):
        if condition not in conditions:
          conditions = (*conditions, condition)
      found.append(dict(
          plan, key=root['member']['mangledName'], owner=nearest['owner'],
          rootOwner=root['owner'], access=nearest['access'],
          pure=nearest['pure'], conditions=conditions, **shape))
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
      if nearest['final']:
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
    try:
      ownerKey = self._keyOf(owner)
    except LookupError:
      #  Written in a namespace, as 'Qt::FocusPolicy', or in no class
      #  the tree knows: nothing keeps it from being named.
      return False
    kept = self.getDependencyTree().getKept('hidden types')
    try:
      return kept[(ownerKey, own)]
    except KeyError:
      hidden = self._findHiddenType(owner, own)
      kept[(ownerKey, own)] = hidden
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
      named = 'typedef %s (*%sCall%d)(%s);' % (
          function['cGives'], cuteName, index, ', '.join(handed))
      lines.append(self._wrapInConditions(named, function['conditions']))
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
      #  Where a Qt has no such function, its key is not known here
      #  and 'take' says no for it: Qt would never call what Python
      #  hands over.
      asked = '\n'.join((
          '    if (!std::strcmp(key, "%s")) {' % function['key'],
          '      taken[%d] = call;' % index,
          '      return true;',
          '    }'))
      lines.append(self._wrapInConditions(asked, function['conditions']))
    lines.append('    return false;')
    lines.append('  }')
    for index, function in enumerate(functions):
      lines.append('')
      written = '\n'.join(self._writeOverride(index, function))
      lines.append(self._wrapInConditions(written, function['conditions']))
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
    if len(whole) <= 77 or not arguments:
      #  A function that takes nothing has no place to break its line
      #  at, as 'QPlatformScreen::subpixelAntialiasingTypeHint()'.
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

  @staticmethod
  def _usesList(plan: Record) -> bool:
    """Says whether a ritual takes or gives a list, or is one of the
    rituals of a list itself."""
    if plan['kind'] == 'list':
      return True
    giving = plan.get('giving') or dict()
    if giving.get('kind') == 'list':
      return True
    arguments = plan.get('arguments') or ()
    return any(a['passing'].get('kind') == 'list' for a in arguments)

  @staticmethod
  def _usesMap(plan: Record) -> bool:
    """Says whether a ritual takes or gives a map, or is one of the
    rituals of a map itself."""
    if plan['kind'] == 'map':
      return True
    giving = plan.get('giving') or dict()
    if giving.get('kind') == 'map':
      return True
    arguments = plan.get('arguments') or ()
    return any(a['passing'].get('kind') == 'map' for a in arguments)

  def getListKinds(self) -> Dict[Tuple[str, str], Record]:
    """
    Gives every kind of list the functions of Qt take or give, as
    '_findListKind' describes it, under the part of the class it holds
    and its tag, as ('QtCore', 'QUrl').

    Found for you by going through every class the tree knows, once
    for each tree. The class a kind holds writes the rituals of that
    kind, and its cute class collects the kind, so each has to know
    whether some function somewhere hands such a list around.
    """
    kept = self.getDependencyTree().getKept('list kinds')
    with self.__list_kinds_lock__:
      if 'found' not in kept:
        kept['found'] = self._findListKinds()
      return kept['found']

  def _findListKinds(self) -> Dict[Tuple[str, str], Record]:
    """Does the going through the tree for 'getListKinds', which keeps
    the answer."""
    tree = self.getDependencyTree()
    kinds = dict()  # type: Dict[Tuple[str, str], Record]
    wanted = ('CXXMethodDecl', 'CXXConstructorDecl')
    cute = tree.getCuteNames()
    for classKey in tree.getClasses():
      if classKey not in cute:
        #  No function of Python hands its lists around.
        continue
      other = self._getGenerator(classKey)
      aliases = other._getTypeTables()['aliases']
      for member in other._readRecord(classKey[1]).get('inner', ()):
        if member.get('kind') not in wanted:
          continue
        given = self._splitFunctionType(member['type']['qualType'])[0]
        types = [given, *(
            child['type']['qualType']
            for child in member.get('inner', ())
            if isinstance(child, dict) and child.get('kind') == 'ParmVarDecl'
        )]
        for cppType in types:
          bare = cppType.replace('const ', '').replace(' &', '').strip()
          templated = any(
              mark in cppType for mark in ('QList<', 'QMap<', 'QHash<'))
          if not templated and bare not in aliases:
            #  A list is written 'QList<...>', or by a second name Qt
            #  has for one, as 'QStringList'. Anything else is spared
            #  the spelling out.
            continue
          spelled = other._spellOutside(cppType)
          for found in (
              other._findListKind(spelled), other._findMapKind(spelled)):
            if found is None:
              continue
            #  The kind is under the part of the class it holds, as
            #  that class sees it: a list of QtGraphs' 'QBarSet *' is
            #  another kind than one of QtCharts' 'QBarSet *'.
            try:
              holder = other._keyOf(found['holds'])[0]
            except LookupError:
              holder = ''
            kinds.setdefault((holder, found['tag']), found)
    return kinds

  def getOwnListKinds(self) -> List[Record]:
    """Gives the kinds of list that hold the class, as 'QList<QUrl>'
    for QUrl and 'QList<QAction *>' for QAction: most classes none."""
    className, partName = self.getClassName(), self.getPartName()
    return [
        listed for (holder, _), listed in self.getListKinds().items()
        if 'listType' in listed and listed['holds'] == className
        and holder == partName and listed['crossing'] != 'text'
    ]

  def getOwnMapKinds(self) -> List[Record]:
    """Gives the kinds of map whose values are of the class, as
    'QMap<int, QVariant>' for QVariant: most classes none. They are
    found in the same going through the tree as the lists."""
    className, partName = self.getClassName(), self.getPartName()
    return [
        mapped for (holder, _), mapped in self.getListKinds().items()
        if 'mapType' in mapped and mapped['holds'] == className
        and holder == partName
    ]

  def getMapNames(self, mapped: Record) -> List[str]:
    """Gives the names Qt itself has for one kind of map, as
    'QVariantMap' for 'QMap<QString, QVariant>': for most kinds none."""
    aliases = self._getTypeTables()['aliases']
    return sorted(
        name for name, meant in aliases.items()
        if meant == mapped['mapType'] and name.isidentifier()
    )

  def _planMaps(self) -> List[Record]:
    """
    Works out the eight rituals of each kind of map whose values are
    of the class: the one making an empty map, the one putting a value
    at a key, the one giving how many keys it has, the ones giving the
    key and the value at a place, the one saying whether it has a key,
    the one giving the value at a key, and the one removing the map.
    """
    plans = []  # type: List[Record]
    for mapped in self.getOwnMapKinds():
      mapType, value = mapped['mapType'], mapped['value']
      byValue = mapped['crossing'] == 'value'
      byText = mapped['keyWord'] == 'text'
      keyTaken = 'const %s *' % mapped['key'] if byText else 'int'
      keyGiven = '%s *' % mapped['key'] if byText else 'int'
      keyHanded = '*key' if byText else 'key'
      keyBack = '*std::next(self->keyBegin(), index)'
      if byText:
        keyBack = 'new %s(%s)' % (mapped['key'], keyBack)
      taken = 'const %s *' % value if byValue else value
      given = '%s *' % value if byValue else value
      handed = '*value' if byValue else 'value'
      word = mapped['keyWord']
      own, read = '%s *' % mapType, 'const %s *' % mapType

      def back(found: str) -> str:
        """What goes back for a value found in the map."""
        return 'new %s(%s)' % (value, found) if byValue else found

      shapes = (
          ('make', '%s()' % mapType, own, (), ('address',),
           'return new %s();' % mapType),
          ('put', 'insert(const Key &key, const T &value)', 'void',
           (('self', own), ('key', keyTaken), ('value', taken)),
           ('nothing', 'address', word, 'address'),
           'self->insert(%s, %s);' % (keyHanded, handed)),
          ('size', 'size() const', 'long long', (('self', read),),
           ('long long', 'address'), 'return self->size();'),
          ('key', 'the key at a place', keyGiven,
           (('self', read), ('index', 'long long')),
           (word, 'address', 'long long'), 'return %s;' % keyBack),
          ('value', 'the value at a place', given,
           (('self', read), ('index', 'long long')),
           ('address', 'address', 'long long'),
           'return %s;' % back('*std::next(self->constBegin(), index)')),
          ('has', 'contains(const Key &key) const', 'bool',
           (('self', read), ('key', keyTaken)), ('bool', 'address', word),
           'return self->contains(%s);' % keyHanded),
          ('get', 'value(const Key &key) const', given,
           (('self', read), ('key', keyTaken)),
           ('address', 'address', word),
           'return %s;' % back('self->value(%s)' % keyHanded)),
          ('drop', '~%s()' % mapped['pattern'], 'void', (('self', own),),
           ('nothing', 'address'), 'delete self;'),
      )
      for role, shown, gives, takes, row, line in shapes:
        plan = dict(
            ritualName='ritual_map_%s_%s' % (role, mapped['tag']),
            function='%s: %s' % (mapType, shown), kind='map',
            gives=gives, takes=takes, row=row, needs=(),
            unknownTypes=(), unsureNumbers=(), words=(), variadic=False,
            name='', arguments=(), giving=None, inPlace=False,
            mapped=mapped, mapRole=role,
        )
        plan['text'] = self._writeRitual(plan, ['  %s' % line])
        plans.append(plan)
    return plans

  def getListNames(self, listed: Record) -> List[str]:
    """Gives the names Qt itself has for one kind of list, as
    'QModelIndexList' for 'QList<QModelIndex>': for most kinds none."""
    aliases = self._getTypeTables()['aliases']
    return sorted(
        name for name, meant in aliases.items()
        if meant == listed['listType'] and name.isidentifier()
    )

  def _planLists(self) -> List[Record]:
    """
    Works out the five rituals of each kind of list that holds the
    class: the one making an empty list, the one adding an element, the
    one giving how many it holds, the one giving the element at a
    place, and the one removing the list.
    """
    plans = []  # type: List[Record]
    for listed in self.getOwnListKinds():
      listType, element = listed['listType'], listed['element']
      byValue = listed['crossing'] == 'value'
      handed = 'const %s *' % element if byValue else element
      back = '%s *' % element if byValue else element
      shapes = (
          ('make', '%s::QList()' % listType, '%s *' % listType, (),
           ('address',), 'return new %s();' % listType),
          ('add', 'void %s::append(const %s &value)' % (listType, element),
           'void', (('self', '%s *' % listType), ('element', handed)),
           ('nothing', 'address', 'address'),
           'self->append(%selement);' % ('*' if byValue else '')),
          ('size', 'qsizetype %s::size() const' % listType, 'long long',
           (('self', 'const %s *' % listType),), ('long long', 'address'),
           'return self->size();'),
          ('at', 'const %s &%s::at(qsizetype i) const' % (element, listType),
           back, (('self', 'const %s *' % listType), ('index', 'long long')),
           ('address', 'address', 'long long'),
           'return new %s(self->at(index));' % element if byValue
           else 'return self->at(index);'),
          ('drop', '%s::~QList()' % listType, 'void',
           (('self', '%s *' % listType),), ('nothing', 'address'),
           'delete self;'),
      )
      for role, shown, gives, takes, row, line in shapes:
        plan = dict(
            ritualName='ritual_list_%s_%s' % (role, listed['tag']),
            function=shown, kind='list', gives=gives, takes=takes,
            row=row, needs=(), unknownTypes=(), unsureNumbers=(),
            words=(), variadic=False, name='', arguments=(), giving=None,
            inPlace=False, listed=listed, listRole=role,
        )
        plan['text'] = self._writeRitual(plan, ['  %s' % line])
        plans.append(plan)
    return plans

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
    record = self._readRecord(className)
    for child in record.get('inner', ()):
      if isinstance(child, dict) and child.get('kind') == 'FinalAttr':
        #  Qt forbids building a class on this one, so no object of it
        #  is of a class of ours, and the ordinary call never comes
        #  back to Python.
        return plans
    #  The names the class also has a function of that only Qt itself
    #  may call. A function of such a name that a class built on this
    #  one may call cannot be reached apart from the other one.
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

  def getNotWrittenExtras(self) -> Reasons:
    """
    Gives the rituals of ours that stand for no function of the header
    by themselves, as the one running just Qt's own function, which
    '_settleSource' had to drop, each with the reason. They are no
    part of 'getNotWritten', which accounts for the functions of the
    header alone.
    """
    self.getWritten()
    return (*(self.__unwritten_extras__ or ()),)

  def getRitualNames(self) -> Tuple[str, ...]:
    """Gives the name of every ritual of the class, in order."""
    return (*(ritual['ritualName'] for ritual in self.getWritten()),)

  def _getHeading(self) -> str:
    """Says who wrote a file, from what, and that it is written anew."""
    headerReader = self.getHeaderReader()
    headerPath = self.getDependencyTree().getHeaderPath(
        self.getClassName(), self.getPartName())
    relative = os.path.relpath(headerPath, headerReader.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.RitualGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, headerReader.getQtVersion())
    return ' '.join(info.split())

  def getRitualText(self) -> str:
    """
    Gives the whole text of the ritual file, without writing it.

    Written for you from 'getWritten': a heading, the lines pulling in
    the header file of the class, as 'HeaderReader.getIncludeLines' gives
    them, the same for each value class a ritual copies, and then each
    ritual under the Qt function it calls.
    """
    tree = self.getDependencyTree()
    className = self.getClassName()
    heading = textwrap.wrap(self._getHeading(), 73)
    blocks = ['\n'.join('//  %s' % line for line in heading)]
    #  The class Qt keeps the data of another class in, as
    #  'QWidgetTextControlPrivate', names that class in its 'q_func'
    #  ('Q_DECLARE_PUBLIC'), and its header file may not pull in the
    #  one declaring it: Qt's own '.cpp' files pull that one in first.
    needed = [
        *self._findPublicClasses(), *self.__pulled_first__, className]
    for ritual in self.getWritten():
      needed.extend(n for n in ritual['needs'] if n not in needed)
    if self.hasCuteClass():
      #  The C++ class of ours holds the functions of the classes this
      #  one is built on as well, and a value one of them takes or
      #  gives has to be known in full here.
      for function in self.getOverridable():
        needed.extend(n for n in function['needs'] if n not in needed)
    includeLines = []  # type: List[str]
    privateLine = self._getPrivateGlobalLine()
    if privateLine:
      #  The file may ask of a part Qt keeps to itself: the class is
      #  declared in a header file Qt calls private, or code taken from
      #  Qt's source stands in it. The private list of the part answers
      #  that, and is read before any '#if'.
      includeLines.append(privateLine)
    partName = self.getPartName()
    for name in needed:
      headerReader = tree.getHeaderReader(name, partName)
      lines = headerReader.getIncludeLines(
          tree.getHeaderPath(name, partName))
      for line in lines.split('\n'):
        if line.strip() and line not in includeLines:
          includeLines.append(line)
    #  A function whose code lies in another header file than the one
    #  its class is declared in: that header file is pulled in as well.
    ownPath = tree.getHeaderPath(className, partName)
    for ritual in self.getWritten():
      ritualName = ritual['ritualName']
      for start in ('ritual_own', 'ritual'):
        if ritualName.startswith(start):
          break
      codePath = tree.getDefinedPath(ritualName[len(start):], partName)
      if codePath is None or codePath == ownPath:
        continue
      for headerReader in tree.getHeaderReaders():
        if not codePath.startswith('%s/' % headerReader.getPartFolder()):
          continue
        for line in headerReader.getIncludeLines(codePath).split('\n'):
          if line.strip() and line not in includeLines:
            includeLines.append(line)
    owned = [r for r in self.getWritten() if r['kind'] == 'own']
    if any(self._usesList(ritual) for ritual in self.getWritten()):
      includeLines.append('#include <QtCore/qlist.h>')
    if any(self._usesMap(ritual) for ritual in self.getWritten()):
      includeLines.append('#include <QtCore/qmap.h>')
      includeLines.append('#include <QtCore/qhash.h>')
      includeLines.append('#include <iterator>')
    if self.hasCuteClass():
      includeLines.append('#include <cstring>')
    #  A header file Qt keeps apart, as 'qabstractspinbox_p.h', stays
    #  with this file as well, out of the common header 'Build' makes:
    #  Qt writes those for its own files one at a time, and all of them
    #  together do not mean what each means alone. That one declares an
    #  'operator+' of two QVariant for everybody, which makes the '+' of
    #  two QLatin1StringView in 'qdbusabstractinterface.cpp' ambiguous.
    #  Qt's header files for everybody are meant to be read together.
    apart = re.compile(r'^#include <Qt\w+/\d+\.\d+\.\d+/Qt\w+/')
    grouped = []  # type: List[str]
    for line in includeLines:
      if line == privateLine or not apart.match(line):
        grouped.append(line)
        continue
      if grouped and grouped[-1] == self.__not_common_end__:
        grouped.insert(len(grouped) - 1, line)
        continue
      grouped.extend((self.__not_common_start__, line,
                      self.__not_common_end__))
    includeLines = grouped
    #  What the code taken from Qt's source needs comes as Qt's files
    #  have it, with the '#if' lines around it, so no line of it is
    #  left out for standing above already. It stays with this file,
    #  out of the common header 'Build' makes of the lines under no
    #  '#if': a header file of Qt's source may be one to be read once
    #  only, as 'qmetaobject_moc_p.h', which has no guard.
    if self.getSourceIncludes():
      includeLines.extend((
          self.__not_common_start__, *self.getSourceIncludes(),
          self.__not_common_end__))
    conditions = self.getFileConditions()
    #  A switch another part has, asked by an '#if' of the file, as
    #  'QT_CONFIG(http)' of QtNetwork in a file of QtHttpServer, is
    #  answered by the list of that part, pulled in first.
    asking = [*conditions]
    for ritual in self.getWritten():
      asking.extend(ritual.get('conditions', ()))
    if self.hasCuteClass():
      for function in self.getOverridable():
        asking.extend(function.get('conditions', ()))
    switchLines = self._findSwitchLines(asking, privateLine)
    if conditions:
      #  Qt declares the class under an '#if', so the whole file stands
      #  under it: where a Qt has no such class, nothing of the file is
      #  compiled. What an '#if' of Qt's asks can only be answered once
      #  the header file of the part has been read, so that comes first.
      asked = ['#include <%s/%s>' % (
          partName, HeaderFolder.getGlobalHeader(partName))]
      if privateLine:
        asked.append(privateLine)
      opening = [
          *switchLines, *asked, *('#if %s' % one for one in conditions)]
      blocks[0] = '\n'.join((blocks[0], *opening, *includeLines))
    else:
      blocks[0] = '\n'.join((blocks[0], *switchLines, *includeLines))
    if self.getSourceText():
      blocks.append(self.getSourceText())
    ownClass = self._writeOwnClass(owned)
    if ownClass:
      blocks.append(ownClass)
    if self.hasCuteClass():
      blocks.append(self._writeCuteClass())
    blocks.extend(ritual['text'] for ritual in self.getWritten())
    if conditions:
      blocks.append('\n'.join(
          '#endif  // %s' % one for one in reversed(conditions)))
    return '%s\n' % '\n\n'.join(blocks)

  def getFileConditions(self) -> Tuple[str, ...]:
    """
    Gives the conditions the whole ritual file stands under, outermost
    first: the one under which Qt installs the header file of the
    class, as 'QT_CONFIG(metal)' for 'qrhimetal_p.h', when there is
    one, or, where that one asks what no compiler knows, whether the
    header file is there, as '__has_include(<QtOpcUa/qopcuakeypair.h>)';
    then what each '#if' line around the class asks. Where one does
    not hold, nothing of the file is compiled.
    """
    tree = self.getDependencyTree()
    className = self.getClassName()
    conditions = self._findConditions(self._readRecord(className))
    headerPath = tree.getHeaderPath(className, self.getPartName())
    installed = HeaderReader.getHeaderFolder().getInstallCondition(
        headerPath)
    if installed is None:
      #  Qt installs the header file under a condition no compiler can
      #  be asked, as 'OPENSSL_FOUND' or 'ANDROID_EMBEDDED': whether it
      #  is installed is asked in its place, as the compiler can.
      relative = os.path.relpath(
          headerPath, self.getHeaderReader().getQtHeaderFolder())
      installed = '__has_include(<%s>)' % relative
    if installed:
      return (installed, *conditions)
    return conditions

  def _findSwitchLines(
      self,
      conditions: List[str],
      privateLine: str,
  ) -> List[str]:
    """
    Gives the lines that pull in the list of switches of each other
    part whose switch the conditions ask, as 'QT_CONFIG(http)' of
    QtNetwork: its header file that brings the list in, or, for a
    switch Qt keeps to itself, the one in its folder 'private'. A part
    with no such file of its own has the list pulled in itself. The
    public list of the part of the class comes with the class.
    """
    folder = HeaderReader.getHeaderFolder()
    version = HeaderReader.getQtVersion()
    partName = self.getPartName()
    lines = []  # type: List[str]
    for name in re.findall(r'QT_CONFIG\((\w+)\)', ' '.join(conditions)):
      owner = folder.getSwitchOwner(name)
      if owner is None:
        continue
      ownerName, private = owner
      if not private:
        if ownerName == partName:
          continue
        line = '#include <%s/%s>' % (
            ownerName, HeaderFolder.getGlobalHeader(ownerName))
      else:
        header = HeaderFolder.getPrivateGlobalHeader(ownerName)
        if not header:
          header = '%s-config_p.h' % ownerName.lower()
        line = '#include <%s/%s/%s/private/%s>' % (
            ownerName, version, ownerName, header)
        if line == privateLine:
          continue
      if line not in lines:
        lines.append(line)
    return lines

  def _findPublicClasses(self) -> Tuple[str, ...]:
    """
    Gives the class whose data the class of the generator keeps, as
    'QWidgetTextControl' for 'QWidgetTextControlPrivate': the class its
    function 'q_func' gives, which Qt's 'Q_DECLARE_PUBLIC' writes.
    Nothing for a class with no such function, or one giving a class
    the tree does not know.
    """
    tree = self.getDependencyTree()
    className = self.getClassName()
    found = []  # type: List[str]
    for member in self._readRecord(className).get('inner', ()):
      if not isinstance(member, dict) or member.get('name') != 'q_func':
        continue
      qualType = member.get('type', dict()).get('qualType', '')
      match = re.match(r'\s*(?:const\s+)?([\w:]+)\s*\*', qualType)
      if match is None:
        continue
      name = match.group(1)
      if name != className and tree.hasClass(name, self.getPartName()):
        if name not in found:
          found.append(name)
    return (*found,)

  def _getPrivateGlobalLine(self) -> str:
    """
    Gives the line pulling in the private global header file of the
    part of the class, as '#include <QtWidgets/6.12.0/QtWidgets/private/
    qtwidgetsglobal_p.h>', where the ritual file needs it: the class is
    declared in a header file Qt keeps apart, or code taken from Qt's
    source stands in the file. Else ''.
    """
    tree = self.getDependencyTree()
    className, partName = self.getClassName(), self.getPartName()
    headerReader = tree.getHeaderReader(className, partName)
    headerPath = tree.getHeaderPath(className, partName)
    apart = any(
        headerPath.startswith(folder)
        for folder in headerReader.getApartFolders())
    if not apart and not self.getSourceText():
      return ''
    if not HeaderFolder.getPrivateGlobalHeader(partName):
      #  A part with no such file of its own, as QtXml, has no private
      #  switches: its files ask those of QtCore.
      partName = 'QtCore'
    return '#include <%s/%s/%s/private/%s>' % (
        partName, HeaderReader.getQtVersion(), partName,
        HeaderFolder.getPrivateGlobalHeader(partName))

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
    of the ritual file; for a part of 'HeaderReader.getOwnOrderParts'
    only, under 'parts first' the part and the parts it needs, the
    nearest first, whose folders the compiler looked in first, so that
    'Rituals.build' does the same; and under 'rows' each ritual with
    its row.
    """
    about = textwrap.wrap(self._getHeading(), 66)
    lines = ['{', '  "about": [']
    lines.extend(
        '    %s%s' % (json.dumps(line), ',' if line is not about[-1] else '')
        for line in about
    )
    lines.append('  ],')
    partName = self.getPartName()
    if partName in HeaderReader.getOwnOrderParts():
      first = HeaderReader.getNeededParts(partName)
      lines.append('  "parts first": [')
      packed = '   '
      for position, name in enumerate(first):
        piece = json.dumps(name)
        if position < len(first) - 1:
          piece = '%s,' % piece
        if len(packed) + 1 + len(piece) > 77 and packed.strip():
          lines.append(packed)
          packed = '   '
        packed = '%s %s' % (packed, piece)
      lines.append(packed)
      lines.append('  ],')
    lines.append('  "rows": {')
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

  def setPartName(self, partName: str) -> None:
    """
    Tells the generator which part of Qt the class is under, as
    'QtGraphs' for its 'QBarSeries'. Every name the generator meets is
    seen from that part, as 'DependencyTree' has it.

    Required. Calling it again forgets what was decided before.

    Raises
    ------

    TypeException
      'partName' is not text.
    """
    if not isinstance(partName, str):
      raise TypeException('partName', partName, str)
    self.__part_name__ = partName
    self.__written_rituals__ = None
    self.__unwritten_functions__ = None
    self.__overridable_functions__ = None
    self.__has_cute_class__ = None
    self.__type_tables__ = None
    self.__known_names__ = None

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

    Only what Python has something for counts: a class that gets a
    cute class, as 'DependencyTree.getCuteNames' has them, the classes
    of Qt that cross as Python's own text, and an enum written in such
    a class or in no class at all. A type left out here cannot be
    passed, and a function naming it gets no ritual.
    """
    if self.__type_tables__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      #  Each name as seen from the part of the class: a class of
      #  QtGraphs names QtGraphs' own 'QBarSeries'. Every class of a
      #  part sees them alike, so they are kept for the part.
      tree, partName = self.getDependencyTree(), self.getPartName()
      kept = tree.getKept('type tables')
      if partName in kept:
        self.__type_tables__ = kept[partName]
        return self._getTypeTables(_recursion=True)
      cuteKeys, copyableKeys = tree.getCuteNames(), tree.getCopyableNames()
      seen = {
          name: tree.getClassKey(name, partName)
          for name in {name for _, name in tree.getClasses()}}
      textNames = (self.__text_name__, *self.__view_names__)
      cute = frozenset((
          *(name for name, key in seen.items() if key in cuteKeys),
          *textNames,
      ))
      enums = []  # type: List[str]
      for enumName in sorted({name for _, name in tree.getEnumNames()}):
        owner = enumName.rpartition('::')[0]
        if owner not in seen or owner in cute:
          enums.append(enumName)
      self.__type_tables__ = dict(
          aliases=tree.getAliasTypes(partName),
          enums=frozenset(enums),
          classes=frozenset(name for name in seen if name in cute),
          enumTypes=tree.getEnumTypes(partName),
          copyable=frozenset(
              name for name, key in seen.items()
              if key in copyableKeys and name in cute),
      )
      kept[partName] = self.__type_tables__
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

  def _findListKind(self, cppType: str) -> Optional[Record]:
    """
    Says which kind of list a type hands around as a value. Qt has one
    class of list for each thing a list can hold: 'QList<QUrl>',
    'QList<QAction *>', and 'QStringList', its second name for
    'QList<QString>'.

    Parameters
    ----------

    cppType : str
      A type with every name in full, as 'QList<QUrl>', 'const
      QList<QUrl> &' or 'QStringList'.

    Returns
    -------

    Optional[Record]
      None for a type that is no list handed around as a value, and for
      a list of something that cannot be an element yet: a number, an
      enum, a pair, a class Qt writes inside another. Else 'listType':
      the list as C++ writes it;
      'element': what it holds, as C++ writes it; 'crossing': how one
      element crosses, 'value', 'address' or 'text'; 'holds': the class
      of the element; 'tag': the kind as the names of its rituals have
      it, as 'QUrl' and 'QAction_ptr'.
    """
    if cppType.endswith(' &'):
      if not cppType.startswith('const '):
        return None
      cppType = cppType[:-2]
    if cppType.startswith('const '):
      cppType = cppType[6:]
    cppType = self._followAliases(cppType.strip())
    if not cppType.startswith('QList<') or not cppType.endswith('>'):
      return None
    element = cppType[len('QList<'):-1].strip()
    tables = self._getTypeTables()
    if element == self.__text_name__:
      crossing, holds, tag = 'text', element, element
    elif element.endswith(' *') and element[:-2] in tables['classes']:
      crossing, holds = 'address', element[:-2]
      tag = '%s_ptr' % holds
    elif element in tables['copyable']:
      crossing, holds, tag = 'value', element, element
    else:
      return None
    if '::' in holds:
      #  A class Qt writes inside another: not as an element yet.
      return None
    return dict(
        listType='QList<%s>' % element, element=element,
        crossing=crossing, holds=holds, tag=tag,
    )

  def _findMapKind(self, cppType: str) -> Optional[Record]:
    """
    Says which kind of map a type hands around as a value. Qt has one
    class of map for each kind of key and value: 'QMap<int, QVariant>',
    'QHash<int, QByteArray>', and 'QVariantMap', its second name for
    'QMap<QString, QVariant>'.

    Parameters
    ----------

    cppType : str
      A type with every name in full.

    Returns
    -------

    Optional[Record]
      None for a type that is no map handed around as a value, and for
      a map that cannot be passed yet: its keys are neither 'int' nor
      text, or its values are no class written inside no other. Else
      'mapType': the map as C++ writes it; 'pattern': 'QMap' or
      'QHash'; 'key': the keys, as C++ writes them; 'keyWord': their
      word in a row, 'int' or 'text'; 'value': the values, as C++
      writes them; 'crossing': how one value crosses, 'value' or
      'address'; 'holds': the class of the values; 'tag': the kind as
      the names of its rituals have it, as 'QMap_int_QVariant'.
    """
    if cppType.endswith(' &'):
      if not cppType.startswith('const '):
        return None
      cppType = cppType[:-2]
    if cppType.startswith('const '):
      cppType = cppType[6:]
    cppType = self._followAliases(cppType.strip())
    pattern = cppType.partition('<')[0]
    if pattern not in ('QMap', 'QHash') or not cppType.endswith('>'):
      return None
    key, comma, value = cppType[len(pattern) + 1:-1].partition(',')
    key, value = key.strip(), value.strip()
    if not comma:
      return None
    tables = self._getTypeTables()
    if self._followAliases(key) == 'int':
      keyWord, keyTag = 'int', 'int'
    elif key == self.__text_name__:
      keyWord, keyTag = 'text', key
    else:
      return None
    if value.endswith(' *') and value[:-2] in tables['classes']:
      crossing, holds = 'address', value[:-2]
    elif value in tables['copyable'] and value != self.__text_name__:
      crossing, holds = 'value', value
    else:
      return None
    if '::' in holds:
      return None
    ending = '_ptr' if crossing == 'address' else ''
    return dict(
        mapType='%s<%s, %s>' % (pattern, key, value), pattern=pattern,
        key=key, keyWord=keyWord, value=value, crossing=crossing,
        holds=holds, tag='%s_%s_%s%s' % (pattern, keyTag, holds, ending),
    )

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
    listed = self._findListKind(plain)
    if listed:
      #  A list crosses as a value does: by the address of the C++ list.
      return dict(
          kind='list', word='address', className=listed['listType'],
          listed=listed,
      )
    mapped = self._findMapKind(plain)
    if mapped:
      #  A map crosses as a value does too.
      return dict(
          kind='map', word='address', className=mapped['mapType'],
          mapped=mapped,
      )
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
          *(name for _, name in tree.getClasses()),
          *(name for _, name in tree.getEnumNames()),
          *tree.getAliasTypes(self.getPartName()),
      ))
      return self._getKnownNames(_recursion=True)
    return self.__known_names__

  def _findConditions(self, record: Record) -> Tuple[str, ...]:
    """
    Gives the conditions under which Qt declares a function, a class
    or an enum: what each '#if' line around its declaration asks,
    outermost first, as 'HeaderReader.getConditions' reads them from
    the text of the header file. Empty for a thing under no '#if', and
    for one the compiler made itself, which stands at no line.

    Parameters
    ----------

    record : Record
      What the compiler wrote down about the thing, with the place it
      is declared at under 'loc'.
    """
    place = record.get('loc', dict())
    place = place.get('expansionLoc', place)
    headerPath, line = place.get('file'), place.get('line')
    if not headerPath or not line:
      return ()
    return HeaderReader.getConditions(headerPath, line)

  def _findOwnConditions(self, member: Record) -> Tuple[str, ...]:
    """Gives the conditions of a function of the class that go beyond
    those of the class itself. The ones of the class stand around the
    whole ritual file; see 'getRitualText'."""
    whole = self._findConditions(self._readRecord(self.getClassName()))
    own = self._findConditions(member)
    if own[:len(whole)] == whole:
      return own[len(whole):]
    return own

  @staticmethod
  def _wrapInConditions(text: str, conditions: Tuple[str, ...]) -> str:
    """
    Gives a piece of C++ text with one '#if' line for each condition
    above it, outermost first, and the '#endif' lines below it.

    A ritual stands between the same '#if' lines as the function it
    calls stands between in Qt's header file. The compiler of each
    machine then compiles the ritual exactly where that machine's Qt
    has the function, and leaves it out where it has not. Nothing is
    decided here: the text is the same for every system.
    """
    if not conditions:
      return text
    opening, closing = [], []  # type: List[str], List[str]
    for condition in conditions:
      line = '#if %s' % condition
      if len(line) > 77:
        #  A long question goes on in the next line after a backslash.
        pieces = textwrap.wrap(
            line, 73, break_long_words=False, break_on_hyphens=False)
        line = ' \\\n    '.join(pieces)
      opening.append(line)
      note = '#endif  // %s' % condition
      closing.insert(0, note if len(note) <= 77 else '#endif')
    return '\n'.join((*opening, text, *closing))

  def getPrivateArguments(self) -> Tuple[str, ...]:
    """
    Gives the '-I' arguments by which the compiler finds the headers
    Qt calls private for the compiles of the class, or none when no
    part of the tree reads those and no source of Qt was provided.
    They are those of the probe header its compiles start from; see
    '_getProbePart'.
    """
    return self._getPrivateArguments(self._getProbePart())

  def _getPrivateArguments(self, partName: str) -> Tuple[str, ...]:
    """
    Gives the '-I' arguments by which the compiler finds the headers
    Qt calls private: those 'HeaderReader.getPrivateIncludeFolders'
    gives the part of that name, or, for '', those of
    'HeaderReader.getSharedIncludeFolders', in the order of the
    alphabet. None when no part of the tree reads those and no source
    of Qt was provided.
    """
    tree = self.getDependencyTree()
    headerReaders = tree.getHeaderReaders()
    if tree.getSourceReader() is None:
      if not any(reader.hasPrivate() for reader in headerReaders):
        return ()
    folders = HeaderReader.getSharedIncludeFolders()
    for reader in headerReaders:
      if partName and reader.getPartName() == partName:
        folders = reader.getPrivateIncludeFolders()
    return (*('-I%s' % folder for folder in folders),)

  def _getProbePart(self) -> str:
    """
    Gives the part whose folders the compiles of the class are told:
    the part of the class where it has a probe header of its own; else
    '', the folders in the order of the alphabet, which the one of
    every part is made with. A precompiled header serves only a compile
    told the same.
    """
    kept = self.getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    partName = self.getPartName()
    return partName if partName in kept['own'] else ''

  def getSourceText(self) -> str:
    """Gives the code taken from Qt's own source for the class, as C++
    text under a heading saying whose it is, or '' when none was."""
    if self.__source_text__ is None:
      self.getWritten()
    return self.__source_text__ or ''

  def getSourceIncludes(self) -> Tuple[str, ...]:
    """Gives the lines that pull in what the code of 'getSourceText'
    needs, as the files of Qt's source it was taken from have them."""
    if self.__source_includes__ is None:
      self.getWritten()
    return self.__source_includes__ or ()

  def _findSourceCode(
      self,
      member: Record,
      className: Optional[str] = None,
  ) -> Optional[Record]:
    """
    Gives the definition of a function in Qt's own source, as
    'SourceReader.findDefinitions' has it, or None when no source was
    provided or the source has not exactly one definition that takes
    what the function takes. The function is one of the class of the
    generator, or of 'className' where that is given.
    """
    tree = self.getDependencyTree()
    source = tree.getSourceReader()
    if source is None:
      return None
    if className is None:
      className = self.getClassName()
    name = member.get('name', '')
    if member.get('kind') == 'CXXConstructorDecl':
      name = className.rpartition('::')[2]
    taken = [
        entry['type']['qualType'] for entry in member.get('inner', ())
        if entry.get('kind') == 'ParmVarDecl'
    ]
    whole = member.get('type', dict()).get('qualType', '')
    const = True if re.search(r'\)\s*const\b', whole) else False
    partName = tree.getPartName(className, self.getPartName())
    found = [
        definition for definition
        in source.findDefinitions(partName, '%s::%s' % (className, name))
        if len(definition['arguments']) == len(taken)
        and definition['const'] == const
    ]
    if len(found) > 1:
      #  Several forms take as many: the one whose every argument
      #  begins with the type the header declares.
      def squeeze(written: str) -> str:
        return ''.join(written.split())
      found = [
          definition for definition in found
          if all(squeeze(argument).startswith(squeeze(cppType))
                 for argument, cppType
                 in zip(definition['arguments'], taken))
      ]
    return found[0] if len(found) == 1 else None

  def _isOfQt(self, symbol: str) -> bool:
    """Says whether a name the compiler made stands for something of
    Qt: a name of the C++ library or of the system does not. It is of
    Qt when a name in it begins with 'Q' or 'q'; when it is of a class
    the tree knows, seen from the part, as the table of virtual
    functions of QtDataVisualization's 'AbstractRenderItem',
    '_ZTV18AbstractRenderItem', or a function of it; or when Qt's
    header files declare it, as the logging category 'lcImageIo' that
    Qt's 'qimage_p.h' declares; see '_getDeclaredSymbols'."""
    if re.search(r'\d+[Qq][A-Za-z_]', symbol):
      return True
    #  The first name the compiler's own name holds: after '_Z', what
    #  it made for a class ('TV', 'TI', 'TS', 'TT'), a scope ('N') and
    #  what qualifies a function of it ('K', 'V', 'r', 'R', 'O').
    first = re.match(r'_Z(?:T[VIST])?(?:N[KVrRO]*)?(\d+)', symbol)
    if first is not None:
      start, length = first.end(), int(first.group(1))
      name = symbol[start:start + length]
      if self.getDependencyTree().hasClass(name, self.getPartName()):
        return True
    return self._plainSymbol(symbol) in self._getDeclaredSymbols()

  def _getProbeCommand(self, partName: str) -> Tuple[str, ...]:
    """Gives the start of the 'clang++' command of '_probeText', which
    the precompiled header of 'getProbeHeader' is made with as well: a
    precompiled header serves only a compile told the same. The folders
    are those of the part of that name, or of the first part of the
    tree for ''; see '_getPrivateArguments'."""
    return (
        'clang++', '-std=c++17', *Machine.getCompilerFlags(), '-O0', '-w',
        '-fno-access-control', '-ffunction-sections', '-ferror-limit=0',
        '-I%s' % HeaderReader.getQtHeaderFolder(),
        *self._getPrivateArguments(partName),
    )

  def getProbeHeader(self) -> str:
    """
    Gives the path of the precompiled header each compile of
    '_probeText' starts from: the own list of every part of the tree,
    as '#include <QtCore/QtCore>', read by the compiler once and
    written down as the compiler keeps it. A compile that starts from
    it takes a tenth of the time, since reading Qt's headers is most
    of the work.

    Made for you at the first call, which takes about twenty seconds,
    and kept with the tree. It lies in a folder of its own in the work
    folder of the first part of the tree, about 65 MB, and that folder
    is removed when the Python that made it ends. Call it once before
    handing the tree to other processes, and they all start from the
    one file.

    A part whose line the compiler blames for an error is left out,
    and the header made again without it: Qt's QtGraphs refuses to be
    in one compile with QtCharts or QtDataVisualization, since they
    use the same class names. 'getLeftOutParts' gives those parts,
    with what the compiler said. Each of them gets a header of its
    own, of the part and the parts it needs, as Qt's own build has
    them together, and the compiles of its classes start from that
    one. So does each part of 'HeaderReader.getOwnOrderParts', whose
    folders come in its own order, where the one of every part is made
    with them in the order of the alphabet. A part whose own header the
    compiler refuses has its classes written down as missed, and
    'write' refuses them.

    Raises
    ------

    RuntimeError
      The compiler refused to make it, and blamed no line of a part.
      The message holds what it said.

    LookupError
      The part of the class is left out, and the compiler refused its
      own header; see 'getRefusedParts'.
    """
    kept = self.getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    partName = self.getPartName()
    if partName in kept['refused']:
      infoSpec = """%s is not written: its part %s is left out of the
      probe header, and the compiler refused its own one: %s"""
      info = infoSpec % (
          self.getClassName(), partName, kept['refused'][partName])
      raise LookupError(' '.join(info.split()))
    return kept['own'].get(partName, kept['path'])

  def _makeProbeHeaders(self, kept: Dict[str, Any]) -> None:
    """Makes the probe headers 'getProbeHeader' gives, and keeps them
    with what the compiler said of the parts left out."""
    tree = self.getDependencyTree()
    lines = []  # type: List[Tuple[str, str]]
    headerReaders = tree.getHeaderReaders()
    held = dict()  # type: Dict[str, str]
    for headerReader in headerReaders:
      partName = headerReader.getPartName()
      partFolder = headerReader.getPartFolder()
      if os.path.isfile(os.path.join(partFolder, partName)):
        held[partName] = '#include <%s/%s>' % (partName, partName)
        lines.append((partName, held[partName]))
    folder = tempfile.mkdtemp(
        prefix='probe_header_', dir=headerReaders[0].getWorkFolder())
    Finalize(
        None, shutil.rmtree, args=(folder,),
        kwargs=dict(ignore_errors=True), exitpriority=0)
    leftOut = dict()  # type: Dict[str, str]
    while True:
      said, blamed = self._compileProbeHeader(folder, 'probe', lines, '')
      if said is None:
        break
      blamed = {number for number in blamed if number <= len(lines)}
      if not blamed:
        infoSpec = """The compiler refused to make the precompiled
        header the settling compiles start from: %s"""
        info = infoSpec % said[:800]
        raise RuntimeError(' '.join(info.split()))
      for number in sorted(blamed, reverse=True):
        partName = lines.pop(number - 1)[0]
        leftOut[partName] = said[:600]
    own, refused = dict(), dict()  # type: Dict[str, str], Dict[str, str]
    #  A part left out, and a part whose folders come in its own order,
    #  as QtGraphs, whose 'private/qabstractseries_p.h' is its own and
    #  not that of QtCharts; see 'HeaderReader.getOwnOrderParts'.
    apart = [
        *leftOut, *(
            name for name in sorted(HeaderReader.getOwnOrderParts())
            if name in held and name not in leftOut)]

    def makeOwn(partName: str) -> Tuple[str, Optional[str]]:
      """Makes the probe header of one part and every part it needs,
      those first, as Qt's own build reads them for the part."""
      needed, at = [partName], 0
      while at < len(needed):
        try:
          needs = HeaderFolder.getPartNeeds(needed[at])
        except LookupError:
          needs = ()
        needed.extend(need for need in needs if need not in needed)
        at += 1
      ownLines = [
          (one, held[one]) for one in reversed(needed) if one in held]
      said, _ = self._compileProbeHeader(
          folder, 'probe_%s' % partName, ownLines, partName)
      return partName, said

    with ThreadPoolExecutor(os.cpu_count() or 1) as pool:
      for partName, said in pool.map(makeOwn, apart):
        if said is None:
          own[partName] = os.path.join(folder, 'probe_%s.pch' % partName)
        else:
          refused[partName] = said[:600]
    for partName, said in refused.items():
      for className in tree[partName]:
        tree.addMissedClass(
            '%s::%s' % (partName, className),
            'its part is left out of the probe header, and the compiler '
            'refused its own one: %s' % said)
    kept['left out'] = leftOut
    kept['own'] = own
    kept['refused'] = refused
    kept['path'] = os.path.join(folder, 'probe.pch')

  def _compileProbeHeader(
      self,
      folder: str,
      stem: str,
      lines: List[Tuple[str, str]],
      partName: str,
  ) -> Tuple[Optional[str], Set[int]]:
    """Writes the lines into '<stem>.h' in the folder and makes
    '<stem>.pch' of it, with the folders of the part of that name, or of
    the first part of the tree for ''. Gives None when the compiler made
    it; else what it said, and the numbers of the lines it blamed."""
    headerFile = os.path.join(folder, '%s.h' % stem)
    with open(headerFile, 'w') as file:
      file.write('%s\n' % '\n'.join(line for _, line in lines))
    command = (
        *self._getProbeCommand(partName), '-fpch-instantiate-templates',
        '-x', 'c++-header', headerFile,
        '-o', os.path.join(folder, '%s.pch' % stem),
    )
    done = subprocess.run(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        universal_newlines=True)
    if not done.returncode:
      return None, set()
    said = ' '.join(done.stderr.split())
    return said, self._findBlamedLines(done.stderr, '%s.h' % stem)

  def getLeftOutParts(self) -> Dict[str, str]:
    """
    Gives the parts 'getProbeHeader' left out of the header of every
    part, each with what the compiler said of it; an empty dict when it
    left out none. Makes the probe headers when they are not made yet.
    """
    kept = self.getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    return dict(kept['left out'])

  def getRefusedParts(self) -> Dict[str, str]:
    """
    Gives the parts left out whose own probe header the compiler
    refused as well, each with what it said: their classes are not
    written. Makes the probe headers when they are not made yet.
    """
    kept = self.getDependencyTree().getKept('probe header')
    if 'path' not in kept:
      self._makeProbeHeaders(kept)
    return dict(kept['refused'])

  @staticmethod
  def _findBlamedLines(said: str, fileName: str) -> Set[int]:
    """
    Gives the numbers of the lines of the file of that name that an
    error the compiler printed stands under: the line the error is on,
    or the line of the file the header holding the error was included
    from. The lines a note or a warning stands under are not taken.

    The compiler prints the files a header was included from only when
    they are not those of the message before, so a message without
    them stands under those of the message before.
    """
    blamed, chain = set(), set()  # type: Set[int], Set[int]
    inStack = False
    #  The path before the name ends in '/', or in '\' on Windows.
    place = re.compile(r'(?:^|[/\\])%s:(\d+):' % re.escape(fileName))
    for line in said.splitlines():
      stripped = line.strip()
      if stripped.startswith(('In file included from', 'from ')):
        if not inStack:
          chain, inStack = set(), True
        chain.update(int(number) for number in place.findall(stripped))
        continue
      inStack = False
      if ': error: ' in stripped or ': fatal error: ' in stripped:
        here = place.search(stripped.split(' ')[0])
        if here:
          blamed.add(int(here.group(1)))
        else:
          blamed.update(chain)
    return blamed

  def _probeText(
      self,
      text: str,
  ) -> Tuple[Dict[int, str], Dict[str, Set[str]], Set[str]]:
    """
    Compiles the text of a ritual file, joining nothing, and says what
    came of it. The compile starts from the precompiled header of
    'getProbeHeader', and ends at the text the compiler would make an
    object file of: see '_readCompilerText'.

    Returns
    -------

    Tuple
      What the compiler refused: for each line it complained of, what
      it said. Then, when it refused nothing: for each name the
      compiled file defines, the names its code leans on directly; and
      the names the compiled file needs from elsewhere.
    """
    with tempfile.TemporaryDirectory() as folder:
      probeFile = os.path.join(folder, 'probe.cpp')
      compiledFile = os.path.join(folder, 'probe.ll')
      with open(probeFile, 'w') as file:
        file.write(text)
      command = (
          *self._getProbeCommand(self._getProbePart()), '-S', '-emit-llvm',
          '-include-pch', self.getProbeHeader(), probeFile,
          '-o', compiledFile,
      )
      done = subprocess.run(
          command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
          universal_newlines=True)
      if done.returncode:
        #  Each thing the compiler refuses, with the first line of the
        #  file it names for it: the line of the error itself, or,
        #  where the error lies in a header of Qt, the line of the
        #  file that the compiler says asked for it.
        refused = dict()  # type: Dict[int, str]
        error = re.compile(r':\d+:\d+: (?:fatal )?error: (.*)')
        place = re.compile(r'probe\.cpp:(\d+):\d+: ')
        pulled = re.compile(r'In file included from .*probe\.cpp:(\d+)')
        #  What the compiler said last and has no line of ours for yet,
        #  with the line that pulled in the file it lies in.
        waiting = [None, None]  # type: List[Any]
        asked = None  # type: Optional[int]

        def settle() -> None:
          """What is waiting goes to the line that pulled its file in,
          when the compiler named no line of ours after it."""
          if waiting[0] is not None and waiting[1] is not None:
            refused.setdefault(waiting[1], waiting[0])
          waiting[0], waiting[1] = None, None

        for line in done.stderr.split('\n'):
          #  Above an error in a file that was pulled in, the compiler
          #  names the line of ours that pulled it in.
          through = pulled.search(line)
          if through is not None:
            settle()
            asked = int(through.group(1))
            continue
          match = error.search(line)
          if match is not None:
            settle()
            waiting[0], waiting[1] = match.group(1), asked
            asked = None
          where = place.search(line)
          if waiting[0] is not None and where is not None:
            #  The error itself, or a note under it, names a line of
            #  ours: that line is nearer than the one pulling a file in.
            refused.setdefault(int(where.group(1)), waiting[0])
            waiting[0], waiting[1] = None, None
        settle()
        if not refused:
          refused[0] = ' '.join(done.stderr.split())[:400]
        return refused, dict(), set()

      with open(compiledFile, encoding='utf-8') as file:
        leans, wanted = self._readCompilerText(file.read())
      return dict(), leans, wanted

  def _settleSource(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> None:
    """
    Decides which functions get their code from Qt's own source, keeps
    that code for 'getSourceText', and takes out every ritual that
    leans on something that cannot be had.

    It does so for a class that has a function '_findReason' let
    through though it cannot be called, for a class of a header Qt
    calls private, and for a class Qt marks nowhere. The whole ritual
    file is compiled to an object file, against the header files made
    from Qt's source. For each
    ritual it is then looked up what its code leans on, through
    everything the object file holds itself. What Qt's source marks
    for use from outside Qt is fine; see '_isMarkedName'. For anything
    else, Qt's source is asked for a definition, which is then taken
    along. A ritual leaning on something that cannot be had that way,
    as the table through which C++ looks functions up in an object of
    a class Qt keeps to itself, is moved from 'written' to
    'unwritten', with what stood in the way.

    Raises
    ------

    RuntimeError
      The compiler refuses the file for something that is no code
      taken from Qt's source and no line pulling a file in for it: a
      ritual itself does not compile. The message holds what it said.
    """
    self.__source_text__, self.__source_includes__ = '', ()
    self.__unwritten_extras__ = []
    self.__pulled_first__ = ()
    tree = self.getDependencyTree()
    source = tree.getSourceReader()
    if source is None:
      return
    className = self.getClassName()
    record = self._readRecord(className)
    chosen = dict()  # type: Dict[str, Record]
    for member in record.get('inner', ()):
      if member.get('kind') not in self.__function_kinds__:
        continue
      if 'mangledName' not in member or self._canBeCalled(member):
        continue
      definition = self._findSourceCode(member)
      if definition is not None:
        chosen[member['mangledName']] = definition
    headerReader = self.getHeaderReader()
    private = False
    if headerReader.hasPrivate():
      headerPath = tree.getHeaderPath(className, self.getPartName())
      private = any(
          headerPath.startswith(folder)
          for folder in headerReader.getApartFolders())
    named = self._nameWritten(written)
    #  A class Qt marks nowhere, neither itself nor a class it is
    #  written inside, as 'QOpenGLFunctions_1_0_CoreBackend': Qt's
    #  library offers none of its functions, and code of it in a header
    #  file may call one of them, as its constructor calls 'init()'.
    parts = className.split('::')
    unmarked = not any(
        self._isMarkedForExport('::'.join(parts[:count]))
        for count in range(len(parts), 0, -1))
    if not private and not unmarked and not any(
        name in named for name in chosen):
      #  No ritual calls a function whose code would be taken, so
      #  there is nothing to compile for: every ritual calls what Qt's
      #  source marks or what a header has the code of.
      return
    helpers = dict()  # type: Dict[str, Record]
    lost = set()  # type: Set[str]
    marker = '//  ' + '-' * 71
    #  What the code of each ritual leans on, by the name of the ritual,
    #  as the last round found it.
    reachedBy = dict()  # type: Dict[str, Set[str]]

    def drop(plan: Record, reason: str) -> None:
      written.remove(plan)
      if plan['kind'] in self.__ours_only__:
        #  A ritual of ours, as the one running just Qt's own function:
        #  no function of the header by itself, so kept apart.
        self.__unwritten_extras__.append((plan['function'], reason))
      else:
        unwritten.append((plan['function'], reason))

    for _ in range(60):
      #  One round: write the file as it would be, compile it, look at
      #  what each ritual leans on. A round that changes nothing is
      #  the last.
      named = self._nameWritten(written)
      taken = [*helpers.items()]
      taken.extend(
          (name, definition) for name, definition in chosen.items()
          if name in named and name not in helpers)
      compiled = {*helpers}
      self._keepSource(taken, lost, marker)
      self.__written_rituals__ = (*written,)
      self.__unwritten_functions__ = (*unwritten,)
      text = self.getRitualText()
      self.__written_rituals__ = None
      self.__unwritten_functions__ = None
      refused, leans, wanted = self._probeText(text)
      lines = text.split('\n')
      changed = False
      if refused:
        #  Which line belongs to what: a line pulling a file in, a
        #  definition taken from Qt's source, or a ritual.
        starts = []  # type: List[Tuple[int, str]]
        for number, line in enumerate(lines, 1):
          match = re.match(r'//  from (\S+), line \d+, as (\S+)$', line)
          if match is not None:
            starts.append((number, match.group(2)))
        ends = lines.index(marker) + 1 if marker in lines else 0
        for lineNumber, said in sorted(refused.items()):
          line = ''
          if 0 < lineNumber <= len(lines):
            line = lines[lineNumber - 1]
          pulled = self.__source_includes__
          squeezed = ''.join(line.split())
          if squeezed.startswith('#include') and line in pulled:
            lost.add(line)
            changed = True
            continue
          owner = None  # type: Optional[str]
          if lineNumber <= ends:
            for number, name in starts:
              if number <= lineNumber:
                owner = name
          if owner is None:
            continue
          infoSpec = """Qt's library has no name for it, and its code in
          Qt's source does not compile apart from its file: %s"""
          reason = ' '.join((infoSpec % said).split())
          if owner in helpers:
            del helpers[owner]
            lost.add(owner)
            changed = True
          elif owner in chosen:
            for plan in [*written]:
              if plan.get('ritualName', '')[len('ritual'):] == owner:
                drop(plan, reason)
            del chosen[owner]
            changed = True
        if not changed:
          #  A header file of Qt that does not stand alone, as
          #  'qdbusthreaddebug_p.h', names a class it leaves to the
          #  file pulling it in to declare. Qt's own '.cpp' files pull
          #  the header file of that class in first; so does this one.
          unknown = re.compile(
              r"(?:unknown type name|incomplete type|undeclared "
              r"identifier) '([A-Za-z_][\w:]*)'")
          for said in refused.values():
            for name in unknown.findall(said):
              known = tree.hasClass(name, self.getPartName())
              if known and name != className and (
                  name not in self.__pulled_first__):
                self.__pulled_first__ = (*self.__pulled_first__, name)
                changed = True
          if changed:
            continue
        if not changed:
          #  The compiler refuses the file for something that is none
          #  of the code taken along. Written like this it would not
          #  compile anywhere, so nothing is written.
          infoSpec = """The compiler refuses the ritual file of '%s' as
          it would be written, for what no code taken from Qt's source
          is to blame: %s"""
          shown = '; '.join(
              'line %d: %s' % pair for pair in sorted(refused.items()))
          info = infoSpec % (className, shown[:600])
          raise RuntimeError(' '.join(info.split()))
        continue
      #  What the code leans on is sorted by Qt's source: a thing Qt
      #  marks for use from outside Qt, and writes so that it can be
      #  called from there, can be called. Of anything else the code
      #  is taken along as well, or the ritual goes. No Qt that is
      #  compiled or installed is asked which names it has.
      shownNames = self._demangle(sorted(
          symbol for symbol in wanted if self._isOfQt(symbol)))
      marked = {
          symbol for symbol, shown in shownNames.items()
          if self._isMarkedName(shown, symbol)
      }
      for plan in [*written]:
        ritualName = plan.get('ritualName')
        if ritualName not in leans:
          continue
        reached, waiting = set(), [ritualName]
        while waiting:
          for other in leans.get(waiting.pop(), ()):
            if other not in reached:
              reached.add(other)
              waiting.append(other)
        reachedBy[ritualName] = reached
        for symbol in sorted(reached):
          if symbol not in wanted:
            continue
          if symbol in marked or not self._isOfQt(symbol):
            continue
          found = None
          if symbol in helpers and symbol not in compiled:
            #  Found for a ritual higher up, in this very round.
            continue
          if symbol in helpers:
            #  Its code was in the file that was compiled, and the name
            #  is still not there: what Qt's source has under it is
            #  another function. It is not taken a second time.
            del helpers[symbol]
            lost.add(symbol)
          elif symbol not in lost:
            found = self._findHelper(symbol)
          if found is not None:
            helpers[symbol] = found
            changed = True
            continue
          said = subprocess.run(
              (*Machine.getDemangler(), symbol), stdout=subprocess.PIPE,
              universal_newlines=True).stdout.strip()
          infoSpec = """leans on '%s', which Qt's source does not
          mark for use from outside Qt and has no code for that could
          be taken"""
          drop(plan, ' '.join((infoSpec % said).split()))
          changed = True
          break
      if not changed:
        break
    named = self._nameWritten(written)
    taken = [*helpers.items()]
    taken.extend(
        (name, definition) for name, definition in chosen.items()
        if name in named and name not in helpers)
    self._keepSource(taken, lost, marker)
    #  A ritual that calls code taken from Qt's source stands between
    #  the '#if' lines that code stands between in its '.cpp' file as
    #  well: where they do not hold, the code is not there to call.
    copied = dict(taken)
    for plan in written:
      if 'bare' not in plan:
        continue
      leaning = [plan.get('compilerName', '')]
      leaning.extend(sorted(reachedBy.get(plan['ritualName'], ())))
      conditions = (*plan['conditions'],)
      for symbol in leaning:
        if symbol not in copied:
          continue
        definition = copied[symbol]
        for condition in self._findCopiedConditions(definition):
          if condition not in conditions:
            conditions = (*conditions, condition)
      if conditions != plan['conditions']:
        plan['conditions'] = conditions
        plan['text'] = self._wrapInConditions(plan['bare'], conditions)

  def _findCopiedConditions(self, definition: Record) -> Tuple[str, ...]:
    """
    Gives what the '#if' lines around a definition taken from Qt's
    source ask, as 'SourceReader.getConditions' reads them; and, when
    the code itself has '#if' lines that ask for a system or for a
    processor, as '#ifdef Q_OS_MACOS' in
    'QToolBarLayout::updateMacBorderMetrics()', the system and the
    processor the generator checked it for, as 'defined(Q_OS_LINUX)'.
    Elsewhere those lines let in code the compiler here never saw,
    which may call what Qt's library there does not offer, as that one
    calls 'qt_mainwindow_layout' on macOS.
    """
    found = SourceReader.getConditions(
        definition['path'], definition['line'])
    text = definition['text']
    if self.__system_asked__.search(text):
      found = (*found, self._getCheckedSystem())
    if self.__processor_asked__.search(text):
      found = (*found, self._getCheckedProcessor())
    return found

  @staticmethod
  def _getCheckedSystem() -> str:
    """Gives what the compiler knows the system by that the generator
    checks its code for, the one it runs on, as 'defined(Q_OS_LINUX)'.
    """
    systems = dict(
        Linux='defined(Q_OS_LINUX)', Darwin='defined(Q_OS_DARWIN)',
        Windows='defined(Q_OS_WIN)')
    system = platform.system()
    if system not in systems:
      infoSpec = """The generator checks code for the system it runs on,
      and knows no name of the compiler for '%s'."""
      raise NotImplementedError(' '.join((infoSpec % system).split()))
    return systems[system]

  @staticmethod
  def _getCheckedProcessor() -> str:
    """Gives what the compiler knows the processor by that the
    generator checks its code for, the one it runs on, as
    'defined(Q_PROCESSOR_X86_64)'."""
    processors = dict(
        x86_64='defined(Q_PROCESSOR_X86_64)',
        AMD64='defined(Q_PROCESSOR_X86_64)',
        aarch64='defined(Q_PROCESSOR_ARM_64)',
        arm64='defined(Q_PROCESSOR_ARM_64)')
    processor = platform.machine()
    if processor not in processors:
      infoSpec = """The generator checks code for the processor it runs
      on, and knows no name of the compiler for '%s'."""
      raise NotImplementedError(' '.join((infoSpec % processor).split()))
    return processors[processor]

  @staticmethod
  def _nameWritten(written: List[Record]) -> Set[str]:
    """Gives the name the compiler has for the function each ritual
    calls: the name of the ritual without 'ritual' in front."""
    return {
        plan.get('ritualName', '')[len('ritual'):] for plan in written
    }

  def _keepSource(
      self,
      taken: List[Tuple[str, Record]],
      lost: Set[str],
      marker: str,
  ) -> None:
    """Writes the code taken from Qt's source, with its heading, and
    the lines pulling in what it needs, where 'getSourceText' and
    'getSourceIncludes' find them."""
    self.__source_text__, self.__source_includes__ = '', ()
    if not taken:
      return
    folder = self.getDependencyTree().getSourceReader().getSourceFolder()
    lines = [
        "//  Qt's own code, from here to the line of dashes: taken from",
        "//  Qt's source, because Qt's library carries it under no name.",
        '//  Copyright (C) The Qt Company Ltd. It is licensed',
        '//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so',
        '//  here. Each function is as Qt wrote it, with the word',
        "//  'inline' put before it where Qt did not write it.",
    ]
    kept, seen = [], set()  # type: List[str], Set[str]
    for name, definition in taken:
      where = os.path.relpath(definition['path'], folder)
      lines.append('')
      lines.append('//  from %s, line %d, as %s' % (
          where, definition['line'], name))
      text = definition['text']
      if not re.search(r'\binline\b', text.split('(')[0]):
        text = 'inline %s' % text
      #  Between the '#if' lines it stands between in its '.cpp' file.
      lines.append(self._wrapInConditions(
          text, self._findCopiedConditions(definition)))
      if definition['path'] in seen:
        continue
      #  The lines of each file once, whole and in their order: an
      #  '#if' among them has its '#endif' among them.
      seen.add(definition['path'])
      #  Each as the part of the '.cpp' file sees it, and only once it
      #  is spelled so can it be told whether the compiler refused it.
      spelled = (
          self._spellInclude(line, definition['path'])
          for line in definition['includes'])
      kept.extend(line for line in spelled if line not in lost)
    lines.append(marker)
    self.__source_text__ = '\n'.join(lines)
    self.__source_includes__ = (*kept,)

  def _spellInclude(self, line: str, sourcePath: str) -> str:
    """
    Gives a line of a '.cpp' file of Qt's source that pulls a header
    file in by a name no part is named in, as '#include
    <private/qaction_p.h>' in QtWidgets' 'qmenu.cpp', with the part
    named that has the file, as the part of the '.cpp' file sees it:
    '#include <QtGui/private/qaction_p.h>'. Qt's own build looks in the
    folders of the part itself and of the parts it needs, the nearest
    first; a ritual file is compiled with the folders of every part,
    where QtWidgets would find Qt3DInput's 'qaction_p.h' first. Any
    other line comes back as it is: one naming its part already, one
    of no header file of the parts it sees, and one that is no
    '#include'.
    """
    match = re.match(
        r'^(\s*#\s*include\s*)[<"]([^>"]+)[>"](.*)$', line)
    if match is None:
      return line
    lead, name, rest = match.groups()
    if re.match(r'^Qt\w*/', name):
      return line
    folder = HeaderReader.getHeaderFolder()
    partName = folder.getPartOfPath(sourcePath)
    if partName is None:
      return line
    made, version = folder.getFolder(), HeaderReader.getQtVersion()
    for seen in HeaderReader.getNeededParts(partName):
      inner = os.path.join(made, seen, version, seen)
      if '/' in name:
        #  As 'private/qaction_p.h' or 'qpa/qplatformwindow.h'.
        candidates = [(os.path.join(inner, name), name)]
      elif name.endswith('_p.h'):
        candidates = [(
            os.path.join(inner, 'private', name), 'private/%s' % name)]
      else:
        candidates = [(os.path.join(made, seen, name), name)]
      for path, spelled in candidates:
        if os.path.isfile(path):
          return '%s<%s/%s>%s' % (lead, seen, spelled, rest)
    return line

  def _findHelper(self, symbol: str) -> Optional[Record]:
    """
    Gives the definition, in Qt's source, of a function known only by
    the name the compiler made for it, or None when the source has not
    exactly one that takes as many arguments.
    """
    source = self.getDependencyTree().getSourceReader()
    said = subprocess.run(
        (*Machine.getDemangler(), symbol), stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True).stdout.strip()
    if '(' not in said or said == symbol:
      return None
    name = said[:said.index('(')].strip()
    inside = said[said.index('(') + 1:said.rindex(')')]
    count = len(source._splitArguments(inside))
    const = said.rstrip().endswith('const')
    #  The code of a function of a class is in the source of the part
    #  that has the class, as the part of the generator sees it: two
    #  parts may each have a class by one name, as QtGraphs and
    #  QtDataVisualization each a 'QBar3DSeriesPrivate', whose functions
    #  the compiler names alike. Of a function of no class the tree
    #  knows, the part and the parts it needs are looked in, the
    #  nearest first.
    tree = self.getDependencyTree()
    seenFrom = self.getPartName()
    owner = name.rpartition('::')[0]
    if owner and tree.hasClass(owner, seenFrom):
      partNames = (tree.getClassKey(owner, seenFrom)[0],)
    else:
      partNames = tree.getNeededParts(seenFrom)
    for partName in partNames:
      found = [
          definition for definition
          in source.findDefinitions(partName, name)
          if len(definition['arguments']) == count
          and definition['const'] == const
      ]
      if len(found) == 1:
        return found[0]
    return None

  def _isMarkedForExport(self, className: str) -> bool:
    """
    Says whether Qt marks a class for export on its own, as in
    'class Q_CORE_EXPORT QObject'. A class the tree does not know
    counts as not marked.

    It matters for a class written inside another. Qt's library for
    Linux and for macOS offers the functions of such a class when the
    class around it is marked. Qt's library for Windows offers them
    only when the class is marked itself.
    """
    tree = self.getDependencyTree()
    try:
      classKey = self._keyOf(className)
    except LookupError:
      return False
    kept = tree.getKept('export marks')
    try:
      return kept[classKey]
    except KeyError:
      pass
    record = self._readRecord(className)
    marked = any(
        isinstance(child, dict) and child.get('kind') == 'VisibilityAttr'
        for child in record.get('inner', ()))
    kept[classKey] = marked
    return marked

  def _getMarkedSymbols(self) -> FrozenSet[str]:
    """
    Gives the compiler's own name of everything Qt marks for use from
    outside Qt, as the compiler wrote the mark down when it read Qt's
    header files.

    Taken are a function or a value carrying a word such as
    'Q_CORE_EXPORT' itself, a function Qt writes inside a class with
    'friend' in front and such a word, and every function and value of
    a class, or of an instance of a template, that carries one, as
    'extern template struct Q_CORE_EXPORT
    QMetaTypeInterfaceWrapper<bool>'. A class written inside a marked
    class adds its own only where it is marked itself. The compiler has
    written out Qt's shorthands by then, so a mark made through one, as
    'QT_DECLARE_EXPORTED_QT_LOGGING_CATEGORY', counts as well. The
    names are kept as '_sameFunction' compares them. Kept on the tree
    after the first call; call it once before handing the tree to
    other processes, and they all start from it.
    """
    tree = self.getDependencyTree()
    kept = tree.getKept('marked symbols')
    if 'names' in kept:
      return kept['names']
    found, declared = set(), set()  # type: Set[str], Set[str]
    recordKinds = ('CXXRecordDecl', 'ClassTemplateSpecializationDecl')

    def walk(node: Any, inMarked: bool) -> None:
      """Takes the names of one record and of what it holds."""
      if not isinstance(node, dict):
        return
      kind = node.get('kind', '')
      marked = self._hasMark(node)
      if 'mangledName' in node:
        declared.add(self._plainSymbol(node['mangledName']))
        if marked or inMarked:
          found.add(self._plainSymbol(node['mangledName']))
      if kind in recordKinds:
        inner = marked
      elif kind in ('FriendDecl', 'NamespaceDecl', 'LinkageSpecDecl'):
        inner = False
      else:
        inner = inMarked
      for child in node.get('inner', ()) or ():
        walk(child, inner)

    for headerReader in tree.getHeaderReaders():
      for headerFile in headerReader.getHeaderFiles():
        if not headerFile.wasRead() or not headerFile.getRecordCount():
          #  Refused by the compiler, or holding no records.
          continue
        #  Read one record at a time and keep none: the records of all
        #  the parts together are more than a process should hold.
        with open(headerFile.getRecordPath()) as file:
          for line in file:
            walk(json.loads(line), False)
    kept['names'] = frozenset(found)
    kept['declared'] = frozenset(declared)
    return kept['names']

  def _getDeclaredSymbols(self) -> FrozenSet[str]:
    """
    Gives the compiler's own name of everything Qt's header files
    declare, marked or not, kept as '_sameFunction' compares them.
    Found by the same reading as '_getMarkedSymbols', and kept on the
    tree with those.
    """
    kept = self.getDependencyTree().getKept('marked symbols')
    if 'declared' not in kept:
      self._getMarkedSymbols()
    return kept['declared']

  @staticmethod
  def _plainSymbol(symbol: str) -> str:
    """
    Gives a name the compiler made with the mark of the kind of
    constructor or destructor taken out. The compiler makes two names
    for one constructor, ending its name with 'C1' or 'C2', and three
    for one destructor, 'D0', 'D1' and 'D2'; a record has the first.
    """
    symbol = re.sub(r'C[123](?=E)', 'C1', symbol)
    return re.sub(r'D[012](?=E)', 'D1', symbol)

  @staticmethod
  def _hasMark(member: Record) -> bool:
    """Says whether the compiler wrote down Qt's mark for use from
    outside Qt on a function itself, as 'Q_CORE_EXPORT'."""
    return any(
        isinstance(child, dict) and child.get('kind') == 'VisibilityAttr'
        for child in member.get('inner', ()))

  def _sameFunction(self, first: str, second: str) -> bool:
    """Says whether two names the compiler made stand for one function;
    see '_plainSymbol'."""
    return self._plainSymbol(first) == self._plainSymbol(second)

  def _isMarkedName(self, shown: str, symbol: str) -> bool:
    """
    Says whether Qt's source marks, for use from outside Qt, the thing
    a name of the compiler stands for, and writes it so that it can be
    called from there.

    A function of a class is marked when the class itself is, or the
    function. The class is that very class: one written inside a
    marked class with no mark of its own is not marked. What the
    compiler makes for a class, as its table of virtual functions,
    goes with the class. A function made from a template is not
    marked: its code is in a header file or nowhere. Anything else is
    marked when the compiler wrote Qt's mark down on it, as
    '_getMarkedSymbols' has them: a function outside of every class, a
    friend, a value of an instance of a template. A marked function
    that Qt writes 'inline' with its code in no header file counts as
    not marked: see '_isWrittenInline'.

    Parameters
    ----------

    shown : str
      The name as C++ writes it, with what a function takes, as
      'c++filt' gives it.

    symbol : str
      The same name as the compiler made it.
    """
    for start in self.__made_for_class__:
      if shown.startswith(start):
        className = shown[len(start):].split('<')[0].strip()
        return self._isMarkedForExport(className)
    for start in self.__made_for_function__:
      if shown.startswith(start):
        shown = shown[len(start):]
    head, end = shown, shown.rfind(')')
    if end >= 0:
      depth, start = 0, -1
      for index in range(end, -1, -1):
        letter = shown[index]
        depth += 1 if letter == ')' else -1 if letter == '(' else 0
        if depth == 0:
          start = index
          break
      if start < 0:
        return False
      head = shown[:start]
    #  What stands before the name: the type a function made from a
    #  template gives.
    depth, cut = 0, 0
    for index, letter in enumerate(head):
      depth += 1 if letter == '<' else -1 if letter == '>' else 0
      if letter == ' ' and depth == 0:
        cut = index + 1
    name, parts, depth, last = head[cut:], [], 0, 0
    for index, letter in enumerate(name):
      depth += 1 if letter == '<' else -1 if letter == '>' else 0
      if depth == 0 and name[index:index + 2] == '::':
        parts.append(name[last:index])
        last = index + 2
    parts.append(name[last:])
    if '<' in parts[-1] and 'operator' not in parts[-1]:
      return False
    className = '::'.join(part.split('<')[0] for part in parts[:-1])
    bare = parts[-1].split('<')[0]
    markedSymbol = self._plainSymbol(symbol) in self._getMarkedSymbols()
    if not className or className not in self._getKnownNames():
      return markedSymbol
    try:
      record = self._readRecord(className)
    except (ValueError, LookupError):
      return markedSymbol
    members = [
        member for member in record.get('inner', ())
        if isinstance(member, dict) and member.get('name') == bare
    ]
    if not markedSymbol and not self._isMarkedForExport(className):
      if not any(self._hasMark(member) for member in members):
        return False
    for member in members:
      if self._sameFunction(member.get('mangledName', ''), symbol):
        return not self._isWrittenInline(className, member)
    return True

  @staticmethod
  def _demangle(symbols: List[str]) -> Dict[str, str]:
    """Gives each name the compiler made as C++ writes it, by one run
    of 'c++filt' for all of them."""
    if not symbols:
      return dict()
    said = subprocess.run(
        Machine.getDemangler(), input='\n'.join(symbols),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, universal_newlines=True).stdout
    return dict(zip(symbols, said.split('\n')))

  def _isMarked(self, member: Record) -> bool:
    """
    Says whether Qt's source marks a function of the class for use
    from outside Qt: the function carries a word such as
    'Q_CORE_EXPORT' itself, or the class it belongs to does.

    The class it belongs to is that very class. A class written inside
    a marked class, with no mark of its own, counts as not marked:
    only then does every system agree that the function is there.
    """
    if self._hasMark(member):
      return True
    return self._isMarkedForExport(self.getClassName())

  def _canBeCalled(self, member: Record) -> bool:
    """
    Says whether a ritual can call this function of Qt, going by Qt's
    source alone. No Qt that is compiled or installed is looked at.

    A function can be called in three cases. Its code is written in a
    header file, so the compiler of each machine makes it where the
    ritual is compiled. Or it is virtual, so it is found through the
    object it is called on. Or Qt's source marks it, or the class it
    belongs to, for use from outside, and writes its code so that it
    can be called from there; see '_isMarked' and
    '_isWrittenToBeCalled'. Any other function has no name by which
    anything outside Qt could reach it, and a ritual for it has to
    carry a copy of its code.

    A few functions Qt declares only to have the compiler check
    something, and writes no code for anywhere, as
    'QEvent::qt_check_for_QGADGET_macro()'. They cannot be called
    whatever they are marked.

    Parameters
    ----------

    member : Record
      What the compiler wrote down about the function, with its own name
      for it under 'mangledName'.
    """
    tree = self.getDependencyTree()
    if member.get('name', '').startswith(self.__never_written__):
      return False
    name = member['mangledName']
    if member.get('virtual') or tree.hasBody(member):
      return True
    if tree.isDefined(name, self.getPartName()):
      return True
    if not self._isMarked(member):
      return False
    return self._isWrittenToBeCalled(member)

  def _isWrittenToBeCalled(self, member: Record) -> bool:
    """
    Says whether Qt's source writes the code of a marked function of
    the class in a way that lets it be called from outside Qt.

    Two things in the source say no, whatever the mark. Qt writes code
    for the function nowhere: it only declares it, as it declares the
    constructor of 'QStandardPaths' so that nobody can make one. Or
    Qt writes it 'inline' with its code in no header file; see
    '_isWrittenInline'.

    The source is asked under every name C++ code can give the class,
    as 'DependencyTree.getSpellings' has them: Qt writes the code of
    'QLatin1String::compare_helper' as 'QLatin1StringView::...'. A
    constructor or destructor is named after the class as spelled.
    Without Qt's source at hand the mark alone decides.
    """
    if member.get('kind') == 'FunctionDecl':
      #  A function outside of every class, which Qt wrote inside the
      #  class with 'friend' in front: it has no class in its name.
      return True
    tree = self.getDependencyTree()
    source = tree.getSourceReader()
    if source is None:
      return True
    className, partName = self.getClassName(), self.getPartName()
    name, kind = member.get('name', ''), member.get('kind', '')
    for spelled in tree.getSpellings(className, partName):
      last = spelled.rpartition('::')[2]
      if kind == 'CXXConstructorDecl':
        asked = '%s::%s' % (spelled, last)
      elif kind == 'CXXDestructorDecl':
        asked = '%s::~%s' % (spelled, last)
      else:
        asked = '%s::%s' % (spelled, name)
      if source.hasCode(partName, asked):
        break
    else:
      return False
    return not self._isWrittenInline(className, member)

  def _isWrittenInline(self, className: str, member: Record) -> bool:
    """
    Says whether Qt writes a function of a class 'inline' with its code
    in no header file. The compiler then puts the code where Qt calls
    it, and Qt's library keeps no function under its name. Qt writes
    the word in the header file, as
    'inline explicit QJsonDocument(QCborValue data);', or in front of
    the code in the '.cpp' file, as 'QCborStreamReader::preparse()'.

    Parameters
    ----------

    className : str
      The class the function belongs to.

    member : Record
      What the compiler wrote down about the function.
    """
    tree = self.getDependencyTree()
    if tree.hasBody(member):
      return False
    if tree.isDefined(member.get('mangledName', ''), self.getPartName()):
      return False
    if member.get('inline'):
      return True
    definition = self._findSourceCode(member, className)
    if definition is None:
      return False
    head = definition['text'].split('(')[0]
    return True if re.search(r'\binline\b', head) else False

  def _getLookupOrder(self) -> List[str]:
    """Gives the class of the generator and every class it is built
    on, nearest first, as C++ looks a name up: the class, the classes it
    is built on, then theirs. Kept for the class."""
    tree = self.getDependencyTree()
    className = self.getClassName()
    scopes = self.__spelling_scopes__
    if scopes is None or scopes[0] != className:
      partName = self.getPartName()
      scopes, waiting = [], [className]  # type: List[str], List[str]
      while waiting:
        name = waiting.pop(0)
        if name in scopes:
          continue
        scopes.append(name)
        for parent in tree.getParents(name, partName):
          parent = parent.split('<')[0].strip()
          if tree.hasClass(parent, partName) and parent not in scopes:
            waiting.append(parent)
      for _, name in reversed(tree.getAncestors(className, partName)):
        if name not in scopes:
          scopes.append(name)
      self.__spelling_scopes__ = scopes
    return scopes

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
    #  Nearest first, as C++ looks a name up: the class, the classes it
    #  is built on, then theirs. 'Type' in 'QGles2Buffer' is the one of
    #  'QRhiBuffer', not the one of 'QRhiResource' further down.
    scopes = self._getLookupOrder()

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
    if self._hidesPlainNew():
      barred.add('operator new')
    return barred

  def _hidesPlainNew(self) -> bool:
    """
    Says whether the nearest class declaring an 'operator new', the
    class itself or one it is built on, declares only ones that take
    more than the size. Those hide the plain one, and 'new' alone does
    not compile: the nodes of 'QQmlJS::AST' are built on
    'QQmlJS::Managed', whose 'operator new' takes a pool of memory.
    """
    for scope in self._getLookupOrder():
      try:
        record = self._readRecord(scope)
      except (ValueError, LookupError):
        continue
      sizes = [
          sum(1 for child in member.get('inner', ())
              if isinstance(child, dict)
              and child.get('kind') == 'ParmVarDecl')
          for member in record.get('inner', ())
          if isinstance(member, dict)
          and member.get('name') == 'operator new']
      if sizes:
        return 1 not in sizes
    return False

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
      if passing['kind'] in ('list', 'map'):
        #  Qt reads the list or the map at the address, and the header
        #  of what it holds has to be known for that.
        held = passing.get('listed') or passing.get('mapped')
        needs.append(held['holds'])
        takes.append((name, 'const %s *' % passing['className']))
        passed.append('*%s' % name)
      elif passing['kind'] in ('value', 'text', 'view'):
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
      if giving['kind'] in ('list', 'map'):
        #  A copy of the list or the map is made here, and its address
        #  goes back.
        held = giving.get('listed') or giving.get('mapped')
        needs.append(held['holds'])
        given = '%s *' % giving['className']
        opening, closing = 'return new %s(' % giving['className'], '));'
      elif giving['kind'] in ('value', 'text', 'view'):
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
    plan['conditions'] = self._findOwnConditions(member)
    plan['bare'] = self._writeRitual(plan, body)
    plan['text'] = self._wrapInConditions(plan['bare'], plan['conditions'])
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
    partName = self.getPartName()
    parents = tree.getParents(className, partName)
    return (*(p for p in parents[1:] if tree.hasClass(p, partName)),)

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

    That C++ marks a function 'private' or 'protected' is no such
    reason. C++ means by it that only the class itself, or a class
    built on it, may call the function. cutienator does not care: the
    rituals are compiled with '-fno-access-control', which turns that
    rule of the compiler off, and every function Qt has is taken.

    That Qt has marked a function as deprecated is no such reason. It
    gets its ritual like any other, and the compiler then passes on
    Qt's own notice of it, as 'Use territory() instead'. That notice
    is wanted: it is what a warning is for.
    """
    if member.get('explicitlyDeleted'):
      return 'forbidden: Qt declares it only to forbid its use'
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
      if self._findSourceCode(member) is None:
        infoSpec = """cannot be called and cannot be copied: no header
        file has its code, Qt's source does not mark it or its class
        for use from outside Qt or writes it 'inline' or nowhere, and
        Qt's source has no code for it that could be told from the
        rest"""
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
      One of the four setters has not been called.

    LookupError
      The tree has no class of that name, or the compiler refused to
      read the part of the class for the probe compiles
      ('getRefusedParts').
    """
    #  A class whose part the compiler refuses to read for the probe
    #  compiles is not written; see 'getProbeHeader'.
    self.getProbeHeader()
    ritualFile = self.getRitualFile()
    with open(ritualFile, 'w') as file:
      file.write(self.getRitualText())
    with open(self.getRowsFile(), 'w') as file:
      file.write(self.getRowsText())
    return ritualFile
