"""
QCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qcalendar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QCalendarSystem, QLocaleFormatType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDate, QDateTime, QLocale, QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QLocale = WAIT['QLocale']
  QTime = WAIT['QTime']


class QCalendar(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCalendar: a plain Python object standing in front of
  one C++ QCalendar.

  C++ hands a QCalendar around as a copy, so every C++ QCalendar behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCalendar that has a ritual and that Python can call
  so far, 23 names in all: 'isValid', 'daysInMonth', 'daysInYear',
  'monthsInYear', 'isDateValid', 'isLeapYear', 'isGregorian', 'isLunar',
  'isLuniSolar', 'isSolar', 'isProleptic', 'hasYearZero',
  'maximumDaysInMonth', 'minimumDaysInMonth', 'maximumMonthsInYear', 'name',
  'dateFromParts', 'dayOfWeek', 'monthName', 'standaloneMonthName',
  'weekDayName', 'standaloneWeekDayName', 'dateTimeToString'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCalendar::QCalendar(SystemId id)': names 'QCalendar::SystemId',
    which has no cute class yet.
  - Qt's 'QDate QCalendar::dateFromParts(const YearMonthDay &parts) const':
    names 'QCalendar::YearMonthDay', which has no cute class yet.
  - Qt's 'QDate QCalendar::matchCenturyToWeekday(const YearMonthDay &parts,
    int dow) const': names 'QCalendar::YearMonthDay', which has no cute class
    yet.
  - Qt's 'YearMonthDay QCalendar::partsFromDate(QDate date) const': gives
    'QCalendar::YearMonthDay', which has no cute class yet.
  - Qt's 'QCalendar::~QCalendar()': the destructor: Python removes its C++
    QCalendar by it, and has no other use for it.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 1 declared and nowhere to be found; 1 a
  template; 1 private; 1 takes or gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QCalendar is created at the first use, not by 'QCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCalendar back gives a copy the ritual made for
    Python, in a new cute QCalendar.
  """

  #  The enums Qt writes inside QCalendar, and the names Qt has for the
  #  combinations of its flags enums.
  System = QCalendarSystem

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCalendar'

  #  Qt's '~QCalendar()'. Naming it makes this a value class: Python owns
  #  every C++ QCalendar behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QCalendarD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isValid
    """
    #  bool QCalendar::isValid() const
    return self.uglySide.call('ritual_ZNK9QCalendar7isValidEv')

  @overload(int)
  @overload(int, int)
  def daysInMonth(self, month: int, year: int = -2147483648) -> int:
    """
    Calls Qt's 'int QCalendar::daysInMonth(int month, int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#daysInMonth

    Parameters
    ----------

    month : int
      Passed on as it is.

    year : int
      Passed on as it is. May be left out, as in Qt: it is then -2147483648.
    """
    #  int QCalendar::daysInMonth(int month, int year) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar11daysInMonthEii', month, year,
    )

  @overload(int)
  def daysInYear(self, year: int) -> int:
    """
    Calls Qt's 'int QCalendar::daysInYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#daysInYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  int QCalendar::daysInYear(int year) const
    return self.uglySide.call('ritual_ZNK9QCalendar10daysInYearEi', year)

  @overload(int)
  def monthsInYear(self, year: int) -> int:
    """
    Calls Qt's 'int QCalendar::monthsInYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#monthsInYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  int QCalendar::monthsInYear(int year) const
    return self.uglySide.call('ritual_ZNK9QCalendar12monthsInYearEi', year)

  @overload(int, int, int)
  def isDateValid(self, year: int, month: int, day: int) -> bool:
    """
    Calls Qt's 'bool QCalendar::isDateValid(int year, int month, int day)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isDateValid

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.

    day : int
      Passed on as it is.
    """
    #  bool QCalendar::isDateValid(int year, int month, int day) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar11isDateValidEiii', year, month, day,
    )

  @overload(int)
  def isLeapYear(self, year: int) -> bool:
    """
    Calls Qt's 'bool QCalendar::isLeapYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QCalendar::isLeapYear(int year) const
    return self.uglySide.call('ritual_ZNK9QCalendar10isLeapYearEi', year)

  def isGregorian(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::isGregorian() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isGregorian
    """
    #  bool QCalendar::isGregorian() const
    return self.uglySide.call('ritual_ZNK9QCalendar11isGregorianEv')

  def isLunar(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::isLunar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isLunar
    """
    #  bool QCalendar::isLunar() const
    return self.uglySide.call('ritual_ZNK9QCalendar7isLunarEv')

  def isLuniSolar(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::isLuniSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isLuniSolar
    """
    #  bool QCalendar::isLuniSolar() const
    return self.uglySide.call('ritual_ZNK9QCalendar11isLuniSolarEv')

  def isSolar(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::isSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isSolar
    """
    #  bool QCalendar::isSolar() const
    return self.uglySide.call('ritual_ZNK9QCalendar7isSolarEv')

  def isProleptic(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::isProleptic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#isProleptic
    """
    #  bool QCalendar::isProleptic() const
    return self.uglySide.call('ritual_ZNK9QCalendar11isProlepticEv')

  def hasYearZero(self) -> bool:
    """
    Calls Qt's 'bool QCalendar::hasYearZero() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#hasYearZero
    """
    #  bool QCalendar::hasYearZero() const
    return self.uglySide.call('ritual_ZNK9QCalendar11hasYearZeroEv')

  def maximumDaysInMonth(self) -> int:
    """
    Calls Qt's 'int QCalendar::maximumDaysInMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#maximumDaysInMonth
    """
    #  int QCalendar::maximumDaysInMonth() const
    return self.uglySide.call('ritual_ZNK9QCalendar18maximumDaysInMonthEv')

  def minimumDaysInMonth(self) -> int:
    """
    Calls Qt's 'int QCalendar::minimumDaysInMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#minimumDaysInMonth
    """
    #  int QCalendar::minimumDaysInMonth() const
    return self.uglySide.call('ritual_ZNK9QCalendar18minimumDaysInMonthEv')

  def maximumMonthsInYear(self) -> int:
    """
    Calls Qt's 'int QCalendar::maximumMonthsInYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#maximumMonthsInYear
    """
    #  int QCalendar::maximumMonthsInYear() const
    return self.uglySide.call('ritual_ZNK9QCalendar19maximumMonthsInYearEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QCalendar::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendar::name() const
    return self.uglySide.call('ritual_ZNK9QCalendar4nameEv')

  @overload(int, int, int)
  def dateFromParts(self, year: int, month: int, day: int) -> QDate:
    """
    Calls Qt's 'QDate QCalendar::dateFromParts(int year, int month, int day)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#dateFromParts

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.

    day : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendar::dateFromParts(int year, int month, int day) const
    address = self.uglySide.call(
        'ritual_ZNK9QCalendar13dateFromPartsEiii', year, month, day,
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(QDate)
  def dayOfWeek(self, date: QDate) -> int:
    """
    Calls Qt's 'int QCalendar::dayOfWeek(QDate date) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#dayOfWeek

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  int QCalendar::dayOfWeek(QDate date) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar9dayOfWeekE5QDate', self._valueOf(date),
    )

  @overload(QLocale, int)
  @overload(QLocale, int, int)
  @overload(QLocale, int, int, QLocaleFormatType)
  def monthName(
      self,
      locale: QLocale,
      month: int,
      year: int = -2147483648,
      format: QLocale.FormatType = QLocaleFormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QCalendar::monthName(const QLocale &locale, int
    month, int year, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#monthName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    month : int
      Passed on as it is.

    year : int
      Passed on as it is. May be left out, as in Qt: it is then -2147483648.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocaleFormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendar::monthName(const QLocale &locale, int month, int
    #      year, QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar9monthNameERK7QLocaleiiNS0_10FormatTypeE',
        self._valueOf(locale), month, year, format.value,
    )

  @overload(QLocale, int)
  @overload(QLocale, int, int)
  @overload(QLocale, int, int, QLocaleFormatType)
  def standaloneMonthName(
      self,
      locale: QLocale,
      month: int,
      year: int = -2147483648,
      format: QLocale.FormatType = QLocaleFormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QCalendar::standaloneMonthName(const QLocale &locale,
    int month, int year, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#standaloneMonthName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    month : int
      Passed on as it is.

    year : int
      Passed on as it is. May be left out, as in Qt: it is then -2147483648.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocaleFormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendar::standaloneMonthName(const QLocale &locale, int
    #      month, int year, QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar19standaloneMonthNameERK7QLocaleiiNS0_10Format'
        'TypeE',
        self._valueOf(locale), month, year, format.value,
    )

  @overload(QLocale, int)
  @overload(QLocale, int, QLocaleFormatType)
  def weekDayName(
      self,
      locale: QLocale,
      day: int,
      format: QLocale.FormatType = QLocaleFormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QCalendar::weekDayName(const QLocale &locale, int
    day, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#weekDayName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    day : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocaleFormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendar::weekDayName(const QLocale &locale, int day,
    #      QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar11weekDayNameERK7QLocaleiNS0_10FormatTypeE',
        self._valueOf(locale), day, format.value,
    )

  @overload(QLocale, int)
  @overload(QLocale, int, QLocaleFormatType)
  def standaloneWeekDayName(
      self,
      locale: QLocale,
      day: int,
      format: QLocale.FormatType = QLocaleFormatType.LongFormat,
  ) -> str:
    """
    Calls Qt's 'QString QCalendar::standaloneWeekDayName(const QLocale
    &locale, int day, QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendar.html#standaloneWeekDayName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    day : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number. May be left out, as in Qt: it is then
      QLocaleFormatType.LongFormat.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendar::standaloneWeekDayName(const QLocale &locale, int
    #      day, QLocale::FormatType format) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar21standaloneWeekDayNameERK7QLocaleiNS0_10Forma'
        'tTypeE',
        self._valueOf(locale), day, format.value,
    )

  @overload(str, QDateTime, QDate, QTime, QLocale)
  def dateTimeToString(
      self,
      format: str,
      datetime: QDateTime,
      dateOnly: QDate,
      timeOnly: QTime,
      locale: QLocale,
  ) -> str:
    """
    Calls Qt's 'QString QCalendar::dateTimeToString(QStringView format, const
    QDateTime &datetime, QDate dateOnly, QTime timeOnly, const QLocale
    &locale) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#dateTimeToString

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    datetime : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    dateOnly : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    timeOnly : QTime
      Passed on as a value: Qt reads the C++ QTime, which stays Python's own.

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendar::dateTimeToString(QStringView format, const
    #      QDateTime &datetime, QDate dateOnly, QTime timeOnly, const QLocale
    #      &locale) const
    return self.uglySide.call(
        'ritual_ZNK9QCalendar16dateTimeToStringE11QStringViewRK9QDateTime5Q'
        'Date5QTimeRK7QLocale',
        format, self._valueOf(datetime), self._valueOf(dateOnly),
        self._valueOf(timeOnly), self._valueOf(locale),
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QCalendar::QCalendar()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#QCalendar
    """
    #  QCalendar::QCalendar()
    self._noteCreation(QCalendar, lambda: Rituals.call(
        'ritual_ZN9QCalendarC1Ev',
    ))

  @overload(System)
  def __init__(self, system: System) -> None:
    """
    Notes what was given, for Qt's 'QCalendar::QCalendar(System system)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#QCalendar

    Parameters
    ----------

    system : System
      Passed on as its number.
    """
    #  QCalendar::QCalendar(System system)
    self._noteCreation(QCalendar, lambda: Rituals.call(
        'ritual_ZN9QCalendarC1ENS_6SystemE', system.value,
    ))

  @overload(str)
  def __init__(self, name: str) -> None:
    """
    Notes what was given, for Qt's 'QCalendar::QCalendar(QAnyStringView
    name)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#QCalendar

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QCalendar::QCalendar(QAnyStringView name)
    self._noteCreation(QCalendar, lambda: Rituals.call(
        'ritual_ZN9QCalendarC1E14QAnyStringView', name,
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
