"""
QBasicMutex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qmutex.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']


class QBasicMutex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QBasicMutex: a plain Python object standing in front
  of one C++ QBasicMutex.

  What exists
  -----------

  Every function of Qt's QBasicMutex that has a ritual and that Python can
  call so far, 7 names in all: 'lock', 'unlock', 'tryLock', 'try_lock',
  'fastTryLock', 'lockInternal', 'unlockInternal'. It can be made from
  Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  8 of the 18 functions Qt declares: 4 forbidden; 4 takes or gives a type
  that cannot be passed yet.

  What to expect
  --------------

  - The C++ QBasicMutex is created at the first use, not by
    'QBasicMutex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBasicMutex.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBasicMutex'

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
    Notes what was given, for Qt's 'QBasicMutex::QBasicMutex()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#QBasicMutex
    """
    #  QBasicMutex::QBasicMutex()
    self._noteCreation(QBasicMutex, lambda: Rituals.call(
        'ritual_ZN11QBasicMutexC1Ev',
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

  def lock(self) -> None:
    """
    Calls Qt's 'void QBasicMutex::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#lock
    """
    #  void QBasicMutex::lock()
    self.uglySide.call('ritual_ZN11QBasicMutex4lockEv')

  def unlock(self) -> None:
    """
    Calls Qt's 'void QBasicMutex::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#unlock
    """
    #  void QBasicMutex::unlock()
    self.uglySide.call('ritual_ZN11QBasicMutex6unlockEv')

  def tryLock(self) -> bool:
    """
    Calls Qt's 'bool QBasicMutex::tryLock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#tryLock
    """
    #  bool QBasicMutex::tryLock()
    return self.uglySide.call('ritual_ZN11QBasicMutex7tryLockEv')

  def try_lock(self) -> bool:
    """
    Calls Qt's 'bool QBasicMutex::try_lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#try_lock
    """
    #  bool QBasicMutex::try_lock()
    return self.uglySide.call('ritual_ZN11QBasicMutex8try_lockEv')

  def fastTryLock(self) -> bool:
    """
    Calls Qt's 'bool QBasicMutex::fastTryLock()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#fastTryLock
    """
    #  bool QBasicMutex::fastTryLock()
    return self.uglySide.call('ritual_ZN11QBasicMutex11fastTryLockEv')

  @overload()
  def lockInternal(self) -> None:
    """
    Calls Qt's 'void QBasicMutex::lockInternal()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#lockInternal
    """
    #  void QBasicMutex::lockInternal()
    self.uglySide.call('ritual_ZN11QBasicMutex12lockInternalEv')

  @overload(QDeadlineTimer)
  def lockInternal(self, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QBasicMutex::lockInternal(QDeadlineTimer timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#lockInternal

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QBasicMutex::lockInternal(QDeadlineTimer timeout)
    return self.uglySide.call(
        'ritual_ZN11QBasicMutex12lockInternalE14QDeadlineTimer',
        self._valueOf(timeout),
    )

  @overload(int)
  def lockInternal(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QBasicMutex::lockInternal(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#lockInternal

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QBasicMutex::lockInternal(int timeout)
    return self.uglySide.call(
        'ritual_ZN11QBasicMutex12lockInternalEi', timeout,
    )

  def unlockInternal(self) -> None:
    """
    Calls Qt's 'void QBasicMutex::unlockInternal()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicmutex.html#unlockInternal
    """
    #  void QBasicMutex::unlockInternal()
    self.uglySide.call('ritual_ZN11QBasicMutex14unlockInternalEv')
