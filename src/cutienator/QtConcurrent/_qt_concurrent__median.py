"""
QtConcurrent::Median binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtConcurrent/qtconcurrentmedian.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class Median(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtConcurrent::Median: a plain Python object standing
  in front of one C++ QtConcurrent::Median.

  C++ hands a QtConcurrent::Median around as a copy, so every C++
  QtConcurrent::Median behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QtConcurrent::Median that has a ritual and that
  Python can call so far, 4 names in all: 'reset', 'addValue',
  'isMedianValid', 'median'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtConcurrent::Median::~Median()': the destructor: Python removes
    its C++ QtConcurrent::Median by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QtConcurrent::Median is created at the first use, not by
    'QtConcurrent::Median(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtConcurrent::Median back gives a copy the ritual
    made for Python, in a new cute QtConcurrent::Median.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtConcurrent::Median'

  #  Qt's '~QtConcurrent::Median()'. Naming it makes this a value class:
  #  Python owns every C++ QtConcurrent::Median behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN12QtConcurrent6MedianD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isMedianValid(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::Median::isMedianValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-median.html#isMedianValid
    """
    #  bool QtConcurrent::Median::isMedianValid() const
    return self.uglySide.call(
        'ritual_ZNK12QtConcurrent6Median13isMedianValidEv',
    )

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QtConcurrent::Median::Median()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtconcurrent-median.html#Median
    """
    #  QtConcurrent::Median::Median()
    self._noteCreation(Median, lambda: Rituals.call(
        'ritual_ZN12QtConcurrent6MedianC1Ev',
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

  def reset(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::Median::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qtconcurrent-median.html#reset
    """
    #  void QtConcurrent::Median::reset()
    self.uglySide.call('ritual_ZN12QtConcurrent6Median5resetEv')

  @overload(float)
  def addValue(self, value: float) -> None:
    """
    Calls Qt's 'void QtConcurrent::Median::addValue(double value)'.

    Qt's own words: https://doc.qt.io/qt-6/qtconcurrent-median.html#addValue

    Parameters
    ----------

    value : float
      Passed on as it is.
    """
    #  void QtConcurrent::Median::addValue(double value)
    self.uglySide.call('ritual_ZN12QtConcurrent6Median8addValueEd', value)

  def median(self) -> float:
    """
    Calls Qt's 'double QtConcurrent::Median::median()'.

    Qt's own words: https://doc.qt.io/qt-6/qtconcurrent-median.html#median
    """
    #  double QtConcurrent::Median::median()
    return self.uglySide.call('ritual_ZN12QtConcurrent6Median6medianEv')
