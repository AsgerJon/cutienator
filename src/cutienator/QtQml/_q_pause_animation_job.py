"""
QPauseAnimationJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qpauseanimationjob_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QPauseAnimationJob to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QPauseAnimationJob(QAbstractAnimationJob):
  """
  The cute side of Qt's QPauseAnimationJob: a plain Python object standing in
  front of one C++ QPauseAnimationJob.

  It is built on the cute 'QAbstractAnimationJob', as Qt's QPauseAnimationJob
  is built on Qt's QAbstractAnimationJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPauseAnimationJob that has a ritual and that Python
  can call so far, 4 names in all: 'duration', 'setDuration',
  'updateCurrentTime', 'debugAnimation'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPauseAnimationJob::~QPauseAnimationJob()': the destructor: Python
    never removes a C++ QPauseAnimationJob.

  What has no ritual
  ------------------

  2 of the 8 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QPauseAnimationJob is created at the first use, not by
    'QPauseAnimationJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPauseAnimationJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPauseAnimationJob'

  #  A C++ QPauseAnimationJob Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPauseAnimationJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def duration(self) -> int:
    """
    Calls Qt's 'int QPauseAnimationJob::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qpauseanimationjob.html#duration
    """
    #  int QPauseAnimationJob::duration() const
    ritual = 'ritual_ZNK18QPauseAnimationJob8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPauseAnimationJob8durationEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDuration(self, msecs: int) -> None:
    """
    Calls Qt's 'void QPauseAnimationJob::setDuration(int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimationjob.html#setDuration

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  void QPauseAnimationJob::setDuration(int msecs)
    self.uglySide.call('ritual_ZN18QPauseAnimationJob11setDurationEi', msecs)

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
  @overload(int)
  def __init__(self, duration: int = 250) -> None:
    """
    Notes what was given, for Qt's
    'QPauseAnimationJob::QPauseAnimationJob(int duration)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimationjob.html#QPauseAnimationJob

    Parameters
    ----------

    duration : int
      Passed on as it is. May be left out, as in Qt: it is then 250.
    """
    #  QPauseAnimationJob::QPauseAnimationJob(int duration)
    self._noteCreation(QPauseAnimationJob, lambda: Rituals.call(
        'ritual_ZN18QPauseAnimationJobC1Ei', duration,
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
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QPauseAnimationJob::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimationjob.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QPauseAnimationJob::updateCurrentTime(int a0)
    ritual = 'ritual_ZN18QPauseAnimationJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPauseAnimationJob17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QPauseAnimationJob::debugAnimation(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpauseanimationjob.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QPauseAnimationJob::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK18QPauseAnimationJob14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPauseAnimationJob14debugAnimationE6QDebug'
    self.uglySide.call(ritual, self._valueOf(d))
