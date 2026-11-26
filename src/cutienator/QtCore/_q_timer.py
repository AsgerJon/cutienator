"""
QTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qtimer.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject, QTimerEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTimer(QObject):
  """
  The cute side of Qt's QTimer: a plain Python object standing in front of
  one C++ QTimer.

  It is built on the cute 'QObject', as Qt's QTimer is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTimer that has a ritual and that Python can call so
  far, 20 names in all: 'metaObject', 'tr', 'isActive', 'timerId', 'id',
  'setInterval', 'interval', 'remainingTime', 'setTimerType', 'timerType',
  'setSingleShot', 'isSingleShot', 'singleShot', 'start', 'stop', 'timeout',
  'timerEvent', 'startTimer', 'killTimer', 'defaultTypeFor'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTimer::qt_metacast(const char *a0)': one of Qt's own inner
    workings.
  - Qt's 'int QTimer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)':
    one of Qt's own inner workings.
  - Qt's 'QTimer::~QTimer()': the destructor: Python never removes a C++
    QTimer.
  - Qt's 'QBindable<bool> QTimer::bindableActive()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<int> QTimer::bindableInterval()': gives a type Python has
    no way to take yet.
  - Qt's 'QBindable<Qt::TimerType> QTimer::bindableTimerType()': gives a type
    Python has no way to take yet.
  - Qt's 'QBindable<bool> QTimer::bindableSingleShot()': gives a type Python
    has no way to take yet.
  - Qt's 'void QTimer::setInterval(std::chrono::milliseconds value)': takes a
    type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds QTimer::intervalAsDuration() const':
    gives a type Python has no way to take yet.
  - Qt's 'std::chrono::milliseconds QTimer::remainingTimeAsDuration() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QTimer::singleShot(std::chrono::nanoseconds value, const
    QObject *receiver, const char *member)': takes a type Python has no way
    to hand over yet.
  - Qt's 'void QTimer::singleShot(std::chrono::nanoseconds interval,
    Qt::TimerType timerType, const QObject *receiver, const char *member)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QTimer::start(std::chrono::milliseconds value)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QTimerPrivate *QTimer::d_func()': gives 'QTimerPrivate', which has
    no cute class yet.
  - Qt's 'const QTimerPrivate *QTimer::d_func() const': gives
    'QTimerPrivate', which has no cute class yet.
  - Qt's 'std::chrono::nanoseconds
    QTimer::from_msecs(std::chrono::milliseconds a0)': takes a type Python
    has no way to hand over yet.
  - Qt's 'std::chrono::nanoseconds QTimer::toDuration(int msecs)': gives a
    type Python has no way to take yet.
  - Qt's 'std::chrono::nanoseconds
    QTimer::toDuration(std::chrono::nanoseconds ns)': takes a type Python has
    no way to hand over yet.
  - Qt's 'Qt::TimerType QTimer::defaultTypeFor(std::chrono::nanoseconds
    interval)': takes a type Python has no way to hand over yet.
  - Qt's 'void QTimer::singleShotImpl(std::chrono::nanoseconds interval,
    Qt::TimerType timerType, const QObject *receiver,
    QtPrivate::QSlotObjectBase *slotObj)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  9 of the 52 functions Qt declares: 5 a template; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QTimer is created at the first use, not by 'QTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTimer.
  - Qt tells when it has removed the C++ QTimer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QTimer that has no cute function yet, 'bindableActive',
    'bindableInterval', 'bindableSingleShot', 'bindableTimerType',
    'callOnTimeout', 'from_msecs', 'intervalAsDuration',
    'remainingTimeAsDuration', 'singleShotImpl', 'toDuration', holds a
    function that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QTimer::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#tr

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
    #  QString QTimer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN6QTimer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int, QObject, str)
  @overload(int, QObject, NoneType)
  @overload(int, NoneType, str)
  @overload(int, NoneType, NoneType)
  def singleShot(
      msec: int,
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QTimer::singleShot(int msec, const QObject *receiver,
    const char *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#singleShot

    Parameters
    ----------

    msec : int
      Passed on as it is.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QTimer::singleShot(int msec, const QObject *receiver, const char
    #      *member)
    Rituals.call(
        'ritual_ZN6QTimer10singleShotEiPK7QObjectPKc',
        msec, CuteMixin._addressOf(receiver, 'QObject'),
        CuteMixin._bytesOf(member),
    )

  @staticmethod
  @overload(int, Qt.TimerType, QObject, str)
  @overload(int, Qt.TimerType, QObject, NoneType)
  @overload(int, Qt.TimerType, NoneType, str)
  @overload(int, Qt.TimerType, NoneType, NoneType)
  def singleShot(
      msec: int,
      timerType: Qt.TimerType,
      receiver: Optional[QObject],
      member: Optional[str],
  ) -> None:
    """
    Calls Qt's 'void QTimer::singleShot(int msec, Qt::TimerType timerType,
    const QObject *receiver, const char *member)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#singleShot

    Parameters
    ----------

    msec : int
      Passed on as it is.

    timerType : Qt.TimerType
      Passed on as its number.

    receiver : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    member : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  void QTimer::singleShot(int msec, Qt::TimerType timerType, const
    #      QObject *receiver, const char *member)
    Rituals.call(
        'ritual_ZN6QTimer10singleShotEiN2Qt9TimerTypeEPK7QObjectPKc',
        msec, timerType.value, CuteMixin._addressOf(receiver, 'QObject'),
        CuteMixin._bytesOf(member),
    )

  @staticmethod
  @overload(int)
  def defaultTypeFor(msecs: int) -> Qt.TimerType:
    """
    Calls Qt's 'Qt::TimerType QTimer::defaultTypeFor(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#defaultTypeFor

    Parameters
    ----------

    msecs : int
      Passed on as it is.

    Returns
    -------

    Qt.TimerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerType(number)'
      gives.
    """
    #  Qt::TimerType QTimer::defaultTypeFor(int msecs)
    return Qt.TimerType(Rituals.call(
        'ritual_ZN6QTimer14defaultTypeForEi', msecs,
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTimer'

  #  A C++ QTimer Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTimer::metaObject() const
    address = self.uglySide.call('ritual_ZNK6QTimer10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QTimer::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#isActive
    """
    #  bool QTimer::isActive() const
    return self.uglySide.call('ritual_ZNK6QTimer8isActiveEv')

  def timerId(self) -> int:
    """
    Calls Qt's 'int QTimer::timerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#timerId
    """
    #  int QTimer::timerId() const
    return self.uglySide.call('ritual_ZNK6QTimer7timerIdEv')

  def id(self) -> Qt.TimerId:
    """
    Calls Qt's 'Qt::TimerId QTimer::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#id

    Returns
    -------

    Qt.TimerId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerId(number)'
      gives.
    """
    #  Qt::TimerId QTimer::id() const
    return Qt.TimerId(self.uglySide.call('ritual_ZNK6QTimer2idEv'))

  def interval(self) -> int:
    """
    Calls Qt's 'int QTimer::interval() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#interval
    """
    #  int QTimer::interval() const
    return self.uglySide.call('ritual_ZNK6QTimer8intervalEv')

  def remainingTime(self) -> int:
    """
    Calls Qt's 'int QTimer::remainingTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#remainingTime
    """
    #  int QTimer::remainingTime() const
    return self.uglySide.call('ritual_ZNK6QTimer13remainingTimeEv')

  def timerType(self) -> Qt.TimerType:
    """
    Calls Qt's 'Qt::TimerType QTimer::timerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#timerType

    Returns
    -------

    Qt.TimerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerType(number)'
      gives.
    """
    #  Qt::TimerType QTimer::timerType() const
    return Qt.TimerType(self.uglySide.call('ritual_ZNK6QTimer9timerTypeEv'))

  def isSingleShot(self) -> bool:
    """
    Calls Qt's 'bool QTimer::isSingleShot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#isSingleShot
    """
    #  bool QTimer::isSingleShot() const
    return self.uglySide.call('ritual_ZNK6QTimer12isSingleShotEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setInterval(self, msec: int) -> None:
    """
    Calls Qt's 'void QTimer::setInterval(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#setInterval

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QTimer::setInterval(int msec)
    self.uglySide.call('ritual_ZN6QTimer11setIntervalEi', msec)

  @overload(Qt.TimerType)
  def setTimerType(self, atype: Qt.TimerType) -> None:
    """
    Calls Qt's 'void QTimer::setTimerType(Qt::TimerType atype)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#setTimerType

    Parameters
    ----------

    atype : Qt.TimerType
      Passed on as its number.
    """
    #  void QTimer::setTimerType(Qt::TimerType atype)
    self.uglySide.call(
        'ritual_ZN6QTimer12setTimerTypeEN2Qt9TimerTypeE', atype.value,
    )

  @overload(bool)
  def setSingleShot(self, singleShot: bool) -> None:
    """
    Calls Qt's 'void QTimer::setSingleShot(bool singleShot)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#setSingleShot

    Parameters
    ----------

    singleShot : bool
      Passed on as it is.
    """
    #  void QTimer::setSingleShot(bool singleShot)
    self.uglySide.call('ritual_ZN6QTimer13setSingleShotEb', singleShot)

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
    Notes what was given, for Qt's 'QTimer::QTimer(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#QTimer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTimer::QTimer(QObject *parent)
    self._noteCreation(QTimer, lambda: Rituals.call(
        'ritual_ZN6QTimerC1EP7QObject', self._addressOf(parent, 'QObject'),
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
  def start(self, msec: int) -> None:
    """
    Calls Qt's 'void QTimer::start(int msec)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#start

    Parameters
    ----------

    msec : int
      Passed on as it is.
    """
    #  void QTimer::start(int msec)
    self.uglySide.call('ritual_ZN6QTimer5startEi', msec)

  @overload()
  def start(self) -> None:
    """
    Calls Qt's 'void QTimer::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#start
    """
    #  void QTimer::start()
    self.uglySide.call('ritual_ZN6QTimer5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QTimer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#stop
    """
    #  void QTimer::stop()
    self.uglySide.call('ritual_ZN6QTimer4stopEv')

  def timeout(self) -> None:
    """
    Calls Qt's 'void QTimer::timeout(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#timeout
    """
    #  void QTimer::timeout(QPrivateSignal a0)
    self.uglySide.call('ritual_ZN6QTimer7timeoutENS_14QPrivateSignalE')

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QTimer::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTimer::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN6QTimer10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN6QTimer10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(int)
  def startTimer(self, a0: int) -> int:
    """
    Calls Qt's 'int QTimer::startTimer(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#startTimer

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QTimer::startTimer(int a0)
    return self.uglySide.call('ritual_ZN6QTimer10startTimerEi', a0)

  @overload(int)
  def killTimer(self, a0: int) -> None:
    """
    Calls Qt's 'void QTimer::killTimer(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtimer.html#killTimer

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QTimer::killTimer(int a0)
    self.uglySide.call('ritual_ZN6QTimer9killTimerEi', a0)

  @staticmethod
  def bindableActive(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QTimer::bindableActive()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QTimer.bindableActive' has no cute function yet. Qt's "
        "'QBindable<bool> QTimer::bindableActive()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableInterval(*__, **_) -> Never:
    """
    Qt's 'QBindable<int> QTimer::bindableInterval()': gives a type Python has
    no way to take yet.
    """
    raise NotImplementedError(
        "'QTimer.bindableInterval' has no cute function yet. Qt's "
        "'QBindable<int> QTimer::bindableInterval()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def bindableSingleShot(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QTimer::bindableSingleShot()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimer.bindableSingleShot' has no cute function yet. Qt's "
        "'QBindable<bool> QTimer::bindableSingleShot()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableTimerType(*__, **_) -> Never:
    """
    Qt's 'QBindable<Qt::TimerType> QTimer::bindableTimerType()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimer.bindableTimerType' has no cute function yet. Qt's "
        "'QBindable<Qt::TimerType> QTimer::bindableTimerType()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def callOnTimeout(*__, **_) -> Never:
    """
    Qt's 'QTimer::callOnTimeout': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QTimer.callOnTimeout' has no cute function yet. Qt's "
        "'QTimer::callOnTimeout': a template: a pattern and no single "
        "function.")

  @staticmethod
  def from_msecs(*__, **_) -> Never:
    """
    Qt's 'std::chrono::nanoseconds
    QTimer::from_msecs(std::chrono::milliseconds a0)': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTimer.from_msecs' has no cute function yet. Qt's "
        "'std::chrono::nanoseconds "
        "QTimer::from_msecs(std::chrono::milliseconds a0)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def intervalAsDuration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QTimer::intervalAsDuration() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimer.intervalAsDuration' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QTimer::intervalAsDuration() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def remainingTimeAsDuration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QTimer::remainingTimeAsDuration() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QTimer.remainingTimeAsDuration' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QTimer::remainingTimeAsDuration() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def singleShotImpl(*__, **_) -> Never:
    """
    Qt's 'void QTimer::singleShotImpl(std::chrono::nanoseconds interval,
    Qt::TimerType timerType, const QObject *receiver,
    QtPrivate::QSlotObjectBase *slotObj)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QTimer.singleShotImpl' has no cute function yet. Qt's 'void "
        "QTimer::singleShotImpl(std::chrono::nanoseconds interval, "
        "Qt::TimerType timerType, const QObject *receiver, "
        "QtPrivate::QSlotObjectBase *slotObj)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def toDuration(*__, **_) -> Never:
    """
    - Qt's 'std::chrono::nanoseconds QTimer::toDuration(int msecs)': gives a
      type Python has no way to take yet.
    - Qt's 'std::chrono::nanoseconds
      QTimer::toDuration(std::chrono::nanoseconds ns)': takes a type Python
      has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTimer.toDuration' has no cute function yet. Qt's "
        "'std::chrono::nanoseconds QTimer::toDuration(int msecs)': gives a "
        "type Python has no way to take yet. Qt's 'std::chrono::nanoseconds "
        "QTimer::toDuration(std::chrono::nanoseconds ns)': takes a type "
        "Python has no way to hand over yet.")
