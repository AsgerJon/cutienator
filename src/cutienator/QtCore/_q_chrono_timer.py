"""
QChronoTimer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qchronotimer.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QMetaObject, QTimerEvent, QTimerPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QChronoTimer(QObject):
  """
  The cute side of Qt's QChronoTimer: a plain Python object standing in front
  of one C++ QChronoTimer.

  It is built on the cute 'QObject', as Qt's QChronoTimer is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QChronoTimer that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'isActive', 'id',
  'setTimerType', 'timerType', 'setSingleShot', 'isSingleShot', 'start',
  'stop', 'timeout', 'timerEvent', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QChronoTimer::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QChronoTimer::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QChronoTimer::QChronoTimer(std::chrono::nanoseconds nsec, QObject
    *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QChronoTimer::~QChronoTimer()': the destructor: Python never
    removes a C++ QChronoTimer.
  - Qt's 'QBindable<bool> QChronoTimer::bindableActive()': gives a type
    Python has no way to take yet.
  - Qt's 'void QChronoTimer::setInterval(std::chrono::nanoseconds nsec)':
    takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::nanoseconds QChronoTimer::interval() const': gives a
    type Python has no way to take yet.
  - Qt's 'QBindable<std::chrono::nanoseconds>
    QChronoTimer::bindableInterval()': gives a type Python has no way to take
    yet.
  - Qt's 'std::chrono::nanoseconds QChronoTimer::remainingTime() const':
    gives a type Python has no way to take yet.
  - Qt's 'QBindable<Qt::TimerType> QChronoTimer::bindableTimerType()': gives
    a type Python has no way to take yet.
  - Qt's 'QBindable<bool> QChronoTimer::bindableSingleShot()': gives a type
    Python has no way to take yet.
  - Qt's 'const QTimerPrivate *QChronoTimer::d_func() const': takes in Python
    what 'QTimerPrivate *QChronoTimer::d_func()' takes.

  What has no ritual
  ------------------

  7 of the 33 functions Qt declares: 4 forbidden; 2 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QChronoTimer is created at the first use, not by
    'QChronoTimer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QChronoTimer.
  - Qt tells when it has removed the C++ QChronoTimer. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QChronoTimer that has no cute function yet,
    'bindableActive', 'bindableInterval', 'bindableSingleShot',
    'bindableTimerType', 'callOnTimeout', 'interval', 'remainingTime',
    'setInterval', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QChronoTimer::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#tr

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
    #  QString QChronoTimer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QChronoTimer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QChronoTimer'

  #  A C++ QChronoTimer Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QChronoTimer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QChronoTimer::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QChronoTimer::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QChronoTimer10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QChronoTimer::isActive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#isActive
    """
    #  bool QChronoTimer::isActive() const
    return self.uglySide.call('ritual_ZNK12QChronoTimer8isActiveEv')

  def id(self) -> Qt.TimerId:
    """
    Calls Qt's 'Qt::TimerId QChronoTimer::id() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#id

    Returns
    -------

    Qt.TimerId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerId(number)'
      gives.
    """
    #  Qt::TimerId QChronoTimer::id() const
    return Qt.TimerId(self.uglySide.call('ritual_ZNK12QChronoTimer2idEv'))

  def timerType(self) -> Qt.TimerType:
    """
    Calls Qt's 'Qt::TimerType QChronoTimer::timerType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#timerType

    Returns
    -------

    Qt.TimerType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.TimerType(number)'
      gives.
    """
    #  Qt::TimerType QChronoTimer::timerType() const
    return Qt.TimerType(self.uglySide.call(
        'ritual_ZNK12QChronoTimer9timerTypeEv',
    ))

  def isSingleShot(self) -> bool:
    """
    Calls Qt's 'bool QChronoTimer::isSingleShot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#isSingleShot
    """
    #  bool QChronoTimer::isSingleShot() const
    return self.uglySide.call('ritual_ZNK12QChronoTimer12isSingleShotEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.TimerType)
  def setTimerType(self, atype: Qt.TimerType) -> None:
    """
    Calls Qt's 'void QChronoTimer::setTimerType(Qt::TimerType atype)'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#setTimerType

    Parameters
    ----------

    atype : Qt.TimerType
      Passed on as its number.
    """
    #  void QChronoTimer::setTimerType(Qt::TimerType atype)
    self.uglySide.call(
        'ritual_ZN12QChronoTimer12setTimerTypeEN2Qt9TimerTypeE', atype.value,
    )

  @overload(bool)
  def setSingleShot(self, singleShot: bool) -> None:
    """
    Calls Qt's 'void QChronoTimer::setSingleShot(bool singleShot)'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#setSingleShot

    Parameters
    ----------

    singleShot : bool
      Passed on as it is.
    """
    #  void QChronoTimer::setSingleShot(bool singleShot)
    self.uglySide.call(
        'ritual_ZN12QChronoTimer13setSingleShotEb', singleShot,
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
    Notes what was given, for Qt's 'QChronoTimer::QChronoTimer(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#QChronoTimer

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QChronoTimer::QChronoTimer(QObject *parent)
    self._noteCreation(QChronoTimer, lambda: Rituals.call(
        'ritual_ZN12QChronoTimerC1EP7QObject',
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

  def start(self) -> None:
    """
    Calls Qt's 'void QChronoTimer::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#start
    """
    #  void QChronoTimer::start()
    self.uglySide.call('ritual_ZN12QChronoTimer5startEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QChronoTimer::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#stop
    """
    #  void QChronoTimer::stop()
    self.uglySide.call('ritual_ZN12QChronoTimer4stopEv')

  def timeout(self) -> None:
    """
    Calls Qt's 'void QChronoTimer::timeout(QPrivateSignal a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#timeout
    """
    #  void QChronoTimer::timeout(QPrivateSignal a0)
    self.uglySide.call(
        'ritual_ZN12QChronoTimer7timeoutENS_14QPrivateSignalE',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QChronoTimer::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QChronoTimer::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN12QChronoTimer10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QChronoTimer10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  def d_func(self) -> Optional[QTimerPrivate]:
    """
    Calls Qt's 'QTimerPrivate *QChronoTimer::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qchronotimer.html#d_func

    Returns
    -------

    Optional[QTimerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTimerPrivate *QChronoTimer::d_func()
    address = self.uglySide.call('ritual_ZN12QChronoTimer6d_funcEv')
    from . import QTimerPrivate
    return QTimerPrivate._cuteAt(address)

  @staticmethod
  def bindableActive(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QChronoTimer::bindableActive()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.bindableActive' has no cute function yet. Qt's "
        "'QBindable<bool> QChronoTimer::bindableActive()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableInterval(*__, **_) -> Never:
    """
    Qt's 'QBindable<std::chrono::nanoseconds>
    QChronoTimer::bindableInterval()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.bindableInterval' has no cute function yet. Qt's "
        "'QBindable<std::chrono::nanoseconds> "
        "QChronoTimer::bindableInterval()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def bindableSingleShot(*__, **_) -> Never:
    """
    Qt's 'QBindable<bool> QChronoTimer::bindableSingleShot()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.bindableSingleShot' has no cute function yet. Qt's "
        "'QBindable<bool> QChronoTimer::bindableSingleShot()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def bindableTimerType(*__, **_) -> Never:
    """
    Qt's 'QBindable<Qt::TimerType> QChronoTimer::bindableTimerType()': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.bindableTimerType' has no cute function yet. Qt's "
        "'QBindable<Qt::TimerType> QChronoTimer::bindableTimerType()': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def callOnTimeout(*__, **_) -> Never:
    """
    Qt's 'QChronoTimer::callOnTimeout': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QChronoTimer.callOnTimeout' has no cute function yet. Qt's "
        "'QChronoTimer::callOnTimeout': a template: a pattern and no single "
        "function.")

  @staticmethod
  def interval(*__, **_) -> Never:
    """
    Qt's 'std::chrono::nanoseconds QChronoTimer::interval() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.interval' has no cute function yet. Qt's "
        "'std::chrono::nanoseconds QChronoTimer::interval() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def remainingTime(*__, **_) -> Never:
    """
    Qt's 'std::chrono::nanoseconds QChronoTimer::remainingTime() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.remainingTime' has no cute function yet. Qt's "
        "'std::chrono::nanoseconds QChronoTimer::remainingTime() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def setInterval(*__, **_) -> Never:
    """
    Qt's 'void QChronoTimer::setInterval(std::chrono::nanoseconds nsec)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QChronoTimer.setInterval' has no cute function yet. Qt's 'void "
        "QChronoTimer::setInterval(std::chrono::nanoseconds nsec)': takes a "
        "type Python has no way to hand over yet.")
