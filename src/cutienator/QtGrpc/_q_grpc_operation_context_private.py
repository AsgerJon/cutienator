"""
QGrpcOperationContextPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/6.12.0/QtGrpc/private/qgrpcoperationcontext_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGrpcOperationContextPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGrpcOperationContext


class QGrpcOperationContextPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGrpcOperationContextPrivate: a plain Python object
  standing in front of one C++ QGrpcOperationContextPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's
  QGrpcOperationContextPrivate is built on Qt's QObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcOperationContextPrivate that has a ritual and
  that Python can call so far, 1 name in all: 'q_func'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGrpcOperationContext *QGrpcOperationContextPrivate::q_func()
    const': takes in Python what 'QGrpcOperationContext
    *QGrpcOperationContextPrivate::q_func()' takes.
  - Qt's 'QGrpcOperationContextPrivate::QGrpcOperationContextPrivate(QtGrpc::
    RpcDescriptor &&descriptor_, QGrpcCallOptions options_,
    std::shared_ptr<QAbstractProtobufSerializer> &&serializer_, quint64
    operationId_)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGrpcOperationContextPrivate is created at the first use, not by
    'QGrpcOperationContextPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcOperationContextPrivate.
  - Each name of Qt's QGrpcOperationContextPrivate that has no cute function
    yet, '__init__', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcOperationContextPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Qt's 'QGrpcOperationContextPrivate::QGrpcOperationContextPrivate(QtGrpc::
    RpcDescriptor &&descriptor_, QGrpcCallOptions options_,
    std::shared_ptr<QAbstractProtobufSerializer> &&serializer_, quint64
    operationId_)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationContextPrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QGrpcOperationContextPrivate::QGrpcOperationContextPrivate(QtGrpc:"
        ":RpcDescriptor &&descriptor_, QGrpcCallOptions options_, "
        "std::shared_ptr<QAbstractProtobufSerializer> &&serializer_, "
        "quint64 operationId_)': takes a type Python has no way to hand "
        "over yet.")

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

  def q_func(self) -> Optional[QGrpcOperationContext]:
    """
    Calls Qt's 'QGrpcOperationContext
    *QGrpcOperationContextPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgrpcoperationcontextprivate.html#q_func

    Returns
    -------

    Optional[QGrpcOperationContext]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGrpcOperationContext *QGrpcOperationContextPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QGrpcOperationContextPrivate6q_funcEv',
    )
    from . import QGrpcOperationContext
    return QGrpcOperationContext._cuteAt(address)
