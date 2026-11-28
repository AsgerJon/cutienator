"""
QCalendarBackend binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcalendarbackend_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCalendarBackend to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QCalendar, QLocale, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QCalendarLocale, QDate, QDateTime, QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
  QTime = WAIT['QTime']


class QCalendarBackend(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCalendarBackend: a plain Python object standing in
  front of one C++ QCalendarBackend.

  What exists
  -----------

  Every function of Qt's QCalendarBackend that has a ritual and that Python
  can call so far, 34 names in all: 'name', 'names', 'calendarSystem',
  'calendarId', 'daysInMonth', 'daysInYear', 'monthsInYear', 'isDateValid',
  'isLeapYear', 'isLunar', 'isLuniSolar', 'isSolar', 'isProleptic',
  'hasYearZero', 'maximumDaysInMonth', 'minimumDaysInMonth',
  'maximumMonthsInYear', 'julianDayToDate', 'dayOfWeek',
  'matchCenturyToWeekday', 'monthName', 'standaloneMonthName', 'weekDayName',
  'standaloneWeekDayName', 'dateTimeToString', 'isGregorian',
  'registerCustomBackend', 'availableCalendars', 'localeMonthIndexData',
  'setIndex', 'fromName', 'fromId', 'fromEnum', 'gregorian'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCalendarBackend::~QCalendarBackend()': the destructor: Python
    never removes a C++ QCalendarBackend.
  - Qt's 'bool QCalendarBackend::dateToJulianDay(int year, int month, int
    day, qint64 *jd) const': takes a number to change where it is.
  - Qt's 'const char16_t *QCalendarBackend::localeMonthData() const': gives
    'unsigned short', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 42 functions Qt declares: 4 forbidden; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QCalendarBackend is created at the first use, not by
    'QCalendarBackend(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCalendarBackend.
  - Each name of Qt's QCalendarBackend that has no cute function yet,
    '__init__', 'dateToJulianDay', 'localeMonthData', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def availableCalendars() -> QStringList:
    """
    Calls Qt's 'QStringList QCalendarBackend::availableCalendars()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#availableCalendars

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCalendarBackend::availableCalendars()
    address = Rituals.call(
        'ritual_ZN16QCalendarBackend18availableCalendarsEv',
    )
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(str)
  def fromName(name: str) -> Optional[QCalendarBackend]:
    """
    Calls Qt's 'const QCalendarBackend
    *QCalendarBackend::fromName(QAnyStringView name)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#fromName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QCalendarBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarBackend *QCalendarBackend::fromName(QAnyStringView
    #      name)
    address = Rituals.call(
        'ritual_ZN16QCalendarBackend8fromNameE14QAnyStringView', name,
    )
    return QCalendarBackend._cuteAt(address)

  @staticmethod
  @overload(QCalendar.SystemId)
  def fromId(id: QCalendar.SystemId) -> Optional[QCalendarBackend]:
    """
    Calls Qt's 'const QCalendarBackend
    *QCalendarBackend::fromId(QCalendar::SystemId id)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#fromId

    Parameters
    ----------

    id : QCalendar.SystemId
      Passed on as a value: Qt reads the C++ QCalendar::SystemId, which stays
      Python's own.

    Returns
    -------

    Optional[QCalendarBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarBackend *QCalendarBackend::fromId(QCalendar::SystemId
    #      id)
    address = Rituals.call(
        'ritual_ZN16QCalendarBackend6fromIdEN9QCalendar8SystemIdE',
        CuteMixin._valueOf(id),
    )
    return QCalendarBackend._cuteAt(address)

  @staticmethod
  @overload(QCalendar.System)
  def fromEnum(system: QCalendar.System) -> Optional[QCalendarBackend]:
    """
    Calls Qt's 'const QCalendarBackend
    *QCalendarBackend::fromEnum(QCalendar::System system)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#fromEnum

    Parameters
    ----------

    system : QCalendar.System
      Passed on as its number.

    Returns
    -------

    Optional[QCalendarBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarBackend *QCalendarBackend::fromEnum(QCalendar::System
    #      system)
    address = Rituals.call(
        'ritual_ZN16QCalendarBackend8fromEnumEN9QCalendar6SystemE',
        system.value,
    )
    return QCalendarBackend._cuteAt(address)

  @staticmethod
  def gregorian() -> Optional[QCalendarBackend]:
    """
    Calls Qt's 'const QCalendarBackend *QCalendarBackend::gregorian()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#gregorian

    Returns
    -------

    Optional[QCalendarBackend]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarBackend *QCalendarBackend::gregorian()
    address = Rituals.call('ritual_ZN16QCalendarBackend9gregorianEv')
    return QCalendarBackend._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCalendarBackend'

  #  A C++ QCalendarBackend Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCalendarBackend'

  #  The functions Qt calls itself that QCalendarBackend is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dateToJulianDay': (
          'bool QCalendarBackend::dateToJulianDay(int, int, int, qint64 *) '
          'const',
      ),
      'dateTimeToString': (
          'QString QCalendarBackend::dateTimeToString(QStringView, const '
          'QDateTime &, QDate, QTime, const QLocale &) const',
      ),
      'localeMonthData': (
          'const char16_t *QCalendarBackend::localeMonthData() const',
      ),
  }

  #  The functions Qt calls itself that QCalendarBackend is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'name': (
          ('_ZNK16QCalendarBackend4nameEv',
           ('address', 'text', ''),
           ()),
      ),
      'daysInMonth': (
          ('_ZNK16QCalendarBackend11daysInMonthEii',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'daysInYear': (
          ('_ZNK16QCalendarBackend10daysInYearEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'monthsInYear': (
          ('_ZNK16QCalendarBackend12monthsInYearEi',
           ('int', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isDateValid': (
          ('_ZNK16QCalendarBackend11isDateValidEiii',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'isLeapYear': (
          ('_ZNK16QCalendarBackend10isLeapYearEi',
           ('bool', 'number', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'isLunar': (
          ('_ZNK16QCalendarBackend7isLunarEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isLuniSolar': (
          ('_ZNK16QCalendarBackend11isLuniSolarEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isSolar': (
          ('_ZNK16QCalendarBackend7isSolarEv',
           ('bool', 'number', ''),
           ()),
      ),
      'isProleptic': (
          ('_ZNK16QCalendarBackend11isProlepticEv',
           ('bool', 'number', ''),
           ()),
      ),
      'hasYearZero': (
          ('_ZNK16QCalendarBackend11hasYearZeroEv',
           ('bool', 'number', ''),
           ()),
      ),
      'maximumDaysInMonth': (
          ('_ZNK16QCalendarBackend18maximumDaysInMonthEv',
           ('int', 'number', ''),
           ()),
      ),
      'minimumDaysInMonth': (
          ('_ZNK16QCalendarBackend18minimumDaysInMonthEv',
           ('int', 'number', ''),
           ()),
      ),
      'maximumMonthsInYear': (
          ('_ZNK16QCalendarBackend19maximumMonthsInYearEv',
           ('int', 'number', ''),
           ()),
      ),
      'julianDayToDate': (
          ('_ZNK16QCalendarBackend15julianDayToDateEx',
           ('address', 'value', 'QtCore:QCalendar.YearMonthDay'),
           (
               ('long long', 'number', ''),
           )),
      ),
      'dayOfWeek': (
          ('_ZNK16QCalendarBackend9dayOfWeekEx',
           ('int', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'matchCenturyToWeekday': (
          ('_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar12Ye'
           'arMonthDayEi',
           ('long long', 'number', ''),
           (
               ('address', 'value', 'QtCore:QCalendar.YearMonthDay'),
               ('int', 'number', ''),
           )),
      ),
      'monthName': (
          ('_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTypeE',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:QLocale.FormatType'),
           )),
      ),
      'standaloneMonthName': (
          ('_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_10F'
           'ormatTypeE',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:QLocale.FormatType'),
           )),
      ),
      'weekDayName': (
          ('_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatType'
           'E',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:QLocale.FormatType'),
           )),
      ),
      'standaloneWeekDayName': (
          ('_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0_10'
           'FormatTypeE',
           ('address', 'text', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
               ('int', 'number', ''),
               ('int', 'enum', 'QtCore:QLocale.FormatType'),
           )),
      ),
      'localeMonthIndexData': (
          ('_ZNK16QCalendarBackend20localeMonthIndexDataEv',
           ('address', 'address', 'QtCore:QCalendarLocale'),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QCalendarBackend::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendarBackend::name() const
    return self.uglySide.call('ritual_ZNK16QCalendarBackend4nameEv')

  def names(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCalendarBackend::names() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#names

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCalendarBackend::names() const
    address = self.uglySide.call('ritual_ZNK16QCalendarBackend5namesEv')
    return QStringList._cuteOwning(address)

  def calendarSystem(self) -> QCalendar.System:
    """
    Calls Qt's 'QCalendar::System QCalendarBackend::calendarSystem() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#calendarSystem

    Returns
    -------

    QCalendar.System
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QCalendar.System(number)'
      gives.
    """
    #  QCalendar::System QCalendarBackend::calendarSystem() const
    return QCalendar.System(self.uglySide.call(
        'ritual_ZNK16QCalendarBackend14calendarSystemEv',
    ))

  def calendarId(self) -> QCalendar.SystemId:
    """
    Calls Qt's 'QCalendar::SystemId QCalendarBackend::calendarId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#calendarId

    Returns
    -------

    QCalendar.SystemId
      A new cute QCalendar::SystemId around the copy Qt gave back. Python
      owns it.
    """
    #  QCalendar::SystemId QCalendarBackend::calendarId() const
    address = self.uglySide.call(
        'ritual_ZNK16QCalendarBackend10calendarIdEv',
    )
    return QCalendar.SystemId._cuteOwning(address)

  @overload(int, int)
  def daysInMonth(self, month: int, year: int) -> int:
    """
    Calls Qt's 'int QCalendarBackend::daysInMonth(int month, int year)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#daysInMonth

    Parameters
    ----------

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.
    """
    #  int QCalendarBackend::daysInMonth(int month, int year) const
    return self.uglySide.call(
        'ritual_ZNK16QCalendarBackend11daysInMonthEii', month, year,
    )

  @overload(int)
  def daysInYear(self, year: int) -> int:
    """
    Calls Qt's 'int QCalendarBackend::daysInYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#daysInYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  int QCalendarBackend::daysInYear(int year) const
    ritual = 'ritual_ZNK16QCalendarBackend10daysInYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend10daysInYearEi'
    return self.uglySide.call(ritual, year)

  @overload(int)
  def monthsInYear(self, year: int) -> int:
    """
    Calls Qt's 'int QCalendarBackend::monthsInYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#monthsInYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  int QCalendarBackend::monthsInYear(int year) const
    ritual = 'ritual_ZNK16QCalendarBackend12monthsInYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend12monthsInYearEi'
    return self.uglySide.call(ritual, year)

  @overload(int, int, int)
  def isDateValid(self, year: int, month: int, day: int) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isDateValid(int year, int month, int
    day) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isDateValid

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.

    day : int
      Passed on as it is.
    """
    #  bool QCalendarBackend::isDateValid(int year, int month, int day) const
    ritual = 'ritual_ZNK16QCalendarBackend11isDateValidEiii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend11isDateValidEiii'
    return self.uglySide.call(ritual, year, month, day)

  @overload(int)
  def isLeapYear(self, year: int) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isLeapYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QCalendarBackend::isLeapYear(int year) const
    return self.uglySide.call(
        'ritual_ZNK16QCalendarBackend10isLeapYearEi', year,
    )

  def isLunar(self) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isLunar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isLunar
    """
    #  bool QCalendarBackend::isLunar() const
    return self.uglySide.call('ritual_ZNK16QCalendarBackend7isLunarEv')

  def isLuniSolar(self) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isLuniSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isLuniSolar
    """
    #  bool QCalendarBackend::isLuniSolar() const
    return self.uglySide.call('ritual_ZNK16QCalendarBackend11isLuniSolarEv')

  def isSolar(self) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isSolar
    """
    #  bool QCalendarBackend::isSolar() const
    return self.uglySide.call('ritual_ZNK16QCalendarBackend7isSolarEv')

  def isProleptic(self) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isProleptic() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isProleptic
    """
    #  bool QCalendarBackend::isProleptic() const
    ritual = 'ritual_ZNK16QCalendarBackend11isProlepticEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend11isProlepticEv'
    return self.uglySide.call(ritual)

  def hasYearZero(self) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::hasYearZero() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#hasYearZero
    """
    #  bool QCalendarBackend::hasYearZero() const
    ritual = 'ritual_ZNK16QCalendarBackend11hasYearZeroEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend11hasYearZeroEv'
    return self.uglySide.call(ritual)

  def maximumDaysInMonth(self) -> int:
    """
    Calls Qt's 'int QCalendarBackend::maximumDaysInMonth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#maximumDaysInMonth
    """
    #  int QCalendarBackend::maximumDaysInMonth() const
    ritual = 'ritual_ZNK16QCalendarBackend18maximumDaysInMonthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend18maximumDaysInMonthEv'
    return self.uglySide.call(ritual)

  def minimumDaysInMonth(self) -> int:
    """
    Calls Qt's 'int QCalendarBackend::minimumDaysInMonth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#minimumDaysInMonth
    """
    #  int QCalendarBackend::minimumDaysInMonth() const
    ritual = 'ritual_ZNK16QCalendarBackend18minimumDaysInMonthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend18minimumDaysInMonthEv'
    return self.uglySide.call(ritual)

  def maximumMonthsInYear(self) -> int:
    """
    Calls Qt's 'int QCalendarBackend::maximumMonthsInYear() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#maximumMonthsInYear
    """
    #  int QCalendarBackend::maximumMonthsInYear() const
    ritual = 'ritual_ZNK16QCalendarBackend19maximumMonthsInYearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend19maximumMonthsInYearEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def julianDayToDate(self, jd: int) -> QCalendar.YearMonthDay:
    """
    Calls Qt's 'QCalendar::YearMonthDay
    QCalendarBackend::julianDayToDate(qint64 jd) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#julianDayToDate

    Parameters
    ----------

    jd : int
      Passed on as it is.

    Returns
    -------

    QCalendar.YearMonthDay
      A new cute QCalendar::YearMonthDay around the copy Qt gave back. Python
      owns it.
    """
    #  QCalendar::YearMonthDay QCalendarBackend::julianDayToDate(qint64 jd)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QCalendarBackend15julianDayToDateEx', jd,
    )
    return QCalendar.YearMonthDay._cuteOwning(address)

  @overload(int)
  def dayOfWeek(self, jd: int) -> int:
    """
    Calls Qt's 'int QCalendarBackend::dayOfWeek(qint64 jd) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#dayOfWeek

    Parameters
    ----------

    jd : int
      Passed on as it is.
    """
    #  int QCalendarBackend::dayOfWeek(qint64 jd) const
    ritual = 'ritual_ZNK16QCalendarBackend9dayOfWeekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QCalendarBackend9dayOfWeekEx'
    return self.uglySide.call(ritual, jd)

  @overload(QCalendar.YearMonthDay, int)
  def matchCenturyToWeekday(
      self,
      parts: QCalendar.YearMonthDay,
      dow: int,
  ) -> int:
    """
    Calls Qt's 'qint64 QCalendarBackend::matchCenturyToWeekday(const
    QCalendar::YearMonthDay &parts, int dow) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#matchCenturyToWeekday

    Parameters
    ----------

    parts : QCalendar.YearMonthDay
      Passed on as a value: Qt reads the C++ QCalendar::YearMonthDay, which
      stays Python's own.

    dow : int
      Passed on as it is.
    """
    #  qint64 QCalendarBackend::matchCenturyToWeekday(const
    #      QCalendar::YearMonthDay &parts, int dow) const
    ritual = (
        'ritual_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCalendar1'
        '2YearMonthDayEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCalendarBackend21matchCenturyToWeekdayERKN9QCal'
          'endar12YearMonthDayEi')
    return self.uglySide.call(ritual, self._valueOf(parts), dow)

  @overload(QLocale, int, int, QLocale.FormatType)
  def monthName(
      self,
      locale: QLocale,
      month: int,
      year: int,
      format: QLocale.FormatType,
  ) -> str:
    """
    Calls Qt's 'QString QCalendarBackend::monthName(const QLocale &locale,
    int month, int year, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#monthName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendarBackend::monthName(const QLocale &locale, int month,
    #      int year, QLocale::FormatType format) const
    ritual = (
        'ritual_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10FormatTyp'
        'eE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCalendarBackend9monthNameERK7QLocaleiiNS0_10For'
          'matTypeE')
    return self.uglySide.call(
        ritual, self._valueOf(locale), month, year, format.value,
    )

  @overload(QLocale, int, int, QLocale.FormatType)
  def standaloneMonthName(
      self,
      locale: QLocale,
      month: int,
      year: int,
      format: QLocale.FormatType,
  ) -> str:
    """
    Calls Qt's 'QString QCalendarBackend::standaloneMonthName(const QLocale
    &locale, int month, int year, QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#standaloneMonthName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendarBackend::standaloneMonthName(const QLocale &locale,
    #      int month, int year, QLocale::FormatType format) const
    ritual = (
        'ritual_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocaleiiNS0_'
        '10FormatTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCalendarBackend19standaloneMonthNameERK7QLocale'
          'iiNS0_10FormatTypeE')
    return self.uglySide.call(
        ritual, self._valueOf(locale), month, year, format.value,
    )

  @overload(QLocale, int, QLocale.FormatType)
  def weekDayName(
      self,
      locale: QLocale,
      day: int,
      format: QLocale.FormatType,
  ) -> str:
    """
    Calls Qt's 'QString QCalendarBackend::weekDayName(const QLocale &locale,
    int day, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#weekDayName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    day : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendarBackend::weekDayName(const QLocale &locale, int day,
    #      QLocale::FormatType format) const
    ritual = (
        'ritual_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10FormatT'
        'ypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCalendarBackend11weekDayNameERK7QLocaleiNS0_10F'
          'ormatTypeE')
    return self.uglySide.call(
        ritual, self._valueOf(locale), day, format.value,
    )

  @overload(QLocale, int, QLocale.FormatType)
  def standaloneWeekDayName(
      self,
      locale: QLocale,
      day: int,
      format: QLocale.FormatType,
  ) -> str:
    """
    Calls Qt's 'QString QCalendarBackend::standaloneWeekDayName(const QLocale
    &locale, int day, QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#standaloneWeekDayName

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    day : int
      Passed on as it is.

    format : QLocale.FormatType
      Passed on as its number.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCalendarBackend::standaloneWeekDayName(const QLocale &locale,
    #      int day, QLocale::FormatType format) const
    ritual = (
        'ritual_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLocaleiNS0'
        '_10FormatTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK16QCalendarBackend21standaloneWeekDayNameERK7QLoca'
          'leiNS0_10FormatTypeE')
    return self.uglySide.call(
        ritual, self._valueOf(locale), day, format.value,
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
    Calls Qt's 'QString QCalendarBackend::dateTimeToString(QStringView
    format, const QDateTime &datetime, QDate dateOnly, QTime timeOnly, const
    QLocale &locale) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#dateTimeToString

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
    #  QString QCalendarBackend::dateTimeToString(QStringView format, const
    #      QDateTime &datetime, QDate dateOnly, QTime timeOnly, const QLocale
    #      &locale) const
    return self.uglySide.call(
        'ritual_ZNK16QCalendarBackend16dateTimeToStringE11QStringViewRK9QDa'
        'teTime5QDate5QTimeRK7QLocale',
        format, self._valueOf(datetime), self._valueOf(dateOnly),
        self._valueOf(timeOnly), self._valueOf(locale),
    )

  def isGregorian(self) -> bool:
    """
    Calls Qt's 'bool QCalendarBackend::isGregorian() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#isGregorian
    """
    #  bool QCalendarBackend::isGregorian() const
    return self.uglySide.call('ritual_ZNK16QCalendarBackend11isGregorianEv')

  def localeMonthIndexData(self) -> Optional[QCalendarLocale]:
    """
    Calls Qt's 'const QCalendarLocale
    *QCalendarBackend::localeMonthIndexData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#localeMonthIndexData

    Returns
    -------

    Optional[QCalendarLocale]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarLocale *QCalendarBackend::localeMonthIndexData() const
    address = self.uglySide.call(
        'ritual_ZNK16QCalendarBackend20localeMonthIndexDataEv',
    )
    from . import QCalendarLocale
    return QCalendarLocale._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QCalendarBackend::setIndex(size_t index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarbackend.html#setIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QCalendarBackend::setIndex(size_t index)
    self.uglySide.call('ritual_ZN16QCalendarBackend8setIndexEm', index)

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
    Qt's 'QCalendarBackend::QCalendarBackend()': the class is abstract, so
    C++ cannot make one, and the C++ class of ours does not fill in every
    function it leaves open.
    """
    raise NotImplementedError(
        "'QCalendarBackend.__init__' has no cute function yet. Qt's "
        "'QCalendarBackend::QCalendarBackend()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open.")

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

  @overload(QStringList)
  def registerCustomBackend(self, names: QStringList) -> QCalendar.SystemId:
    """
    Calls Qt's 'QCalendar::SystemId
    QCalendarBackend::registerCustomBackend(const QStringList &names)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarbackend.html#registerCustomBackend

    Parameters
    ----------

    names : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    QCalendar.SystemId
      A new cute QCalendar::SystemId around the copy Qt gave back. Python
      owns it.
    """
    #  QCalendar::SystemId QCalendarBackend::registerCustomBackend(const
    #      QStringList &names)
    address = self.uglySide.call(
        'ritual_ZN16QCalendarBackend21registerCustomBackendERK5QListI7QStri'
        'ngE',
        self._valueOf(names),
    )
    return QCalendar.SystemId._cuteOwning(address)

  @staticmethod
  def dateToJulianDay(*__, **_) -> Never:
    """
    Qt's 'bool QCalendarBackend::dateToJulianDay(int year, int month, int
    day, qint64 *jd) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QCalendarBackend.dateToJulianDay' has no cute function yet. Qt's "
        "'bool QCalendarBackend::dateToJulianDay(int year, int month, int "
        "day, qint64 *jd) const': takes a number to change where it is.")

  @staticmethod
  def localeMonthData(*__, **_) -> Never:
    """
    Qt's 'const char16_t *QCalendarBackend::localeMonthData() const': gives
    'unsigned short', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCalendarBackend.localeMonthData' has no cute function yet. Qt's "
        "'const char16_t *QCalendarBackend::localeMonthData() const': gives "
        "'unsigned short', which has no cute class yet.")
