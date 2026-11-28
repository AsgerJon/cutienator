"""
QThreadPoolPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qthreadpool_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QThreadPoolPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDeadlineTimer, QRunnable, QThreadPool
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QRunnable = WAIT['QRunnable']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QThreadPoolPrivate(QObjectPrivate):
  """
  The cute side of Qt's QThreadPoolPrivate: a plain Python object standing in
  front of one C++ QThreadPoolPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QThreadPoolPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QThreadPoolPrivate that has a ritual and that Python
  can call so far, 13 names in all: 'q_func', 'tryStart', 'enqueueTask',
  'activeThreadCount', 'tryToStartMoreThreads', 'areAllThreadsActive',
  'tooManyThreadsActive', 'maxThreadCount', 'startThread', 'reset',
  'waitForDone', 'clear', 'stealAndRunRunnable'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QThreadPool *QThreadPoolPrivate::q_func() const': takes in
    Python what 'QThreadPool *QThreadPoolPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 16 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QThreadPoolPrivate is created at the first use, not by
    'QThreadPoolPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QThreadPoolPrivate.
  - Each name of Qt's QThreadPoolPrivate that has no cute function yet,
    'deletePageIfFinished', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QThreadPoolPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def activeThreadCount(self) -> int:
    """
    Calls Qt's 'int QThreadPoolPrivate::activeThreadCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#activeThreadCount
    """
    #  int QThreadPoolPrivate::activeThreadCount() const
    return self.uglySide.call(
        'ritual_ZNK18QThreadPoolPrivate17activeThreadCountEv',
    )

  def areAllThreadsActive(self) -> bool:
    """
    Calls Qt's 'bool QThreadPoolPrivate::areAllThreadsActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#areAllThreadsActive
    """
    #  bool QThreadPoolPrivate::areAllThreadsActive() const
    return self.uglySide.call(
        'ritual_ZNK18QThreadPoolPrivate19areAllThreadsActiveEv',
    )

  def tooManyThreadsActive(self) -> bool:
    """
    Calls Qt's 'bool QThreadPoolPrivate::tooManyThreadsActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#tooManyThreadsActive
    """
    #  bool QThreadPoolPrivate::tooManyThreadsActive() const
    return self.uglySide.call(
        'ritual_ZNK18QThreadPoolPrivate20tooManyThreadsActiveEv',
    )

  def maxThreadCount(self) -> int:
    """
    Calls Qt's 'int QThreadPoolPrivate::maxThreadCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#maxThreadCount
    """
    #  int QThreadPoolPrivate::maxThreadCount() const
    return self.uglySide.call(
        'ritual_ZNK18QThreadPoolPrivate14maxThreadCountEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Notes what was given, for Qt's
    'QThreadPoolPrivate::QThreadPoolPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#QThreadPoolPrivate
    """
    #  QThreadPoolPrivate::QThreadPoolPrivate()
    self._noteCreation(QThreadPoolPrivate, lambda: Rituals.call(
        'ritual_ZN18QThreadPoolPrivateC1Ev',
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

  def q_func(self) -> Optional[QThreadPool]:
    """
    Calls Qt's 'QThreadPool *QThreadPoolPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpoolprivate.html#q_func

    Returns
    -------

    Optional[QThreadPool]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThreadPool *QThreadPoolPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QThreadPoolPrivate6q_funcEv')
    from . import QThreadPool
    return QThreadPool._cuteAt(address)

  @overload(QRunnable)
  @overload(NoneType)
  def tryStart(self, task: Optional[QRunnable]) -> bool:
    """
    Calls Qt's 'bool QThreadPoolPrivate::tryStart(QRunnable *task)'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpoolprivate.html#tryStart

    Parameters
    ----------

    task : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QThreadPoolPrivate::tryStart(QRunnable *task)
    return self.uglySide.call(
        'ritual_ZN18QThreadPoolPrivate8tryStartEP9QRunnable',
        self._addressOf(task, 'QRunnable'),
    )

  @overload(QRunnable)
  @overload(NoneType)
  @overload(QRunnable, int)
  @overload(NoneType, int)
  def enqueueTask(
      self,
      task: Optional[QRunnable],
      priority: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QThreadPoolPrivate::enqueueTask(QRunnable *task, int
    priority)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#enqueueTask

    Parameters
    ----------

    task : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    priority : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QThreadPoolPrivate::enqueueTask(QRunnable *task, int priority)
    self.uglySide.call(
        'ritual_ZN18QThreadPoolPrivate11enqueueTaskEP9QRunnablei',
        self._addressOf(task, 'QRunnable'), priority,
    )

  def tryToStartMoreThreads(self) -> None:
    """
    Calls Qt's 'void QThreadPoolPrivate::tryToStartMoreThreads()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#tryToStartMoreThreads
    """
    #  void QThreadPoolPrivate::tryToStartMoreThreads()
    self.uglySide.call(
        'ritual_ZN18QThreadPoolPrivate21tryToStartMoreThreadsEv',
    )

  @overload()
  @overload(QRunnable)
  @overload(NoneType)
  def startThread(self, runnable: Optional[QRunnable] = None) -> None:
    """
    Calls Qt's 'void QThreadPoolPrivate::startThread(QRunnable *runnable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#startThread

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QThreadPoolPrivate::startThread(QRunnable *runnable)
    self.uglySide.call(
        'ritual_ZN18QThreadPoolPrivate11startThreadEP9QRunnable',
        self._addressOf(runnable, 'QRunnable'),
    )

  def reset(self) -> None:
    """
    Calls Qt's 'void QThreadPoolPrivate::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpoolprivate.html#reset
    """
    #  void QThreadPoolPrivate::reset()
    self.uglySide.call('ritual_ZN18QThreadPoolPrivate5resetEv')

  @overload(QDeadlineTimer)
  def waitForDone(self, timer: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QThreadPoolPrivate::waitForDone(const QDeadlineTimer
    &timer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#waitForDone

    Parameters
    ----------

    timer : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QThreadPoolPrivate::waitForDone(const QDeadlineTimer &timer)
    return self.uglySide.call(
        'ritual_ZN18QThreadPoolPrivate11waitForDoneERK14QDeadlineTimer',
        self._valueOf(timer),
    )

  def clear(self) -> None:
    """
    Calls Qt's 'void QThreadPoolPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qthreadpoolprivate.html#clear
    """
    #  void QThreadPoolPrivate::clear()
    self.uglySide.call('ritual_ZN18QThreadPoolPrivate5clearEv')

  @overload(QRunnable)
  @overload(NoneType)
  def stealAndRunRunnable(self, runnable: Optional[QRunnable]) -> None:
    """
    Calls Qt's 'void QThreadPoolPrivate::stealAndRunRunnable(QRunnable
    *runnable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qthreadpoolprivate.html#stealAndRunRunnable

    Parameters
    ----------

    runnable : Optional[QRunnable]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QThreadPoolPrivate::stealAndRunRunnable(QRunnable *runnable)
    self.uglySide.call(
        'ritual_ZN18QThreadPoolPrivate19stealAndRunRunnableEP9QRunnable',
        self._addressOf(runnable, 'QRunnable'),
    )

  @staticmethod
  def deletePageIfFinished(*__, **_) -> Never:
    """
    Qt's 'void QThreadPoolPrivate::deletePageIfFinished(QueuePage *page)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QThreadPoolPrivate.deletePageIfFinished' has no cute function "
        "yet. Qt's 'void QThreadPoolPrivate::deletePageIfFinished(QueuePage "
        "*page)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
