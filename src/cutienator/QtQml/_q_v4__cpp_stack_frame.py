"""
QV4::CppStackFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::CppStackFrame to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class CppStackFrame(QV4.CppStackFrameBase):
  """
  The cute side of Qt's QV4::CppStackFrame: a plain Python object standing in
  front of one C++ QV4::CppStackFrame.

  It is built on the cute 'QV4::CppStackFrameBase', as Qt's
  QV4::CppStackFrame is built on Qt's QV4::CppStackFrameBase, and has
  everything that class has.

  C++ hands a QV4::CppStackFrame around as a copy, so every C++
  QV4::CppStackFrame behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::CppStackFrame that has a ritual and that Python
  can call so far, 16 names in all: 'init', 'isJSTypesFrame',
  'isMetaTypesFrame', 'source', 'function', 'lineNumber', 'statementNumber',
  'missingLineNumber', 'parentFrame', 'setParentFrame', 'argc', 'context',
  'callContext', 'thisObject', 'push', 'pop'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::CppStackFrame::~CppStackFrame()': the destructor: Python
    removes its C++ QV4::CppStackFrame by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QV4::CppStackFrame is created at the first use, not by
    'QV4::CppStackFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::CppStackFrame back gives a copy the ritual made
    for Python, in a new cute QV4::CppStackFrame.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::CppStackFrame'

  #  Qt's '~QV4::CppStackFrame()'. Naming it makes this a value class: Python
  #  owns every C++ QV4::CppStackFrame behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN3QV413CppStackFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isJSTypesFrame(self) -> bool:
    """
    Calls Qt's 'bool QV4::CppStackFrame::isJSTypesFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-cppstackframe.html#isJSTypesFrame
    """
    #  bool QV4::CppStackFrame::isJSTypesFrame() const
    return self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame14isJSTypesFrameEv',
    )

  def isMetaTypesFrame(self) -> bool:
    """
    Calls Qt's 'bool QV4::CppStackFrame::isMetaTypesFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-cppstackframe.html#isMetaTypesFrame
    """
    #  bool QV4::CppStackFrame::isMetaTypesFrame() const
    return self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame16isMetaTypesFrameEv',
    )

  def source(self) -> str:
    """
    Calls Qt's 'QString QV4::CppStackFrame::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#source

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CppStackFrame::source() const
    return self.uglySide.call('ritual_ZNK3QV413CppStackFrame6sourceEv')

  def function(self) -> str:
    """
    Calls Qt's 'QString QV4::CppStackFrame::function() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#function

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QV4::CppStackFrame::function() const
    return self.uglySide.call('ritual_ZNK3QV413CppStackFrame8functionEv')

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QV4::CppStackFrame::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#lineNumber
    """
    #  int QV4::CppStackFrame::lineNumber() const
    return self.uglySide.call('ritual_ZNK3QV413CppStackFrame10lineNumberEv')

  def statementNumber(self) -> int:
    """
    Calls Qt's 'int QV4::CppStackFrame::statementNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-cppstackframe.html#statementNumber
    """
    #  int QV4::CppStackFrame::statementNumber() const
    return self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame15statementNumberEv',
    )

  def missingLineNumber(self) -> int:
    """
    Calls Qt's 'int QV4::CppStackFrame::missingLineNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-cppstackframe.html#missingLineNumber
    """
    #  int QV4::CppStackFrame::missingLineNumber() const
    return self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame17missingLineNumberEv',
    )

  def parentFrame(self) -> Optional[CppStackFrame]:
    """
    Calls Qt's 'CppStackFrame *QV4::CppStackFrame::parentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#parentFrame

    Returns
    -------

    Optional[CppStackFrame]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  CppStackFrame *QV4::CppStackFrame::parentFrame() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame11parentFrameEv',
    )
    return CppStackFrame._cuteAt(address)

  def argc(self) -> int:
    """
    Calls Qt's 'int QV4::CppStackFrame::argc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#argc
    """
    #  int QV4::CppStackFrame::argc() const
    return self.uglySide.call('ritual_ZNK3QV413CppStackFrame4argcEv')

  def context(self) -> Optional[QV4.ExecutionContext]:
    """
    Calls Qt's 'ExecutionContext *QV4::CppStackFrame::context() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#context

    Returns
    -------

    Optional[QV4.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionContext *QV4::CppStackFrame::context() const
    address = self.uglySide.call('ritual_ZNK3QV413CppStackFrame7contextEv')
    return QV4.ExecutionContext._cuteAt(address)

  @overload()
  def callContext(self) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext *QV4::CppStackFrame::callContext() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#callContext

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext *QV4::CppStackFrame::callContext() const
    address = self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame11callContextEv',
    )
    return QV4.Heap.CallContext._cuteAt(address)

  @overload(WAIT['QV4.Heap.ExecutionContext'])
  @overload(NoneType)
  def callContext(
      self,
      ctx: Optional[QV4.Heap.ExecutionContext],
  ) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext
    *QV4::CppStackFrame::callContext(Heap::ExecutionContext *ctx) const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#callContext

    Parameters
    ----------

    ctx : Optional[QV4.Heap.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext
    #      *QV4::CppStackFrame::callContext(Heap::ExecutionContext *ctx)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK3QV413CppStackFrame11callContextEPNS_4Heap16ExecutionCon'
        'textE',
        self._addressOf(ctx),
    )
    return QV4.Heap.CallContext._cuteAt(address)

  def thisObject(self) -> int:
    """
    Calls Qt's 'ReturnedValue QV4::CppStackFrame::thisObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#thisObject
    """
    #  ReturnedValue QV4::CppStackFrame::thisObject() const
    return self.uglySide.call('ritual_ZNK3QV413CppStackFrame10thisObjectEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setParentFrame(self, parentFrame: Optional[CppStackFrame]) -> None:
    """
    Calls Qt's 'void QV4::CppStackFrame::setParentFrame(CppStackFrame
    *parentFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-cppstackframe.html#setParentFrame

    Parameters
    ----------

    parentFrame : Optional[CppStackFrame]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::CppStackFrame::setParentFrame(CppStackFrame *parentFrame)
    self.uglySide.call(
        'ritual_ZN3QV413CppStackFrame14setParentFrameEPS0_',
        self._addressOf(parentFrame),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QV4::CppStackFrame::CppStackFrame()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-cppstackframe.html#CppStackFrame
    """
    #  QV4::CppStackFrame::CppStackFrame()
    self._noteCreation(CppStackFrame, lambda: Rituals.call(
        'ritual_ZN3QV413CppStackFrameC1Ev',
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

  @overload(WAIT['QV4.Function'], int, QV4.CppStackFrameBase.Kind)
  @overload(NoneType, int, QV4.CppStackFrameBase.Kind)
  def init(
      self,
      v4Function: Optional[QV4.Function],
      argc: int,
      kind: QV4.CppStackFrameBase.Kind,
  ) -> None:
    """
    Calls Qt's 'void QV4::CppStackFrame::init(Function *v4Function, int argc,
    Kind kind)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#init

    Parameters
    ----------

    v4Function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    argc : int
      Passed on as it is.

    kind : QV4.CppStackFrameBase.Kind
      Passed on as its number.
    """
    #  void QV4::CppStackFrame::init(Function *v4Function, int argc, Kind
    #      kind)
    self.uglySide.call(
        'ritual_ZN3QV413CppStackFrame4initEPNS_8FunctionEiNS_17CppStackFram'
        'eBase4KindE',
        self._addressOf(v4Function), argc, kind.value,
    )

  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def push(self, engine: Optional[QV4.EngineBase]) -> None:
    """
    Calls Qt's 'void QV4::CppStackFrame::push(EngineBase *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#push

    Parameters
    ----------

    engine : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::CppStackFrame::push(EngineBase *engine)
    self.uglySide.call(
        'ritual_ZN3QV413CppStackFrame4pushEPNS_10EngineBaseE',
        self._addressOf(engine),
    )

  @overload(WAIT['QV4.EngineBase'])
  @overload(NoneType)
  def pop(self, engine: Optional[QV4.EngineBase]) -> None:
    """
    Calls Qt's 'void QV4::CppStackFrame::pop(EngineBase *engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-cppstackframe.html#pop

    Parameters
    ----------

    engine : Optional[QV4.EngineBase]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::CppStackFrame::pop(EngineBase *engine)
    self.uglySide.call(
        'ritual_ZN3QV413CppStackFrame3popEPNS_10EngineBaseE',
        self._addressOf(engine),
    )
