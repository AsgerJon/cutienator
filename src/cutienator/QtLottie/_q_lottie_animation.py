"""
QLottieAnimation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLottie/6.12.0/QtLottie/private/qlottieanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QLottieAnimation to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QUrl, QVersionNumber
  from ..QtGui import QPainter
  from ..QtQuick import QQuickItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QPainter = WAIT['QPainter']
  QQuickItem = WAIT['QQuickItem']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QLottieAnimation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLottieAnimation: a plain Python object standing in
  front of one C++ QLottieAnimation.

  What exists
  -----------

  Every function of Qt's QLottieAnimation that has a ritual and that Python
  can call so far, 47 names in all: 'metaObject', 'tr', 'paint', 'status',
  'source', 'setSource', 'frameRate', 'setFrameRate', 'resetFrameRate',
  'quality', 'setQuality', 'direction', 'setDirection', 'startFrame',
  'endFrame', 'currentFrame', 'version', 'start', 'play', 'pause',
  'togglePause', 'stop', 'gotoAndPlay', 'gotoAndStop', 'getDuration',
  'jsonSource', 'statusChanged', 'qualityChanged', 'sourceChanged',
  'finished', 'frameRateChanged', 'autoPlayChanged', 'loopsChanged',
  'directionChanged', 'startFrameChanged', 'endFrameChanged',
  'currentFrameChanged', 'loadFinished', 'renderNextFrame',
  'componentComplete', 'setStatus', 'setStartFrame', 'setEndFrame', 'load',
  'parse', 'gotoFrame', 'reset'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QLottieAnimation::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QLottieAnimation::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QLottieAnimation::~QLottieAnimation()': the destructor: Python
    never removes a C++ QLottieAnimation.

  What has no ritual
  ------------------

  2 of the 55 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QLottieAnimation is created at the first use, not by
    'QLottieAnimation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLottieAnimation.
  - Qt tells when it has removed the C++ QLottieAnimation. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QLottieAnimation, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Direction(CuteNum):
    """
    The enum 'QLottieAnimation::Direction' of Qt, with the 2 names Qt gives
    in it.
    """

    Forward = Kee[int](1)
    Reverse = Kee[int](-1)

  class LoopCount(CuteNum):
    """
    The enum 'QLottieAnimation::LoopCount' of Qt, with the 1 names Qt gives
    in it.
    """

    Infinite = Kee[int](-1)

  class Quality(CuteNum):
    """
    The enum 'QLottieAnimation::Quality' of Qt, with the 3 names Qt gives in
    it.
    """

    LowQuality = Kee[int](0)
    MediumQuality = Kee[int](1)
    HighQuality = Kee[int](2)

  class Status(CuteNum):
    """
    The enum 'QLottieAnimation::Status' of Qt, with the 4 names Qt gives in
    it.
    """

    Null = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString QLottieAnimation::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#tr

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
    #  QString QLottieAnimation::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QLottieAnimation2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLottieAnimation'

  #  A C++ QLottieAnimation Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QLottieAnimation'

  #  The functions Qt calls itself that QLottieAnimation is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'parse': (
          ('_ZN16QLottieAnimation5parseERK10QByteArray',
           ('int', 'number', ''),
           (
               ('address', 'value', 'QtCore:QByteArray'),
           )),
      ),
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
    Calls Qt's 'const QMetaObject *QLottieAnimation::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QLottieAnimation::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QLottieAnimation10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status QLottieAnimation::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QLottieAnimation::status() const
    return QLottieAnimation.Status(self.uglySide.call(
        'ritual_ZNK16QLottieAnimation6statusEv',
    ))

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QLottieAnimation::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QLottieAnimation::source() const
    address = self.uglySide.call('ritual_ZNK16QLottieAnimation6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def frameRate(self) -> int:
    """
    Calls Qt's 'int QLottieAnimation::frameRate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#frameRate
    """
    #  int QLottieAnimation::frameRate() const
    return self.uglySide.call('ritual_ZNK16QLottieAnimation9frameRateEv')

  def quality(self) -> Quality:
    """
    Calls Qt's 'Quality QLottieAnimation::quality() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#quality

    Returns
    -------

    Quality
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Quality(number)' gives.
    """
    #  Quality QLottieAnimation::quality() const
    return QLottieAnimation.Quality(self.uglySide.call(
        'ritual_ZNK16QLottieAnimation7qualityEv',
    ))

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QLottieAnimation::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QLottieAnimation::direction() const
    return QLottieAnimation.Direction(self.uglySide.call(
        'ritual_ZNK16QLottieAnimation9directionEv',
    ))

  def startFrame(self) -> int:
    """
    Calls Qt's 'int QLottieAnimation::startFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#startFrame
    """
    #  int QLottieAnimation::startFrame() const
    return self.uglySide.call('ritual_ZNK16QLottieAnimation10startFrameEv')

  def endFrame(self) -> int:
    """
    Calls Qt's 'int QLottieAnimation::endFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#endFrame
    """
    #  int QLottieAnimation::endFrame() const
    return self.uglySide.call('ritual_ZNK16QLottieAnimation8endFrameEv')

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QLottieAnimation::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#currentFrame
    """
    #  int QLottieAnimation::currentFrame() const
    return self.uglySide.call('ritual_ZNK16QLottieAnimation12currentFrameEv')

  def version(self) -> QVersionNumber:
    """
    Calls Qt's 'QVersionNumber QLottieAnimation::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#version

    Returns
    -------

    QVersionNumber
      A new cute QVersionNumber around the copy Qt gave back. Python owns it.
    """
    #  QVersionNumber QLottieAnimation::version() const
    address = self.uglySide.call('ritual_ZNK16QLottieAnimation7versionEv')
    from ..QtCore import QVersionNumber
    return QVersionNumber._cuteOwning(address)

  def jsonSource(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QLottieAnimation::jsonSource() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#jsonSource

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QLottieAnimation::jsonSource() const
    address = self.uglySide.call(
        'ritual_ZNK16QLottieAnimation10jsonSourceEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setSource(const QUrl &source)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QLottieAnimation::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(int)
  def setFrameRate(self, frameRate: int) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setFrameRate(int frameRate)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#setFrameRate

    Parameters
    ----------

    frameRate : int
      Passed on as it is.
    """
    #  void QLottieAnimation::setFrameRate(int frameRate)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation12setFrameRateEi', frameRate,
    )

  @overload(Quality)
  def setQuality(self, quality: Quality) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setQuality(Quality quality)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#setQuality

    Parameters
    ----------

    quality : Quality
      Passed on as its number.
    """
    #  void QLottieAnimation::setQuality(Quality quality)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation10setQualityENS_7QualityE',
        quality.value,
    )

  @overload(Direction)
  def setDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setDirection(Direction direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#setDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QLottieAnimation::setDirection(Direction direction)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation12setDirectionENS_9DirectionE',
        direction.value,
    )

  @overload(Status)
  def setStatus(self, status: Status) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setStatus(Status status)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void QLottieAnimation::setStatus(Status status)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation9setStatusENS_6StatusE', status.value,
    )

  @overload(int)
  def setStartFrame(self, startFrame: int) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setStartFrame(int startFrame)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#setStartFrame

    Parameters
    ----------

    startFrame : int
      Passed on as it is.
    """
    #  void QLottieAnimation::setStartFrame(int startFrame)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation13setStartFrameEi', startFrame,
    )

  @overload(int)
  def setEndFrame(self, endFrame: int) -> None:
    """
    Calls Qt's 'void QLottieAnimation::setEndFrame(int endFrame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#setEndFrame

    Parameters
    ----------

    endFrame : int
      Passed on as it is.
    """
    #  void QLottieAnimation::setEndFrame(int endFrame)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation11setEndFrameEi', endFrame,
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
    'QLottieAnimation::QLottieAnimation(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#QLottieAnimation

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QLottieAnimation::QLottieAnimation(QQuickItem *parent)
    self._noteCreation(QLottieAnimation, lambda: Rituals.call(
        'ritual_ZN16QLottieAnimationC1EP10QQuickItem',
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

  @overload(QPainter)
  @overload(NoneType)
  def paint(self, painter: Optional[QPainter]) -> None:
    """
    Calls Qt's 'void QLottieAnimation::paint(QPainter *painter)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#paint

    Parameters
    ----------

    painter : Optional[QPainter]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QLottieAnimation::paint(QPainter *painter)
    ritual = 'ritual_ZN16QLottieAnimation5paintEP8QPainter'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QLottieAnimation5paintEP8QPainter'
    self.uglySide.call(ritual, self._addressOf(painter))

  def resetFrameRate(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::resetFrameRate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#resetFrameRate
    """
    #  void QLottieAnimation::resetFrameRate()
    self.uglySide.call('ritual_ZN16QLottieAnimation14resetFrameRateEv')

  def start(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#start
    """
    #  void QLottieAnimation::start()
    self.uglySide.call('ritual_ZN16QLottieAnimation5startEv')

  def play(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#play
    """
    #  void QLottieAnimation::play()
    self.uglySide.call('ritual_ZN16QLottieAnimation4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#pause
    """
    #  void QLottieAnimation::pause()
    self.uglySide.call('ritual_ZN16QLottieAnimation5pauseEv')

  def togglePause(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::togglePause()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#togglePause
    """
    #  void QLottieAnimation::togglePause()
    self.uglySide.call('ritual_ZN16QLottieAnimation11togglePauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#stop
    """
    #  void QLottieAnimation::stop()
    self.uglySide.call('ritual_ZN16QLottieAnimation4stopEv')

  @overload(int)
  def gotoAndPlay(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieAnimation::gotoAndPlay(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#gotoAndPlay

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieAnimation::gotoAndPlay(int frame)
    self.uglySide.call('ritual_ZN16QLottieAnimation11gotoAndPlayEi', frame)

  @overload(str)
  def gotoAndPlay(self, frameMarker: str) -> bool:
    """
    Calls Qt's 'bool QLottieAnimation::gotoAndPlay(const QString
    &frameMarker)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#gotoAndPlay

    Parameters
    ----------

    frameMarker : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QLottieAnimation::gotoAndPlay(const QString &frameMarker)
    return self.uglySide.call(
        'ritual_ZN16QLottieAnimation11gotoAndPlayERK7QString', frameMarker,
    )

  @overload(int)
  def gotoAndStop(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieAnimation::gotoAndStop(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#gotoAndStop

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieAnimation::gotoAndStop(int frame)
    self.uglySide.call('ritual_ZN16QLottieAnimation11gotoAndStopEi', frame)

  @overload(str)
  def gotoAndStop(self, frameMarker: str) -> bool:
    """
    Calls Qt's 'bool QLottieAnimation::gotoAndStop(const QString
    &frameMarker)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#gotoAndStop

    Parameters
    ----------

    frameMarker : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QLottieAnimation::gotoAndStop(const QString &frameMarker)
    return self.uglySide.call(
        'ritual_ZN16QLottieAnimation11gotoAndStopERK7QString', frameMarker,
    )

  @overload()
  @overload(bool)
  def getDuration(self, inFrames: bool = False) -> float:
    """
    Calls Qt's 'double QLottieAnimation::getDuration(bool inFrames)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#getDuration

    Parameters
    ----------

    inFrames : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  double QLottieAnimation::getDuration(bool inFrames)
    return self.uglySide.call(
        'ritual_ZN16QLottieAnimation11getDurationEb', inFrames,
    )

  def statusChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::statusChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#statusChanged
    """
    #  void QLottieAnimation::statusChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation13statusChangedEv')

  def qualityChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::qualityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#qualityChanged
    """
    #  void QLottieAnimation::qualityChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation14qualityChangedEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#sourceChanged
    """
    #  void QLottieAnimation::sourceChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation13sourceChangedEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#finished
    """
    #  void QLottieAnimation::finished()
    self.uglySide.call('ritual_ZN16QLottieAnimation8finishedEv')

  def frameRateChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::frameRateChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#frameRateChanged
    """
    #  void QLottieAnimation::frameRateChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation16frameRateChangedEv')

  def autoPlayChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::autoPlayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#autoPlayChanged
    """
    #  void QLottieAnimation::autoPlayChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation15autoPlayChangedEv')

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::loopsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#loopsChanged
    """
    #  void QLottieAnimation::loopsChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation12loopsChangedEv')

  def directionChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::directionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#directionChanged
    """
    #  void QLottieAnimation::directionChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation16directionChangedEv')

  def startFrameChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::startFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#startFrameChanged
    """
    #  void QLottieAnimation::startFrameChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation17startFrameChangedEv')

  def endFrameChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::endFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#endFrameChanged
    """
    #  void QLottieAnimation::endFrameChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation15endFrameChangedEv')

  def currentFrameChanged(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::currentFrameChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#currentFrameChanged
    """
    #  void QLottieAnimation::currentFrameChanged()
    self.uglySide.call('ritual_ZN16QLottieAnimation19currentFrameChangedEv')

  @overload(QByteArray)
  def loadFinished(self, json: QByteArray) -> None:
    """
    Calls Qt's 'void QLottieAnimation::loadFinished(const QByteArray &json)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#loadFinished

    Parameters
    ----------

    json : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QLottieAnimation::loadFinished(const QByteArray &json)
    self.uglySide.call(
        'ritual_ZN16QLottieAnimation12loadFinishedERK10QByteArray',
        self._valueOf(json),
    )

  def renderNextFrame(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::renderNextFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#renderNextFrame
    """
    #  void QLottieAnimation::renderNextFrame()
    self.uglySide.call('ritual_ZN16QLottieAnimation15renderNextFrameEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qlottieanimation.html#componentComplete
    """
    #  void QLottieAnimation::componentComplete()
    ritual = 'ritual_ZN16QLottieAnimation17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QLottieAnimation17componentCompleteEv'
    self.uglySide.call(ritual)

  def load(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::load()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#load
    """
    #  void QLottieAnimation::load()
    self.uglySide.call('ritual_ZN16QLottieAnimation4loadEv')

  @overload(QByteArray)
  def parse(self, jsonSource: QByteArray) -> int:
    """
    Calls Qt's 'int QLottieAnimation::parse(const QByteArray &jsonSource)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#parse

    Parameters
    ----------

    jsonSource : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  int QLottieAnimation::parse(const QByteArray &jsonSource)
    ritual = 'ritual_ZN16QLottieAnimation5parseERK10QByteArray'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QLottieAnimation5parseERK10QByteArray'
    return self.uglySide.call(ritual, self._valueOf(jsonSource))

  @overload(int)
  def gotoFrame(self, frame: int) -> None:
    """
    Calls Qt's 'void QLottieAnimation::gotoFrame(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#gotoFrame

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QLottieAnimation::gotoFrame(int frame)
    self.uglySide.call('ritual_ZN16QLottieAnimation9gotoFrameEi', frame)

  def reset(self) -> None:
    """
    Calls Qt's 'void QLottieAnimation::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qlottieanimation.html#reset
    """
    #  void QLottieAnimation::reset()
    self.uglySide.call('ritual_ZN16QLottieAnimation5resetEv')
