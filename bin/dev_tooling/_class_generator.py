"""ClassGenerator writes the Python file of one cute class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import collections
import keyword
import os
import textwrap
import threading
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree, QtPart, RitualGenerator, EnumGenerator

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Records = Tuple[Record, ...]
  Reasons = Tuple[Tuple[str, str], ...]
  Names = Tuple[str, ...]


#  How many letters a line may have right now, kept for each thread: 77,
#  and two less for each class the one being written stands inside.
_LOCAL = threading.local()


def _width() -> int:
  """Gives how many letters a line may have right now."""
  return getattr(_LOCAL, 'width', 77)


class ClassGenerator:
  """
  Writes the Python file of one cute class: the class standing for one
  class of Qt, with one function for each ritual of that class that
  Python can call. It writes what a person wrote for 'QSize' and
  'QObject' by hand, from the same plan the ritual file of the class is
  written from, so the two agree. This is the generator side of the
  tooling; 'ClassTester' is the side that verifies what it wrote.

    generator = ClassGenerator()
    generator.setDependencyTree(tree)
    generator.setClassName('QSize')
    generator.setCuteNames('QSize', 'QPoint')   # the cute classes
    generator.setWorkFolder('/some/folder/cutienator')
    generator.write()        # writes '.../cutienator/QtCore/_q_size.py'
    generator.getFunctions()    # the functions of that class
    generator.getLeftOut()      # the rituals with no function, and why

  Terms
  -----

  - A cute class is a plain Python class standing for one class of Qt.
    An object of it stands in front of one C++ object.
  - A ritual, a ritual file and a row are as 'RitualGenerator' explains
    them.
  - A signature is what stands between the brackets of one
    '@overload(...)': the classes of the arguments one call may have.
  - A late class is any cute class the one being written is not built
    on. Its file is not brought in by the file being written: the body
    names it through 'WAIT', and its signatures wait until a program
    brings it in.

  You provide
  -----------

  - 'setDependencyTree': the tree of the parts of Qt. Required.
  - 'setClassName': the class of Qt to write the cute class of.
    Required.
  - 'setCuteNames': every class of Qt that has, or is about to get, a
    cute class. A function naming any other class is left out.
    Required.
  - 'setWorkFolder': the folder of the package 'cutienator'. The file
    goes into the folder of its part of Qt there. Required before
    'write' only.

  How a type of Qt looks in Python
  --------------------------------

  - A number is an 'int', a 'float' or a 'bool'.
  - Text, Qt's 'QString' and C's 'const char *', is a 'str'.
  - An enum is a member of its class, as 'Qt.AspectRatioMode', and the
    combinations of a flags enum are values of the class of that enum,
    named as Qt names them, as 'Qt.WindowFlags'.
  - An object Qt takes or gives by its address is an object of its cute
    class. None is taken for no object, and for no text where Qt takes
    text as C has it, since C++ lets nothing be given there. Whether
    Qt can do with nothing in that place is as in C++.
  - An object Qt takes or gives as a value is an object of its cute
    class, which Python owns.

  What it writes for one function of Qt
  -------------------------------------

  - One function of the same name, calling the ritual. A name that is
    a word of Python gets an underscore after it, as 'raise_'.
  - A function taking nothing, alone at its name, is a plain function.
    Every other function is given its signature with '@overload'.
  - Where None is taken, and where Qt fills in an argument that is
    left out, the function gets one more signature for each such call,
    stacked on the one function. What Qt fills in is the default of
    the Python argument. An argument whose default cannot be said in
    Python has to be given, and so has every argument before it.
  - A signature naming a late class waits, and shares its function
    with the other signatures of the stack.
  - A function giving an object of a late class, or making one for an
    argument that was left out, brings that class in itself, at that
    call, as 'from ..QtGui import QFont'.

  What it writes at the top of the file
  -------------------------------------

  - The file brings in what its class is built on, and the namespace
    'Qt', the cute way: it asks the package of their part, as
    'from ..QtCore import Qt, QObject'. The package brings in the one
    file each is in, the first time it is asked for. So bringing in
    one class brings in the files of the classes it is built on, and
    of the classes holding what it names, and no others.
  - The enums and the classes Qt writes inside the class are written
    inside it, where C++, PySide6 and PyQt have them: 'class
    RenderFlag(CuteFlags)' in the body of 'QWidget', so its only name
    is 'QWidget.RenderFlag'. Nothing of Qt has a name Qt does not give
    it.
  - An enum or a class Qt writes inside another class is reached
    through that class, as 'QPalette.ColorRole' and
    'QMetaObject.Connection', so the file of that class is brought in:
    'from ..QtGui import QPalette'. Such a class is no late class.
  - Each late class a signature takes is bound to a 'WAIT' there, as
    "QFont = WAIT['QFont']", under 'else:' of 'if TYPE_CHECKING:'.
    Under 'if TYPE_CHECKING:' stands the import of every late class
    an annotation names, the cute way, from the package of its part,
    as 'from ..QtGui import QFont'. A type checker reads those lines
    and Python does not run them, so they bring nothing in. Why a
    call never meets a signature that still waits is told in the
    docstring of 'cutienator.cute.WAIT'.
  - Each constructor of Qt is one '__init__', which notes what it was
    given. The C++ object is made at the first use. Qt's application,
    'QCoreApplication' and every class built on it, is made at once:
    nearly every other object of Qt can only be made after it.

  What gets no function, though it has a ritual
  ---------------------------------------------

  The destructor; an operator; a function naming a class that has no
  cute class, or giving a value of a class Python cannot own; one
  taking a number to change in place or a single letter of C; one whose
  calls an earlier function of its name takes already; one that is
  another kind of method than most of its name; and Qt's own inner
  workings, named 'qt_...'. Each is listed by 'getLeftOut', and in the
  docstring of the class.

  What to expect
  --------------

  - The cute class is built on the cute class of the first class its
    Qt class is built on. A second one, as 'QPaintDevice' for
    'QWidget', is not reflected.
  - A class Qt writes inside another, as 'QMetaObject::Connection', is
    a cute class written inside the cute class of that class, in its
    file, with lines two letters shorter. It has no file of its own,
    and 'getClassText' and 'write' refuse it: the generator of the
    class around it writes it, through 'getNestedLines'.
  - The body of a class written inside another does not see the names
    of the body around it, as Python has it. What it waits for it
    binds itself, under 'if not TYPE_CHECKING:', the class around it
    included. A function of it naming an enum of the class around it,
    or a class beside it, is left out, and the docstring says so.
  - The getters decide and write nothing. Only 'write' touches a file,
    and it replaces the file whole.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getStem(cppName: str) -> str:
    """
    Gives a name of Qt in small letters, with an underscore before each
    word: 'q_object' for 'QObject'.
    """
    stem = []  # type: List[str]
    for letter in cppName.replace('::', '__'):
      if letter.isupper() and stem and stem[-1] != '_':
        stem.append('_')
      stem.append(letter.lower())
    return ''.join(stem)

  @staticmethod
  def _wrapWords(words: str, indent: str, width: int = 0) -> List[str]:
    """Gives words as lines of at most 'width' letters, each indented:
    as many as a line may have right now when none is given."""
    return textwrap.wrap(
        ' '.join(words.split()), width or _width(), initial_indent=indent,
        subsequent_indent=indent, break_long_words=False,
        break_on_hyphens=False,
    ) or [indent.rstrip()]

  @staticmethod
  def _wrapCpp(shown: str, first: str, later: str) -> List[str]:
    """
    Gives a function as C++ writes it as lines of at most 77 letters.

    C++ writes a name with what it takes right behind it, as
    'QWidget::setParent(QWidget', which can be longer than a line. Such
    a word is broken behind a '(' or a '::'.

    Parameters
    ----------

    shown : str
      The function as C++ writes it.

    first : str
      What the first line starts with.

    later : str
      What every other line starts with.
    """
    lines, line = [], first
    for word in shown.split():
      pieces = [word]
      while len(later) + len(pieces[-1]) > _width():
        long = pieces.pop()
        room = _width() - len(later)
        cut = max(long.rfind('(', 0, room), long.rfind('::', 0, room - 1))
        if cut <= 0:
          pieces.append(long)
          break
        cut += 1 if long[cut] == '(' else 2
        pieces.extend((long[:cut], long[cut:]))
      for index, piece in enumerate(pieces):
        glue = '' if index or line in (first, later) else ' '
        if len(line) + len(glue) + len(piece) > _width():
          if line.strip() and line not in (first, later):
            lines.append(line)
            line, glue = later, ''
        line = '%s%s%s' % (line, glue, piece)
    lines.append(line)
    return lines

  @staticmethod
  def _unwrap(node: Optional[Record]) -> Optional[Record]:
    """
    Gives what the compiler wrote down for a value, without the layers
    it puts around it that change nothing of the value.
    """
    layers = (
        'ImplicitCastExpr', 'ExprWithCleanups', 'ConstantExpr',
        'MaterializeTemporaryExpr', 'CXXBindTemporaryExpr', 'ParenExpr',
    )
    while node is not None and node.get('kind') in layers:
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      node = inner[0] if inner else None
    return node

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The constants of the classes of Qt that are numbers, gathered once
  #  for each tree; see '_findConstantNumber'.
  __constant_lock__ = threading.RLock()
  __constant_numbers__ = dict()  # type: Dict[int, Dict[str, Set[Any]]]
  #  The name Python has for each operator of C++ that takes two: the
  #  one asked of what stands on the left, and the one asked of what
  #  stands on the right when the left has said it cannot. For a
  #  comparison the second is the comparison turned round.
  __binary_operators__ = {
      '+': ('__add__', '__radd__'), '-': ('__sub__', '__rsub__'),
      '*': ('__mul__', '__rmul__'), '/': ('__truediv__', '__rtruediv__'),
      '%': ('__mod__', '__rmod__'), '&': ('__and__', '__rand__'),
      '|': ('__or__', '__ror__'), '^': ('__xor__', '__rxor__'),
      '<<': ('__lshift__', '__rlshift__'),
      '>>': ('__rshift__', '__rrshift__'),
      '==': ('__eq__', '__eq__'), '!=': ('__ne__', '__ne__'),
      '<': ('__lt__', '__gt__'), '<=': ('__le__', '__ge__'),
      '>': ('__gt__', '__lt__'), '>=': ('__ge__', '__le__'),
  }
  #  The same for an operator that takes one, and for one that changes
  #  the object it is called on.
  __unary_operators__ = {'-': '__neg__', '+': '__pos__', '~': '__invert__'}
  __in_place_operators__ = {
      '+=': '__iadd__', '-=': '__isub__', '*=': '__imul__',
      '/=': '__itruediv__', '%=': '__imod__', '&=': '__iand__',
      '|=': '__ior__', '^=': '__ixor__', '<<=': '__ilshift__',
      '>>=': '__irshift__',
  }
  #  What a number type built into C++ is in Python.
  __python_numbers__ = dict(
      bool='bool', float='float', double='float',
  )

  #  The words Python has for the names of Qt that are words of Python
  #  in an enum; see 'EnumGenerator'.
  __python_words__ = {'None': 'NULL', 'True': 'TRUE', 'False': 'FALSE'}

  #  The sections of a class body, in order, each with its banner.
  __section_names__ = (
      'STATIC METHODS', 'NAMESPACE', 'GETTERS', 'SETTERS', 'NOTIFIERS',
      'Python API', 'CONSTRUCTORS', 'DOMAIN SPECIFIC', 'OPTIONAL METHODS',
      'REQUIRED METHODS', 'PARENT METHODS', 'PUBLIC METHODS',
  )

  #  The class of Qt whose objects Qt can watch, and tell the removal
  #  of. Its cute class says so, and every class built on it inherits
  #  that.
  __watched_name__ = 'QObject'

  #  The class of Qt that everything else of Qt needs to be there
  #  first. It, and every class built on it, is made at once.
  __application_name__ = 'QCoreApplication'

  #  The parts of Qt, each after the parts it is built on.
  __part_order__ = ('QtCore', 'QtGui', 'QtWidgets')

  #  Fallback Variables

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __class_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]
  __cute_names__ = None  # type: Optional[Names]
  __ritual_generators__ = None  # type: Optional[Dict[str, Any]]
  __made_functions__ = None  # type: Optional[Records]
  __left_out__ = None  # type: Optional[Reasons]
  __needed_names__ = None  # type: Optional[Record]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getDependencyTree(self) -> DependencyTree:
    """
    Gives the dependency tree the generator works from.

    Provided by you, through 'setDependencyTree'.

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
    Gives the class of Qt the cute class stands for, as 'QSize'.

    Provided by you, through 'setClassName'.

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
    Gives the folder of the package the file is written into.

    Provided by you, through 'setWorkFolder'.

    Raises
    ------

    MissingVariable
      'setWorkFolder' has not been called.
    """
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getCuteNames(self) -> Names:
    """
    Gives every class of Qt that has, or is about to get, a cute class.

    Provided by you, through 'setCuteNames'.

    Raises
    ------

    MissingVariable
      'setCuteNames' has not been called.
    """
    if self.__cute_names__ is None:
      raise MissingVariable(self, '__cute_names__', tuple)
    return self.__cute_names__

  def getPythonName(self, className: Optional[str] = None) -> str:
    """
    Gives the name the cute class of a class of Qt has in Python:
    'QSize' for 'QSize', and 'Connection' for
    'QMetaObject::Connection'. It is that of the class being written
    when none is named.
    """
    className = className or self.getClassName()
    return className.rpartition('::')[2]

  def getDottedName(self, className: Optional[str] = None) -> str:
    """
    Gives the name by which Python reaches the cute class of a class of
    Qt from the top of its file, as C++, PySide6 and PyQt have it:
    'QSize' for 'QSize', and 'QMetaObject.Connection' for
    'QMetaObject::Connection'. It is that of the class being written
    when none is named.
    """
    className = className or self.getClassName()
    return className.replace('::', '.')

  def isNested(self) -> bool:
    """Says whether Qt writes the class inside another class. Such a
    class is written inside the cute class of that class, in its file."""
    return True if '::' in self.getClassName() else False

  def getInnerGenerators(self) -> Tuple[Any, ...]:
    """
    Gives the generator of each class Qt writes right inside this one,
    in alphabetical order. Each writes its class into the body of this
    one. Made for you, once, and kept.
    """
    if self.__inner_generators__ is None:
      generators = []
      for innerName in self.getInnerNames():
        generator = type(self)()
        generator.setDependencyTree(self.getDependencyTree())
        generator.setClassName(innerName)
        generator.setCuteNames(*self.getCuteNames())
        generators.append(generator)
      self.__inner_generators__ = (*generators,)
    return self.__inner_generators__

  def getAllGenerators(self) -> Tuple[Any, ...]:
    """Gives this generator and that of every class written inside
    its class, however deep, each once."""
    found = [self]
    for generator in self.getInnerGenerators():
      found.extend(generator.getAllGenerators())
    return (*found,)

  def getOwnerName(self, className: Optional[str] = None) -> str:
    """
    Gives the class Qt writes a class inside, as 'QMetaObject' for
    'QMetaObject::Connection', or '' for a class written inside none.
    """
    className = className or self.getClassName()
    return className.rpartition('::')[0]

  def getInnerNames(self) -> Names:
    """
    Gives the classes Qt writes right inside the class that have a
    cute class, in alphabetical order. The cute class holds each under
    its own name.
    """
    className = self.getClassName()
    return (*sorted(
        name for name in self.getCuteNames()
        if self.getOwnerName(name) == className),)

  def getPartName(self, className: Optional[str] = None) -> str:
    """
    Gives the part of Qt a class belongs to, as 'QtCore': that of the
    class being written when none is named.
    """
    className = className or self.getClassName()
    return self.getDependencyTree().getPartName(className)

  def getFileStem(self, className: Optional[str] = None) -> str:
    """
    Gives the name of the file of a cute class without its ending, as
    '_q_size' for 'QSize': that of the class being written when none
    is named.
    """
    className = className or self.getClassName()
    #  A class written inside another has no file of its own: it stands
    #  in the file of the outermost class around it.
    return '_%s' % self.getStem(className.split('::')[0])

  def getClassFile(self) -> str:
    """
    Gives the full path of the file, as
    '/some/folder/cutienator/QtCore/_q_size.py'.

    Found for you. Having the path does not mean the file is there;
    'write' makes it.
    """
    name = '%s.py' % self.getFileStem()
    return os.path.join(self.getWorkFolder(), self.getPartName(), name)

  def getRitualGenerator(self, className: Optional[str] = None) -> Any:
    """
    Gives the generator of the ritual file of a class: that of the
    class being written when none is named. The functions of the cute
    class are written from its plan.

    Made for you, once for each class, and kept.

    Returns
    -------

    RitualGenerator
      With the tree and the class set, and no work folder.
    """
    className = className or self.getClassName()
    if self.__ritual_generators__ is None:
      self.__ritual_generators__ = dict()
    if className not in self.__ritual_generators__:
      generator = RitualGenerator()
      generator.setDependencyTree(self.getDependencyTree())
      generator.setClassName(className)
      self.__ritual_generators__[className] = generator
    return self.__ritual_generators__[className]

  def getBaseName(self) -> Optional[str]:
    """
    Gives the class of Qt whose cute class this one is built on: the
    first class the Qt class is built on, when that has a cute class.
    Gives None for a class built on no such class.
    """
    parents = self.getDependencyTree().getParents(self.getClassName())
    if not parents or parents[0] not in self.getCuteNames():
      return None
    if '::' in parents[0] or not self._isMadeBefore(parents[0]):
      return None
    return parents[0]

  def getUnreflectedParents(self) -> Names:
    """Gives the classes the Qt class is built on that the cute class
    is not built on."""
    parents = self.getDependencyTree().getParents(self.getClassName())
    reflected = (self.getBaseName(), *self.getFurtherBaseNames())
    return (*(p for p in parents if p not in reflected),)

  def getEnumGenerators(self) -> Tuple[Any, ...]:
    """
    Gives the generator of each enum Qt writes inside the class that
    code outside the class may use, in alphabetical order.

    Made for you. 'write' has each of them write its file.
    """
    tree, className = self.getDependencyTree(), self.getClassName()
    generators = []
    for enumName in tree.getEnumRecordNames():
      if tree.getEnumRecord(enumName)['ownerName'] != className:
        continue
      generator = self._getEnumGenerator(enumName)
      if generator.findRefusal() is None:
        generators.append(generator)
    return (*generators,)

  def getFunctions(self, **kwargs) -> Records:
    """
    Gives the functions of the cute class, in the order they are
    written.

    Decided for you, at the first call, and kept. Nothing is written to
    a file by this. You pass nothing; the keyword is for the method's
    own use.

    Returns
    -------

    Records
      A 'Tuple[Dict[str, Any], ...]'. Each function says:
      'pythonName': its name in Python, as 'scaled' or '__init__'.
      'plan': the ritual it calls, as 'RitualGenerator' has it.
      'kind': 'constructor', 'method' or 'static method'.
      'parameters': its arguments in Python, in order.
      'signatures': each signature it is given, as the texts between
      the brackets of one '@overload(...)'.
      'signatureKeys': the same signatures by the classes they take,
      whatever names the file writes those by.
      'section': the section of the class body it stands in.

    Raises
    ------

    MissingVariable
      One of the first three setters has not been called.

    LookupError
      The tree has no class of that name.
    """
    if self.__made_functions__ is None:
      if kwargs.get('_recursion', False):
        raise RecursionError
      #  Worked out twice: the first time tells which classes have an
      #  enum this one names, and those are no late classes the second
      #  time.
      self.__owners__ = ()
      self._createFunctions()
      self.__owners__ = (*self.__needed_names__['owners'],)
      self._createFunctions()
      return self.getFunctions(_recursion=True)
    return self.__made_functions__

  def getLeftOut(self) -> Reasons:
    """
    Gives the rituals of the class that get no function, each with the
    reason, in the order the header declares them.

    Decided for you, together with 'getFunctions'.

    Returns
    -------

    Reasons
      A 'Tuple[Tuple[str, str], ...]': the Qt function as C++ writes
      it, and the reason in words.
    """
    self.getFunctions()
    return self.__left_out__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _forget(self) -> None:
    """Forgets what was decided, after a setter changed what it is
    decided from."""
    self.__made_functions__ = None
    self.__left_out__ = None
    self.__needed_names__ = None

  def setDependencyTree(self, dependencyTree: DependencyTree) -> None:
    """
    Tells the generator which dependency tree to work from.

    Required. Calling it again forgets what was decided before.

    Raises
    ------

    TypeException
      'dependencyTree' is not a 'DependencyTree'.
    """
    if not isinstance(dependencyTree, DependencyTree):
      raise TypeException('dependencyTree', dependencyTree, DependencyTree)
    self.__dependency_tree__ = dependencyTree
    self.__ritual_generators__ = None
    self._forget()

  def setClassName(self, className: str) -> None:
    """
    Tells the generator which class of Qt to write the cute class of.

    Required. Calling it again forgets what was decided before.

    Parameters
    ----------

    className : str
      The class by the name the dependency tree has it under, as
      'QSize'.

    Raises
    ------

    TypeException
      'className' is not text.
    """
    if not isinstance(className, str):
      raise TypeException('className', className, str)
    self.__class_name__ = className
    self._forget()

  def setCuteNames(self, *cuteNames: str) -> None:
    """
    Tells the generator which classes of Qt have, or are about to get,
    a cute class.

    Required. A function naming a class that is not among them is left
    out, with that reason. Calling it again forgets what was decided
    before.

    Parameters
    ----------

    *cuteNames : str
      The classes, by the names the dependency tree has them under.

    Raises
    ------

    TypeException
      One of them is not text.
    """
    for cuteName in cuteNames:
      if not isinstance(cuteName, str):
        raise TypeException('cuteName', cuteName, str)
    self.__cute_names__ = (*cuteNames,)
    self._forget()

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Tells the generator where the package 'cutienator' is.

    Required before 'write' and 'getClassFile'.

    Parameters
    ----------

    workFolder : str
      The path of the folder of the package, which exists. The file is
      written into the folder of its part of Qt there, as 'QtCore'.

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
            ('setCuteNames', self.__cute_names__),
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

  def _getEnumGenerator(self, enumName: str) -> Any:
    """Gives the generator of one enum, with the tree and the folder
    it writes into set when that is known."""
    generator = EnumGenerator()
    generator.setDependencyTree(self.getDependencyTree())
    generator.setEnumName(enumName)
    if self.__work_folder__ is not None:
      generator.setWorkFolder(self.__work_folder__)
    return generator

  def _isMadeBefore(self, otherName: str) -> bool:
    """
    Says whether the cute class of another class of Qt is made before
    the one being written, so that this one can be built on it.

    A class of an earlier part of Qt is. A class of the same part is
    when the dependency tree makes it earlier.
    """
    tree, className = self.getDependencyTree(), self.getClassName()
    order = self.__part_order__
    here = order.index(tree.getPartName(className))
    there = order.index(tree.getPartName(otherName))
    if there != here:
      return True if there < here else False
    #  A class written inside another is made right before the
    #  outermost class around it, whose file brings it in.
    mine, theirs = className.split('::')[0], otherName.split('::')[0]
    if mine == theirs:
      return len(otherName) > len(className)
    makeOrder = tree.getMakeOrder()
    return makeOrder.index(theirs) < makeOrder.index(mine)

  def getFurtherBaseNames(self) -> Names:
    """
    Gives the classes of Qt after the first that the cute class is
    built on as well, as 'QPaintDevice' for 'QWidget', in the order C++
    names them. The cute class is built on the cute class of each, and
    names the ritual that gives where that part of an object is; see
    'RitualGenerator.getFurtherBases'.
    """
    parents = self.getDependencyTree().getParents(self.getClassName())
    return (*(
        parent for parent in parents[1:]
        if parent in self.getCuteNames() and '::' not in parent
        and self._isMadeBefore(parent)
    ),)

  def _getBuiltOn(self) -> Names:
    """
    Gives every class of Qt the cute class is built on, the nearest
    first: what it is built on, what those are built on, and so on.
    Their files are brought in with the file being written whatever it
    names, so naming them costs nothing.
    """
    tree, cuteNames = self.getDependencyTree(), self.getCuteNames()
    builtOn = [*filter(None, (self.getBaseName(),))]
    builtOn.extend(self.getFurtherBaseNames())
    for name in builtOn:
      for parent in tree.getParents(name):
        if parent in cuteNames and '::' not in parent:
          if parent not in builtOn:
            builtOn.append(parent)
    return (*builtOn,)

  def _getPartNames(self) -> Names:
    """
    Gives every class of Qt that some cute class is built on after its
    first, and every class those are built on: the classes whose part
    of an object may begin somewhere inside the object, as
    'QPaintDevice', which is such a part of a QWidget.

    A function of such a class hands its ritual the address of that
    part, through 'CuteMixin._callAs', and an object given where such a
    class is taken is handed over as the address of that part.
    """
    if self.__part_names__ is None:
      tree, cuteNames = self.getDependencyTree(), self.getCuteNames()
      found = []  # type: List[str]
      for className in cuteNames:
        for parent in tree.getParents(className)[1:]:
          if parent in cuteNames and parent not in found:
            found.append(parent)
      for name in found:
        for parent in tree.getParents(name):
          if parent in cuteNames and parent not in found:
            found.append(parent)
      self.__part_names__ = (*found,)
    return self.__part_names__

  #  The classes that hold an enum or a class this one names, known
  #  after the functions are worked out a first time. Their files are
  #  brought in.
  __owners__ = None
  #  The generators of the classes written inside this one.
  __inner_generators__ = None
  #  The classes whose part of an object may begin inside the object.
  __part_names__ = None

  def _getNeeds(self) -> Dict[str, List[str]]:
    """
    Gives the names the file needs for this class and for every class
    written inside it: what the top of the file brings in, and what it
    shows a type checker. What a class written inside another waits for
    is not among 'late': such a class binds its own 'WAIT' lines.
    """
    self.getFunctions()
    needs = collections.defaultdict(list)  # type: Dict[str, List[str]]

    def note(kind: str, *names: str) -> None:
      needs[kind].extend(n for n in names if n and n not in needs[kind])

    for kind, names in self.__needed_names__.items():
      note(kind, *names)
    for generator in self.getEnumGenerators():
      if generator.isFlags():
        note('top', 'CuteFlags')
      else:
        note('top', 'CuteNum', 'Kee')
    if self.getRitualGenerator().getOwnListKinds():
      #  The end of the file makes the list of the class.
      note('lists', 'QList')
    for mapped in self.getRitualGenerator().getOwnMapKinds():
      #  And the maps that have the class for their values.
      note('lists', mapped['pattern'])
    baseName, further = self.getBaseName(), self.getFurtherBaseNames()
    if baseName is None and not further:
      note('top', 'CuteMixin', 'MetaCute')
    note('classes', baseName, *further)
    if needs['late']:
      note('top', 'WAIT')
    note('classes', *needs['owners'])
    for generator in self.getInnerGenerators():
      inner = generator._getNeeds()
      for kind in ('top', 'typing', 'classes', 'namespace', 'lists'):
        note(kind, *inner[kind])
      #  What the class inside waits for is shown to a type checker by
      #  the file, beside what its annotations name.
      note('hinted', *inner['hinted'], *inner['late'])
    return needs

  def _note(self, kind: str, name: str) -> None:
    """Notes a name the file needs: a class to import ('classes'), a
    late class a signature takes ('late'), a class an annotation names
    ('hinted'), an enum of a late class ('enums'), or one of the names
    the top of the file brings in."""
    if self.__needed_names__ is None:
      self.__needed_names__ = collections.defaultdict(list)
    if name not in self.__needed_names__[kind]:
      self.__needed_names__[kind].append(name)

  def _findList(self, listed: Record) -> Any:
    """
    Says how the body names the cute class of one kind of list of Qt.

    Parameters
    ----------

    listed : Record
      The kind, as 'RitualGenerator._findListKind' describes it.

    Returns
    -------

    Any
      The reason, in words, when the list cannot be named from here.
      Else what '_findClass' gives for the class the list holds, with
      'entry', 'name' and 'holder' written as the list of it, as
      'QList[QUrl]', or as 'QStringList' for the list of text; and
      'lateName': the class to wait for, and 'className': the class
      the list holds.
    """
    if listed['crossing'] == 'text':
      self._note('lists', 'QStringList')
      return dict(
          entry='QStringList', name='QStringList', holder='QStringList',
          late=False, lateName='', bring='', hint='', className='QString',
      )
    holds = listed['holds']
    found = self._findClass(holds)
    if isinstance(found, str):
      return "a list of '%s': %s" % (holds, found)
    if found is None:
      return "a list of '%s', which has no cute class yet" % holds
    self._note('lists', 'QList')
    entry = found['entry']
    if entry == 'THIS':
      #  The list of the class being written is made after the class,
      #  further down this file, so a signature naming it waits.
      self._note('top', 'WAIT')
      entry = "WAIT['%s']" % holds
    return dict(
        found, entry='QList[%s]' % entry, name='QList[%s]' % found['name'],
        holder='QList[%s]' % found['holder'], lateName=found['entry'],
        className=holds,
    )

  def _findMap(self, mapped: Record) -> Any:
    """
    Says how the body names the cute class of one kind of map of Qt,
    as '_findList' says it for a list: 'QMap[int, QVariant]'.

    Parameters
    ----------

    mapped : Record
      The kind, as 'RitualGenerator._findMapKind' describes it.
    """
    holds, pattern = mapped['holds'], mapped['pattern']
    found = self._findClass(holds)
    if isinstance(found, str):
      return "a map to '%s': %s" % (holds, found)
    if found is None:
      return "a map to '%s', which has no cute class yet" % holds
    self._note('lists', pattern)
    entry = found['entry']
    if entry == 'THIS':
      self._note('top', 'WAIT')
      entry = "WAIT['%s']" % holds
    key = 'str' if mapped['keyWord'] == 'text' else 'int'
    return dict(
        found, entry='%s[%s, %s]' % (pattern, key, entry),
        name='%s[%s, %s]' % (pattern, key, found['name']),
        holder='%s[%s, %s]' % (pattern, key, found['holder']),
        lateName=found['entry'], className=holds,
    )

  def _findClass(self, otherName: str) -> Optional[Record]:
    """
    Says how the body names the cute class of a class of Qt.

    Returns
    -------

    Optional[Record]
      None for a class that has no cute class. Else 'entry': what
      stands for it in a signature, as 'THIS' or 'QEvent'; 'name': how
      an annotation writes it; 'late': whether it is a late class;
      'bring': the class whose file holds it, or ''; 'hint': the class
      a type checker has to be shown for the annotation, or '';
      'holder': what a function writes to reach the class. Or the
      reason, in words, when the class cannot be named from here.
    """
    className = self.getClassName()
    if otherName == className:
      name = self.getDottedName()
      return dict(
          entry='THIS', name=name, late=False, bring='', hint='',
          holder=name)
    if otherName not in self.getCuteNames():
      return None
    mine, theirs = className.split('::')[0], otherName.split('::')[0]
    if className.startswith('%s::' % otherName):
      #  A class this one is written inside is made after it, in this
      #  very file, so it waits and nothing is brought in for it.
      if '::' in otherName:
        return 'names a class it is written two deep inside'
      return dict(
          entry=otherName, name=otherName, late=True, bring='', hint='',
          holder=otherName)
    ownerName = self.getOwnerName(otherName)
    if not ownerName:
      #  A class this one is not built on is a late class: its file is
      #  brought in by the program that uses it, not by this one. A
      #  class that holds an enum or a class this one names is brought
      #  in for that already.
      late = otherName not in self._getBuiltOn() and (
          otherName not in (self.__owners__ or ()))
      if mine == theirs:
        late = True
      return dict(
          entry=otherName, name=otherName, late=late, bring=otherName,
          hint=otherName, holder=otherName)
    name = self.getPythonName(otherName)
    dotted = self.getDottedName(otherName)
    if ownerName == className:
      #  A class written inside this one stands in the body under its
      #  own name. A function reaches it through the class.
      return dict(
          entry=name, name=name, late=False, bring='', hint='',
          holder=dotted)
    if mine == theirs:
      #  Written inside the same class as this one, beside it or deeper:
      #  a class body does not see the names of the body around it.
      infoSpec = """names '%s', which stands beside this class inside
      '%s' and cannot be named from here"""
      return ' '.join((infoSpec % (otherName, mine)).split())
    for depth in range(1, otherName.count('::') + 1):
      if '::'.join(otherName.split('::')[:depth]) not in self.getCuteNames():
        return None
    #  A class written inside another class is reached through that
    #  class, as Qt writes it, so the file of that class is brought in.
    self._note('owners', theirs)
    return dict(
        entry=dotted, name=dotted, late=False, bring='', hint='',
        holder=dotted)

  def _findEnum(self, enumName: str, flags: bool) -> Optional[Record]:
    """
    Says how the body names the class of an enum of Qt.

    Parameters
    ----------

    enumName : str
      The full name of the enum, as 'Qt::WindowType'.

    flags : bool
      Whether the combinations of the enum are meant, which Qt names
      apart, as 'Qt::WindowFlags'.

    Returns
    -------

    Optional[Record]
      None for an enum the body cannot name. Else 'entry': the class as
      a signature writes it, as 'Qt.WindowFlags' or 'QPalette.ColorRole';
      'shown': the class as an annotation writes it, as
      'QPalette.ColorRole'; 'owner': the class it is reached through,
      or '' for the namespace 'Qt', for an enum of the class being
      written and for one brought in from its own file; 'generator':
      the 'EnumGenerator' of the enum.
    """
    tree = self.getDependencyTree()
    try:
      record = tree.getEnumRecord(enumName)
    except ValueError:
      return None
    generator = self._getEnumGenerator(enumName)
    if generator.findRefusal() is not None:
      return None
    ownName, ownerName = record['ownName'], record['ownerName']
    if flags:
      flagsName = generator.getFlagsName()
      if flagsName is None:
        return None
      ownName = flagsName.rpartition('::')[2]
    if ownerName == self.getClassName():
      return dict(
          entry=ownName, shown=ownName, owner='', generator=generator,
          own=True)
    if ownerName == 'Qt':
      self._note('namespace', 'Qt')
      entry = 'Qt.%s' % ownName
      return dict(entry=entry, shown=entry, owner='', generator=generator)
    if not record['insideClass']:
      return None
    if ownerName not in self.getCuteNames():
      return None
    className = self.getClassName()
    if ownerName.split('::')[0] == className.split('::')[0]:
      #  An enum of the class this one is written inside, or of a class
      #  beside it: a class body does not see the names of the body
      #  around it, and that class is not made yet.
      return None
    #  The enum stands inside its class, as Qt writes it, so the file of
    #  that class is brought in for it.
    self._note('owners', ownerName.split('::')[0])
    entry = '%s.%s' % (self.getDottedName(ownerName), ownName)
    return dict(
        entry=entry, shown=entry, owner=ownerName, generator=generator)

  def _findEnumNumber(self, referenced: Record) -> Optional[int]:
    """
    Gives the number of one name of an enum that a default of Qt
    refers to, or None when it is not found.

    Parameters
    ----------

    referenced : Record
      What the compiler wrote down of the name referred to: its 'name'
      and the 'type' of its enum.
    """
    tree, name = self.getDependencyTree(), referenced.get('name')
    enumName = referenced.get('type', dict()).get('qualType', '')
    className = self.getClassName()
    for scope in ('', className, *tree.getAncestors(className)):
      fullName = '%s::%s' % (scope, enumName) if scope else enumName
      try:
        members = tree.getEnumRecord(fullName)['members']
      except ValueError:
        continue
      for memberName, number in members:
        if memberName == name:
          return number
    #  An enum without a name of its own is in no list of enums. Its
    #  names are found in the record of the class that writes it.
    for scope in (className, *tree.getAncestors(className)):
      for child in tree.getClassRecord(scope).get('inner', ()):
        if child.get('kind') != 'EnumDecl' or child.get('name'):
          continue
        collected = DependencyTree._collectEnumMembers(child)
        if collected['unsure'] is not None:
          continue
        for memberName, number in collected['members']:
          if memberName == name:
            return number
    return None

  def _findNumber(self, node: Optional[Record]) -> Any:
    """
    Gives the number a default of Qt stands for, as an 'int', a 'float'
    or a 'bool', or None when it is no plain number.
    """
    node = self._unwrap(node)
    if node is None:
      return None
    kind = node.get('kind')
    if kind == 'CXXBoolLiteralExpr':
      return True if node.get('value') else False
    if kind == 'IntegerLiteral':
      return int(node['value'])
    if kind == 'FloatingLiteral':
      return float(node['value'])
    if kind == 'UnaryOperator' and node.get('opcode') in ('-', '+'):
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      number = self._findNumber(inner[0]) if inner else None
      if number is None or isinstance(number, bool):
        return None
      return -number if node['opcode'] == '-' else number
    if kind == 'BinaryOperator' and node.get('opcode') in ('+', '-', '*'):
      #  Qt writes some numbers as a sum, as 'Qt::UserRole + 1'.
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      if len(inner) != 2:
        return None
      left, right = self._findNumber(inner[0]), self._findNumber(inner[1])
      for number in (left, right):
        if number is None or isinstance(number, bool):
          return None
      if node['opcode'] == '+':
        return left + right
      return left - right if node['opcode'] == '-' else left * right
    if kind == 'DeclRefExpr':
      referenced = node.get('referencedDecl', dict())
      if referenced.get('kind') == 'EnumConstantDecl':
        return self._findEnumNumber(referenced)
      if referenced.get('kind') == 'VarDecl':
        return self._findConstantNumber(referenced)
    return None

  def _findConstantNumber(self, referenced: Record) -> Any:
    """
    Gives the number of a constant of a class of Qt that a default
    refers to, as 'QLocale::DefaultTwoDigitBaseYear', which is 1900.

    What the compiler wrote down of the reference holds the name of
    the constant and not its class. So the constants of every cute
    class are gathered once for each tree, and a name is taken when
    the classes that have it agree on one number.

    Returns
    -------

    Any
      The number, or None when no class has such a constant, or the
      classes that have one disagree.
    """
    tree = self.getDependencyTree()
    with self.__constant_lock__:
      numbers = self.__constant_numbers__.get(id(tree), None)
      if numbers is None:
        #  Kept before it is filled: a constant written in terms of
        #  another one asks here again, and finds what is there so far.
        numbers = dict()
        self.__constant_numbers__[id(tree)] = numbers
        for className in self.getCuteNames():
          for child in tree.getClassRecord(className).get('inner', ()):
            if child.get('kind') != 'VarDecl':
              continue
            if not child.get('constexpr', False):
              continue
            written = child.get('inner', ())
            written = [c for c in written if isinstance(c, dict)]
            number = self._findNumber(written[0]) if written else None
            if number is None or isinstance(number, bool):
              continue
            numbers.setdefault(child.get('name'), set()).add(number)
    found = numbers.get(referenced.get('name'), ())
    return [*found][0] if len(found) == 1 else None

  def _findJoinedNames(self, node: Optional[Record]) -> Optional[List[str]]:
    """
    Gives the names of the members of an enum that a default of Qt
    stands for: the one name it refers to, or the names it joins with
    '|', as 'DrawWindowBackground | DrawChildren'. Gives None when the
    default is anything else.
    """
    node = self._unwrap(node)
    if node is None:
      return None
    kind = node.get('kind')
    inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
    if kind in ('CXXFunctionalCastExpr', 'CXXStaticCastExpr'):
      return self._findJoinedNames(inner[0]) if inner else None
    if kind in ('CXXConstructExpr', 'CXXTemporaryObjectExpr'):
      given = self._findGiven(node)
      return self._findJoinedNames(given[0]) if len(given) == 1 else None
    if kind == 'DeclRefExpr':
      referenced = node.get('referencedDecl', dict())
      if referenced.get('kind') != 'EnumConstantDecl':
        return None
      return [referenced.get('name')]
    if kind == 'BinaryOperator' and node.get('opcode') == '|':
      joined = inner
    elif kind == 'CXXOperatorCallExpr' and inner:
      called = self._unwrap(inner[0]) or dict()
      if called.get('referencedDecl', dict()).get('name') != 'operator|':
        return None
      joined = inner[1:]
    else:
      return None
    names = []  # type: List[str]
    for part in joined:
      found = self._findJoinedNames(part)
      if found is None:
        return None
      names.extend(found)
    return names or None

  def _findMadeOf(self, node: Optional[Record]) -> Optional[Tuple[str, ...]]:
    """
    Says in Python one thing a default of Qt makes a value of, as the
    'Qt::white' of 'QColor(Qt::white)': a number written out, or a
    member of an enum of the namespace Qt, which every class file has
    at hand.

    Returns
    -------

    Optional[Tuple[Any, ...]]
      None when it is anything else. Else the kind, 'number', 'enum' or
      'value'; the enum or the class as C++ names it, or '' for a
      number; the text in Python, as '0', 'Qt.GlobalColor.white' or
      'QPoint(0, 0)'; and the late classes the text names, which have
      to be brought in before it is run.
    """
    node = self._unwrap(node)
    if node is None:
      return None
    kind = node.get('kind')
    if kind in ('CXXTemporaryObjectExpr', 'CXXConstructExpr'):
      #  A value made of what this very method can say, as the
      #  'QPoint(0, 0)' of 'QRect(QPoint(0, 0), QSize(-1, -1))'.
      cppName = node.get('type', dict()).get('qualType', '')
      cppName = cppName.replace('const ', '').strip()
      found = self._findClass(cppName)
      if not isinstance(found, dict):
        return None
      parts = [self._findMadeOf(one) for one in self._findGiven(node)]
      if any(part is None for part in parts):
        return None
      if parts and not self._canBeMadeOf(cppName, parts):
        return None
      if not parts and not self._canBeMadeEmpty(cppName):
        return None
      brings = [name for part in parts for name in part[3]]
      if found['late'] and found['bring']:
        brings.append(found['bring'])
      made = '%s(%s)' % (
          found['holder'], ', '.join(part[2] for part in parts))
      return ('value', cppName, made, (*brings,))
    if kind == 'DeclRefExpr':
      referenced = node.get('referencedDecl', dict())
      if referenced.get('kind') != 'EnumConstantDecl':
        return None
      enumName = referenced.get('type', dict()).get('qualType', '')
      if not enumName.startswith('Qt::'):
        return None
      found = self._findEnum(enumName, False)
      if not isinstance(found, dict):
        return None
      name = referenced.get('name')
      record = found['generator'].getEnumRecord()
      if all(name != member for member, _ in record['members']):
        return None
      name = self.__python_words__.get(name, name)
      return ('enum', enumName, '%s.%s' % (found['entry'], name), ())
    literals = ('IntegerLiteral', 'FloatingLiteral')
    if kind == 'UnaryOperator':
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      below = self._unwrap(inner[0]) if inner else None
      if below is None or below.get('kind') not in literals:
        return None
    elif kind not in literals:
      return None
    number = self._findNumber(node)
    if number is None or isinstance(number, bool):
      return None
    return ('number', '', repr(number), ())

  def _canBeMadeOf(self, className: str, parts: List[Any]) -> bool:
    """Says whether the cute class of a class of Qt can be made of what
    '_findMadeOf' gave: whether it has a ritual for a constructor
    taking just that: number for number, enum for enum and value for
    value."""
    for plan in self.getRitualGenerator(className).getWritten():
      if plan['kind'] != 'constructor':
        continue
      arguments = plan['arguments']
      if len(arguments) != len(parts):
        continue
      for argument, part in zip(arguments, parts):
        kind, cppName, passing = part[0], part[1], argument['passing']
        if passing['kind'] != kind:
          break
        if kind == 'number' and passing['className'] == 'char':
          break
        if kind == 'enum' and argument['written'] != cppName:
          break
        if kind == 'value' and passing['className'] != cppName:
          break
      else:
        return True
    return False

  @staticmethod
  def _findGiven(node: Record) -> List[Record]:
    """Gives what a default of Qt hands to the constructor it calls,
    leaving out what that constructor fills in itself."""
    return [
        child for child in node.get('inner', ())
        if isinstance(child, dict)
        and child.get('kind') != 'CXXDefaultArgExpr'
    ]

  def _findDefault(self, argument: Record, parameter: Record) -> Any:
    """
    Says in Python what Qt fills in for an argument that is left out.

    Parameters
    ----------

    argument : Record
      The argument as the plan of the ritual has it.

    parameter : Record
      The same argument as this generator has it in Python.

    Returns
    -------

    Optional[Record]
      None when it cannot be said in Python. Else 'text': the default
      of the Python argument, as 'None' or '-1'; and for a value that
      has to be made anew for each call, 'made': what makes it, as
      'QPoint()'.
    """
    node = self._unwrap(argument['default'])
    if node is None:
      return None
    kind, nodeKind = parameter['kind'], node.get('kind')
    making = ('CXXTemporaryObjectExpr', 'CXXConstructExpr')
    if nodeKind == 'CXXFunctionalCastExpr':
      inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
      node = self._unwrap(inner[0]) if inner else None
      if node is None:
        return None
      nodeKind = node.get('kind')
    if kind in ('address', 'chars'):
      if nodeKind == 'CXXNullPtrLiteralExpr':
        return dict(text='None')
      if nodeKind == 'IntegerLiteral' and node.get('value') == '0':
        return dict(text='None')
      if kind == 'address' and nodeKind == 'CallExpr':
        return self._findCalledDefault(node, parameter)
      return None
    if kind == 'number':
      number = self._findNumber(node)
      if number is None:
        return None
      wanted = parameter['annotation']
      if wanted == 'bool':
        return dict(text=repr(True if number else False))
      if wanted == 'float':
        return dict(text=repr(float(number)))
      if isinstance(number, float):
        return None
      return dict(text=repr(int(number)))
    if kind in ('enum', 'flags'):
      if nodeKind in making and not self._findGiven(node):
        if kind == 'flags':
          return dict(text='%s()' % parameter['entry'])
        return None
      #  One member, or for flags several joined with '|', as Qt's
      #  'RenderFlags(DrawWindowBackground | DrawChildren)'.
      names = self._findJoinedNames(node)
      if names is None or (len(names) > 1 and kind != 'flags'):
        return None
      record = parameter['enumGenerator'].getEnumRecord()
      members = [name for name, _ in record['members']]
      if any(name not in members for name in names):
        return None
      words = self.__python_words__
      return dict(text=' | '.join(
          '%s.%s' % (parameter['entry'], words.get(name, name))
          for name in names))
    if kind == 'text':
      if nodeKind in making and not self._findGiven(node):
        return dict(text="''")
      return None
    if kind == 'value':
      if nodeKind not in making:
        return None
      given = self._findGiven(node)
      if not given:
        if self._canBeMadeEmpty(parameter['className']):
          made = '%s()' % parameter['holder']
          return dict(text='None', made=made)
        return None
      #  A value Qt makes of numbers written out, of a member of an
      #  enum of the namespace Qt, or of such values in turn:
      #  'QMarginsF(0, 0, 0, 0)', 'QColor(Qt::white)',
      #  'QRect(QPoint(0, 0), QSize(-1, -1))'.
      parts = [self._findMadeOf(one) for one in given]
      if any(part is None for part in parts):
        return None
      if not self._canBeMadeOf(parameter['className'], parts):
        return None
      made = '%s(%s)' % (
          parameter['holder'], ', '.join(part[2] for part in parts))
      brings = []  # type: List[str]
      for part in parts:
        brings.extend(n for n in part[3] if n not in brings)
      return dict(text='None', made=made, brings=(*brings,))
    return None

  def _findCalledDefault(self, node: Record, parameter: Record) -> Any:
    """
    Says in Python what Qt fills in for an object it gets by calling a
    function of the class of that object with nothing handed over, as
    'QPointingDevice::primaryPointingDevice()' for the device of a
    'QMouseEvent'.

    None stands for no object there, so it cannot also stand for an
    argument that was left out. '...' does: no signature takes it, so
    it reaches the function only where the argument is left out.

    Parameters
    ----------

    node : Record
      The call, as the compiler wrote it down.

    parameter : Record
      The argument as this generator has it in Python.

    Returns
    -------

    Optional[Record]
      None when it cannot be said in Python: the call hands something
      over, or the cute class of the object has no such function that
      is called on no object and with nothing. Else 'text': '...';
      'left': the same, what the function finds there; 'made': the
      call in Python; 'brings': the class it is called on.
    """
    inner = [c for c in node.get('inner', ()) if isinstance(c, dict)]
    if not inner:
      return None
    if any(c.get('kind') != 'CXXDefaultArgExpr' for c in inner[1:]):
      return None
    called = self._unwrap(inner[0])
    if called is None or called.get('kind') != 'DeclRefExpr':
      return None
    referenced = called.get('referencedDecl', dict())
    if referenced.get('kind') != 'CXXMethodDecl':
      return None
    name, className = referenced.get('name'), parameter['className']
    found = [
        plan for plan in self.getRitualGenerator(className).getWritten()
        if plan['kind'] == 'static method'
        and plan['function'].split('(')[0].endswith(
            ' *%s::%s' % (className, name))
    ]
    if len(found) != 1:
      return None
    for argument in found[0]['arguments']:
      if argument.get('default') is None:
        return None
    made = '%s.%s()' % (parameter['holder'], name)
    return dict(text='...', left='...', made=made, brings=(className,))

  def _canBeMadeEmpty(self, className: str) -> bool:
    """Says whether the cute class of a class of Qt can be made with
    nothing given: whether it has a ritual for such a constructor."""
    for plan in self.getRitualGenerator(className).getWritten():
      if plan['kind'] == 'constructor' and not plan['arguments']:
        return True
    return False

  def _canBeOwned(self, className: str) -> bool:
    """Says whether Python can own a C++ object of a class: whether
    C++ can copy it, and a ritual removes it."""
    tree = self.getDependencyTree()
    if className not in tree.getCopyableNames():
      return False
    for plan in self.getRitualGenerator(className).getWritten():
      if plan['kind'] == 'destructor':
        return True
    return False

  def isApplication(self) -> bool:
    """Says whether the class is Qt's application, or built on it."""
    tree, className = self.getDependencyTree(), self.getClassName()
    if className == self.__application_name__:
      return True
    return self.__application_name__ in tree.getAncestors(className)

  def getDeleteRitual(self) -> Optional[str]:
    """
    Gives the ritual removing a C++ object of the class, for a class
    whose C++ objects are values, which Python owns. Gives None for
    any other class.
    """
    if not self._canBeOwned(self.getClassName()):
      return None
    for plan in self.getRitualGenerator().getWritten():
      if plan['kind'] == 'destructor':
        return plan['ritualName']
    return None

  def _planParameter(self, argument: Record, static: bool) -> Any:
    """
    Says how one argument of a Qt function looks in Python.

    Parameters
    ----------

    argument : Record
      The argument as the plan of the ritual has it.

    static : bool
      Whether the function is called on no object, so that it has no
      'self' to reach a helper through.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the function cannot be written for
      this argument. Else a record: 'name', 'kind', 'entry' (what
      stands for it in a signature), 'annotation', 'passed' (what the
      ritual is handed), 'words' (what its docstring says) and 'late'.
    """
    passing, name = argument['passing'], argument['name']
    if keyword.iskeyword(name):
      name = '%s_' % name
    kind = passing['kind']
    helper = 'CuteMixin' if static else 'self'
    record = dict(
        name=name, kind=kind, late=False, nullable=False, default=None,
    )
    if kind == 'number':
      number = passing['className']
      if number == 'char':
        return 'takes a single letter as C has it'
      annotation = self.__python_numbers__.get(number, 'int')
      return dict(
          record, entry=annotation, annotation=annotation, passed=name,
          words='Passed on as it is.',
      )
    if kind in ('text', 'view'):
      words = 'Passed on as it is: a QString is made of it for the call.'
      return dict(
          record, kind='text', entry='str', annotation='str',
          passed=name, words=words,
      )
    if kind == 'chars':
      return dict(
          record, entry='str', annotation='str',
          passed='%s._bytesOf(%s)' % (helper, name),
          words='Passed on as the bytes of the text.',
      )
    if kind in ('enum', 'flags'):
      plain = argument['plain']
      if kind == 'flags':
        enumName = passing['className'][len('QFlags<'):-1]
      else:
        enumName = plain
      found = self._findEnum(enumName, kind == 'flags')
      if found is None:
        infoSpec = """names the enum '%s', whose class cannot be named
        here"""
        return ' '.join((infoSpec % enumName).split())
      if found['owner']:
        self._note('classes', found['owner'])
      return dict(
          record, entry=found['entry'], annotation=found['shown'],
          passed='%s.value' % name, words='Passed on as its number.',
          enumGenerator=found['generator'], key='enum %s' % enumName,
      )
    if kind == 'map':
      found = self._findMap(passing['mapped'])
      if isinstance(found, str):
        return 'names %s' % found
      infoSpec = """Passed on as a map of Qt: Qt reads the C++ map,
      which stays Python's own. A dict of Python is made into one
      first, and refused when a key or a value does not fit."""
      return dict(
          record, entry=found['entry'], annotation=found['name'],
          passed='%s._valueOf(%s)' % (helper, name),
          words=' '.join(infoSpec.split()), late=found['late'],
          lateName=found['lateName'], className=found['className'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'], key='map %s' % found['entry'],
      )
    if kind == 'list':
      found = self._findList(passing['listed'])
      if isinstance(found, str):
        return 'names %s' % found
      infoSpec = """Passed on as a list of Qt: Qt reads the C++ list,
      which stays Python's own. A list or tuple of Python is made into
      one first, and refused when an element does not fit."""
      return dict(
          record, entry=found['entry'], annotation=found['name'],
          passed='%s._valueOf(%s)' % (helper, name),
          words=' '.join(infoSpec.split()), late=found['late'],
          lateName=found['lateName'], className=found['className'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'], key='list %s' % found['className'],
      )
    if kind in ('address', 'value'):
      if kind == 'address':
        pointed = argument['plain'][:-2]
        if pointed.startswith('const '):
          pointed = pointed[6:]
      else:
        pointed = passing['className']
      found = self._findClass(pointed)
      if isinstance(found, str):
        return found
      if found is None:
        return "names '%s', which has no cute class yet" % pointed
      #  A class other classes are built on beside another is named, so
      #  that the address is that of its part of the object.
      part = ", '%s'" % pointed if pointed in self._getPartNames() else ''
      if kind == 'address':
        passed = '%s._addressOf(%s%s)' % (helper, name, part)
        words = 'Passed on as the address of its C++ object.'
      else:
        passed = '%s._valueOf(%s%s)' % (helper, name, part)
        infoSpec = """Passed on as a value: Qt reads the C++ %s, which
        stays Python's own."""
        words = ' '.join((infoSpec % pointed).split())
      return dict(
          record, entry=found['entry'], annotation=found['name'],
          passed=passed, words=words, late=found['late'],
          className=pointed, bring=found['bring'], hint=found['hint'],
          holder=found['holder'], key='class %s' % pointed,
      )
    if kind == 'number address':
      return 'takes a number to change where it is'
    return 'takes a type Python has no way to hand over yet'

  def _planGiving(self, plan: Record, static: bool) -> Any:
    """
    Says how what a Qt function gives looks in Python.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the function cannot be written for
      what it gives. Else a record: 'kind', 'annotation', 'words'
      (what the docstring says under 'Returns', or ''), and for a class
      'name' and 'late'.
    """
    giving = plan['giving']
    kind = giving['kind']
    if kind == 'nothing':
      return dict(kind=kind, annotation='None', words='')
    if kind == 'number':
      annotation = self.__python_numbers__.get(giving['className'], 'int')
      if giving['className'] == 'char':
        return 'gives a single letter as C has it'
      return dict(kind=kind, annotation=annotation, words='')
    if kind in ('text', 'view'):
      words = 'The text Qt gave back.'
      return dict(kind='text', annotation='str', words=words)
    if kind == 'chars':
      self._note('typing', 'Optional')
      words = 'The text Qt gave back. None when Qt gave back no text.'
      return dict(kind=kind, annotation='Optional[str]', words=words)
    if kind in ('enum', 'flags'):
      written = RitualGenerator._stripReadOnly(giving['written'])
      tables = self.getRitualGenerator()._getTypeTables()
      plain = self.getRitualGenerator()._followAliases(written)
      if kind == 'flags':
        enumName = giving['className'][len('QFlags<'):-1]
      else:
        enumName = plain if plain in tables['enums'] else written
      found = self._findEnum(enumName, kind == 'flags')
      if found is None:
        infoSpec = """gives the enum '%s', whose class cannot be named
        here"""
        return ' '.join((infoSpec % enumName).split())
      if found['owner']:
        self._note('classes', found['owner'])
      if kind == 'enum':
        infoSpec = """The member standing for the number Qt gave back.
        For a number Qt gives no name it is the member without a name
        that '%s(number)' gives."""
        words = ' '.join((infoSpec % found['shown']).split())
      else:
        words = 'The value standing for the combination Qt gave back.'
      maker = found['entry']
      if found.get('own'):
        #  An enum of this class, and the name Qt has for the
        #  combinations of a flags enum of it, are bound in the body of
        #  the class alone, so a function reaches them through the class.
        maker = '%s.%s' % (self.getDottedName(), maker)
      return dict(
          kind=kind, annotation=found['shown'], words=words,
          entry=found['entry'], maker=maker,
      )
    if kind == 'map':
      found = self._findMap(giving['mapped'])
      if isinstance(found, str):
        return 'gives %s' % found
      infoSpec = """A new cute map around the copy Qt gave back. Python
      owns it."""
      return dict(
          kind=kind, annotation=found['name'], name=found['name'],
          words=' '.join(infoSpec.split()), late=found['late'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'],
      )
    if kind == 'list':
      found = self._findList(giving['listed'])
      if isinstance(found, str):
        return 'gives %s' % found
      infoSpec = """A new cute list around the copy Qt gave back. Python
      owns it."""
      return dict(
          kind=kind, annotation=found['name'], name=found['name'],
          words=' '.join(infoSpec.split()), late=found['late'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'],
      )
    if kind in ('address', 'value'):
      if kind == 'address':
        pointed = self.getRitualGenerator()._followAliases(
            giving['written'])
        pointed = pointed[:-2] if pointed.endswith(' *') else pointed
        if pointed.startswith('const '):
          pointed = pointed[6:]
        pointed = self.getRitualGenerator()._followAliases(pointed)
      else:
        pointed = giving['className']
      found = self._findClass(pointed)
      if isinstance(found, str):
        return found.replace('names', 'gives', 1)
      if found is None:
        return "gives '%s', which has no cute class yet" % pointed
      if kind == 'value' and not self._canBeOwned(pointed):
        infoSpec = """gives a value of '%s', which Python cannot own: no
        ritual removes one"""
        return ' '.join((infoSpec % pointed).split())
      if kind == 'address':
        self._note('typing', 'Optional')
        annotation = 'Optional[%s]' % found['name']
        infoSpec = """The cute object standing for what Qt gave back.
        None when Qt gave back no object."""
      else:
        annotation = found['name']
        infoSpec = """A new cute %s around the copy Qt gave back. Python
        owns it."""
        infoSpec = infoSpec % pointed
      return dict(
          kind=kind, annotation=annotation, name=found['name'],
          words=' '.join(infoSpec.split()), late=found['late'],
          bring=found['bring'], hint=found['hint'],
          holder=found['holder'],
      )
    return 'gives a type Python has no way to take yet'

  def _planFunction(self, plan: Record) -> Any:
    """
    Works out the function of one ritual: its name, its arguments and
    what it gives, in Python.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when the ritual gets no function. Else the
      function, as 'getFunctions' gives it, with its signatures still
      to be decided.
    """
    kind, name = plan['kind'], plan['name']
    if kind == 'destructor':
      if self.getDeleteRitual() is None:
        return 'the destructor: Python never removes a C++ %s' % (
            self.getClassName(),)
      infoSpec = """the destructor: Python removes its C++ %s by it, and
      has no other use for it"""
      return ' '.join((infoSpec % self.getClassName()).split())
    operator = None  # type: Optional[Record]
    if name.startswith('operator'):
      operator = self._planOperator(plan)
      if isinstance(operator, str):
        return operator
    if name.startswith('qt_'):
      return "one of Qt's own inner workings"
    static = kind != 'method'
    parameters = []  # type: List[Record]
    arguments = [*plan['arguments']]
    selfPassed = ''
    if operator is not None and operator['selfIndex'] is not None:
      #  Qt writes the operator as a function of no object, and hands it
      #  the object as an argument. In Python that argument is 'self'.
      taken = dict(arguments.pop(operator['selfIndex']), name='self')
      own = self._planParameter(taken, True)
      if isinstance(own, str):
        return own
      selfPassed = own['passed']
    while arguments:
      argument = arguments.pop(0)
      passing = argument['passing']
      following = arguments[0]['passing']['kind'] if arguments else ''
      if passing['kind'] == 'number address':
        if following == 'texts address':
          #  The texts a program was started with, and how many they
          #  are, are one argument in Python: a list of them.
          texts = arguments.pop(0)
          helper = 'CuteMixin' if static and kind != 'constructor' else (
              'self')
          infoSpec = """The texts the program was started with, as
          'sys.argv'. Passed on as Qt takes them: how many they are,
          and where the first one is."""
          parameters.append(dict(
              name=texts['name'], kind='texts', late=False,
              nullable=False, default=None, entry='list',
              annotation='list',
              passed='*%s._startTextsOf(%s)' % (helper, texts['name']),
              words=' '.join(infoSpec.split()),
          ))
          continue
      parameter = self._planParameter(
          argument, static and kind != 'constructor')
      if isinstance(parameter, str):
        return parameter
      parameter['argument'] = argument
      parameters.append(parameter)
    gives = None  # type: Optional[Record]
    if kind != 'constructor':
      gives = self._planGiving(plan, static)
      if isinstance(gives, str):
        return gives
    pythonName = '__init__' if kind == 'constructor' else name
    if operator is not None:
      pythonName = operator['pythonName']
    if keyword.iskeyword(pythonName):
      pythonName = '%s_' % pythonName
    #  What Qt fills in, from the last argument backwards for as long as
    #  it can be said in Python.
    for parameter in reversed(parameters):
      argument = parameter.get('argument')
      if argument is None or argument['default'] is None:
        break
      default = self._findDefault(argument, parameter)
      if default is None:
        break
      parameter['default'] = default
    for parameter in parameters:
      #  C++ lets nothing be given wherever an address is taken.
      if parameter['kind'] in ('address', 'chars'):
        parameter['nullable'] = True
    return dict(
        pythonName=pythonName, plan=plan, kind=kind,
        parameters=parameters, gives=gives, operator=operator,
        selfPassed=selfPassed, inPlace=plan.get('inPlace', False),
    )

  def _planOperator(self, plan: Record) -> Any:
    """
    Says which name Python has for an operator of Qt, and which of its
    arguments is the object in Python.

    Python has solved operators already, and the cute class goes by
    it: 'a + b' asks 'a.__add__(b)', and when that gives
    'NotImplemented' it asks 'b.__radd__(a)'. An operator Qt writes
    with 'friend' inside the class is a function of no object, taking
    both sides as arguments. Where the class stands first it is the
    plain name, and where it stands second the name Python asks the
    right side for.

    Returns
    -------

    Union[Record, str]
      The reason, in words, when Python has no name for the operator.
      Else 'pythonName': the name, as '__add__'; and 'selfIndex': the
      place of the argument that is 'self' in Python, or None for an
      operator Qt writes as a function of the object.
    """
    kind, symbol = plan['kind'], plan['name'][len('operator'):].strip()
    count, className = len(plan['arguments']), self.getClassName()
    binary, unary = self.__binary_operators__, self.__unary_operators__
    noName = 'an operator Python has no name for'
    if kind == 'friend':
      own = [
          argument['passing'].get('kind') == 'value'
          and argument['passing'].get('className') == className
          for argument in plan['arguments']
      ]
      if count == 1 and own[0] and symbol in unary:
        return dict(pythonName=unary[symbol], selfIndex=0)
      if count != 2 or symbol not in binary:
        return noName
      if own[0]:
        return dict(pythonName=binary[symbol][0], selfIndex=0)
      if own[1]:
        return dict(pythonName=binary[symbol][1], selfIndex=1)
      return 'an operator between other classes, written inside this one'
    if kind != 'method':
      return noName
    if symbol == '=':
      return 'assignment: Python binds a name and has no operator for it'
    if symbol in self.__in_place_operators__ and count == 1:
      if not plan.get('inPlace', False):
        return noName
      name = self.__in_place_operators__[symbol]
      return dict(pythonName=name, selfIndex=None)
    if count == 1 and symbol in binary:
      return dict(pythonName=binary[symbol][0], selfIndex=None)
    if count == 0 and symbol in unary:
      return dict(pythonName=unary[symbol], selfIndex=None)
    if symbol == '[]' and count == 1:
      return dict(pythonName='__getitem__', selfIndex=None)
    if symbol == '()':
      return dict(pythonName='__call__', selfIndex=None)
    if symbol == 'bool' and count == 0:
      return dict(pythonName='__bool__', selfIndex=None)
    return noName

  @staticmethod
  def _findSection(function: Record) -> str:
    """Gives the section of the class body a function stands in."""
    plan = function['plan']
    if function.get('operator') is not None:
      return 'Python API'
    if function['kind'] == 'constructor':
      return 'CONSTRUCTORS'
    if function['kind'] == 'static method':
      return 'STATIC METHODS'
    name = plan['name']
    if name.startswith('set') and name[3:4].isupper():
      return 'SETTERS'
    if 'const' in plan['words'] and function['gives']['kind'] != 'nothing':
      return 'GETTERS'
    return 'PUBLIC METHODS'

  def _createSignatures(self, function: Record) -> None:
    """
    Gives a function its signatures: the full call first decided, then
    one for each call that leaves out what Qt fills in, and one more
    for each place None is taken. A signature naming a late class is
    one of them as any other.
    """
    parameters = function['parameters']
    fewest = len(parameters)
    for parameter in reversed(parameters):
      if parameter['default'] is None:
        break
      fewest -= 1
    signatures = []  # type: List[Tuple[str, ...]]
    keys = []  # type: List[Tuple[str, ...]]
    for count in range(fewest, len(parameters) + 1):
      built = [((), ())]  # type: List[Tuple[Tuple, Tuple]]
      for parameter in parameters[:count]:
        #  The class of an enum has two names where Qt names its
        #  combinations apart, and a class of Qt may be written as
        #  'THIS'. What a signature takes goes by the class itself.
        entry = parameter['entry']
        entries = [(entry, parameter.get('key', entry))]
        if parameter['nullable']:
          entries.append(('NoneType', 'NoneType'))
        built = [
            ((*shown, text), (*known, key))
            for shown, known in built for text, key in entries
        ]
      signatures.extend(shown for shown, _ in built)
      keys.extend(known for _, known in built)
    function['signatures'] = signatures
    function['signatureKeys'] = keys

  def _isMoreSpecial(self, first: Tuple, other: Tuple) -> bool:
    """
    Says whether one signature takes only calls another takes as well,
    and not every one of them: whether a class in it is built on the
    class at the same place of the other.
    """
    if len(first) != len(other) or first == other:
      return False
    tree, className = self.getDependencyTree(), self.getClassName()
    for one, another in zip(first, other):
      if one == another:
        continue
      one = className if one == 'THIS' else one
      another = className if another == 'THIS' else another
      try:
        ancestors = tree.getAncestors(one)
      except LookupError:
        return False
      if another not in ancestors:
        return False
    return True

  def _createFunctions(self) -> None:
    """Decides the functions of the cute class and what is left out."""
    self.__needed_names__ = collections.defaultdict(list)
    planned, leftOut = [], []  # type: List[Record], List[Tuple[str, str]]
    enumNames = set()  # type: Set[str]
    for generator in self.getEnumGenerators():
      enumNames.add(generator.getOwnName())
      flagsName = generator.getFlagsName()
      if flagsName:
        enumNames.add(flagsName.rpartition('::')[2])
    #  Three kinds of ritual are no function of the class by
    #  themselves. The one of a class the class is built on after the
    #  first, which the class names in '__cast_rituals__'. The one that
    #  hands a Python function over, which it names in
    #  '__take_ritual__'. And the one that runs just the class's own
    #  function, where the ordinary ritual lets C++ look the function
    #  up in the object: it belongs to the function of that name.
    apart = ('cast', 'take', 'own', 'list', 'map')
    written = self.getRitualGenerator().getWritten()
    start = len('ritual_own')
    owned = {
        plan['ritualName'][start:]: plan for plan in written
        if plan['kind'] == 'own'
    }
    plans = [plan for plan in written if plan['kind'] not in apart]
    ordinary = {plan['ritualName'][len('ritual'):] for plan in plans}
    for compilerName, plan in owned.items():
      if compilerName not in ordinary:
        #  A function only a class built on this one may call has no
        #  ordinary ritual. The one running the class's own is its one.
        plans.append(dict(plan, kind='method', ownOnly=True))
    for plan in plans:
      function = self._planFunction(plan)
      if isinstance(function, str):
        leftOut.append((plan['function'], function))
        continue
      if function['pythonName'] in enumNames:
        infoSpec = """the class has an enum of that name, which holds
        the name"""
        leftOut.append((plan['function'], ' '.join(infoSpec.split())))
        continue
      function['section'] = self._findSection(function)
      compilerName = plan['ritualName'][len('ritual'):]
      if not plan.get('ownOnly') and compilerName in owned:
        function['ownRitual'] = owned[compilerName]['ritualName']
      self._createSignatures(function)
      planned.append(function)
    byName = collections.OrderedDict()  # type: Dict[str, List[Record]]
    for function in planned:
      byName.setdefault(function['pythonName'], []).append(function)
    functions = []  # type: List[Record]
    for pythonName, group in byName.items():
      #  Where Qt has, under one name, a function called on an object
      #  and one called on the class, as 'file.exists()' beside
      #  'QFile.exists(fileName)', both are written under that name, the
      #  one called on the class with '@staticmethod', as Qt declares
      #  them. worktoy reaches the first through an object and the
      #  second through the class.
      #  A call an earlier function of the name takes already is not
      #  taken again. A function called on an object and one called on
      #  the class never take the same call, so each kind is looked at
      #  apart.
      taken = dict()  # type: Dict[Tuple[Any, ...], str]
      kept = []
      for function in group:
        shown, kind = function['plan']['function'], function['kind']
        if kind != 'static method':
          #  An operator Qt writes with 'friend' is called on an object
          #  in Python, as a function of the object is.
          kind = 'method'
        pairs = [*zip(function['signatures'], function['signatureKeys'])]
        fresh = [(s, k) for s, k in pairs if (kind, k) not in taken]
        if not fresh:
          full = function['signatureKeys'][-1]
          infoSpec = """takes in Python what '%s' takes"""
          leftOut.append((shown, infoSpec % taken[(kind, full)]))
          continue
        function['signatures'] = [s for s, _ in fresh]
        function['signatureKeys'] = [k for _, k in fresh]
        for _, key in fresh:
          taken[(kind, key)] = shown
        kept.append(function)
      #  worktoy asks the signatures of one class in the order written,
      #  so the more special one is written first.
      ordered = []  # type: List[Record]
      for function in kept:
        place = len(ordered)
        for index, earlier in enumerate(ordered):
          pairs = [
              (mine, theirs) for mine in function['signatures']
              for theirs in earlier['signatures']
          ]
          if any(self._isMoreSpecial(*pair) for pair in pairs):
            place = index
            break
        ordered.insert(place, function)
      #  A name Python asks one side of an operator for gets a function
      #  that says 'NotImplemented' to what no signature takes, so that
      #  Python goes on to ask the other side; see '_writeFallback'.
      pairs = self.__binary_operators__.values()
      asked = [name for pair in pairs for name in pair]
      asked.extend(self.__in_place_operators__.values())
      fallback = True if ordered and pythonName in asked else False
      for function in ordered:
        function['section'] = ordered[0]['section']
        function['overloaded'] = True if (
            len(ordered) > 1 or function['signatures'] != [()]
            or function['kind'] == 'constructor' or fallback) else False
      if fallback:
        ordered[-1]['fallbackAfter'] = True
      functions.extend(ordered)
    written = self.getRitualGenerator().getWritten()
    declared = [plan['function'] for plan in written]
    leftOut.sort(key=lambda pair: declared.index(pair[0]))
    for function in functions:
      self._noteFunction(function)
    self.__made_functions__ = (*functions,)
    self.__left_out__ = (*leftOut,)

  def _noteFunction(self, function: Record) -> None:
    """Notes the names the file needs for one function it writes."""
    if function['overloaded']:
      self._note('top', 'overload')
    static = function['kind'] == 'static method'
    if function['kind'] != 'method':
      self._note('top', 'Rituals')
    for signature in function['signatures']:
      if 'THIS' in signature:
        self._note('top', 'THIS')
      if 'NoneType' in signature:
        self._note('top', 'NoneType')
    for parameter in function['parameters']:
      if parameter['nullable']:
        self._note('typing', 'Optional')
      default = parameter['default']
      if default is not None and 'made' in default:
        self._note('typing', 'Optional')
      if static and parameter['kind'] in ('address', 'value', 'chars'):
        self._note('top', 'CuteMixin')
      if parameter.get('late'):
        #  A list waits for the class it holds.
        self._note('late', parameter.get('lateName') or parameter['entry'])
        if parameter['hint']:
          self._note('hinted', parameter['hint'])
      elif parameter.get('bring'):
        self._note('classes', parameter['bring'])
    gives = function['gives']
    if gives and gives.get('late'):
      if gives['hint']:
        self._note('hinted', gives['hint'])
    elif gives and gives.get('bring'):
      self._note('classes', gives['bring'])

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  WRITING  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _getHeading(self) -> List[str]:
    """Says who wrote the file, from what, and that it is written
    anew."""
    tree, className = self.getDependencyTree(), self.getClassName()
    headerPath = tree.getHeaderPath(className)
    relative = os.path.relpath(headerPath, QtPart.getQtHeaderFolder())
    infoSpec = """Written by dev_tooling.ClassGenerator from the records
    of %s, Qt %s. Changes made here are lost."""
    info = infoSpec % (relative, QtPart.getQtVersion())
    return self._wrapWords(info, '#  ')

  def _writeImports(self) -> List[str]:
    """Gives the lines at the top of the file that bring in names."""
    needed = self._getNeeds()
    className = self.getClassName()
    lines = ['from __future__ import annotations', '']
    lines.extend(('from typing import TYPE_CHECKING', ''))
    top = needed['top']
    worktoy = []
    if 'THIS' in top:
      worktoy.append('from worktoy.core.sentinels import THIS')
    if 'overload' in top:
      worktoy.append('from worktoy.dispatch import overload')
    if 'Kee' in top:
      worktoy.append('from worktoy.keenum import Kee')
    if worktoy:
      lines.extend((*worktoy, ''))
    cute = [name for name in (
        'CuteMixin', 'CuteFlags', 'CuteNum', 'MetaCute', 'WAIT',
    ) if name in top]
    ours = []
    if cute:
      ours.append('from ..cute import %s' % ', '.join(cute))
    if 'Rituals' in top:
      ours.append('from ..occult import Rituals')
    classes = [n for n in needed['classes'] if n != className]
    #  The namespace 'Qt', the classes this one is built on, and each
    #  class that holds an enum or a class this file names, are asked of
    #  the package of their part, the cute way. The package brings in
    #  the one file each of them is in, and no other.
    for partName in self.__part_order__:
      names = sorted(n for n in classes if self.getPartName(n) == partName)
      if partName == 'QtCore':
        #  'QList' and 'QStringList' are classes of QtCore the tree
        #  knows nothing of: cutienator writes them by hand.
        names = sorted({*names, *needed['lists']})
      if partName == 'QtCore' and 'Qt' in needed['namespace']:
        names.insert(0, 'Qt')
      ours.extend(self._writeAsking(partName, names, ''))
    lines.extend(ours)
    typing = sorted(needed['typing'])
    #  What this class waits for. A class written inside it binds its
    #  own 'WAIT' lines, in its body.
    late = sorted(self.__needed_names__['late'])
    #  What the annotations name and the file does not bring in.
    hinted = {*late, *needed['hinted']}
    hinted = sorted(hinted - {className, *classes})
    if typing or hinted:
      lines.append('')
      lines.append('if TYPE_CHECKING:  # pragma: no cover, no mutate')
    if typing:
      lines.append('  from typing import %s' % ', '.join(typing))
    if typing and hinted:
      lines.append('')
    #  A type checker is shown each class the cute way, from the
    #  package of its part. Python never runs these lines, so they
    #  bring nothing in.
    for partName in self.__part_order__:
      names = [n for n in hinted if self.getPartName(n) == partName]
      lines.extend(self._writeAsking(partName, names, '  '))
    if late:
      lines.append('else:')
      infoSpec = """The cute classes this file names and is not built on.
      Each is brought in by the program that uses it, and a signature
      naming it waits until then; see 'WAIT'."""
      lines.extend(self._wrapWords(infoSpec, '  #  '))
      for lateName in late:
        lines.append("  %s = WAIT['%s']" % (lateName, lateName))
    if 'NoneType' in top:
      lines.append('')
      infoSpec = """The class of None, for a signature that takes None in
      the place of an object or of text."""
      lines.extend(self._wrapWords(infoSpec, '#  '))
      lines.append('NoneType = type(None)')
    return lines

  def _writeAsking(
      self,
      partName: str,
      names: List[str],
      indent: str,
  ) -> List[str]:
    """
    Gives the lines that ask the package of one part of Qt for names of
    it, the cute way: 'from ..QtGui import QFont, QIcon', or
    'from . import QEvent' in a file of that same part. As many names
    stand on a line as fit, and the import is written again for the
    rest. No name gives no line.

    Asking the package is as cheap as asking the file: the package
    brings in the one file a class is in, the first time the class is
    asked for.
    """
    module = '.' if partName == self.getPartName() else '..%s' % partName
    opening, line = '%sfrom %s import ' % (indent, module), ''
    lines = []  # type: List[str]
    for name in names:
      longer = '%s, %s' % (line, name) if line else name
      if line and len(opening) + len(longer) > _width():
        lines.append('%s%s' % (opening, line))
        longer = name
      line = longer
    if line:
      lines.append('%s%s' % (opening, line))
    return lines

  def _writeBringing(self, otherName: str, indent: str) -> str:
    """
    Gives the line by which a function brings in the cute class of
    another class of Qt, the cute way: 'from ..QtGui import QFont'. A
    class Qt writes inside another is brought in with that class, as
    'from ..QtCore import QMetaObject' for 'QMetaObject::Connection'.
    """
    asked = otherName.split('::')[0]
    return self._writeAsking(self.getPartName(asked), [asked], indent)[0]

  def _countNotWritten(self) -> List[Tuple[int, str]]:
    """Gives how many functions of the class have no ritual, for each
    reason, the most frequent first."""
    reasons = collections.Counter()  # type: Any
    for _, reason in self.getRitualGenerator().getNotWritten():
      reasons[reason.partition(':')[0]] += 1
    return [
        (count, reason) for reason, count in reasons.most_common() if count
    ]

  def _writeClassDocstring(self) -> List[str]:
    """Gives the docstring of the cute class."""
    className, baseName = self.getClassName(), self.getBaseName()
    functions, leftOut = self.getFunctions(), self.getLeftOut()
    written = self.getRitualGenerator().getWritten()
    notWritten = self.getRitualGenerator().getNotWritten()
    owned = self.getDeleteRitual() is not None
    paragraphs = []  # type: List[Any]
    infoSpec = """The cute side of Qt's %s: a plain Python object
    standing in front of one C++ %s."""
    paragraphs.append(infoSpec % (className, className))
    if baseName is not None:
      infoSpec = """It is built on the cute '%s', as Qt's %s is built on
      Qt's %s, and has everything that class has."""
      info = infoSpec % (baseName, className, baseName)
      for parent in self.getFurtherBaseNames():
        infoSpec = """ It is built on the cute '%s' as well, as Qt's %s
        is built on Qt's %s too, and has everything that class has."""
        info = '%s%s' % (info, ' '.join(
            (infoSpec % (parent, className, parent)).split()))
        info = info.replace('.It is', '. It is')
      for parent in self.getUnreflectedParents():
        infoSpec = """ Qt's %s is built on Qt's %s as well, which is not
        reflected."""
        info = '%s%s' % (info, infoSpec % (className, parent))
      paragraphs.append(info)
    if owned:
      infoSpec = """C++ hands a %s around as a copy, so every C++ %s
      behind a cute one is Python's own: it is removed, by the ritual
      named in '__delete_ritual__', when the cute object goes."""
      paragraphs.append(infoSpec % (className, className))
    names = [*dict.fromkeys(
        f['pythonName'] for f in functions if f['kind'] != 'constructor')]
    makers = [f for f in functions if f['kind'] == 'constructor']
    paragraphs.append(('What exists', None))
    if names:
      infoSpec = """Every function of Qt's %s that has a ritual and that
      Python can call so far, %d %s in all: %s."""
      shown = ', '.join("'%s'" % name for name in names)
      word = 'name' if len(names) == 1 else 'names'
      info = infoSpec % (className, len(names), word, shown)
    else:
      info = """No function of Qt's %s yet.""" % className
    if makers:
      infoSpec = """ It can be made from Python, in %d %s; see
      '__init__'."""
      word = 'way' if len(makers) == 1 else 'ways'
      info = '%s%s' % (info, infoSpec % (len(makers), word))
    else:
      infoSpec = """ None can be made from Python: one comes out of a
      function of another class that gives one back."""
      info = '%s%s' % (info, infoSpec)
    paragraphs.append(info)
    if leftOut:
      paragraphs.append(('What has a ritual and is left out, and why', None))
      for shown, reason in leftOut:
        paragraphs.append(('- ', "Qt's '%s': %s." % (shown, reason)))
    without = len(notWritten)
    if without:
      paragraphs.append(('What has no ritual', None))
      infoSpec = """%d of the %d functions Qt declares:"""
      #  A ritual of our own making stands for no function Qt declares,
      #  and one that runs just the class's own function for one that
      #  has a ritual already.
      ours = ('cast', 'take', 'own', 'list', 'map')
      declared = [plan for plan in written if plan['kind'] not in ours]
      total = len(declared) + len(notWritten)
      counted = '; '.join(
          '%d %s' % pair for pair in self._countNotWritten())
      paragraphs.append(
          '%s %s.' % (infoSpec % (without, total), counted))
    paragraphs.append(('What to expect', None))
    infoSpec = """The C++ %s is created at the first use, not by
    '%s(...)'."""
    if self.isApplication():
      infoSpec = """The C++ %s is created by '%s(...)' at once, since
      nearly every other object of Qt can only be made after it."""
    expected = [infoSpec % (className, className)]
    infoSpec = """A wrong argument is refused in Python, with
    'DispatchException', and never reaches C++."""
    expected.append(infoSpec)
    infoSpec = """None is taken wherever Qt takes an object by its
    address, or text as C has it, and is passed on as nothing. Whether
    Qt can do with nothing there is as in C++."""
    expected.append(infoSpec)
    if owned:
      infoSpec = """A function giving a %s back gives a copy the ritual
      made for Python, in a new cute %s."""
      expected.append(infoSpec % (className, className))
    else:
      infoSpec = """Python never removes the C++ %s."""
      expected.append(infoSpec % className)
    tree = self.getDependencyTree()
    watched = self.__watched_name__
    if className == watched or watched in tree.getAncestors(className):
      infoSpec = """Qt tells when it has removed the C++ %s. Every call
      on the cute object, and every use of it as an argument, then
      raises 'RuntimeError', and nothing reaches C++."""
      expected.append(infoSpec % className)
    for info in expected:
      paragraphs.append(('- ', info))
    lines = ['  """']
    previous = None  # type: Any
    for paragraph in paragraphs:
      if isinstance(paragraph, tuple) and paragraph[1] is None:
        lines.extend(('', '  %s' % paragraph[0]))
        lines.extend(('  %s' % ('-' * len(paragraph[0])), ''))
      elif isinstance(paragraph, tuple):
        lines.extend(self._wrapCpp(paragraph[1], '  - ', '    '))
      else:
        if previous is not None and not isinstance(previous, tuple):
          lines.append('')
        lines.extend(self._wrapWords(paragraph, '  '))
      previous = paragraph
    lines.append('  """')
    return lines

  @staticmethod
  def _writeBanner(sectionName: str) -> List[str]:
    """Gives the three lines that head one section of a class body."""
    full = '  %s#' % ('# ' * ((_width() - 3) // 2))
    head = '  #  %s  ' % sectionName
    if len(head) % 2:
      head = '%s ' % head
    while len(head) < len(full):
      head = '%s# ' % head
    return [full, head.rstrip(), full]

  def _writeNames(self) -> List[str]:
    """
    Gives the lines right under the docstring of the class, which bind
    what the signatures below them name: the classes and the enums Qt
    writes inside the class.

    They stand above every section, since a signature can only name
    what the body has bound on a line above it.
    """
    className, lines = self.getClassName(), []  # type: str, List[str]
    late = sorted(self.__needed_names__['late'])
    if self.isNested() and late:
      infoSpec = """The cute classes this class names and is not built on.
      Each waits until it is made; see 'WAIT'. A type checker reads the
      imports at the top of the file instead."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec, '  #  '))
      lines.append('  if not TYPE_CHECKING:')
      for lateName in late:
        lines.append("    %s = WAIT['%s']" % (lateName, lateName))
    generators = self.getEnumGenerators()
    if generators:
      infoSpec = """The enums Qt writes inside %s, each a class in here
      as in C++, and the names Qt has for the combinations of its flags
      enums."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec % className, '  #  '))
      for generator in generators:
        ownName = generator.getOwnName()
        lines.append('')
        lines.extend(generator.getNestedLines(_width()))
        flagsName = generator.getFlagsName()
        if flagsName:
          shortName = flagsName.rpartition('::')[2]
          lines.append('')
          lines.extend(self._writeBinding(shortName, ownName))
    inner = self.getInnerGenerators()
    if inner:
      infoSpec = """The classes Qt writes inside %s, each a class in here
      as in C++."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec % className, '  #  '))
      for generator in inner:
        lines.append('')
        lines.extend(generator.getNestedLines())
    return lines

  @staticmethod
  def _writeBinding(name: str, joinedName: str) -> List[str]:
    """Gives the line of the class body that binds a name to what the
    package gave, on two lines when one would be too long."""
    line = '  %s = %s' % (name, joinedName)
    if len(line) <= _width():
      return [line]
    return ['  %s = (' % name, '      %s)' % joinedName]

  def _writeNamespace(self) -> List[str]:
    """Gives the lines of the section that holds the variables of the
    class: the class of Qt it stands for, and its delete ritual."""
    className = self.getClassName()
    lines = ['  #  Class Variables']
    lines.append('  #  The class of Qt this class stands for.')
    lines.append("  __qt_class__ = '%s'" % className)
    if className == self.__watched_name__:
      infoSpec = """Qt can watch a %s and tell when it has removed it.
      Every class built on this one is a %s too, and inherits this."""
      lines.append('')
      lines.extend(self._wrapWords(
          infoSpec % (className, className), '  #  '))
      lines.append('  __watched_by_qt__ = True')
    casts = [
        plan for plan in self.getRitualGenerator().getWritten()
        if plan['kind'] == 'cast'
        and plan['baseName'] in self.getFurtherBaseNames()
    ]
    if casts:
      lines.append('')
      infoSpec = """Qt's %s is built on more than one class. The part of
      a C++ %s that belongs to a class after the first begins somewhere
      inside the object, and the ritual named for that class gives
      where; see 'CuteMixin._addressAs'."""
      lines.extend(self._wrapWords(
          infoSpec % (className, className), '  #  '))
      lines.append('  __cast_rituals__ = {')
      for plan in casts:
        line = "      '%s': '%s'," % (plan['baseName'], plan['ritualName'])
        if len(line) > _width():
          line = "      '%s':\n          '%s'," % (
              plan['baseName'], plan['ritualName'])
        lines.append(line)
      lines.append('  }')
    lines.extend(self._writeTakingOver())
    deleteRitual = self.getDeleteRitual()
    if deleteRitual is not None:
      lines.append('')
      infoSpec = """Qt's '~%s()'. Naming it makes this a value class:
      Python owns every C++ %s behind a cute one, and removes it by
      this ritual."""
      info = infoSpec % (className, className)
      lines.extend(self._wrapWords(info, '  #  '))
      line = "  __delete_ritual__ = '%s'" % deleteRitual
      if len(line) > _width():
        line = "  __delete_ritual__ = (\n      '%s')" % deleteRitual
      lines.append(line)
    lines.extend((
        '', '  #  Fallback Variables', '', '  #  Private Variables',
        '', '  #  Public Variables', '', '  #  Virtual Variables',
    ))
    return lines

  def _writeCall(
      self,
      opening: str,
      called: str,
      ritualName: str,
      passed: List[str],
      closing: str = ')',
      leading: str = '',
      named: str = '',
  ) -> List[str]:
    """
    Gives the lines of one call of a ritual, kept to 77 letters where
    the names allow it.

    Parameters
    ----------

    opening : str
      What stands before the call, indent included, as
      '    address = '.

    called : str
      What is called, as 'self.uglySide.call'.

    ritualName : str
      The ritual.

    passed : List[str]
      What the ritual is handed, in order.

    closing : str
      What ends the call, as ')' or '))'.

    leading : str
      What the call is handed before the ritual, as "'QPaintDevice'"
      for 'self._callAs', or nothing.

    named : str
      The name the lines above bound the ritual to, where the function
      picks between two, or nothing.
    """
    quoted = named or "'%s'" % ritualName
    head = [leading] if leading else []
    whole = '%s%s(%s%s' % (
        opening, called, ', '.join([*head, quoted, *passed]), closing)
    if len(whole) <= _width():
      return [whole]
    indent = ' ' * (len(opening) - len(opening.lstrip()))
    if opening.endswith('(') and len('%s%s(' % (opening, called)) > _width():
      #  What stands before the call fills the line, as the name of a
      #  class and of an enum of it. The call goes on lines of its own
      #  below it.
      lines = [opening]
      lines.extend(self._writeCall(
          '%s    ' % indent, called, ritualName, passed, closing[:1],
          leading))
      lines[-1] = '%s%s' % (lines[-1], closing[1:])
      return lines
    inner = '%s    ' % indent
    lines = ['%s%s(' % (opening, called)]
    rest = ', '.join(passed)
    whole = '%s%s,' % (inner, ', '.join([*head, quoted, *passed]))
    if len(whole) <= _width():
      lines.append(whole)
    else:
      first = '%s%s,' % (inner, ', '.join([*head, quoted]))
      if len(first) > _width():
        if head:
          lines.append('%s%s,' % (inner, leading))
        first = '%s%s,' % (inner, quoted)
      if len(first) > _width():
        #  A name longer than a line is written as two texts side by
        #  side, which Python reads as one.
        room = _width() - len(inner) - 3
        pieces = [
            ritualName[i:i + room] for i in range(0, len(ritualName), room)
        ]
        for piece in pieces[:-1]:
          lines.append("%s'%s'" % (inner, piece))
        first = "%s'%s'," % (inner, pieces[-1])
      lines.append(first)
      if rest:
        packed = textwrap.wrap(
            '%s,' % rest, _width(), initial_indent=inner,
            subsequent_indent=inner, break_long_words=False,
            break_on_hyphens=False,
        )
        lines.extend(packed)
    lines.append('%s%s' % (indent, closing))
    return lines

  def _writeDef(self, function: Record) -> List[str]:
    """Gives the decorators and the 'def' line of one function."""
    lines = []  # type: List[str]
    static = function['kind'] == 'static method'
    if static:
      lines.append('  @staticmethod')
    if function['overloaded']:
      for signature in function['signatures']:
        line = '  @overload(%s)' % ', '.join(signature)
        if len(line) <= _width():
          lines.append(line)
          continue
        lines.append('  @overload(')
        lines.extend(textwrap.wrap(
            '%s,' % ', '.join(signature), _width(), initial_indent='      ',
            subsequent_indent='      ', break_long_words=False,
        ))
        lines.append('  )')
    shown = [] if static else ['self']
    stacked = len(function['signatures']) > 1
    for parameter in function['parameters']:
      annotation = parameter['annotation']
      default = parameter['default'] if stacked else None
      if parameter['nullable'] or (default and 'made' in default):
        annotation = 'Optional[%s]' % annotation
      text = '%s: %s' % (parameter['name'], annotation)
      if default is not None:
        text = '%s = %s' % (text, default['text'])
      shown.append(text)
    gives = function['gives']
    annotation = 'None' if gives is None else gives['annotation']
    if function.get('inPlace'):
      #  'a += b' gives 'a' itself back, in C++ and in Python.
      annotation = self.getDottedName()
    whole = '  def %s(%s) -> %s:' % (
        function['pythonName'], ', '.join(shown), annotation)
    if len(whole) <= _width():
      lines.append(whole)
    else:
      lines.append('  def %s(' % function['pythonName'])
      for text in shown:
        line = '      %s,' % text
        if len(line) > _width() and ' = ' in text:
          #  A default too long for the line goes on a line of its own.
          named, _, default = text.partition(' = ')
          lines.append('      %s = (' % named)
          line = '          %s),' % default
          if len(line) > _width() and ' | ' in default:
            #  Flags joined with '|' go one to a line.
            *first, last = default.split(' | ')
            lines.extend('          %s |' % one for one in first)
            line = '          %s),' % last
        lines.append(line)
      lines.append('  ) -> %s:' % annotation)
    return lines

  def _writeDocstring(self, function: Record) -> List[str]:
    """Gives the docstring of one function."""
    plan, className = function['plan'], self.getClassName()
    stem = className.lower().replace('::', '-')
    if function['kind'] == 'constructor':
      infoSpec = """Notes what was given, for Qt's '%s', which is called
      at the first use."""
      if self.isApplication():
        infoSpec = """Calls Qt's '%s' at once: nearly every other
        object of Qt can only be made after the application."""
      anchor = self.getPythonName()
    else:
      infoSpec = """Calls Qt's '%s'."""
      anchor = plan['name']
    lines = ['    """']
    lines.extend(self._wrapCpp(
        infoSpec % plan['function'], '    ', '    '))
    link = 'https://doc.qt.io/qt-6/%s.html#%s' % (stem, anchor)
    whole = "    Qt's own words: %s" % link
    lines.append('')
    if len(whole) <= _width():
      lines.append(whole)
    else:
      if len(link) > _width() - 4:
        #  A link cannot be broken, so one too long for a line is given
        #  as the page alone, without the place on it.
        link = link.partition('#')[0]
      lines.extend(("    Qt's own words:", '    %s' % link))
    stacked = len(function['signatures']) > 1
    parameters = function['parameters']
    if parameters:
      lines.extend(('', '    Parameters', '    ----------'))
      for parameter in parameters:
        annotation = parameter['annotation']
        words = parameter['words']
        if parameter['nullable']:
          annotation = 'Optional[%s]' % annotation
          if parameter['kind'] == 'chars':
            words = '%s None is passed on as no text.' % words
          else:
            words = '%s None is passed on as no object.' % words
        default = parameter['default'] if stacked else None
        if default is not None:
          if 'left' in default:
            infoSpec = """%s May be left out, as in Qt: what '%s'
            gives is then passed on."""
            words = infoSpec % (words, default['made'])
          elif 'made' in default:
            annotation = 'Optional[%s]' % annotation
            infoSpec = """%s May be left out, as in Qt: a new '%s' is
            then passed on."""
            words = infoSpec % (words, default['made'])
          else:
            infoSpec = """%s May be left out, as in Qt: it is then %s."""
            words = infoSpec % (words, default['text'])
        lines.append('')
        lines.append('    %s : %s' % (parameter['name'], annotation))
        lines.extend(self._wrapWords(words, '      '))
    gives = function['gives']
    if gives is not None and gives['words']:
      lines.extend(('', '    Returns', '    -------', ''))
      lines.append('    %s' % gives['annotation'])
      lines.extend(self._wrapWords(gives['words'], '      '))
    lines.append('    """')
    if len(lines) == 3 and len(lines[1]) <= 70:
      return ['    """%s"""' % lines[1].strip()]
    return lines

  def _writeBody(self, function: Record) -> List[str]:
    """Gives the lines of one function below its docstring."""
    plan, className = function['plan'], self.getDottedName()
    kind, gives = function['kind'], function['gives']
    lines = self._wrapCpp(plan['function'], '    #  ', '    #      ')
    stacked = len(function['signatures']) > 1
    passed = []
    for parameter in function['parameters']:
      default = parameter['default'] if stacked else None
      if default is not None and 'made' in default:
        name = parameter['name']
        left = default.get('left', 'None')
        lines.append('    if %s is %s:' % (name, left))
        brought = []  # type: List[str]
        if parameter['late'] and parameter['bring']:
          brought.append(parameter['bring'])
        for otherName in default.get('brings', ()):
          if otherName not in brought:
            brought.append(otherName)
        for otherName in brought:
          lines.append(self._writeBringing(otherName, '      '))
        lines.append('      %s = %s' % (name, default['made']))
      passed.append(parameter['passed'])
    ritualName = plan['ritualName']
    if kind == 'constructor':
      opening = '    self._noteCreation(%s, lambda: ' % className
      if len('%sRituals.call(' % opening) > _width():
        #  The name of the class fills the line, so it goes on a line of
        #  its own below.
        lines.append('    self._noteCreation(')
        opening = '        %s, lambda: ' % className
      lines.extend(self._writeCall(
          opening, 'Rituals.call', ritualName, passed, '))'))
      if self.isApplication():
        #  Reading the ugly side is the first use.
        lines.append('    self._getUglySide()')
      return lines
    called = 'Rituals.call' if kind in ('static method', 'friend') else (
        'self.uglySide.call')
    if kind == 'friend':
      #  The ritual takes the object where Qt's operator takes it.
      place = function['operator']['selfIndex']
      passed = [*passed[:place], function['selfPassed'], *passed[place:]]
    leading = ''
    if kind == 'method' and self.getClassName() in self._getPartNames():
      #  The object may be of a class built on this one beside another,
      #  whose part of this class begins inside the object. The ritual
      #  is handed the address of that part.
      called, leading = 'self._callAs', "'%s'" % self.getClassName()
    named = ''
    if function.get('ownRitual'):
      #  C++ looks this function up in the object. In an object of ours
      #  that leads to the Python function a class of the program wrote
      #  in its place, which may be the very one calling this. So for
      #  such an object just the class's own function is run.
      named = 'ritual'
      for indent, ritual in (('    ', ritualName), (
          '      ', function['ownRitual'])):
        line = "%sritual = '%s'" % (indent, ritual)
        if len(line) <= _width():
          lines.append(line)
        else:
          #  A name too long for the line is written in pieces, which
          #  Python reads as one text.
          room = _width() - len(indent) - 7
          pieces = [
              ritual[at:at + room] for at in range(0, len(ritual), room)]
          lines.append('%sritual = (' % indent)
          lines.extend("%s    '%s'" % (indent, piece) for piece in pieces)
          lines[-1] = '%s)' % lines[-1]
        if indent == '    ':
          lines.append('    if self.uglySide.isOurs():')
    givenKind = gives['kind']
    if givenKind == 'nothing':
      lines.extend(self._writeCall(
          '    ', called, ritualName, passed, ')', leading, named))
    elif givenKind in ('number', 'text'):
      lines.extend(self._writeCall(
          '    return ', called, ritualName, passed, ')', leading, named))
    elif givenKind == 'chars':
      lines.extend(self._writeCall(
          '    chars = ', called, ritualName, passed, ')', leading, named))
      lines.append('    return None if chars is None else chars.decode()')
    elif givenKind in ('enum', 'flags'):
      lines.extend(self._writeCall(
          '    return %s(' % gives['maker'], called, ritualName, passed,
          '))', leading, named,
      ))
    else:
      lines.extend(self._writeCall(
          '    address = ', called, ritualName, passed, ')', leading, named))
      holder = gives['holder']
      if gives['late'] and gives['bring']:
        #  The file of the class may not be brought in yet. It is
        #  brought in here, at the first call.
        lines.append(self._writeBringing(gives['bring'], '    '))
      maker = '_cuteAt' if givenKind == 'address' else '_cuteOwning'
      lines.append('    return %s.%s(address)' % (holder, maker))
    if function.get('inPlace'):
      lines.append('    return self')
    return lines

  @staticmethod
  def _writeFallback(pythonName: str) -> List[str]:
    """
    Gives the lines of the function that answers, at a name Python asks
    one side of an operator for, a call no signature takes.

    Python has a word for that answer: 'NotImplemented'. Python then
    asks the other side, and when that cannot either, 'a + b' raises
    'TypeError' and 'a == b' is False. It stands where the door stands
    at every other overloaded name.
    """
    return [
        '',
        '  @overload.fallback',
        '  def %s(self, *args: object) -> object:' % pythonName,
        '    """',
        '    Tells Python that no function of this name takes what it was',
        "    handed, with Python's own word for it. Python then asks the",
        '    other side of the operator.',
        '    """',
        '    return NotImplemented',
    ]

  def _findWhere(self, how: str, what: str) -> Optional[str]:
    """
    Says where the cute class or enum of something Qt hands a function
    is found, as 'QtGui:QPaintEvent' or 'QtCore:Qt.FocusPolicy', for
    the function that receives it from C++. Gives '' for a number and
    None when there is no cute class or enum for it.
    """
    if how in ('number', 'nothing', 'text'):
      return ''
    tree, cuteNames = self.getDependencyTree(), self.getCuteNames()
    #  The combinations of an enum are values of the class of the enum.
    listed = how in ('enum', 'flags')
    holder = what.rpartition('::')[0] if listed else what
    if holder not in cuteNames and holder != 'Qt':
      return None
    if not listed and what not in cuteNames:
      return None
    partName = 'QtCore' if holder == 'Qt' else tree.getPartName(
        holder.split('::')[0])
    return '%s:%s' % (partName, what.replace('::', '.'))

  @staticmethod
  def _writeShape(indent: str, shape: Any) -> List[str]:
    """Gives the lines of one thing a function gives or takes, as the
    table of functions to take over holds it, on two lines when one
    would be too long."""
    line = '%s%r,' % (indent, (*shape,))
    if len(line) <= _width():
      return [line]
    word, how, where = shape
    return [
        '%s(%r, %r,' % (indent, word, how),
        '%s %r),' % (indent, where),
    ]

  def _writeTakingOver(self) -> List[str]:
    """
    Gives the lines of the class body that say which ritual hands a
    Python function over to an object of the class, and which
    functions Qt calls itself that the class is the first to declare,
    so that a class of a program built on it can write them anew.
    """
    generator = self.getRitualGenerator()
    className, lines = self.getClassName(), []  # type: str, List[str]
    for plan in generator.getWritten():
      if plan['kind'] != 'take':
        continue
      infoSpec = """A C++ %s Python makes is of a C++ class of ours, in
      which Python can take functions over. This ritual hands one over;
      see 'CuteMixin._takeOver'."""
      lines.append('')
      lines.extend(self._wrapWords(infoSpec % className, '  #  '))
      lines.append("  __take_ritual__ = '%s'" % plan['ritualName'])
    table = collections.OrderedDict()  # type: Dict[str, List[Any]]
    for function in generator.getOverridable():
      if function['rootOwner'] != className:
        continue
      shapes = [function['gives'], *function['takes']]
      wheres = [self._findWhere(how, what) for _, how, what in shapes]
      if any(where is None for where in wheres):
        continue
      turned = [(s[0], s[1], w) for s, w in zip(shapes, wheres)]
      table.setdefault(function['name'], []).append(
          (function['key'], turned[0], (*turned[1:],)))
    lines.extend(self._writeLeftOutVirtuals(table))
    if not table:
      return lines
    infoSpec = """The functions Qt calls itself that %s is the first to
    declare. A class of a program built on it can write one anew, and
    Qt then calls that. For each name: the key C++ knows the function
    by, what it gives, and what it takes."""
    lines.append('')
    lines.extend(self._wrapWords(infoSpec % className, '  #  '))
    lines.append('  __virtual_functions__ = {')
    for name, variants in table.items():
      lines.append("      '%s': (" % name)
      for key, gives, takes in variants:
        room = _width() - 14
        pieces = [key[at:at + room] for at in range(0, len(key), room)]
        #  A key too long for the line is written in pieces, which
        #  Python reads as one text.
        lines.append("          ('%s'" % pieces[0])
        lines.extend("           '%s'" % piece for piece in pieces[1:])
        lines[-1] = '%s,' % lines[-1]
        lines.extend(self._writeShape('           ', gives))
        if not takes:
          lines.append('           ()),')
          continue
        lines.append('           (')
        for take in takes:
          lines.extend(self._writeShape('               ', take))
        lines.append('           )),')
      lines.append('      ),')
    lines.append('  }')
    return lines

  def _writeLeftOutVirtuals(self, table: Any) -> List[str]:
    """
    Gives the lines of the class body that name the functions Qt calls
    itself which the class is the first to declare and of which none
    of that name can be handed to Python yet, each as Qt declares it.
    'CuteMixin._refuseLeftOut' refuses a class of a program that writes
    one of them anew: Qt would never call what it wrote.

    Parameters
    ----------

    table : Any
      The functions of the class that can be handed to Python, by
      name, as '_writeTakingOver' gathered them.
    """
    generator = self.getRitualGenerator()
    leftOut = collections.OrderedDict()  # type: Dict[str, List[str]]
    for virtual in generator.getDeclaredVirtuals():
      if virtual['name'] not in table:
        leftOut.setdefault(virtual['name'], []).append(virtual['written'])
    if not leftOut:
      return []
    infoSpec = """The functions Qt calls itself that %s is the first to
    declare and that cannot be handed to Python yet, each as Qt
    declares it. A class of a program that writes one of them anew is
    refused, since Qt would never call what it wrote; see
    'CuteMixin._refuseLeftOut'."""
    lines = ['']
    lines.extend(self._wrapWords(infoSpec % self.getClassName(), '  #  '))
    lines.append('  __virtual_left_out__ = {')
    for name, declarations in leftOut.items():
      lines.append("      '%s': (" % name)
      for written in declarations:
        #  A declaration too long for the line is written in pieces,
        #  which Python reads as one text.
        pieces, room = [], _width() - 13  # type: List[str], int
        while len(written) > room:
          cut = written.rfind(' ', 0, room) + 1 or room
          pieces.append(written[:cut])
          written = written[cut:]
        pieces.append(written)
        lines.extend("          '%s'" % piece for piece in pieces)
        lines[-1] = '%s,' % lines[-1]
      lines.append('      ),')
    lines.append('  }')
    return lines

  def _writeFunction(self, function: Record) -> List[str]:
    """Gives every line of one function of the class body."""
    lines = [
        *self._writeDef(function), *self._writeDocstring(function),
        *self._writeBody(function),
    ]
    if function.get('fallbackAfter'):
      lines.extend(self._writeFallback(function['pythonName']))
    return lines

  def getClassText(self) -> str:
    """
    Gives the whole text of the file, without writing it.

    Written for you from 'getFunctions' and 'getLeftOut': the heading,
    the names the file brings in, and the class with its docstring and
    its sections.
    """
    if self.isNested():
      infoSpec = """Qt writes '%s' inside another class, so it has no
      file of its own: the generator of '%s' writes it."""
      className = self.getClassName()
      info = infoSpec % (className, className.split('::')[0])
      raise ValueError(' '.join(info.split()))
    className = self.getClassName()
    lines = ['"""', '%s binding of the Qt C++' % className, '"""']
    lines.extend(('#  Apache-2.0 license',
                  '#  Copyright (c) 2026 Asger Jon Vistisen'))
    lines.extend(self._getHeading())
    lines.extend(self._writeImports())
    lines.extend(('', ''))
    lines.extend(self._getClassLines())
    lines.extend(self._writeListKinds())
    return '%s\n' % '\n'.join(lines)

  def getNamedLists(self) -> List[str]:
    """Gives the names Qt has for the kinds of list that hold the
    class, as 'QModelIndexList' in the file of QModelIndex. The package
    of the part has to know that each is found in this file."""
    generator = self.getRitualGenerator()
    names = []  # type: List[str]
    for listed in generator.getOwnListKinds():
      names.extend(generator.getListNames(listed))
    for mapped in generator.getOwnMapKinds():
      names.extend(generator.getMapNames(mapped))
    return names

  def _writeListKinds(self) -> List[str]:
    """
    Gives the lines at the end of the file that make the class of each
    kind of list holding the class, and collect it in 'QList'. The
    list of a class is made in the file of that class, so that there
    is one as soon as there can be an object of the class.
    """
    generator = self.getRitualGenerator()
    className, lines = self.getClassName(), []  # type: str, List[str]
    for listed in generator.getOwnListKinds():
      names = generator.getListNames(listed)
      rituals = {
          plan['listRole']: plan['ritualName']
          for plan in generator.getWritten()
          if plan['kind'] == 'list' and plan['listed'] is listed
      }
      infoSpec = """Qt's '%s': the list of %s, which 'QList[%s]' gives.
      It is made here, so that there is one as soon as there can be a
      %s.""" % (listed['listType'], className, className, className)
      if names:
        infoSpec = """%s Qt has a name of its own for it.""" % infoSpec
      lines.extend(('', ''))
      lines.extend(self._wrapWords(infoSpec, '#  '))
      lines.append('%sQList.createKind(' % ''.join(
          '%s = ' % name for name in names))
      lines.append("    %s, '%s'," % (className, listed['crossing']))
      if names:
        lines.append("    name='%s'," % names[0])
      for role in ('make', 'add', 'size', 'at', 'drop'):
        lines.append("    %s='%s'," % (role, rituals[role]))
      lines.append(')')
    for mapped in generator.getOwnMapKinds():
      names = generator.getMapNames(mapped)
      rituals = {
          plan['mapRole']: plan['ritualName']
          for plan in generator.getWritten()
          if plan['kind'] == 'map' and plan['mapped'] is mapped
      }
      key = 'str' if mapped['keyWord'] == 'text' else 'int'
      pattern = mapped['pattern']
      infoSpec = """Qt's '%s': the %s from %s to %s, which '%s[%s, %s]'
      gives. It is completed here, in the file of the class of its
      values.""" % (
          mapped['mapType'], pattern, 'text' if key == 'str' else 'a number',
          className, pattern, key, className)
      if names:
        infoSpec = """%s Qt has a name of its own for it.""" % infoSpec
      lines.extend(('', ''))
      lines.extend(self._wrapWords(infoSpec, '#  '))
      lines.append('%s%s.createKind(' % (
          ''.join('%s = ' % name for name in names), pattern))
      lines.append("    %s, %s, '%s'," % (
          key, className, mapped['crossing']))
      if names:
        lines.append("    name='%s'," % names[0])
      for role in ('make', 'put', 'size', 'key', 'value', 'has', 'get',
                   'drop'):
        lines.append("    %s='%s'," % (role, rituals[role]))
      lines.append(')')
    return lines

  def _getClassLines(self) -> List[str]:
    """Gives the class statement and everything below it."""
    baseName, pythonName = self.getBaseName(), self.getPythonName()
    bases = [*filter(None, (baseName,)), *self.getFurtherBaseNames()]
    functions = self.getFunctions()
    lines = []  # type: List[str]
    if not bases:
      lines.append('class %s(CuteMixin, metaclass=MetaCute):' % pythonName)
    else:
      lines.append('class %s(%s):' % (pythonName, ', '.join(bases)))
    lines.extend(self._writeClassDocstring())
    lines.extend(self._writeNames())
    for sectionName in self.__section_names__:
      lines.append('')
      lines.extend(self._writeBanner(sectionName))
      if sectionName == 'NAMESPACE':
        lines.append('')
        lines.extend(self._writeNamespace())
      for function in functions:
        if function['section'] != sectionName:
          continue
        lines.append('')
        lines.extend(self._writeFunction(function))
    return '\n'.join(lines).split('\n')

  def getNestedLines(self) -> List[str]:
    """
    Gives the class as the lines that stand in the body of the class Qt
    writes it inside, where C++, PySide6 and PyQt have it:
    'QMetaObject.Connection'. Its lines are two letters shorter, and
    stand two letters further in.
    """
    held = _width()
    _LOCAL.width = held - 2
    try:
      lines = self._getClassLines()
    finally:
      _LOCAL.width = held
    return ['  %s' % line if line.strip() else '' for line in lines]

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
    Writes the file of the cute class into the folder of its part of
    Qt, replacing the one written before, and the file of each enum Qt
    writes inside the class beside it.

    Returns
    -------

    str
      The full path of the file of the class, which now exists.

    Raises
    ------

    MissingVariable
      One of the four setters has not been called.

    LookupError
      The tree has no class of that name.
    """
    classFile = self.getClassFile()
    text = self.getClassText()
    with open(classFile, 'w') as file:
      file.write(text)
    return classFile
