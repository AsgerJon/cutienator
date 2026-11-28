"""
QtTemporalPattern::TemporalField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qttemporalpattern_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QtTemporalPattern::TemporalField to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QtTemporalPattern


class TemporalField(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtTemporalPattern::TemporalField: a plain Python
  object standing in front of one C++ QtTemporalPattern::TemporalField.

  C++ hands a QtTemporalPattern::TemporalField around as a copy, so every C++
  QtTemporalPattern::TemporalField behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QtTemporalPattern::TemporalField that has a ritual
  and that Python can call so far, 3 names in all: 'part', '__eq__',
  '__ne__'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtTemporalPattern::TemporalField::~TemporalField()': the
    destructor: Python removes its C++ QtTemporalPattern::TemporalField by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtTemporalPattern::TemporalField is created at the first use, not
    by 'QtTemporalPattern::TemporalField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtTemporalPattern::TemporalField back gives a copy
    the ritual made for Python, in a new cute
    QtTemporalPattern::TemporalField.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtTemporalPattern::TemporalField'

  #  Qt's '~QtTemporalPattern::TemporalField()'. Naming it makes this a value
  #  class: Python owns every C++ QtTemporalPattern::TemporalField behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN17QtTemporalPattern13TemporalFieldD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def part(self) -> QtTemporalPattern.DateTimePart:
    """
    Calls Qt's 'DateTimePart QtTemporalPattern::TemporalField::part() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttemporalpattern-temporalfield.html#part

    Returns
    -------

    QtTemporalPattern.DateTimePart
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtTemporalPattern.DateTimePart(number)' gives.
    """
    #  DateTimePart QtTemporalPattern::TemporalField::part() const
    return QtTemporalPattern.DateTimePart(self.uglySide.call(
        'ritual_ZNK17QtTemporalPattern13TemporalField4partEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: TemporalField) -> bool:
    """
    Calls Qt's 'bool operator==(const TemporalField &lhs, const TemporalField
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttemporalpattern-temporalfield.html#operator==

    Parameters
    ----------

    rhs : TemporalField
      Passed on as a value: Qt reads the C++
      QtTemporalPattern::TemporalField, which stays Python's own.
    """
    #  bool operator==(const TemporalField &lhs, const TemporalField &rhs)
    return Rituals.call(
        'ritual_ZN17QtTemporalPatterneqERKNS_13TemporalFieldES2_',
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
  def __ne__(self, rhs: TemporalField) -> bool:
    """
    Calls Qt's 'bool operator!=(const TemporalField &lhs, const TemporalField
    &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qttemporalpattern-temporalfield.html#operator!=

    Parameters
    ----------

    rhs : TemporalField
      Passed on as a value: Qt reads the C++
      QtTemporalPattern::TemporalField, which stays Python's own.
    """
    #  bool operator!=(const TemporalField &lhs, const TemporalField &rhs)
    return Rituals.call(
        'ritual_ZN17QtTemporalPatternneERKNS_13TemporalFieldES2_',
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
