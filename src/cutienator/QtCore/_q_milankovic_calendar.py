"""
QMilankovicCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qmilankoviccalendar_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QMilankovicCalendar to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QCalendar, QRomanCalendar, QStringList


class QMilankovicCalendar(QRomanCalendar):
  """
  The cute side of Qt's QMilankovicCalendar: a plain Python object standing
  in front of one C++ QMilankovicCalendar.

  It is built on the cute 'QRomanCalendar', as Qt's QMilankovicCalendar is
  built on Qt's QRomanCalendar, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMilankovicCalendar that has a ritual and that
  Python can call so far, 4 names in all: 'name', 'nameList', 'isLeapYear',
  'julianDayToDate'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QMilankovicCalendar::dateToJulianDay(int year, int month, int
    day, qint64 *jd) const': takes a number to change where it is.

  What to expect
  --------------

  - The C++ QMilankovicCalendar is created at the first use, not by
    'QMilankovicCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMilankovicCalendar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def nameList() -> QStringList:
    """
    Calls Qt's 'QStringList QMilankovicCalendar::nameList()'.

    Qt's own words: https://doc.qt.io/qt-6/qmilankoviccalendar.html#nameList

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QMilankovicCalendar::nameList()
    address = Rituals.call('ritual_ZN19QMilankovicCalendar8nameListEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMilankovicCalendar'

  #  A C++ QMilankovicCalendar Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMilankovicCalendar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QMilankovicCalendar::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmilankoviccalendar.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QMilankovicCalendar::name() const
    ritual = 'ritual_ZNK19QMilankovicCalendar4nameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QMilankovicCalendar4nameEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def isLeapYear(self, year: int) -> bool:
    """
    Calls Qt's 'bool QMilankovicCalendar::isLeapYear(int year) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmilankoviccalendar.html#isLeapYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  bool QMilankovicCalendar::isLeapYear(int year) const
    ritual = 'ritual_ZNK19QMilankovicCalendar10isLeapYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QMilankovicCalendar10isLeapYearEi'
    return self.uglySide.call(ritual, year)

  @overload(int)
  def julianDayToDate(self, jd: int) -> QCalendar.YearMonthDay:
    """
    Calls Qt's 'QCalendar::YearMonthDay
    QMilankovicCalendar::julianDayToDate(qint64 jd) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmilankoviccalendar.html#julianDayToDate

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
    #  QCalendar::YearMonthDay QMilankovicCalendar::julianDayToDate(qint64
    #      jd) const
    ritual = 'ritual_ZNK19QMilankovicCalendar15julianDayToDateEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QMilankovicCalendar15julianDayToDateEx'
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
