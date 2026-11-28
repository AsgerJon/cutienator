"""
QHijriCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qhijricalendar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QHijriCalendar to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QCalendarBackend

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCalendarLocale


class QHijriCalendar(QCalendarBackend):
  """
  The cute side of Qt's QHijriCalendar: a plain Python object standing in
  front of one C++ QHijriCalendar.

  It is built on the cute 'QCalendarBackend', as Qt's QHijriCalendar is built
  on Qt's QCalendarBackend, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QHijriCalendar that has a ritual and that Python can
  call so far, 7 names in all: 'daysInMonth', 'maximumDaysInMonth',
  'daysInYear', 'isLunar', 'isLuniSolar', 'isSolar', 'localeMonthIndexData'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const char16_t *QHijriCalendar::localeMonthData() const': gives
    'unsigned short', which has no cute class yet.

  What to expect
  --------------

  - The C++ QHijriCalendar is created at the first use, not by
    'QHijriCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QHijriCalendar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QHijriCalendar'

  #  A C++ QHijriCalendar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QHijriCalendar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def daysInMonth(self, month: int, year: int) -> int:
    """
    Calls Qt's 'int QHijriCalendar::daysInMonth(int month, int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhijricalendar.html#daysInMonth

    Parameters
    ----------

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.
    """
    #  int QHijriCalendar::daysInMonth(int month, int year) const
    ritual = 'ritual_ZNK14QHijriCalendar11daysInMonthEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar11daysInMonthEii'
    return self.uglySide.call(ritual, month, year)

  def maximumDaysInMonth(self) -> int:
    """
    Calls Qt's 'int QHijriCalendar::maximumDaysInMonth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhijricalendar.html#maximumDaysInMonth
    """
    #  int QHijriCalendar::maximumDaysInMonth() const
    ritual = 'ritual_ZNK14QHijriCalendar18maximumDaysInMonthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar18maximumDaysInMonthEv'
    return self.uglySide.call(ritual)

  @overload(int)
  def daysInYear(self, year: int) -> int:
    """
    Calls Qt's 'int QHijriCalendar::daysInYear(int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhijricalendar.html#daysInYear

    Parameters
    ----------

    year : int
      Passed on as it is.
    """
    #  int QHijriCalendar::daysInYear(int year) const
    ritual = 'ritual_ZNK14QHijriCalendar10daysInYearEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar10daysInYearEi'
    return self.uglySide.call(ritual, year)

  def isLunar(self) -> bool:
    """
    Calls Qt's 'bool QHijriCalendar::isLunar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhijricalendar.html#isLunar
    """
    #  bool QHijriCalendar::isLunar() const
    ritual = 'ritual_ZNK14QHijriCalendar7isLunarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar7isLunarEv'
    return self.uglySide.call(ritual)

  def isLuniSolar(self) -> bool:
    """
    Calls Qt's 'bool QHijriCalendar::isLuniSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhijricalendar.html#isLuniSolar
    """
    #  bool QHijriCalendar::isLuniSolar() const
    ritual = 'ritual_ZNK14QHijriCalendar11isLuniSolarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar11isLuniSolarEv'
    return self.uglySide.call(ritual)

  def isSolar(self) -> bool:
    """
    Calls Qt's 'bool QHijriCalendar::isSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhijricalendar.html#isSolar
    """
    #  bool QHijriCalendar::isSolar() const
    ritual = 'ritual_ZNK14QHijriCalendar7isSolarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar7isSolarEv'
    return self.uglySide.call(ritual)

  def localeMonthIndexData(self) -> Optional[QCalendarLocale]:
    """
    Calls Qt's 'const QCalendarLocale *QHijriCalendar::localeMonthIndexData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhijricalendar.html#localeMonthIndexData

    Returns
    -------

    Optional[QCalendarLocale]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarLocale *QHijriCalendar::localeMonthIndexData() const
    ritual = 'ritual_ZNK14QHijriCalendar20localeMonthIndexDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QHijriCalendar20localeMonthIndexDataEv'
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
