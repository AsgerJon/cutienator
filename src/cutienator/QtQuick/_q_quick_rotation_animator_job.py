"""
QQuickRotationAnimatorJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickRotationAnimatorJob to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickRotationAnimator, QQuickTransformAnimatorJob


class QQuickRotationAnimatorJob(QQuickTransformAnimatorJob):
  """
  The cute side of Qt's QQuickRotationAnimatorJob: a plain Python object
  standing in front of one C++ QQuickRotationAnimatorJob.

  It is built on the cute 'QQuickTransformAnimatorJob', as Qt's
  QQuickRotationAnimatorJob is built on Qt's QQuickTransformAnimatorJob, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRotationAnimatorJob that has a ritual and that
  Python can call so far, 4 names in all: 'updateCurrentTime', 'writeBack',
  'setDirection', 'direction'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QQuickRotationAnimatorJob is created at the first use, not by
    'QQuickRotationAnimatorJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRotationAnimatorJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRotationAnimatorJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def direction(self) -> QQuickRotationAnimator.RotationDirection:
    """
    Calls Qt's 'QQuickRotationAnimator::RotationDirection
    QQuickRotationAnimatorJob::direction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimatorjob.html#direction

    Returns
    -------

    QQuickRotationAnimator.RotationDirection
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickRotationAnimator.RotationDirection(number)' gives.
    """
    #  QQuickRotationAnimator::RotationDirection
    #      QQuickRotationAnimatorJob::direction() const
    return QQuickRotationAnimator.RotationDirection(self.uglySide.call(
        'ritual_ZNK25QQuickRotationAnimatorJob9directionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickRotationAnimator.RotationDirection)
  def setDirection(
      self,
      direction: QQuickRotationAnimator.RotationDirection,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickRotationAnimatorJob::setDirection(QQuickRotationAnimator::
    RotationDirection direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimatorjob.html#setDirection

    Parameters
    ----------

    direction : QQuickRotationAnimator.RotationDirection
      Passed on as its number.
    """
    #  void QQuickRotationAnimatorJob::setDirection(QQuickRotationAnimator::
    #      RotationDirection direction)
    self.uglySide.call(
        'ritual_ZN25QQuickRotationAnimatorJob12setDirectionEN22QQuickRotati'
        'onAnimator17RotationDirectionE',
        direction.value,
    )

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
    'QQuickRotationAnimatorJob::QQuickRotationAnimatorJob()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimatorjob.html
    """
    #  QQuickRotationAnimatorJob::QQuickRotationAnimatorJob()
    self._noteCreation(QQuickRotationAnimatorJob, lambda: Rituals.call(
        'ritual_ZN25QQuickRotationAnimatorJobC1Ev',
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

  @overload(int)
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimatorJob::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimatorjob.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuickRotationAnimatorJob::updateCurrentTime(int time)
    ritual = 'ritual_ZN25QQuickRotationAnimatorJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN25QQuickRotationAnimatorJob17updateCurrentTimeEi')
    self.uglySide.call(ritual, time)

  def writeBack(self) -> None:
    """
    Calls Qt's 'void QQuickRotationAnimatorJob::writeBack()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrotationanimatorjob.html#writeBack
    """
    #  void QQuickRotationAnimatorJob::writeBack()
    ritual = 'ritual_ZN25QQuickRotationAnimatorJob9writeBackEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QQuickRotationAnimatorJob9writeBackEv'
    self.uglySide.call(ritual)
