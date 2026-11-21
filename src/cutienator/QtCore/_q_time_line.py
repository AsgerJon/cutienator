"""
QTimeLine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtimeline.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject, QTimeLineDirection, QTimeLineState

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEasingCurve, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEasingCurve = WAIT['QEasingCurve']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTimeLine(QObject):
  """
  The cute side of Qt's QTimeLine: a plain Python object standing in front of
  one C++ QTimeLine.

  It is built on the cute 'QObject', as Qt's QTimeLine is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTimeLine that has a ritual and that Python can call
  so far, 29 names in all: 'metaObject', 'tr', 'state', 'loopCount',
  'setLoopCount', 'direction', 'setDirection', 'duration', 'setDuration',
  'startFrame', 'setStartFrame', 'endFrame', 'setEndFrame', 'setFrameRange',
  'updateInterval', 'setUpdateInterval', 'easingCurve', 'setEasingCurve',
  'currentTime', 'currentFrame', 'currentValue', 'frameForTime',
  'valueForTime', 'start', 'resume', 'stop', 'setPaused', 'setCurrentTime',
  'toggleDirection'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTimeLine::~QTimeLine()': the destructor: Python never removes a
    C++ QTimeLine.

  What has no ritual
  ------------------

  19 of the 50 functions Qt declares: 8 takes or gives a type that cannot be
  passed yet; 4 a signal; 3 private; 2 forbidden; 1 a template; 1 protected.

  What to expect
  --------------

  - The C++ QTimeLine is created at the first use, not by 'QTimeLine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTimeLine.
  - Qt tells when it has removed the C++ QTimeLine. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QTimeLine, and the names Qt has for the
  #  combinations of its flags enums.
  Direction = QTimeLineDirection
  State = QTimeLineState

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
    Calls Qt's 'QString QTimeLine::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#tr

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
    #  QString QTimeLine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9QTimeLine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimeLine'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTimeLine::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTimeLine::metaObject() const
    address = self.uglySide.call('ritual_ZNK9QTimeLine10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def state(self) -> State:
    """
    Calls Qt's 'State QTimeLine::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QTimeLine::state() const
    return QTimeLine.State(self.uglySide.call(
        'ritual_ZNK9QTimeLine5stateEv',
    ))

  def loopCount(self) -> int:
    """
    Calls Qt's 'int QTimeLine::loopCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#loopCount
    """
    #  int QTimeLine::loopCount() const
    return self.uglySide.call('ritual_ZNK9QTimeLine9loopCountEv')

  def direction(self) -> Direction:
    """
    Calls Qt's 'Direction QTimeLine::direction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#direction

    Returns
    -------

    Direction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Direction(number)' gives.
    """
    #  Direction QTimeLine::direction() const
    return QTimeLine.Direction(self.uglySide.call(
        'ritual_ZNK9QTimeLine9directionEv',
    ))

  def duration(self) -> int:
    """
    Calls Qt's 'int QTimeLine::duration() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#duration
    """
    #  int QTimeLine::duration() const
    return self.uglySide.call('ritual_ZNK9QTimeLine8durationEv')

  def startFrame(self) -> int:
    """
    Calls Qt's 'int QTimeLine::startFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#startFrame
    """
    #  int QTimeLine::startFrame() const
    return self.uglySide.call('ritual_ZNK9QTimeLine10startFrameEv')

  def endFrame(self) -> int:
    """
    Calls Qt's 'int QTimeLine::endFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#endFrame
    """
    #  int QTimeLine::endFrame() const
    return self.uglySide.call('ritual_ZNK9QTimeLine8endFrameEv')

  def updateInterval(self) -> int:
    """
    Calls Qt's 'int QTimeLine::updateInterval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#updateInterval
    """
    #  int QTimeLine::updateInterval() const
    return self.uglySide.call('ritual_ZNK9QTimeLine14updateIntervalEv')

  def easingCurve(self) -> QEasingCurve:
    """
    Calls Qt's 'QEasingCurve QTimeLine::easingCurve() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#easingCurve

    Returns
    -------

    QEasingCurve
      A new cute QEasingCurve around the copy Qt gave back. Python owns it.
    """
    #  QEasingCurve QTimeLine::easingCurve() const
    address = self.uglySide.call('ritual_ZNK9QTimeLine11easingCurveEv')
    from . import QEasingCurve
    return QEasingCurve._cuteOwning(address)

  def currentTime(self) -> int:
    """
    Calls Qt's 'int QTimeLine::currentTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#currentTime
    """
    #  int QTimeLine::currentTime() const
    return self.uglySide.call('ritual_ZNK9QTimeLine11currentTimeEv')

  def currentFrame(self) -> int:
    """
    Calls Qt's 'int QTimeLine::currentFrame() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#currentFrame
    """
    #  int QTimeLine::currentFrame() const
    return self.uglySide.call('ritual_ZNK9QTimeLine12currentFrameEv')

  def currentValue(self) -> float:
    """
    Calls Qt's 'qreal QTimeLine::currentValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#currentValue
    """
    #  qreal QTimeLine::currentValue() const
    return self.uglySide.call('ritual_ZNK9QTimeLine12currentValueEv')

  @overload(int)
  def frameForTime(self, msec: int) -> int:
    """
    Calls Qt's 'int QTimeLine::frameForTime(int msec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#frameForTime

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  int QTimeLine::frameForTime(int msec) const
    return self.uglySide.call('ritual_ZNK9QTimeLine12frameForTimeEi', msec)

  @overload(int)
  def valueForTime(self, msec: int) -> float:
    """
    Calls Qt's 'qreal QTimeLine::valueForTime(int msec) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#valueForTime

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  qreal QTimeLine::valueForTime(int msec) const
    return self.uglySide.call('ritual_ZNK9QTimeLine12valueForTimeEi', msec)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setLoopCount(self, count: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setLoopCount(int count)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setLoopCount

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QTimeLine::setLoopCount(int count)
    self.uglySide.call('ritual_ZN9QTimeLine12setLoopCountEi', count)

  @overload(Direction)
  def setDirection(self, direction: Direction) -> None:
    """
    Calls Qt's 'void QTimeLine::setDirection(Direction direction)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setDirection

    Parameters
    ----------

    direction : Direction
      Passed on as its number.
    """
    #  void QTimeLine::setDirection(Direction direction)
    self.uglySide.call(
        'ritual_ZN9QTimeLine12setDirectionENS_9DirectionE', direction.value,
    )

  @overload(int)
  def setDuration(self, duration: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setDuration(int duration)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setDuration

    Parameters
    ----------

    duration : int
      Passed on as it is.
    """
    #  void QTimeLine::setDuration(int duration)
    self.uglySide.call('ritual_ZN9QTimeLine11setDurationEi', duration)

  @overload(int)
  def setStartFrame(self, frame: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setStartFrame(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setStartFrame

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QTimeLine::setStartFrame(int frame)
    self.uglySide.call('ritual_ZN9QTimeLine13setStartFrameEi', frame)

  @overload(int)
  def setEndFrame(self, frame: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setEndFrame(int frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setEndFrame

    Parameters
    ----------

    frame : int
      Passed on as it is.
    """
    #  void QTimeLine::setEndFrame(int frame)
    self.uglySide.call('ritual_ZN9QTimeLine11setEndFrameEi', frame)

  @overload(int, int)
  def setFrameRange(self, startFrame: int, endFrame: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setFrameRange(int startFrame, int endFrame)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setFrameRange

    Parameters
    ----------

    startFrame : int
      Passed on as it is.

    endFrame : int
      Passed on as it is.
    """
    #  void QTimeLine::setFrameRange(int startFrame, int endFrame)
    self.uglySide.call(
        'ritual_ZN9QTimeLine13setFrameRangeEii', startFrame, endFrame,
    )

  @overload(int)
  def setUpdateInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setUpdateInterval(int interval)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setUpdateInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QTimeLine::setUpdateInterval(int interval)
    self.uglySide.call('ritual_ZN9QTimeLine17setUpdateIntervalEi', interval)

  @overload(QEasingCurve)
  def setEasingCurve(self, curve: QEasingCurve) -> None:
    """
    Calls Qt's 'void QTimeLine::setEasingCurve(const QEasingCurve &curve)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setEasingCurve

    Parameters
    ----------

    curve : QEasingCurve
      Passed on as a value: Qt reads the C++ QEasingCurve, which stays
      Python's own.
    """
    #  void QTimeLine::setEasingCurve(const QEasingCurve &curve)
    self.uglySide.call(
        'ritual_ZN9QTimeLine14setEasingCurveERK12QEasingCurve',
        self._valueOf(curve),
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QTimeLine::setPaused(bool paused)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QTimeLine::setPaused(bool paused)
    self.uglySide.call('ritual_ZN9QTimeLine9setPausedEb', paused)

  @overload(int)
  def setCurrentTime(self, msec: int) -> None:
    """
    Calls Qt's 'void QTimeLine::setCurrentTime(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#setCurrentTime

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QTimeLine::setCurrentTime(int msec)
    self.uglySide.call('ritual_ZN9QTimeLine14setCurrentTimeEi', msec)

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
  @overload(int, QObject)
  @overload(int, NoneType)
  def __init__(
      self,
      duration: int = 1000,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTimeLine::QTimeLine(int duration,
    QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#QTimeLine

    Parameters
    ----------

    duration : int
      Passed on as it is. May be left out, as in Qt: it is then 1000.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTimeLine::QTimeLine(int duration, QObject *parent)
    self._noteCreation(QTimeLine, lambda: Rituals.call(
        'ritual_ZN9QTimeLineC1EiP7QObject',
        duration, self._addressOf(parent),
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

  def start(self) -> None:
    """
    Calls Qt's 'void QTimeLine::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#start
    """
    #  void QTimeLine::start()
    self.uglySide.call('ritual_ZN9QTimeLine5startEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QTimeLine::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#resume
    """
    #  void QTimeLine::resume()
    self.uglySide.call('ritual_ZN9QTimeLine6resumeEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QTimeLine::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#stop
    """
    #  void QTimeLine::stop()
    self.uglySide.call('ritual_ZN9QTimeLine4stopEv')

  def toggleDirection(self) -> None:
    """
    Calls Qt's 'void QTimeLine::toggleDirection()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimeline.html#toggleDirection
    """
    #  void QTimeLine::toggleDirection()
    self.uglySide.call('ritual_ZN9QTimeLine15toggleDirectionEv')
