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
  from typing import Never, Optional

  from . import QEvent, QFutureInterfaceBase, QFutureWatcherBasePrivate
  from . import QMetaMethod, QMetaObject
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
  can call so far, 42 names in all: 'metaObject', 'tr', 'd_func',
  'progressValue', 'progressMinimum', 'progressMaximum', 'progressText',
  'isStarted', 'isFinished', 'isRunning', 'isCanceled', 'isPaused',
  'isSuspending', 'isSuspended', 'waitForFinished', 'setPendingResultsLimit',
  'event', 'started', 'finished', 'canceled', 'paused', 'suspending',
  'suspended', 'resumed', 'resultReadyAt', 'resultsReadyAt',
  'progressRangeChanged', 'progressValueChanged', 'progressTextChanged',
  'cancel', 'setSuspended', 'suspend', 'resume', 'toggleSuspended',
  'setPaused', 'pause', 'togglePaused', 'connectNotify', 'disconnectNotify',
  'connectOutputInterface', 'disconnectOutputInterface', 'futureInterface'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QFutureWatcherBase::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QFutureWatcherBase::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QFutureWatcherBasePrivate *QFutureWatcherBase::d_func()
    const': takes in Python what 'QFutureWatcherBasePrivate
    *QFutureWatcherBase::d_func()' takes.
  - Qt's 'QFutureInterfaceBase &QFutureWatcherBase::futureInterface()': gives
    a type Python has no way to take yet.

  What has no ritual
  ------------------

  3 of the 49 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

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
  - Each name of Qt's QFutureWatcherBase that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
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

  #  The functions Qt calls itself that QFutureWatcherBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'futureInterface': (
          ('_ZNK18QFutureWatcherBase15futureInterfaceEv',
           ('address', 'value', 'QtCore:QFutureInterfaceBase'),
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

  def futureInterface(self) -> QFutureInterfaceBase:
    """
    Calls Qt's 'const QFutureInterfaceBase
    &QFutureWatcherBase::futureInterface() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#futureInterface

    Returns
    -------

    QFutureInterfaceBase
      A new cute QFutureInterfaceBase around the copy Qt gave back. Python
      owns it.
    """
    #  const QFutureInterfaceBase &QFutureWatcherBase::futureInterface()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QFutureWatcherBase15futureInterfaceEv',
    )
    from . import QFutureInterfaceBase
    return QFutureInterfaceBase._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QFutureWatcherBase::QFutureWatcherBase(QObject *parent)': the class
    is abstract, so C++ cannot make one, and the C++ class of ours does not
    fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QFutureWatcherBase.__init__' has no cute function yet. Qt's "
        "'QFutureWatcherBase::QFutureWatcherBase(QObject *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  def d_func(self) -> Optional[QFutureWatcherBasePrivate]:
    """
    Calls Qt's 'QFutureWatcherBasePrivate *QFutureWatcherBase::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#d_func

    Returns
    -------

    Optional[QFutureWatcherBasePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFutureWatcherBasePrivate *QFutureWatcherBase::d_func()
    address = self.uglySide.call('ritual_ZN18QFutureWatcherBase6d_funcEv')
    from . import QFutureWatcherBasePrivate
    return QFutureWatcherBasePrivate._cuteAt(address)

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

  def started(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::started()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#started
    """
    #  void QFutureWatcherBase::started()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase7startedEv')

  def finished(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::finished()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#finished
    """
    #  void QFutureWatcherBase::finished()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase8finishedEv')

  def canceled(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::canceled()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#canceled
    """
    #  void QFutureWatcherBase::canceled()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase8canceledEv')

  def paused(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::paused()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#paused
    """
    #  void QFutureWatcherBase::paused()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase6pausedEv')

  def suspending(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::suspending()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#suspending
    """
    #  void QFutureWatcherBase::suspending()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase10suspendingEv')

  def suspended(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::suspended()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#suspended
    """
    #  void QFutureWatcherBase::suspended()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase9suspendedEv')

  def resumed(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::resumed()'.

    Qt's own words: https://doc.qt.io/qt-6/qfuturewatcherbase.html#resumed
    """
    #  void QFutureWatcherBase::resumed()
    self.uglySide.call('ritual_ZN18QFutureWatcherBase7resumedEv')

  @overload(int)
  def resultReadyAt(self, resultIndex: int) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::resultReadyAt(int resultIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#resultReadyAt

    Parameters
    ----------

    resultIndex : int
      Passed on as it is.
    """
    #  void QFutureWatcherBase::resultReadyAt(int resultIndex)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase13resultReadyAtEi', resultIndex,
    )

  @overload(int, int)
  def resultsReadyAt(self, beginIndex: int, endIndex: int) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::resultsReadyAt(int beginIndex, int
    endIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#resultsReadyAt

    Parameters
    ----------

    beginIndex : int
      Passed on as it is.

    endIndex : int
      Passed on as it is.
    """
    #  void QFutureWatcherBase::resultsReadyAt(int beginIndex, int endIndex)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase14resultsReadyAtEii',
        beginIndex, endIndex,
    )

  @overload(int, int)
  def progressRangeChanged(self, minimum: int, maximum: int) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::progressRangeChanged(int minimum,
    int maximum)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressRangeChanged

    Parameters
    ----------

    minimum : int
      Passed on as it is.

    maximum : int
      Passed on as it is.
    """
    #  void QFutureWatcherBase::progressRangeChanged(int minimum, int
    #      maximum)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase20progressRangeChangedEii',
        minimum, maximum,
    )

  @overload(int)
  def progressValueChanged(self, progressValue: int) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::progressValueChanged(int
    progressValue)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressValueChanged

    Parameters
    ----------

    progressValue : int
      Passed on as it is.
    """
    #  void QFutureWatcherBase::progressValueChanged(int progressValue)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase20progressValueChangedEi',
        progressValue,
    )

  @overload(str)
  def progressTextChanged(self, progressText: str) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::progressTextChanged(const QString
    &progressText)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#progressTextChanged

    Parameters
    ----------

    progressText : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFutureWatcherBase::progressTextChanged(const QString
    #      &progressText)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase19progressTextChangedERK7QString',
        progressText,
    )

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
    ritual = 'ritual_ZN18QFutureWatcherBase13connectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFutureWatcherBase13connectNotifyERK11QMetaMethod')
    self.uglySide.call(ritual, self._valueOf(signal))

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
    ritual = (
        'ritual_ZN18QFutureWatcherBase16disconnectNotifyERK11QMetaMethod')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QFutureWatcherBase16disconnectNotifyERK11QMetaMet'
          'hod')
    self.uglySide.call(ritual, self._valueOf(signal))

  def connectOutputInterface(self) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::connectOutputInterface()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#connectOutputInterface
    """
    #  void QFutureWatcherBase::connectOutputInterface()
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase22connectOutputInterfaceEv',
    )

  @overload()
  @overload(bool)
  def disconnectOutputInterface(
      self,
      pendingAssignment: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QFutureWatcherBase::disconnectOutputInterface(bool
    pendingAssignment)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfuturewatcherbase.html#disconnectOutputInterface

    Parameters
    ----------

    pendingAssignment : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QFutureWatcherBase::disconnectOutputInterface(bool
    #      pendingAssignment)
    self.uglySide.call(
        'ritual_ZN18QFutureWatcherBase25disconnectOutputInterfaceEb',
        pendingAssignment,
    )
