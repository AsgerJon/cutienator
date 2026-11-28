"""
QSemaphore binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qsemaphore.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QDeadlineTimer
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeadlineTimer = WAIT['QDeadlineTimer']


class QSemaphore(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSemaphore: a plain Python object standing in front
  of one C++ QSemaphore.

  What exists
  -----------

  Every function of Qt's QSemaphore that has a ritual and that Python can
  call so far, 5 names in all: 'acquire', 'tryAcquire', 'release',
  'available', 'try_acquire'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSemaphore::~QSemaphore()': the destructor: Python never removes a
    C++ QSemaphore.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 3 a template; 2 forbidden.

  What to expect
  --------------

  - The C++ QSemaphore is created at the first use, not by 'QSemaphore(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSemaphore.
  - Each name of Qt's QSemaphore that has no cute function yet,
    'try_acquire_for', 'try_acquire_until', holds a function that raises
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
  __qt_class__ = 'QSemaphore'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def available(self) -> int:
    """
    Calls Qt's 'int QSemaphore::available() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#available
    """
    #  int QSemaphore::available() const
    return self.uglySide.call('ritual_ZNK10QSemaphore9availableEv')

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
  @overload(int)
  def __init__(self, n: int = 0) -> None:
    """
    Notes what was given, for Qt's 'QSemaphore::QSemaphore(int n)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#QSemaphore

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  QSemaphore::QSemaphore(int n)
    self._noteCreation(QSemaphore, lambda: Rituals.call(
        'ritual_ZN10QSemaphoreC1Ei', n,
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

  @overload()
  @overload(int)
  def acquire(self, n: int = 1) -> None:
    """
    Calls Qt's 'void QSemaphore::acquire(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#acquire

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QSemaphore::acquire(int n)
    self.uglySide.call('ritual_ZN10QSemaphore7acquireEi', n)

  @overload()
  @overload(int)
  def tryAcquire(self, n: int = 1) -> bool:
    """
    Calls Qt's 'bool QSemaphore::tryAcquire(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#tryAcquire

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  bool QSemaphore::tryAcquire(int n)
    return self.uglySide.call('ritual_ZN10QSemaphore10tryAcquireEi', n)

  @overload(int, int)
  def tryAcquire(self, n: int, timeout: int) -> bool:
    """
    Calls Qt's 'bool QSemaphore::tryAcquire(int n, int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#tryAcquire

    Parameters
    ----------

    n : int
      Passed on as it is.

    timeout : int
      Passed on as it is.
    """
    #  bool QSemaphore::tryAcquire(int n, int timeout)
    return self.uglySide.call(
        'ritual_ZN10QSemaphore10tryAcquireEii', n, timeout,
    )

  @overload(int, QDeadlineTimer)
  def tryAcquire(self, n: int, timeout: QDeadlineTimer) -> bool:
    """
    Calls Qt's 'bool QSemaphore::tryAcquire(int n, QDeadlineTimer timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#tryAcquire

    Parameters
    ----------

    n : int
      Passed on as it is.

    timeout : QDeadlineTimer
      Passed on as a value: Qt reads the C++ QDeadlineTimer, which stays
      Python's own.
    """
    #  bool QSemaphore::tryAcquire(int n, QDeadlineTimer timeout)
    return self.uglySide.call(
        'ritual_ZN10QSemaphore10tryAcquireEi14QDeadlineTimer',
        n, self._valueOf(timeout),
    )

  @overload()
  @overload(int)
  def release(self, n: int = 1) -> None:
    """
    Calls Qt's 'void QSemaphore::release(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#release

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QSemaphore::release(int n)
    self.uglySide.call('ritual_ZN10QSemaphore7releaseEi', n)

  def try_acquire(self) -> bool:
    """
    Calls Qt's 'bool QSemaphore::try_acquire()'.

    Qt's own words: https://doc.qt.io/qt-6/qsemaphore.html#try_acquire
    """
    #  bool QSemaphore::try_acquire()
    return self.uglySide.call('ritual_ZN10QSemaphore11try_acquireEv')

  @staticmethod
  def try_acquire_for(*__, **_) -> Never:
    """
    Qt's 'QSemaphore::try_acquire_for': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QSemaphore.try_acquire_for' has no cute function yet. Qt's "
        "'QSemaphore::try_acquire_for': a template: a pattern and no single "
        "function.")

  @staticmethod
  def try_acquire_until(*__, **_) -> Never:
    """
    Qt's 'QSemaphore::try_acquire_until': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QSemaphore.try_acquire_until' has no cute function yet. Qt's "
        "'QSemaphore::try_acquire_until': a template: a pattern and no "
        "single function.")
