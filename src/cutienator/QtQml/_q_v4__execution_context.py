"""
QV4::ExecutionContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::ExecutionContext to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ExecutionContext(QV4.Managed):
  """
  The cute side of Qt's QV4::ExecutionContext: a plain Python object standing
  in front of one C++ QV4::ExecutionContext.

  It is built on the cute 'QV4::Managed', as Qt's QV4::ExecutionContext is
  built on Qt's QV4::Managed, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::ExecutionContext that has a ritual and that
  Python can call so far, 16 names in all: '__dataTest', 'd_unchecked', 'd',
  'defaultInternalClass', 'newBlockContext', 'cloneBlockContext',
  'newCallContext', 'newWithContext', 'newCatchContext',
  'createMutableBinding', 'setProperty', 'getProperty', 'getPropertyAndBase',
  'deleteProperty', 'asCallContext', 'virtualDeleteProperty'. None can be
  made from Python: one comes out of a function of another class that gives
  one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QV4::VTable *QV4::ExecutionContext::staticVTable()': gives
    'QV4::VTable', which has no cute class yet.
  - Qt's 'const CallContext *QV4::ExecutionContext::asCallContext() const':
    takes in Python what 'CallContext
    *QV4::ExecutionContext::asCallContext()' takes.

  What has no ritual
  ------------------

  4 of the 22 functions Qt declares: 3 forbidden; 1 not a gap.

  What to expect
  --------------

  - The C++ QV4::ExecutionContext is created at the first use, not by
    'QV4::ExecutionContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::ExecutionContext.
  """

  #  The enums Qt writes inside QV4::ExecutionContext, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum):
    """
    The enum 'QV4::ExecutionContext::Error' of Qt, with the 3 names Qt gives
    in it.
    """

    NoError = Kee[int](0)
    TypeError = Kee[int](1)
    RangeError = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def defaultInternalClass(
      e: Optional[QV4.EngineBase],
  ) -> Optional[QV4.Heap.InternalClass]:
    """
    Calls Qt's 'Heap::InternalClass
    *QV4::ExecutionContext::defaultInternalClass(QV4::EngineBase *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#defaultInternalClass

    Parameters
    ----------

    e : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.InternalClass]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::InternalClass
    #      *QV4::ExecutionContext::defaultInternalClass(QV4::EngineBase *e)
    address = Rituals.call(
        'ritual_ZN3QV416ExecutionContext20defaultInternalClassEPNS_10Engine'
        'BaseE',
        CuteMixin._addressOf(e),
    )
    return QV4.Heap.InternalClass._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.CppStackFrame'], int)
  @overload(NoneType, int)
  def newBlockContext(
      frame: Optional[QV4.CppStackFrame],
      blockIndex: int,
  ) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext
    *QV4::ExecutionContext::newBlockContext(QV4::CppStackFrame *frame, int
    blockIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#newBlockContext

    Parameters
    ----------

    frame : Optional[QV4.CppStackFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    blockIndex : int
      Passed on as it is.

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext
    #      *QV4::ExecutionContext::newBlockContext(QV4::CppStackFrame *frame,
    #      int blockIndex)
    address = Rituals.call(
        'ritual_ZN3QV416ExecutionContext15newBlockContextEPNS_13CppStackFra'
        'meEi',
        CuteMixin._addressOf(frame), blockIndex,
    )
    return QV4.Heap.CallContext._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.ExecutionEngine'], WAIT['QV4.Heap.CallContext'])
  @overload(WAIT['QV4.ExecutionEngine'], NoneType)
  @overload(NoneType, WAIT['QV4.Heap.CallContext'])
  @overload(NoneType, NoneType)
  def cloneBlockContext(
      engine: Optional[QV4.ExecutionEngine],
      callContext: Optional[QV4.Heap.CallContext],
  ) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext
    *QV4::ExecutionContext::cloneBlockContext(ExecutionEngine *engine,
    Heap::CallContext *callContext)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#cloneBlockContext

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    callContext : Optional[QV4.Heap.CallContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext
    #      *QV4::ExecutionContext::cloneBlockContext(ExecutionEngine *engine,
    #      Heap::CallContext *callContext)
    address = Rituals.call(
        'ritual_ZN3QV416ExecutionContext17cloneBlockContextEPNS_15Execution'
        'EngineEPNS_4Heap11CallContextE',
        CuteMixin._addressOf(engine), CuteMixin._addressOf(callContext),
    )
    return QV4.Heap.CallContext._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.JSTypesStackFrame'])
  @overload(NoneType)
  def newCallContext(
      frame: Optional[QV4.JSTypesStackFrame],
  ) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext
    *QV4::ExecutionContext::newCallContext(JSTypesStackFrame *frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#newCallContext

    Parameters
    ----------

    frame : Optional[QV4.JSTypesStackFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext
    #      *QV4::ExecutionContext::newCallContext(JSTypesStackFrame *frame)
    address = Rituals.call(
        'ritual_ZN3QV416ExecutionContext14newCallContextEPNS_17JSTypesStack'
        'FrameE',
        CuteMixin._addressOf(frame),
    )
    return QV4.Heap.CallContext._cuteAt(address)

  @staticmethod
  @overload(WAIT['QV4.CppStackFrame'], int, WAIT['QV4.Heap.String'])
  @overload(WAIT['QV4.CppStackFrame'], int, NoneType)
  @overload(NoneType, int, WAIT['QV4.Heap.String'])
  @overload(NoneType, int, NoneType)
  def newCatchContext(
      frame: Optional[QV4.CppStackFrame],
      blockIndex: int,
      exceptionVarName: Optional[QV4.Heap.String],
  ) -> Optional[QV4.Heap.ExecutionContext]:
    """
    Calls Qt's 'Heap::ExecutionContext
    *QV4::ExecutionContext::newCatchContext(CppStackFrame *frame, int
    blockIndex, Heap::String *exceptionVarName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#newCatchContext

    Parameters
    ----------

    frame : Optional[QV4.CppStackFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    blockIndex : int
      Passed on as it is.

    exceptionVarName : Optional[QV4.Heap.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ExecutionContext
    #      *QV4::ExecutionContext::newCatchContext(CppStackFrame *frame, int
    #      blockIndex, Heap::String *exceptionVarName)
    address = Rituals.call(
        'ritual_ZN3QV416ExecutionContext15newCatchContextEPNS_13CppStackFra'
        'meEiPNS_4Heap6StringE',
        CuteMixin._addressOf(frame), blockIndex,
        CuteMixin._addressOf(exceptionVarName),
    )
    return QV4.Heap.ExecutionContext._cuteAt(address)

  @staticmethod
  @overload(QV4.Managed, WAIT['QV4.PropertyKey'])
  @overload(NoneType, WAIT['QV4.PropertyKey'])
  def virtualDeleteProperty(
      a0: Optional[QV4.Managed],
      a1: QV4.PropertyKey,
  ) -> bool:
    """
    Calls Qt's 'bool QV4::ExecutionContext::virtualDeleteProperty(Managed
    *a0, PropertyKey a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#virtualDeleteProperty

    Parameters
    ----------

    a0 : Optional[QV4.Managed]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QV4.PropertyKey
      Passed on as a value: Qt reads the C++ QV4::PropertyKey, which stays
      Python's own.
    """
    #  bool QV4::ExecutionContext::virtualDeleteProperty(Managed *a0,
    #      PropertyKey a1)
    return Rituals.call(
        'ritual_ZN3QV416ExecutionContext21virtualDeletePropertyEPNS_7Manage'
        'dENS_11PropertyKeyE',
        CuteMixin._addressOf(a0), CuteMixin._valueOf(a1),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::ExecutionContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def d_unchecked(self) -> Optional[QV4.Heap.ExecutionContext]:
    """
    Calls Qt's 'QV4::Heap::ExecutionContext
    *QV4::ExecutionContext::d_unchecked() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#d_unchecked

    Returns
    -------

    Optional[QV4.Heap.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ExecutionContext *QV4::ExecutionContext::d_unchecked()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV416ExecutionContext11d_uncheckedEv',
    )
    return QV4.Heap.ExecutionContext._cuteAt(address)

  def d(self) -> Optional[QV4.Heap.ExecutionContext]:
    """
    Calls Qt's 'QV4::Heap::ExecutionContext *QV4::ExecutionContext::d()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-executioncontext.html#d

    Returns
    -------

    Optional[QV4.Heap.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::Heap::ExecutionContext *QV4::ExecutionContext::d() const
    address = self.uglySide.call('ritual_ZNK3QV416ExecutionContext1dEv')
    return QV4.Heap.ExecutionContext._cuteAt(address)

  @overload(WAIT['QV4.Heap.Object'])
  @overload(NoneType)
  def newWithContext(
      self,
      with_: Optional[QV4.Heap.Object],
  ) -> Optional[QV4.Heap.ExecutionContext]:
    """
    Calls Qt's 'Heap::ExecutionContext
    *QV4::ExecutionContext::newWithContext(Heap::Object *with) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#newWithContext

    Parameters
    ----------

    with_ : Optional[QV4.Heap.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::ExecutionContext
    #      *QV4::ExecutionContext::newWithContext(Heap::Object *with) const
    address = self.uglySide.call(
        'ritual_ZNK3QV416ExecutionContext14newWithContextEPNS_4Heap6ObjectE',
        self._addressOf(with_),
    )
    return QV4.Heap.ExecutionContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.String'], QV4.Value)
  @overload(NoneType, QV4.Value)
  def setProperty(
      self,
      name: Optional[QV4.String],
      value: QV4.Value,
  ) -> Error:
    """
    Calls Qt's 'Error QV4::ExecutionContext::setProperty(String *name, const
    Value &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#setProperty

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    value : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QV4::ExecutionContext::setProperty(String *name, const Value
    #      &value)
    return ExecutionContext.Error(self.uglySide.call(
        'ritual_ZN3QV416ExecutionContext11setPropertyEPNS_6StringERKNS_5Val'
        'ueE',
        self._addressOf(name), self._valueOf(value),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def __dataTest(self) -> None:
    """
    Calls Qt's 'void QV4::ExecutionContext::__dataTest()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#__dataTest
    """
    #  void QV4::ExecutionContext::__dataTest()
    self.uglySide.call('ritual_ZN3QV416ExecutionContext10__dataTestEv')

  @overload(WAIT['QV4.String'], bool)
  @overload(NoneType, bool)
  def createMutableBinding(
      self,
      name: Optional[QV4.String],
      deletable: bool,
  ) -> None:
    """
    Calls Qt's 'void QV4::ExecutionContext::createMutableBinding(String
    *name, bool deletable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#createMutableBinding

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    deletable : bool
      Passed on as it is.
    """
    #  void QV4::ExecutionContext::createMutableBinding(String *name, bool
    #      deletable)
    self.uglySide.call(
        'ritual_ZN3QV416ExecutionContext20createMutableBindingEPNS_6StringE'
        'b',
        self._addressOf(name), deletable,
    )

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def getProperty(self, name: Optional[QV4.String]) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::ExecutionContext::getProperty(String
    *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#getProperty

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::ExecutionContext::getProperty(String *name)
    return self.uglySide.call(
        'ritual_ZN3QV416ExecutionContext11getPropertyEPNS_6StringE',
        self._addressOf(name),
    )

  @overload(WAIT['QV4.String'], QV4.Value)
  @overload(WAIT['QV4.String'], NoneType)
  @overload(NoneType, QV4.Value)
  @overload(NoneType, NoneType)
  def getPropertyAndBase(
      self,
      name: Optional[QV4.String],
      base: Optional[QV4.Value],
  ) -> int:
    """
    Calls Qt's 'ReturnedValue
    QV4::ExecutionContext::getPropertyAndBase(String *name, Value *base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#getPropertyAndBase

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    base : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  ReturnedValue QV4::ExecutionContext::getPropertyAndBase(String *name,
    #      Value *base)
    return self.uglySide.call(
        'ritual_ZN3QV416ExecutionContext18getPropertyAndBaseEPNS_6StringEPN'
        'S_5ValueE',
        self._addressOf(name), self._addressOf(base),
    )

  @overload(WAIT['QV4.String'])
  @overload(NoneType)
  def deleteProperty(self, name: Optional[QV4.String]) -> bool:
    """
    Calls Qt's 'bool QV4::ExecutionContext::deleteProperty(String *name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#deleteProperty

    Parameters
    ----------

    name : Optional[QV4.String]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QV4::ExecutionContext::deleteProperty(String *name)
    return self.uglySide.call(
        'ritual_ZN3QV416ExecutionContext14deletePropertyEPNS_6StringE',
        self._addressOf(name),
    )

  def asCallContext(self) -> Optional[QV4.CallContext]:
    """
    Calls Qt's 'CallContext *QV4::ExecutionContext::asCallContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-executioncontext.html#asCallContext

    Returns
    -------

    Optional[QV4.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CallContext *QV4::ExecutionContext::asCallContext()
    address = self.uglySide.call(
        'ritual_ZN3QV416ExecutionContext13asCallContextEv',
    )
    return QV4.CallContext._cuteAt(address)
