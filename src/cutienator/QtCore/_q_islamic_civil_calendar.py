"""
QIslamicCivilCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qislamiccivilcalendar_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QIslamicCivilCalendar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QCalendar, QHijriCalendar, QStringList


class QIslamicCivilCalendar(QHijriCalendar):
  """
  The cute side of Qt's QIslamicCivilCalendar: a plain Python object standing
  in front of one C++ QIslamicCivilCalendar.

  It is built on the cute 'QHijriCalendar', as Qt's QIslamicCivilCalendar is
  built on Qt's QHijriCalendar, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QIslamicCivilCalendar that has a ritual and that
  Python can call so far, 4 names in all: 'name', 'nameList', 'isLeapYear',
  'julianDayToDate'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QIslamicCivilCalendar::dateToJulianDay(int year, int month,
    int day, qint64 *jd) const': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QIslamicCivilCalendar is created at the first use, not by
    'QIslamicCivilCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QIslamicCivilCalendar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def nameList() -> QStringList:
    """
    Calls Qt's 'QStringList QIslamicCivilCalendar::nameList()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qislamiccivilcalendar.html#nameList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QIslamicCivilCalendar::nameList()
    address = Rituals.call('ritual_ZN21QIslamicCivilCalendar8nameListEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QIslamicCivilCalendar'

  #  A C++ QIslamicCivilCalendar Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QIslamicCivilCalendar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QIslamicCivilCalendar::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qislamiccivilcalendar.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QIslamicCivilCalendar::name() const
    ritual = 'ritual_ZNK21QIslamicCivilCalendar4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QIslamicCivilCalendar4nameEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def isLeapYear(self, year: int) -> bool:
    """
    Calls Qt's 'bool QIslamicCivilCalendar::isLeapYear(int year) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qislamiccivilcalendar.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QIslamicCivilCalendar::isLeapYear(int year) const
    ritual = 'ritual_ZNK21QIslamicCivilCalendar10isLeapYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QIslamicCivilCalendar10isLeapYearEi'
    return self.uglySide.call(ritual, year)

  @overload(int)
  def julianDayToDate(self, jd: int) -> QCalendar.YearMonthDay:
    """
    Calls Qt's 'QCalendar::YearMonthDay
    QIslamicCivilCalendar::julianDayToDate(qint64 jd) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qislamiccivilcalendar.html#julianDayToDate

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
    #  QCalendar::YearMonthDay QIslamicCivilCalendar::julianDayToDate(qint64
    #      jd) const
    ritual = 'ritual_ZNK21QIslamicCivilCalendar15julianDayToDateEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QIslamicCivilCalendar15julianDayToDateEx'
    address = self.uglySide.call(ritual, jd)
    return QCalendar.YearMonthDay._cuteOwning(address)

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
