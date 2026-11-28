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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QLocale, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDate, QDateTime, QTime
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDate = WAIT['QDate']
  QDateTime = WAIT['QDateTime']
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
  so far, 26 names in all: 'isValid', 'daysInMonth', 'daysInYear',
  'monthsInYear', 'isDateValid', 'isLeapYear', 'isGregorian', 'isLunar',
  'isLuniSolar', 'isSolar', 'isProleptic', 'hasYearZero',
  'maximumDaysInMonth', 'minimumDaysInMonth', 'maximumMonthsInYear', 'name',
  'dateFromParts', 'matchCenturyToWeekday', 'partsFromDate', 'dayOfWeek',
  'monthName', 'standaloneMonthName', 'weekDayName', 'standaloneWeekDayName',
  'dateTimeToString', 'availableCalendars'. It can be made from Python, in 4
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCalendar::~QCalendar()': the destructor: Python removes its C++
    QCalendar by it, and has no other use for it.

  What has no ritual
  ------------------

  3 of the 35 functions Qt declares: 3 not a gap.

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

  #  The enums Qt writes inside QCalendar, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class System(CuteNum, scoped=True):
    """
    The enum 'QCalendar::System' of Qt, with the 7 names Qt gives in it. C++
    keeps these names inside the enum, so the class that holds the enum does
    not have them.
    """

    Gregorian = Kee[int](0)
    Julian = Kee[int](8)
    Milankovic = Kee[int](9)
    Jalali = Kee[int](10)
    IslamicCivil = Kee[int](11)
    Last = Kee[int](11)
    User = Kee[int](-1)

  #  The classes Qt writes inside QCalendar, each a class in here as in C++.

  class SystemId(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCalendar::SystemId: a plain Python object standing
    in front of one C++ QCalendar::SystemId.

    C++ hands a QCalendar::SystemId around as a copy, so every C++
    QCalendar::SystemId behind a cute one is Python's own: it is removed, by
    the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCalendar::SystemId that has a ritual and that
    Python can call so far, 3 names in all: 'isInEnum', 'index', 'isValid'.
    It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCalendar::SystemId::SystemId(QCalendar::System e)': names the
      enum 'QCalendar::System', whose class cannot be named here.
    - Qt's 'QCalendar::SystemId::~SystemId()': the destructor: Python removes
      its C++ QCalendar::SystemId by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QCalendar::SystemId is created at the first use, not by
      'QCalendar::SystemId(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCalendar::SystemId back gives a copy the ritual
      made for Python, in a new cute QCalendar::SystemId.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCalendar::SystemId'

    #  Qt's '~QCalendar::SystemId()'. Naming it makes this a value class:
    #  Python owns every C++ QCalendar::SystemId behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QCalendar8SystemIdD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isInEnum(self) -> bool:
      """
      Calls Qt's 'bool QCalendar::SystemId::isInEnum() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcalendar-systemid.html#isInEnum
      """
      #  bool QCalendar::SystemId::isInEnum() const
      return self.uglySide.call('ritual_ZNK9QCalendar8SystemId8isInEnumEv')

    def index(self) -> int:
      """
      Calls Qt's 'size_t QCalendar::SystemId::index() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcalendar-systemid.html#index
      """
      #  size_t QCalendar::SystemId::index() const
      return self.uglySide.call('ritual_ZNK9QCalendar8SystemId5indexEv')

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QCalendar::SystemId::isValid() const'.

      Qt's own words: https://doc.qt.io/qt-6/qcalendar-systemid.html#isValid
      """
      #  bool QCalendar::SystemId::isValid() const
      return self.uglySide.call('ritual_ZNK9QCalendar8SystemId7isValidEv')

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(int)
    def __init__(self, i: int) -> None:
      """
      Notes what was given, for Qt's 'QCalendar::SystemId::SystemId(size_t
      i)', which is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcalendar-systemid.html#SystemId

      Parameters
      ----------

      i : int
        Passed on as it is.
      """
      #  QCalendar::SystemId::SystemId(size_t i)
      self._noteCreation(QCalendar.SystemId, lambda: Rituals.call(
          'ritual_ZN9QCalendar8SystemIdC1Em', i,
      ))

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QCalendar::SystemId::SystemId()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qcalendar-systemid.html#SystemId
      """
      #  QCalendar::SystemId::SystemId()
      self._noteCreation(QCalendar.SystemId, lambda: Rituals.call(
          'ritual_ZN9QCalendar8SystemIdC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  class YearMonthDay(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCalendar::YearMonthDay: a plain Python object
    standing in front of one C++ QCalendar::YearMonthDay.

    C++ hands a QCalendar::YearMonthDay around as a copy, so every C++
    QCalendar::YearMonthDay behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QCalendar::YearMonthDay that has a ritual and that
    Python can call so far, 1 name in all: 'isValid'. It can be made from
    Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCalendar::YearMonthDay::~YearMonthDay()': the destructor: Python
      removes its C++ QCalendar::YearMonthDay by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QCalendar::YearMonthDay is created at the first use, not by
      'QCalendar::YearMonthDay(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCalendar::YearMonthDay back gives a copy the
      ritual made for Python, in a new cute QCalendar::YearMonthDay.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCalendar::YearMonthDay'

    #  Qt's '~QCalendar::YearMonthDay()'. Naming it makes this a value class:
    #  Python owns every C++ QCalendar::YearMonthDay behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN9QCalendar12YearMonthDayD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QCalendar::YearMonthDay::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qcalendar-yearmonthday.html#isValid
      """
      #  bool QCalendar::YearMonthDay::isValid() const
      return self.uglySide.call(
          'ritual_ZNK9QCalendar12YearMonthDay7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QCalendar::YearMonthDay::YearMonthDay()', which is called at the first
      use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcalendar-yearmonthday.html#YearMonthDay
      """
      #  QCalendar::YearMonthDay::YearMonthDay()
      self._noteCreation(QCalendar.YearMonthDay, lambda: Rituals.call(
          'ritual_ZN9QCalendar12YearMonthDayC1Ev',
      ))

    @overload(int)
    @overload(int, int)
    @overload(int, int, int)
    def __init__(self, y: int, m: int = 1, d: int = 1) -> None:
      """
      Notes what was given, for Qt's
      'QCalendar::YearMonthDay::YearMonthDay(int y, int m, int d)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qcalendar-yearmonthday.html#YearMonthDay

      Parameters
      ----------

      y : int
        Passed on as it is.

      m : int
        Passed on as it is. May be left out, as in Qt: it is then 1.

      d : int
        Passed on as it is. May be left out, as in Qt: it is then 1.
      """
      #  QCalendar::YearMonthDay::YearMonthDay(int y, int m, int d)
      self._noteCreation(QCalendar.YearMonthDay, lambda: Rituals.call(
          'ritual_ZN9QCalendar12YearMonthDayC1Eiii', y, m, d,
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def availableCalendars() -> QStringList:
    """
    Calls Qt's 'QStringList QCalendar::availableCalendars()'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#availableCalendars

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCalendar::availableCalendars()
    address = Rituals.call('ritual_ZN9QCalendar18availableCalendarsEv')
    return QStringList._cuteOwning(address)

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

  @overload(YearMonthDay)
  def dateFromParts(self, parts: YearMonthDay) -> QDate:
    """
    Calls Qt's 'QDate QCalendar::dateFromParts(const YearMonthDay &parts)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#dateFromParts

    Parameters
    ----------

    parts : YearMonthDay
      Passed on as a value: Qt reads the C++ QCalendar::YearMonthDay, which
      stays Python's own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendar::dateFromParts(const YearMonthDay &parts) const
    address = self.uglySide.call(
        'ritual_ZNK9QCalendar13dateFromPartsERKNS_12YearMonthDayE',
        self._valueOf(parts),
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(YearMonthDay, int)
  def matchCenturyToWeekday(self, parts: YearMonthDay, dow: int) -> QDate:
    """
    Calls Qt's 'QDate QCalendar::matchCenturyToWeekday(const YearMonthDay
    &parts, int dow) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendar.html#matchCenturyToWeekday

    Parameters
    ----------

    parts : YearMonthDay
      Passed on as a value: Qt reads the C++ QCalendar::YearMonthDay, which
      stays Python's own.

    dow : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QCalendar::matchCenturyToWeekday(const YearMonthDay &parts, int
    #      dow) const
    address = self.uglySide.call(
        'ritual_ZNK9QCalendar21matchCenturyToWeekdayERKNS_12YearMonthDayEi',
        self._valueOf(parts), dow,
    )
    from . import QDate
    return QDate._cuteOwning(address)

  @overload(QDate)
  def partsFromDate(self, date: QDate) -> YearMonthDay:
    """
    Calls Qt's 'YearMonthDay QCalendar::partsFromDate(QDate date) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#partsFromDate

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.

    Returns
    -------

    YearMonthDay
      A new cute QCalendar::YearMonthDay around the copy Qt gave back. Python
      owns it.
    """
    #  YearMonthDay QCalendar::partsFromDate(QDate date) const
    address = self.uglySide.call(
        'ritual_ZNK9QCalendar13partsFromDateE5QDate', self._valueOf(date),
    )
    return QCalendar.YearMonthDay._cuteOwning(address)

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
  @overload(QLocale, int, int, QLocale.FormatType)
  def monthName(
      self,
      locale: QLocale,
      month: int,
      year: int = -2147483648,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
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
      QLocale.FormatType.LongFormat.

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
  @overload(QLocale, int, int, QLocale.FormatType)
  def standaloneMonthName(
      self,
      locale: QLocale,
      month: int,
      year: int = -2147483648,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
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
      QLocale.FormatType.LongFormat.

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
  @overload(QLocale, int, QLocale.FormatType)
  def weekDayName(
      self,
      locale: QLocale,
      day: int,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
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
      QLocale.FormatType.LongFormat.

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
  @overload(QLocale, int, QLocale.FormatType)
  def standaloneWeekDayName(
      self,
      locale: QLocale,
      day: int,
      format: QLocale.FormatType = QLocale.FormatType.LongFormat,
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
      QLocale.FormatType.LongFormat.

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

  @overload(SystemId)
  def __init__(self, id: SystemId) -> None:
    """
    Notes what was given, for Qt's 'QCalendar::QCalendar(SystemId id)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qcalendar.html#QCalendar

    Parameters
    ----------

    id : SystemId
      Passed on as a value: Qt reads the C++ QCalendar::SystemId, which stays
      Python's own.
    """
    #  QCalendar::QCalendar(SystemId id)
    self._noteCreation(QCalendar, lambda: Rituals.call(
        'ritual_ZN9QCalendarC1ENS_8SystemIdE', self._valueOf(id),
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
