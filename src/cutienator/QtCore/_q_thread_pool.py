"""
QThreadPool binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qthreadpool.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject, QThreadPriority, QThreadQualityOfService

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDeadlineTimer, QMetaObject, QRunnable, QThread
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QRunnable = WAIT['QRunnable']
  QThread = WAIT['QThread']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThreadPool(QObject):
  """
  The cute side of Qt's QThreadPool: a plain Python object standing in front
  of one C++ QThreadPool.

  It is built on the cute 'QObject', as Qt's QThreadPool is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QThreadPool that has a ritual and that Python can
  call so far, 23 names in all: 'metaObject', 'tr', 'globalInstance',
  'start', 'tryStart', 'startOnReservedThread', 'expiryTimeout',
  'setExpiryTimeout', 'maxThreadCount', 'setMaxThreadCount',
  'activeThreadCount', 'setStackSize', 'stackSize', 'setThreadPriority',
  'threadPriority', 'reserveThread', 'releaseThread', 'setServiceLevel',
  'serviceLevel', 'waitForDone', 'clear', 'contains', 'tryTake'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QThreadPool::~QThreadPool()': the destructor: Python never removes
    a C++ QThreadPool.

  What has no ritual
  ------------------

  9 of the 35 functions Qt declares: 4 a template; 3 private; 2 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QThreadPool is created at the first use, not by
    'QThreadPool(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QThreadPool.
  - Qt tells when it has removed the C++ QThreadPool. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QThreadPool::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#tr

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
    #  QString QThreadPool::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QThreadPool2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def globalInstance() -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QThreadPool::globalInstance()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#globalInstance

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QThreadPool::globalInstance()
    address = Rituals.call('ritual_ZN11QThreadPool14globalInstanceEv')
    return QThreadPool._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThreadPool'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QThreadPool::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QThreadPool::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QThreadPool10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def expiryTimeout(self) -> int:
    """
    Calls Qt's 'int QThreadPool::expiryTimeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#expiryTimeout
    """
    #  int QThreadPool::expiryTimeout() const
    return self.uglySide.call('ritual_ZNK11QThreadPool13expiryTimeoutEv')

  def maxThreadCount(self) -> int:
    """
    Calls Qt's 'int QThreadPool::maxThreadCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#maxThreadCount
    """
    #  int QThreadPool::maxThreadCount() const
    return self.uglySide.call('ritual_ZNK11QThreadPool14maxThreadCountEv')

  def activeThreadCount(self) -> int:
    """
    Calls Qt's 'int QThreadPool::activeThreadCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#activeThreadCount
    """
    #  int QThreadPool::activeThreadCount() const
    return self.uglySide.call('ritual_ZNK11QThreadPool17activeThreadCountEv')

  def stackSize(self) -> int:
    """
    Calls Qt's 'uint QThreadPool::stackSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#stackSize
    """
    #  uint QThreadPool::stackSize() const
    return self.uglySide.call('ritual_ZNK11QThreadPool9stackSizeEv')

  def threadPriority(self) -> QThread.Priority:
    """
    Calls Qt's 'QThread::Priority QThreadPool::threadPriority() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#threadPriority

    Returns
    -------

    QThread.Priority
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QThread.Priority(number)'
      gives.
    """
    #  QThread::Priority QThreadPool::threadPriority() const
    return QThreadPriority(self.uglySide.call(
        'ritual_ZNK11QThreadPool14threadPriorityEv',
    ))

  def serviceLevel(self) -> QThread.QualityOfService:
    """
    Calls Qt's 'QThread::QualityOfService QThreadPool::serviceLevel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#serviceLevel

    Returns
    -------

    QThread.QualityOfService
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QThread.QualityOfService(number)' gives.
    """
    #  QThread::QualityOfService QThreadPool::serviceLevel() const
    return QThreadQualityOfService(self.uglySide.call(
        'ritual_ZNK11QThreadPool12serviceLevelEv',
    ))

  @overload(QThread)
  @overload(NoneType)
  def contains(self, thread: Optional[QThread]) -> bool:
    """
    Calls Qt's 'bool QThreadPool::contains(const QThread *thread) const'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#contains

    Parameters
    ----------

    thread : Optional[QThread]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QThreadPool::contains(const QThread *thread) const
    return self.uglySide.call(
        'ritual_ZNK11QThreadPool8containsEPK7QThread',
        self._addressOf(thread),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setExpiryTimeout(self, expiryTimeout: int) -> None:
    """
    Calls Qt's 'void QThreadPool::setExpiryTimeout(int expiryTimeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#setExpiryTimeout

    Parameters
    ----------

    expiryTimeout : int
      Passed on as it is.
    """
    #  void QThreadPool::setExpiryTimeout(int expiryTimeout)
    self.uglySide.call(
        'ritual_ZN11QThreadPool16setExpiryTimeoutEi', expiryTimeout,
    )

  @overload(int)
  def setMaxThreadCount(self, maxThreadCount: int) -> None:
    """
    Calls Qt's 'void QThreadPool::setMaxThreadCount(int maxThreadCount)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#setMaxThreadCount

    Parameters
    ----------

    maxThreadCount : int
      Passed on as it is.
    """
    #  void QThreadPool::setMaxThreadCount(int maxThreadCount)
    self.uglySide.call(
        'ritual_ZN11QThreadPool17setMaxThreadCountEi', maxThreadCount,
    )

  @overload(int)
  def setStackSize(self, stackSize: int) -> None:
    """
    Calls Qt's 'void QThreadPool::setStackSize(uint stackSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#setStackSize

    Parameters
    ----------

    stackSize : int
      Passed on as it is.
    """
    #  void QThreadPool::setStackSize(uint stackSize)
    self.uglySide.call('ritual_ZN11QThreadPool12setStackSizeEj', stackSize)

  @overload(QThreadPriority)
  def setThreadPriority(self, priority: QThread.Priority) -> None:
    """
    Calls Qt's 'void QThreadPool::setThreadPriority(QThread::Priority
    priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#setThreadPriority

    Parameters
    ----------

    priority : QThread.Priority
      Passed on as its number.
    """
    #  void QThreadPool::setThreadPriority(QThread::Priority priority)
    self.uglySide.call(
        'ritual_ZN11QThreadPool17setThreadPriorityEN7QThread8PriorityE',
        priority.value,
    )

  @overload(QThreadQualityOfService)
  def setServiceLevel(self, serviceLevel: QThread.QualityOfService) -> None:
    """
    Calls Qt's 'void QThreadPool::setServiceLevel(QThread::QualityOfService
    serviceLevel)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#setServiceLevel

    Parameters
    ----------

    serviceLevel : QThread.QualityOfService
      Passed on as its number.
    """
    #  void QThreadPool::setServiceLevel(QThread::QualityOfService
    #      serviceLevel)
    self.uglySide.call(
        'ritual_ZN11QThreadPool15setServiceLevelEN7QThread16QualityOfServic'
        'eE',
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
    Notes what was given, for Qt's 'QThreadPool::QThreadPool(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#QThreadPool

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QThreadPool::QThreadPool(QObject *parent)
    self._noteCreation(QThreadPool, lambda: Rituals.call(
        'ritual_ZN11QThreadPoolC1EP7QObject', self._addressOf(parent),
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

  @overload(QRunnable)
  @overload(NoneType)
  @overload(QRunnable, int)
  @overload(NoneType, int)
  def start(self, runnable: Optional[QRunnable], priority: int = 0) -> None:
    """
    Calls Qt's 'void QThreadPool::start(QRunnable *runnable, int priority)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#start

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    priority : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QThreadPool::start(QRunnable *runnable, int priority)
    self.uglySide.call(
        'ritual_ZN11QThreadPool5startEP9QRunnablei',
        self._addressOf(runnable), priority,
    )

  @overload(QRunnable)
  @overload(NoneType)
  def tryStart(self, runnable: Optional[QRunnable]) -> bool:
    """
    Calls Qt's 'bool QThreadPool::tryStart(QRunnable *runnable)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#tryStart

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QThreadPool::tryStart(QRunnable *runnable)
    return self.uglySide.call(
        'ritual_ZN11QThreadPool8tryStartEP9QRunnable',
        self._addressOf(runnable),
    )

  @overload(QRunnable)
  @overload(NoneType)
  def startOnReservedThread(self, runnable: Optional[QRunnable]) -> None:
    """
    Calls Qt's 'void QThreadPool::startOnReservedThread(QRunnable
    *runnable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpool.html#startOnReservedThread

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QThreadPool::startOnReservedThread(QRunnable *runnable)
    self.uglySide.call(
        'ritual_ZN11QThreadPool21startOnReservedThreadEP9QRunnable',
        self._addressOf(runnable),
    )

  def reserveThread(self) -> None:
    """
    Calls Qt's 'void QThreadPool::reserveThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#reserveThread
    """
    #  void QThreadPool::reserveThread()
    self.uglySide.call('ritual_ZN11QThreadPool13reserveThreadEv')

  def releaseThread(self) -> None:
    """
    Calls Qt's 'void QThreadPool::releaseThread()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#releaseThread
    """
    #  void QThreadPool::releaseThread()
    self.uglySide.call('ritual_ZN11QThreadPool13releaseThreadEv')

  @overload(int)
  def waitForDone(self, msecs: int) -> bool:
    """
    Calls Qt's 'bool QThreadPool::waitForDone(int msecs)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#waitForDone

    Parameters
    ----------

    msecs : int
      Passed on as it is.
    """
    #  bool QThreadPool::waitForDone(int msecs)
    return self.uglySide.call('ritual_ZN11QThreadPool11waitForDoneEi', msecs)

  @overload(QDeadlineTimer)
  def waitForDone(self, deadline: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QThreadPool::waitForDone(QDeadlineTimer deadline)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#waitForDone

    Parameters
    ----------

    deadline : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QThreadPool::waitForDone(QDeadlineTimer deadline)
    return self.uglySide.call(
        'ritual_ZN11QThreadPool11waitForDoneE14QDeadlineTimer',
        self._valueOf(deadline),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QThreadPool::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#clear
    """
    #  void QThreadPool::clear()
    self.uglySide.call('ritual_ZN11QThreadPool5clearEv')

  @overload(QRunnable)
  @overload(NoneType)
  def tryTake(self, runnable: Optional[QRunnable]) -> bool:
    """
    Calls Qt's 'bool QThreadPool::tryTake(QRunnable *runnable)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpool.html#tryTake

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QThreadPool::tryTake(QRunnable *runnable)
    return self.uglySide.call(
        'ritual_ZN11QThreadPool7tryTakeEP9QRunnable',
        self._addressOf(runnable),
    )
