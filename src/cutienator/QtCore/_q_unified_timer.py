"""
QUnifiedTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QUnifiedTimer to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractAnimationTimer, QAnimationDriver, QMetaObject
  from . import QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractAnimationTimer = WAIT['QAbstractAnimationTimer']
  QAnimationDriver = WAIT['QAnimationDriver']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QUnifiedTimer(QObject):
  """
  The cute side of Qt's QUnifiedTimer: a plain Python object standing in
  front of one C++ QUnifiedTimer.

  It is built on the cute 'QObject', as Qt's QUnifiedTimer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QUnifiedTimer that has a ritual and that Python can
  call so far, 26 names in all: 'metaObject', 'tr', 'instance',
  'startAnimationTimer', 'stopAnimationTimer', 'pauseAnimationTimer',
  'resumeAnimationTimer', 'setTimingInterval', 'setConsistentTiming',
  'getSpeedModifier', 'setSpeedModifier', 'installAnimationDriver',
  'uninstallAnimationDriver', 'canUninstallAnimationDriver', 'restart',
  'maybeUpdateAnimationsToCurrentTime', 'updateAnimationTimers',
  'runningAnimationCount', 'startAnimationDriver', 'stopAnimationDriver',
  'elapsed', 'timerEvent', 'startTimers', 'stopTimer', 'localRestart',
  'closestPausedAnimationTimerTimeToFinish'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QUnifiedTimer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QUnifiedTimer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QUnifiedTimer::~QUnifiedTimer()': the destructor: Python never
    removes a C++ QUnifiedTimer.
  - Qt's 'void QUnifiedTimer::registerProfilerCallback(void (*)(qint64) cb)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 34 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QUnifiedTimer is created at the first use, not by
    'QUnifiedTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QUnifiedTimer.
  - Qt tells when it has removed the C++ QUnifiedTimer. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QUnifiedTimer that has no cute function yet,
    'registerProfilerCallback', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QUnifiedTimer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#tr

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
    #  QString QUnifiedTimer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QUnifiedTimer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload()
  def instance() -> Optional[QUnifiedTimer]:
    """
    Calls Qt's 'QUnifiedTimer *QUnifiedTimer::instance()'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#instance

    Returns
    -------

    Optional[QUnifiedTimer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUnifiedTimer *QUnifiedTimer::instance()
    address = Rituals.call('ritual_ZN13QUnifiedTimer8instanceEv')
    return QUnifiedTimer._cuteAt(address)

  @staticmethod
  @overload(bool)
  def instance(create: bool) -> Optional[QUnifiedTimer]:
    """
    Calls Qt's 'QUnifiedTimer *QUnifiedTimer::instance(bool create)'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#instance

    Parameters
    ----------

    create : bool
      Passed on as it is.

    Returns
    -------

    Optional[QUnifiedTimer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QUnifiedTimer *QUnifiedTimer::instance(bool create)
    address = Rituals.call('ritual_ZN13QUnifiedTimer8instanceEb', create)
    return QUnifiedTimer._cuteAt(address)

  @staticmethod
  @overload(QAbstractAnimationTimer)
  @overload(NoneType)
  def startAnimationTimer(timer: Optional[QAbstractAnimationTimer]) -> None:
    """
    Calls Qt's 'void
    QUnifiedTimer::startAnimationTimer(QAbstractAnimationTimer *timer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#startAnimationTimer

    Parameters
    ----------

    timer : Optional[QAbstractAnimationTimer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUnifiedTimer::startAnimationTimer(QAbstractAnimationTimer
    #      *timer)
    Rituals.call(
        'ritual_ZN13QUnifiedTimer19startAnimationTimerEP23QAbstractAnimatio'
        'nTimer',
        CuteMixin._addressOf(timer),
    )

  @staticmethod
  @overload(QAbstractAnimationTimer)
  @overload(NoneType)
  def stopAnimationTimer(timer: Optional[QAbstractAnimationTimer]) -> None:
    """
    Calls Qt's 'void
    QUnifiedTimer::stopAnimationTimer(QAbstractAnimationTimer *timer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#stopAnimationTimer

    Parameters
    ----------

    timer : Optional[QAbstractAnimationTimer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUnifiedTimer::stopAnimationTimer(QAbstractAnimationTimer *timer)
    Rituals.call(
        'ritual_ZN13QUnifiedTimer18stopAnimationTimerEP23QAbstractAnimation'
        'Timer',
        CuteMixin._addressOf(timer),
    )

  @staticmethod
  @overload(QAbstractAnimationTimer, int)
  @overload(NoneType, int)
  def pauseAnimationTimer(
      timer: Optional[QAbstractAnimationTimer],
      duration: int,
  ) -> None:
    """
    Calls Qt's 'void
    QUnifiedTimer::pauseAnimationTimer(QAbstractAnimationTimer *timer, int
    duration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#pauseAnimationTimer

    Parameters
    ----------

    timer : Optional[QAbstractAnimationTimer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    duration : int
      Passed on as it is.
    """
    #  void QUnifiedTimer::pauseAnimationTimer(QAbstractAnimationTimer
    #      *timer, int duration)
    Rituals.call(
        'ritual_ZN13QUnifiedTimer19pauseAnimationTimerEP23QAbstractAnimatio'
        'nTimeri',
        CuteMixin._addressOf(timer), duration,
    )

  @staticmethod
  @overload(QAbstractAnimationTimer)
  @overload(NoneType)
  def resumeAnimationTimer(timer: Optional[QAbstractAnimationTimer]) -> None:
    """
    Calls Qt's 'void
    QUnifiedTimer::resumeAnimationTimer(QAbstractAnimationTimer *timer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#resumeAnimationTimer

    Parameters
    ----------

    timer : Optional[QAbstractAnimationTimer]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUnifiedTimer::resumeAnimationTimer(QAbstractAnimationTimer
    #      *timer)
    Rituals.call(
        'ritual_ZN13QUnifiedTimer20resumeAnimationTimerEP23QAbstractAnimati'
        'onTimer',
        CuteMixin._addressOf(timer),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUnifiedTimer'

  #  A C++ QUnifiedTimer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QUnifiedTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QUnifiedTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QUnifiedTimer::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QUnifiedTimer10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def getSpeedModifier(self) -> float:
    """
    Calls Qt's 'qreal QUnifiedTimer::getSpeedModifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#getSpeedModifier
    """
    #  qreal QUnifiedTimer::getSpeedModifier() const
    return self.uglySide.call(
        'ritual_ZNK13QUnifiedTimer16getSpeedModifierEv',
    )

  def runningAnimationCount(self) -> int:
    """
    Calls Qt's 'qsizetype QUnifiedTimer::runningAnimationCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#runningAnimationCount
    """
    #  qsizetype QUnifiedTimer::runningAnimationCount() const
    return self.uglySide.call(
        'ritual_ZNK13QUnifiedTimer21runningAnimationCountEv',
    )

  def elapsed(self) -> int:
    """
    Calls Qt's 'qint64 QUnifiedTimer::elapsed() const'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#elapsed
    """
    #  qint64 QUnifiedTimer::elapsed() const
    return self.uglySide.call('ritual_ZNK13QUnifiedTimer7elapsedEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTimingInterval(self, interval: int) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::setTimingInterval(int interval)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#setTimingInterval

    Parameters
    ----------

    interval : int
      Passed on as it is.
    """
    #  void QUnifiedTimer::setTimingInterval(int interval)
    self.uglySide.call(
        'ritual_ZN13QUnifiedTimer17setTimingIntervalEi', interval,
    )

  @overload(bool)
  def setConsistentTiming(self, consistent: bool) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::setConsistentTiming(bool consistent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#setConsistentTiming

    Parameters
    ----------

    consistent : bool
      Passed on as it is.
    """
    #  void QUnifiedTimer::setConsistentTiming(bool consistent)
    self.uglySide.call(
        'ritual_ZN13QUnifiedTimer19setConsistentTimingEb', consistent,
    )

  @overload(float)
  def setSpeedModifier(self, speed: float) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::setSpeedModifier(qreal speed)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#setSpeedModifier

    Parameters
    ----------

    speed : float
      Passed on as it is.
    """
    #  void QUnifiedTimer::setSpeedModifier(qreal speed)
    self.uglySide.call('ritual_ZN13QUnifiedTimer16setSpeedModifierEd', speed)

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
    Notes what was given, for Qt's 'QUnifiedTimer::QUnifiedTimer()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#QUnifiedTimer
    """
    #  QUnifiedTimer::QUnifiedTimer()
    self._noteCreation(QUnifiedTimer, lambda: Rituals.call(
        'ritual_ZN13QUnifiedTimerC1Ev',
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

  @overload(QAnimationDriver)
  @overload(NoneType)
  def installAnimationDriver(
      self,
      driver: Optional[QAnimationDriver],
  ) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::installAnimationDriver(QAnimationDriver
    *driver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#installAnimationDriver

    Parameters
    ----------

    driver : Optional[QAnimationDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUnifiedTimer::installAnimationDriver(QAnimationDriver *driver)
    self.uglySide.call(
        'ritual_ZN13QUnifiedTimer22installAnimationDriverEP16QAnimationDriv'
        'er',
        self._addressOf(driver),
    )

  @overload(QAnimationDriver)
  @overload(NoneType)
  def uninstallAnimationDriver(
      self,
      driver: Optional[QAnimationDriver],
  ) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::uninstallAnimationDriver(QAnimationDriver
    *driver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#uninstallAnimationDriver

    Parameters
    ----------

    driver : Optional[QAnimationDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUnifiedTimer::uninstallAnimationDriver(QAnimationDriver *driver)
    self.uglySide.call(
        'ritual_ZN13QUnifiedTimer24uninstallAnimationDriverEP16QAnimationDr'
        'iver',
        self._addressOf(driver),
    )

  @overload(QAnimationDriver)
  @overload(NoneType)
  def canUninstallAnimationDriver(
      self,
      driver: Optional[QAnimationDriver],
  ) -> bool:
    """
    Calls Qt's 'bool
    QUnifiedTimer::canUninstallAnimationDriver(QAnimationDriver *driver)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#canUninstallAnimationDriver

    Parameters
    ----------

    driver : Optional[QAnimationDriver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QUnifiedTimer::canUninstallAnimationDriver(QAnimationDriver
    #      *driver)
    return self.uglySide.call(
        'ritual_ZN13QUnifiedTimer27canUninstallAnimationDriverEP16QAnimatio'
        'nDriver',
        self._addressOf(driver),
    )

  def restart(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::restart()'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#restart
    """
    #  void QUnifiedTimer::restart()
    self.uglySide.call('ritual_ZN13QUnifiedTimer7restartEv')

  def maybeUpdateAnimationsToCurrentTime(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::maybeUpdateAnimationsToCurrentTime()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html
    """
    #  void QUnifiedTimer::maybeUpdateAnimationsToCurrentTime()
    self.uglySide.call(
        'ritual_ZN13QUnifiedTimer34maybeUpdateAnimationsToCurrentTimeEv',
    )

  def updateAnimationTimers(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::updateAnimationTimers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#updateAnimationTimers
    """
    #  void QUnifiedTimer::updateAnimationTimers()
    self.uglySide.call('ritual_ZN13QUnifiedTimer21updateAnimationTimersEv')

  def startAnimationDriver(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::startAnimationDriver()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#startAnimationDriver
    """
    #  void QUnifiedTimer::startAnimationDriver()
    self.uglySide.call('ritual_ZN13QUnifiedTimer20startAnimationDriverEv')

  def stopAnimationDriver(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::stopAnimationDriver()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html#stopAnimationDriver
    """
    #  void QUnifiedTimer::stopAnimationDriver()
    self.uglySide.call('ritual_ZN13QUnifiedTimer19stopAnimationDriverEv')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QUnifiedTimer::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN13QUnifiedTimer10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QUnifiedTimer10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  def startTimers(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::startTimers()'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#startTimers
    """
    #  void QUnifiedTimer::startTimers()
    self.uglySide.call('ritual_ZN13QUnifiedTimer11startTimersEv')

  def stopTimer(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::stopTimer()'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#stopTimer
    """
    #  void QUnifiedTimer::stopTimer()
    self.uglySide.call('ritual_ZN13QUnifiedTimer9stopTimerEv')

  def localRestart(self) -> None:
    """
    Calls Qt's 'void QUnifiedTimer::localRestart()'.

    Qt's own words: https://doc.qt.io/qt-6/qunifiedtimer.html#localRestart
    """
    #  void QUnifiedTimer::localRestart()
    self.uglySide.call('ritual_ZN13QUnifiedTimer12localRestartEv')

  def closestPausedAnimationTimerTimeToFinish(self) -> int:
    """
    Calls Qt's 'int
    QUnifiedTimer::closestPausedAnimationTimerTimeToFinish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qunifiedtimer.html
    """
    #  int QUnifiedTimer::closestPausedAnimationTimerTimeToFinish()
    return self.uglySide.call(
        'ritual_ZN13QUnifiedTimer39closestPausedAnimationTimerTimeToFinishE'
        'v',
    )

  @staticmethod
  def registerProfilerCallback(*__, **_) -> Never:
    """
    Qt's 'void QUnifiedTimer::registerProfilerCallback(void (*)(qint64) cb)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QUnifiedTimer.registerProfilerCallback' has no cute function yet. "
        "Qt's 'void QUnifiedTimer::registerProfilerCallback(void "
        "(*)(qint64) cb)': takes a type Python has no way to hand over yet.")
