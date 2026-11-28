"""
QSvgAnimationController binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgAnimationController to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSvgAbstractAnimator


class QSvgAnimationController(QSvgAbstractAnimator):
  """
  The cute side of Qt's QSvgAnimationController: a plain Python object
  standing in front of one C++ QSvgAnimationController.

  It is built on the cute 'QSvgAbstractAnimator', as Qt's
  QSvgAnimationController is built on Qt's QSvgAbstractAnimator, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgAnimationController that has a ritual and that
  Python can call so far, 3 names in all: 'restartAnimation',
  'currentElapsed', 'setAnimatorTime'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimationController::~QSvgAnimationController()': the
    destructor: Python never removes a C++ QSvgAnimationController.

  What to expect
  --------------

  - The C++ QSvgAnimationController is created at the first use, not by
    'QSvgAnimationController(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAnimationController.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimationController'

  #  A C++ QSvgAnimationController Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAnimationController'

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

  @overload(int)
  def setAnimatorTime(self, time: int) -> None:
    """
    Calls Qt's 'void QSvgAnimationController::setAnimatorTime(qint64 time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimationcontroller.html#setAnimatorTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QSvgAnimationController::setAnimatorTime(qint64 time)
    ritual = 'ritual_ZN23QSvgAnimationController15setAnimatorTimeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSvgAnimationController15setAnimatorTimeEx'
    self.uglySide.call(ritual, time)

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
    Notes what was given, for Qt's
    'QSvgAnimationController::QSvgAnimationController()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimationcontroller.html
    """
    #  QSvgAnimationController::QSvgAnimationController()
    self._noteCreation(QSvgAnimationController, lambda: Rituals.call(
        'ritual_ZN23QSvgAnimationControllerC1Ev',
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

  def restartAnimation(self) -> None:
    """
    Calls Qt's 'void QSvgAnimationController::restartAnimation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimationcontroller.html#restartAnimation
    """
    #  void QSvgAnimationController::restartAnimation()
    ritual = 'ritual_ZN23QSvgAnimationController16restartAnimationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSvgAnimationController16restartAnimationEv'
    self.uglySide.call(ritual)

  def currentElapsed(self) -> int:
    """
    Calls Qt's 'qint64 QSvgAnimationController::currentElapsed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsvganimationcontroller.html#currentElapsed
    """
    #  qint64 QSvgAnimationController::currentElapsed()
    ritual = 'ritual_ZN23QSvgAnimationController14currentElapsedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QSvgAnimationController14currentElapsedEv'
    return self.uglySide.call(ritual)
