"""
QThread binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qthread.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QAbstractEventDispatcher, QDeadlineTimer, QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAbstractEventDispatcher = WAIT['QAbstractEventDispatcher']
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThread(QObject):
  """
  The cute side of Qt's QThread: a plain Python object standing in front of
  one C++ QThread.

  It is built on the cute 'QObject', as Qt's QThread is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QThread that has a ritual and that Python can call
  so far, 30 names in all: 'metaObject', 'tr', 'currentThread',
  'isMainThread', 'idealThreadCount', 'yieldCurrentThread', 'setPriority',
  'priority', 'isFinished', 'isRunning', 'requestInterruption',
  'isInterruptionRequested', 'setStackSize', 'stackSize', 'eventDispatcher',
  'setEventDispatcher', 'event', 'loopLevel', 'isCurrentThread',
  'setServiceLevel', 'serviceLevel', 'start', 'terminate', 'exit', 'quit',
  'wait', 'sleep', 'msleep', 'usleep', 'run'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QThread::~QThread()': the destructor: Python never removes a C++
    QThread.

  What has no ritual
  ------------------

  16 of the 49 functions Qt declares: 5 private; 4 takes or gives a type that
  cannot be passed yet; 3 protected; 2 a template; 2 a signal.

  What to expect
  --------------

  - The C++ QThread is created at the first use, not by 'QThread(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QThread.
  - Qt tells when it has removed the C++ QThread. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QThread, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class Priority(CuteNum):
    """
    The enum 'QThread::Priority' of Qt, with the 8 names Qt gives in it.
    """

    IdlePriority = Kee[int](0)
    LowestPriority = Kee[int](1)
    LowPriority = Kee[int](2)
    NormalPriority = Kee[int](3)
    HighPriority = Kee[int](4)
    HighestPriority = Kee[int](5)
    TimeCriticalPriority = Kee[int](6)
    InheritPriority = Kee[int](7)

  class QualityOfService(CuteNum, scoped=True):
    """
    The enum 'QThread::QualityOfService' of Qt, with the 3 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Auto = Kee[int](0)
    High = Kee[int](1)
    Eco = Kee[int](2)

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
    Calls Qt's 'QString QThread::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#tr

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
    #  QString QThread::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN7QThread2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def currentThread() -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QThread::currentThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#currentThread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QThread::currentThread()
    address = Rituals.call('ritual_ZN7QThread13currentThreadEv')
    return QThread._cuteAt(address)

  @staticmethod
  def isMainThread() -> bool:
    """
    Calls Qt's 'bool QThread::isMainThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#isMainThread
    """
    #  bool QThread::isMainThread()
    return Rituals.call('ritual_ZN7QThread12isMainThreadEv')

  @staticmethod
  def idealThreadCount() -> int:
    """
    Calls Qt's 'int QThread::idealThreadCount()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#idealThreadCount
    """
    #  int QThread::idealThreadCount()
    return Rituals.call('ritual_ZN7QThread16idealThreadCountEv')

  @staticmethod
  def yieldCurrentThread() -> None:
    """
    Calls Qt's 'void QThread::yieldCurrentThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#yieldCurrentThread
    """
    #  void QThread::yieldCurrentThread()
    Rituals.call('ritual_ZN7QThread18yieldCurrentThreadEv')

  @staticmethod
  @overload(int)
  def sleep(a0: int) -> None:
    """
    Calls Qt's 'void QThread::sleep(unsigned long a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#sleep

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QThread::sleep(unsigned long a0)
    Rituals.call('ritual_ZN7QThread5sleepEm', a0)

  @staticmethod
  @overload(int)
  def msleep(a0: int) -> None:
    """
    Calls Qt's 'void QThread::msleep(unsigned long a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#msleep

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QThread::msleep(unsigned long a0)
    Rituals.call('ritual_ZN7QThread6msleepEm', a0)

  @staticmethod
  @overload(int)
  def usleep(a0: int) -> None:
    """
    Calls Qt's 'void QThread::usleep(unsigned long a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#usleep

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QThread::usleep(unsigned long a0)
    Rituals.call('ritual_ZN7QThread6usleepEm', a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThread'

  #  A C++ QThread Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QThread'

  #  The functions Qt calls itself that QThread is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'run': (
          ('_ZN7QThread3runEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *QThread::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QThread::metaObject() const
    address = self.uglySide.call('ritual_ZNK7QThread10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def priority(self) -> Priority:
    """
    Calls Qt's 'Priority QThread::priority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#priority

    Returns
    -------

    Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Priority(number)' gives.
    """
    #  Priority QThread::priority() const
    return QThread.Priority(self.uglySide.call(
        'ritual_ZNK7QThread8priorityEv',
    ))

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QThread::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#isFinished
    """
    #  bool QThread::isFinished() const
    return self.uglySide.call('ritual_ZNK7QThread10isFinishedEv')

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QThread::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#isRunning
    """
    #  bool QThread::isRunning() const
    return self.uglySide.call('ritual_ZNK7QThread9isRunningEv')

  def isInterruptionRequested(self) -> bool:
    """
    Calls Qt's 'bool QThread::isInterruptionRequested() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthread.html#isInterruptionRequested
    """
    #  bool QThread::isInterruptionRequested() const
    return self.uglySide.call(
        'ritual_ZNK7QThread23isInterruptionRequestedEv',
    )

  def stackSize(self) -> int:
    """
    Calls Qt's 'uint QThread::stackSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#stackSize
    """
    #  uint QThread::stackSize() const
    return self.uglySide.call('ritual_ZNK7QThread9stackSizeEv')

  def eventDispatcher(self) -> Optional[QAbstractEventDispatcher]:
    """
    Calls Qt's 'QAbstractEventDispatcher *QThread::eventDispatcher() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#eventDispatcher

    Returns
    -------

    Optional[QAbstractEventDispatcher]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractEventDispatcher *QThread::eventDispatcher() const
    address = self.uglySide.call('ritual_ZNK7QThread15eventDispatcherEv')
    from . import QAbstractEventDispatcher
    return QAbstractEventDispatcher._cuteAt(address)

  def loopLevel(self) -> int:
    """
    Calls Qt's 'int QThread::loopLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#loopLevel
    """
    #  int QThread::loopLevel() const
    return self.uglySide.call('ritual_ZNK7QThread9loopLevelEv')

  def isCurrentThread(self) -> bool:
    """
    Calls Qt's 'bool QThread::isCurrentThread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#isCurrentThread
    """
    #  bool QThread::isCurrentThread() const
    return self.uglySide.call('ritual_ZNK7QThread15isCurrentThreadEv')

  def serviceLevel(self) -> QualityOfService:
    """
    Calls Qt's 'QualityOfService QThread::serviceLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#serviceLevel

    Returns
    -------

    QualityOfService
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QualityOfService(number)'
      gives.
    """
    #  QualityOfService QThread::serviceLevel() const
    return QThread.QualityOfService(self.uglySide.call(
        'ritual_ZNK7QThread12serviceLevelEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Priority)
  def setPriority(self, priority: Priority) -> None:
    """
    Calls Qt's 'void QThread::setPriority(Priority priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#setPriority

    Parameters
    ----------

    priority : Priority
      Passed on as its number.
    """
    #  void QThread::setPriority(Priority priority)
    self.uglySide.call(
        'ritual_ZN7QThread11setPriorityENS_8PriorityE', priority.value,
    )

  @overload(int)
  def setStackSize(self, stackSize: int) -> None:
    """
    Calls Qt's 'void QThread::setStackSize(uint stackSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#setStackSize

    Parameters
    ----------

    stackSize : int
      Passed on as it is.
    """
    #  void QThread::setStackSize(uint stackSize)
    self.uglySide.call('ritual_ZN7QThread12setStackSizeEj', stackSize)

  @overload(QAbstractEventDispatcher)
  @overload(NoneType)
  def setEventDispatcher(
      self,
      eventDispatcher: Optional[QAbstractEventDispatcher],
  ) -> None:
    """
    Calls Qt's 'void QThread::setEventDispatcher(QAbstractEventDispatcher
    *eventDispatcher)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#setEventDispatcher

    Parameters
    ----------

    eventDispatcher : Optional[QAbstractEventDispatcher]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QThread::setEventDispatcher(QAbstractEventDispatcher
    #      *eventDispatcher)
    self.uglySide.call(
        'ritual_ZN7QThread18setEventDispatcherEP24QAbstractEventDispatcher',
        self._addressOf(eventDispatcher),
    )

  @overload(QualityOfService)
  def setServiceLevel(self, serviceLevel: QualityOfService) -> None:
    """
    Calls Qt's 'void QThread::setServiceLevel(QualityOfService
    serviceLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#setServiceLevel

    Parameters
    ----------

    serviceLevel : QualityOfService
      Passed on as its number.
    """
    #  void QThread::setServiceLevel(QualityOfService serviceLevel)
    self.uglySide.call(
        'ritual_ZN7QThread15setServiceLevelENS_16QualityOfServiceE',
        serviceLevel.value,
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
    Notes what was given, for Qt's 'QThread::QThread(QObject *parent)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#QThread

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QThread::QThread(QObject *parent)
    self._noteCreation(QThread, lambda: Rituals.call(
        'ritual_ZN7QThreadC1EP7QObject', self._addressOf(parent),
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

  def requestInterruption(self) -> None:
    """
    Calls Qt's 'void QThread::requestInterruption()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#requestInterruption
    """
    #  void QThread::requestInterruption()
    self.uglySide.call('ritual_ZN7QThread19requestInterruptionEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QThread::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QThread::event(QEvent *event)
    ritual = 'ritual_ZN7QThread5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN7QThread5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload()
  @overload(Priority)
  def start(self, a0: Priority = Priority.InheritPriority) -> None:
    """
    Calls Qt's 'void QThread::start(Priority a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#start

    Parameters
    ----------

    a0 : Priority
      Passed on as its number. May be left out, as in Qt: it is then
      Priority.InheritPriority.
    """
    #  void QThread::start(Priority a0)
    self.uglySide.call('ritual_ZN7QThread5startENS_8PriorityE', a0.value)

  def terminate(self) -> None:
    """
    Calls Qt's 'void QThread::terminate()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#terminate
    """
    #  void QThread::terminate()
    self.uglySide.call('ritual_ZN7QThread9terminateEv')

  @overload()
  @overload(int)
  def exit(self, retcode: int = 0) -> None:
    """
    Calls Qt's 'void QThread::exit(int retcode)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#exit

    Parameters
    ----------

    retcode : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QThread::exit(int retcode)
    self.uglySide.call('ritual_ZN7QThread4exitEi', retcode)

  def quit(self) -> None:
    """
    Calls Qt's 'void QThread::quit()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#quit
    """
    #  void QThread::quit()
    self.uglySide.call('ritual_ZN7QThread4quitEv')

  @overload(QDeadlineTimer)
  def wait(self, deadline: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QThread::wait(QDeadlineTimer deadline)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#wait

    Parameters
    ----------

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QThread::wait(QDeadlineTimer deadline)
    return self.uglySide.call(
        'ritual_ZN7QThread4waitE14QDeadlineTimer', self._valueOf(deadline),
    )

  @overload(int)
  def wait(self, time: int) -> bool:
    """
    Calls Qt's 'bool QThread::wait(unsigned long time)'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#wait

    Parameters
    ----------

    time : int
      Passed on as it is.
    """
    #  bool QThread::wait(unsigned long time)
    return self.uglySide.call('ritual_ZN7QThread4waitEm', time)

  def run(self) -> None:
    """
    Calls Qt's 'void QThread::run()'.

    Qt's own words: https://doc.qt.io/qt-6/qthread.html#run
    """
    #  void QThread::run()
    self.uglySide.call('ritual_own_ZN7QThread3runEv')
