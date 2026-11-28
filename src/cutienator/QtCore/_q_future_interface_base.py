"""
QFutureInterfaceBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfutureinterface.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QException, QRunnable, QThreadPool
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QException = WAIT['QException']
  QRunnable = WAIT['QRunnable']
  QThreadPool = WAIT['QThreadPool']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFutureInterfaceBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFutureInterfaceBase: a plain Python object standing
  in front of one C++ QFutureInterfaceBase.

  C++ hands a QFutureInterfaceBase around as a copy, so every C++
  QFutureInterfaceBase behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFutureInterfaceBase that has a ritual and that
  Python can call so far, 62 names in all: 'reportStarted', 'reportFinished',
  'reportCanceled', 'reportException', 'reportResultsReady', 'setRunnable',
  'setThreadPool', 'threadPool', 'setFilterMode', 'setProgressRange',
  'progressMinimum', 'progressMaximum', 'isProgressUpdateNeeded',
  'setProgressValue', 'progressValue', 'setProgressValueAndText',
  'progressText', 'setExpectedResultCount', 'expectedResultCount',
  'resultCount', 'queryState', 'isRunning', 'isStarted', 'isCanceled',
  'isFinished', 'isPaused', 'setPaused', 'togglePaused', 'isSuspending',
  'isSuspended', 'isThrottled', 'isResultReadyAt', 'isValid', 'loadState',
  'cancel', 'cancelAndFinish', 'cancelChain',
  'setAddResultsIfCanceledEnabled', 'isAddResultsIfCanceledEnabled',
  'setSuspended', 'toggleSuspended', 'reportSuspended', 'setThrottled',
  'waitForFinished', 'waitForNextResult', 'waitForResult', 'waitForResume',
  'suspendIfRequested', 'hasException', 'resultStoreBase', '__eq__',
  '__ne__', 'isChainCanceled', 'refT', 'derefT', 'reset',
  'rethrowPossibleException', 'cleanContinuation', 'runContinuation',
  'setLaunchAsync', 'launchAsync', 'isRunningOrPending'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFutureInterfaceBase::QFutureInterfaceBase(QFutureInterfaceBase
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QFutureInterfaceBase &QFutureInterfaceBase::operator=(const
    QFutureInterfaceBase &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QFutureInterfaceBase
    &QFutureInterfaceBase::operator=(QFutureInterfaceBase &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QFutureInterfaceBase::~QFutureInterfaceBase()': the destructor:
    Python removes its C++ QFutureInterfaceBase by it, and has no other use
    for it.
  - Qt's 'void QFutureInterfaceBase::reportException(std::exception_ptr e)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QMutex &QFutureInterfaceBase::mutex() const': gives a type Python
    has no way to take yet.
  - Qt's 'QtPrivate::ExceptionStore &QFutureInterfaceBase::exceptionStore()':
    gives a type Python has no way to take yet.
  - Qt's 'QtPrivate::ResultStoreBase
    &QFutureInterfaceBase::resultStoreBase()': gives a type Python has no way
    to take yet.
  - Qt's 'void QFutureInterfaceBase::swap(QFutureInterfaceBase &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QFutureInterfaceBase::setContinuation(std::function<void
    (const QFutureInterfaceBase &)> func, void *continuationFutureData,
    ContinuationType type)': takes a type Python has no way to hand over yet.
  - Qt's 'void QFutureInterfaceBase::setContinuation(const QObject *context,
    std::function<void ()> func, const QVariant &continuationFuture,
    ContinuationType type)': takes a type Python has no way to hand over yet.
  - Qt's 'void QFutureInterfaceBase::cancel(CancelMode mode)': names the enum
    'QFutureInterfaceBase::CancelMode', whose class cannot be named here.
  - Qt's 'void QFutureInterfaceBase::cancelChain(CancelMode mode)': names the
    enum 'QFutureInterfaceBase::CancelMode', whose class cannot be named
    here.

  What has no ritual
  ------------------

  1 of the 78 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QFutureInterfaceBase is created at the first use, not by
    'QFutureInterfaceBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFutureInterfaceBase back gives a copy the ritual
    made for Python, in a new cute QFutureInterfaceBase.
  - Each name of Qt's QFutureInterfaceBase that has no cute function yet,
    'exceptionStore', 'get', 'mutex', 'setContinuation', 'swap', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QFutureInterfaceBase, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """
    The enum 'QFutureInterfaceBase::State' of Qt, with the 9 names Qt gives
    in it.
    """

    NoState = Kee[int](0)
    Running = Kee[int](1)
    Started = Kee[int](2)
    Finished = Kee[int](4)
    Canceled = Kee[int](8)
    Suspending = Kee[int](16)
    Suspended = Kee[int](32)
    Throttled = Kee[int](64)
    Pending = Kee[int](128)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFutureInterfaceBase'

  #  Qt's '~QFutureInterfaceBase()'. Naming it makes this a value class:
  #  Python owns every C++ QFutureInterfaceBase behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QFutureInterfaceBaseD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def threadPool(self) -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QFutureInterfaceBase::threadPool() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#threadPool

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QFutureInterfaceBase::threadPool() const
    address = self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase10threadPoolEv',
    )
    from . import QThreadPool
    return QThreadPool._cuteAt(address)

  def progressMinimum(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBase::progressMinimum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#progressMinimum
    """
    #  int QFutureInterfaceBase::progressMinimum() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase15progressMinimumEv',
    )

  def progressMaximum(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBase::progressMaximum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#progressMaximum
    """
    #  int QFutureInterfaceBase::progressMaximum() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase15progressMaximumEv',
    )

  def isProgressUpdateNeeded(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isProgressUpdateNeeded() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isProgressUpdateNeeded
    """
    #  bool QFutureInterfaceBase::isProgressUpdateNeeded() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase22isProgressUpdateNeededEv',
    )

  def progressValue(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBase::progressValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#progressValue
    """
    #  int QFutureInterfaceBase::progressValue() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase13progressValueEv',
    )

  def progressText(self) -> str:
    """
    Calls Qt's 'QString QFutureInterfaceBase::progressText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#progressText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFutureInterfaceBase::progressText() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase12progressTextEv',
    )

  def resultCount(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBase::resultCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#resultCount
    """
    #  int QFutureInterfaceBase::resultCount() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase11resultCountEv',
    )

  @overload(State)
  def queryState(self, state: State) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::queryState(State state) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#queryState

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  bool QFutureInterfaceBase::queryState(State state) const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase10queryStateENS_5StateE',
        state.value,
    )

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isRunning() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isRunning
    """
    #  bool QFutureInterfaceBase::isRunning() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase9isRunningEv')

  def isStarted(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isStarted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isStarted
    """
    #  bool QFutureInterfaceBase::isStarted() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase9isStartedEv')

  def isCanceled(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isCanceled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isCanceled
    """
    #  bool QFutureInterfaceBase::isCanceled() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase10isCanceledEv',
    )

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isFinished() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isFinished
    """
    #  bool QFutureInterfaceBase::isFinished() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase10isFinishedEv',
    )

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfutureinterfacebase.html#isPaused
    """
    #  bool QFutureInterfaceBase::isPaused() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase8isPausedEv')

  def isSuspending(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isSuspending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isSuspending
    """
    #  bool QFutureInterfaceBase::isSuspending() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase12isSuspendingEv',
    )

  def isSuspended(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isSuspended() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isSuspended
    """
    #  bool QFutureInterfaceBase::isSuspended() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase11isSuspendedEv',
    )

  def isThrottled(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isThrottled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isThrottled
    """
    #  bool QFutureInterfaceBase::isThrottled() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase11isThrottledEv',
    )

  @overload(int)
  def isResultReadyAt(self, index: int) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isResultReadyAt(int index) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isResultReadyAt

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  bool QFutureInterfaceBase::isResultReadyAt(int index) const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase15isResultReadyAtEi', index,
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfutureinterfacebase.html#isValid
    """
    #  bool QFutureInterfaceBase::isValid() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase7isValidEv')

  def loadState(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBase::loadState() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#loadState
    """
    #  int QFutureInterfaceBase::loadState() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase9loadStateEv')

  def isAddResultsIfCanceledEnabled(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isAddResultsIfCanceledEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html
    """
    #  bool QFutureInterfaceBase::isAddResultsIfCanceledEnabled() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase29isAddResultsIfCanceledEnabledEv',
    )

  def hasException(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::hasException() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#hasException
    """
    #  bool QFutureInterfaceBase::hasException() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase12hasExceptionEv',
    )

  def resultStoreBase(self) -> QtPrivate.ResultStoreBase:
    """
    Calls Qt's 'const QtPrivate::ResultStoreBase
    &QFutureInterfaceBase::resultStoreBase() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#resultStoreBase

    Returns
    -------

    QtPrivate.ResultStoreBase
      A new cute QtPrivate::ResultStoreBase around the copy Qt gave back.
      Python owns it.
    """
    #  const QtPrivate::ResultStoreBase
    #      &QFutureInterfaceBase::resultStoreBase() const
    address = self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase15resultStoreBaseEv',
    )
    return QtPrivate.ResultStoreBase._cuteOwning(address)

  def isChainCanceled(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isChainCanceled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isChainCanceled
    """
    #  bool QFutureInterfaceBase::isChainCanceled() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase15isChainCanceledEv',
    )

  def refT(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::refT() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfutureinterfacebase.html#refT
    """
    #  bool QFutureInterfaceBase::refT() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase4refTEv')

  def derefT(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::derefT() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfutureinterfacebase.html#derefT
    """
    #  bool QFutureInterfaceBase::derefT() const
    return self.uglySide.call('ritual_ZNK20QFutureInterfaceBase6derefTEv')

  def launchAsync(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::launchAsync() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#launchAsync
    """
    #  bool QFutureInterfaceBase::launchAsync() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase11launchAsyncEv',
    )

  def isRunningOrPending(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::isRunningOrPending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#isRunningOrPending
    """
    #  bool QFutureInterfaceBase::isRunningOrPending() const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBase18isRunningOrPendingEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QRunnable)
  @overload(NoneType)
  def setRunnable(self, runnable: Optional[QRunnable]) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setRunnable(QRunnable *runnable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setRunnable

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFutureInterfaceBase::setRunnable(QRunnable *runnable)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase11setRunnableEP9QRunnable',
        self._addressOf(runnable, 'QRunnable'),
    )

  @overload(QThreadPool)
  @overload(NoneType)
  def setThreadPool(self, pool: Optional[QThreadPool]) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setThreadPool(QThreadPool *pool)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setThreadPool

    Parameters
    ----------

    pool : Optional[QThreadPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QFutureInterfaceBase::setThreadPool(QThreadPool *pool)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase13setThreadPoolEP11QThreadPool',
        self._addressOf(pool),
    )

  @overload(bool)
  def setFilterMode(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setFilterMode(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setFilterMode

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setFilterMode(bool enable)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase13setFilterModeEb', enable,
    )

  @overload(int, int)
  def setProgressRange(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setProgressRange(int minimum, int
    maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setProgressRange

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setProgressRange(int minimum, int maximum)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase16setProgressRangeEii',
        minimum, maximum,
    )

  @overload(int)
  def setProgressValue(self, progressValue: int) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setProgressValue(int
    progressValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setProgressValue

    Parameters
    ----------

    progressValue : int
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setProgressValue(int progressValue)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase16setProgressValueEi', progressValue,
    )

  @overload(int, str)
  def setProgressValueAndText(
      self,
      progressValue: int,
      progressText: str,
  ) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setProgressValueAndText(int
    progressValue, const QString &progressText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setProgressValueAndText

    Parameters
    ----------

    progressValue : int
      Passed on as it is.

    progressText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFutureInterfaceBase::setProgressValueAndText(int progressValue,
    #      const QString &progressText)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase23setProgressValueAndTextEiRK7QStri'
        'ng',
        progressValue, progressText,
    )

  @overload(int)
  def setExpectedResultCount(self, resultCount: int) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setExpectedResultCount(int
    resultCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setExpectedResultCount

    Parameters
    ----------

    resultCount : int
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setExpectedResultCount(int resultCount)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase22setExpectedResultCountEi',
        resultCount,
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setPaused(bool paused)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setPaused(bool paused)
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase9setPausedEb', paused)

  @overload(bool)
  def setAddResultsIfCanceledEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void
    QFutureInterfaceBase::setAddResultsIfCanceledEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setAddResultsIfCanceledEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase30setAddResultsIfCanceledEnabledEb',
        enable,
    )

  @overload(bool)
  def setSuspended(self, suspend: bool) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setSuspended(bool suspend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setSuspended

    Parameters
    ----------

    suspend : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setSuspended(bool suspend)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase12setSuspendedEb', suspend,
    )

  @overload(bool)
  def setThrottled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setThrottled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setThrottled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setThrottled(bool enable)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase12setThrottledEb', enable,
    )

  @overload(bool)
  def setLaunchAsync(self, value: bool) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::setLaunchAsync(bool value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#setLaunchAsync

    Parameters
    ----------

    value : bool
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::setLaunchAsync(bool value)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase14setLaunchAsyncEb', value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QFutureInterfaceBase) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::operator==(const
    QFutureInterfaceBase &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#operator==

    Parameters
    ----------

    other : QFutureInterfaceBase
      Passed on as a value: Qt reads the C++ QFutureInterfaceBase, which
      stays Python's own.
    """
    #  bool QFutureInterfaceBase::operator==(const QFutureInterfaceBase
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBaseeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QFutureInterfaceBase) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::operator!=(const
    QFutureInterfaceBase &other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#operator!=

    Parameters
    ----------

    other : QFutureInterfaceBase
      Passed on as a value: Qt reads the C++ QFutureInterfaceBase, which
      stays Python's own.
    """
    #  bool QFutureInterfaceBase::operator!=(const QFutureInterfaceBase
    #      &other) const
    return self.uglySide.call(
        'ritual_ZNK20QFutureInterfaceBaseneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(State)
  def __init__(self, initialState: State = State.NoState) -> None:
    """
    Notes what was given, for Qt's
    'QFutureInterfaceBase::QFutureInterfaceBase(State initialState)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#QFutureInterfaceBase

    Parameters
    ----------

    initialState : State
      Passed on as its number. May be left out, as in Qt: it is then
      State.NoState.
    """
    #  QFutureInterfaceBase::QFutureInterfaceBase(State initialState)
    self._noteCreation(QFutureInterfaceBase, lambda: Rituals.call(
        'ritual_ZN20QFutureInterfaceBaseC1ENS_5StateE', initialState.value,
    ))

  @overload(THIS)
  def __init__(self, other: QFutureInterfaceBase) -> None:
    """
    Notes what was given, for Qt's
    'QFutureInterfaceBase::QFutureInterfaceBase(const QFutureInterfaceBase
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#QFutureInterfaceBase

    Parameters
    ----------

    other : QFutureInterfaceBase
      Passed on as a value: Qt reads the C++ QFutureInterfaceBase, which
      stays Python's own.
    """
    #  QFutureInterfaceBase::QFutureInterfaceBase(const QFutureInterfaceBase
    #      &other)
    self._noteCreation(QFutureInterfaceBase, lambda: Rituals.call(
        'ritual_ZN20QFutureInterfaceBaseC1ERKS_', self._valueOf(other),
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

  def reportStarted(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reportStarted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#reportStarted
    """
    #  void QFutureInterfaceBase::reportStarted()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase13reportStartedEv')

  def reportFinished(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reportFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#reportFinished
    """
    #  void QFutureInterfaceBase::reportFinished()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase14reportFinishedEv')

  def reportCanceled(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reportCanceled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#reportCanceled
    """
    #  void QFutureInterfaceBase::reportCanceled()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase14reportCanceledEv')

  @overload(QException)
  def reportException(self, e: QException) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reportException(const QException
    &e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#reportException

    Parameters
    ----------

    e : QException
      Passed on as a value: Qt reads the C++ QException, which stays Python's
      own.
    """
    #  void QFutureInterfaceBase::reportException(const QException &e)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase15reportExceptionERK10QException',
        self._valueOf(e),
    )

  @overload(int, int)
  def reportResultsReady(self, beginIndex: int, endIndex: int) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reportResultsReady(int beginIndex,
    int endIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#reportResultsReady

    Parameters
    ----------

    beginIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::reportResultsReady(int beginIndex, int
    #      endIndex)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase18reportResultsReadyEii',
        beginIndex, endIndex,
    )

  def expectedResultCount(self) -> int:
    """
    Calls Qt's 'int QFutureInterfaceBase::expectedResultCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#expectedResultCount
    """
    #  int QFutureInterfaceBase::expectedResultCount()
    return self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase19expectedResultCountEv',
    )

  def togglePaused(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::togglePaused()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#togglePaused
    """
    #  void QFutureInterfaceBase::togglePaused()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase12togglePausedEv')

  def cancel(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qfutureinterfacebase.html#cancel
    """
    #  void QFutureInterfaceBase::cancel()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase6cancelEv')

  def cancelAndFinish(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::cancelAndFinish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#cancelAndFinish
    """
    #  void QFutureInterfaceBase::cancelAndFinish()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase15cancelAndFinishEv')

  def cancelChain(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::cancelChain()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#cancelChain
    """
    #  void QFutureInterfaceBase::cancelChain()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase11cancelChainEv')

  def toggleSuspended(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::toggleSuspended()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#toggleSuspended
    """
    #  void QFutureInterfaceBase::toggleSuspended()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase15toggleSuspendedEv')

  def reportSuspended(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reportSuspended() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#reportSuspended
    """
    #  void QFutureInterfaceBase::reportSuspended() const
    self.uglySide.call('ritual_ZNK20QFutureInterfaceBase15reportSuspendedEv')

  def waitForFinished(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::waitForFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#waitForFinished
    """
    #  void QFutureInterfaceBase::waitForFinished()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase15waitForFinishedEv')

  def waitForNextResult(self) -> bool:
    """
    Calls Qt's 'bool QFutureInterfaceBase::waitForNextResult()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#waitForNextResult
    """
    #  bool QFutureInterfaceBase::waitForNextResult()
    return self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase17waitForNextResultEv',
    )

  @overload(int)
  def waitForResult(self, resultIndex: int) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::waitForResult(int resultIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#waitForResult

    Parameters
    ----------

    resultIndex : int
      Passed on as it is.
    """
    #  void QFutureInterfaceBase::waitForResult(int resultIndex)
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase13waitForResultEi', resultIndex,
    )

  def waitForResume(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::waitForResume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#waitForResume
    """
    #  void QFutureInterfaceBase::waitForResume()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase13waitForResumeEv')

  def suspendIfRequested(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::suspendIfRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#suspendIfRequested
    """
    #  void QFutureInterfaceBase::suspendIfRequested()
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase18suspendIfRequestedEv',
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qfutureinterfacebase.html#reset
    """
    #  void QFutureInterfaceBase::reset()
    self.uglySide.call('ritual_ZN20QFutureInterfaceBase5resetEv')

  def rethrowPossibleException(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::rethrowPossibleException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#rethrowPossibleException
    """
    #  void QFutureInterfaceBase::rethrowPossibleException()
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase24rethrowPossibleExceptionEv',
    )

  def cleanContinuation(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::cleanContinuation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#cleanContinuation
    """
    #  void QFutureInterfaceBase::cleanContinuation()
    self.uglySide.call(
        'ritual_ZN20QFutureInterfaceBase17cleanContinuationEv',
    )

  def runContinuation(self) -> None:
    """
    Calls Qt's 'void QFutureInterfaceBase::runContinuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfutureinterfacebase.html#runContinuation
    """
    #  void QFutureInterfaceBase::runContinuation() const
    self.uglySide.call('ritual_ZNK20QFutureInterfaceBase15runContinuationEv')

  @staticmethod
  def exceptionStore(*__, **_) -> Never:
    """
    Qt's 'QtPrivate::ExceptionStore &QFutureInterfaceBase::exceptionStore()':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBase.exceptionStore' has no cute function yet. "
        "Qt's 'QtPrivate::ExceptionStore "
        "&QFutureInterfaceBase::exceptionStore()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QFutureInterfaceBase::get': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBase.get' has no cute function yet. Qt's "
        "'QFutureInterfaceBase::get': a template: a pattern and no single "
        "function.")

  @staticmethod
  def mutex(*__, **_) -> Never:
    """
    Qt's 'QMutex &QFutureInterfaceBase::mutex() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBase.mutex' has no cute function yet. Qt's "
        "'QMutex &QFutureInterfaceBase::mutex() const': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setContinuation(*__, **_) -> Never:
    """
    - Qt's 'void QFutureInterfaceBase::setContinuation(std::function<void
      (const QFutureInterfaceBase &)> func, void *continuationFutureData,
      ContinuationType type)': takes a type Python has no way to hand over
      yet.
    - Qt's 'void QFutureInterfaceBase::setContinuation(const QObject
      *context, std::function<void ()> func, const QVariant
      &continuationFuture, ContinuationType type)': takes a type Python has
      no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBase.setContinuation' has no cute function yet. "
        "Qt's 'void "
        "QFutureInterfaceBase::setContinuation(std::function<void (const "
        "QFutureInterfaceBase &)> func, void *continuationFutureData, "
        "ContinuationType type)': takes a type Python has no way to hand "
        "over yet. Qt's 'void QFutureInterfaceBase::setContinuation(const "
        "QObject *context, std::function<void ()> func, const QVariant "
        "&continuationFuture, ContinuationType type)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QFutureInterfaceBase::swap(QFutureInterfaceBase &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFutureInterfaceBase.swap' has no cute function yet. Qt's 'void "
        "QFutureInterfaceBase::swap(QFutureInterfaceBase &other)': takes a "
        "type Python has no way to hand over yet.")
