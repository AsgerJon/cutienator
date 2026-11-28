"""
QSequentialAnimationGroupJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qsequentialanimationgroupjob_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSequentialAnimationGroupJob to be private: it declares the class
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
  from typing import Never, Optional

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSequentialAnimationGroupJob(QAnimationGroupJob):
  """
  The cute side of Qt's QSequentialAnimationGroupJob: a plain Python object
  standing in front of one C++ QSequentialAnimationGroupJob.

  It is built on the cute 'QAnimationGroupJob', as Qt's
  QSequentialAnimationGroupJob is built on Qt's QAnimationGroupJob, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSequentialAnimationGroupJob that has a ritual and
  that Python can call so far, 15 names in all: 'duration',
  'currentAnimation', 'clear', 'updateCurrentTime', 'updateState',
  'updateDirection', 'uncontrolledAnimationFinished', 'debugAnimation',
  'animationActualTotalDuration', 'setCurrentAnimation',
  'activateCurrentAnimation', 'animationInserted', 'animationRemoved',
  'atEnd', 'restart'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSequentialAnimationGroupJob::~QSequentialAnimationGroupJob()': the
    destructor: Python never removes a C++ QSequentialAnimationGroupJob.
  - Qt's 'AnimationIndex QSequentialAnimationGroupJob::indexForCurrentTime()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QSequentialAnimationGroupJob::rewindForwards(const
    AnimationIndex &newAnimationIndex)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QSequentialAnimationGroupJob::advanceForwards(const
    AnimationIndex &newAnimationIndex)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSequentialAnimationGroupJob is created at the first use, not by
    'QSequentialAnimationGroupJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSequentialAnimationGroupJob.
  - Each name of Qt's QSequentialAnimationGroupJob that has no cute function
    yet, 'advanceForwards', 'indexForCurrentTime', 'rewindForwards', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSequentialAnimationGroupJob'

  #  A C++ QSequentialAnimationGroupJob Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSequentialAnimationGroupJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def duration(self) -> int:
    """
    Calls Qt's 'int QSequentialAnimationGroupJob::duration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#duration
    """
    #  int QSequentialAnimationGroupJob::duration() const
    ritual = 'ritual_ZNK28QSequentialAnimationGroupJob8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK28QSequentialAnimationGroupJob8durationEv'
    return self.uglySide.call(ritual)

  def currentAnimation(self) -> Optional[QAbstractAnimationJob]:
    """
    Calls Qt's 'QAbstractAnimationJob
    *QSequentialAnimationGroupJob::currentAnimation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#currentAnimation

    Returns
    -------

    Optional[QAbstractAnimationJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractAnimationJob
    #      *QSequentialAnimationGroupJob::currentAnimation() const
    address = self.uglySide.call(
        'ritual_ZNK28QSequentialAnimationGroupJob16currentAnimationEv',
    )
    return QAbstractAnimationJob._cuteAt(address)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationActualTotalDuration(
      self,
      anim: Optional[QAbstractAnimationJob],
  ) -> int:
    """
    Calls Qt's 'int
    QSequentialAnimationGroupJob::animationActualTotalDuration(const
    QAbstractAnimationJob *anim) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSequentialAnimationGroupJob::animationActualTotalDuration(const
    #      QAbstractAnimationJob *anim) const
    return self.uglySide.call(
        'ritual_ZNK28QSequentialAnimationGroupJob28animationActualTotalDura'
        'tionEPK21QAbstractAnimationJob',
        self._addressOf(anim, 'QAbstractAnimationJob'),
    )

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QSequentialAnimationGroupJob::atEnd() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#atEnd
    """
    #  bool QSequentialAnimationGroupJob::atEnd() const
    return self.uglySide.call(
        'ritual_ZNK28QSequentialAnimationGroupJob5atEndEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  @overload(QAbstractAnimationJob, bool)
  @overload(NoneType, bool)
  def setCurrentAnimation(
      self,
      anim: Optional[QAbstractAnimationJob],
      intermediate: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QSequentialAnimationGroupJob::setCurrentAnimation(const
    QAbstractAnimationJob *anim, bool intermediate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    intermediate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSequentialAnimationGroupJob::setCurrentAnimation(const
    #      QAbstractAnimationJob *anim, bool intermediate)
    self.uglySide.call(
        'ritual_ZN28QSequentialAnimationGroupJob19setCurrentAnimationEPK21Q'
        'AbstractAnimationJobb',
        self._addressOf(anim, 'QAbstractAnimationJob'), intermediate,
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
    'QSequentialAnimationGroupJob::QSequentialAnimationGroupJob()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html
    """
    #  QSequentialAnimationGroupJob::QSequentialAnimationGroupJob()
    self._noteCreation(QSequentialAnimationGroupJob, lambda: Rituals.call(
        'ritual_ZN28QSequentialAnimationGroupJobC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QSequentialAnimationGroupJob::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#clear
    """
    #  void QSequentialAnimationGroupJob::clear()
    ritual = 'ritual_ZN28QSequentialAnimationGroupJob5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN28QSequentialAnimationGroupJob5clearEv'
    self.uglySide.call(ritual)

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QSequentialAnimationGroupJob::updateCurrentTime(int
    a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSequentialAnimationGroupJob::updateCurrentTime(int a0)
    ritual = 'ritual_ZN28QSequentialAnimationGroupJob17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSequentialAnimationGroupJob17updateCurrentTimeEi')
    self.uglySide.call(ritual, a0)

  @overload(QAbstractAnimationJob.State, QAbstractAnimationJob.State)
  def updateState(
      self,
      newState: QAbstractAnimationJob.State,
      oldState: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroupJob::updateState(QAbstractAnimationJob::State
    newState, QAbstractAnimationJob::State oldState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimationJob.State
      Passed on as its number.

    oldState : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QSequentialAnimationGroupJob::updateState(QAbstractAnimationJob::
    #      State newState, QAbstractAnimationJob::State oldState)
    ritual = (
        'ritual_ZN28QSequentialAnimationGroupJob11updateStateEN21QAbstractA'
        'nimationJob5StateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSequentialAnimationGroupJob11updateStateEN21QAbs'
          'tractAnimationJob5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)

  @overload(QAbstractAnimationJob.Direction)
  def updateDirection(
      self,
      direction: QAbstractAnimationJob.Direction,
  ) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroupJob::updateDirection(QAbstractAnimationJob::
    Direction direction)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#updateDirection

    Parameters
    ----------

    direction : QAbstractAnimationJob.Direction
      Passed on as its number.
    """
    #  void QSequentialAnimationGroupJob::updateDirection(
    #      QAbstractAnimationJob::Direction direction)
    ritual = (
        'ritual_ZN28QSequentialAnimationGroupJob15updateDirectionEN21QAbstr'
        'actAnimationJob9DirectionE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSequentialAnimationGroupJob15updateDirectionEN21'
          'QAbstractAnimationJob9DirectionE')
    self.uglySide.call(ritual, direction.value)

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def uncontrolledAnimationFinished(
      self,
      animation: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroupJob::uncontrolledAnimationFinished(
    QAbstractAnimationJob *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html

    Parameters
    ----------

    animation : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSequentialAnimationGroupJob::uncontrolledAnimationFinished(
    #      QAbstractAnimationJob *animation)
    ritual = (
        'ritual_ZN28QSequentialAnimationGroupJob29uncontrolledAnimationFini'
        'shedEP21QAbstractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSequentialAnimationGroupJob29uncontrolledAnimati'
          'onFinishedEP21QAbstractAnimationJob')
    self.uglySide.call(
        ritual, self._addressOf(animation, 'QAbstractAnimationJob'),
    )

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QSequentialAnimationGroupJob::debugAnimation(QDebug d)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QSequentialAnimationGroupJob::debugAnimation(QDebug d) const
    ritual = (
        'ritual_ZNK28QSequentialAnimationGroupJob14debugAnimationE6QDebug')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK28QSequentialAnimationGroupJob14debugAnimationE6QD'
          'ebug')
    self.uglySide.call(ritual, self._valueOf(d))

  @overload()
  @overload(bool)
  def activateCurrentAnimation(self, intermediate: bool = False) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroupJob::activateCurrentAnimation(bool
    intermediate)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html

    Parameters
    ----------

    intermediate : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QSequentialAnimationGroupJob::activateCurrentAnimation(bool
    #      intermediate)
    self.uglySide.call(
        'ritual_ZN28QSequentialAnimationGroupJob24activateCurrentAnimationE'
        'b',
        intermediate,
    )

  @overload(QAbstractAnimationJob)
  @overload(NoneType)
  def animationInserted(self, anim: Optional[QAbstractAnimationJob]) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroupJob::animationInserted(QAbstractAnimationJob
    *anim)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSequentialAnimationGroupJob::animationInserted(
    #      QAbstractAnimationJob *anim)
    ritual = (
        'ritual_ZN28QSequentialAnimationGroupJob17animationInsertedEP21QAbs'
        'tractAnimationJob')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSequentialAnimationGroupJob17animationInsertedEP'
          '21QAbstractAnimationJob')
    self.uglySide.call(
        ritual, self._addressOf(anim, 'QAbstractAnimationJob'),
    )

  @overload(
      QAbstractAnimationJob, QAbstractAnimationJob, QAbstractAnimationJob,
  )
  @overload(QAbstractAnimationJob, QAbstractAnimationJob, NoneType)
  @overload(QAbstractAnimationJob, NoneType, QAbstractAnimationJob)
  @overload(QAbstractAnimationJob, NoneType, NoneType)
  @overload(NoneType, QAbstractAnimationJob, QAbstractAnimationJob)
  @overload(NoneType, QAbstractAnimationJob, NoneType)
  @overload(NoneType, NoneType, QAbstractAnimationJob)
  @overload(NoneType, NoneType, NoneType)
  def animationRemoved(
      self,
      anim: Optional[QAbstractAnimationJob],
      a1: Optional[QAbstractAnimationJob],
      a2: Optional[QAbstractAnimationJob],
  ) -> None:
    """
    Calls Qt's 'void
    QSequentialAnimationGroupJob::animationRemoved(QAbstractAnimationJob
    *anim, QAbstractAnimationJob *a1, QAbstractAnimationJob *a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#animationRemoved

    Parameters
    ----------

    anim : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a2 : Optional[QAbstractAnimationJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSequentialAnimationGroupJob::animationRemoved(
    #      QAbstractAnimationJob *anim, QAbstractAnimationJob *a1,
    #      QAbstractAnimationJob *a2)
    ritual = (
        'ritual_ZN28QSequentialAnimationGroupJob16animationRemovedEP21QAbst'
        'ractAnimationJobS1_S1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN28QSequentialAnimationGroupJob16animationRemovedEP2'
          '1QAbstractAnimationJobS1_S1_')
    self.uglySide.call(
        ritual,
        self._addressOf(anim, 'QAbstractAnimationJob'), self._addressOf(a1,
        'QAbstractAnimationJob'), self._addressOf(a2,
        'QAbstractAnimationJob'),
    )

  def restart(self) -> None:
    """
    Calls Qt's 'void QSequentialAnimationGroupJob::restart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsequentialanimationgroupjob.html#restart
    """
    #  void QSequentialAnimationGroupJob::restart()
    self.uglySide.call('ritual_ZN28QSequentialAnimationGroupJob7restartEv')

  @staticmethod
  def advanceForwards(*__, **_) -> Never:
    """
    Qt's 'void QSequentialAnimationGroupJob::advanceForwards(const
    AnimationIndex &newAnimationIndex)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSequentialAnimationGroupJob.advanceForwards' has no cute "
        "function yet. Qt's 'void "
        "QSequentialAnimationGroupJob::advanceForwards(const AnimationIndex "
        "&newAnimationIndex)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def indexForCurrentTime(*__, **_) -> Never:
    """
    Qt's 'AnimationIndex QSequentialAnimationGroupJob::indexForCurrentTime()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSequentialAnimationGroupJob.indexForCurrentTime' has no cute "
        "function yet. Qt's 'AnimationIndex "
        "QSequentialAnimationGroupJob::indexForCurrentTime() const': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def rewindForwards(*__, **_) -> Never:
    """
    Qt's 'void QSequentialAnimationGroupJob::rewindForwards(const
    AnimationIndex &newAnimationIndex)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QSequentialAnimationGroupJob.rewindForwards' has no cute function "
        "yet. Qt's 'void QSequentialAnimationGroupJob::rewindForwards(const "
        "AnimationIndex &newAnimationIndex)': takes a type Python has no "
        "way to hand over yet.")
