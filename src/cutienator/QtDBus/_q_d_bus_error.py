"""
QDBusError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDBus/qdbuserror.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QDBusMessage
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDBusMessage = WAIT['QDBusMessage']


class QDBusError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDBusError: a plain Python object standing in front
  of one C++ QDBusError.

  C++ hands a QDBusError around as a copy, so every C++ QDBusError behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDBusError that has a ritual and that Python can
  call so far, 5 names in all: 'type', 'name', 'message', 'isValid',
  'errorString'. It can be made from Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDBusError::QDBusError(const DBusError *error)': names 'DBusError',
    which has no cute class yet.
  - Qt's 'QDBusError::QDBusError(QDBusError &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QDBusError &QDBusError::operator=(QDBusError &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QDBusError &QDBusError::operator=(const QDBusError &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QDBusError &QDBusError::operator=(const QDBusMessage &msg)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QDBusError::swap(QDBusError &other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QDBusError::~QDBusError()': the destructor: Python removes its C++
    QDBusError by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QDBusError is created at the first use, not by 'QDBusError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDBusError back gives a copy the ritual made for
    Python, in a new cute QDBusError.
  - Each name of Qt's QDBusError that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDBusError, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ErrorType(CuteNum):
    """
    The enum 'QDBusError::ErrorType' of Qt, with the 29 names Qt gives in it.
    """

    NoError = Kee[int](0)
    Other = Kee[int](1)
    Failed = Kee[int](2)
    NoMemory = Kee[int](3)
    ServiceUnknown = Kee[int](4)
    NoReply = Kee[int](5)
    BadAddress = Kee[int](6)
    NotSupported = Kee[int](7)
    LimitsExceeded = Kee[int](8)
    AccessDenied = Kee[int](9)
    NoServer = Kee[int](10)
    Timeout = Kee[int](11)
    NoNetwork = Kee[int](12)
    AddressInUse = Kee[int](13)
    Disconnected = Kee[int](14)
    InvalidArgs = Kee[int](15)
    UnknownMethod = Kee[int](16)
    TimedOut = Kee[int](17)
    InvalidSignature = Kee[int](18)
    UnknownInterface = Kee[int](19)
    UnknownObject = Kee[int](20)
    UnknownProperty = Kee[int](21)
    PropertyReadOnly = Kee[int](22)
    InternalError = Kee[int](23)
    InvalidService = Kee[int](24)
    InvalidObjectPath = Kee[int](25)
    InvalidInterface = Kee[int](26)
    InvalidMember = Kee[int](27)
    LastErrorType = Kee[int](27)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(ErrorType)
  def errorString(error: ErrorType) -> str:
    """
    Calls Qt's 'QString QDBusError::errorString(ErrorType error)'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#errorString

    Parameters
    ----------

    error : ErrorType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusError::errorString(ErrorType error)
    return Rituals.call(
        'ritual_ZN10QDBusError11errorStringENS_9ErrorTypeE', error.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDBusError'

  #  Qt's '~QDBusError()'. Naming it makes this a value class: Python owns
  #  every C++ QDBusError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QDBusErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> ErrorType:
    """
    Calls Qt's 'ErrorType QDBusError::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#type

    Returns
    -------

    ErrorType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorType(number)' gives.
    """
    #  ErrorType QDBusError::type() const
    return QDBusError.ErrorType(self.uglySide.call(
        'ritual_ZNK10QDBusError4typeEv',
    ))

  def name(self) -> str:
    """
    Calls Qt's 'QString QDBusError::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusError::name() const
    return self.uglySide.call('ritual_ZNK10QDBusError4nameEv')

  def message(self) -> str:
    """
    Calls Qt's 'QString QDBusError::message() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#message

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDBusError::message() const
    return self.uglySide.call('ritual_ZNK10QDBusError7messageEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDBusError::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#isValid
    """
    #  bool QDBusError::isValid() const
    return self.uglySide.call('ritual_ZNK10QDBusError7isValidEv')

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDBusError::QDBusError()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#QDBusError
    """
    #  QDBusError::QDBusError()
    self._noteCreation(QDBusError, lambda: Rituals.call(
        'ritual_ZN10QDBusErrorC1Ev',
    ))

  @overload(QDBusMessage)
  def __init__(self, msg: QDBusMessage) -> None:
    """
    Notes what was given, for Qt's 'QDBusError::QDBusError(const QDBusMessage
    &msg)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#QDBusError

    Parameters
    ----------

    msg : QDBusMessage
      Passed on as a value: Qt reads the C++ QDBusMessage, which stays
      Python's own.
    """
    #  QDBusError::QDBusError(const QDBusMessage &msg)
    self._noteCreation(QDBusError, lambda: Rituals.call(
        'ritual_ZN10QDBusErrorC1ERK12QDBusMessage', self._valueOf(msg),
    ))

  @overload(ErrorType, str)
  def __init__(self, error: ErrorType, message: str) -> None:
    """
    Notes what was given, for Qt's 'QDBusError::QDBusError(ErrorType error,
    const QString &message)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#QDBusError

    Parameters
    ----------

    error : ErrorType
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QDBusError::QDBusError(ErrorType error, const QString &message)
    self._noteCreation(QDBusError, lambda: Rituals.call(
        'ritual_ZN10QDBusErrorC1ENS_9ErrorTypeERK7QString',
        error.value, message,
    ))

  @overload(THIS)
  def __init__(self, other: QDBusError) -> None:
    """
    Notes what was given, for Qt's 'QDBusError::QDBusError(const QDBusError
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdbuserror.html#QDBusError

    Parameters
    ----------

    other : QDBusError
      Passed on as a value: Qt reads the C++ QDBusError, which stays Python's
      own.
    """
    #  QDBusError::QDBusError(const QDBusError &other)
    self._noteCreation(QDBusError, lambda: Rituals.call(
        'ritual_ZN10QDBusErrorC1ERKS_', self._valueOf(other),
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
    Qt's 'void QDBusError::swap(QDBusError &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDBusError.swap' has no cute function yet. Qt's 'void "
        "QDBusError::swap(QDBusError &other)': takes a type Python has no "
        "way to hand over yet.")
