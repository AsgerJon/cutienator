"""
QQuickAnimatedSprite binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatedsprite_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickAnimatedSprite to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQuickAnimatedSpritePrivate, QSGNode, QSGSpriteNode
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSGNode = WAIT['QSGNode']
  QSGSpriteNode = WAIT['QSGSpriteNode']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatedSprite(QQuickItem):
  """
  The cute side of Qt's QQuickAnimatedSprite: a plain Python object standing
  in front of one C++ QQuickAnimatedSprite.

  It is built on the cute 'QQuickItem', as Qt's QQuickAnimatedSprite is built
  on Qt's QQuickItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatedSprite that has a ritual and that
  Python can call so far, 70 names in all: 'metaObject', 'tr', 'running',
  'interpolate', 'source', 'reverse', 'frameSync', 'frameCount',
  'frameHeight', 'frameWidth', 'frameX', 'frameY', 'frameRate',
  'frameDuration', 'loops', 'paused', 'currentFrame', 'finishBehavior',
  'setFinishBehavior', 'pausedChanged', 'runningChanged',
  'interpolateChanged', 'sourceChanged', 'reverseChanged',
  'frameSyncChanged', 'frameCountChanged', 'frameHeightChanged',
  'frameWidthChanged', 'frameXChanged', 'frameYChanged', 'frameRateChanged',
  'frameDurationChanged', 'loopsChanged', 'currentFrameChanged',
  'finishBehaviorChanged', 'finished', 'start', 'stop', 'restart', 'advance',
  'pause', 'resume', 'setRunning', 'setPaused', 'setInterpolate',
  'setSource', 'setReverse', 'setFrameSync', 'setFrameCount',
  'setFrameHeight', 'setFrameWidth', 'setFrameX', 'setFrameY',
  'setFrameRate', 'setFrameDuration', 'resetFrameRate', 'resetFrameDuration',
  'setLoops', 'setCurrentFrame', 'createEngine', 'reset',
  'componentComplete', 'updatePaintNode', 'itemChange', 'maybeUpdate',
  'isCurrentFrameChangedConnected', 'prepareNextFrame', 'reloadImage',
  'initNode', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimatedSprite::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAnimatedSprite::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QQuickAnimatedSpritePrivate *QQuickAnimatedSprite::d_func()
    const': takes in Python what 'QQuickAnimatedSpritePrivate
    *QQuickAnimatedSprite::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 76 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickAnimatedSprite is created at the first use, not by
    'QQuickAnimatedSprite(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatedSprite.
  - Qt tells when it has removed the C++ QQuickAnimatedSprite. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickAnimatedSprite, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FinishBehavior(CuteNum):
    """
    The enum 'QQuickAnimatedSprite::FinishBehavior' of Qt, with the 2 names
    Qt gives in it.
    """

    FinishAtInitialFrame = Kee[int](0)
    FinishAtFinalFrame = Kee[int](1)

  class LoopParameters(CuteNum):
    """
    The enum 'QQuickAnimatedSprite::LoopParameters' of Qt, with the 1 names
    Qt gives in it.
    """

    Infinite = Kee[int](-1)

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
    Calls Qt's 'QString QQuickAnimatedSprite::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#tr

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
    #  QString QQuickAnimatedSprite::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QQuickAnimatedSprite2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatedSprite'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnimatedSprite::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimatedSprite::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def running(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedSprite::running() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#running
    """
    #  bool QQuickAnimatedSprite::running() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite7runningEv')

  def interpolate(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedSprite::interpolate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#interpolate
    """
    #  bool QQuickAnimatedSprite::interpolate() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite11interpolateEv',
    )

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuickAnimatedSprite::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuickAnimatedSprite::source() const
    address = self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def reverse(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedSprite::reverse() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#reverse
    """
    #  bool QQuickAnimatedSprite::reverse() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite7reverseEv')

  def frameSync(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedSprite::frameSync() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameSync
    """
    #  bool QQuickAnimatedSprite::frameSync() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite9frameSyncEv')

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::frameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameCount
    """
    #  int QQuickAnimatedSprite::frameCount() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite10frameCountEv',
    )

  def frameHeight(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::frameHeight() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameHeight
    """
    #  int QQuickAnimatedSprite::frameHeight() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite11frameHeightEv',
    )

  def frameWidth(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::frameWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameWidth
    """
    #  int QQuickAnimatedSprite::frameWidth() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite10frameWidthEv',
    )

  def frameX(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::frameX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameX
    """
    #  int QQuickAnimatedSprite::frameX() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite6frameXEv')

  def frameY(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::frameY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameY
    """
    #  int QQuickAnimatedSprite::frameY() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite6frameYEv')

  def frameRate(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimatedSprite::frameRate() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameRate
    """
    #  qreal QQuickAnimatedSprite::frameRate() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite9frameRateEv')

  def frameDuration(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::frameDuration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameDuration
    """
    #  int QQuickAnimatedSprite::frameDuration() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite13frameDurationEv',
    )

  def loops(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#loops
    """
    #  int QQuickAnimatedSprite::loops() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite5loopsEv')

  def paused(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedSprite::paused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#paused
    """
    #  bool QQuickAnimatedSprite::paused() const
    return self.uglySide.call('ritual_ZNK20QQuickAnimatedSprite6pausedEv')

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedSprite::currentFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#currentFrame
    """
    #  int QQuickAnimatedSprite::currentFrame() const
    return self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite12currentFrameEv',
    )

  def finishBehavior(self) -> FinishBehavior:
    """
    Calls Qt's 'FinishBehavior QQuickAnimatedSprite::finishBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#finishBehavior

    Returns
    -------

    FinishBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FinishBehavior(number)'
      gives.
    """
    #  FinishBehavior QQuickAnimatedSprite::finishBehavior() const
    return QQuickAnimatedSprite.FinishBehavior(self.uglySide.call(
        'ritual_ZNK20QQuickAnimatedSprite14finishBehaviorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(FinishBehavior)
  def setFinishBehavior(self, arg: FinishBehavior) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFinishBehavior(FinishBehavior
    arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFinishBehavior

    Parameters
    ----------

    arg : FinishBehavior
      Passed on as its number.
    """
    #  void QQuickAnimatedSprite::setFinishBehavior(FinishBehavior arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite17setFinishBehaviorENS_14FinishBeha'
        'viorE',
        arg.value,
    )

  @overload(bool)
  def setRunning(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setRunning(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setRunning

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setRunning(bool arg)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite10setRunningEb', arg)

  @overload(bool)
  def setPaused(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setPaused(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setPaused

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setPaused(bool arg)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite9setPausedEb', arg)

  @overload(bool)
  def setInterpolate(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setInterpolate(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setInterpolate

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setInterpolate(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite14setInterpolateEb', arg,
    )

  @overload(QUrl)
  def setSource(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setSource(const QUrl &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setSource

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickAnimatedSprite::setSource(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite9setSourceERK4QUrl',
        self._valueOf(arg),
    )

  @overload(bool)
  def setReverse(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setReverse(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setReverse

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setReverse(bool arg)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite10setReverseEb', arg)

  @overload(bool)
  def setFrameSync(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameSync(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameSync

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameSync(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite12setFrameSyncEb', arg,
    )

  @overload(int)
  def setFrameCount(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameCount(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameCount

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameCount(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite13setFrameCountEi', arg,
    )

  @overload(int)
  def setFrameHeight(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameHeight(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameHeight

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameHeight(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite14setFrameHeightEi', arg,
    )

  @overload(int)
  def setFrameWidth(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameWidth(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameWidth

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameWidth(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite13setFrameWidthEi', arg,
    )

  @overload(int)
  def setFrameX(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameX(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameX

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameX(int arg)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite9setFrameXEi', arg)

  @overload(int)
  def setFrameY(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameY(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameY

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameY(int arg)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite9setFrameYEi', arg)

  @overload(float)
  def setFrameRate(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameRate(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameRate

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameRate(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite12setFrameRateEd', arg,
    )

  @overload(int)
  def setFrameDuration(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setFrameDuration(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setFrameDuration

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setFrameDuration(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite16setFrameDurationEi', arg,
    )

  @overload(int)
  def setLoops(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setLoops(int arg)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#setLoops

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setLoops(int arg)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite8setLoopsEi', arg)

  @overload(int)
  def setCurrentFrame(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::setCurrentFrame(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#setCurrentFrame

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::setCurrentFrame(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite15setCurrentFrameEi', arg,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickAnimatedSprite::QQuickAnimatedSprite(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#QQuickAnimatedSprite

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnimatedSprite::QQuickAnimatedSprite(QQuickItem *parent)
    self._noteCreation(QQuickAnimatedSprite, lambda: Rituals.call(
        'ritual_ZN20QQuickAnimatedSpriteC1EP10QQuickItem',
        self._addressOf(parent),
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

  @overload(bool)
  def pausedChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::pausedChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#pausedChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::pausedChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite13pausedChangedEb', arg,
    )

  @overload(bool)
  def runningChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::runningChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#runningChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::runningChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite14runningChangedEb', arg,
    )

  @overload(bool)
  def interpolateChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::interpolateChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#interpolateChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::interpolateChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite18interpolateChangedEb', arg,
    )

  @overload(QUrl)
  def sourceChanged(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::sourceChanged(const QUrl &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#sourceChanged

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickAnimatedSprite::sourceChanged(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite13sourceChangedERK4QUrl',
        self._valueOf(arg),
    )

  @overload(bool)
  def reverseChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::reverseChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#reverseChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::reverseChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite14reverseChangedEb', arg,
    )

  @overload(bool)
  def frameSyncChanged(self, arg: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameSyncChanged(bool arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameSyncChanged

    Parameters
    ----------

    arg : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameSyncChanged(bool arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite16frameSyncChangedEb', arg,
    )

  @overload(int)
  def frameCountChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameCountChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameCountChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameCountChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite17frameCountChangedEi', arg,
    )

  @overload(int)
  def frameHeightChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameHeightChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameHeightChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameHeightChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite18frameHeightChangedEi', arg,
    )

  @overload(int)
  def frameWidthChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameWidthChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameWidthChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameWidthChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite17frameWidthChangedEi', arg,
    )

  @overload(int)
  def frameXChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameXChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameXChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameXChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite13frameXChangedEi', arg,
    )

  @overload(int)
  def frameYChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameYChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameYChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameYChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite13frameYChangedEi', arg,
    )

  @overload(float)
  def frameRateChanged(self, arg: float) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameRateChanged(qreal arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameRateChanged

    Parameters
    ----------

    arg : float
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameRateChanged(qreal arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite16frameRateChangedEd', arg,
    )

  @overload(int)
  def frameDurationChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::frameDurationChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#frameDurationChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::frameDurationChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite20frameDurationChangedEi', arg,
    )

  @overload(int)
  def loopsChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::loopsChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#loopsChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::loopsChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite12loopsChangedEi', arg,
    )

  @overload(int)
  def currentFrameChanged(self, arg: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::currentFrameChanged(int arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#currentFrameChanged

    Parameters
    ----------

    arg : int
      Passed on as it is.
    """
    #  void QQuickAnimatedSprite::currentFrameChanged(int arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite19currentFrameChangedEi', arg,
    )

  @overload(FinishBehavior)
  def finishBehaviorChanged(self, arg: FinishBehavior) -> None:
    """
    Calls Qt's 'void
    QQuickAnimatedSprite::finishBehaviorChanged(QQuickAnimatedSprite::
    FinishBehavior arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#finishBehaviorChanged

    Parameters
    ----------

    arg : FinishBehavior
      Passed on as its number.
    """
    #  void QQuickAnimatedSprite::finishBehaviorChanged(
    #      QQuickAnimatedSprite::FinishBehavior arg)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite21finishBehaviorChangedENS_14Finish'
        'BehaviorE',
        arg.value,
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#finished
    """
    #  void QQuickAnimatedSprite::finished()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite8finishedEv')

  def start(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#start
    """
    #  void QQuickAnimatedSprite::start()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#stop
    """
    #  void QQuickAnimatedSprite::stop()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite4stopEv')

  def restart(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#restart
    """
    #  void QQuickAnimatedSprite::restart()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite7restartEv')

  @overload()
  @overload(int)
  def advance(self, frames: int = 1) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::advance(int frames)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#advance

    Parameters
    ----------

    frames : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QQuickAnimatedSprite::advance(int frames)
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite7advanceEi', frames)

  def pause(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#pause
    """
    #  void QQuickAnimatedSprite::pause()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite5pauseEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#resume
    """
    #  void QQuickAnimatedSprite::resume()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite6resumeEv')

  def resetFrameRate(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::resetFrameRate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#resetFrameRate
    """
    #  void QQuickAnimatedSprite::resetFrameRate()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite14resetFrameRateEv')

  def resetFrameDuration(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::resetFrameDuration()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#resetFrameDuration
    """
    #  void QQuickAnimatedSprite::resetFrameDuration()
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite18resetFrameDurationEv',
    )

  def createEngine(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::createEngine()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#createEngine
    """
    #  void QQuickAnimatedSprite::createEngine()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite12createEngineEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#reset
    """
    #  void QQuickAnimatedSprite::reset()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite5resetEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#componentComplete
    """
    #  void QQuickAnimatedSprite::componentComplete()
    ritual = 'ritual_ZN20QQuickAnimatedSprite17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QQuickAnimatedSprite17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QSGNode, QQuickItem.UpdatePaintNodeData)
  @overload(QSGNode, NoneType)
  @overload(NoneType, QQuickItem.UpdatePaintNodeData)
  @overload(NoneType, NoneType)
  def updatePaintNode(
      self,
      a0: Optional[QSGNode],
      a1: Optional[QQuickItem.UpdatePaintNodeData],
  ) -> Optional[QSGNode]:
    """
    Calls Qt's 'QSGNode *QQuickAnimatedSprite::updatePaintNode(QSGNode *a0,
    UpdatePaintNodeData *a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#updatePaintNode

    Parameters
    ----------

    a0 : Optional[QSGNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QQuickItem.UpdatePaintNodeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSGNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGNode *QQuickAnimatedSprite::updatePaintNode(QSGNode *a0,
    #      UpdatePaintNodeData *a1)
    ritual = (
        'ritual_ZN20QQuickAnimatedSprite15updatePaintNodeEP7QSGNodePN10QQui'
        'ckItem19UpdatePaintNodeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAnimatedSprite15updatePaintNodeEP7QSGNodePN'
          '10QQuickItem19UpdatePaintNodeDataE')
    address = self.uglySide.call(
        ritual, self._addressOf(a0, 'QSGNode'), self._addressOf(a1),
    )
    from . import QSGNode
    return QSGNode._cuteAt(address)

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::itemChange(ItemChange a0, const
    ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickAnimatedSprite::itemChange(ItemChange a0, const
    #      ItemChangeData &a1)
    ritual = (
        'ritual_ZN20QQuickAnimatedSprite10itemChangeEN10QQuickItem10ItemCha'
        'ngeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuickAnimatedSprite10itemChangeEN10QQuickItem10I'
          'temChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def maybeUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::maybeUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#maybeUpdate
    """
    #  void QQuickAnimatedSprite::maybeUpdate()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite11maybeUpdateEv')

  def isCurrentFrameChangedConnected(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedSprite::isCurrentFrameChangedConnected()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html
    """
    #  bool QQuickAnimatedSprite::isCurrentFrameChangedConnected()
    return self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite30isCurrentFrameChangedConnectedEv',
    )

  @overload(QSGSpriteNode)
  @overload(NoneType)
  def prepareNextFrame(self, node: Optional[QSGSpriteNode]) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::prepareNextFrame(QSGSpriteNode
    *node)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#prepareNextFrame

    Parameters
    ----------

    node : Optional[QSGSpriteNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickAnimatedSprite::prepareNextFrame(QSGSpriteNode *node)
    self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite16prepareNextFrameEP13QSGSpriteNode',
        self._addressOf(node),
    )

  def reloadImage(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedSprite::reloadImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedsprite.html#reloadImage
    """
    #  void QQuickAnimatedSprite::reloadImage()
    self.uglySide.call('ritual_ZN20QQuickAnimatedSprite11reloadImageEv')

  def initNode(self) -> Optional[QSGSpriteNode]:
    """
    Calls Qt's 'QSGSpriteNode *QQuickAnimatedSprite::initNode()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#initNode

    Returns
    -------

    Optional[QSGSpriteNode]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGSpriteNode *QQuickAnimatedSprite::initNode()
    address = self.uglySide.call(
        'ritual_ZN20QQuickAnimatedSprite8initNodeEv',
    )
    from . import QSGSpriteNode
    return QSGSpriteNode._cuteAt(address)

  def d_func(self) -> Optional[QQuickAnimatedSpritePrivate]:
    """
    Calls Qt's 'QQuickAnimatedSpritePrivate *QQuickAnimatedSprite::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedsprite.html#d_func

    Returns
    -------

    Optional[QQuickAnimatedSpritePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatedSpritePrivate *QQuickAnimatedSprite::d_func()
    address = self.uglySide.call('ritual_ZN20QQuickAnimatedSprite6d_funcEv')
    from . import QQuickAnimatedSpritePrivate
    return QQuickAnimatedSpritePrivate._cuteAt(address)
