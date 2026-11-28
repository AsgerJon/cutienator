"""
QV4::Function binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4function_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Function to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlPrivate, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl
  from . import QQmlSourceLocation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Function(QV4.FunctionData):
  """
  The cute side of Qt's QV4::Function: a plain Python object standing in
  front of one C++ QV4::Function.

  It is built on the cute 'QV4::FunctionData', as Qt's QV4::Function is built
  on Qt's QV4::FunctionData, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Function that has a ritual and that Python can
  call so far, 17 names in all: 'executableCompilationUnit', 'runtimeString',
  'call', 'create', 'destroy', 'mark', 'updateInternalClass', 'name',
  'sourceFile', 'finalUrl', 'isStrict', 'isArrowFunction', 'isGenerator',
  'isClosureWrapper', 'sourceLocation', 'nestedFunction', 'isJittable'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Function::~Function()': the destructor: Python never removes a
    C++ QV4::Function.
  - Qt's 'bool QV4::Function::call(QObject *thisObject, void **a, const
    QMetaType *types, int argc, ExecutionContext *context)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QString QV4::Function::prettyName(const Function *function, const
    void *address)': names 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QV4::Function is created at the first use, not by
    'QV4::Function(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Function.
  - Each name of Qt's QV4::Function that has no cute function yet,
    'prettyName', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QV4::Function, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Kind(CuteNum):
    """
    The enum 'QV4::Function::Kind' of Qt, with the 4 names Qt gives in it.
    """

    JsUntyped = Kee[int](0)
    JsTyped = Kee[int](1)
    AotCompiled = Kee[int](2)
    Eval = Kee[int](3)

  #  The classes Qt writes inside QV4::Function, each a class in here as in
  #  C++.

  class AOTCompiledFunction(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Function::AOTCompiledFunction: a plain Python
    object standing in front of one C++ QV4::Function::AOTCompiledFunction.

    C++ hands a QV4::Function::AOTCompiledFunction around as a copy, so every
    C++ QV4::Function::AOTCompiledFunction behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QV4::Function::AOTCompiledFunction yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Function::AOTCompiledFunction::~AOTCompiledFunction()': the
      destructor: Python removes its C++ QV4::Function::AOTCompiledFunction
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Function::AOTCompiledFunction is created at the first use,
      not by 'QV4::Function::AOTCompiledFunction(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Function::AOTCompiledFunction back gives a
      copy the ritual made for Python, in a new cute
      QV4::Function::AOTCompiledFunction.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Function::AOTCompiledFunction'

    #  Qt's '~QV4::Function::AOTCompiledFunction()'. Naming it makes this a
    #  value class: Python owns every C++ QV4::Function::AOTCompiledFunction
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV48Function19AOTCompiledFunctionD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class JSTypedFunction(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Function::JSTypedFunction: a plain Python
    object standing in front of one C++ QV4::Function::JSTypedFunction.

    C++ hands a QV4::Function::JSTypedFunction around as a copy, so every C++
    QV4::Function::JSTypedFunction behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QV4::Function::JSTypedFunction yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Function::JSTypedFunction::~JSTypedFunction()': the
      destructor: Python removes its C++ QV4::Function::JSTypedFunction by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QV4::Function::JSTypedFunction is created at the first use, not
      by 'QV4::Function::JSTypedFunction(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Function::JSTypedFunction back gives a copy
      the ritual made for Python, in a new cute
      QV4::Function::JSTypedFunction.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Function::JSTypedFunction'

    #  Qt's '~QV4::Function::JSTypedFunction()'. Naming it makes this a value
    #  class: Python owns every C++ QV4::Function::JSTypedFunction behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV48Function15JSTypedFunctionD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'], NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      NoneType, WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType,
      WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType,
      WAIT['QV4.CompiledData.Function'], NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, NoneType,
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'], NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'], NoneType,
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'], NoneType, NoneType,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(NoneType, NoneType, WAIT['QV4.CompiledData.Function'], NoneType)
  @overload(
      NoneType, NoneType, NoneType, WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(NoneType, NoneType, NoneType, NoneType)
  def create(
      engine: Optional[QV4.ExecutionEngine],
      unit: Optional[QV4.ExecutableCompilationUnit],
      function: Optional[QV4.CompiledData.Function],
      aotFunction: Optional[QQmlPrivate.AOTCompiledFunction],
  ) -> Optional[Function]:
    """
    Calls Qt's 'Function *QV4::Function::create(ExecutionEngine *engine,
    ExecutableCompilationUnit *unit, const CompiledData::Function *function,
    const QQmlPrivate::AOTCompiledFunction *aotFunction)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#create

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    unit : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.CompiledData.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aotFunction : Optional[QQmlPrivate.AOTCompiledFunction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Function *QV4::Function::create(ExecutionEngine *engine,
    #      ExecutableCompilationUnit *unit, const CompiledData::Function
    #      *function, const QQmlPrivate::AOTCompiledFunction *aotFunction)
    address = Rituals.call(
        'ritual_ZN3QV48Function6createEPNS_15ExecutionEngineEPNS_25Executab'
        'leCompilationUnitEPKNS_12CompiledData8FunctionEPKN11QQmlPrivate19A'
        'OTCompiledFunctionE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(unit),
        CuteMixin._addressOf(function), CuteMixin._addressOf(aotFunction),
    )
    return Function._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Function'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def executableCompilationUnit(
      self,
  ) -> Optional[QV4.ExecutableCompilationUnit]:
    """
    Calls Qt's 'QV4::ExecutableCompilationUnit
    *QV4::Function::executableCompilationUnit() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-function.html#executableCompilationUnit

    Returns
    -------

    Optional[QV4.ExecutableCompilationUnit]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutableCompilationUnit
    #      *QV4::Function::executableCompilationUnit() const
    address = self.uglySide.call(
        'ritual_ZNK3QV48Function25executableCompilationUnitEv',
    )
    return QV4.ExecutableCompilationUnit._cuteAt(address)

  @overload(int)
  def runtimeString(self, i: int) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'QV4::Heap::String *QV4::Function::runtimeString(uint i)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#runtimeString

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::String *QV4::Function::runtimeString(uint i) const
    address = self.uglySide.call(
        'ritual_ZNK3QV48Function13runtimeStringEj', i,
    )
    return QV4.Heap.String._cuteAt(address)

  def name(self) -> Optional[QV4.Heap.String]:
    """
    Calls Qt's 'Heap::String *QV4::Function::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#name

    Returns
    -------

    Optional[QV4.Heap.String]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::String *QV4::Function::name() const
    address = self.uglySide.call('ritual_ZNK3QV48Function4nameEv')
    return QV4.Heap.String._cuteAt(address)

  def sourceFile(self) -> str:
    """
    Calls Qt's 'QString QV4::Function::sourceFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#sourceFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::Function::sourceFile() const
    return self.uglySide.call('ritual_ZNK3QV48Function10sourceFileEv')

  def finalUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QV4::Function::finalUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#finalUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QV4::Function::finalUrl() const
    address = self.uglySide.call('ritual_ZNK3QV48Function8finalUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def isStrict(self) -> bool:
    """
    Calls Qt's 'bool QV4::Function::isStrict() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#isStrict
    """
    #  bool QV4::Function::isStrict() const
    return self.uglySide.call('ritual_ZNK3QV48Function8isStrictEv')

  def isArrowFunction(self) -> bool:
    """
    Calls Qt's 'bool QV4::Function::isArrowFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#isArrowFunction
    """
    #  bool QV4::Function::isArrowFunction() const
    return self.uglySide.call('ritual_ZNK3QV48Function15isArrowFunctionEv')

  def isGenerator(self) -> bool:
    """
    Calls Qt's 'bool QV4::Function::isGenerator() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#isGenerator
    """
    #  bool QV4::Function::isGenerator() const
    return self.uglySide.call('ritual_ZNK3QV48Function11isGeneratorEv')

  def isClosureWrapper(self) -> bool:
    """
    Calls Qt's 'bool QV4::Function::isClosureWrapper() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#isClosureWrapper
    """
    #  bool QV4::Function::isClosureWrapper() const
    return self.uglySide.call('ritual_ZNK3QV48Function16isClosureWrapperEv')

  def sourceLocation(self) -> QQmlSourceLocation:
    """
    Calls Qt's 'QQmlSourceLocation QV4::Function::sourceLocation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#sourceLocation

    Returns
    -------

    QQmlSourceLocation
      A new cute QQmlSourceLocation around the copy Qt gave back. Python owns
      it.
    """
    #  QQmlSourceLocation QV4::Function::sourceLocation() const
    address = self.uglySide.call('ritual_ZNK3QV48Function14sourceLocationEv')
    from . import QQmlSourceLocation
    return QQmlSourceLocation._cuteOwning(address)

  def nestedFunction(self) -> Optional[Function]:
    """
    Calls Qt's 'Function *QV4::Function::nestedFunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#nestedFunction

    Returns
    -------

    Optional[Function]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Function *QV4::Function::nestedFunction() const
    address = self.uglySide.call('ritual_ZNK3QV48Function14nestedFunctionEv')
    return Function._cuteAt(address)

  def isJittable(self) -> bool:
    """
    Calls Qt's 'bool QV4::Function::isJittable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#isJittable
    """
    #  bool QV4::Function::isJittable() const
    return self.uglySide.call('ritual_ZNK3QV48Function10isJittableEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'], NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      NoneType, WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], WAIT['QV4.ExecutableCompilationUnit'],
      NoneType, NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType,
      WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType,
      WAIT['QV4.CompiledData.Function'], NoneType,
  )
  @overload(
      WAIT['QV4.ExecutionEngine'], NoneType, NoneType,
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(WAIT['QV4.ExecutionEngine'], NoneType, NoneType, NoneType)
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'],
      WAIT['QV4.CompiledData.Function'], NoneType,
  )
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'], NoneType,
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(
      NoneType, WAIT['QV4.ExecutableCompilationUnit'], NoneType, NoneType,
  )
  @overload(
      NoneType, NoneType, WAIT['QV4.CompiledData.Function'],
      WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(NoneType, NoneType, WAIT['QV4.CompiledData.Function'], NoneType)
  @overload(
      NoneType, NoneType, NoneType, WAIT['QQmlPrivate.AOTCompiledFunction'],
  )
  @overload(NoneType, NoneType, NoneType, NoneType)
  def __init__(
      self,
      engine: Optional[QV4.ExecutionEngine],
      unit: Optional[QV4.ExecutableCompilationUnit],
      function: Optional[QV4.CompiledData.Function],
      aotFunction: Optional[QQmlPrivate.AOTCompiledFunction],
  ) -> None:
    """
    Notes what was given, for Qt's 'QV4::Function::Function(ExecutionEngine
    *engine, ExecutableCompilationUnit *unit, const CompiledData::Function
    *function, const QQmlPrivate::AOTCompiledFunction *aotFunction)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#Function

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    unit : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : Optional[QV4.CompiledData.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    aotFunction : Optional[QQmlPrivate.AOTCompiledFunction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Function::Function(ExecutionEngine *engine,
    #      ExecutableCompilationUnit *unit, const CompiledData::Function
    #      *function, const QQmlPrivate::AOTCompiledFunction *aotFunction)
    self._noteCreation(Function, lambda: Rituals.call(
        'ritual_ZN3QV48FunctionC1EPNS_15ExecutionEngineEPNS_25ExecutableCom'
        'pilationUnitEPKNS_12CompiledData8FunctionEPKN11QQmlPrivate19AOTCom'
        'piledFunctionE',
        self._addressOf(engine), self._addressOf(unit),
        self._addressOf(function), self._addressOf(aotFunction),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload(
      WAIT['QV4.Value'], WAIT['QV4.Value'], int,
      WAIT['QV4.ExecutionContext'],
  )
  @overload(WAIT['QV4.Value'], WAIT['QV4.Value'], int, NoneType)
  @overload(WAIT['QV4.Value'], NoneType, int, WAIT['QV4.ExecutionContext'])
  @overload(WAIT['QV4.Value'], NoneType, int, NoneType)
  @overload(NoneType, WAIT['QV4.Value'], int, WAIT['QV4.ExecutionContext'])
  @overload(NoneType, WAIT['QV4.Value'], int, NoneType)
  @overload(NoneType, NoneType, int, WAIT['QV4.ExecutionContext'])
  @overload(NoneType, NoneType, int, NoneType)
  def call(
      self,
      thisObject: Optional[QV4.Value],
      argv: Optional[QV4.Value],
      argc: int,
      context: Optional[QV4.ExecutionContext],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::Function::call(const Value *thisObject,
    const Value *argv, int argc, ExecutionContext *context)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#call

    Parameters
    ----------

    thisObject : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    context : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::Function::call(const Value *thisObject, const Value
    #      *argv, int argc, ExecutionContext *context)
    return self.uglySide.call(
        'ritual_ZN3QV48Function4callEPKNS_5ValueES3_iPNS_16ExecutionContext'
        'E',
        self._addressOf(thisObject), self._addressOf(argv), argc,
        self._addressOf(context),
    )

  def destroy(self) -> None:
    """
    Calls Qt's 'void QV4::Function::destroy()'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#destroy
    """
    #  void QV4::Function::destroy()
    self.uglySide.call('ritual_ZN3QV48Function7destroyEv')

  @overload(WAIT['QV4.MarkStack'])
  @overload(NoneType)
  def mark(self, ms: Optional[QV4.MarkStack]) -> None:
    """
    Calls Qt's 'void QV4::Function::mark(QV4::MarkStack *ms)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-function.html#mark

    Parameters
    ----------

    ms : Optional[QV4.MarkStack]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::Function::mark(QV4::MarkStack *ms)
    self.uglySide.call(
        'ritual_ZN3QV48Function4markEPNS_9MarkStackE', self._addressOf(ms),
    )

  @overload(WAIT['QV4.ExecutionEngine'], QList[QByteArray])
  @overload(NoneType, QList[QByteArray])
  def updateInternalClass(
      self,
      engine: Optional[QV4.ExecutionEngine],
      parameters: QList[QByteArray],
  ) -> None:
    """
    Calls Qt's 'void QV4::Function::updateInternalClass(ExecutionEngine
    *engine, const QList<QByteArray> &parameters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-function.html#updateInternalClass

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parameters : QList[QByteArray]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QV4::Function::updateInternalClass(ExecutionEngine *engine, const
    #      QList<QByteArray> &parameters)
    self.uglySide.call(
        'ritual_ZN3QV48Function19updateInternalClassEPNS_15ExecutionEngineE'
        'RK5QListI10QByteArrayE',
        self._addressOf(engine), self._valueOf(parameters),
    )

  @staticmethod
  def prettyName(*__, **_) -> Never:
    """
    Qt's 'QString QV4::Function::prettyName(const Function *function, const
    void *address)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.Function.prettyName' has no cute function yet. Qt's 'QString "
        "QV4::Function::prettyName(const Function *function, const void "
        "*address)': names 'void', which has no cute class yet.")
