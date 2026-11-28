"""
QJalaliCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qjalalicalendar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QJalaliCalendar to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QCalendar, QCalendarBackend, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCalendarLocale


class QJalaliCalendar(QCalendarBackend):
  """
  The cute side of Qt's QJalaliCalendar: a plain Python object standing in
  front of one C++ QJalaliCalendar.

  It is built on the cute 'QCalendarBackend', as Qt's QJalaliCalendar is
  built on Qt's QCalendarBackend, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QJalaliCalendar that has a ritual and that Python
  can call so far, 9 names in all: 'name', 'nameList', 'daysInMonth',
  'isLeapYear', 'isLunar', 'isLuniSolar', 'isSolar', 'julianDayToDate',
  'localeMonthIndexData'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QJalaliCalendar::dateToJulianDay(int year, int month, int day,
    qint64 *jd) const': takes a number to change where it is.
  - Qt's 'const char16_t *QJalaliCalendar::localeMonthData() const': gives
    'unsigned short', which has no cute class yet.

  What to expect
  --------------

  - The C++ QJalaliCalendar is created at the first use, not by
    'QJalaliCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QJalaliCalendar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def nameList() -> QStringList:
    """
    Calls Qt's 'QStringList QJalaliCalendar::nameList()'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#nameList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QJalaliCalendar::nameList()
    address = Rituals.call('ritual_ZN15QJalaliCalendar8nameListEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QJalaliCalendar'

  #  A C++ QJalaliCalendar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QJalaliCalendar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QJalaliCalendar::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QJalaliCalendar::name() const
    ritual = 'ritual_ZNK15QJalaliCalendar4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar4nameEv'
    return self.uglySide.call(ritual)

  @overload(int, int)
  def daysInMonth(self, month: int, year: int) -> int:
    """
    Calls Qt's 'int QJalaliCalendar::daysInMonth(int month, int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#daysInMonth

    Parameters
    ----------

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.
    """
    #  int QJalaliCalendar::daysInMonth(int month, int year) const
    ritual = 'ritual_ZNK15QJalaliCalendar11daysInMonthEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar11daysInMonthEii'
    return self.uglySide.call(ritual, month, year)

  @overload(int)
  def isLeapYear(self, year: int) -> bool:
    """
    Calls Qt's 'bool QJalaliCalendar::isLeapYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QJalaliCalendar::isLeapYear(int year) const
    ritual = 'ritual_ZNK15QJalaliCalendar10isLeapYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar10isLeapYearEi'
    return self.uglySide.call(ritual, year)

  def isLunar(self) -> bool:
    """
    Calls Qt's 'bool QJalaliCalendar::isLunar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#isLunar
    """
    #  bool QJalaliCalendar::isLunar() const
    ritual = 'ritual_ZNK15QJalaliCalendar7isLunarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar7isLunarEv'
    return self.uglySide.call(ritual)

  def isLuniSolar(self) -> bool:
    """
    Calls Qt's 'bool QJalaliCalendar::isLuniSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#isLuniSolar
    """
    #  bool QJalaliCalendar::isLuniSolar() const
    ritual = 'ritual_ZNK15QJalaliCalendar11isLuniSolarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar11isLuniSolarEv'
    return self.uglySide.call(ritual)

  def isSolar(self) -> bool:
    """
    Calls Qt's 'bool QJalaliCalendar::isSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qjalalicalendar.html#isSolar
    """
    #  bool QJalaliCalendar::isSolar() const
    ritual = 'ritual_ZNK15QJalaliCalendar7isSolarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar7isSolarEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def julianDayToDate(self, jd: int) -> QCalendar.YearMonthDay:
    """
    Calls Qt's 'QCalendar::YearMonthDay
    QJalaliCalendar::julianDayToDate(qint64 jd) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjalalicalendar.html#julianDayToDate

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
    #  QCalendar::YearMonthDay QJalaliCalendar::julianDayToDate(qint64 jd)
    #      const
    ritual = 'ritual_ZNK15QJalaliCalendar15julianDayToDateEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar15julianDayToDateEx'
    address = self.uglySide.call(ritual, jd)
    return QCalendar.YearMonthDay._cuteOwning(address)

  def localeMonthIndexData(self) -> Optional[QCalendarLocale]:
    """
    Calls Qt's 'const QCalendarLocale
    *QJalaliCalendar::localeMonthIndexData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qjalalicalendar.html#localeMonthIndexData

    Returns
    -------

    Optional[QCalendarLocale]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarLocale *QJalaliCalendar::localeMonthIndexData() const
    ritual = 'ritual_ZNK15QJalaliCalendar20localeMonthIndexDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QJalaliCalendar20localeMonthIndexDataEv'
    address = self.uglySide.call(ritual)
    from . import QCalendarLocale
    return QCalendarLocale._cuteAt(address)

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
