"""
QSvgAnimator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSvg/6.12.0/QtSvg/private/qsvganimator_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QSvgAnimator to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSvgAbstractAnimator


class QSvgAnimator(QSvgAbstractAnimator):
  """
  The cute side of Qt's QSvgAnimator: a plain Python object standing in front
  of one C++ QSvgAnimator.

  It is built on the cute 'QSvgAbstractAnimator', as Qt's QSvgAnimator is
  built on Qt's QSvgAbstractAnimator, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSvgAnimator that has a ritual and that Python can
  call so far, 3 names in all: 'restartAnimation', 'currentElapsed',
  'setAnimatorTime'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSvgAnimator::~QSvgAnimator()': the destructor: Python never
    removes a C++ QSvgAnimator.

  What to expect
  --------------

  - The C++ QSvgAnimator is created at the first use, not by
    'QSvgAnimator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSvgAnimator.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSvgAnimator'

  #  A C++ QSvgAnimator Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSvgAnimator'

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
    Calls Qt's 'void QSvgAnimator::setAnimatorTime(qint64 time)'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimator.html#setAnimatorTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QSvgAnimator::setAnimatorTime(qint64 time)
    ritual = 'ritual_ZN12QSvgAnimator15setAnimatorTimeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSvgAnimator15setAnimatorTimeEx'
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
    Notes what was given, for Qt's 'QSvgAnimator::QSvgAnimator()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimator.html#QSvgAnimator
    """
    #  QSvgAnimator::QSvgAnimator()
    self._noteCreation(QSvgAnimator, lambda: Rituals.call(
        'ritual_ZN12QSvgAnimatorC1Ev',
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
    Calls Qt's 'void QSvgAnimator::restartAnimation()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimator.html#restartAnimation
    """
    #  void QSvgAnimator::restartAnimation()
    ritual = 'ritual_ZN12QSvgAnimator16restartAnimationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSvgAnimator16restartAnimationEv'
    self.uglySide.call(ritual)

  def currentElapsed(self) -> int:
    """
    Calls Qt's 'qint64 QSvgAnimator::currentElapsed()'.

    Qt's own words: https://doc.qt.io/qt-6/qsvganimator.html#currentElapsed
    """
    #  qint64 QSvgAnimator::currentElapsed()
    ritual = 'ritual_ZN12QSvgAnimator14currentElapsedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QSvgAnimator14currentElapsedEv'
    return self.uglySide.call(ritual)
