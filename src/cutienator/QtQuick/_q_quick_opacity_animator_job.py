"""
QQuickOpacityAnimatorJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatorjob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickOpacityAnimatorJob to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QQuickAnimatorJob


class QQuickOpacityAnimatorJob(QQuickAnimatorJob):
  """
  The cute side of Qt's QQuickOpacityAnimatorJob: a plain Python object
  standing in front of one C++ QQuickOpacityAnimatorJob.

  It is built on the cute 'QQuickAnimatorJob', as Qt's
  QQuickOpacityAnimatorJob is built on Qt's QQuickAnimatorJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickOpacityAnimatorJob that has a ritual and that
  Python can call so far, 4 names in all: 'invalidate', 'updateCurrentTime',
  'writeBack', 'postSync'. It can be made from Python, in 1 way; see
  '__init__'.

  What to expect
  --------------

  - The C++ QQuickOpacityAnimatorJob is created at the first use, not by
    'QQuickOpacityAnimatorJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickOpacityAnimatorJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickOpacityAnimatorJob'

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QQuickOpacityAnimatorJob::QQuickOpacityAnimatorJob()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickopacityanimatorjob.html
    """
    #  QQuickOpacityAnimatorJob::QQuickOpacityAnimatorJob()
    self._noteCreation(QQuickOpacityAnimatorJob, lambda: Rituals.call(
        'ritual_ZN24QQuickOpacityAnimatorJobC1Ev',
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

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickOpacityAnimatorJob::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickopacityanimatorjob.html#invalidate
    """
    #  void QQuickOpacityAnimatorJob::invalidate()
    ritual = 'ritual_ZN24QQuickOpacityAnimatorJob10invalidateEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickOpacityAnimatorJob10invalidateEv'
    self.uglySide.call(ritual)

  @overload(int)
  def updateCurrentTime(self, time: int) -> None:
    """
    Calls Qt's 'void QQuickOpacityAnimatorJob::updateCurrentTime(int time)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickopacityanimatorjob.html#updateCurrentTime

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  void QQuickOpacityAnimatorJob::updateCurrentTime(int time)
    ritual = 'ritual_ZN24QQuickOpacityAnimatorJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickOpacityAnimatorJob17updateCurrentTimeEi'
    self.uglySide.call(ritual, time)

  def writeBack(self) -> None:
    """
    Calls Qt's 'void QQuickOpacityAnimatorJob::writeBack()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickopacityanimatorjob.html#writeBack
    """
    #  void QQuickOpacityAnimatorJob::writeBack()
    ritual = 'ritual_ZN24QQuickOpacityAnimatorJob9writeBackEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickOpacityAnimatorJob9writeBackEv'
    self.uglySide.call(ritual)

  def postSync(self) -> None:
    """
    Calls Qt's 'void QQuickOpacityAnimatorJob::postSync()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickopacityanimatorjob.html#postSync
    """
    #  void QQuickOpacityAnimatorJob::postSync()
    ritual = 'ritual_ZN24QQuickOpacityAnimatorJob8postSyncEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN24QQuickOpacityAnimatorJob8postSyncEv'
    self.uglySide.call(ritual)
