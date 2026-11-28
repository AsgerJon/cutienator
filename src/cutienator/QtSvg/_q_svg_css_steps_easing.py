"""
QSvgCssStepsEasing binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvgcsseasing_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgCssStepsEasing to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSvgCssValues, QSvgCssEasing


class QSvgCssStepsEasing(QSvgCssEasing):
  """
  The cute side of Qt's QSvgCssStepsEasing: a plain Python object standing in
  front of one C++ QSvgCssStepsEasing.

  It is built on the cute 'QSvgCssEasing', as Qt's QSvgCssStepsEasing is
  built on Qt's QSvgCssEasing, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgCssStepsEasing that has a ritual and that Python
  can call so far, 3 names in all: 'progress', 'stops', 'stepPosition'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgCssStepsEasing::~QSvgCssStepsEasing()': the destructor: Python
    never removes a C++ QSvgCssStepsEasing.

  What to expect
  --------------

  - The C++ QSvgCssStepsEasing is created at the first use, not by
    'QSvgCssStepsEasing(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgCssStepsEasing.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgCssStepsEasing'

  #  A C++ QSvgCssStepsEasing Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgCssStepsEasing'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def progress(self, t: float) -> float:
    """
    Calls Qt's 'qreal QSvgCssStepsEasing::progress(qreal t) const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcssstepseasing.html#progress

    Parameters
    ----------

    t : float
      Passed on as it is.
    """
    #  qreal QSvgCssStepsEasing::progress(qreal t) const
    ritual = 'ritual_ZNK18QSvgCssStepsEasing8progressEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSvgCssStepsEasing8progressEd'
    return self.uglySide.call(ritual, t)

  def stops(self) -> int:
    """
    Calls Qt's 'quint32 QSvgCssStepsEasing::stops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsvgcssstepseasing.html#stops
    """
    #  quint32 QSvgCssStepsEasing::stops() const
    return self.uglySide.call('ritual_ZNK18QSvgCssStepsEasing5stopsEv')

  def stepPosition(self) -> QSvgCssValues.StepPosition:
    """
    Calls Qt's 'QSvgCssValues::StepPosition
    QSvgCssStepsEasing::stepPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcssstepseasing.html#stepPosition

    Returns
    -------

    QSvgCssValues.StepPosition
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QSvgCssValues.StepPosition(number)' gives.
    """
    #  QSvgCssValues::StepPosition QSvgCssStepsEasing::stepPosition() const
    return QSvgCssValues.StepPosition(self.uglySide.call(
        'ritual_ZNK18QSvgCssStepsEasing12stepPositionEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, QSvgCssValues.StepPosition)
  def __init__(
      self,
      stops: int,
      position: QSvgCssValues.StepPosition,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSvgCssStepsEasing::QSvgCssStepsEasing(quint32 stops,
    QSvgCssValues::StepPosition position)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvgcssstepseasing.html#QSvgCssStepsEasing

    Parameters
    ----------

    stops : int
      Passed on as it is.

    position : QSvgCssValues.StepPosition
      Passed on as its number.
    """
    #  QSvgCssStepsEasing::QSvgCssStepsEasing(quint32 stops,
    #      QSvgCssValues::StepPosition position)
    self._noteCreation(QSvgCssStepsEasing, lambda: Rituals.call(
        'ritual_ZN18QSvgCssStepsEasingC1EjN13QSvgCssValues12StepPositionE',
        stops, position.value,
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
