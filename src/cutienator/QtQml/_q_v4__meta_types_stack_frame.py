"""
QV4::MetaTypesStackFrame binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4stackframe_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::MetaTypesStackFrame to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQmlPrivate, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaType, QObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MetaTypesStackFrame(QV4.CppStackFrame):
  """
  The cute side of Qt's QV4::MetaTypesStackFrame: a plain Python object
  standing in front of one C++ QV4::MetaTypesStackFrame.

  It is built on the cute 'QV4::CppStackFrame', as Qt's
  QV4::MetaTypesStackFrame is built on Qt's QV4::CppStackFrame, and has
  everything that class has.

  C++ hands a QV4::MetaTypesStackFrame around as a copy, so every C++
  QV4::MetaTypesStackFrame behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QV4::MetaTypesStackFrame that has a ritual and that
  Python can call so far, 11 names in all: 'returnType',
  'isReturnValueUndefined', 'setReturnValueUndefined', 'argTypes',
  'returnAndArgTypes', 'thisObject', 'context', 'setContext', 'locals',
  'setLocals', 'callContext'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QV4::MetaTypesStackFrame::init(Function *v4Function, QObject
    *thisObject, ExecutionContext *context, void **returnAndArgs, const
    QMetaType *metaTypes, int argc)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void *QV4::MetaTypesStackFrame::returnValue() const': gives 'void',
    which has no cute class yet.
  - Qt's 'void **QV4::MetaTypesStackFrame::argv() const': gives a type Python
    has no way to take yet.
  - Qt's 'void **QV4::MetaTypesStackFrame::returnAndArgValues() const': gives
    a type Python has no way to take yet.
  - Qt's 'QV4::MetaTypesStackFrame::~MetaTypesStackFrame()': the destructor:
    Python removes its C++ QV4::MetaTypesStackFrame by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ QV4::MetaTypesStackFrame is created at the first use, not by
    'QV4::MetaTypesStackFrame(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QV4::MetaTypesStackFrame back gives a copy the ritual
    made for Python, in a new cute QV4::MetaTypesStackFrame.
  - Each name of Qt's QV4::MetaTypesStackFrame that has no cute function yet,
    'argv', 'returnAndArgValues', 'returnValue', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::MetaTypesStackFrame'

  #  Qt's '~QV4::MetaTypesStackFrame()'. Naming it makes this a value class:
  #  Python owns every C++ QV4::MetaTypesStackFrame behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN3QV419MetaTypesStackFrameD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def returnType(self) -> QMetaType:
    """
    Calls Qt's 'QMetaType QV4::MetaTypesStackFrame::returnType() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#returnType

    Returns
    -------

    QMetaType
      A new cute QMetaType around the copy Qt gave back. Python owns it.
    """
    #  QMetaType QV4::MetaTypesStackFrame::returnType() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame10returnTypeEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteOwning(address)

  def isReturnValueUndefined(self) -> bool:
    """
    Calls Qt's 'bool QV4::MetaTypesStackFrame::isReturnValueUndefined()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html
    """
    #  bool QV4::MetaTypesStackFrame::isReturnValueUndefined() const
    return self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame22isReturnValueUndefinedEv',
    )

  def argTypes(self) -> Optional[QMetaType]:
    """
    Calls Qt's 'const QMetaType *QV4::MetaTypesStackFrame::argTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#argTypes

    Returns
    -------

    Optional[QMetaType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaType *QV4::MetaTypesStackFrame::argTypes() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame8argTypesEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteAt(address)

  def returnAndArgTypes(self) -> Optional[QMetaType]:
    """
    Calls Qt's 'const QMetaType
    *QV4::MetaTypesStackFrame::returnAndArgTypes() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#returnAndArgTypes

    Returns
    -------

    Optional[QMetaType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaType *QV4::MetaTypesStackFrame::returnAndArgTypes() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame17returnAndArgTypesEv',
    )
    from ..QtCore import QMetaType
    return QMetaType._cuteAt(address)

  def thisObject(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QV4::MetaTypesStackFrame::thisObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#thisObject

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QV4::MetaTypesStackFrame::thisObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame10thisObjectEv',
    )
    from ..QtCore import QObject
    return QObject._cuteAt(address)

  def context(self) -> Optional[QV4.ExecutionContext]:
    """
    Calls Qt's 'ExecutionContext *QV4::MetaTypesStackFrame::context() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#context

    Returns
    -------

    Optional[QV4.ExecutionContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ExecutionContext *QV4::MetaTypesStackFrame::context() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame7contextEv',
    )
    return QV4.ExecutionContext._cuteAt(address)

  def locals(self) -> Optional[QQmlPrivate.AOTTrackedLocalsStorage]:
    """
    Calls Qt's 'const QQmlPrivate::AOTTrackedLocalsStorage
    *QV4::MetaTypesStackFrame::locals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#locals

    Returns
    -------

    Optional[QQmlPrivate.AOTTrackedLocalsStorage]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlPrivate::AOTTrackedLocalsStorage
    #      *QV4::MetaTypesStackFrame::locals() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame6localsEv',
    )
    return QQmlPrivate.AOTTrackedLocalsStorage._cuteAt(address)

  def callContext(self) -> Optional[QV4.Heap.CallContext]:
    """
    Calls Qt's 'Heap::CallContext *QV4::MetaTypesStackFrame::callContext()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#callContext

    Returns
    -------

    Optional[QV4.Heap.CallContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Heap::CallContext *QV4::MetaTypesStackFrame::callContext() const
    address = self.uglySide.call(
        'ritual_ZNK3QV419MetaTypesStackFrame11callContextEv',
    )
    return QV4.Heap.CallContext._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setReturnValueUndefined(self) -> None:
    """
    Calls Qt's 'void QV4::MetaTypesStackFrame::setReturnValueUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html
    """
    #  void QV4::MetaTypesStackFrame::setReturnValueUndefined()
    self.uglySide.call(
        'ritual_ZN3QV419MetaTypesStackFrame23setReturnValueUndefinedEv',
    )

  @overload(WAIT['QV4.ExecutionContext'])
  @overload(NoneType)
  def setContext(self, context: Optional[QV4.ExecutionContext]) -> None:
    """
    Calls Qt's 'void QV4::MetaTypesStackFrame::setContext(ExecutionContext
    *context)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#setContext

    Parameters
    ----------

    context : Optional[QV4.ExecutionContext]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::MetaTypesStackFrame::setContext(ExecutionContext *context)
    self.uglySide.call(
        'ritual_ZN3QV419MetaTypesStackFrame10setContextEPNS_16ExecutionCont'
        'extE',
        self._addressOf(context),
    )

  @overload(WAIT['QQmlPrivate.AOTTrackedLocalsStorage'])
  @overload(NoneType)
  def setLocals(
      self,
      locals: Optional[QQmlPrivate.AOTTrackedLocalsStorage],
  ) -> None:
    """
    Calls Qt's 'void QV4::MetaTypesStackFrame::setLocals(const
    QQmlPrivate::AOTTrackedLocalsStorage *locals)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-metatypesstackframe.html#setLocals

    Parameters
    ----------

    locals : Optional[QQmlPrivate.AOTTrackedLocalsStorage]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QV4::MetaTypesStackFrame::setLocals(const
    #      QQmlPrivate::AOTTrackedLocalsStorage *locals)
    self.uglySide.call(
        'ritual_ZN3QV419MetaTypesStackFrame9setLocalsEPKN11QQmlPrivate23AOT'
        'TrackedLocalsStorageE',
        self._addressOf(locals),
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

  @staticmethod
  def argv(*__, **_) -> Never:
    """
    Qt's 'void **QV4::MetaTypesStackFrame::argv() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.MetaTypesStackFrame.argv' has no cute function yet. Qt's "
        "'void **QV4::MetaTypesStackFrame::argv() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def returnAndArgValues(*__, **_) -> Never:
    """
    Qt's 'void **QV4::MetaTypesStackFrame::returnAndArgValues() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QV4.MetaTypesStackFrame.returnAndArgValues' has no cute function "
        "yet. Qt's 'void **QV4::MetaTypesStackFrame::returnAndArgValues() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def returnValue(*__, **_) -> Never:
    """
    Qt's 'void *QV4::MetaTypesStackFrame::returnValue() const': gives 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QV4.MetaTypesStackFrame.returnValue' has no cute function yet. "
        "Qt's 'void *QV4::MetaTypesStackFrame::returnValue() const': gives "
        "'void', which has no cute class yet.")
