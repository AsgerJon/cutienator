"""
QParallelAnimationGroupJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qparallelanimationgroupjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QParallelAnimationGroupJob to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QAbstractAnimationJob, QAnimationGroupJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QParallelAnimationGroupJob(QAnimationGroupJob):
  """
  The cute side of Qt's QParallelAnimationGroupJob: a plain Python object
  standing in front of one C++ QParallelAnimationGroupJob.

  It is built on the cute 'QAnimationGroupJob', as Qt's
  QParallelAnimationGroupJob is built on Qt's QAnimationGroupJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QParallelAnimationGroupJob that has a ritual and
  that Python can call so far, 8 names in all: 'duration',
  'updateCurrentTime', 'updateState', 'updateDirection',
  'uncontrolledAnimationFinished', 'debugAnimation', 'shouldAnimationStart',
  'applyGroupState'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QParallelAnimationGroupJob::~QParallelAnimationGroupJob()': the
    destructor: Python never removes a C++ QParallelAnimationGroupJob.

  What has no ritual
  ------------------

  2 of the 12 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QParallelAnimationGroupJob is created at the first use, not by
    'QParallelAnimationGroupJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QParallelAnimationGroupJob.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QParallelAnimationGroupJob'

  #  A C++ QParallelAnimationGroupJob Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QParallelAnimationGroupJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def duration(self) -> int:
    """
    Calls Qt's 'int QParallelAnimationGroupJob::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html#duration
    """
    #  int QParallelAnimationGroupJob::duration() const
    ritual = 'ritual_ZNK26QParallelAnimationGroupJob8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QParallelAnimationGroupJob8durationEv'
    return self.uglySide.call(ritual)

  @overload(QAbstractAnimationJob, bool)
  @overload(NoneType, bool)
  def shouldAnimationStart(
      self,
      animation: Optional[QAbstractAnimationJob],
      startIfAtEnd: bool,
  ) -> bool:
    """
    Calls Qt's 'bool
    QParallelAnimationGroupJob::shouldAnimationStart(QAbstractAnimationJob
    *animation, bool startIfAtEnd) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    startIfAtEnd : bool
      Passed on as it is.
    """
    #  bool QParallelAnimationGroupJob::shouldAnimationStart(
    #      QAbstractAnimationJob *animation, bool startIfAtEnd) const
    return self.uglySide.call(
        'ritual_ZNK26QParallelAnimationGroupJob20shouldAnimationStartEP21QA'
        'bstractAnimationJobb',
        self._addressOf(animation, 'QAbstractAnimationJob'), startIfAtEnd,
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
    Notes what was given, for Qt's
    'QParallelAnimationGroupJob::QParallelAnimationGroupJob()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html
    """
    #  QParallelAnimationGroupJob::QParallelAnimationGroupJob()
    self._noteCreation(QParallelAnimationGroupJob, lambda: Rituals.call(
        'ritual_ZN26QParallelAnimationGroupJobC1Ev',
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
  def updateCurrentTime(self, currentTime: int) -> None:
    """
    Calls Qt's 'void QParallelAnimationGroupJob::updateCurrentTime(int
    currentTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html#updateCurrentTime

    Parameters
    ----------

    currentTime : int
      Passed on as it is.
    """
    #  void QParallelAnimationGroupJob::updateCurrentTime(int currentTime)
    ritual = 'ritual_ZN26QParallelAnimationGroupJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QParallelAnimationGroupJob17updateCurrentTimeEi')
    self.uglySide.call(ritual, currentTime)

  @overload(QAbstractAnimationJob.State, QAbstractAnimationJob.State)
  def updateState(
      self,
      newState: QAbstractAnimationJob.State,
      oldState: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void
    QParallelAnimationGroupJob::updateState(QAbstractAnimationJob::State
    newState, QAbstractAnimationJob::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimationJob.State
      Passed on as its number.

    oldState : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QParallelAnimationGroupJob::updateState(QAbstractAnimationJob::
    #      State newState, QAbstractAnimationJob::State oldState)
    ritual = (
        'ritual_ZN26QParallelAnimationGroupJob11updateStateEN21QAbstractAni'
        'mationJob5StateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QParallelAnimationGroupJob11updateStateEN21QAbstr'
          'actAnimationJob5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)

  @overload(QAbstractAnimationJob.Direction)
  def updateDirection(
      self,
      direction: QAbstractAnimationJob.Direction,
  ) -> None:
    """
    Calls Qt's 'void
    QParallelAnimationGroupJob::updateDirection(QAbstractAnimationJob::
    Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html#updateDirection

    Parameters
    ----------

    direction : QAbstractAnimationJob.Direction
      Passed on as its number.
    """
    #  void QParallelAnimationGroupJob::updateDirection(
    #      QAbstractAnimationJob::Direction direction)
    ritual = (
        'ritual_ZN26QParallelAnimationGroupJob15updateDirectionEN21QAbstrac'
        'tAnimationJob9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QParallelAnimationGroupJob15updateDirectionEN21QA'
          'bstractAnimationJob9DirectionE')
    self.uglySide.call(ritual, direction.value)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def uncontrolledAnimationFinished(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QParallelAnimationGroupJob::uncontrolledAnimationFinished(
    QAbstractAnimationJob *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QParallelAnimationGroupJob::uncontrolledAnimationFinished(
    #      QAbstractAnimationJob *animation)
    ritual = (
        'ritual_ZN26QParallelAnimationGroupJob29uncontrolledAnimationFinish'
        'edEP21QAbstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QParallelAnimationGroupJob29uncontrolledAnimation'
          'FinishedEP21QAbstractAnimationJob')
    self.uglySide.call(
        ritual, self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QParallelAnimationGroupJob::debugAnimation(QDebug d)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QParallelAnimationGroupJob::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK26QParallelAnimationGroupJob14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK26QParallelAnimationGroupJob14debugAnimationE6QDeb'
          'ug')
    self.uglySide.call(ritual, self._valueOf(d))

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def applyGroupState(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QParallelAnimationGroupJob::applyGroupState(QAbstractAnimationJob
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qparallelanimationgroupjob.html#applyGroupState

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QParallelAnimationGroupJob::applyGroupState(QAbstractAnimationJob
    #      *animation)
    self.uglySide.call(
        'ritual_ZN26QParallelAnimationGroupJob15applyGroupStateEP21QAbstrac'
        'tAnimationJob',
        self._addressOf(animation, 'QAbstractAnimationJob'),
    )
