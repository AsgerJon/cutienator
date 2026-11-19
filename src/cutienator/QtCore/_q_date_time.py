"""
QDateTime binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qdatetime.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ._qt import Qt
from ._q_date_time_transition_resolution import TransitionResolution
from ._q_date_time_year_range import YearRange


class QDateTime(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDateTime: a plain Python object standing in front of
  one C++ QDateTime.

  C++ hands a QDateTime around as a copy, so every C++ QDateTime behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDateTime that has a ritual and that Python can call
  so far, 32 names in all: 'isNull', 'isValid', 'timeSpec', 'offsetFromUtc',
  'timeZoneAbbreviation', 'isDaylightTime', 'toMSecsSinceEpoch',
  'toSecsSinceEpoch', 'setTimeSpec', 'setOffsetFromUtc',
  'setMSecsSinceEpoch', 'setSecsSinceEpoch', 'toString', 'addDays',
  'addMonths', 'addYears', 'addSecs', 'addMSecs', 'toTimeSpec',
  'toLocalTime', 'toUTC', 'toOffsetFromUtc', 'daysTo', 'secsTo', 'msecsTo',
  'currentDateTime', 'currentDateTimeUtc', 'fromString',
  'fromMSecsSinceEpoch', 'fromSecsSinceEpoch', 'currentMSecsSinceEpoch',
  'currentSecsSinceEpoch'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDateTime::QDateTime(QDate date, QTime time, Qt::TimeSpec spec, int
    offsetSeconds)': names 'QDate', which has no cute class yet.
  - Qt's 'QDateTime::QDateTime(QDate date, QTime time, const QTimeZone
    &timeZone, TransitionResolution resolve)': names 'QDate', which has no
    cute class yet.
  - Qt's 'QDateTime::QDateTime(QDate date, QTime time, TransitionResolution
    resolve)': names 'QDate', which has no cute class yet.
  - Qt's 'QDateTime::~QDateTime()': the destructor: Python removes its C++
    QDateTime by it, and has no other use for it.
  - Qt's 'QDate QDateTime::date() const': gives 'QDate', which has no cute
    class yet.
  - Qt's 'QTime QDateTime::time() const': gives 'QTime', which has no cute
    class yet.
  - Qt's 'QTimeZone QDateTime::timeRepresentation() const': gives
    'QTimeZone', which has no cute class yet.
  - Qt's 'QTimeZone QDateTime::timeZone() const': gives 'QTimeZone', which
    has no cute class yet.
  - Qt's 'void QDateTime::setDate(QDate date, TransitionResolution resolve)':
    names 'QDate', which has no cute class yet.
  - Qt's 'void QDateTime::setTime(QTime time, TransitionResolution resolve)':
    names 'QTime', which has no cute class yet.
  - Qt's 'void QDateTime::setTimeZone(const QTimeZone &toZone,
    TransitionResolution resolve)': names 'QTimeZone', which has no cute
    class yet.
  - Qt's 'QString QDateTime::toString(const QString &format, QCalendar cal)
    const': names 'QCalendar', which has no cute class yet.
  - Qt's 'QString QDateTime::toString(QStringView format) const': takes in
    Python what 'QString QDateTime::toString(const QString &format) const'
    takes.
  - Qt's 'QString QDateTime::toString(QStringView format, QCalendar cal)
    const': names 'QCalendar', which has no cute class yet.
  - Qt's 'QDateTime QDateTime::toTimeZone(const QTimeZone &toZone) const':
    names 'QTimeZone', which has no cute class yet.
  - Qt's 'QDateTime QDateTime::currentDateTime(const QTimeZone &zone)': names
    'QTimeZone', which has no cute class yet.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string,
    Qt::DateFormat format)': takes in Python what 'QDateTime
    QDateTime::fromString(QStringView string, Qt::DateFormat format)' takes.
  - Qt's 'QDateTime QDateTime::fromString(QStringView string, QStringView
    format, QCalendar cal)': names 'QCalendar', which has no cute class yet.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string, QStringView
    format, QCalendar cal)': names 'QCalendar', which has no cute class yet.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string, const
    QString &format, QCalendar cal)': names 'QCalendar', which has no cute
    class yet.
  - Qt's 'QDateTime QDateTime::fromString(QStringView string, QStringView
    format, int baseYear, QCalendar cal)': names 'QCalendar', which has no
    cute class yet.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string, QStringView
    format, int baseYear)': takes in Python what 'QDateTime
    QDateTime::fromString(QStringView string, QStringView format, int
    baseYear)' takes.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string, QStringView
    format, int baseYear, QCalendar cal)': names 'QCalendar', which has no
    cute class yet.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string, const
    QString &format, int baseYear)': takes in Python what 'QDateTime
    QDateTime::fromString(QStringView string, QStringView format, int
    baseYear)' takes.
  - Qt's 'QDateTime QDateTime::fromString(const QString &string, const
    QString &format, int baseYear, QCalendar cal)': names 'QCalendar', which
    has no cute class yet.
  - Qt's 'QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs, const
    QTimeZone &timeZone)': names 'QTimeZone', which has no cute class yet.
  - Qt's 'QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs, const
    QTimeZone &timeZone)': names 'QTimeZone', which has no cute class yet.

  What has no ritual
  ------------------

  9 of the 74 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 1 private.

  What to expect
  --------------

  - The C++ QDateTime is created at the first use, not by 'QDateTime(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDateTime back gives a copy the ritual made for
    Python, in a new cute QDateTime.
  """

  #  The enums Qt writes inside QDateTime, and the names Qt has for the
  #  combinations of its flags enums.
  TransitionResolution = TransitionResolution
  YearRange = YearRange

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def currentDateTime() -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::currentDateTime()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#currentDateTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::currentDateTime()
    address = Rituals.call('ritual_ZN9QDateTime15currentDateTimeEv')
    return QDateTime._cuteOwning(address)

  @staticmethod
  def currentDateTimeUtc() -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::currentDateTimeUtc()'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#currentDateTimeUtc

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::currentDateTimeUtc()
    address = Rituals.call('ritual_ZN9QDateTime18currentDateTimeUtcEv')
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(str)
  @overload(str, Qt.DateFormat)
  def fromString(
      string: str,
      format: Qt.DateFormat = Qt.DateFormat.TextDate,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::fromString(QStringView string,
    Qt::DateFormat format)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : Qt.DateFormat
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.DateFormat.TextDate.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::fromString(QStringView string, Qt::DateFormat
    #      format)
    address = Rituals.call(
        'ritual_ZN9QDateTime10fromStringE11QStringViewN2Qt10DateFormatE',
        string, format.value,
    )
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(str, str, int)
  def fromString(string: str, format: str, baseYear: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::fromString(QStringView string,
    QStringView format, int baseYear)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#fromString

    Parameters
    ----------

    string : str
      Passed on as it is: a QString is made of it for the call.

    format : str
      Passed on as it is: a QString is made of it for the call.

    baseYear : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::fromString(QStringView string, QStringView
    #      format, int baseYear)
    address = Rituals.call(
        'ritual_ZN9QDateTime10fromStringE11QStringViewS0_i',
        string, format, baseYear,
    )
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(int, Qt.TimeSpec)
  @overload(int, Qt.TimeSpec, int)
  def fromMSecsSinceEpoch(
      msecs: int,
      spec: Qt.TimeSpec,
      offsetFromUtc: int = 0,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs,
    Qt::TimeSpec spec, int offsetFromUtc)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#fromMSecsSinceEpoch

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    spec : Qt.TimeSpec
      Passed on as its number.

    offsetFromUtc : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs, Qt::TimeSpec
    #      spec, int offsetFromUtc)
    address = Rituals.call(
        'ritual_ZN9QDateTime19fromMSecsSinceEpochExN2Qt8TimeSpecEi',
        msecs, spec.value, offsetFromUtc,
    )
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromMSecsSinceEpoch(msecs: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#fromMSecsSinceEpoch

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::fromMSecsSinceEpoch(qint64 msecs)
    address = Rituals.call(
        'ritual_ZN9QDateTime19fromMSecsSinceEpochEx', msecs,
    )
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(int, Qt.TimeSpec)
  @overload(int, Qt.TimeSpec, int)
  def fromSecsSinceEpoch(
      secs: int,
      spec: Qt.TimeSpec,
      offsetFromUtc: int = 0,
  ) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs,
    Qt::TimeSpec spec, int offsetFromUtc)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#fromSecsSinceEpoch

    Parameters
    ----------

    secs : int
      Passed on as it is.

    spec : Qt.TimeSpec
      Passed on as its number.

    offsetFromUtc : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs, Qt::TimeSpec
    #      spec, int offsetFromUtc)
    address = Rituals.call(
        'ritual_ZN9QDateTime18fromSecsSinceEpochExN2Qt8TimeSpecEi',
        secs, spec.value, offsetFromUtc,
    )
    return QDateTime._cuteOwning(address)

  @staticmethod
  @overload(int)
  def fromSecsSinceEpoch(secs: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#fromSecsSinceEpoch

    Parameters
    ----------

    secs : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::fromSecsSinceEpoch(qint64 secs)
    address = Rituals.call('ritual_ZN9QDateTime18fromSecsSinceEpochEx', secs)
    return QDateTime._cuteOwning(address)

  @staticmethod
  def currentMSecsSinceEpoch() -> int:
    """
    Calls Qt's 'qint64 QDateTime::currentMSecsSinceEpoch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetime.html#currentMSecsSinceEpoch
    """
    #  qint64 QDateTime::currentMSecsSinceEpoch()
    return Rituals.call('ritual_ZN9QDateTime22currentMSecsSinceEpochEv')

  @staticmethod
  def currentSecsSinceEpoch() -> int:
    """
    Calls Qt's 'qint64 QDateTime::currentSecsSinceEpoch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetime.html#currentSecsSinceEpoch
    """
    #  qint64 QDateTime::currentSecsSinceEpoch()
    return Rituals.call('ritual_ZN9QDateTime21currentSecsSinceEpochEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDateTime'

  #  Qt's '~QDateTime()'. Naming it makes this a value class: Python owns
  #  every C++ QDateTime behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QDateTimeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDateTime::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#isNull
    """
    #  bool QDateTime::isNull() const
    return self.uglySide.call('ritual_ZNK9QDateTime6isNullEv')

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QDateTime::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#isValid
    """
    #  bool QDateTime::isValid() const
    return self.uglySide.call('ritual_ZNK9QDateTime7isValidEv')

  def timeSpec(self) -> Qt.TimeSpec:
    """
    Calls Qt's 'Qt::TimeSpec QDateTime::timeSpec() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#timeSpec

    Returns
    -------

    Qt.TimeSpec
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimeSpec(number)'
      gives.
    """
    #  Qt::TimeSpec QDateTime::timeSpec() const
    return Qt.TimeSpec(self.uglySide.call('ritual_ZNK9QDateTime8timeSpecEv'))

  def offsetFromUtc(self) -> int:
    """
    Calls Qt's 'int QDateTime::offsetFromUtc() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#offsetFromUtc
    """
    #  int QDateTime::offsetFromUtc() const
    return self.uglySide.call('ritual_ZNK9QDateTime13offsetFromUtcEv')

  def timeZoneAbbreviation(self) -> str:
    """
    Calls Qt's 'QString QDateTime::timeZoneAbbreviation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdatetime.html#timeZoneAbbreviation

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTime::timeZoneAbbreviation() const
    return self.uglySide.call('ritual_ZNK9QDateTime20timeZoneAbbreviationEv')

  def isDaylightTime(self) -> bool:
    """
    Calls Qt's 'bool QDateTime::isDaylightTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#isDaylightTime
    """
    #  bool QDateTime::isDaylightTime() const
    return self.uglySide.call('ritual_ZNK9QDateTime14isDaylightTimeEv')

  def toMSecsSinceEpoch(self) -> int:
    """
    Calls Qt's 'qint64 QDateTime::toMSecsSinceEpoch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toMSecsSinceEpoch
    """
    #  qint64 QDateTime::toMSecsSinceEpoch() const
    return self.uglySide.call('ritual_ZNK9QDateTime17toMSecsSinceEpochEv')

  def toSecsSinceEpoch(self) -> int:
    """
    Calls Qt's 'qint64 QDateTime::toSecsSinceEpoch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toSecsSinceEpoch
    """
    #  qint64 QDateTime::toSecsSinceEpoch() const
    return self.uglySide.call('ritual_ZNK9QDateTime16toSecsSinceEpochEv')

  @overload()
  @overload(Qt.DateFormat)
  def toString(self, format: Qt.DateFormat = Qt.DateFormat.TextDate) -> str:
    """
    Calls Qt's 'QString QDateTime::toString(Qt::DateFormat format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toString

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
    #  QString QDateTime::toString(Qt::DateFormat format) const
    return self.uglySide.call(
        'ritual_ZNK9QDateTime8toStringEN2Qt10DateFormatE', format.value,
    )

  @overload(str)
  def toString(self, format: str) -> str:
    """
    Calls Qt's 'QString QDateTime::toString(const QString &format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toString

    Parameters
    ----------

    format : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDateTime::toString(const QString &format) const
    return self.uglySide.call(
        'ritual_ZNK9QDateTime8toStringERK7QString', format,
    )

  @overload(int)
  def addDays(self, days: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::addDays(qint64 days) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#addDays

    Parameters
    ----------

    days : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::addDays(qint64 days) const
    address = self.uglySide.call('ritual_ZNK9QDateTime7addDaysEx', days)
    return QDateTime._cuteOwning(address)

  @overload(int)
  def addMonths(self, months: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::addMonths(int months) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#addMonths

    Parameters
    ----------

    months : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::addMonths(int months) const
    address = self.uglySide.call('ritual_ZNK9QDateTime9addMonthsEi', months)
    return QDateTime._cuteOwning(address)

  @overload(int)
  def addYears(self, years: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::addYears(int years) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#addYears

    Parameters
    ----------

    years : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::addYears(int years) const
    address = self.uglySide.call('ritual_ZNK9QDateTime8addYearsEi', years)
    return QDateTime._cuteOwning(address)

  @overload(int)
  def addSecs(self, secs: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::addSecs(qint64 secs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#addSecs

    Parameters
    ----------

    secs : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::addSecs(qint64 secs) const
    address = self.uglySide.call('ritual_ZNK9QDateTime7addSecsEx', secs)
    return QDateTime._cuteOwning(address)

  @overload(int)
  def addMSecs(self, msecs: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::addMSecs(qint64 msecs) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#addMSecs

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::addMSecs(qint64 msecs) const
    address = self.uglySide.call('ritual_ZNK9QDateTime8addMSecsEx', msecs)
    return QDateTime._cuteOwning(address)

  @overload(Qt.TimeSpec)
  def toTimeSpec(self, spec: Qt.TimeSpec) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::toTimeSpec(Qt::TimeSpec spec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toTimeSpec

    Parameters
    ----------

    spec : Qt.TimeSpec
      Passed on as its number.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::toTimeSpec(Qt::TimeSpec spec) const
    address = self.uglySide.call(
        'ritual_ZNK9QDateTime10toTimeSpecEN2Qt8TimeSpecE', spec.value,
    )
    return QDateTime._cuteOwning(address)

  def toLocalTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::toLocalTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toLocalTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::toLocalTime() const
    address = self.uglySide.call('ritual_ZNK9QDateTime11toLocalTimeEv')
    return QDateTime._cuteOwning(address)

  def toUTC(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::toUTC() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toUTC

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::toUTC() const
    address = self.uglySide.call('ritual_ZNK9QDateTime5toUTCEv')
    return QDateTime._cuteOwning(address)

  @overload(int)
  def toOffsetFromUtc(self, offsetSeconds: int) -> QDateTime:
    """
    Calls Qt's 'QDateTime QDateTime::toOffsetFromUtc(int offsetSeconds)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#toOffsetFromUtc

    Parameters
    ----------

    offsetSeconds : int
      Passed on as it is.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QDateTime::toOffsetFromUtc(int offsetSeconds) const
    address = self.uglySide.call(
        'ritual_ZNK9QDateTime15toOffsetFromUtcEi', offsetSeconds,
    )
    return QDateTime._cuteOwning(address)

  @overload(THIS)
  def daysTo(self, a0: QDateTime) -> int:
    """
    Calls Qt's 'qint64 QDateTime::daysTo(const QDateTime &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#daysTo

    Parameters
    ----------

    a0 : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  qint64 QDateTime::daysTo(const QDateTime &a0) const
    return self.uglySide.call(
        'ritual_ZNK9QDateTime6daysToERKS_', self._valueOf(a0),
    )

  @overload(THIS)
  def secsTo(self, a0: QDateTime) -> int:
    """
    Calls Qt's 'qint64 QDateTime::secsTo(const QDateTime &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#secsTo

    Parameters
    ----------

    a0 : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  qint64 QDateTime::secsTo(const QDateTime &a0) const
    return self.uglySide.call(
        'ritual_ZNK9QDateTime6secsToERKS_', self._valueOf(a0),
    )

  @overload(THIS)
  def msecsTo(self, a0: QDateTime) -> int:
    """
    Calls Qt's 'qint64 QDateTime::msecsTo(const QDateTime &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#msecsTo

    Parameters
    ----------

    a0 : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  qint64 QDateTime::msecsTo(const QDateTime &a0) const
    return self.uglySide.call(
        'ritual_ZNK9QDateTime7msecsToERKS_', self._valueOf(a0),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.TimeSpec)
  def setTimeSpec(self, spec: Qt.TimeSpec) -> None:
    """
    Calls Qt's 'void QDateTime::setTimeSpec(Qt::TimeSpec spec)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#setTimeSpec

    Parameters
    ----------

    spec : Qt.TimeSpec
      Passed on as its number.
    """
    #  void QDateTime::setTimeSpec(Qt::TimeSpec spec)
    self.uglySide.call(
        'ritual_ZN9QDateTime11setTimeSpecEN2Qt8TimeSpecE', spec.value,
    )

  @overload(int)
  def setOffsetFromUtc(self, offsetSeconds: int) -> None:
    """
    Calls Qt's 'void QDateTime::setOffsetFromUtc(int offsetSeconds)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#setOffsetFromUtc

    Parameters
    ----------

    offsetSeconds : int
      Passed on as it is.
    """
    #  void QDateTime::setOffsetFromUtc(int offsetSeconds)
    self.uglySide.call(
        'ritual_ZN9QDateTime16setOffsetFromUtcEi', offsetSeconds,
    )

  @overload(int)
  def setMSecsSinceEpoch(self, msecs: int) -> None:
    """
    Calls Qt's 'void QDateTime::setMSecsSinceEpoch(qint64 msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#setMSecsSinceEpoch

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QDateTime::setMSecsSinceEpoch(qint64 msecs)
    self.uglySide.call('ritual_ZN9QDateTime18setMSecsSinceEpochEx', msecs)

  @overload(int)
  def setSecsSinceEpoch(self, secs: int) -> None:
    """
    Calls Qt's 'void QDateTime::setSecsSinceEpoch(qint64 secs)'.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#setSecsSinceEpoch

    Parameters
    ----------

    secs : int
      Passed on as it is.
    """
    #  void QDateTime::setSecsSinceEpoch(qint64 secs)
    self.uglySide.call('ritual_ZN9QDateTime17setSecsSinceEpochEx', secs)

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
    Notes what was given, for Qt's 'QDateTime::QDateTime()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#QDateTime
    """
    #  QDateTime::QDateTime()
    self._noteCreation(QDateTime, lambda: Rituals.call(
        'ritual_ZN9QDateTimeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QDateTime) -> None:
    """
    Notes what was given, for Qt's 'QDateTime::QDateTime(const QDateTime
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdatetime.html#QDateTime

    Parameters
    ----------

    other : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.
    """
    #  QDateTime::QDateTime(const QDateTime &other)
    self._noteCreation(QDateTime, lambda: Rituals.call(
        'ritual_ZN9QDateTimeC1ERKS_', self._valueOf(other),
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
