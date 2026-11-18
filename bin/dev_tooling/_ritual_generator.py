"""RitualGenerator writes the ritual file of one Qt class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

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
  Reasons = Tuple[Tuple[str, str], ...]


class RitualGenerator:
  """
  Writes the ritual file of one Qt class: one ritual for each function
  of the class whose types it can pass. This is the generator side of
  the tooling; 'RitualTester' is the side that verifies what it wrote.

    generator = RitualGenerator()
    generator.setDependencyTree(tree)
    generator.setClassName('QObject')
    generator.setWorkFolder('/some/folder')
    generator.write()            # writes '/some/folder/q_object.cpp'
    generator.getWritten()       # the 28 rituals in that file
    generator.getNotWritten()    # the other 52 functions, with reasons

  Terms
  -----

  - A ritual is one function of ours that Python can call, and that
    calls one Qt function. It is named 'ritual' followed by the
    compiler's own name for that Qt function.
  - A ritual file is a C++ file holding rituals.
  - To pass a type is to hand a value of it from Python to C++, or
    back.

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
    'double', also under a second name, as 'qsizetype'.
  - Text as C has it: 'const char *'.
  - Enums, as 'Qt::TimerType'.
  - Addresses of objects: 'QThread *' and 'const QObject *', for every
    class of the tree.

  What to expect
  --------------

  - Every function the header declares for the class is accounted for:
    it is in 'getWritten', or in 'getNotWritten' with the reason.
    Nothing is passed over silently. Functions the compiler makes up
    itself are no part of the header and are not counted.
  - A function is not written when it takes or gives a type that is
    not in the list above, when it is private or protected, when Qt
    forbids it, when it is a signal, or when it is a template.
  - The getters decide and write nothing. Only 'write' touches a file,
    and it replaces the ritual file whole.
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
  __written_rituals__ = None  # type: Optional[Rituals]
  __unwritten_functions__ = None  # type: Optional[Reasons]
  __known_names__ = None  # type: Optional[FrozenSet[str]]
  __offered_names__ = None  # type: Optional[FrozenSet[str]]

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
    self.__written_rituals__ = (*written,)
    self.__unwritten_functions__ = (*unwritten,)

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
      'kind': 'constructor', 'destructor', 'method' or 'static method'.
      'gives': the type the ritual gives back, as C++ writes it.
      'takes': what the ritual takes, in order, each as a name and a
      type. For a ritual on an object the first is 'self', the address
      of the object.
      'text': the C++ text of the ritual.

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

  def getRitualText(self) -> str:
    """
    Gives the whole text of the ritual file, without writing it.

    Written for you from 'getWritten': a heading, the lines pulling in
    the header file of the class, as 'QtPart.getIncludeLines' gives
    them, and then each ritual under the Qt function it calls.
    """
    qtPart = self.getQtPart()
    headerPath = self.getDependencyTree().getHeaderPath(self.getClassName())
    relative = os.path.relpath(headerPath, qtPart.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.RitualGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, qtPart.getQtVersion())
    heading = textwrap.wrap(' '.join(info.split()), 73)
    blocks = ['\n'.join('//  %s' % line for line in heading)]
    includeLines = qtPart.getIncludeLines(headerPath).rstrip('\n')
    blocks[0] = '%s\n%s' % (blocks[0], includeLines)
    blocks.extend(ritual['text'] for ritual in self.getWritten())
    return '%s\n' % '\n\n'.join(blocks)

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
    self.__known_names__ = None
    self.__offered_names__ = None

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

  def _findKind(self, cppType: str) -> str:
    """
    Says how a type is passed: 'nothing', 'number', 'text', 'enum' or
    'address'. Gives '' for a type the generator cannot pass yet.
    """
    tree = self.getDependencyTree()
    aliases = tree.getAliasTypes()
    seen = set()
    while cppType in aliases and cppType not in seen:
      seen.add(cppType)
      cppType = aliases[cppType]
    if cppType == 'void':
      return 'nothing'
    if cppType in self.__number_types__:
      return 'number'
    if cppType == 'const char *':
      return 'text'
    if cppType in tree.getEnumNames():
      return 'enum'
    if cppType.endswith(' *'):
      pointed = cppType[:-2]
      if pointed.startswith('const '):
        pointed = pointed[6:]
      if pointed in tree.getClassNames():
        return 'address'
    return ''

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

  def _planFunction(self, member: Record) -> Record:
    """
    Works out the ritual of one function of the class, whether or not
    it can be written: its name, what it takes and gives, and its text.
    """
    className = self.getClassName()
    kind = self.__function_kinds__[member['kind']]
    if kind == 'method' and member.get('storageClass') == 'static':
      kind = 'static method'
    functionType = member['type']['qualType']
    given, taken, words = self._splitFunctionType(functionType)
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
      arguments.append((name, cppType['qualType'], plain))
    shown = ', '.join(self._joinType(t, n) for n, t, _ in arguments)
    shown = '%s::%s(%s)' % (className, member['name'], shown)
    if kind in ('method', 'static method'):
      shown = self._joinType(given, shown)
    if 'const' in words:
      shown = '%s const' % shown
    passed = ', '.join(name for name, _, _ in arguments)
    #  From here on the types are for the ritual, which stands outside
    #  the class and needs every name in full.
    given = self._spellOutside(given)
    takes = [
        (name, self._spellOutside(cppType)) for name, cppType, _ in arguments
    ]
    if kind == 'constructor':
      given = '%s *' % className
      body = 'return new %s(%s);' % (className, passed)
    elif kind == 'destructor':
      given = 'void'
      takes.insert(0, ('self', '%s *' % className))
      body = 'delete self;'
    elif kind == 'static method':
      body = '%s::%s(%s);' % (className, member['name'], passed)
    else:
      const = 'const ' if 'const' in words else ''
      takes.insert(0, ('self', '%s%s *' % (const, className)))
      body = 'self->%s(%s);' % (member['name'], passed)
    if kind in ('method', 'static method') and given != 'void':
      body = 'return %s' % body
    plan = dict(
        ritualName='ritual%s' % member.get('mangledName', ''),
        function=shown, kind=kind, gives=given, takes=(*takes,),
        plainTypes=(*(plain for _, _, plain in arguments),),
        words=(*words,), variadic='...' in taken,
    )
    plan['text'] = self._writeRitual(plan, body)
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
    unknown = [
        plain for plain in plan['plainTypes'] if not self._findKind(plain)
    ]
    if plan['kind'] in ('method', 'static method'):
      if not self._findKind(plan['gives']):
        unknown.append(plan['gives'])
    if unknown:
      names = ', '.join(dict.fromkeys(unknown))
      return 'takes or gives a type that cannot be passed yet: %s' % names
    return ''

  def _writeRitual(self, plan: Record, body: str) -> str:
    """
    Gives the C++ text of one ritual, under the function it calls.

    Every ritual starts with the line 'extern "C" Q_DECL_EXPORT'. The
    first part gives it the plain name Python finds it by. The second is
    Qt's own mark for a function a shared object is to offer: Windows
    offers only what carries it, and on Linux and macOS it changes
    nothing.
    """
    shown = textwrap.wrap(plan['function'], 71) or ['']
    lines = ['//  %s' % shown[0]]
    lines.extend('//      %s' % line for line in shown[1:])
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
    lines.append('  %s' % body)
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
    Writes the ritual file of the class into the work folder, replacing
    one written before.

    Returns
    -------

    str
      The full path of the ritual file, which now exists.

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
    return ritualFile
