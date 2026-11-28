"""
QtConcurrent::ThreadEngineBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtConcurrent/qtconcurrentthreadengine.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QRunnable
from . import QtConcurrent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QException, QThreadPool
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QException = WAIT['QException']
  QThreadPool = WAIT['QThreadPool']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ThreadEngineBase(QRunnable):
  """
  The cute side of Qt's QtConcurrent::ThreadEngineBase: a plain Python object
  standing in front of one C++ QtConcurrent::ThreadEngineBase.

  It is built on the cute 'QRunnable', as Qt's QtConcurrent::ThreadEngineBase
  is built on Qt's QRunnable, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QtConcurrent::ThreadEngineBase that has a ritual and
  that Python can call so far, 21 names in all: 'startSingleThreaded',
  'startThread', 'isCanceled', 'waitForResume', 'isProgressReportingEnabled',
  'setProgressValue', 'setProgressRange', 'acquireBarrierSemaphore',
  'reportIfSuspensionDone', 'start', 'finish', 'threadFunction',
  'shouldStartThread', 'shouldThrottleThread', 'startThreadInternal',
  'startThreads', 'threadExit', 'threadThrottleExit', 'run',
  'asynchronousFinish', 'handleException'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtConcurrent::ThreadEngineBase::~ThreadEngineBase()': the
    destructor: Python never removes a C++ QtConcurrent::ThreadEngineBase.

  What to expect
  --------------

  - The C++ QtConcurrent::ThreadEngineBase is created at the first use, not
    by 'QtConcurrent::ThreadEngineBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtConcurrent::ThreadEngineBase.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtConcurrent::ThreadEngineBase'

  #  A C++ QtConcurrent::ThreadEngineBase Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QtConcurrent_ThreadEngineBase'

  #  The functions Qt calls itself that QtConcurrent::ThreadEngineBase is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'start': (
          ('_ZN12QtConcurrent16ThreadEngineBase5startEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'finish': (
          ('_ZN12QtConcurrent16ThreadEngineBase6finishEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'threadFunction': (
          ('_ZN12QtConcurrent16ThreadEngineBase14threadFunctionEv',
           ('int', 'enum', 'QtConcurrent:QtConcurrent.ThreadFunctionResult'),
           ()),
      ),
      'shouldStartThread': (
          ('_ZN12QtConcurrent16ThreadEngineBase17shouldStartThreadEv',
           ('bool', 'number', ''),
           ()),
      ),
      'shouldThrottleThread': (
          ('_ZN12QtConcurrent16ThreadEngineBase20shouldThrottleThreadEv',
           ('bool', 'number', ''),
           ()),
      ),
      'asynchronousFinish': (
          ('_ZN12QtConcurrent16ThreadEngineBase18asynchronousFinishEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setProgressValue(self, progress: int) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::setProgressValue(int
    progress)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html

    Parameters
    ----------

    progress : int
      Passed on as it is.
    """
    #  void QtConcurrent::ThreadEngineBase::setProgressValue(int progress)
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase16setProgressValueEi',
        progress,
    )

  @overload(int, int)
  def setProgressRange(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::setProgressRange(int
    minimum, int maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QtConcurrent::ThreadEngineBase::setProgressRange(int minimum, int
    #      maximum)
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase16setProgressRangeEii',
        minimum, maximum,
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

  @overload(QThreadPool)
  @overload(NoneType)
  def __init__(self, pool: Optional[QThreadPool]) -> None:
    """
    Notes what was given, for Qt's
    'QtConcurrent::ThreadEngineBase::ThreadEngineBase(QThreadPool *pool)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html

    Parameters
    ----------

    pool : Optional[QThreadPool]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QtConcurrent::ThreadEngineBase::ThreadEngineBase(QThreadPool *pool)
    self._noteCreation(ThreadEngineBase, lambda: Rituals.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBaseC1EP11QThreadPool',
        self._addressOf(pool),
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

  def startSingleThreaded(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::startSingleThreaded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  void QtConcurrent::ThreadEngineBase::startSingleThreaded()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase19startSingleThreadedEv',
    )

  def startThread(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::startThread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#startThread
    """
    #  void QtConcurrent::ThreadEngineBase::startThread()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase11startThreadEv',
    )

  def isCanceled(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::ThreadEngineBase::isCanceled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#isCanceled
    """
    #  bool QtConcurrent::ThreadEngineBase::isCanceled()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase10isCanceledEv',
    )

  def waitForResume(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::waitForResume()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#waitForResume
    """
    #  void QtConcurrent::ThreadEngineBase::waitForResume()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase13waitForResumeEv',
    )

  def isProgressReportingEnabled(self) -> bool:
    """
    Calls Qt's 'bool
    QtConcurrent::ThreadEngineBase::isProgressReportingEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  bool QtConcurrent::ThreadEngineBase::isProgressReportingEnabled()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase26isProgressReportingEnab'
        'ledEv',
    )

  def acquireBarrierSemaphore(self) -> None:
    """
    Calls Qt's 'void
    QtConcurrent::ThreadEngineBase::acquireBarrierSemaphore()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  void QtConcurrent::ThreadEngineBase::acquireBarrierSemaphore()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase23acquireBarrierSemaphore'
        'Ev',
    )

  def reportIfSuspensionDone(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::reportIfSuspensionDone()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  void QtConcurrent::ThreadEngineBase::reportIfSuspensionDone() const
    self.uglySide.call(
        'ritual_ZNK12QtConcurrent16ThreadEngineBase22reportIfSuspensionDone'
        'Ev',
    )

  def start(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::start()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#start
    """
    #  void QtConcurrent::ThreadEngineBase::start()
    ritual = 'ritual_ZN12QtConcurrent16ThreadEngineBase5startEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QtConcurrent16ThreadEngineBase5startEv'
    self.uglySide.call(ritual)

  def finish(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::finish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#finish
    """
    #  void QtConcurrent::ThreadEngineBase::finish()
    ritual = 'ritual_ZN12QtConcurrent16ThreadEngineBase6finishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QtConcurrent16ThreadEngineBase6finishEv'
    self.uglySide.call(ritual)

  def threadFunction(self) -> QtConcurrent.ThreadFunctionResult:
    """
    Calls Qt's 'ThreadFunctionResult
    QtConcurrent::ThreadEngineBase::threadFunction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#threadFunction

    Returns
    -------

    QtConcurrent.ThreadFunctionResult
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtConcurrent.ThreadFunctionResult(number)' gives.
    """
    #  ThreadFunctionResult QtConcurrent::ThreadEngineBase::threadFunction()
    ritual = 'ritual_ZN12QtConcurrent16ThreadEngineBase14threadFunctionEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QtConcurrent16ThreadEngineBase14threadFunctionEv')
    return QtConcurrent.ThreadFunctionResult(self.uglySide.call(ritual))

  def shouldStartThread(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::ThreadEngineBase::shouldStartThread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  bool QtConcurrent::ThreadEngineBase::shouldStartThread()
    ritual = 'ritual_ZN12QtConcurrent16ThreadEngineBase17shouldStartThreadEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QtConcurrent16ThreadEngineBase17shouldStartThread'
          'Ev')
    return self.uglySide.call(ritual)

  def shouldThrottleThread(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::ThreadEngineBase::shouldThrottleThread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  bool QtConcurrent::ThreadEngineBase::shouldThrottleThread()
    ritual = (
        'ritual_ZN12QtConcurrent16ThreadEngineBase20shouldThrottleThreadEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QtConcurrent16ThreadEngineBase20shouldThrottleThr'
          'eadEv')
    return self.uglySide.call(ritual)

  def startThreadInternal(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::ThreadEngineBase::startThreadInternal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  bool QtConcurrent::ThreadEngineBase::startThreadInternal()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase19startThreadInternalEv',
    )

  def startThreads(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::startThreads()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#startThreads
    """
    #  void QtConcurrent::ThreadEngineBase::startThreads()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase12startThreadsEv',
    )

  def threadExit(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::threadExit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#threadExit
    """
    #  void QtConcurrent::ThreadEngineBase::threadExit()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase10threadExitEv',
    )

  def threadThrottleExit(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::ThreadEngineBase::threadThrottleExit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  bool QtConcurrent::ThreadEngineBase::threadThrottleExit()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase18threadThrottleExitEv',
    )

  def run(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#run
    """
    #  void QtConcurrent::ThreadEngineBase::run()
    ritual = 'ritual_ZN12QtConcurrent16ThreadEngineBase3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QtConcurrent16ThreadEngineBase3runEv'
    self.uglySide.call(ritual)

  def asynchronousFinish(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::asynchronousFinish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html
    """
    #  void QtConcurrent::ThreadEngineBase::asynchronousFinish()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase18asynchronousFinishEv',
    )

  @overload(QException)
  def handleException(self, exception: QException) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBase::handleException(const
    QException &exception)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebase.html#handleException

    Parameters
    ----------

    exception : QException
      Passed on as a value: Qt reads the C++ QException, which stays Python's
      own.
    """
    #  void QtConcurrent::ThreadEngineBase::handleException(const QException
    #      &exception)
    self.uglySide.call(
        'ritual_ZN12QtConcurrent16ThreadEngineBase15handleExceptionERK10QEx'
        'ception',
        self._valueOf(exception),
    )
