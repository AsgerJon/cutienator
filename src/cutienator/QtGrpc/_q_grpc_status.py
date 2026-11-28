"""
QGrpcStatus binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpc/qgrpcstatus.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QGrpcStatus(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QGrpcStatus: a plain Python object standing in front
  of one C++ QGrpcStatus.

  C++ hands a QGrpcStatus around as a copy, so every C++ QGrpcStatus behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QGrpcStatus that has a ritual and that Python can
  call so far, 6 names in all: 'code', 'isOk', 'message', '__eq__', '__ne__',
  '__rlshift__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QGrpcStatus::~QGrpcStatus()': the destructor: Python removes its
    C++ QGrpcStatus by it, and has no other use for it.
  - Qt's 'QGrpcStatus &QGrpcStatus::operator=(const QGrpcStatus &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QGrpcStatus::QGrpcStatus(QGrpcStatus &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QGrpcStatus &QGrpcStatus::operator=(QGrpcStatus &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QGrpcStatus::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'void QGrpcStatus::swap(QGrpcStatus &other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'bool operator==(const QGrpcStatus &lhs, const QtGrpc::StatusCode
    &rhs)': takes a type Python has no way to hand over yet.
  - Qt's 'bool operator!=(const QGrpcStatus &lhs, const QtGrpc::StatusCode
    &rhs)': takes a type Python has no way to hand over yet.
  - Qt's 'bool operator==(const QtGrpc::StatusCode &lhs, const QGrpcStatus
    &rhs)': takes a type Python has no way to hand over yet.
  - Qt's 'bool operator!=(const QtGrpc::StatusCode &lhs, const QGrpcStatus
    &rhs)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator<<(QDataStream &out, const QGrpcStatus
    &status)': takes a type Python has no way to hand over yet.
  - Qt's 'QDataStream &operator>>(QDataStream &in, QGrpcStatus &status)': an
    operator between other classes, written inside this one.

  What has no ritual
  ------------------

  4 of the 24 functions Qt declares: 4 not a gap.

  What to expect
  --------------

  - The C++ QGrpcStatus is created at the first use, not by
    'QGrpcStatus(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QGrpcStatus back gives a copy the ritual made for
    Python, in a new cute QGrpcStatus.
  - Each name of Qt's QGrpcStatus that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGrpcStatus'

  #  Qt's '~QGrpcStatus()'. Naming it makes this a value class: Python owns
  #  every C++ QGrpcStatus behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QGrpcStatusD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def code(self) -> QtGrpc.StatusCode:
    """
    Calls Qt's 'QtGrpc::StatusCode QGrpcStatus::code() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#code

    Returns
    -------

    QtGrpc.StatusCode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGrpc.StatusCode(number)' gives.
    """
    #  QtGrpc::StatusCode QGrpcStatus::code() const
    return QtGrpc.StatusCode(self.uglySide.call(
        'ritual_ZNK11QGrpcStatus4codeEv',
    ))

  def isOk(self) -> bool:
    """
    Calls Qt's 'bool QGrpcStatus::isOk() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#isOk
    """
    #  bool QGrpcStatus::isOk() const
    return self.uglySide.call('ritual_ZNK11QGrpcStatus4isOkEv')

  def message(self) -> str:
    """
    Calls Qt's 'const QString &QGrpcStatus::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QGrpcStatus::message() const
    return self.uglySide.call('ritual_ZNKR11QGrpcStatus7messageEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QGrpcStatus) -> bool:
    """
    Calls Qt's 'bool operator==(const QGrpcStatus &lhs, const QGrpcStatus
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#operator==

    Parameters
    ----------

    rhs : QGrpcStatus
      Passed on as a value: Qt reads the C++ QGrpcStatus, which stays
      Python's own.
    """
    #  bool operator==(const QGrpcStatus &lhs, const QGrpcStatus &rhs)
    return Rituals.call(
        'ritual_ZeqRK11QGrpcStatusS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QGrpcStatus) -> bool:
    """
    Calls Qt's 'bool operator!=(const QGrpcStatus &lhs, const QGrpcStatus
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#operator!=

    Parameters
    ----------

    rhs : QGrpcStatus
      Passed on as a value: Qt reads the C++ QGrpcStatus, which stays
      Python's own.
    """
    #  bool operator!=(const QGrpcStatus &lhs, const QGrpcStatus &rhs)
    return Rituals.call(
        'ritual_ZneRK11QGrpcStatusS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(QDebug)
  def __rlshift__(self, debug: QDebug) -> QDebug:
    """
    Calls Qt's 'QDebug operator<<(QDebug debug, const QGrpcStatus &status)'.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#operator<<

    Parameters
    ----------

    debug : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug operator<<(QDebug debug, const QGrpcStatus &status)
    address = Rituals.call(
        'ritual_Zls6QDebugRK11QGrpcStatus',
        CuteMixin._valueOf(debug), CuteMixin._valueOf(self),
    )
    from ..QtCore import QDebug
    return QDebug._cuteOwning(address)

  @overload.fallback
  def __rlshift__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QtGrpc.StatusCode)
  @overload(QtGrpc.StatusCode, str)
  def __init__(self, code: QtGrpc.StatusCode, message: str = '') -> None:
    """
    Notes what was given, for Qt's
    'QGrpcStatus::QGrpcStatus(QtGrpc::StatusCode code, QAnyStringView
    message)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#QGrpcStatus

    Parameters
    ----------

    code : QtGrpc.StatusCode
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QGrpcStatus::QGrpcStatus(QtGrpc::StatusCode code, QAnyStringView
    #      message)
    self._noteCreation(QGrpcStatus, lambda: Rituals.call(
        'ritual_ZN11QGrpcStatusC1EN6QtGrpc10StatusCodeE14QAnyStringView',
        code.value, message,
    ))

  @overload(THIS)
  def __init__(self, other: QGrpcStatus) -> None:
    """
    Notes what was given, for Qt's 'QGrpcStatus::QGrpcStatus(const
    QGrpcStatus &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qgrpcstatus.html#QGrpcStatus

    Parameters
    ----------

    other : QGrpcStatus
      Passed on as a value: Qt reads the C++ QGrpcStatus, which stays
      Python's own.
    """
    #  QGrpcStatus::QGrpcStatus(const QGrpcStatus &other)
    self._noteCreation(QGrpcStatus, lambda: Rituals.call(
        'ritual_ZN11QGrpcStatusC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QGrpcStatus::swap(QGrpcStatus &other)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QGrpcStatus.swap' has no cute function yet. Qt's 'void "
        "QGrpcStatus::swap(QGrpcStatus &other)': takes a type Python has no "
        "way to hand over yet.")
