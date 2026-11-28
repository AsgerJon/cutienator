"""
QSmoothedAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSmoothedAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtQml import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QDebug
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDebug = WAIT['QDebug']


class QSmoothedAnimation(QAbstractAnimationJob):
  """
  The cute side of Qt's QSmoothedAnimation: a plain Python object standing in
  front of one C++ QSmoothedAnimation.

  It is built on the cute 'QAbstractAnimationJob', as Qt's QSmoothedAnimation
  is built on Qt's QAbstractAnimationJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSmoothedAnimation that has a ritual and that Python
  can call so far, 11 names in all: 'duration', 'restart', 'init',
  'prepareForRestart', 'clearTemplate', 'updateCurrentTime', 'updateState',
  'debugAnimation', 'easeFollow', 'recalc', 'delayedStop'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSmoothedAnimation::~QSmoothedAnimation()': the destructor: Python
    never removes a C++ QSmoothedAnimation.

  What has no ritual
  ------------------

  3 of the 15 functions Qt declares: 2 forbidden; 1 leans on 'vtable for
  QSmoothedAnimationTimer', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QSmoothedAnimation is created at the first use, not by
    'QSmoothedAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSmoothedAnimation.
  - Each name of Qt's QSmoothedAnimation that has no cute function yet,
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
  __qt_class__ = 'QSmoothedAnimation'

  #  A C++ QSmoothedAnimation Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSmoothedAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def duration(self) -> int:
    """
    Calls Qt's 'int QSmoothedAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsmoothedanimation.html#duration
    """
    #  int QSmoothedAnimation::duration() const
    ritual = 'ritual_ZNK18QSmoothedAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSmoothedAnimation8durationEv'
    return self.uglySide.call(ritual)

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
    Qt's
    'QSmoothedAnimation::QSmoothedAnimation(QQuickSmoothedAnimationPrivate
    *a0)': leans on 'vtable for QSmoothedAnimationTimer', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'QSmoothedAnimation.__init__' has no cute function yet. Qt's "
        "'QSmoothedAnimation::QSmoothedAnimation(QQuickSmoothedAnimationPriv"
        "ate *a0)': leans on 'vtable for QSmoothedAnimationTimer', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def restart(self) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qsmoothedanimation.html#restart
    """
    #  void QSmoothedAnimation::restart()
    self.uglySide.call('ritual_ZN18QSmoothedAnimation7restartEv')

  def init(self) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qsmoothedanimation.html#init
    """
    #  void QSmoothedAnimation::init()
    self.uglySide.call('ritual_ZN18QSmoothedAnimation4initEv')

  def prepareForRestart(self) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::prepareForRestart()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsmoothedanimation.html#prepareForRestart
    """
    #  void QSmoothedAnimation::prepareForRestart()
    self.uglySide.call('ritual_ZN18QSmoothedAnimation17prepareForRestartEv')

  def clearTemplate(self) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::clearTemplate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsmoothedanimation.html#clearTemplate
    """
    #  void QSmoothedAnimation::clearTemplate()
    self.uglySide.call('ritual_ZN18QSmoothedAnimation13clearTemplateEv')

  @overload(int)
  def updateCurrentTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsmoothedanimation.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QSmoothedAnimation::updateCurrentTime(int a0)
    ritual = 'ritual_ZN18QSmoothedAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QSmoothedAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)

  @overload(QAbstractAnimationJob.State, QAbstractAnimationJob.State)
  def updateState(
      self,
      a0: QAbstractAnimationJob.State,
      a1: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void
    QSmoothedAnimation::updateState(QAbstractAnimationJob::State a0,
    QAbstractAnimationJob::State a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsmoothedanimation.html#updateState

    Parameters
    ----------

    a0 : QAbstractAnimationJob.State
      Passed on as its number.

    a1 : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QSmoothedAnimation::updateState(QAbstractAnimationJob::State a0,
    #      QAbstractAnimationJob::State a1)
    ritual = (
        'ritual_ZN18QSmoothedAnimation11updateStateEN21QAbstractAnimationJo'
        'b5StateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QSmoothedAnimation11updateStateEN21QAbstractAnima'
          'tionJob5StateES1_')
    self.uglySide.call(ritual, a0.value, a1.value)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::debugAnimation(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsmoothedanimation.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QSmoothedAnimation::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK18QSmoothedAnimation14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QSmoothedAnimation14debugAnimationE6QDebug'
    self.uglySide.call(ritual, self._valueOf(d))

  @overload(float)
  def easeFollow(self, a0: float) -> float:
    """
    Calls Qt's 'qreal QSmoothedAnimation::easeFollow(qreal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qsmoothedanimation.html#easeFollow

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  qreal QSmoothedAnimation::easeFollow(qreal a0)
    return self.uglySide.call(
        'ritual_ZN18QSmoothedAnimation10easeFollowEd', a0,
    )

  def recalc(self) -> bool:
    """
    Calls Qt's 'bool QSmoothedAnimation::recalc()'.

    Qt's own words: https://doc.qt.io/qt-6/qsmoothedanimation.html#recalc
    """
    #  bool QSmoothedAnimation::recalc()
    return self.uglySide.call('ritual_ZN18QSmoothedAnimation6recalcEv')

  def delayedStop(self) -> None:
    """
    Calls Qt's 'void QSmoothedAnimation::delayedStop()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsmoothedanimation.html#delayedStop
    """
    #  void QSmoothedAnimation::delayedStop()
    self.uglySide.call('ritual_ZN18QSmoothedAnimation11delayedStopEv')
