"""
QSqlError binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSql/qsqlerror.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSqlError(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSqlError: a plain Python object standing in front of
  one C++ QSqlError.

  C++ hands a QSqlError around as a copy, so every C++ QSqlError behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSqlError that has a ritual and that Python can call
  so far, 8 names in all: '__eq__', '__ne__', 'driverText', 'databaseText',
  'type', 'nativeErrorCode', 'text', 'isValid'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSqlError::QSqlError(QSqlError &&other)': takes a type Python has
    no way to hand over yet.
  - Qt's 'QSqlError &QSqlError::operator=(const QSqlError &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QSqlError &QSqlError::operator=(QSqlError &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QSqlError::~QSqlError()': the destructor: Python removes its C++
    QSqlError by it, and has no other use for it.
  - Qt's 'void QSqlError::swap(QSqlError &other)': takes a type Python has no
    way to hand over yet.

  What to expect
  --------------

  - The C++ QSqlError is created at the first use, not by 'QSqlError(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSqlError back gives a copy the ritual made for
    Python, in a new cute QSqlError.
  - Each name of Qt's QSqlError that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QSqlError, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ErrorType(CuteNum):
    """
    The enum 'QSqlError::ErrorType' of Qt, with the 5 names Qt gives in it.
    """

    NoError = Kee[int](0)
    ConnectionError = Kee[int](1)
    StatementError = Kee[int](2)
    TransactionError = Kee[int](3)
    UnknownError = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSqlError'

  #  Qt's '~QSqlError()'. Naming it makes this a value class: Python owns
  #  every C++ QSqlError behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QSqlErrorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def driverText(self) -> str:
    """
    Calls Qt's 'QString QSqlError::driverText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#driverText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlError::driverText() const
    return self.uglySide.call('ritual_ZNK9QSqlError10driverTextEv')

  def databaseText(self) -> str:
    """
    Calls Qt's 'QString QSqlError::databaseText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#databaseText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlError::databaseText() const
    return self.uglySide.call('ritual_ZNK9QSqlError12databaseTextEv')

  def type(self) -> ErrorType:
    """
    Calls Qt's 'ErrorType QSqlError::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#type

    Returns
    -------

    ErrorType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorType(number)' gives.
    """
    #  ErrorType QSqlError::type() const
    return QSqlError.ErrorType(self.uglySide.call(
        'ritual_ZNK9QSqlError4typeEv',
    ))

  def nativeErrorCode(self) -> str:
    """
    Calls Qt's 'QString QSqlError::nativeErrorCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#nativeErrorCode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlError::nativeErrorCode() const
    return self.uglySide.call('ritual_ZNK9QSqlError15nativeErrorCodeEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QSqlError::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSqlError::text() const
    return self.uglySide.call('ritual_ZNK9QSqlError4textEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QSqlError::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#isValid
    """
    #  bool QSqlError::isValid() const
    return self.uglySide.call('ritual_ZNK9QSqlError7isValidEv')

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
  def __eq__(self, other: QSqlError) -> bool:
    """
    Calls Qt's 'bool QSqlError::operator==(const QSqlError &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#operator==

    Parameters
    ----------

    other : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  bool QSqlError::operator==(const QSqlError &other) const
    return self.uglySide.call(
        'ritual_ZNK9QSqlErroreqERKS_', self._valueOf(other),
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
  def __ne__(self, other: QSqlError) -> bool:
    """
    Calls Qt's 'bool QSqlError::operator!=(const QSqlError &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#operator!=

    Parameters
    ----------

    other : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  bool QSqlError::operator!=(const QSqlError &other) const
    return self.uglySide.call(
        'ritual_ZNK9QSqlErrorneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(str)
  @overload(str, str)
  @overload(str, str, ErrorType)
  @overload(str, str, ErrorType, str)
  def __init__(
      self,
      driverText: str = '',
      databaseText: str = '',
      type: ErrorType = ErrorType.NoError,
      nativeErrorCode: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's 'QSqlError::QSqlError(const QString
    &driverText, const QString &databaseText, ErrorType type, const QString
    &nativeErrorCode)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#QSqlError

    Parameters
    ----------

    driverText : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    databaseText : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    type : ErrorType
      Passed on as its number. May be left out, as in Qt: it is then
      ErrorType.NoError.

    nativeErrorCode : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  QSqlError::QSqlError(const QString &driverText, const QString
    #      &databaseText, ErrorType type, const QString &nativeErrorCode)
    self._noteCreation(QSqlError, lambda: Rituals.call(
        'ritual_ZN9QSqlErrorC1ERK7QStringS2_NS_9ErrorTypeES2_',
        driverText, databaseText, type.value, nativeErrorCode,
    ))

  @overload(THIS)
  def __init__(self, other: QSqlError) -> None:
    """
    Notes what was given, for Qt's 'QSqlError::QSqlError(const QSqlError
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsqlerror.html#QSqlError

    Parameters
    ----------

    other : QSqlError
      Passed on as a value: Qt reads the C++ QSqlError, which stays Python's
      own.
    """
    #  QSqlError::QSqlError(const QSqlError &other)
    self._noteCreation(QSqlError, lambda: Rituals.call(
        'ritual_ZN9QSqlErrorC1ERKS_', self._valueOf(other),
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
    Qt's 'void QSqlError::swap(QSqlError &other)': takes a type Python has no
    way to hand over yet.
    """
    raise NotImplementedError(
        "'QSqlError.swap' has no cute function yet. Qt's 'void "
        "QSqlError::swap(QSqlError &other)': takes a type Python has no way "
        "to hand over yet.")
