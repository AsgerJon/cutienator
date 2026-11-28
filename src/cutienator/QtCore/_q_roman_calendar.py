"""
QRomanCalendar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qromancalendar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QRomanCalendar to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QCalendarBackend, QLocale

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QCalendarLocale


class QRomanCalendar(QCalendarBackend):
  """
  The cute side of Qt's QRomanCalendar: a plain Python object standing in
  front of one C++ QRomanCalendar.

  It is built on the cute 'QCalendarBackend', as Qt's QRomanCalendar is built
  on Qt's QCalendarBackend, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QRomanCalendar that has a ritual and that Python can
  call so far, 8 names in all: 'daysInMonth', 'minimumDaysInMonth',
  'isLunar', 'isLuniSolar', 'isSolar', 'monthName', 'standaloneMonthName',
  'localeMonthIndexData'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const char16_t *QRomanCalendar::localeMonthData() const': gives
    'unsigned short', which has no cute class yet.

  What to expect
  --------------

  - The C++ QRomanCalendar is created at the first use, not by
    'QRomanCalendar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRomanCalendar.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QRomanCalendar'

  #  A C++ QRomanCalendar Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QRomanCalendar'

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
    Calls Qt's 'int QRomanCalendar::daysInMonth(int month, int year) const'.

    Qt's own words: https://doc.qt.io/qt-6/qromancalendar.html#daysInMonth

    Parameters
    ----------

    month : int
      Passed on as it is.

    year : int
      Passed on as it is.
    """
    #  int QRomanCalendar::daysInMonth(int month, int year) const
    ritual = 'ritual_ZNK14QRomanCalendar11daysInMonthEii'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QRomanCalendar11daysInMonthEii'
    return self.uglySide.call(ritual, month, year)

  def minimumDaysInMonth(self) -> int:
    """
    Calls Qt's 'int QRomanCalendar::minimumDaysInMonth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qromancalendar.html#minimumDaysInMonth
    """
    #  int QRomanCalendar::minimumDaysInMonth() const
    ritual = 'ritual_ZNK14QRomanCalendar18minimumDaysInMonthEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QRomanCalendar18minimumDaysInMonthEv'
    return self.uglySide.call(ritual)

  def isLunar(self) -> bool:
    """
    Calls Qt's 'bool QRomanCalendar::isLunar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qromancalendar.html#isLunar
    """
    #  bool QRomanCalendar::isLunar() const
    ritual = 'ritual_ZNK14QRomanCalendar7isLunarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QRomanCalendar7isLunarEv'
    return self.uglySide.call(ritual)

  def isLuniSolar(self) -> bool:
    """
    Calls Qt's 'bool QRomanCalendar::isLuniSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qromancalendar.html#isLuniSolar
    """
    #  bool QRomanCalendar::isLuniSolar() const
    ritual = 'ritual_ZNK14QRomanCalendar11isLuniSolarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QRomanCalendar11isLuniSolarEv'
    return self.uglySide.call(ritual)

  def isSolar(self) -> bool:
    """
    Calls Qt's 'bool QRomanCalendar::isSolar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qromancalendar.html#isSolar
    """
    #  bool QRomanCalendar::isSolar() const
    ritual = 'ritual_ZNK14QRomanCalendar7isSolarEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QRomanCalendar7isSolarEv'
    return self.uglySide.call(ritual)

  @overload(QLocale, int, int, QLocale.FormatType)
  def monthName(
      self,
      locale: QLocale,
      month: int,
      year: int,
      format: QLocale.FormatType,
  ) -> str:
    """
    Calls Qt's 'QString QRomanCalendar::monthName(const QLocale &locale, int
    month, int year, QLocale::FormatType format) const'.

    Qt's own words: https://doc.qt.io/qt-6/qromancalendar.html#monthName

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
    #  QString QRomanCalendar::monthName(const QLocale &locale, int month,
    #      int year, QLocale::FormatType format) const
    ritual = (
        'ritual_ZNK14QRomanCalendar9monthNameERK7QLocaleiiNS0_10FormatTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QRomanCalendar9monthNameERK7QLocaleiiNS0_10Forma'
          'tTypeE')
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
    Calls Qt's 'QString QRomanCalendar::standaloneMonthName(const QLocale
    &locale, int month, int year, QLocale::FormatType format) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qromancalendar.html#standaloneMonthName

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
    #  QString QRomanCalendar::standaloneMonthName(const QLocale &locale, int
    #      month, int year, QLocale::FormatType format) const
    ritual = (
        'ritual_ZNK14QRomanCalendar19standaloneMonthNameERK7QLocaleiiNS0_10'
        'FormatTypeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK14QRomanCalendar19standaloneMonthNameERK7QLocaleii'
          'NS0_10FormatTypeE')
    return self.uglySide.call(
        ritual, self._valueOf(locale), month, year, format.value,
    )

  def localeMonthIndexData(self) -> Optional[QCalendarLocale]:
    """
    Calls Qt's 'const QCalendarLocale *QRomanCalendar::localeMonthIndexData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qromancalendar.html#localeMonthIndexData

    Returns
    -------

    Optional[QCalendarLocale]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QCalendarLocale *QRomanCalendar::localeMonthIndexData() const
    ritual = 'ritual_ZNK14QRomanCalendar20localeMonthIndexDataEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK14QRomanCalendar20localeMonthIndexDataEv'
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
