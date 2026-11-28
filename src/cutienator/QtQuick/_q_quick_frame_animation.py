"""
QQuickFrameAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickframeanimation_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickFrameAnimation to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickFrameAnimation(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQuickFrameAnimation: a plain Python object standing
  in front of one C++ QQuickFrameAnimation.

  It is built on the cute 'QObject', as Qt's QQuickFrameAnimation is built on
  Qt's QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQuickFrameAnimation is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickFrameAnimation that has a ritual and that
  Python can call so far, 27 names in all: 'metaObject', 'tr', 'isRunning',
  'setRunning', 'isPaused', 'setPaused', 'currentFrame', 'frameTime',
  'smoothFrameTime', 'elapsedTime', 'classBegin', 'componentComplete',
  'start', 'stop', 'restart', 'pause', 'resume', 'reset', 'triggered',
  'runningChanged', 'pausedChanged', 'currentFrameChanged',
  'frameTimeChanged', 'smoothFrameTimeChanged', 'elapsedTimeChanged',
  'setCurrentFrame', 'setElapsedTime'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickFrameAnimation::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickFrameAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickFrameAnimationPrivate *QQuickFrameAnimation::d_func()': gives
    'QQuickFrameAnimationPrivate', which has no cute class yet.
  - Qt's 'const QQuickFrameAnimationPrivate *QQuickFrameAnimation::d_func()
    const': gives 'QQuickFrameAnimationPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickFrameAnimation is created at the first use, not by
    'QQuickFrameAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickFrameAnimation.
  - Qt tells when it has removed the C++ QQuickFrameAnimation. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QQuickFrameAnimation::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickFrameAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickFrameAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickFrameAnimation'

  #  Qt's QQuickFrameAnimation is built on more than one class. The part of a
  #  C++ QQuickFrameAnimation that belongs to a class after the first begins
  #  somewhere inside the object, and the ritual named for that class gives
  #  where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuickFrameAnimation_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickFrameAnimation::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickFrameAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickFrameAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QQuickFrameAnimation::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#isRunning
    """
    #  bool QQuickFrameAnimation::isRunning() const
    return self.uglySide.call('ritual_ZNK20QQuickFrameAnimation9isRunningEv')

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QQuickFrameAnimation::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#isPaused
    """
    #  bool QQuickFrameAnimation::isPaused() const
    return self.uglySide.call('ritual_ZNK20QQuickFrameAnimation8isPausedEv')

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QQuickFrameAnimation::currentFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#currentFrame
    """
    #  int QQuickFrameAnimation::currentFrame() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickFrameAnimation12currentFrameEv',
    )

  def frameTime(self) -> float:
    """
    Calls Qt's 'qreal QQuickFrameAnimation::frameTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#frameTime
    """
    #  qreal QQuickFrameAnimation::frameTime() const
    return self.uglySide.call('ritual_ZNK20QQuickFrameAnimation9frameTimeEv')

  def smoothFrameTime(self) -> float:
    """
    Calls Qt's 'qreal QQuickFrameAnimation::smoothFrameTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#smoothFrameTime
    """
    #  qreal QQuickFrameAnimation::smoothFrameTime() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickFrameAnimation15smoothFrameTimeEv',
    )

  def elapsedTime(self) -> float:
    """
    Calls Qt's 'qreal QQuickFrameAnimation::elapsedTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#elapsedTime
    """
    #  qreal QQuickFrameAnimation::elapsedTime() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickFrameAnimation11elapsedTimeEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setRunning(self, running: bool) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::setRunning(bool running)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#setRunning

    Parameters
    ----------

    running : bool
      Passed on as it is.
    """
    #  void QQuickFrameAnimation::setRunning(bool running)
    self.uglySide.call(
        'ritual_ZN20QQuickFrameAnimation10setRunningEb', running,
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::setPaused(bool paused)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QQuickFrameAnimation::setPaused(bool paused)
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation9setPausedEb', paused)

  @overload(int)
  def setCurrentFrame(self, frame: int) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::setCurrentFrame(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#setCurrentFrame

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QQuickFrameAnimation::setCurrentFrame(int frame)
    self.uglySide.call(
        'ritual_ZN20QQuickFrameAnimation15setCurrentFrameEi', frame,
    )

  @overload(float)
  def setElapsedTime(self, elapsedTime: float) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::setElapsedTime(qreal
    elapsedTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#setElapsedTime

    Parameters
    ----------

    elapsedTime : float
      Passed on as it is.
    """
    #  void QQuickFrameAnimation::setElapsedTime(qreal elapsedTime)
    self.uglySide.call(
        'ritual_ZN20QQuickFrameAnimation14setElapsedTimeEd', elapsedTime,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickFrameAnimation::QQuickFrameAnimation(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#QQuickFrameAnimation

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickFrameAnimation::QQuickFrameAnimation(QObject *parent)
    self._noteCreation(QQuickFrameAnimation, lambda: Rituals.call(
        'ritual_ZN20QQuickFrameAnimationC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#classBegin
    """
    #  void QQuickFrameAnimation::classBegin()
    ritual = 'ritual_ZN20QQuickFrameAnimation10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickFrameAnimation10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#componentComplete
    """
    #  void QQuickFrameAnimation::componentComplete()
    ritual = 'ritual_ZN20QQuickFrameAnimation17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickFrameAnimation17componentCompleteEv'
    self.uglySide.call(ritual)

  def start(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#start
    """
    #  void QQuickFrameAnimation::start()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#stop
    """
    #  void QQuickFrameAnimation::stop()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation4stopEv')

  def restart(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#restart
    """
    #  void QQuickFrameAnimation::restart()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation7restartEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#pause
    """
    #  void QQuickFrameAnimation::pause()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#resume
    """
    #  void QQuickFrameAnimation::resume()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation6resumeEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickframeanimation.html#reset
    """
    #  void QQuickFrameAnimation::reset()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation5resetEv')

  def triggered(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::triggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#triggered
    """
    #  void QQuickFrameAnimation::triggered()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation9triggeredEv')

  def runningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::runningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#runningChanged
    """
    #  void QQuickFrameAnimation::runningChanged()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation14runningChangedEv')

  def pausedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::pausedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#pausedChanged
    """
    #  void QQuickFrameAnimation::pausedChanged()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation13pausedChangedEv')

  def currentFrameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::currentFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#currentFrameChanged
    """
    #  void QQuickFrameAnimation::currentFrameChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickFrameAnimation19currentFrameChangedEv',
    )

  def frameTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::frameTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#frameTimeChanged
    """
    #  void QQuickFrameAnimation::frameTimeChanged()
    self.uglySide.call('ritual_ZN20QQuickFrameAnimation16frameTimeChangedEv')

  def smoothFrameTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::smoothFrameTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#smoothFrameTimeChanged
    """
    #  void QQuickFrameAnimation::smoothFrameTimeChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickFrameAnimation22smoothFrameTimeChangedEv',
    )

  def elapsedTimeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickFrameAnimation::elapsedTimeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickframeanimation.html#elapsedTimeChanged
    """
    #  void QQuickFrameAnimation::elapsedTimeChanged()
    self.uglySide.call(
        'ritual_ZN20QQuickFrameAnimation18elapsedTimeChangedEv',
    )
