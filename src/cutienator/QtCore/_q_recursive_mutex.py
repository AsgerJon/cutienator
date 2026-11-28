"""
QRecursiveMutex binding of the Qt C++
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
  from typing import Never, Optional

  from . import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']


class QRecursiveMutex(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QRecursiveMutex: a plain Python object standing in
  front of one C++ QRecursiveMutex.

  What exists
  -----------

  Every function of Qt's QRecursiveMutex that has a ritual and that Python
  can call so far, 4 names in all: 'lock', 'tryLock', 'unlock', 'try_lock'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QRecursiveMutex::~QRecursiveMutex()': the destructor: Python never
    removes a C++ QRecursiveMutex.

  What has no ritual
  ------------------

  6 of the 13 functions Qt declares: 4 forbidden; 2 a template.

  What to expect
  --------------

  - The C++ QRecursiveMutex is created at the first use, not by
    'QRecursiveMutex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QRecursiveMutex.
  - Each name of Qt's QRecursiveMutex that has no cute function yet,
    'try_lock_for', 'try_lock_until', holds a function that raises
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
  __qt_class__ = 'QRecursiveMutex'

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
    Notes what was given, for Qt's 'QRecursiveMutex::QRecursiveMutex()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qrecursivemutex.html#QRecursiveMutex
    """
    #  QRecursiveMutex::QRecursiveMutex()
    self._noteCreation(QRecursiveMutex, lambda: Rituals.call(
        'ritual_ZN15QRecursiveMutexC1Ev',
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
    Calls Qt's 'void QRecursiveMutex::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qrecursivemutex.html#lock
    """
    #  void QRecursiveMutex::lock()
    self.uglySide.call('ritual_ZN15QRecursiveMutex4lockEv')

  @overload(int)
  def tryLock(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QRecursiveMutex::tryLock(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qrecursivemutex.html#tryLock

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QRecursiveMutex::tryLock(int timeout)
    return self.uglySide.call(
        'ritual_ZN15QRecursiveMutex7tryLockEi', timeout,
    )

  @overload()
  @overload(QDeadlineTimer)
  def tryLock(self, timer: Optional[QDeadlineTimer] = None) -> bool:
    """
    Calls Qt's 'bool QRecursiveMutex::tryLock(QDeadlineTimer timer)'.

    Qt's own words: https://doc.qt.io/qt-6/qrecursivemutex.html#tryLock

    Parameters
    ----------

    timer : Optional[QDeadlineTimer]
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own. May be left out, as in Qt: a new 'QDeadlineTimer()' is
      then passed on.
    """
    #  bool QRecursiveMutex::tryLock(QDeadlineTimer timer)
    if timer is None:
      from . import QDeadlineTimer
      timer = QDeadlineTimer()
    return self.uglySide.call(
        'ritual_ZN15QRecursiveMutex7tryLockE14QDeadlineTimer',
        self._valueOf(timer),
    )

  def unlock(self) -> None:
    """
    Calls Qt's 'void QRecursiveMutex::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qrecursivemutex.html#unlock
    """
    #  void QRecursiveMutex::unlock()
    self.uglySide.call('ritual_ZN15QRecursiveMutex6unlockEv')

  def try_lock(self) -> bool:
    """
    Calls Qt's 'bool QRecursiveMutex::try_lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qrecursivemutex.html#try_lock
    """
    #  bool QRecursiveMutex::try_lock()
    return self.uglySide.call('ritual_ZN15QRecursiveMutex8try_lockEv')

  @staticmethod
  def try_lock_for(*__, **_) -> Never:
    """
    Qt's 'QRecursiveMutex::try_lock_for': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QRecursiveMutex.try_lock_for' has no cute function yet. Qt's "
        "'QRecursiveMutex::try_lock_for': a template: a pattern and no "
        "single function.")

  @staticmethod
  def try_lock_until(*__, **_) -> Never:
    """
    Qt's 'QRecursiveMutex::try_lock_until': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QRecursiveMutex.try_lock_until' has no cute function yet. Qt's "
        "'QRecursiveMutex::try_lock_until': a template: a pattern and no "
        "single function.")
