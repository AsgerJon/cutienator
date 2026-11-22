"""
QFutureWatcherBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfuturewatcher.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QEvent, QMetaMethod, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMetaMethod = WAIT['QMetaMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFutureWatcherBase(QObject):
  """
  The cute side of Qt's QFutureWatcherBase: a plain Python object standing in
  front of one C++ QFutureWatcherBase.

  It is built on the cute 'QObject', as Qt's QFutureWatcherBase is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFutureWatcherBase that has a ritual and that Python
  can call so far, 26 names in all: 'metaObject', 'tr', 'progressValue',
  'progressMinimum', 'progressMaximum', 'progressText', 'isStarted',
  'isFinished', 'isRunning', 'isCanceled', 'isPaused', 'isSuspending',
  'isSuspended', 'waitForFinished', 'setPendingResultsLimit', 'event',
  'cancel', 'setSuspended', 'suspend', 'resume', 'toggleSuspended',
  'setPaused', 'pause', 'togglePaused', 'connectNotify', 'disconnectNotify'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has no ritual
  ------------------

  23 of the 49 functions Qt declares: 12 a signal; 5 private; 2 takes or
  gives a type that cannot be passed yet; 2 protected; 1 a template; 1 the
  class is abstract, so C++ cannot make one.

  What to expect
  --------------

  - The C++ QFutureWatcherBase is created at the first use, not by
    'QFutureWatcherBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFutureWatcherBase.
  - Qt tells when it has removed the C++ QFutureWatcherBase. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QFutureWatcherBase::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#tr

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
    #  QString QFutureWatcherBase::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QFutureWatcherBase2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFutureWatcherBase'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFutureWatcherBase::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFutureWatcherBase::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase10metaObjectEv',
    )
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def progressValue(self) -> int:
    """
    Calls Qt's 'int QFutureWatcherBase::progressValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressValue
    """
    #  int QFutureWatcherBase::progressValue() const
    return self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase13progressValueEv',
    )

  def progressMinimum(self) -> int:
    """
    Calls Qt's 'int QFutureWatcherBase::progressMinimum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressMinimum
    """
    #  int QFutureWatcherBase::progressMinimum() const
    return self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase15progressMinimumEv',
    )

  def progressMaximum(self) -> int:
    """
    Calls Qt's 'int QFutureWatcherBase::progressMaximum() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressMaximum
    """
    #  int QFutureWatcherBase::progressMaximum() const
    return self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase15progressMaximumEv',
    )

  def progressText(self) -> str:
    """
    Calls Qt's 'QString QFutureWatcherBase::progressText() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressText

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFutureWatcherBase::progressText() const
    return self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase12progressTextEv',
    )

  def isStarted(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isStarted() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#isStarted
    """
    #  bool QFutureWatcherBase::isStarted() const
    return self.uglySide.call('ritual_ZNK18QFutureWatcherBase9isStartedEv')

  def isFinished(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isFinished() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#isFinished
    """
    #  bool QFutureWatcherBase::isFinished() const
    return self.uglySide.call('ritual_ZNK18QFutureWatcherBase10isFinishedEv')

  def isRunning(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isRunning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#isRunning
    """
    #  bool QFutureWatcherBase::isRunning() const
    return self.uglySide.call('ritual_ZNK18QFutureWatcherBase9isRunningEv')

  def isCanceled(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isCanceled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#isCanceled
    """
    #  bool QFutureWatcherBase::isCanceled() const
    return self.uglySide.call('ritual_ZNK18QFutureWatcherBase10isCanceledEv')

  def isPaused(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isPaused() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#isPaused
    """
    #  bool QFutureWatcherBase::isPaused() const
    return self.uglySide.call('ritual_ZNK18QFutureWatcherBase8isPausedEv')

  def isSuspending(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isSuspending() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#isSuspending
    """
    #  bool QFutureWatcherBase::isSuspending() const
    return self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase12isSuspendingEv',
    )

  def isSuspended(self) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::isSuspended() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#isSuspended
    """
    #  bool QFutureWatcherBase::isSuspended() const
    return self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase11isSuspendedEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPendingResultsLimit(self, limit: int) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::setPendingResultsLimit(int limit)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#setPendingResultsLimit

    Parameters
    ----------

    limit : int
      Passed on as it is.
    """
    #  void QFutureWatcherBase::setPendingResultsLimit(int limit)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase22setPendingResultsLimitEi', limit,
    )

  @overload(bool)
  def setSuspended(self, suspend: bool) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::setSuspended(bool suspend)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#setSuspended

    Parameters
    ----------

    suspend : bool
      Passed on as it is.
    """
    #  void QFutureWatcherBase::setSuspended(bool suspend)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase12setSuspendedEb', suspend,
    )

  @overload(bool)
  def setPaused(self, paused: bool) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::setPaused(bool paused)'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#setPaused

    Parameters
    ----------

    paused : bool
      Passed on as it is.
    """
    #  void QFutureWatcherBase::setPaused(bool paused)
    self.uglySide.call('ritual_ZN18QFutureWatcherBase9setPausedEb', paused)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def waitForFinished(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::waitForFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#waitForFinished
    """
    #  void QFutureWatcherBase::waitForFinished()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase15waitForFinishedEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QFutureWatcherBase::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QFutureWatcherBase::event(QEvent *event)
    ritual = 'ritual_ZN18QFutureWatcherBase5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QFutureWatcherBase5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  def cancel(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#cancel
    """
    #  void QFutureWatcherBase::cancel()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase6cancelEv')

  def suspend(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::suspend()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#suspend
    """
    #  void QFutureWatcherBase::suspend()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase7suspendEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#resume
    """
    #  void QFutureWatcherBase::resume()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase6resumeEv')

  def toggleSuspended(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::toggleSuspended()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#toggleSuspended
    """
    #  void QFutureWatcherBase::toggleSuspended()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase15toggleSuspendedEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#pause
    """
    #  void QFutureWatcherBase::pause()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase5pauseEv')

  def togglePaused(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::togglePaused()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#togglePaused
    """
    #  void QFutureWatcherBase::togglePaused()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase12togglePausedEv')

  @overload(QMetaMethod)
  def connectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::connectNotify(const QMetaMethod
    &signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#connectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QFutureWatcherBase::connectNotify(const QMetaMethod &signal)
    self.uglySide.call(
        'ritual_own_ZN18QFutureWatcherBase13connectNotifyERK11QMetaMethod',
        self._valueOf(signal),
    )

  @overload(QMetaMethod)
  def disconnectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::disconnectNotify(const QMetaMethod
    &signal)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#disconnectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QFutureWatcherBase::disconnectNotify(const QMetaMethod &signal)
    self.uglySide.call(
        'ritual_own_ZN18QFutureWatcherBase16disconnectNotifyERK11QMetaMetho'
        'd',
        self._valueOf(signal),
    )
