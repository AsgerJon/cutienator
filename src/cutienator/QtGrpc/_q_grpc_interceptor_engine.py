"""
QGrpcInterceptorEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/6.12.0/QtGrpc/private/qgrpcinterceptorengine_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QGrpcInterceptorEngine to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QGrpcInterceptorEngine(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcInterceptorEngine: a plain Python object
  standing in front of one C++ QGrpcInterceptorEngine.

  What exists
  -----------

  Every function of Qt's QGrpcInterceptorEngine that has a ritual and that
  Python can call so far, 1 name in all: 'hasHandlerFor'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcInterceptorEngine::QGrpcInterceptorEngine(const
    QAbstractGrpcChannel &parentChannel)': takes a type Python has no way to
    hand over yet.
  - Qt's 'const QGrpcInterceptorChain
    &QGrpcInterceptorEngine::interceptorChain() const': gives a type Python
    has no way to take yet.
  - Qt's 'QGrpcStartInterceptor::Continuation
    QGrpcInterceptorEngine::onStart(QGrpcOperationContext &context,
    QProtobufMessage &message, QGrpcCallOptions &callOptions)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void
    QGrpcInterceptorEngine::onInitialMetadata(QGrpcOperationContext &context,
    QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
    no way to hand over yet.
  - Qt's 'void
    QGrpcInterceptorEngine::onMessageReceived(QGrpcOperationContext &context,
    QByteArray &messageData)': takes a type Python has no way to hand over
    yet.
  - Qt's 'void QGrpcInterceptorEngine::onWriteMessage(QGrpcOperationContext
    &context, QProtobufMessage &message)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QGrpcInterceptorEngine::onWritesDone(QGrpcOperationContext
    &context)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    QGrpcInterceptorEngine::onTrailingMetadata(QGrpcOperationContext
    &context, QMultiHash<QByteArray, QByteArray> &metadata)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QGrpcInterceptorEngine::onFinished(QGrpcOperationContext
    &context, QGrpcStatus &status)': takes a type Python has no way to hand
    over yet.
  - Qt's 'void QGrpcInterceptorEngine::onCancel(QGrpcOperationContext
    &context)': takes a type Python has no way to hand over yet.
  - Qt's 'void QGrpcInterceptorEngine::addInterceptor(QSpan<const
    QtGrpcPrivate::InterceptorCapabilityBinding> bindings)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 1 a template; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QGrpcInterceptorEngine is created at the first use, not by
    'QGrpcInterceptorEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcInterceptorEngine.
  - Each name of Qt's QGrpcInterceptorEngine that has no cute function yet,
    '__init__', 'addInterceptor', 'interceptorChain', 'invoke', 'onCancel',
    'onFinished', 'onInitialMetadata', 'onMessageReceived', 'onStart',
    'onTrailingMetadata', 'onWriteMessage', 'onWritesDone',
    'setInterceptorChain', holds a function that raises
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
  __qt_class__ = 'QGrpcInterceptorEngine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtGrpc.InterceptorCapability)
  def hasHandlerFor(self, capability: QtGrpc.InterceptorCapability) -> bool:
    """
    Calls Qt's 'bool
    QGrpcInterceptorEngine::hasHandlerFor(QtGrpc::InterceptorCapability
    capability) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptorengine.html#hasHandlerFor

    Parameters
    ----------

    capability : QtGrpc.InterceptorCapability
      Passed on as its number.
    """
    #  bool QGrpcInterceptorEngine::hasHandlerFor(QtGrpc::
    #      InterceptorCapability capability) const
    return self.uglySide.call(
        'ritual_ZNK22QGrpcInterceptorEngine13hasHandlerForEN6QtGrpc21Interc'
        'eptorCapabilityE',
        capability.value,
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QGrpcInterceptorEngine::QGrpcInterceptorEngine(const
    QAbstractGrpcChannel &parentChannel)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.__init__' has no cute function yet. Qt's "
        "'QGrpcInterceptorEngine::QGrpcInterceptorEngine(const "
        "QAbstractGrpcChannel &parentChannel)': takes a type Python has no "
        "way to hand over yet.")

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
  def addInterceptor(*__, **_) -> Never:
    """
    Qt's 'void QGrpcInterceptorEngine::addInterceptor(QSpan<const
    QtGrpcPrivate::InterceptorCapabilityBinding> bindings)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.addInterceptor' has no cute function yet. "
        "Qt's 'void QGrpcInterceptorEngine::addInterceptor(QSpan<const "
        "QtGrpcPrivate::InterceptorCapabilityBinding> bindings)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def interceptorChain(*__, **_) -> Never:
    """
    Qt's 'const QGrpcInterceptorChain
    &QGrpcInterceptorEngine::interceptorChain() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.interceptorChain' has no cute function "
        "yet. Qt's 'const QGrpcInterceptorChain "
        "&QGrpcInterceptorEngine::interceptorChain() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def invoke(*__, **_) -> Never:
    """
    Qt's 'QGrpcInterceptorEngine::invoke': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.invoke' has no cute function yet. Qt's "
        "'QGrpcInterceptorEngine::invoke': a template: a pattern and no "
        "single function.")

  @staticmethod
  def onCancel(*__, **_) -> Never:
    """
    Qt's 'void QGrpcInterceptorEngine::onCancel(QGrpcOperationContext
    &context)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onCancel' has no cute function yet. Qt's "
        "'void QGrpcInterceptorEngine::onCancel(QGrpcOperationContext "
        "&context)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def onFinished(*__, **_) -> Never:
    """
    Qt's 'void QGrpcInterceptorEngine::onFinished(QGrpcOperationContext
    &context, QGrpcStatus &status)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onFinished' has no cute function yet. Qt's "
        "'void QGrpcInterceptorEngine::onFinished(QGrpcOperationContext "
        "&context, QGrpcStatus &status)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def onInitialMetadata(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcInterceptorEngine::onInitialMetadata(QGrpcOperationContext &context,
    QMultiHash<QByteArray, QByteArray> &metadata)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onInitialMetadata' has no cute function "
        "yet. Qt's 'void "
        "QGrpcInterceptorEngine::onInitialMetadata(QGrpcOperationContext "
        "&context, QMultiHash<QByteArray, QByteArray> &metadata)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def onMessageReceived(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcInterceptorEngine::onMessageReceived(QGrpcOperationContext &context,
    QByteArray &messageData)': takes a type Python has no way to hand over
    yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onMessageReceived' has no cute function "
        "yet. Qt's 'void "
        "QGrpcInterceptorEngine::onMessageReceived(QGrpcOperationContext "
        "&context, QByteArray &messageData)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def onStart(*__, **_) -> Never:
    """
    Qt's 'QGrpcStartInterceptor::Continuation
    QGrpcInterceptorEngine::onStart(QGrpcOperationContext &context,
    QProtobufMessage &message, QGrpcCallOptions &callOptions)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onStart' has no cute function yet. Qt's "
        "'QGrpcStartInterceptor::Continuation "
        "QGrpcInterceptorEngine::onStart(QGrpcOperationContext &context, "
        "QProtobufMessage &message, QGrpcCallOptions &callOptions)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def onTrailingMetadata(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcInterceptorEngine::onTrailingMetadata(QGrpcOperationContext
    &context, QMultiHash<QByteArray, QByteArray> &metadata)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onTrailingMetadata' has no cute function "
        "yet. Qt's 'void "
        "QGrpcInterceptorEngine::onTrailingMetadata(QGrpcOperationContext "
        "&context, QMultiHash<QByteArray, QByteArray> &metadata)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def onWriteMessage(*__, **_) -> Never:
    """
    Qt's 'void QGrpcInterceptorEngine::onWriteMessage(QGrpcOperationContext
    &context, QProtobufMessage &message)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onWriteMessage' has no cute function yet. "
        "Qt's 'void "
        "QGrpcInterceptorEngine::onWriteMessage(QGrpcOperationContext "
        "&context, QProtobufMessage &message)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def onWritesDone(*__, **_) -> Never:
    """
    Qt's 'void QGrpcInterceptorEngine::onWritesDone(QGrpcOperationContext
    &context)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.onWritesDone' has no cute function yet. "
        "Qt's 'void "
        "QGrpcInterceptorEngine::onWritesDone(QGrpcOperationContext "
        "&context)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setInterceptorChain(*__, **_) -> Never:
    """
    Qt's 'void
    QGrpcInterceptorEngine::setInterceptorChain(QGrpcInterceptorChain
    chain)': the compiler refuses its ritual as it would be written here:
    call to deleted constructor of 'QGrpcInterceptorChain'.
    """
    raise NotImplementedError(
        "'QGrpcInterceptorEngine.setInterceptorChain' has no cute function "
        "yet. Qt's 'void "
        "QGrpcInterceptorEngine::setInterceptorChain(QGrpcInterceptorChain "
        "chain)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of 'QGrpcInterceptorChain'.")
