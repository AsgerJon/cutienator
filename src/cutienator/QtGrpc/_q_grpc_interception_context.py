"""
QGrpcInterceptionContext binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcinterceptor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute, WAIT
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QGrpcCallOptions


class QGrpcInterceptionContext(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcInterceptionContext: a plain Python object
  standing in front of one C++ QGrpcInterceptionContext.

  What exists
  -----------

  Every function of Qt's QGrpcInterceptionContext that has a ritual and that
  Python can call so far, 4 names in all: 'version', 'descriptor',
  'callOptions', 'operationId'. None can be made from Python: one comes out
  of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcInterceptionContext::~QGrpcInterceptionContext()': the
    destructor: Python never removes a C++ QGrpcInterceptionContext.
  - Qt's 'const QAbstractGrpcChannel &QGrpcInterceptionContext::channel()
    const': gives a type Python has no way to take yet.
  - Qt's 'QGrpcInterceptionContext::QGrpcInterceptionContext(const
    QAbstractGrpcChannel &channel, QGrpcOperationContext &context)': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  11 of the 18 functions Qt declares: 11 forbidden.

  What to expect
  --------------

  - The C++ QGrpcInterceptionContext is created at the first use, not by
    'QGrpcInterceptionContext(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcInterceptionContext.
  - Each name of Qt's QGrpcInterceptionContext that has no cute function yet,
    '__init__', 'channel', holds a function that raises
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
  __qt_class__ = 'QGrpcInterceptionContext'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def version(self) -> int:
    """
    Calls Qt's 'quint32 QGrpcInterceptionContext::version() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptioncontext.html#version
    """
    #  quint32 QGrpcInterceptionContext::version() const
    return self.uglySide.call(
        'ritual_ZNK24QGrpcInterceptionContext7versionEv',
    )

  def descriptor(self) -> QtGrpc.RpcDescriptor:
    """
    Calls Qt's 'QtGrpc::RpcDescriptor QGrpcInterceptionContext::descriptor()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptioncontext.html#descriptor

    Returns
    -------

    QtGrpc.RpcDescriptor
      A new cute QtGrpc::RpcDescriptor around the copy Qt gave back. Python
      owns it.
    """
    #  QtGrpc::RpcDescriptor QGrpcInterceptionContext::descriptor() const
    address = self.uglySide.call(
        'ritual_ZNK24QGrpcInterceptionContext10descriptorEv',
    )
    return QtGrpc.RpcDescriptor._cuteOwning(address)

  def callOptions(self) -> QGrpcCallOptions:
    """
    Calls Qt's 'const QGrpcCallOptions
    &QGrpcInterceptionContext::callOptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptioncontext.html#callOptions

    Returns
    -------

    QGrpcCallOptions
      A new cute QGrpcCallOptions around the copy Qt gave back. Python owns
      it.
    """
    #  const QGrpcCallOptions &QGrpcInterceptionContext::callOptions() const
    address = self.uglySide.call(
        'ritual_ZNKR24QGrpcInterceptionContext11callOptionsEv',
    )
    from . import QGrpcCallOptions
    return QGrpcCallOptions._cuteOwning(address)

  def operationId(self) -> int:
    """
    Calls Qt's 'quint64 QGrpcInterceptionContext::operationId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcinterceptioncontext.html#operationId
    """
    #  quint64 QGrpcInterceptionContext::operationId() const
    return self.uglySide.call(
        'ritual_ZNK24QGrpcInterceptionContext11operationIdEv',
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
    Qt's 'QGrpcInterceptionContext::QGrpcInterceptionContext(const
    QAbstractGrpcChannel &channel, QGrpcOperationContext &context)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptionContext.__init__' has no cute function yet. Qt's "
        "'QGrpcInterceptionContext::QGrpcInterceptionContext(const "
        "QAbstractGrpcChannel &channel, QGrpcOperationContext &context)': "
        "takes a type Python has no way to hand over yet.")

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
  def channel(*__, **_) -> Never:
    """
    Qt's 'const QAbstractGrpcChannel &QGrpcInterceptionContext::channel()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGrpcInterceptionContext.channel' has no cute function yet. Qt's "
        "'const QAbstractGrpcChannel &QGrpcInterceptionContext::channel() "
        "const': gives a type Python has no way to take yet.")
