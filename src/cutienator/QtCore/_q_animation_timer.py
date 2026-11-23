"""
QAnimationTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QAnimationTimer to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QAbstractAnimationTimer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractAnimation, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimation = WAIT['QAbstractAnimation']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QAnimationTimer(QAbstractAnimationTimer):
  """
  The cute side of Qt's QAnimationTimer: a plain Python object standing in
  front of one C++ QAnimationTimer.

  It is built on the cute 'QAbstractAnimationTimer', as Qt's QAnimationTimer
  is built on Qt's QAbstractAnimationTimer, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QAnimationTimer that has a ritual and that Python
  can call so far, 8 names in all: 'metaObject', 'restartAnimationTimer',
  'updateAnimationsTime', 'runningAnimationCount', 'startAnimations',
  'stopTimer', 'registerRunningAnimation', 'unregisterRunningAnimation'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has no ritual
  ------------------

  15 of the 23 functions Qt declares: 6 leans on 'vtable for
  QAnimationTimer', which Qt's library does not offer and Qt's source has no
  code for that could be taken; 3 leans on 'QAnimationTimer; 2 takes or gives
  a type that cannot be passed yet; 2 declared and nowhere to be found; 1 a
  template; 1 Qt's library has no name for it, and its code in Qt's source
  does not compile apart from its file.

  What to expect
  --------------

  - The C++ QAnimationTimer is created at the first use, not by
    'QAnimationTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAnimationTimer.
  - Qt tells when it has removed the C++ QAnimationTimer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAnimationTimer'

  #  A C++ QAnimationTimer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAnimationTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QAnimationTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationtimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QAnimationTimer::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QAnimationTimer10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def runningAnimationCount(self) -> int:
    """
    Calls Qt's 'qsizetype QAnimationTimer::runningAnimationCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationtimer.html#runningAnimationCount
    """
    #  qsizetype QAnimationTimer::runningAnimationCount() const
    ritual = 'ritual_ZNK15QAnimationTimer21runningAnimationCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QAnimationTimer21runningAnimationCountEv'
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

  def restartAnimationTimer(self) -> None:
    """
    Calls Qt's 'void QAnimationTimer::restartAnimationTimer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationtimer.html#restartAnimationTimer
    """
    #  void QAnimationTimer::restartAnimationTimer()
    self.uglySide.call('ritual_ZN15QAnimationTimer21restartAnimationTimerEv')

  @overload(int)
  def updateAnimationsTime(self, delta: int) -> None:
    """
    Calls Qt's 'void QAnimationTimer::updateAnimationsTime(qint64 delta)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationtimer.html#updateAnimationsTime

    Parameters
    ----------

    delta : int
      Passed on as it is.
    """
    #  void QAnimationTimer::updateAnimationsTime(qint64 delta)
    ritual = 'ritual_ZN15QAnimationTimer20updateAnimationsTimeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QAnimationTimer20updateAnimationsTimeEx'
    self.uglySide.call(ritual, delta)

  def startAnimations(self) -> None:
    """
    Calls Qt's 'void QAnimationTimer::startAnimations()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationtimer.html#startAnimations
    """
    #  void QAnimationTimer::startAnimations()
    self.uglySide.call('ritual_ZN15QAnimationTimer15startAnimationsEv')

  def stopTimer(self) -> None:
    """
    Calls Qt's 'void QAnimationTimer::stopTimer()'.

    Qt's own words: https://doc.qt.io/qt-6/qanimationtimer.html#stopTimer
    """
    #  void QAnimationTimer::stopTimer()
    self.uglySide.call('ritual_ZN15QAnimationTimer9stopTimerEv')

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def registerRunningAnimation(
      self,
      animation: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationTimer::registerRunningAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationtimer.html#registerRunningAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationTimer::registerRunningAnimation(QAbstractAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN15QAnimationTimer24registerRunningAnimationEP18QAbstractA'
        'nimation',
        self._addressOf(animation),
    )

  @overload(QAbstractAnimation)
  @overload(NoneType)
  def unregisterRunningAnimation(
      self,
      animation: Optional[QAbstractAnimation],
  ) -> None:
    """
    Calls Qt's 'void
    QAnimationTimer::unregisterRunningAnimation(QAbstractAnimation
    *animation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qanimationtimer.html#unregisterRunningAnimation

    Parameters
    ----------

    animation : Optional[QAbstractAnimation]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QAnimationTimer::unregisterRunningAnimation(QAbstractAnimation
    #      *animation)
    self.uglySide.call(
        'ritual_ZN15QAnimationTimer26unregisterRunningAnimationEP18QAbstrac'
        'tAnimation',
        self._addressOf(animation),
    )
