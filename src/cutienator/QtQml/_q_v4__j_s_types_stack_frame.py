"""
QV4::JSTypesStackFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::JSTypesStackFrame to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class JSTypesStackFrame(QV4.CppStackFrame):
  """
  The cute side of Qt's QV4::JSTypesStackFrame: a plain Python object
  standing in front of one C++ QV4::JSTypesStackFrame.

  It is built on the cute 'QV4::CppStackFrame', as Qt's
  QV4::JSTypesStackFrame is built on Qt's QV4::CppStackFrame, and has
  everything that class has.

  C++ hands a QV4::JSTypesStackFrame around as a copy, so every C++
  QV4::JSTypesStackFrame behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::JSTypesStackFrame that has a ritual and that
  Python can call so far, 20 names in all: 'init', 'argv',
  'requiredJSStackFrameSize', 'setupJSFrame', 'context', 'setContext',
  'callContext', 'isTailCalling', 'setTailCalling', 'pendingTailCall',
  'setPendingTailCall', 'yield_', 'setYield', 'yieldIsIterator',
  'setYieldIsIterator', 'callerCanHandleTailCall', 'thisObject',
  'framePointer', 'push', 'pop'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::JSTypesStackFrame::~JSTypesStackFrame()': the destructor:
    Python removes its C++ QV4::JSTypesStackFrame by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QV4::JSTypesStackFrame is created at the first use, not by
    'QV4::JSTypesStackFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::JSTypesStackFrame back gives a copy the ritual
    made for Python, in a new cute QV4::JSTypesStackFrame.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(int)
  def requiredJSStackFrameSize(nRegisters: int) -> int:
    """
    Calls Qt's 'uint QV4::JSTypesStackFrame::requiredJSStackFrameSize(uint
    nRegisters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html

    Parameters
    ----------

    nRegisters : int
      Passed on as it is.
    """
    #  uint QV4::JSTypesStackFrame::requiredJSStackFrameSize(uint nRegisters)
    return Rituals.call(
        'ritual_ZN3QV417JSTypesStackFrame24requiredJSStackFrameSizeEj',
        nRegisters,
    )

  @staticmethod
  @overload(WAIT['QV4.Function'])
  @overload(NoneType)
  def requiredJSStackFrameSize(v4Function: Optional[QV4.Function]) -> int:
    """
    Calls Qt's 'uint
    QV4::JSTypesStackFrame::requiredJSStackFrameSize(Function *v4Function)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html

    Parameters
    ----------

    v4Function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  uint QV4::JSTypesStackFrame::requiredJSStackFrameSize(Function
    #      *v4Function)
    return Rituals.call(
        'ritual_ZN3QV417JSTypesStackFrame24requiredJSStackFrameSizeEPNS_8Fu'
        'nctionE',
        CuteMixin._addressOf(v4Function),
    )

  @overload()
  def requiredJSStackFrameSize(self) -> int:
    """
    Calls Qt's 'uint QV4::JSTypesStackFrame::requiredJSStackFrameSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html
    """
    #  uint QV4::JSTypesStackFrame::requiredJSStackFrameSize() const
    return self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame24requiredJSStackFrameSizeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::JSTypesStackFrame'

  #  Qt's '~QV4::JSTypesStackFrame()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::JSTypesStackFrame behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV417JSTypesStackFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def argv(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'const Value *QV4::JSTypesStackFrame::argv() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#argv

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const Value *QV4::JSTypesStackFrame::argv() const
    address = self.uglySide.call('ritual_ZNK3QV417JSTypesStackFrame4argvEv')
    return QV4.Value._cuteAt(address)

  def context(self) -> Optional[QV4.ExecutionContext]:
    """
    Calls Qt's 'ExecutionContext *QV4::JSTypesStackFrame::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#context

    Returns
    -------

    Optional[QV4.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionContext *QV4::JSTypesStackFrame::context() const
    address = self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame7contextEv',
    )
    return QV4.ExecutionContext._cuteAt(address)

  def callContext(self) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext *QV4::JSTypesStackFrame::callContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#callContext

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext *QV4::JSTypesStackFrame::callContext() const
    address = self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame11callContextEv',
    )
    return QV4.Heap.CallContext._cuteAt(address)

  def isTailCalling(self) -> bool:
    """
    Calls Qt's 'bool QV4::JSTypesStackFrame::isTailCalling() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#isTailCalling
    """
    #  bool QV4::JSTypesStackFrame::isTailCalling() const
    return self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame13isTailCallingEv',
    )

  def pendingTailCall(self) -> bool:
    """
    Calls Qt's 'bool QV4::JSTypesStackFrame::pendingTailCall() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#pendingTailCall
    """
    #  bool QV4::JSTypesStackFrame::pendingTailCall() const
    return self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame15pendingTailCallEv',
    )

  def yield_(self) -> Optional[str]:
    """
    Calls Qt's 'const char *QV4::JSTypesStackFrame::yield() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#yield

    Returns
    -------

    Optional[str]
      The text Qt gave back. None when Qt gave back no text.
    """
    #  const char *QV4::JSTypesStackFrame::yield() const
    chars = self.uglySide.call('ritual_ZNK3QV417JSTypesStackFrame5yieldEv')
    return None if chars is None else chars.decode()

  def yieldIsIterator(self) -> bool:
    """
    Calls Qt's 'bool QV4::JSTypesStackFrame::yieldIsIterator() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#yieldIsIterator
    """
    #  bool QV4::JSTypesStackFrame::yieldIsIterator() const
    return self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame15yieldIsIteratorEv',
    )

  def callerCanHandleTailCall(self) -> bool:
    """
    Calls Qt's 'bool QV4::JSTypesStackFrame::callerCanHandleTailCall()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#callerCanHandleTailCall
    """
    #  bool QV4::JSTypesStackFrame::callerCanHandleTailCall() const
    return self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame23callerCanHandleTailCallEv',
    )

  def thisObject(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::JSTypesStackFrame::thisObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#thisObject
    """
    #  ReturnedValue QV4::JSTypesStackFrame::thisObject() const
    return self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame10thisObjectEv',
    )

  def framePointer(self) -> Optional[QV4.Value]:
    """
    Calls Qt's 'Value *QV4::JSTypesStackFrame::framePointer() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#framePointer

    Returns
    -------

    Optional[QV4.Value]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Value *QV4::JSTypesStackFrame::framePointer() const
    address = self.uglySide.call(
        'ritual_ZNK3QV417JSTypesStackFrame12framePointerEv',
    )
    return QV4.Value._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionContext'])
  @overload(NoneType)
  def setContext(self, context: Optional[QV4.ExecutionContext]) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setContext(ExecutionContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setContext

    Parameters
    ----------

    context : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::JSTypesStackFrame::setContext(ExecutionContext *context)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame10setContextEPNS_16ExecutionContex'
        'tE',
        self._addressOf(context),
    )

  @overload(bool)
  def setTailCalling(self, tailCalling: bool) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setTailCalling(bool
    tailCalling)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setTailCalling

    Parameters
    ----------

    tailCalling : bool
      Passed on as it is.
    """
    #  void QV4::JSTypesStackFrame::setTailCalling(bool tailCalling)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame14setTailCallingEb', tailCalling,
    )

  @overload(bool)
  def setPendingTailCall(self, pending: bool) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setPendingTailCall(bool
    pending)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setPendingTailCall

    Parameters
    ----------

    pending : bool
      Passed on as it is.
    """
    #  void QV4::JSTypesStackFrame::setPendingTailCall(bool pending)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame18setPendingTailCallEb', pending,
    )

  @overload(str)
  @overload(NoneType)
  def setYield(self, yield_: Optional[str]) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setYield(const char *yield)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setYield

    Parameters
    ----------

    yield_ : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QV4::JSTypesStackFrame::setYield(const char *yield)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame8setYieldEPKc',
        self._bytesOf(yield_),
    )

  @overload(bool)
  def setYieldIsIterator(self, isIter: bool) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setYieldIsIterator(bool
    isIter)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setYieldIsIterator

    Parameters
    ----------

    isIter : bool
      Passed on as it is.
    """
    #  void QV4::JSTypesStackFrame::setYieldIsIterator(bool isIter)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame18setYieldIsIteratorEb', isIter,
    )

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

  @overload(WAIT['QV4.Function'], WAIT['QV4.Value'], int)
  @overload(WAIT['QV4.Function'], NoneType, int)
  @overload(NoneType, WAIT['QV4.Value'], int)
  @overload(NoneType, NoneType, int)
  @overload(WAIT['QV4.Function'], WAIT['QV4.Value'], int, bool)
  @overload(WAIT['QV4.Function'], NoneType, int, bool)
  @overload(NoneType, WAIT['QV4.Value'], int, bool)
  @overload(NoneType, NoneType, int, bool)
  def init(
      self,
      v4Function: Optional[QV4.Function],
      argv: Optional[QV4.Value],
      argc: int,
      callerCanHandleTailCall: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::init(Function *v4Function, const
    Value *argv, int argc, bool callerCanHandleTailCall)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#init

    Parameters
    ----------

    v4Function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argv : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    callerCanHandleTailCall : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QV4::JSTypesStackFrame::init(Function *v4Function, const Value
    #      *argv, int argc, bool callerCanHandleTailCall)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame4initEPNS_8FunctionEPKNS_5ValueEib',
        self._addressOf(v4Function), self._addressOf(argv), argc,
        callerCanHandleTailCall,
    )

  @overload(
      WAIT['QV4.Value'], WAIT['QV4.Value'],
      WAIT['QV4.Heap.ExecutionContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'],
  )
  @overload(
      WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'],
  )
  @overload(
      NoneType, WAIT['QV4.Value'], WAIT['QV4.Heap.ExecutionContext'],
      WAIT['QV4.Value'], WAIT['QV4.Value'],
  )
  @overload(
      NoneType, WAIT['QV4.Value'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'],
  )
  def setupJSFrame(
      self,
      stackSpace: Optional[QV4.Value],
      function: QV4.Value,
      scope: Optional[QV4.Heap.ExecutionContext],
      thisObject: QV4.Value,
      newTarget: QV4.Value,
  ) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setupJSFrame(Value *stackSpace,
    const Value &function, const Heap::ExecutionContext *scope, const Value
    &thisObject, const Value &newTarget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setupJSFrame

    Parameters
    ----------

    stackSpace : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    scope : Optional[QV4.Heap.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    newTarget : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.
    """
    #  void QV4::JSTypesStackFrame::setupJSFrame(Value *stackSpace, const
    #      Value &function, const Heap::ExecutionContext *scope, const Value
    #      &thisObject, const Value &newTarget)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame12setupJSFrameEPNS_5ValueERKS1_PKN'
        'S_4Heap16ExecutionContextES4_S4_',
        self._addressOf(stackSpace), self._valueOf(function),
        self._addressOf(scope), self._valueOf(thisObject),
        self._valueOf(newTarget),
    )

  @overload(
      WAIT['QV4.Value'], WAIT['QV4.Value'],
      WAIT['QV4.Heap.ExecutionContext'], WAIT['QV4.Value'],
      WAIT['QV4.Value'], int, int,
  )
  @overload(
      WAIT['QV4.Value'], WAIT['QV4.Value'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], int, int,
  )
  @overload(
      NoneType, WAIT['QV4.Value'], WAIT['QV4.Heap.ExecutionContext'],
      WAIT['QV4.Value'], WAIT['QV4.Value'], int, int,
  )
  @overload(
      NoneType, WAIT['QV4.Value'], NoneType, WAIT['QV4.Value'],
      WAIT['QV4.Value'], int, int,
  )
  def setupJSFrame(
      self,
      stackSpace: Optional[QV4.Value],
      function: QV4.Value,
      scope: Optional[QV4.Heap.ExecutionContext],
      thisObject: QV4.Value,
      newTarget: QV4.Value,
      nFormals: int,
      nRegisters: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::setupJSFrame(Value *stackSpace,
    const Value &function, const Heap::ExecutionContext *scope, const Value
    &thisObject, const Value &newTarget, uint nFormals, uint nRegisters)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#setupJSFrame

    Parameters
    ----------

    stackSpace : Optional[QV4.Value]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    function : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    scope : Optional[QV4.Heap.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    thisObject : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    newTarget : QV4.Value
      Passed on as a value: Qt reads the C++ QV4::Value, which stays Python's
      own.

    nFormals : int
      Passed on as it is.

    nRegisters : int
      Passed on as it is.
    """
    #  void QV4::JSTypesStackFrame::setupJSFrame(Value *stackSpace, const
    #      Value &function, const Heap::ExecutionContext *scope, const Value
    #      &thisObject, const Value &newTarget, uint nFormals, uint
    #      nRegisters)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame12setupJSFrameEPNS_5ValueERKS1_PKN'
        'S_4Heap16ExecutionContextES4_S4_jj',
        self._addressOf(stackSpace), self._valueOf(function),
        self._addressOf(scope), self._valueOf(thisObject),
        self._valueOf(newTarget), nFormals, nRegisters,
    )

  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def push(self, engine: Optional[QV4.EngineBase]) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::push(EngineBase *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#push

    Parameters
    ----------

    engine : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::JSTypesStackFrame::push(EngineBase *engine)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame4pushEPNS_10EngineBaseE',
        self._addressOf(engine),
    )

  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def pop(self, engine: Optional[QV4.EngineBase]) -> None:
    """
    Calls Qt's 'void QV4::JSTypesStackFrame::pop(EngineBase *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-jstypesstackframe.html#pop

    Parameters
    ----------

    engine : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::JSTypesStackFrame::pop(EngineBase *engine)
    self.uglySide.call(
        'ritual_ZN3QV417JSTypesStackFrame3popEPNS_10EngineBaseE',
        self._addressOf(engine),
    )
