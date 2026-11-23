"""
QDate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QCalendar, QDateTime, QTimeZone
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCalendar = WAIT['QCalendar']
  QTimeZone = WAIT['QTimeZone']


class QDate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDate: a plain Python object standing in front of one
  C++ QDate.

  C++ hands a QDate around as a copy, so every C++ QDate behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDate that has a ritual and that Python can call so
  far, 32 names in all: 'isNull', 'isValid', 'year', 'month', 'day',
  'dayOfWeek', 'dayOfYear', 'daysInMonth', 'daysInYear', 'startOfDay',
  'endOfDay', 'toString', 'setDate', 'addDays', 'addMonths', 'addYears',
  'daysTo', 'currentDate', 'fromString', 'isLeapYear', 'fromJulianDay',
  'toJulianDay', 'nullJd', 'minJd', 'maxJd', 'unixEpochJd', '__eq__',
  '__ne__', '__lt__', '__gt__', '__le__', '__ge__'. It can be made from
  Python, in 4 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'int QDate::weekNumber(int *yearNum) const': takes a number to
    change where it is.
  - Qt's 'QString QDate::toString(QStringView format) const': takes in Python
    what 'QString QDate::toString(const QString &format) const' takes.
  - Qt's 'QString QDate::toString(QStringView format, QCalendar cal) const':
    takes in Python what 'QString QDate::toString(const QString &format,
    QCalendar cal) const' takes.
  - Qt's 'void QDate::getDate(int *year, int *month, int *day) const': takes
    a number to change where it is.
  - Qt's 'QDate QDate::fromString(const QString &string, Qt::DateFormat
    format)': takes in Python what 'QDate QDate::fromString(QStringView
    string, Qt::DateFormat format)' takes.
  - Qt's 'QDate QDate::fromString(const QString &string, QStringView format,
    QCalendar cal)': takes in Python what 'QDate
    QDate::fromString(QStringView string, QStringView format, QCalendar cal)'
    takes.
  - Qt's 'QDate QDate::fromString(const QString &string, const QString
    &format, QCalendar cal)': takes in Python what 'QDate
    QDate::fromString(QStringView string, QStringView format, QCalendar cal)'
    takes.
  - Qt's 'QDate QDate::fromString(const QString &string, QStringView format,
    int baseYear)': takes in Python what 'QDate QDate::fromString(QStringView
    string, QStringView format, int baseYear)' takes.
  - Qt's 'QDate QDate::fromString(const QString &string, QStringView format,
    int baseYear, QCalendar cal)': takes in Python what 'QDate
    QDate::fromString(QStringView string, QStringView format, int baseYear,
    QCalendar cal)' takes.
  - Qt's 'QDate QDate::fromString(const QString &string, const QString
    &format, int baseYear)': takes in Python what 'QDate
    QDate::fromString(QStringView string, QStringView format, int baseYear)'
    takes.
  - Qt's 'QDate QDate::fromString(const QString &string, const QString
    &format, int baseYear, QCalendar cal)': takes in Python what 'QDate
    QDate::fromString(QStringView string, QStringView format, int baseYear,
    QCalendar cal)' takes.
  - Qt's 'QDate::~QDate()': the destructor: Python removes its C++ QDate by
    it, and has no other use for it.

  What has no ritual
  ------------------

  6 of the 74 functions Qt declares: 6 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QDate is created at the first use, not by 'QDate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDate back gives a copy the ritual made for Python,
    in a new cute QDate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def currentDate() -> QDate:
    """
    Calls Qt's 'QDate QDate::currentDate()'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#currentDate

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::currentDate()
    address = Rituals.call('ritual_ZN5QDate11currentDateEv')
    return QDate._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, Qt.DateFormat)
  def fromString(
      string: str,
      format: Qt.DateFormat = Qt.DateFormat.TextDate,
  ) -> QDate:
    """
    Calls Qt's 'QDate QDate::fromString(QStringView string, Qt::DateFormat
    format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.DateFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.DateFormat.TextDate.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::fromString(QStringView string, Qt::DateFormat format)
    address = Rituals.call(
        'ritual_ZN5QDate10fromStringE11QStringViewN2Qt10DateFormatE',
        string, format.value,
    )
    return QDate._cuteOwning(address)

  @staticmethod
  @overload(str, str, QCalendar)
  def fromString(string: str, format: str, cal: QCalendar) -> QDate:
    """
    Calls Qt's 'QDate QDate::fromString(QStringView string, QStringView
    format, QCalendar cal)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::fromString(QStringView string, QStringView format,
    #      QCalendar cal)
    address = Rituals.call(
        'ritual_ZN5QDate10fromStringE11QStringViewS0_9QCalendar',
        string, format, CuteMixin._valueOf(cal),
    )
    return QDate._cuteOwning(address)

  @staticmethod
  @overload(str, str)
  @overload(str, str, int)
  def fromString(string: str, format: str, baseYear: int = 1900) -> QDate:
    """
    Calls Qt's 'QDate QDate::fromString(QStringView string, QStringView
    format, int baseYear)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    baseYear : int
      Passed on as it is. May be left out, as in Qt: it is then 1900.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::fromString(QStringView string, QStringView format, int
    #      baseYear)
    address = Rituals.call(
        'ritual_ZN5QDate10fromStringE11QStringViewS0_i',
        string, format, baseYear,
    )
    return QDate._cuteOwning(address)

  @staticmethod
  @overload(str, str, int, QCalendar)
  def fromString(
      string: str,
      format: str,
      baseYear: int,
      cal: QCalendar,
  ) -> QDate:
    """
    Calls Qt's 'QDate QDate::fromString(QStringView string, QStringView
    format, int baseYear, QCalendar cal)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    baseYear : int
      Passed on as it is.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::fromString(QStringView string, QStringView format, int
    #      baseYear, QCalendar cal)
    address = Rituals.call(
        'ritual_ZN5QDate10fromStringE11QStringViewS0_i9QCalendar',
        string, format, baseYear, CuteMixin._valueOf(cal),
    )
    return QDate._cuteOwning(address)

  @staticmethod
  @overload(int)
  def isLeapYear(year: int) -> bool:
    """
    Calls Qt's 'bool QDate::isLeapYear(int year)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QDate::isLeapYear(int year)
    return Rituals.call('ritual_ZN5QDate10isLeapYearEi', year)

  @staticmethod
  @overload(int)
  def fromJulianDay(jd_: int) -> QDate:
    """
    Calls Qt's 'QDate QDate::fromJulianDay(qint64 jd_)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#fromJulianDay

    Parameters
    ----------

    jd_ : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::fromJulianDay(qint64 jd_)
    address = Rituals.call('ritual_ZN5QDate13fromJulianDayEx', jd_)
    return QDate._cuteOwning(address)

  @staticmethod
  def nullJd() -> int:
    """
    Calls Qt's 'qint64 QDate::nullJd()'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#nullJd
    """
    #  qint64 QDate::nullJd()
    return Rituals.call('ritual_ZN5QDate6nullJdEv')

  @staticmethod
  def minJd() -> int:
    """
    Calls Qt's 'qint64 QDate::minJd()'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#minJd
    """
    #  qint64 QDate::minJd()
    return Rituals.call('ritual_ZN5QDate5minJdEv')

  @staticmethod
  def maxJd() -> int:
    """
    Calls Qt's 'qint64 QDate::maxJd()'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#maxJd
    """
    #  qint64 QDate::maxJd()
    return Rituals.call('ritual_ZN5QDate5maxJdEv')

  @staticmethod
  def unixEpochJd() -> int:
    """
    Calls Qt's 'qint64 QDate::unixEpochJd()'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#unixEpochJd
    """
    #  qint64 QDate::unixEpochJd()
    return Rituals.call('ritual_ZN5QDate11unixEpochJdEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDate'

  #  Qt's '~QDate()'. Naming it makes this a value class: Python owns every
  #  C++ QDate behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN5QDateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDate::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#isNull
    """
    #  bool QDate::isNull() const
    return self.uglySide.call('ritual_ZNK5QDate6isNullEv')

  @overload()
  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDate::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#isValid
    """
    #  bool QDate::isValid() const
    return self.uglySide.call('ritual_ZNK5QDate7isValidEv')

  @staticmethod
  @overload(int, int, int)
  def isValid(y: int, m: int, d: int) -> bool:
    """
    Calls Qt's 'bool QDate::isValid(int y, int m, int d)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#isValid

    Parameters
    ----------

    y : int
      Passed on as it is.

    m : int
      Passed on as it is.

    d : int
      Passed on as it is.
    """
    #  bool QDate::isValid(int y, int m, int d)
    return Rituals.call('ritual_ZN5QDate7isValidEiii', y, m, d)

  @overload()
  def year(self) -> int:
    """
    Calls Qt's 'int QDate::year() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#year
    """
    #  int QDate::year() const
    return self.uglySide.call('ritual_ZNK5QDate4yearEv')

  @overload(QCalendar)
  def year(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::year(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#year

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::year(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate4yearE9QCalendar', self._valueOf(cal),
    )

  @overload()
  def month(self) -> int:
    """
    Calls Qt's 'int QDate::month() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#month
    """
    #  int QDate::month() const
    return self.uglySide.call('ritual_ZNK5QDate5monthEv')

  @overload(QCalendar)
  def month(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::month(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#month

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::month(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate5monthE9QCalendar', self._valueOf(cal),
    )

  @overload()
  def day(self) -> int:
    """
    Calls Qt's 'int QDate::day() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#day
    """
    #  int QDate::day() const
    return self.uglySide.call('ritual_ZNK5QDate3dayEv')

  @overload(QCalendar)
  def day(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::day(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#day

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::day(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate3dayE9QCalendar', self._valueOf(cal),
    )

  @overload()
  def dayOfWeek(self) -> int:
    """
    Calls Qt's 'int QDate::dayOfWeek() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#dayOfWeek
    """
    #  int QDate::dayOfWeek() const
    return self.uglySide.call('ritual_ZNK5QDate9dayOfWeekEv')

  @overload(QCalendar)
  def dayOfWeek(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::dayOfWeek(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#dayOfWeek

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::dayOfWeek(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate9dayOfWeekE9QCalendar', self._valueOf(cal),
    )

  @overload()
  def dayOfYear(self) -> int:
    """
    Calls Qt's 'int QDate::dayOfYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#dayOfYear
    """
    #  int QDate::dayOfYear() const
    return self.uglySide.call('ritual_ZNK5QDate9dayOfYearEv')

  @overload(QCalendar)
  def dayOfYear(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::dayOfYear(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#dayOfYear

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::dayOfYear(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate9dayOfYearE9QCalendar', self._valueOf(cal),
    )

  @overload()
  def daysInMonth(self) -> int:
    """
    Calls Qt's 'int QDate::daysInMonth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#daysInMonth
    """
    #  int QDate::daysInMonth() const
    return self.uglySide.call('ritual_ZNK5QDate11daysInMonthEv')

  @overload(QCalendar)
  def daysInMonth(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::daysInMonth(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#daysInMonth

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::daysInMonth(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate11daysInMonthE9QCalendar', self._valueOf(cal),
    )

  @overload()
  def daysInYear(self) -> int:
    """
    Calls Qt's 'int QDate::daysInYear() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#daysInYear
    """
    #  int QDate::daysInYear() const
    return self.uglySide.call('ritual_ZNK5QDate10daysInYearEv')

  @overload(QCalendar)
  def daysInYear(self, cal: QCalendar) -> int:
    """
    Calls Qt's 'int QDate::daysInYear(QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#daysInYear

    Parameters
    ----------

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  int QDate::daysInYear(QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate10daysInYearE9QCalendar', self._valueOf(cal),
    )

  @overload(Qt.TimeSpec)
  @overload(Qt.TimeSpec, int)
  def startOfDay(
      self,
      spec: Qt.TimeSpec,
      offsetSeconds: int = 0,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDate::startOfDay(Qt::TimeSpec spec, int
    offsetSeconds) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#startOfDay

    Parameters
    ----------

    spec : Qt.TimeSpec
      Passed on as its number.

    offsetSeconds : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDate::startOfDay(Qt::TimeSpec spec, int offsetSeconds)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK5QDate10startOfDayEN2Qt8TimeSpecEi',
        spec.value, offsetSeconds,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def startOfDay(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDate::startOfDay(const QTimeZone &zone) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#startOfDay

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDate::startOfDay(const QTimeZone &zone) const
    address = self.uglySide.call(
        'ritual_ZNK5QDate10startOfDayERK9QTimeZone', self._valueOf(zone),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  def startOfDay(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDate::startOfDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#startOfDay

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDate::startOfDay() const
    address = self.uglySide.call('ritual_ZNK5QDate10startOfDayEv')
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(Qt.TimeSpec)
  @overload(Qt.TimeSpec, int)
  def endOfDay(self, spec: Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDate::endOfDay(Qt::TimeSpec spec, int
    offsetSeconds) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#endOfDay

    Parameters
    ----------

    spec : Qt.TimeSpec
      Passed on as its number.

    offsetSeconds : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDate::endOfDay(Qt::TimeSpec spec, int offsetSeconds) const
    address = self.uglySide.call(
        'ritual_ZNK5QDate8endOfDayEN2Qt8TimeSpecEi',
        spec.value, offsetSeconds,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def endOfDay(self, zone: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDate::endOfDay(const QTimeZone &zone) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#endOfDay

    Parameters
    ----------

    zone : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDate::endOfDay(const QTimeZone &zone) const
    address = self.uglySide.call(
        'ritual_ZNK5QDate8endOfDayERK9QTimeZone', self._valueOf(zone),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  def endOfDay(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDate::endOfDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#endOfDay

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDate::endOfDay() const
    address = self.uglySide.call('ritual_ZNK5QDate8endOfDayEv')
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  @overload(Qt.DateFormat)
  def toString(self, format: Qt.DateFormat = Qt.DateFormat.TextDate) -> str:
    """
    Calls Qt's 'QString QDate::toString(Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#toString

    Parameters
    ----------

    format : Qt.DateFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.DateFormat.TextDate.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDate::toString(Qt::DateFormat format) const
    return self.uglySide.call(
        'ritual_ZNK5QDate8toStringEN2Qt10DateFormatE', format.value,
    )

  @overload(str)
  def toString(self, format: str) -> str:
    """
    Calls Qt's 'QString QDate::toString(const QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#toString

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDate::toString(const QString &format) const
    return self.uglySide.call('ritual_ZNK5QDate8toStringERK7QString', format)

  @overload(str, QCalendar)
  def toString(self, format: str, cal: QCalendar) -> str:
    """
    Calls Qt's 'QString QDate::toString(const QString &format, QCalendar cal)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#toString

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDate::toString(const QString &format, QCalendar cal) const
    return self.uglySide.call(
        'ritual_ZNK5QDate8toStringERK7QString9QCalendar',
        format, self._valueOf(cal),
    )

  @overload(int)
  def addDays(self, days: int) -> QDate:
    """
    Calls Qt's 'QDate QDate::addDays(qint64 days) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#addDays

    Parameters
    ----------

    days : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::addDays(qint64 days) const
    address = self.uglySide.call('ritual_ZNK5QDate7addDaysEx', days)
    return QDate._cuteOwning(address)

  @overload(int)
  def addMonths(self, months: int) -> QDate:
    """
    Calls Qt's 'QDate QDate::addMonths(int months) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#addMonths

    Parameters
    ----------

    months : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::addMonths(int months) const
    address = self.uglySide.call('ritual_ZNK5QDate9addMonthsEi', months)
    return QDate._cuteOwning(address)

  @overload(int, QCalendar)
  def addMonths(self, months: int, cal: QCalendar) -> QDate:
    """
    Calls Qt's 'QDate QDate::addMonths(int months, QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#addMonths

    Parameters
    ----------

    months : int
      Passed on as it is.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::addMonths(int months, QCalendar cal) const
    address = self.uglySide.call(
        'ritual_ZNK5QDate9addMonthsEi9QCalendar', months, self._valueOf(cal),
    )
    return QDate._cuteOwning(address)

  @overload(int)
  def addYears(self, years: int) -> QDate:
    """
    Calls Qt's 'QDate QDate::addYears(int years) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#addYears

    Parameters
    ----------

    years : int
      Passed on as it is.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::addYears(int years) const
    address = self.uglySide.call('ritual_ZNK5QDate8addYearsEi', years)
    return QDate._cuteOwning(address)

  @overload(int, QCalendar)
  def addYears(self, years: int, cal: QCalendar) -> QDate:
    """
    Calls Qt's 'QDate QDate::addYears(int years, QCalendar cal) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#addYears

    Parameters
    ----------

    years : int
      Passed on as it is.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.

    Returns
    -------

    QDate
      A new cute QDate around the copy Qt gave back. Python owns it.
    """
    #  QDate QDate::addYears(int years, QCalendar cal) const
    address = self.uglySide.call(
        'ritual_ZNK5QDate8addYearsEi9QCalendar', years, self._valueOf(cal),
    )
    return QDate._cuteOwning(address)

  @overload(THIS)
  def daysTo(self, d: QDate) -> int:
    """
    Calls Qt's 'qint64 QDate::daysTo(QDate d) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#daysTo

    Parameters
    ----------

    d : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  qint64 QDate::daysTo(QDate d) const
    return self.uglySide.call('ritual_ZNK5QDate6daysToES_', self._valueOf(d))

  def toJulianDay(self) -> int:
    """
    Calls Qt's 'qint64 QDate::toJulianDay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#toJulianDay
    """
    #  qint64 QDate::toJulianDay() const
    return self.uglySide.call('ritual_ZNK5QDate11toJulianDayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int, int)
  def setDate(self, year: int, month: int, day: int) -> bool:
    """
    Calls Qt's 'bool QDate::setDate(int year, int month, int day)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#setDate

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.

    day : int
      Passed on as it is.
    """
    #  bool QDate::setDate(int year, int month, int day)
    return self.uglySide.call(
        'ritual_ZN5QDate7setDateEiii', year, month, day,
    )

  @overload(int, int, int, QCalendar)
  def setDate(self, year: int, month: int, day: int, cal: QCalendar) -> bool:
    """
    Calls Qt's 'bool QDate::setDate(int year, int month, int day, QCalendar
    cal)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#setDate

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.

    day : int
      Passed on as it is.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  bool QDate::setDate(int year, int month, int day, QCalendar cal)
    return self.uglySide.call(
        'ritual_ZN5QDate7setDateEiii9QCalendar',
        year, month, day, self._valueOf(cal),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QDate) -> bool:
    """
    Calls Qt's 'bool operator==(const QDate &lhs, const QDate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#operator==

    Parameters
    ----------

    rhs : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  bool operator==(const QDate &lhs, const QDate &rhs)
    return Rituals.call(
        'ritual_ZeqRK5QDateS1_',
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
  def __ne__(self, rhs: QDate) -> bool:
    """
    Calls Qt's 'bool operator!=(const QDate &lhs, const QDate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#operator!=

    Parameters
    ----------

    rhs : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  bool operator!=(const QDate &lhs, const QDate &rhs)
    return Rituals.call(
        'ritual_ZneRK5QDateS1_',
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

  @overload(THIS)
  def __lt__(self, rhs: QDate) -> bool:
    """
    Calls Qt's 'bool operator<(const QDate &lhs, const QDate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#operator<

    Parameters
    ----------

    rhs : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  bool operator<(const QDate &lhs, const QDate &rhs)
    return Rituals.call(
        'ritual_ZltRK5QDateS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QDate) -> bool:
    """
    Calls Qt's 'bool operator>(const QDate &lhs, const QDate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#operator>

    Parameters
    ----------

    rhs : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  bool operator>(const QDate &lhs, const QDate &rhs)
    return Rituals.call(
        'ritual_ZgtRK5QDateS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QDate) -> bool:
    """
    Calls Qt's 'bool operator<=(const QDate &lhs, const QDate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#operator<=

    Parameters
    ----------

    rhs : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  bool operator<=(const QDate &lhs, const QDate &rhs)
    return Rituals.call(
        'ritual_ZleRK5QDateS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QDate) -> bool:
    """
    Calls Qt's 'bool operator>=(const QDate &lhs, const QDate &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#operator>=

    Parameters
    ----------

    rhs : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  bool operator>=(const QDate &lhs, const QDate &rhs)
    return Rituals.call(
        'ritual_ZgeRK5QDateS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def __init__(self, julianDay: int) -> None:
    """
    Notes what was given, for Qt's 'QDate::QDate(qint64 julianDay)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#QDate

    Parameters
    ----------

    julianDay : int
      Passed on as it is.
    """
    #  QDate::QDate(qint64 julianDay)
    self._noteCreation(QDate, lambda: Rituals.call(
        'ritual_ZN5QDateC1Ex', julianDay,
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDate::QDate()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#QDate
    """
    #  QDate::QDate()
    self._noteCreation(QDate, lambda: Rituals.call('ritual_ZN5QDateC1Ev'))

  @overload(int, int, int)
  def __init__(self, y: int, m: int, d: int) -> None:
    """
    Notes what was given, for Qt's 'QDate::QDate(int y, int m, int d)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#QDate

    Parameters
    ----------

    y : int
      Passed on as it is.

    m : int
      Passed on as it is.

    d : int
      Passed on as it is.
    """
    #  QDate::QDate(int y, int m, int d)
    self._noteCreation(QDate, lambda: Rituals.call(
        'ritual_ZN5QDateC1Eiii', y, m, d,
    ))

  @overload(int, int, int, QCalendar)
  def __init__(self, y: int, m: int, d: int, cal: QCalendar) -> None:
    """
    Notes what was given, for Qt's 'QDate::QDate(int y, int m, int d,
    QCalendar cal)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdate.html#QDate

    Parameters
    ----------

    y : int
      Passed on as it is.

    m : int
      Passed on as it is.

    d : int
      Passed on as it is.

    cal : QCalendar
      Passed on as a value: Qt reads the C++ QCalendar, which stays Python's
      own.
    """
    #  QDate::QDate(int y, int m, int d, QCalendar cal)
    self._noteCreation(QDate, lambda: Rituals.call(
        'ritual_ZN5QDateC1Eiii9QCalendar', y, m, d, self._valueOf(cal),
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
