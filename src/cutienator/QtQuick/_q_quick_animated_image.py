"""
QQuickAnimatedImage binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickanimatedimage_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickAnimatedImage to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QQuickImage, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from . import QQuickAnimatedImagePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickAnimatedImage(QQuickImage):
  """
  The cute side of Qt's QQuickAnimatedImage: a plain Python object standing
  in front of one C++ QQuickAnimatedImage.

  It is built on the cute 'QQuickImage', as Qt's QQuickAnimatedImage is built
  on Qt's QQuickImage, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickAnimatedImage that has a ritual and that
  Python can call so far, 33 names in all: 'metaObject', 'tr', 'isPlaying',
  'setPlaying', 'isPaused', 'setPaused', 'currentFrame', 'setCurrentFrame',
  'frameCount', 'speed', 'setSpeed', 'setSource', 'loops', 'setLoops',
  'finishBehavior', 'setFinishBehavior', 'playingChanged', 'pausedChanged',
  'frameChanged', 'currentFrameChanged', 'frameCountChanged', 'speedChanged',
  'loopsChanged', 'finishBehaviorChanged', 'finished', 'movieUpdate',
  'movieRequestFinished', 'playingStatusChanged', 'onCacheChanged',
  'onMovieFinished', 'load', 'componentComplete', 'd_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickAnimatedImage::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickAnimatedImage::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickAnimatedImage::~QQuickAnimatedImage()': the destructor:
    Python never removes a C++ QQuickAnimatedImage.
  - Qt's 'const QQuickAnimatedImagePrivate *QQuickAnimatedImage::d_func()
    const': takes in Python what 'QQuickAnimatedImagePrivate
    *QQuickAnimatedImage::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 42 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickAnimatedImage is created at the first use, not by
    'QQuickAnimatedImage(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickAnimatedImage.
  - Qt tells when it has removed the C++ QQuickAnimatedImage. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickAnimatedImage, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class FinishBehavior(CuteNum):
    """
    The enum 'QQuickAnimatedImage::FinishBehavior' of Qt, with the 2 names Qt
    gives in it.
    """

    FinishAtInitialFrame = Kee[int](0)
    FinishAtFinalFrame = Kee[int](1)

  class LoopParameters(CuteNum):
    """
    The enum 'QQuickAnimatedImage::LoopParameters' of Qt, with the 1 names Qt
    gives in it.
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
    Calls Qt's 'QString QQuickAnimatedImage::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#tr

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
    #  QString QQuickAnimatedImage::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickAnimatedImage2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickAnimatedImage'

  #  A C++ QQuickAnimatedImage Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickAnimatedImage'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickAnimatedImage::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickAnimatedImage::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickAnimatedImage10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isPlaying(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedImage::isPlaying() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#isPlaying
    """
    #  bool QQuickAnimatedImage::isPlaying() const
    return self.uglySide.call('ritual_ZNK19QQuickAnimatedImage9isPlayingEv')

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QQuickAnimatedImage::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#isPaused
    """
    #  bool QQuickAnimatedImage::isPaused() const
    return self.uglySide.call('ritual_ZNK19QQuickAnimatedImage8isPausedEv')

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedImage::currentFrame() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#currentFrame
    """
    #  int QQuickAnimatedImage::currentFrame() const
    ritual = 'ritual_ZNK19QQuickAnimatedImage12currentFrameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickAnimatedImage12currentFrameEv'
    return self.uglySide.call(ritual)

  def frameCount(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedImage::frameCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#frameCount
    """
    #  int QQuickAnimatedImage::frameCount() const
    ritual = 'ritual_ZNK19QQuickAnimatedImage10frameCountEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QQuickAnimatedImage10frameCountEv'
    return self.uglySide.call(ritual)

  def speed(self) -> float:
    """
    Calls Qt's 'qreal QQuickAnimatedImage::speed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#speed
    """
    #  qreal QQuickAnimatedImage::speed() const
    return self.uglySide.call('ritual_ZNK19QQuickAnimatedImage5speedEv')

  def loops(self) -> int:
    """
    Calls Qt's 'int QQuickAnimatedImage::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#loops
    """
    #  int QQuickAnimatedImage::loops() const
    return self.uglySide.call('ritual_ZNK19QQuickAnimatedImage5loopsEv')

  def finishBehavior(self) -> FinishBehavior:
    """
    Calls Qt's 'FinishBehavior QQuickAnimatedImage::finishBehavior() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#finishBehavior

    Returns
    -------

    FinishBehavior
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FinishBehavior(number)'
      gives.
    """
    #  FinishBehavior QQuickAnimatedImage::finishBehavior() const
    return QQuickAnimatedImage.FinishBehavior(self.uglySide.call(
        'ritual_ZNK19QQuickAnimatedImage14finishBehaviorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setPlaying(self, play: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setPlaying(bool play)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#setPlaying

    Parameters
    ----------

    play : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedImage::setPlaying(bool play)
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage10setPlayingEb', play)

  @overload(bool)
  def setPaused(self, pause: bool) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setPaused(bool pause)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#setPaused

    Parameters
    ----------

    pause : bool
      Passed on as it is.
    """
    #  void QQuickAnimatedImage::setPaused(bool pause)
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage9setPausedEb', pause)

  @overload(int)
  def setCurrentFrame(self, frame: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setCurrentFrame(int frame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#setCurrentFrame

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QQuickAnimatedImage::setCurrentFrame(int frame)
    ritual = 'ritual_ZN19QQuickAnimatedImage15setCurrentFrameEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnimatedImage15setCurrentFrameEi'
    self.uglySide.call(ritual, frame)

  @overload(float)
  def setSpeed(self, speed: float) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setSpeed(qreal speed)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#setSpeed

    Parameters
    ----------

    speed : float
      Passed on as it is.
    """
    #  void QQuickAnimatedImage::setSpeed(qreal speed)
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage8setSpeedEd', speed)

  @overload(QUrl)
  def setSource(self, a0: QUrl) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setSource(const QUrl &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#setSource

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuickAnimatedImage::setSource(const QUrl &a0)
    ritual = 'ritual_ZN19QQuickAnimatedImage9setSourceERK4QUrl'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnimatedImage9setSourceERK4QUrl'
    self.uglySide.call(ritual, self._valueOf(a0))

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QQuickAnimatedImage::setLoops(int loops)
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage8setLoopsEi', loops)

  @overload(FinishBehavior)
  def setFinishBehavior(self, behavior: FinishBehavior) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::setFinishBehavior(FinishBehavior
    behavior)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#setFinishBehavior

    Parameters
    ----------

    behavior : FinishBehavior
      Passed on as its number.
    """
    #  void QQuickAnimatedImage::setFinishBehavior(FinishBehavior behavior)
    self.uglySide.call(
        'ritual_ZN19QQuickAnimatedImage17setFinishBehaviorENS_14FinishBehav'
        'iorE',
        behavior.value,
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
    'QQuickAnimatedImage::QQuickAnimatedImage(QQuickItem *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#QQuickAnimatedImage

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickAnimatedImage::QQuickAnimatedImage(QQuickItem *parent)
    self._noteCreation(QQuickAnimatedImage, lambda: Rituals.call(
        'ritual_ZN19QQuickAnimatedImageC1EP10QQuickItem',
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

  def playingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::playingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#playingChanged
    """
    #  void QQuickAnimatedImage::playingChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage14playingChangedEv')

  def pausedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::pausedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#pausedChanged
    """
    #  void QQuickAnimatedImage::pausedChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage13pausedChangedEv')

  def frameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::frameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#frameChanged
    """
    #  void QQuickAnimatedImage::frameChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage12frameChangedEv')

  def currentFrameChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::currentFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#currentFrameChanged
    """
    #  void QQuickAnimatedImage::currentFrameChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickAnimatedImage19currentFrameChangedEv',
    )

  def frameCountChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::frameCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#frameCountChanged
    """
    #  void QQuickAnimatedImage::frameCountChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage17frameCountChangedEv')

  def speedChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::speedChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#speedChanged
    """
    #  void QQuickAnimatedImage::speedChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage12speedChangedEv')

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::loopsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#loopsChanged
    """
    #  void QQuickAnimatedImage::loopsChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage12loopsChangedEv')

  def finishBehaviorChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::finishBehaviorChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#finishBehaviorChanged
    """
    #  void QQuickAnimatedImage::finishBehaviorChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickAnimatedImage21finishBehaviorChangedEv',
    )

  def finished(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#finished
    """
    #  void QQuickAnimatedImage::finished()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage8finishedEv')

  def movieUpdate(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::movieUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#movieUpdate
    """
    #  void QQuickAnimatedImage::movieUpdate()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage11movieUpdateEv')

  def movieRequestFinished(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::movieRequestFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#movieRequestFinished
    """
    #  void QQuickAnimatedImage::movieRequestFinished()
    self.uglySide.call(
        'ritual_ZN19QQuickAnimatedImage20movieRequestFinishedEv',
    )

  def playingStatusChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::playingStatusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#playingStatusChanged
    """
    #  void QQuickAnimatedImage::playingStatusChanged()
    self.uglySide.call(
        'ritual_ZN19QQuickAnimatedImage20playingStatusChangedEv',
    )

  def onCacheChanged(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::onCacheChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#onCacheChanged
    """
    #  void QQuickAnimatedImage::onCacheChanged()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage14onCacheChangedEv')

  def onMovieFinished(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::onMovieFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#onMovieFinished
    """
    #  void QQuickAnimatedImage::onMovieFinished()
    self.uglySide.call('ritual_ZN19QQuickAnimatedImage15onMovieFinishedEv')

  def load(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#load
    """
    #  void QQuickAnimatedImage::load()
    ritual = 'ritual_ZN19QQuickAnimatedImage4loadEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnimatedImage4loadEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickAnimatedImage::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickanimatedimage.html#componentComplete
    """
    #  void QQuickAnimatedImage::componentComplete()
    ritual = 'ritual_ZN19QQuickAnimatedImage17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickAnimatedImage17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickAnimatedImagePrivate]:
    """
    Calls Qt's 'QQuickAnimatedImagePrivate *QQuickAnimatedImage::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickanimatedimage.html#d_func

    Returns
    -------

    Optional[QQuickAnimatedImagePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAnimatedImagePrivate *QQuickAnimatedImage::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickAnimatedImage6d_funcEv')
    from . import QQuickAnimatedImagePrivate
    return QQuickAnimatedImagePrivate._cuteAt(address)
