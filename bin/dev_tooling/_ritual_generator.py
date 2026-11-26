"""RitualGenerator writes the ritual file of one Qt class, and the rows
file that goes with it."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree, HeaderReader
from .ritual_experts import (AddressExpert, CallExpert, CharsExpert,
                             ConditionExpert, CopyExpert, CppText,
                             CuteClassExpert, DurationExpert, EnumExpert,
                             FlagsExpert, FunctionAddressExpert,
                             HeldValueExpert,
                             ListExpert, MapExpert, MetaExpert,
                             MovedExpert, NothingExpert, NullExpert,
                             NumberAddressExpert, NumberExpert,
                             ProbeExpert, RawAddressExpert, ReachExpert,
                             ReferenceExpert, RitualExpert,
                             RitualFileExpert, SpellingExpert,
                             TextsAddressExpert, TypeExpert, ValueExpert)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple, Type

  Record = Dict[str, Any]
  Rituals = Tuple[Record, ...]
  Records = Tuple[Record, ...]
  Reasons = Tuple[Tuple[str, str], ...]
  Rows = Dict[str, Tuple[str, ...]]
  Names = Tuple[str, ...]


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

  Experts
  -------

  The generator decides, for each function of the class, whether it is
  written, and hands each kind of work to an expert of
  'dev_tooling.ritual_experts', one of each kind for each generator;
  see 'getExpert'.

  - Reaching a function: the experts of '__reach_experts__' are asked
    in turn, and the first that can reach the function has it: the
    ritual calls it ('CallExpert'), or carries a copy of Qt's code for
    it ('CopyExpert'). Where none can, the reason names every way and
    why each could not.
  - Passing a type: the experts of '__type_experts__' are asked in
    turn, and the first that claims a type says how it crosses, what
    a ritual takes and hands Qt for it, and what it gives back. A type
    none claims cannot be passed yet.
  - The rest, one job each: the '#if' lines ('ConditionExpert'), names
    written in full ('SpellingExpert'), the compiler's view of a file
    ('ProbeExpert'), the C++ class of ours through which Python takes
    functions over ('CuteClassExpert'), and the text of the ritual file
    and of the rows file ('RitualFileExpert').

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

  Each kind is an expert's; its class says more.

  - Nothing: a function giving back 'void' ('NothingExpert').
  - Numbers: 'bool' and the numbers built into C++, as 'int' and
    'double', also under a second name, as 'qsizetype', and taken to
    be read only, as 'const bool' and 'const int &' ('NumberExpert').
  - A number the function may change, taken as 'int &' or 'int *'.
    The ritual takes the address of the number and hands Qt the number
    there. Giving one back is not written ('NumberAddressExpert').
  - Text as C has it: 'const char *' ('CharsExpert').
  - The texts a program was started with, 'char **'. The ritual takes
    the address of the first and hands it on. Giving such back is not
    written ('TextsAddressExpert').
  - Enums, as 'Qt::TimerType' ('EnumExpert').
  - Flags: the type Qt names for the combinations of a flags enum, as
    'Qt::WindowFlags', which C++ reads as 'QFlags<Qt::WindowType>'. The
    ritual takes and gives the number of the combination as an 'int'
    ('FlagsExpert').
  - Addresses of anything, as 'QThread *' and 'const GLfloat *'
    ('AddressExpert').
  - Lists and maps of Qt, by the address of the C++ list or map
    ('ListExpert', 'MapExpert').
  - Values: 'QSize', 'const QSize' and 'const QSize &', for every class
    of the tree C++ can copy. The ritual takes the address of one and
    hands Qt the object there, which Qt copies if it keeps it. For one
    given back, the ritual makes a copy with 'new' and gives its
    address: that copy is known to nobody else, and whoever called the
    ritual has to remove it. Text: Qt's 'QString' in each of those
    three spellings, and the two classes that look at text held
    elsewhere, 'QStringView' and 'QAnyStringView'. It is passed as a
    value of 'QString', and its word in the row is 'text', so Python
    passes a plain 'str' ('ValueExpert').
  - A value Qt may take over, 'T &&', by its address, moved to Qt
    ('MovedExpert').
  - An object Qt reads or changes where it is, 'T &', by its address
    ('ReferenceExpert').

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
  - A function is not written when it takes or gives a type no expert
    claims, when Qt forbids it, when no way reaches it, or when it is a
    template. A signal is written as any function: calling its ritual
    emits it.
  - A number that ends as 'long' on this system, under a name that
    says no width, is not written either. 'long' is 64 bits wide on
    Linux and macOS and 32 on Windows, and the row would be right on
    one of them only.
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
    """Takes apart the type the compiler writes for a function; see
    'CppText.splitFunctionType'."""
    return CppText.splitFunctionType(functionType)

  @staticmethod
  def _joinType(cppType: str, name: str) -> str:
    """Writes a type and a name the way C++ does; see
    'CppText.joinType'."""
    return CppText.joinType(cppType, name)

  @staticmethod
  def _stripReadOnly(cppType: str) -> str:
    """Gives 'int' for 'int', 'const int' and 'const int &'; see
    'CppText.stripReadOnly'."""
    return CppText.stripReadOnly(cppType)

  @staticmethod
  def getFunctionKind(recordKind: Optional[str]) -> Optional[str]:
    """Gives the kind of function a record of the compiler stands for,
    as 'constructor' for 'CXXConstructorDecl', or None for a record
    that is no function of a class."""
    return RitualGenerator.__function_kinds__.get(recordKind)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Names of numbers that a header of the system, not of Qt, gives,
  #  with the number type each stands for. The OpenGL ones are fixed by
  #  the OpenGL specification of Khronos, on every system alike, and
  #  'char16_t' and 'char32_t' are C++'s own characters of 16 and 32
  #  bits, as the numbers of '<cstdint>' have the width their names
  #  say. A function giving one names it alone, and the compiler
  #  reports no type behind it there; see '_followAliases'. A number
  #  as wide as an address, as 'GLsizeiptr' and 'ptrdiff_t', stands for
  #  'long' here, which is that wide on Linux, and so has no word: it
  #  crosses widened, as 'NumberExpert' says, right on every system.
  __system_numbers__ = {
      'GLenum': 'unsigned int', 'GLboolean': 'unsigned char',
      'GLbitfield': 'unsigned int', 'GLbyte': 'signed char',
      'GLubyte': 'unsigned char', 'GLshort': 'short',
      'GLushort': 'unsigned short', 'GLint': 'int', 'GLuint': 'unsigned int',
      'GLsizei': 'int', 'GLfloat': 'float', 'GLclampf': 'float',
      'GLdouble': 'double', 'GLclampd': 'double', 'GLchar': 'char',
      'GLfixed': 'int', 'GLhalf': 'unsigned short',
      'GLint64': 'long long', 'GLuint64': 'unsigned long long',
      'GLsizeiptr': 'long', 'GLintptr': 'long',
      'char16_t': 'unsigned short', 'char32_t': 'unsigned int',
      'int8_t': 'signed char', 'uint8_t': 'unsigned char',
      'int16_t': 'short', 'uint16_t': 'unsigned short',
      'int32_t': 'int', 'uint32_t': 'unsigned int',
      'int64_t': 'long long', 'uint64_t': 'unsigned long long',
      'std::int8_t': 'signed char', 'std::uint8_t': 'unsigned char',
      'std::int16_t': 'short', 'std::uint16_t': 'unsigned short',
      'std::int32_t': 'int', 'std::uint32_t': 'unsigned int',
      'std::int64_t': 'long long', 'std::uint64_t': 'unsigned long long',
      'size_t': 'unsigned long', 'std::size_t': 'unsigned long',
      'ptrdiff_t': 'long', 'std::ptrdiff_t': 'long', 'ssize_t': 'long',
      'intptr_t': 'long', 'uintptr_t': 'unsigned long',
      'std::intptr_t': 'long', 'std::uintptr_t': 'unsigned long',
  }
  #  The operators that change the object they are called on and give
  #  that very object back, as 'a += b'.
  __in_place_operators__ = (
      'operator+=', 'operator-=', 'operator*=', 'operator/=',
      'operator%=', 'operator&=', 'operator|=', 'operator^=',
      'operator<<=', 'operator>>=',
  )
  #  What the compiler calls each kind of function of a class.
  __function_kinds__ = dict(
      CXXConstructorDecl='constructor', CXXDestructorDecl='destructor',
      CXXMethodDecl='method', CXXConversionDecl='method',
  )
  #  The two functions through which a class says how 'new' and 'delete'
  #  work for it. A class forbidding one of them cannot be made, or
  #  removed, by a ritual.
  __making_functions__ = dict(
      constructor='operator new', destructor='operator delete',
  )
  #  The ways a function of Qt is reached from a ritual, in the order
  #  they are asked: the first that can reach a function has it. The
  #  meta-object runs Qt's own code, so it is asked before a copy of
  #  that code is made.
  __reach_experts__ = (CallExpert, MetaExpert, CopyExpert)
  #  The ways a type crosses, in the order they are asked: the first
  #  that claims a type says how it crosses. The order matters where
  #  two would claim one type: 'int *' is a number to change before it
  #  is an address, 'QThread *' an address of an object before it is a
  #  raw one, and 'QSize &&' is moved before it is a reference.
  __type_experts__ = (
      NothingExpert, NumberExpert, CharsExpert, TextsAddressExpert,
      NumberAddressExpert, NullExpert, EnumExpert, FlagsExpert,
      DurationExpert, AddressExpert, FunctionAddressExpert,
      RawAddressExpert, ListExpert, MapExpert, ValueExpert, MovedExpert,
      ReferenceExpert, HeldValueExpert,
  )
  #  The functions moc writes for the meta-object's own workings, and
  #  Qt's checks for the compiler: no function anybody calls, so not a
  #  gap where they get no ritual.
  __meta_workings__ = (
      'qt_static_metacall', 'qt_create_metaobjectdata', 'qt_check_for_',
  )

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __class_name__ = None  # type: Optional[str]
  __part_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]
  __written_rituals__ = None  # type: Optional[Rituals]
  __unwritten_functions__ = None  # type: Optional[Reasons]
  __type_tables__ = None  # type: Optional[Record]
  #  The experts of the generator, one of each kind, made at the first
  #  call of 'getExpert'; and the type expert of each kind of passing.
  __ritual_experts__ = None  # type: Optional[Dict[type, RitualExpert]]
  __type_kinds__ = None  # type: Optional[Dict[str, TypeExpert]]

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

  def getCuteClassName(self) -> str:
    """Gives the name of the C++ class of ours that is built on the
    class of Qt, as 'CuteQWidget'. Python never sees it."""
    return 'Cute%s' % self.getClassName().replace('::', '_')

  def getExpert(self, expertClass: Type[RitualExpert]) -> Any:
    """
    Gives the expert of a kind that works for this generator, as
    'getExpert(CopyExpert)': made at the first call, and kept until a
    setter changes what the generator works on.

    Raises
    ------

    TypeException
      'expertClass' is no class built on 'RitualExpert'.
    """
    if not isinstance(expertClass, type):
      raise TypeException('expertClass', expertClass, type)
    if not issubclass(expertClass, RitualExpert):
      raise TypeException('expertClass', expertClass, RitualExpert)
    experts = self.__ritual_experts__
    if experts is None:
      experts = self.__ritual_experts__ = dict()
    if expertClass not in experts:
      expert = expertClass()
      expert.setGenerator(self)
      experts[expertClass] = expert
    return experts[expertClass]

  def getReachExperts(self) -> Tuple[ReachExpert, ...]:
    """Gives the ways a function of Qt is reached from a ritual, in the
    order they are asked; see '__reach_experts__'."""
    return (*(self.getExpert(cls) for cls in self.__reach_experts__),)

  def getTypeExperts(self) -> Tuple[TypeExpert, ...]:
    """Gives the ways a type crosses, in the order they are asked; see
    '__type_experts__'."""
    return (*(self.getExpert(cls) for cls in self.__type_experts__),)

  def getTypeExpertOf(self, kind: str) -> Optional[TypeExpert]:
    """Gives the type expert whose 'findPassing' gives records of a
    kind, as the 'NumberExpert' for 'number'; None for '', the kind of
    a type no expert claims."""
    if self.__type_kinds__ is None:
      kinds = dict()  # type: Dict[str, TypeExpert]
      for expert in self.getTypeExperts():
        for own in expert.getKinds():
          kinds[own] = expert
      self.__type_kinds__ = kinds
    return self.__type_kinds__.get(kind)

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
    'ProbeExpert.settle' or 'CopyExpert.settle' had to drop, each with
    the reason. They are no part of 'getNotWritten', which accounts for
    the functions of the header alone.
    """
    return (
        *self.getExpert(ProbeExpert).getNotWrittenExtras(),
        *self.getExpert(CopyExpert).getNotWrittenExtras(),
    )

  def getRitualNames(self) -> Tuple[str, ...]:
    """Gives the name of every ritual of the class, in order."""
    return (*(ritual['ritualName'] for ritual in self.getWritten()),)

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

  def getRitualText(self) -> str:
    """Gives the whole text of the ritual file, without writing it; see
    'RitualFileExpert.getRitualText'."""
    return self.getExpert(RitualFileExpert).getRitualText()

  def getRitualTextOf(
      self,
      written: List[Record],
      unwritten: List[Tuple[str, str]],
  ) -> str:
    """Gives the text the ritual file would have with these rituals
    written and these functions not, while the plan is still being
    settled; see 'CopyExpert.settle'. Nothing is kept of them."""
    self.__written_rituals__ = (*written,)
    self.__unwritten_functions__ = (*unwritten,)
    try:
      return self.getRitualText()
    finally:
      self.__written_rituals__ = None
      self.__unwritten_functions__ = None

  def getRowsText(self) -> str:
    """Gives the whole text of the rows file, without writing it; see
    'RitualFileExpert.getRowsText'."""
    return self.getExpert(RitualFileExpert).getRowsText()

  def getFileConditions(self) -> Tuple[str, ...]:
    """Gives the conditions the whole ritual file stands under,
    outermost first; see 'ConditionExpert.getFileConditions'."""
    return self.getExpert(ConditionExpert).getFileConditions()

  def hasCuteClass(self) -> bool:
    """Says whether the class gets a C++ class of ours built on it; see
    'CuteClassExpert.hasCuteClass'."""
    return self.getExpert(CuteClassExpert).hasCuteClass()

  def getOverridable(self) -> Records:
    """Gives the functions of the class that Python can take over; see
    'CuteClassExpert.getOverridable'."""
    return self.getExpert(CuteClassExpert).getOverridable()

  def getDeclaredVirtuals(self) -> Records:
    """Gives every function Qt calls itself that the class is the first
    to declare; see 'CuteClassExpert.getDeclaredVirtuals'."""
    return self.getExpert(CuteClassExpert).getDeclaredVirtuals()

  def getListKinds(self) -> Dict[Tuple[str, str], Record]:
    """Gives every kind of list and of map the functions of Qt take or
    give; see 'ListExpert.getListKinds'."""
    return self.getExpert(ListExpert).getListKinds()

  def getOwnListKinds(self) -> List[Record]:
    """Gives the kinds of list that hold the class; see
    'ListExpert.getOwnListKinds'."""
    return self.getExpert(ListExpert).getOwnListKinds()

  def getOwnMapKinds(self) -> List[Record]:
    """Gives the kinds of map whose values are of the class; see
    'MapExpert.getOwnMapKinds'."""
    return self.getExpert(MapExpert).getOwnMapKinds()

  def getListNames(self, listed: Record) -> List[str]:
    """Gives the names Qt itself has for one kind of list; see
    'ListExpert.getListNames'."""
    return self.getExpert(ListExpert).getListNames(listed)

  def getMapNames(self, mapped: Record) -> List[str]:
    """Gives the names Qt itself has for one kind of map; see
    'MapExpert.getMapNames'."""
    return self.getExpert(MapExpert).getMapNames(mapped)

  def getPrivateArguments(self) -> Tuple[str, ...]:
    """Gives the '-I' arguments by which the compiler finds the headers
    Qt calls private; see 'ProbeExpert.getPrivateArguments'."""
    return self.getExpert(ProbeExpert).getPrivateArguments()

  def getSourceText(self) -> str:
    """Gives the code taken from Qt's own source for the class; see
    'CopyExpert.getSourceText'."""
    return self.getExpert(CopyExpert).getSourceText()

  def getSourceIncludes(self) -> Tuple[str, ...]:
    """Gives the lines that pull in what the code of 'getSourceText'
    needs; see 'CopyExpert.getSourceIncludes'."""
    return self.getExpert(CopyExpert).getSourceIncludes()

  def getProbeHeader(self) -> str:
    """Gives the path of the precompiled header each probe compile
    starts from; see 'ProbeExpert.getProbeHeader'."""
    return self.getExpert(ProbeExpert).getProbeHeader()

  def getLeftOutParts(self) -> Dict[str, str]:
    """Gives the parts left out of the probe header of every part; see
    'ProbeExpert.getLeftOutParts'."""
    return self.getExpert(ProbeExpert).getLeftOutParts()

  def getRefusedParts(self) -> Dict[str, str]:
    """Gives the parts whose own probe header the compiler refused; see
    'ProbeExpert.getRefusedParts'."""
    return self.getExpert(ProbeExpert).getRefusedParts()

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _forget(self) -> None:
    """Forgets what was decided, and the experts that decided it."""
    self.__written_rituals__ = None
    self.__unwritten_functions__ = None
    self.__ritual_experts__ = None
    self.__type_kinds__ = None

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
    self.__type_tables__ = None
    self._forget()

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
    self._forget()

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
    self.__type_tables__ = None
    self._forget()

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
      textNames = (ValueExpert.getTextName(), *ValueExpert.getViewNames())
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
    """Gives the type a name stands for, through every second name,
    and last through '__system_numbers__'."""
    aliases = self._getTypeTables()['aliases']
    seen = set()  # type: Set[str]
    while cppType in aliases and cppType not in seen:
      seen.add(cppType)
      cppType = aliases[cppType]
    return self.__system_numbers__.get(cppType, cppType)

  def _spellOutside(self, cppType: str) -> str:
    """Writes a type the way it has to be written outside the class;
    see 'SpellingExpert.spellOutside'."""
    return self.getExpert(SpellingExpert).spellOutside(cppType)

  def _getKnownNames(self) -> FrozenSet[str]:
    """Gives the full name of every class, enum and second name for a
    type the tree knows; see 'SpellingExpert.getKnownNames'."""
    return self.getExpert(SpellingExpert).getKnownNames()

  def _getHeading(self) -> str:
    """Says who wrote a file, from what, and that it is written anew;
    see 'RitualFileExpert.getHeading'."""
    return self.getExpert(RitualFileExpert).getHeading()

  def _getMarkedSymbols(self) -> FrozenSet[str]:
    """Gives the compiler's own name of everything Qt marks for use
    from outside Qt; see 'CallExpert.getMarkedSymbols'."""
    return self.getExpert(CallExpert).getMarkedSymbols()

  def _findListKind(self, cppType: str) -> Optional[Record]:
    """Says which kind of list a type hands around as a value; see
    'ListExpert.findListKind'."""
    return self.getExpert(ListExpert).findListKind(cppType)

  def _findMapKind(self, cppType: str) -> Optional[Record]:
    """Says which kind of map a type hands around as a value; see
    'MapExpert.findMapKind'."""
    return self.getExpert(MapExpert).findMapKind(cppType)

  def _findPassing(self, written: str, plain: str) -> Optional[Record]:
    """
    Says how a type is passed between Python and C++: the type experts
    are asked in turn, and the first that claims the type says it; see
    '__type_experts__' and 'TypeExpert.findPassing'.

    Parameters
    ----------

    written : str
      The type as the header writes it, with every name in full.

    plain : str
      The same type as the compiler reads it, second names followed.

    Returns
    -------

    Optional[Record]
      None for a type that cannot be passed yet: no expert claims it,
      or the one that claims it cannot pass it. Else a record saying:
      'kind': one of the kinds of the experts, as 'number', 'list' or
      'reference'; 'word': its word in the row, '' for a number that
      has no word that is right on every system; and what the kind
      needs besides, as 'className'.
    """
    plain = self._followAliases(plain)
    for expert in self.getTypeExperts():
      if expert.claims(written, plain):
        return expert.findPassing(written, plain)
    return None

  def _createPlan(self, ) -> None:
    """Decides, for each function of the class, whether it is written."""
    className = self.getClassName()
    record = self._readRecord(className)
    cuteExpert = self.getExpert(CuteClassExpert)
    #  A signal is written as any function is: calling its ritual emits
    #  it, and Python finds it to connect to through the meta-object.
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
        if member.get('name', '').startswith(self.__meta_workings__):
          infoSpec = """not a gap: a template moc writes for the
          meta-object's own workings, or Qt declares for the compiler to
          check something, and nobody calls it"""
        reason = ' '.join(infoSpec.split())
        unwritten.append((self._showTemplate(member), reason))
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
          reason = self._findReason(plan, friend, 'public', False, ())
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
      reason = self._findReason(plan, member, access, abstract, barred)
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
    if cuteExpert.hasCuteClass():
      written.append(cuteExpert.planTake())
    if cuteExpert.isWithinLimit(className):
      written.extend(cuteExpert.planOwn())
    #  A class some list of Qt holds gets the rituals of that list, and
    #  a class some map of Qt has for its values those of that map.
    written.extend(self.getExpert(ListExpert).planLists())
    written.extend(self.getExpert(MapExpert).planMaps())
    #  Each way a type crosses does what it still has to: a value no
    #  cute class stands for gets the ritual removing it, and the
    #  compiler is asked whether it can copy it here.
    for typeExpert in self.getTypeExperts():
      typeExpert.settle(written, unwritten)
    #  The compiler is asked about the file as it would be written, and
    #  each ritual it refuses goes, with what it said.
    self.getExpert(ProbeExpert).settle(written, unwritten)
    #  Each way of reaching a function does what it still has to for
    #  the rituals it reached: a function Qt's library has no name for
    #  gets its code from Qt's source, where that code can be taken.
    for reachExpert in self.getReachExperts():
      reachExpert.settle(written, unwritten)
    self.__written_rituals__ = (*written,)
    self.__unwritten_functions__ = (*unwritten,)

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

  def _findPlacedArguments(self) -> List[Record]:
    """
    Gives what the nearest class declaring an 'operator new', the class
    itself or one it is built on, has its 'operator new' take after the
    size, where it declares only ones that take more than the size.
    Those hide the plain one, and 'new' alone does not compile: the
    nodes of 'QQmlJS::AST' are built on 'QQmlJS::Managed', whose
    'operator new' takes a pool of memory, and are made in it as
    'new (pool) Node(...)'. Gives nothing where 'new' alone compiles.
    """
    for scope in self.getExpert(SpellingExpert).getLookupOrder():
      try:
        record = self._readRecord(scope)
      except (ValueError, LookupError):
        continue
      takes = [
          [child for child in member.get('inner', ())
           if isinstance(child, dict)
           and child.get('kind') == 'ParmVarDecl']
          for member in record.get('inner', ())
          if isinstance(member, dict)
          and member.get('name') == 'operator new']
      if takes:
        if any(len(one) == 1 for one in takes):
          return []
        return [*takes[0][1:]]
    return []

  def _showTemplate(self, member: Record) -> str:
    """Names a template of the class, as 'QObject::findChild'."""
    return '%s::%s' % (self.getClassName(), member.get('name', ''))

  def _hasKeptTwin(self, member: Record) -> bool:
    """Says whether the class declares, beside a function for a value
    about to be thrown away, as 'QString::toUpper() &&', the same
    function for a kept value, as 'QString::toUpper() const &': of the
    same name, taking the same."""
    taken = CppText.splitFunctionType(member['type']['qualType'])[1]
    record = self._readRecord(self.getClassName())
    for other in record.get('inner', ()):
      if other is member or other.get('name') != member.get('name'):
        continue
      if other.get('kind') != member.get('kind'):
        continue
      functionType = other.get('type', dict()).get('qualType', '')
      _, otherTaken, words = CppText.splitFunctionType(functionType)
      if otherTaken == taken and '&&' not in words:
        return True
    return False

  def _findFriendOwner(self, friend: Record, plan: Record) -> str:
    """
    Gives the class an operator written with 'friend' gets its ritual
    with: of the classes that declare it in their body, the one that
    stands first among its arguments. For an operator no other class
    declares, that is this class.
    """
    className = self.getClassName()
    compilerName = friend.get('mangledName', None)
    if compilerName is None:
      return className
    for argument in plan['arguments']:
      passing = argument['passing']
      if passing.get('kind') == 'value':
        otherName = passing.get('className', None)
      elif passing.get('kind') in ('reference', 'moved'):
        #  An object handed over by its address, as 'QPainterPath &'.
        otherName = self._followAliases(argument['written'].replace(
            'const ', '').replace('&', '').strip())
      else:
        otherName = None
      if otherName is None:
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

  def _planFunction(self, member: Record, **kwargs) -> Record:
    """
    Works out the ritual of one function of the class, whether or not
    it can be written: its name, what it takes and gives, its row and
    its text. The keyword 'friend=True' says the function is one Qt
    writes inside the class with 'friend' in front, which belongs to
    no object and is called by its bare name. How each type crosses is
    asked of the type experts; see '_findPassing'.
    """
    className = self.getClassName()
    fileExpert = self.getExpert(RitualFileExpert)
    own, hidden = kwargs.get('own', False), kwargs.get('hidden', False)
    if kwargs.get('friend', False):
      kind = 'friend'
    else:
      kind = self.__function_kinds__[member['kind']]
    if kind == 'method' and member.get('storageClass') == 'static':
      kind = 'static method'
    functionType = member['type']['qualType']
    given, taken, words = CppText.splitFunctionType(functionType)
    #  The same type as the compiler reads it, second names followed.
    plainType = member['type'].get('desugaredQualType', functionType)
    plainGiven = CppText.splitFunctionType(plainType)[0]
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
    shown = ', '.join(CppText.joinType(t, n) for n, t, _, _ in arguments)
    if kind == 'friend':
      shown = '%s(%s)' % (member['name'], shown)
    else:
      shown = '%s::%s(%s)' % (className, member['name'], shown)
    if kind in ('method', 'static method', 'friend'):
      shown = CppText.joinType(given, shown)
    if 'const' in words:
      shown = '%s const' % shown
    #  From here on the types are for the ritual, which stands outside
    #  the class and needs every name in full.
    given = self._spellOutside(given)
    unknown, unsure = [], []  # type: List[str], List[str]
    takes, passed, row, needs = [], [], [], []
    noted = []  # type: List[Record]
    placed = 0
    if kind == 'constructor':
      #  A class whose 'operator new' takes more than the size is made
      #  in place, as 'new (pool) Node(...)': the ritual takes what that
      #  'operator new' takes, before what the constructor takes.
      for entry in self._findPlacedArguments():
        name = entry.get('name', '') or 'a%d' % placed
        while name in {one[0] for one in arguments}:
          name = '%s_' % name
        cppType = entry['type']
        plain = cppType.get('desugaredQualType', cppType['qualType'])
        plain = self._spellOutside(plain)
        arguments.insert(placed, (name, cppType['qualType'], plain, None))
        placed += 1
    for name, cppType, plain, default in arguments:
      written = self._spellOutside(cppType)
      if self._followAliases(plain).split('::')[-1] == 'QPrivateSignal':
        #  Qt's mark that only the class itself emits the signal, which
        #  Q_OBJECT declares in each class: the ritual makes it, and
        #  Python hands nothing for it.
        passed.append('%s::QPrivateSignal()' % className)
        continue
      if plain.replace('const ', '') == '__va_list_tag *':
        #  A 'va_list', which the compiler reports by its own name for
        #  what it is on Linux. Every system passes one as an address.
        written = 'va_list'
      passing = self._findPassing(written, plain)
      expert = None
      if passing is not None:
        expert = self.getTypeExpertOf(passing['kind'])
      if expert is not None and not expert.isTakenFromPython():
        #  A type of one value only, as 'std::nullptr_t': the ritual
        #  makes it, and Python hands nothing for it.
        passed.append(expert.writeTaken(name, written, passing)[1])
        continue
      if passing is None:
        unknown.append(plain)
        passing = dict(kind='', word='')
      elif not passing['word']:
        unsure.append(written)
      noted.append(dict(
          name=name, written=written, plain=self._followAliases(plain),
          passing=passing, default=default,
      ))
      if expert is None:
        #  A type no expert claims stands as the header writes it; the
        #  reason keeps the function from being written.
        takes.append((name, written))
        passed.append(name)
      else:
        takenType, handed, needed = expert.writeTaken(name, written, passing)
        needs.extend(needed)
        takes.append((name, takenType))
        passed.append(handed)
      row.append(passing['word'])
    opening, closing = '', ');'
    giving = None  # type: Optional[Record]
    inPlace = False
    placing, passed = passed[:placed], passed[placed:]
    if kind == 'constructor':
      given, gives = '%s *' % className, 'address'
      made = className
      if self.hasCuteClass():
        #  Every object Python makes is of the C++ class of ours.
        made = self.getCuteClassName()
      opening, called = 'return ', 'new %s' % made
      if placing:
        called = 'new (%s) %s' % (', '.join(placing), made)
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
      if giving and not self.getTypeExpertOf(giving['kind']).canGiveBack():
        #  A kind its expert cannot give back, as a number to be changed
        #  where it is, or a value about to be thrown away.
        giving = None
      if giving is None:
        unknown.append(given)
        giving = dict(kind='', word='')
      elif not giving['word']:
        unsure.append(given)
      gives = giving['word']
      giving = dict(giving, written=given)
      expert = self.getTypeExpertOf(giving['kind'])
      if expert is None:
        #  A type no expert claims: the reason keeps the function from
        #  being written.
        opening = 'return '
      else:
        given, opening, closing, needed = expert.writeGiven(given, giving)
        needs.extend(needed)
    plan = dict(
        ritualName='ritual%s%s' % (
            '_own' if own else '', member.get('mangledName', '')),
        function=shown, kind=kind, gives=given, takes=(*takes,),
        row=(gives, *row), needs=(*dict.fromkeys(needs),),
        unknownTypes=(*dict.fromkeys(unknown),),
        unsureNumbers=(*dict.fromkeys(unsure),),
        words=(*words,), variadic='...' in taken,
        name=member['name'], arguments=(*noted,), giving=giving,
        inPlace=inPlace, placed=placed,
    )
    if kind == 'destructor':
      body = ['  delete self;']
    else:
      body = fileExpert.writeBody(opening, called, passed, closing)
    conditionExpert = self.getExpert(ConditionExpert)
    plan['conditions'] = conditionExpert.findOwnConditions(member)
    plan['bare'] = fileExpert.writeRitual(plan, body)
    plan['text'] = ConditionExpert.wrapInConditions(
        plan['bare'], plan['conditions'])
    return plan

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
    plan['text'] = self.getExpert(RitualFileExpert).writeRitual(plan, body)
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
    fileExpert = self.getExpert(RitualFileExpert)
    plan['text'] = fileExpert.writeRitual(plan, ['  delete self;'])
    return plan

  def _findReason(
      self,
      plan: Record,
      member: Record,
      access: str,
      abstract: bool,
      barred: Any,
  ) -> str:
    """
    Gives the reason a function gets no ritual, in words, or '' when
    nothing stands in the way of writing it.

    The ways of reaching a function are asked in turn, the first that
    can reach it having it; see '__reach_experts__'. Where none can,
    the reason names what each way would do and why it could not.

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
    if member.get('name', '').startswith(self.__meta_workings__):
      infoSpec = """not a gap: moc writes it for the meta-object's own
      workings, or Qt declares it for the compiler to check something,
      and nobody calls it"""
      return ' '.join(infoSpec.split())
    if plan['kind'] == 'constructor' and abstract:
      cuteExpert = self.getExpert(CuteClassExpert)
      if not cuteExpert.fillsEveryOpenFunction():
        infoSpec = """the class is abstract, so C++ cannot make one, and
        the C++ class of ours does not fill in every function it leaves
        open"""
        return ' '.join(infoSpec.split())
    if self.__making_functions__.get(plan['kind']) in barred:
      if plan['kind'] == 'constructor':
        return "the class keeps 'new' to itself, so no ritual can make one"
      infoSpec = """the class keeps 'delete' to itself, so no ritual can
      remove one"""
      return ' '.join(infoSpec.split())
    if plan['variadic']:
      return 'takes any number of arguments'
    if '&&' in plan['words']:
      if self._hasKeptTwin(member):
        infoSpec = """not a gap: the form of a function for a value about
        to be thrown away, whose form for a kept value is written; called
        from Python it would empty the value Python keeps"""
        return ' '.join(infoSpec.split())
      return 'can only be called on a value about to be thrown away'
    if 'mangledName' not in member:
      return 'the compiler gave it no name of its own'
    ways, refusals = [], []  # type: List[str], List[str]
    for reachExpert in self.getReachExperts():
      if reachExpert.canReach(member):
        break
      ways.append(reachExpert.getWay())
      refusals.append(reachExpert.getRefusal())
    else:
      if access == 'private' and not member.get('virtual') \
          and not self.getDependencyTree().hasBody(member) \
          and not self.getExpert(CallExpert).hasWrittenCode(member):
        #  As the private setters of 'Qt3DExtras::QTorusGeometryView',
        #  which hide those of the class it is built on.
        infoSpec = """not a gap: Qt declares it private and writes its
        code nowhere, so that nobody calls it"""
        return ' '.join(infoSpec.split())
      return 'cannot %s: %s' % (
          ' and cannot '.join(ways), ', and '.join(refusals))
    if plan['unknownTypes']:
      names = ', '.join(plan['unknownTypes'])
      return 'takes or gives a type that cannot be passed yet: %s' % names
    if plan['unsureNumbers']:
      infoSpec = """takes or gives a number that is not equally wide on
      every system: %s"""
      names = ', '.join(plan['unsureNumbers'])
      return ' '.join((infoSpec % names).split())
    #  Nothing stands in the way: the way that reached the function
    #  takes it on, and writes the ritual its own way where it has one.
    reachExpert.adopt(plan, member)
    return ''

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
