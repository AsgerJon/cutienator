"""ClassGenerator writes the Python file of one cute class."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import collections
import keyword
import os
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

from . import DependencyTree, RitualGenerator, EnumGenerator
from ._cute_name import CuteName
from ._default_value import DefaultValue
from ._class_text import ClassText
from ._function_plan import FunctionPlan
from .class_tables import (
    APPLICATION_NAME, BINARY_OPERATORS, IN_PLACE_OPERATORS)

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Any, Dict, List, Optional, Set, Tuple

  Record = Dict[str, Any]
  Records = Tuple[Record, ...]
  Reasons = Tuple[Tuple[str, str], ...]
  Names = Tuple[str, ...]


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
    generator.setPartName('QtCore')
    generator.setClassName('QSize')
    generator.setCuteNames(('QtCore', 'QSize'), ('QtCore', 'QPoint'))
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
  - 'setPartName': the part of Qt the class is under, as 'QtCore'.
    Required. Every name the generator meets is seen from that part,
    as 'DependencyTree' has it.
  - 'setClassName': the class of Qt to write the cute class of.
    Required.
  - 'setCuteNames': every class of Qt that has, or is about to get, a
    cute class, each by its part and its name. A function naming any
    other class is left out. Required.
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Fallback Variables

  #  Private Variables
  __dependency_tree__ = None  # type: Optional[DependencyTree]
  __class_name__ = None  # type: Optional[str]
  __part_name__ = None  # type: Optional[str]
  __work_folder__ = None  # type: Optional[str]
  __cute_names__ = None  # type: Optional[Tuple[Tuple[str, str], ...]]
  __ritual_generators__ = None  # type: Optional[Dict[str, Any]]
  __made_functions__ = None  # type: Optional[Records]
  __left_out__ = None  # type: Optional[Reasons]
  __unsupported_names__ = None  # type: Optional[Tuple[Any, ...]]
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

  def getCuteNames(self) -> Tuple[Tuple[str, str], ...]:
    """
    Gives every class of Qt that has, or is about to get, a cute class,
    each by its part and its name, as ('QtCore', 'QSize').

    Provided by you, through 'setCuteNames'.

    Raises
    ------

    MissingVariable
      'setCuteNames' has not been called.
    """
    if self.__cute_names__ is None:
      raise MissingVariable(self, '__cute_names__', tuple)
    return self.__cute_names__

  def _keyOf(self, className: str) -> Tuple[str, str]:
    """
    Gives the class a name stands for, seen from the part of the class
    being written, by its key, as ('QtCore', 'QObject').

    Raises
    ------

    LookupError
      The tree has no class of that name.
    """
    tree = self.getDependencyTree()
    return tree.getClassKey(className, self.getPartName())

  def _isCute(self, className: str) -> bool:
    """Says whether a name, seen from the part of the class being
    written, stands for a class that has, or is about to get, a cute
    class."""
    try:
      classKey = self._keyOf(className)
    except LookupError:
      return False
    return classKey in self.__cute_keys__

  #  The same classes as 'getCuteNames', to look them up.
  __cute_keys__ = frozenset()

  def getDefaultValue(
      self,
      argument: Record,
      parameter: Record,
  ) -> DefaultValue:
    """Gives the 'DefaultValue' of an argument: what Qt fills in for it
    when it is left out, the argument as the plan of the ritual has it
    and as this generator has it in Python."""
    defaultValue = DefaultValue()
    defaultValue.setArgument(argument)
    defaultValue.setParameter(parameter)
    defaultValue.setViewer(self)
    return defaultValue

  def getFunctionPlan(self, plan: Record) -> FunctionPlan:
    """Gives the 'FunctionPlan' of one ritual of the class, as
    'RitualGenerator.getWritten' gives its plan: how it becomes one
    function of the cute class."""
    functionPlan = FunctionPlan()
    functionPlan.setPlan(plan)
    functionPlan.setViewer(self)
    return functionPlan

  def getCuteName(self, name: Optional[str] = None) -> CuteName:
    """Gives the 'CuteName' of a name of Qt, seen from the class being
    written: of that class when none is named."""
    cuteName = CuteName()
    cuteName.setName(name or self.getClassName())
    cuteName.setViewer(self)
    return cuteName

  def getPythonName(self, className: Optional[str] = None) -> str:
    """Gives the name the cute class of a class of Qt has in Python, as
    'CuteName.getPythonName' does: of the class being written when none
    is named."""
    return self.getCuteName(className).getPythonName()

  def getDottedName(self, className: Optional[str] = None) -> str:
    """Gives the name by which Python reaches the cute class of a class
    of Qt from the top of its file, as 'CuteName.getDottedName' does: of
    the class being written when none is named."""
    return self.getCuteName(className).getDottedName()

  def isNested(self) -> bool:
    """Says whether Qt writes the class inside another class. Such a
    class is written inside the cute class of that class, in its file.
    A class Qt writes inside a namespace and no class, as
    'Qt3DCore::QEntity', is not: it has a file of its own."""
    return self.getCuteName().isNested()

  def _isClassName(self, name: str) -> bool:
    """Says whether a name, seen from the part of the class being
    written, stands for a class of the tree, and not for a namespace."""
    try:
      self._keyOf(name)
    except LookupError:
      return False
    return True

  def getLocalName(self, className: Optional[str] = None) -> str:
    """Gives the name by which the file of the class reaches its cute
    class, as 'CuteName.getLocalName' does: 'QEntity' for
    'Qt3DCore::QEntity'; of the class being written when none is
    named."""
    return self.getCuteName(className).getLocalName()

  def getImportName(self, className: str) -> Tuple[str, str]:
    """
    Gives what a file brings in to reach the cute class of a class of
    Qt, and from which part: the class itself, as ('QtGui', 'QFont');
    for a class Qt writes inside another, the outermost class around
    it, as ('QtCore', 'QMetaObject') for 'QMetaObject::Connection'; for
    a class Qt writes inside a namespace and no class, the outermost
    namespace, as ('Qt3DCore', 'Qt3DCore') for 'Qt3DCore::QEntity'.
    Bringing in a namespace brings in no file of a class.
    """
    cuteName = self.getCuteName(className)
    top, spaceName = cuteName.getTopClassName(), cuteName.getSpaceName()
    asked = spaceName.split('::')[0] if spaceName else top
    return self.getPartName(top), asked

  def getWaitKey(self, boundName: str) -> str:
    """
    Gives what a 'WAIT' bound at a name of the file stands for, as
    'getWaitKeyOf' gives it of its late class: for a class this one is
    written inside, bound at its local name, as 'QTransform' for
    'Qt3DCore::QTransform', that class, 'Qt3DCore.QTransform'; for any
    other, the class of the bound name.
    """
    pieces = self.getClassName().split('::')
    for depth in range(1, len(pieces)):
      around = '::'.join(pieces[:depth])
      if self._isClassName(around) and (
          self.getLocalName(around) == boundName):
        return self.getWaitKeyOf(around)
    return self.getWaitKeyOf(boundName)

  def getWaitKeyOf(self, className: str) -> str:
    """
    Gives the name a 'WAIT' waits for a class by: the name Qt has for
    it with dots for '::', as 'Qt3DCore.QEntity'; and for a class whose
    name another part has too, its part before a colon, the part it is
    seen of from this one: 'QtGraphs:QBarSeries'. That class says its
    part in its body; see 'isShared'.
    """
    dotted = className.replace('::', '.')
    if className not in self.getDependencyTree().getSharedNames():
      return dotted
    return '%s:%s' % (self._keyOf(className)[0], dotted)

  def isShared(self) -> bool:
    """Says whether another part of Qt has a class of the name of this
    one too, as QtCharts and QtGraphs both have 'QBarSeries': its body
    then says its part, in '__qt_part__'."""
    tree = self.getDependencyTree()
    return self.getClassName() in tree.getSharedNames()

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
        generator.setPartName(self.getPartName())
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
    """Gives the class Qt writes a class inside, as
    'CuteName.getOwnerName' does: of the class being written when none
    is named."""
    return self.getCuteName(className).getOwnerName()

  def getInnerNames(self) -> Names:
    """
    Gives the classes Qt writes right inside the class that have a
    cute class, in alphabetical order. The cute class holds each under
    its own name.
    """
    className, partName = self.getClassName(), self.getPartName()
    return (*sorted(
        name for part, name in self.getCuteNames()
        if part == partName and self.getOwnerName(name) == className),)

  def getPartName(self, className: Optional[str] = None) -> str:
    """
    Gives the part of Qt a class belongs to, as 'QtCore', the class
    seen from the part of the class being written: that part itself
    when none is named, provided by you through 'setPartName'.

    Raises
    ------

    MissingVariable
      'setPartName' has not been called.
    """
    if self.__part_name__ is None:
      raise MissingVariable(self, '__part_name__', str)
    if className is None:
      return self.__part_name__
    return self._keyOf(className)[0]

  def getFileStem(self, className: Optional[str] = None) -> str:
    """
    Gives the name of the file of a cute class without its ending, as
    '_q_size' for 'QSize': that of the class being written when none
    is named.
    """
    className = className or self.getClassName()
    #  A class written inside another has no file of its own: it stands
    #  in the file of the outermost class around it.
    return '_%s' % self.getStem(
        self.getCuteName(className).getTopClassName())

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
    classKey = self._keyOf(className or self.getClassName())
    if self.__ritual_generators__ is None:
      self.__ritual_generators__ = dict()
    if classKey not in self.__ritual_generators__:
      generator = RitualGenerator()
      generator.setDependencyTree(self.getDependencyTree())
      generator.setPartName(classKey[0])
      generator.setClassName(classKey[1])
      self.__ritual_generators__[classKey] = generator
    return self.__ritual_generators__[classKey]

  def getBaseName(self) -> Optional[str]:
    """
    Gives the class of Qt whose cute class this one is built on: the
    first class the Qt class is built on, when that has a cute class.
    Gives None for a class built on no such class.
    """
    parents = self.getDependencyTree().getParents(
        self.getClassName(), self.getPartName())
    if not parents or not self._isCute(parents[0]):
      return None
    #  A class Qt writes inside another class is made after the class
    #  around it, in its file, so nothing is built on it. A class Qt
    #  writes inside a namespace alone has a file of its own.
    if self.getCuteName(parents[0]).isNested():
      return None
    if not self._isMadeBefore(parents[0]):
      return None
    return parents[0]

  def getUnreflectedParents(self) -> Names:
    """Gives the classes the Qt class is built on that the cute class
    is not built on."""
    parents = self.getDependencyTree().getParents(
        self.getClassName(), self.getPartName())
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
    for partName, enumName in tree.getEnumRecordNames():
      if partName != self.getPartName():
        continue
      if tree.getEnumRecord(enumName, partName)['ownerName'] != className:
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
      self.__owner_classes__ = ()
      self._createFunctions()
      self.__owner_classes__ = (*self.__needed_names__['owners'],)
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

  def getUnsupported(self) -> Tuple[Tuple[str, Reasons], ...]:
    """
    Gives the names of Qt in the class that have no cute function, each
    with the functions of Qt at it and why each has none, by name in
    alphabetical order. The file has a function at each of these names
    that raises 'NotImplementedError', saying why.

    A name gets no such function where it would stand in the way: a name
    with a cute function, an enum or a class at it; one a cute class
    this one is built on declares, whose function then serves; and the
    name of a destructor, of an operator, of Qt's own inner workings,
    and of what Qt forbids or calls no gap.

    Decided for you, together with 'getFunctions'.

    Returns
    -------

    Tuple[Tuple[str, Reasons], ...]
      Each name as Python has it, as 'nativeEvent' or '__init__', and
      for each function of Qt at it: the function as C++ writes it, and
      the reason in words.
    """
    self.getFunctions()
    return self.__unsupported_names__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _forget(self) -> None:
    """Forgets what was decided, after a setter changed what it is
    decided from."""
    self.__made_functions__ = None
    self.__left_out__ = None
    self.__unsupported_names__ = None
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
    self.__ritual_generators__ = None
    self.__inner_generators__ = None
    self.__part_names__ = None
    self._forget()

  def setCuteNames(self, *cuteKeys: Tuple[str, str]) -> None:
    """
    Tells the generator which classes of Qt have, or are about to get,
    a cute class.

    Required. A function naming a class that is not among them is left
    out, with that reason. Calling it again forgets what was decided
    before.

    Parameters
    ----------

    *cuteKeys : Tuple[str, str]
      The classes, each by its part and the name the dependency tree
      has it under, as ('QtCore', 'QSize').

    Raises
    ------

    TypeException
      One of them is not a pair of texts.
    """
    for cuteKey in cuteKeys:
      if not isinstance(cuteKey, tuple) or len(cuteKey) != 2 or not all(
          isinstance(one, str) for one in cuteKey):
        raise TypeException('cuteKey', cuteKey, tuple)
    self.__cute_names__ = (*cuteKeys,)
    self.__cute_keys__ = frozenset(cuteKeys)
    self.__part_names__ = None
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
            ('setPartName', self.__part_name__),
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
    #  The enum as seen from the part of the class being written.
    try:
      enumPart = self.getDependencyTree().getEnumRecord(
          enumName, self.getPartName())['partName']
    except ValueError:
      enumPart = self.getPartName()
    generator.setPartName(enumPart)
    generator.setEnumName(enumName)
    if self.__work_folder__ is not None:
      generator.setWorkFolder(self.__work_folder__)
    return generator

  def getImportOrder(self, partNames: Any) -> Names:
    """
    Gives parts of Qt in the order the file brings names in from them:
    first the parts the part of the class needs, its own part among
    them, each after the parts it is built on, as 'QtCore', 'QtGui',
    'QtWidgets' for a class of QtWidgets; then any other of them, in
    the same order.

    A part needs more parts than any part it is built on, since it
    needs those too, so ordering by how many parts each needs puts
    every part after those it is built on. Parts that need as many are
    in alphabetical order.

    Parameters
    ----------

    partNames : Any
      The parts the file brings names in from, in any order.
    """
    tree, wanted = self.getDependencyTree(), {*partNames}
    needed = {*tree.getNeededParts(self.getPartName())}

    def depth(partName: str) -> Tuple[int, str]:
      """Gives how many parts a part needs, then its name."""
      return len(tree.getNeededParts(partName)), partName

    first = sorted(wanted & needed, key=depth)
    return (*first, *sorted(wanted - needed, key=depth))

  def _isMadeBefore(self, otherName: str) -> bool:
    """
    Says whether the cute class of another class of Qt is made before
    the one being written, so that this one can be built on it.

    A class of an earlier part of Qt is. A class of the same part is
    when the dependency tree makes it earlier.
    """
    tree, className = self.getDependencyTree(), self.getClassName()
    here, there = self.getPartName(), self.getPartName(otherName)
    if there != here:
      #  A part this one needs is made first.
      return there in tree.getNeededParts(here)
    #  A class written inside another is made right before the
    #  outermost class around it, whose file brings it in.
    mine = self.getCuteName().getTopClassName()
    theirs = self.getCuteName(otherName).getTopClassName()
    if mine == theirs:
      return len(otherName) > len(className)
    makeOrder = tree.getMakeOrder()
    return makeOrder.index(self._keyOf(theirs)) < makeOrder.index(
        self._keyOf(mine))

  def getFurtherBaseNames(self) -> Names:
    """
    Gives the classes of Qt after the first that the cute class is
    built on as well, as 'QPaintDevice' for 'QWidget', in the order C++
    names them. The cute class is built on the cute class of each, and
    names the ritual that gives where that part of an object is; see
    'RitualGenerator.getFurtherBases'.
    """
    parents = self.getDependencyTree().getParents(
        self.getClassName(), self.getPartName())
    return (*(
        parent for parent in parents[1:]
        if self._isCute(parent)
        and not self.getCuteName(parent).isNested()
        and self._isMadeBefore(parent)
    ),)

  def _getBuiltOn(self) -> Names:
    """
    Gives every class of Qt the cute class is built on, the nearest
    first: what it is built on, what those are built on, and so on.
    Their files are brought in with the file being written whatever it
    names, so naming them costs nothing.
    """
    tree, partName = self.getDependencyTree(), self.getPartName()
    builtOn = [*filter(None, (self.getBaseName(),))]
    builtOn.extend(self.getFurtherBaseNames())
    for name in builtOn:
      for parent in tree.getParents(name, partName):
        if self._isCute(parent) and (
            not self.getCuteName(parent).isNested()):
          if parent not in builtOn:
            builtOn.append(parent)
    return (*builtOn,)

  def _getPartNames(self) -> Tuple[Tuple[str, str], ...]:
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
      tree, cuteKeys = self.getDependencyTree(), self.__cute_keys__
      found = []  # type: List[Tuple[str, str]]

      def take(parents: Names, partName: str) -> None:
        """Takes those of the classes, as C++ writes them, that have a
        cute class, seen from the part."""
        for parent in parents:
          if not tree.hasClass(parent, partName):
            continue
          parentKey = tree.getClassKey(parent, partName)
          if parentKey in cuteKeys and parentKey not in found:
            found.append(parentKey)

      for partName, className in self.getCuteNames():
        take(tree.getParents(className, partName)[1:], partName)
      for partName, name in found:
        take(tree.getParents(name, partName), partName)
      self.__part_names__ = (*found,)
    return self.__part_names__

  #  The classes that hold an enum or a class this one names, known
  #  after the functions are worked out a first time. Their files are
  #  brought in.
  __owner_classes__ = None
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
    found = self.getCuteName(holds).findClassEntry()
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
      entry = "WAIT['%s']" % self.getWaitKeyOf(holds)
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
    found = self.getCuteName(holds).findClassEntry()
    if isinstance(found, str):
      return "a map to '%s': %s" % (holds, found)
    if found is None:
      return "a map to '%s', which has no cute class yet" % holds
    self._note('lists', pattern)
    entry = found['entry']
    if entry == 'THIS':
      self._note('top', 'WAIT')
      entry = "WAIT['%s']" % self.getWaitKeyOf(holds)
    key = 'str' if mapped['keyWord'] == 'text' else 'int'
    return dict(
        found, entry='%s[%s, %s]' % (pattern, key, entry),
        name='%s[%s, %s]' % (pattern, key, found['name']),
        holder='%s[%s, %s]' % (pattern, key, found['holder']),
        lateName=found['entry'], className=holds,
    )

  def _canBeMadeOf(self, className: str, parts: List[Record]) -> bool:
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
        kind, cppName = part['kind'], part['cppName']
        passing = argument['passing']
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
    try:
      classKey = self._keyOf(className)
    except LookupError:
      return False
    if classKey not in tree.getCopyableNames():
      return False
    for plan in self.getRitualGenerator(className).getWritten():
      if plan['kind'] == 'destructor':
        return True
    return False

  def isApplication(self) -> bool:
    """Says whether the class is Qt's application, or built on it."""
    tree, className = self.getDependencyTree(), self.getClassName()
    if className == APPLICATION_NAME:
      return True
    ancestors = tree.getAncestors(className, self.getPartName())
    return APPLICATION_NAME in [n for _, n in ancestors]

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
        ancestors = tree.getAncestors(one, self.getPartName())
      except LookupError:
        return False
      if another not in [n for _, n in ancestors]:
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
    apart = ('cast', 'take', 'own', 'list', 'map', 'drop')
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
    #  The functions left out for what they take or give, by the name
    #  each would have in Python.
    refused = []  # type: List[Tuple[Optional[str], str, str]]
    for plan in plans:
      functionPlan = self.getFunctionPlan(plan)
      function = functionPlan.findFunction()
      if isinstance(function, str):
        leftOut.append((plan['function'], function))
        refused.append(
            (functionPlan.getPythonName(), plan['function'], function))
        continue
      if function['pythonName'] in enumNames:
        infoSpec = """the class has an enum of that name, which holds
        the name"""
        leftOut.append((plan['function'], ' '.join(infoSpec.split())))
        continue
      compilerName = plan['ritualName'][len('ritual'):]
      if not plan.get('ownOnly') and compilerName in owned:
        function['ownRitual'] = owned[compilerName]['ritualName']
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
      pairs = BINARY_OPERATORS.values()
      asked = [name for pair in pairs for name in pair]
      asked.extend(IN_PLACE_OPERATORS.values())
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
    unsupported = self._findUnsupported(functions, refused, enumNames)
    if unsupported:
      self._note('typing', 'Never')
    self.__unsupported_names__ = unsupported
    self.__made_functions__ = (*functions,)
    self.__left_out__ = (*leftOut,)

  def _findDeclaredName(self, shown: str) -> Optional[str]:
    """
    Gives the name in Python of a function of the class that has no
    ritual, read from the function as C++ writes it: '__init__' for a
    constructor, an underscore after a word of Python. None for a
    destructor, for an operator and for one of Qt's own inner workings,
    named 'qt_...'.

    Raises
    ------

    ValueError
      No name of a function of the class can be read from it.
    """
    if 'operator' in shown.partition('(')[0]:
      return None
    #  The name stands right before the bracket that opens what the
    #  function takes, the first one outside the brackets of a template.
    depth, head = 0, shown
    for index, letter in enumerate(shown):
      if letter == '<':
        depth += 1
      elif letter == '>':
        depth -= 1
      elif letter == '(' and not depth:
        head = shown[:index]
        break
    owner, _, tail = head.rstrip().rpartition('::')
    name = (tail.split() or [''])[-1].lstrip('*&')
    if name.startswith('~') and name[1:] == self.getPythonName():
      return None
    if not owner or not name.isidentifier():
      infoSpec = """No name of a function of '%s' can be read from '%s'."""
      info = infoSpec % (self.getClassName(), shown)
      raise ValueError(' '.join(info.split()))
    if name.startswith('qt_'):
      return None
    if name == self.getPythonName():
      return '__init__'
    return '%s_' % name if keyword.iskeyword(name) else name

  def _getDeclaredAbove(self) -> Set[str]:
    """
    Gives every name, as Python has it, that a cute class this one is
    built on declares, at any distance: what this class has at that
    name in Python comes from there.
    """
    tree = self.getDependencyTree()
    #  The records the ritual generators read, kept by the tree.
    kept = tree.getKept('class records')
    className, partName = self.getClassName(), self.getPartName()
    names = set()  # type: Set[str]
    for classKey in tree.getAncestors(className, partName):
      if classKey not in self.__cute_keys__:
        continue
      if classKey not in kept:
        kept[classKey] = tree.getClassRecord(classKey[1], classKey[0])
      for member in kept[classKey].get('inner', ()):
        name = member.get('name', '') if isinstance(member, dict) else ''
        if name:
          names.add('%s_' % name if keyword.iskeyword(name) else name)
    return names

  def _findUnsupported(
      self,
      functions: List[Record],
      refused: List[Tuple[Optional[str], str, str]],
      enumNames: Set[str],
  ) -> Tuple[Tuple[str, Reasons], ...]:
    """
    Decides the names of Qt in the class that get a class raising when
    called, as 'getUnsupported' gives them.

    Parameters
    ----------

    functions : List[Record]
      The functions of the class, as 'getFunctions' gives them.

    refused : List[Tuple[Optional[str], str, str]]
      The functions with a ritual left out for what they take or give:
      the name each would have in Python, or None; the function as C++
      writes it; and the reason.

    enumNames : Set[str]
      The names the enums of the class are bound to.
    """
    entries = [*refused]
    for shown, reason in self.getRitualGenerator().getNotWritten():
      #  What Qt forbids, and what is no gap, is nothing to stand in for.
      if reason.partition(':')[0] in ('forbidden', 'not a gap'):
        continue
      entries.append((self._findDeclaredName(shown), shown, reason))
    taken = {function['pythonName'] for function in functions}
    taken.update(enumNames)
    taken.update(n.rpartition('::')[2] for n in self.getInnerNames())
    above = self._getDeclaredAbove()
    byName = dict()  # type: Dict[str, List[Tuple[str, str]]]
    for pythonName, shown, reason in entries:
      if pythonName is None or pythonName in taken:
        continue
      if pythonName != '__init__' and pythonName in above:
        continue
      #  Qt names a template by its name alone, so two templates of one
      #  name read alike, and are said once.
      said = byName.setdefault(pythonName, [])
      if (shown, reason) not in said:
        said.append((shown, reason))
    return (*((name, (*byName[name],)) for name in sorted(byName)),)

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

  def _createClassText(self) -> ClassText:
    """Gives a new 'ClassText' of the class: what writes the text of its
    file from what this generator decided."""
    classText = ClassText()
    classText.setViewer(self)
    return classText

  def getClassText(self) -> str:
    """
    Gives the whole text of the file, without writing it, as
    'ClassText.getText' writes it.

    Written for you from 'getFunctions' and 'getLeftOut': the heading,
    the names the file brings in, and the class with its docstring and
    its sections.
    """
    return self._createClassText().getText()

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

  def getNestedLines(self) -> List[str]:
    """
    Gives the class as the lines that stand in the body of the class Qt
    writes it inside, where C++, PySide6 and PyQt have it:
    'QMetaObject.Connection', as 'ClassText.getNestedLines' writes them.
    Its lines are two letters shorter, and stand two letters further in.
    """
    return self._createClassText().getNestedLines()

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
