"""
QActionAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimation_p_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QActionAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtQml import QAbstractAnimationJob

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QDebug
  from . import QAbstractAnimationAction
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimationAction = WAIT['QAbstractAnimationAction']
  QDebug = WAIT['QDebug']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QActionAnimation(QAbstractAnimationJob):
  """
  The cute side of Qt's QActionAnimation: a plain Python object standing in
  front of one C++ QActionAnimation.

  It is built on the cute 'QAbstractAnimationJob', as Qt's QActionAnimation
  is built on Qt's QAbstractAnimationJob, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QActionAnimation that has a ritual and that Python
  can call so far, 5 names in all: 'duration', 'setAnimAction',
  'updateCurrentTime', 'updateState', 'debugAnimation'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QActionAnimation::~QActionAnimation()': the destructor: Python
    never removes a C++ QActionAnimation.

  What has no ritual
  ------------------

  2 of the 10 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QActionAnimation is created at the first use, not by
    'QActionAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QActionAnimation.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QActionAnimation'

  #  A C++ QActionAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QActionAnimation'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def duration(self) -> int:
    """
    Calls Qt's 'int QActionAnimation::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qactionanimation.html#duration
    """
    #  int QActionAnimation::duration() const
    ritual = 'ritual_ZNK16QActionAnimation8durationEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QActionAnimation8durationEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAbstractAnimationAction)
  @overload(NoneType)
  def setAnimAction(
      self,
      action: Optional[QAbstractAnimationAction],
  ) -> None:
    """
    Calls Qt's 'void QActionAnimation::setAnimAction(QAbstractAnimationAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qactionanimation.html#setAnimAction

    Parameters
    ----------

    action : Optional[QAbstractAnimationAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QActionAnimation::setAnimAction(QAbstractAnimationAction *action)
    self.uglySide.call(
        'ritual_ZN16QActionAnimation13setAnimActionEP24QAbstractAnimationAc'
        'tion',
        self._addressOf(action),
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
    Notes what was given, for Qt's 'QActionAnimation::QActionAnimation()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qactionanimation.html#QActionAnimation
    """
    #  QActionAnimation::QActionAnimation()
    self._noteCreation(QActionAnimation, lambda: Rituals.call(
        'ritual_ZN16QActionAnimationC1Ev',
    ))

  @overload(QAbstractAnimationAction)
  @overload(NoneType)
  def __init__(self, action: Optional[QAbstractAnimationAction]) -> None:
    """
    Notes what was given, for Qt's
    'QActionAnimation::QActionAnimation(QAbstractAnimationAction *action)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qactionanimation.html#QActionAnimation

    Parameters
    ----------

    action : Optional[QAbstractAnimationAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QActionAnimation::QActionAnimation(QAbstractAnimationAction *action)
    self._noteCreation(QActionAnimation, lambda: Rituals.call(
        'ritual_ZN16QActionAnimationC1EP24QAbstractAnimationAction',
        self._addressOf(action),
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
    Calls Qt's 'void QActionAnimation::updateCurrentTime(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qactionanimation.html#updateCurrentTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QActionAnimation::updateCurrentTime(int a0)
    ritual = 'ritual_ZN16QActionAnimation17updateCurrentTimeEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QActionAnimation17updateCurrentTimeEi'
    self.uglySide.call(ritual, a0)

  @overload(QAbstractAnimationJob.State, QAbstractAnimationJob.State)
  def updateState(
      self,
      newState: QAbstractAnimationJob.State,
      oldState: QAbstractAnimationJob.State,
  ) -> None:
    """
    Calls Qt's 'void QActionAnimation::updateState(State newState, State
    oldState)'.

    Qt's own words: https://doc.qt.io/qt-6/qactionanimation.html#updateState

    Parameters
    ----------

    newState : QAbstractAnimationJob.State
      Passed on as its number.

    oldState : QAbstractAnimationJob.State
      Passed on as its number.
    """
    #  void QActionAnimation::updateState(State newState, State oldState)
    ritual = (
        'ritual_ZN16QActionAnimation11updateStateEN21QAbstractAnimationJob5'
        'StateES1_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QActionAnimation11updateStateEN21QAbstractAnimati'
          'onJob5StateES1_')
    self.uglySide.call(ritual, newState.value, oldState.value)

  @overload(QDebug)
  def debugAnimation(self, d: QDebug) -> None:
    """
    Calls Qt's 'void QActionAnimation::debugAnimation(QDebug d) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qactionanimation.html#debugAnimation

    Parameters
    ----------

    d : QDebug
      Passed on as a value: Qt reads the C++ QDebug, which stays Python's
      own.
    """
    #  void QActionAnimation::debugAnimation(QDebug d) const
    ritual = 'ritual_ZNK16QActionAnimation14debugAnimationE6QDebug'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QActionAnimation14debugAnimationE6QDebug'
    self.uglySide.call(ritual, self._valueOf(d))
