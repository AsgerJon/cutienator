"""
QBasicReadWriteLock binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDeadlineTimer, QReadWriteLockPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']
  QReadWriteLockPrivate = WAIT['QReadWriteLockPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBasicReadWriteLock(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBasicReadWriteLock: a plain Python object standing
  in front of one C++ QBasicReadWriteLock.

  What exists
  -----------

  Every function of Qt's QBasicReadWriteLock that has a ritual and that
  Python can call so far, 13 names in all: 'lockForRead', 'tryLockForRead',
  'lockForWrite', 'tryLockForWrite', 'unlock', 'lock', 'lock_shared',
  'try_lock', 'try_lock_shared', 'unlock_shared', 'tryLockForReadInternal',
  'tryLockForWriteInternal', 'describeLockForTSan'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool QBasicReadWriteLock::contendedTryLockForRead(QDeadlineTimer
    timeout, void *dd)': names 'void', which has no cute class yet.
  - Qt's 'bool QBasicReadWriteLock::contendedTryLockForWrite(QDeadlineTimer
    timeout, void *dd)': names 'void', which has no cute class yet.
  - Qt's 'void QBasicReadWriteLock::contendedUnlock(void *dd)': names 'void',
    which has no cute class yet.
  - Qt's 'quintptr QBasicReadWriteLock::describeLockInternal(void *dd)':
    names 'void', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 takes or gives a type that cannot be
  passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QBasicReadWriteLock is created at the first use, not by
    'QBasicReadWriteLock(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBasicReadWriteLock.
  - Each name of Qt's QBasicReadWriteLock that has no cute function yet,
    'contendedTryLockForRead', 'contendedTryLockForWrite', 'contendedUnlock',
    'describeLockInternal', 'fastTryLockForRead', 'fastTryLockForWrite',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QReadWriteLockPrivate)
  @overload(NoneType)
  @overload(QReadWriteLockPrivate, int)
  @overload(NoneType, int)
  def describeLockForTSan(
      d: Optional[QReadWriteLockPrivate],
      flags: int = 0,
  ) -> int:
    """
    Calls Qt's 'uint
    QBasicReadWriteLock::describeLockForTSan(QReadWriteLockPrivate *d, uint
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#describeLockForTSan

    Parameters
    ----------

    d : Optional[QReadWriteLockPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    flags : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  uint QBasicReadWriteLock::describeLockForTSan(QReadWriteLockPrivate
    #      *d, uint flags)
    return Rituals.call(
        'ritual_ZN19QBasicReadWriteLock19describeLockForTSanEP21QReadWriteL'
        'ockPrivatej',
        CuteMixin._addressOf(d), flags,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBasicReadWriteLock'

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
    'QBasicReadWriteLock::QBasicReadWriteLock()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#QBasicReadWriteLock
    """
    #  QBasicReadWriteLock::QBasicReadWriteLock()
    self._noteCreation(QBasicReadWriteLock, lambda: Rituals.call(
        'ritual_ZN19QBasicReadWriteLockC1Ev',
    ))

  @overload(QReadWriteLockPrivate)
  @overload(NoneType)
  def __init__(self, d: Optional[QReadWriteLockPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QBasicReadWriteLock::QBasicReadWriteLock(QReadWriteLockPrivate *d)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#QBasicReadWriteLock

    Parameters
    ----------

    d : Optional[QReadWriteLockPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QBasicReadWriteLock::QBasicReadWriteLock(QReadWriteLockPrivate *d)
    self._noteCreation(QBasicReadWriteLock, lambda: Rituals.call(
        'ritual_ZN19QBasicReadWriteLockC1EP21QReadWriteLockPrivate',
        self._addressOf(d),
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

  def lockForRead(self) -> None:
    """
    Calls Qt's 'void QBasicReadWriteLock::lockForRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#lockForRead
    """
    #  void QBasicReadWriteLock::lockForRead()
    self.uglySide.call('ritual_ZN19QBasicReadWriteLock11lockForReadEv')

  @overload()
  def tryLockForRead(self) -> bool:
    """
    Calls Qt's 'bool QBasicReadWriteLock::tryLockForRead()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#tryLockForRead
    """
    #  bool QBasicReadWriteLock::tryLockForRead()
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock14tryLockForReadEv',
    )

  @overload(QDeadlineTimer)
  def tryLockForRead(self, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QBasicReadWriteLock::tryLockForRead(QDeadlineTimer
    timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#tryLockForRead

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QBasicReadWriteLock::tryLockForRead(QDeadlineTimer timeout)
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock14tryLockForReadE14QDeadlineTimer',
        self._valueOf(timeout),
    )

  def lockForWrite(self) -> None:
    """
    Calls Qt's 'void QBasicReadWriteLock::lockForWrite()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#lockForWrite
    """
    #  void QBasicReadWriteLock::lockForWrite()
    self.uglySide.call('ritual_ZN19QBasicReadWriteLock12lockForWriteEv')

  @overload()
  def tryLockForWrite(self) -> bool:
    """
    Calls Qt's 'bool QBasicReadWriteLock::tryLockForWrite()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#tryLockForWrite
    """
    #  bool QBasicReadWriteLock::tryLockForWrite()
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock15tryLockForWriteEv',
    )

  @overload(QDeadlineTimer)
  def tryLockForWrite(self, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QBasicReadWriteLock::tryLockForWrite(QDeadlineTimer
    timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#tryLockForWrite

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QBasicReadWriteLock::tryLockForWrite(QDeadlineTimer timeout)
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock15tryLockForWriteE14QDeadlineTimer',
        self._valueOf(timeout),
    )

  def unlock(self) -> None:
    """
    Calls Qt's 'void QBasicReadWriteLock::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicreadwritelock.html#unlock
    """
    #  void QBasicReadWriteLock::unlock()
    self.uglySide.call('ritual_ZN19QBasicReadWriteLock6unlockEv')

  def lock(self) -> None:
    """
    Calls Qt's 'void QBasicReadWriteLock::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicreadwritelock.html#lock
    """
    #  void QBasicReadWriteLock::lock()
    self.uglySide.call('ritual_ZN19QBasicReadWriteLock4lockEv')

  def lock_shared(self) -> None:
    """
    Calls Qt's 'void QBasicReadWriteLock::lock_shared()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#lock_shared
    """
    #  void QBasicReadWriteLock::lock_shared()
    self.uglySide.call('ritual_ZN19QBasicReadWriteLock11lock_sharedEv')

  def try_lock(self) -> bool:
    """
    Calls Qt's 'bool QBasicReadWriteLock::try_lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicreadwritelock.html#try_lock
    """
    #  bool QBasicReadWriteLock::try_lock()
    return self.uglySide.call('ritual_ZN19QBasicReadWriteLock8try_lockEv')

  def try_lock_shared(self) -> bool:
    """
    Calls Qt's 'bool QBasicReadWriteLock::try_lock_shared()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#try_lock_shared
    """
    #  bool QBasicReadWriteLock::try_lock_shared()
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock15try_lock_sharedEv',
    )

  def unlock_shared(self) -> None:
    """
    Calls Qt's 'void QBasicReadWriteLock::unlock_shared()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#unlock_shared
    """
    #  void QBasicReadWriteLock::unlock_shared()
    self.uglySide.call('ritual_ZN19QBasicReadWriteLock13unlock_sharedEv')

  @overload(QDeadlineTimer, int)
  def tryLockForReadInternal(
      self,
      timeout: QDeadlineTimer,
      tsanFlags: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QBasicReadWriteLock::tryLockForReadInternal(QDeadlineTimer timeout,
    unsigned int tsanFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#tryLockForReadInternal

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.

    tsanFlags : int
      Passed on as it is.
    """
    #  bool QBasicReadWriteLock::tryLockForReadInternal(QDeadlineTimer
    #      timeout, unsigned int tsanFlags)
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock22tryLockForReadInternalE14QDeadline'
        'Timerj',
        self._valueOf(timeout), tsanFlags,
    )

  @overload(QDeadlineTimer, int)
  def tryLockForWriteInternal(
      self,
      timeout: QDeadlineTimer,
      tsanFlags: int,
  ) -> bool:
    """
    Calls Qt's 'bool
    QBasicReadWriteLock::tryLockForWriteInternal(QDeadlineTimer timeout,
    unsigned int tsanFlags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicreadwritelock.html#tryLockForWriteInternal

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.

    tsanFlags : int
      Passed on as it is.
    """
    #  bool QBasicReadWriteLock::tryLockForWriteInternal(QDeadlineTimer
    #      timeout, unsigned int tsanFlags)
    return self.uglySide.call(
        'ritual_ZN19QBasicReadWriteLock23tryLockForWriteInternalE14QDeadlin'
        'eTimerj',
        self._valueOf(timeout), tsanFlags,
    )

  @staticmethod
  def contendedTryLockForRead(*__, **_) -> Never:
    """
    Qt's 'bool QBasicReadWriteLock::contendedTryLockForRead(QDeadlineTimer
    timeout, void *dd)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBasicReadWriteLock.contendedTryLockForRead' has no cute function "
        "yet. Qt's 'bool "
        "QBasicReadWriteLock::contendedTryLockForRead(QDeadlineTimer "
        "timeout, void *dd)': names 'void', which has no cute class yet.")

  @staticmethod
  def contendedTryLockForWrite(*__, **_) -> Never:
    """
    Qt's 'bool QBasicReadWriteLock::contendedTryLockForWrite(QDeadlineTimer
    timeout, void *dd)': names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBasicReadWriteLock.contendedTryLockForWrite' has no cute "
        "function yet. Qt's 'bool "
        "QBasicReadWriteLock::contendedTryLockForWrite(QDeadlineTimer "
        "timeout, void *dd)': names 'void', which has no cute class yet.")

  @staticmethod
  def contendedUnlock(*__, **_) -> Never:
    """
    Qt's 'void QBasicReadWriteLock::contendedUnlock(void *dd)': names 'void',
    which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBasicReadWriteLock.contendedUnlock' has no cute function yet. "
        "Qt's 'void QBasicReadWriteLock::contendedUnlock(void *dd)': names "
        "'void', which has no cute class yet.")

  @staticmethod
  def describeLockInternal(*__, **_) -> Never:
    """
    Qt's 'quintptr QBasicReadWriteLock::describeLockInternal(void *dd)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QBasicReadWriteLock.describeLockInternal' has no cute function "
        "yet. Qt's 'quintptr QBasicReadWriteLock::describeLockInternal(void "
        "*dd)': names 'void', which has no cute class yet.")

  @staticmethod
  def fastTryLockForRead(*__, **_) -> Never:
    """
    Qt's 'bool QBasicReadWriteLock::fastTryLockForRead(QReadWriteLockPrivate
    *&d)': takes or gives a type that cannot be passed yet:
    QReadWriteLockPrivate *&.
    """
    raise NotImplementedError(
        "'QBasicReadWriteLock.fastTryLockForRead' has no cute function yet. "
        "Qt's 'bool "
        "QBasicReadWriteLock::fastTryLockForRead(QReadWriteLockPrivate "
        "*&d)': takes or gives a type that cannot be passed yet: "
        "QReadWriteLockPrivate *&.")

  @staticmethod
  def fastTryLockForWrite(*__, **_) -> Never:
    """
    Qt's 'bool QBasicReadWriteLock::fastTryLockForWrite(QReadWriteLockPrivate
    *&d)': takes or gives a type that cannot be passed yet:
    QReadWriteLockPrivate *&.
    """
    raise NotImplementedError(
        "'QBasicReadWriteLock.fastTryLockForWrite' has no cute function "
        "yet. Qt's 'bool "
        "QBasicReadWriteLock::fastTryLockForWrite(QReadWriteLockPrivate "
        "*&d)': takes or gives a type that cannot be passed yet: "
        "QReadWriteLockPrivate *&.")
