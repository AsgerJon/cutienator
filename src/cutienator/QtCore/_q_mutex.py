"""
QMutex binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtCore/qmutex.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QBasicMutex

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']


class QMutex(QBasicMutex):
  """
  The cute side of Qt's QMutex: a plain Python object standing in front of
  one C++ QMutex.

  It is built on the cute 'QBasicMutex', as Qt's QMutex is built on Qt's
  QBasicMutex, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMutex that has a ritual and that Python can call so
  far, 2 names in all: 'try_lock', 'tryLock'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMutex::~QMutex()': the destructor: Python never removes a C++
    QMutex.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 a template.

  What to expect
  --------------

  - The C++ QMutex is created at the first use, not by 'QMutex(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMutex.
  - Each name of Qt's QMutex that has no cute function yet, 'try_lock_for',
    'try_lock_until', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMutex'

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
    Notes what was given, for Qt's 'QMutex::QMutex()', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qmutex.html#QMutex
    """
    #  QMutex::QMutex()
    self._noteCreation(QMutex, lambda: Rituals.call('ritual_ZN6QMutexC1Ev'))

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

  def try_lock(self) -> bool:
    """
    Calls Qt's 'bool QMutex::try_lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qmutex.html#try_lock
    """
    #  bool QMutex::try_lock()
    return self.uglySide.call('ritual_ZN6QMutex8try_lockEv')

  @overload(int)
  def tryLock(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QMutex::tryLock(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutex.html#tryLock

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QMutex::tryLock(int timeout)
    return self.uglySide.call('ritual_ZN6QMutex7tryLockEi', timeout)

  @overload(QDeadlineTimer)
  def tryLock(self, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QMutex::tryLock(QDeadlineTimer timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qmutex.html#tryLock

    Parameters
    ----------

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QMutex::tryLock(QDeadlineTimer timeout)
    return self.uglySide.call(
        'ritual_ZN6QMutex7tryLockE14QDeadlineTimer', self._valueOf(timeout),
    )

  @staticmethod
  def try_lock_for(*__, **_) -> Never:
    """
    Qt's 'QMutex::try_lock_for': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QMutex.try_lock_for' has no cute function yet. Qt's "
        "'QMutex::try_lock_for': a template: a pattern and no single "
        "function.")

  @staticmethod
  def try_lock_until(*__, **_) -> Never:
    """
    Qt's 'QMutex::try_lock_until': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QMutex.try_lock_until' has no cute function yet. Qt's "
        "'QMutex::try_lock_until': a template: a pattern and no single "
        "function.")
