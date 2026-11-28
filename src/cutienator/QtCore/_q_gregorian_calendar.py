"""
QGregorianCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qgregoriancalendar_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QGregorianCalendar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QCalendar, QRomanCalendar, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QDate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDate = WAIT['QDate']


class QGregorianCalendar(QRomanCalendar):
  """
  The cute side of Qt's QGregorianCalendar: a plain Python object standing in
  front of one C++ QGregorianCalendar.

  It is built on the cute 'QRomanCalendar', as Qt's QGregorianCalendar is
  built on Qt's QRomanCalendar, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QGregorianCalendar that has a ritual and that Python
  can call so far, 12 names in all: 'name', 'nameList', 'isLeapYear',
  'julianDayToDate', 'matchCenturyToWeekday', 'weekDayOfJulian', 'leapTest',
  'monthLength', 'validParts', 'partsFromJulian', 'yearStartWeekDay',
  'yearSharingWeekDays'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QGregorianCalendar::dateToJulianDay(int year, int month, int
    day, qint64 *jd) const': takes a number to change where it is.
  - Qt's 'std::optional<qint64> QGregorianCalendar::julianFromParts(int year,
    int month, int day)': gives a type Python has no way to take yet.

  What to expect
  --------------

  - The C++ QGregorianCalendar is created at the first use, not by
    'QGregorianCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QGregorianCalendar.
  - Each name of Qt's QGregorianCalendar that has no cute function yet,
    'julianFromParts', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def nameList() -> QStringList:
    """
    Calls Qt's 'QStringList QGregorianCalendar::nameList()'.

    Qt's own words: https://doc.qt.io/qt-6/qgregoriancalendar.html#nameList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QGregorianCalendar::nameList()
    address = Rituals.call('ritual_ZN18QGregorianCalendar8nameListEv')
    return QStringList._cuteOwning(address)

  @staticmethod
  @overload(int)
  def weekDayOfJulian(jd: int) -> int:
    """
    Calls Qt's 'int QGregorianCalendar::weekDayOfJulian(qint64 jd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#weekDayOfJulian

    Parameters
    ----------

    jd : int
      Passed on as it is.
    """
    #  int QGregorianCalendar::weekDayOfJulian(qint64 jd)
    return Rituals.call(
        'ritual_ZN18QGregorianCalendar15weekDayOfJulianEx', jd,
    )

  @staticmethod
  @overload(int)
  def leapTest(year: int) -> bool:
    """
    Calls Qt's 'bool QGregorianCalendar::leapTest(int year)'.

    Qt's own words: https://doc.qt.io/qt-6/qgregoriancalendar.html#leapTest

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QGregorianCalendar::leapTest(int year)
    return Rituals.call('ritual_ZN18QGregorianCalendar8leapTestEi', year)

  @staticmethod
  @overload(int, int)
  def monthLength(month: int, year: int) -> int:
    """
    Calls Qt's 'int QGregorianCalendar::monthLength(int month, int year)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#monthLength

    Parameters
    ----------

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.
    """
    #  int QGregorianCalendar::monthLength(int month, int year)
    return Rituals.call(
        'ritual_ZN18QGregorianCalendar11monthLengthEii', month, year,
    )

  @staticmethod
  @overload(int, int, int)
  def validParts(year: int, month: int, day: int) -> bool:
    """
    Calls Qt's 'bool QGregorianCalendar::validParts(int year, int month, int
    day)'.

    Qt's own words: https://doc.qt.io/qt-6/qgregoriancalendar.html#validParts

    Parameters
    ----------

    year : int
      Passed on as it is.

    month : int
      Passed on as it is.

    day : int
      Passed on as it is.
    """
    #  bool QGregorianCalendar::validParts(int year, int month, int day)
    return Rituals.call(
        'ritual_ZN18QGregorianCalendar10validPartsEiii', year, month, day,
    )

  @staticmethod
  @overload(int)
  def partsFromJulian(jd: int) -> QCalendar.YearMonthDay:
    """
    Calls Qt's 'QCalendar::YearMonthDay
    QGregorianCalendar::partsFromJulian(qint64 jd)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#partsFromJulian

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
    #  QCalendar::YearMonthDay QGregorianCalendar::partsFromJulian(qint64 jd)
    address = Rituals.call(
        'ritual_ZN18QGregorianCalendar15partsFromJulianEx', jd,
    )
    return QCalendar.YearMonthDay._cuteOwning(address)

  @staticmethod
  @overload(int)
  def yearStartWeekDay(year: int) -> int:
    """
    Calls Qt's 'int QGregorianCalendar::yearStartWeekDay(int year)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#yearStartWeekDay

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  int QGregorianCalendar::yearStartWeekDay(int year)
    return Rituals.call(
        'ritual_ZN18QGregorianCalendar16yearStartWeekDayEi', year,
    )

  @staticmethod
  @overload(QDate)
  def yearSharingWeekDays(date: QDate) -> int:
    """
    Calls Qt's 'int QGregorianCalendar::yearSharingWeekDays(QDate date)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#yearSharingWeekDays

    Parameters
    ----------

    date : QDate
      Passed on as a value: Qt reads the C++ QDate, which stays Python's own.
    """
    #  int QGregorianCalendar::yearSharingWeekDays(QDate date)
    return Rituals.call(
        'ritual_ZN18QGregorianCalendar19yearSharingWeekDaysE5QDate',
        CuteMixin._valueOf(date),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QGregorianCalendar'

  #  A C++ QGregorianCalendar Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QGregorianCalendar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QGregorianCalendar::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qgregoriancalendar.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QGregorianCalendar::name() const
    ritual = 'ritual_ZNK18QGregorianCalendar4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGregorianCalendar4nameEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def isLeapYear(self, year: int) -> bool:
    """
    Calls Qt's 'bool QGregorianCalendar::isLeapYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qgregoriancalendar.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QGregorianCalendar::isLeapYear(int year) const
    ritual = 'ritual_ZNK18QGregorianCalendar10isLeapYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGregorianCalendar10isLeapYearEi'
    return self.uglySide.call(ritual, year)

  @overload(int)
  def julianDayToDate(self, jd: int) -> QCalendar.YearMonthDay:
    """
    Calls Qt's 'QCalendar::YearMonthDay
    QGregorianCalendar::julianDayToDate(qint64 jd) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#julianDayToDate

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
    #  QCalendar::YearMonthDay QGregorianCalendar::julianDayToDate(qint64 jd)
    #      const
    ritual = 'ritual_ZNK18QGregorianCalendar15julianDayToDateEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QGregorianCalendar15julianDayToDateEx'
    address = self.uglySide.call(ritual, jd)
    return QCalendar.YearMonthDay._cuteOwning(address)

  @overload(QCalendar.YearMonthDay, int)
  def matchCenturyToWeekday(
      self,
      parts: QCalendar.YearMonthDay,
      dow: int,
  ) -> int:
    """
    Calls Qt's 'qint64 QGregorianCalendar::matchCenturyToWeekday(const
    QCalendar::YearMonthDay &parts, int dow) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qgregoriancalendar.html#matchCenturyToWeekday

    Parameters
    ----------

    parts : QCalendar.YearMonthDay
      Passed on as a value: Qt reads the C++ QCalendar::YearMonthDay, which
      stays Python's own.

    dow : int
      Passed on as it is.
    """
    #  qint64 QGregorianCalendar::matchCenturyToWeekday(const
    #      QCalendar::YearMonthDay &parts, int dow) const
    ritual = (
        'ritual_ZNK18QGregorianCalendar21matchCenturyToWeekdayERKN9QCalenda'
        'r12YearMonthDayEi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK18QGregorianCalendar21matchCenturyToWeekdayERKN9QC'
          'alendar12YearMonthDayEi')
    return self.uglySide.call(ritual, self._valueOf(parts), dow)

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

  @staticmethod
  def julianFromParts(*__, **_) -> Never:
    """
    Qt's 'std::optional<qint64> QGregorianCalendar::julianFromParts(int year,
    int month, int day)': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QGregorianCalendar.julianFromParts' has no cute function yet. "
        "Qt's 'std::optional<qint64> "
        "QGregorianCalendar::julianFromParts(int year, int month, int "
        "day)': gives a type Python has no way to take yet.")
