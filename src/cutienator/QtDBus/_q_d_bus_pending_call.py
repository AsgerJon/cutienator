"""
QDBusPendingCall binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbuspendingcall.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDBusError, QDBusMessage, QDBusPendingCallPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusError = WAIT['QDBusError']
  QDBusMessage = WAIT['QDBusMessage']
  QDBusPendingCallPrivate = WAIT['QDBusPendingCallPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDBusPendingCall(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusPendingCall: a plain Python object standing in
  front of one C++ QDBusPendingCall.

  C++ hands a QDBusPendingCall around as a copy, so every C++
  QDBusPendingCall behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusPendingCall that has a ritual and that Python
  can call so far, 8 names in all: 'isFinished', 'waitForFinished',
  'isError', 'isValid', 'error', 'reply', 'fromError', 'fromCompletedCall'.
  It can be made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusPendingCall::QDBusPendingCall(QDBusPendingCall &&other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QDBusPendingCall::~QDBusPendingCall()': the destructor: Python
    removes its C++ QDBusPendingCall by it, and has no other use for it.
  - Qt's 'QDBusPendingCall &QDBusPendingCall::operator=(QDBusPendingCall
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusPendingCall &QDBusPendingCall::operator=(const
    QDBusPendingCall &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'void QDBusPendingCall::swap(QDBusPendingCall &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDBusPendingCall is created at the first use, not by
    'QDBusPendingCall(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusPendingCall back gives a copy the ritual made
    for Python, in a new cute QDBusPendingCall.
  - Each name of Qt's QDBusPendingCall that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QDBusError)
  def fromError(error: QDBusError) -> QDBusPendingCall:
    """
    Calls Qt's 'QDBusPendingCall QDBusPendingCall::fromError(const QDBusError
    &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcall.html#fromError

    Parameters
    ----------

    error : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.

    Returns
    -------

    QDBusPendingCall
      A new cute QDBusPendingCall around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusPendingCall QDBusPendingCall::fromError(const QDBusError &error)
    address = Rituals.call(
        'ritual_ZN16QDBusPendingCall9fromErrorERK10QDBusError',
        CuteMixin._valueOf(error),
    )
    return QDBusPendingCall._cuteOwning(address)

  @staticmethod
  @overload(QDBusMessage)
  def fromCompletedCall(message: QDBusMessage) -> QDBusPendingCall:
    """
    Calls Qt's 'QDBusPendingCall QDBusPendingCall::fromCompletedCall(const
    QDBusMessage &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcall.html#fromCompletedCall

    Parameters
    ----------

    message : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.

    Returns
    -------

    QDBusPendingCall
      A new cute QDBusPendingCall around the copy Qt gave back. Python owns
      it.
    """
    #  QDBusPendingCall QDBusPendingCall::fromCompletedCall(const
    #      QDBusMessage &message)
    address = Rituals.call(
        'ritual_ZN16QDBusPendingCall17fromCompletedCallERK12QDBusMessage',
        CuteMixin._valueOf(message),
    )
    return QDBusPendingCall._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusPendingCall'

  #  Qt's '~QDBusPendingCall()'. Naming it makes this a value class: Python
  #  owns every C++ QDBusPendingCall behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QDBusPendingCallD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QDBusPendingCall::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcall.html#isFinished
    """
    #  bool QDBusPendingCall::isFinished() const
    return self._callAs(
        'QDBusPendingCall', 'ritual_ZNK16QDBusPendingCall10isFinishedEv',
    )

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QDBusPendingCall::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcall.html#isError
    """
    #  bool QDBusPendingCall::isError() const
    return self._callAs(
        'QDBusPendingCall', 'ritual_ZNK16QDBusPendingCall7isErrorEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDBusPendingCall::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcall.html#isValid
    """
    #  bool QDBusPendingCall::isValid() const
    return self._callAs(
        'QDBusPendingCall', 'ritual_ZNK16QDBusPendingCall7isValidEv',
    )

  def error(self) -> QDBusError:
    """
    Calls Qt's 'QDBusError QDBusPendingCall::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcall.html#error

    Returns
    -------

    QDBusError
      A new cute QDBusError around the copy Qt gave back. Python owns it.
    """
    #  QDBusError QDBusPendingCall::error() const
    address = self._callAs(
        'QDBusPendingCall', 'ritual_ZNK16QDBusPendingCall5errorEv',
    )
    from . import QDBusError
    return QDBusError._cuteOwning(address)

  def reply(self) -> QDBusMessage:
    """
    Calls Qt's 'QDBusMessage QDBusPendingCall::reply() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuspendingcall.html#reply

    Returns
    -------

    QDBusMessage
      A new cute QDBusMessage around the copy Qt gave back. Python owns it.
    """
    #  QDBusMessage QDBusPendingCall::reply() const
    address = self._callAs(
        'QDBusPendingCall', 'ritual_ZNK16QDBusPendingCall5replyEv',
    )
    from . import QDBusMessage
    return QDBusMessage._cuteOwning(address)

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

  @overload(THIS)
  def __init__(self, other: QDBusPendingCall) -> None:
    """
    Notes what was given, for Qt's 'QDBusPendingCall::QDBusPendingCall(const
    QDBusPendingCall &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcall.html#QDBusPendingCall

    Parameters
    ----------

    other : QDBusPendingCall
      Passed on as a value: Qt reads the C++ QDBusPendingCall, which stays
      Python's own.
    """
    #  QDBusPendingCall::QDBusPendingCall(const QDBusPendingCall &other)
    self._noteCreation(QDBusPendingCall, lambda: Rituals.call(
        'ritual_ZN16QDBusPendingCallC1ERKS_',
        self._valueOf(other, 'QDBusPendingCall'),
    ))

  @overload(QDBusPendingCallPrivate)
  @overload(NoneType)
  def __init__(self, dd: Optional[QDBusPendingCallPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QDBusPendingCall::QDBusPendingCall(QDBusPendingCallPrivate *dd)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcall.html#QDBusPendingCall

    Parameters
    ----------

    dd : Optional[QDBusPendingCallPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDBusPendingCall::QDBusPendingCall(QDBusPendingCallPrivate *dd)
    self._noteCreation(QDBusPendingCall, lambda: Rituals.call(
        'ritual_ZN16QDBusPendingCallC1EP23QDBusPendingCallPrivate',
        self._addressOf(dd),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDBusPendingCall::QDBusPendingCall()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcall.html#QDBusPendingCall
    """
    #  QDBusPendingCall::QDBusPendingCall()
    self._noteCreation(QDBusPendingCall, lambda: Rituals.call(
        'ritual_ZN16QDBusPendingCallC1Ev',
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

  def waitForFinished(self) -> None:
    """
    Calls Qt's 'void QDBusPendingCall::waitForFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdbuspendingcall.html#waitForFinished
    """
    #  void QDBusPendingCall::waitForFinished()
    self._callAs(
        'QDBusPendingCall', 'ritual_ZN16QDBusPendingCall15waitForFinishedEv',
    )

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QDBusPendingCall::swap(QDBusPendingCall &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusPendingCall.swap' has no cute function yet. Qt's 'void "
        "QDBusPendingCall::swap(QDBusPendingCall &other)': takes a type "
        "Python has no way to hand over yet.")
