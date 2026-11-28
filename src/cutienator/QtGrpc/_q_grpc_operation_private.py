"""
QGrpcOperationPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/6.12.0/QtGrpc/private/qgrpcoperation_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QGrpcOperationPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QGrpcOperation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QGrpcOperation = WAIT['QGrpcOperation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGrpcOperationPrivate(QObjectPrivate):
  """
  The cute side of Qt's QGrpcOperationPrivate: a plain Python object standing
  in front of one C++ QGrpcOperationPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QGrpcOperationPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGrpcOperationPrivate that has a ritual and that
  Python can call so far, 2 names in all: 'q_func', 'get'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QGrpcOperation *QGrpcOperationPrivate::q_func() const': takes
    in Python what 'QGrpcOperation *QGrpcOperationPrivate::q_func()' takes.
  - Qt's 'QGrpcOperationPrivate::~QGrpcOperationPrivate()': the destructor:
    Python never removes a C++ QGrpcOperationPrivate.
  - Qt's 'QGrpcOperationPrivate *QGrpcOperationPrivate::get(QGrpcOperation
    *op)': takes in Python what 'const QGrpcOperationPrivate
    *QGrpcOperationPrivate::get(const QGrpcOperation *op)' takes.
  - Qt's 'void QGrpcOperationPrivate::asyncFinishInvalid(QGrpcStatus
    &&status)': takes a type Python has no way to hand over yet.
  - Qt's 'std::optional<QByteArray>
    QGrpcOperationPrivate::serializeInitialMessage(const QProtobufMessage
    &message)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QGrpcOperationPrivate is created at the first use, not by
    'QGrpcOperationPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGrpcOperationPrivate.
  - Each name of Qt's QGrpcOperationPrivate that has no cute function yet,
    'asyncFinishInvalid', 'serializeInitialMessage', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QGrpcOperationPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum, scoped=True):
    """
    The enum 'QGrpcOperationPrivate::State' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Invalid = Kee[int](0)
    Valid = Kee[int](1)
    Finished = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QGrpcOperation)
  @overload(NoneType)
  def get(op: Optional[QGrpcOperation]) -> Optional[QGrpcOperationPrivate]:
    """
    Calls Qt's 'const QGrpcOperationPrivate *QGrpcOperationPrivate::get(const
    QGrpcOperation *op)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationprivate.html#get

    Parameters
    ----------

    op : Optional[QGrpcOperation]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QGrpcOperationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QGrpcOperationPrivate *QGrpcOperationPrivate::get(const
    #      QGrpcOperation *op)
    address = Rituals.call(
        'ritual_ZN21QGrpcOperationPrivate3getEPK14QGrpcOperation',
        CuteMixin._addressOf(op),
    )
    return QGrpcOperationPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcOperationPrivate'

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

  def q_func(self) -> Optional[QGrpcOperation]:
    """
    Calls Qt's 'QGrpcOperation *QGrpcOperationPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcoperationprivate.html#q_func

    Returns
    -------

    Optional[QGrpcOperation]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QGrpcOperation *QGrpcOperationPrivate::q_func()
    address = self.uglySide.call('ritual_ZN21QGrpcOperationPrivate6q_funcEv')
    from . import QGrpcOperation
    return QGrpcOperation._cuteAt(address)

  @staticmethod
  def asyncFinishInvalid(*__, **_) -> Never:
    """
    Qt's 'void QGrpcOperationPrivate::asyncFinishInvalid(QGrpcStatus
    &&status)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationPrivate.asyncFinishInvalid' has no cute function "
        "yet. Qt's 'void "
        "QGrpcOperationPrivate::asyncFinishInvalid(QGrpcStatus &&status)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def serializeInitialMessage(*__, **_) -> Never:
    """
    Qt's 'std::optional<QByteArray>
    QGrpcOperationPrivate::serializeInitialMessage(const QProtobufMessage
    &message)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcOperationPrivate.serializeInitialMessage' has no cute "
        "function yet. Qt's 'std::optional<QByteArray> "
        "QGrpcOperationPrivate::serializeInitialMessage(const "
        "QProtobufMessage &message)': takes a type Python has no way to "
        "hand over yet.")
