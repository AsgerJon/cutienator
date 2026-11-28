"""
QCalendarLocale binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qcalendarbackend_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QCalendarLocale to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QLocale, QLocaleData


class QCalendarLocale(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCalendarLocale: a plain Python object standing in
  front of one C++ QCalendarLocale.

  C++ hands a QCalendarLocale around as a copy, so every C++ QCalendarLocale
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCalendarLocale that has a ritual and that Python
  can call so far, 2 names in all: 'monthName', 'standaloneMonthName'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCalendarLocale::~QCalendarLocale()': the destructor: Python
    removes its C++ QCalendarLocale by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QCalendarLocale is created at the first use, not by
    'QCalendarLocale(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCalendarLocale back gives a copy the ritual made for
    Python, in a new cute QCalendarLocale.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCalendarLocale'

  #  Qt's '~QCalendarLocale()'. Naming it makes this a value class: Python
  #  owns every C++ QCalendarLocale behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QCalendarLocaleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QLocale.FormatType)
  def monthName(self, type: QLocale.FormatType) -> QLocaleData.DataRange:
    """
    Calls Qt's 'QLocaleData::DataRange
    QCalendarLocale::monthName(QLocale::FormatType type) const'.

    Qt's own words: https://doc.qt.io/qt-6/qcalendarlocale.html#monthName

    Parameters
    ----------

    type : QLocale.FormatType
      Passed on as its number.

    Returns
    -------

    QLocaleData.DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  QLocaleData::DataRange QCalendarLocale::monthName(QLocale::FormatType
    #      type) const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarLocale9monthNameEN7QLocale10FormatTypeE',
        type.value,
    )
    return QLocaleData.DataRange._cuteOwning(address)

  @overload(QLocale.FormatType)
  def standaloneMonthName(
      self,
      type: QLocale.FormatType,
  ) -> QLocaleData.DataRange:
    """
    Calls Qt's 'QLocaleData::DataRange
    QCalendarLocale::standaloneMonthName(QLocale::FormatType type) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcalendarlocale.html#standaloneMonthName

    Parameters
    ----------

    type : QLocale.FormatType
      Passed on as its number.

    Returns
    -------

    QLocaleData.DataRange
      A new cute QLocaleData::DataRange around the copy Qt gave back. Python
      owns it.
    """
    #  QLocaleData::DataRange
    #      QCalendarLocale::standaloneMonthName(QLocale::FormatType type)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK15QCalendarLocale19standaloneMonthNameEN7QLocale10Format'
        'TypeE',
        type.value,
    )
    return QLocaleData.DataRange._cuteOwning(address)

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
