"""
ScatterAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCharts/6.12.0/QtCharts/private/scatteranimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means ScatterAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import QAbstractAnimation
from . import XYAnimation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ScatterAnimation(XYAnimation):
  """
  The cute side of Qt's ScatterAnimation: a plain Python object standing in
  front of one C++ ScatterAnimation.

  It is built on the cute 'XYAnimation', as Qt's ScatterAnimation is built on
  Qt's XYAnimation, and has everything that class has.

  What exists
  -----------

  Every function of Qt's ScatterAnimation that has a ritual and that Python
  can call so far, 1 name in all: 'updateState'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'ScatterAnimation::ScatterAnimation(ScatterChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
  - Qt's 'ScatterAnimation::~ScatterAnimation()': the destructor: Python
    never removes a C++ ScatterAnimation.

  What to expect
  --------------

  - The C++ ScatterAnimation is created at the first use, not by
    'ScatterAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ ScatterAnimation.
  - Qt tells when it has removed the C++ ScatterAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's ScatterAnimation that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'ScatterAnimation'

  #  A C++ ScatterAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_ScatterAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'ScatterAnimation::ScatterAnimation(ScatterChartItem *item, int
    duration, QEasingCurve &curve)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'ScatterAnimation.__init__' has no cute function yet. Qt's "
        "'ScatterAnimation::ScatterAnimation(ScatterChartItem *item, int "
        "duration, QEasingCurve &curve)': takes a type Python has no way to "
        "hand over yet.")

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

  @overload(QAbstractAnimation.State, QAbstractAnimation.State)
  def updateState(
      self,
      newState: QAbstractAnimation.State,
      oldState: QAbstractAnimation.State,
  ) -> None:
    """
    Calls Qt's 'void ScatterAnimation::updateState(QAbstractAnimation::State
    newState, QAbstractAnimation::State oldState)'.

    Qt's own words: https://doc.qt.io/qt-6/scatteranimation.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimation.State
      Passed on as its number.

    oldState : QAbstractAnimation.State
      Passed on as its number.
    """
    #  void ScatterAnimation::updateState(QAbstractAnimation::State newState,
    #      QAbstractAnimation::State oldState)
    ritual = (
        'ritual_ZN16ScatterAnimation11updateStateEN18QAbstractAnimation5Sta'
        'teES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16ScatterAnimation11updateStateEN18QAbstractAnimati'
          'on5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)
