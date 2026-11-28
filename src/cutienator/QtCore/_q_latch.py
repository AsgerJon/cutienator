"""
QLatch binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qlatch_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QLatch to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class QLatch(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLatch: a plain Python object standing in front of
  one C++ QLatch.

  What exists
  -----------

  Every function of Qt's QLatch that has a ritual and that Python can call so
  far, 11 names in all: 'pending', 'countDown', 'tryWait', 'wait',
  'arriveAndWait', 'max', 'count_down', 'try_wait', 'arrive_and_wait',
  'waitInternal', 'wakeUp'. It can be made from Python, in 1 way; see
  '__init__'.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QLatch is created at the first use, not by 'QLatch(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLatch.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def max() -> int:
    """
    Calls Qt's 'int QLatch::max()'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#max
    """
    #  int QLatch::max()
    return Rituals.call('ritual_ZN6QLatch3maxEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLatch'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def pending(self) -> int:
    """
    Calls Qt's 'int QLatch::pending() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#pending
    """
    #  int QLatch::pending() const
    return self.uglySide.call('ritual_ZNK6QLatch7pendingEv')

  def tryWait(self) -> bool:
    """
    Calls Qt's 'bool QLatch::tryWait() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#tryWait
    """
    #  bool QLatch::tryWait() const
    return self.uglySide.call('ritual_ZNK6QLatch7tryWaitEv')

  def try_wait(self) -> bool:
    """
    Calls Qt's 'bool QLatch::try_wait() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#try_wait
    """
    #  bool QLatch::try_wait() const
    return self.uglySide.call('ritual_ZNK6QLatch8try_waitEv')

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

  @overload(int)
  def __init__(self, expected: int) -> None:
    """
    Notes what was given, for Qt's 'QLatch::QLatch(int expected)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#QLatch

    Parameters
    ----------

    expected : int
      Passed on as it is.
    """
    #  QLatch::QLatch(int expected)
    self._noteCreation(QLatch, lambda: Rituals.call(
        'ritual_ZN6QLatchC1Ei', expected,
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
  def countDown(self, n: int = 1) -> None:
    """
    Calls Qt's 'void QLatch::countDown(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#countDown

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLatch::countDown(int n)
    self.uglySide.call('ritual_ZN6QLatch9countDownEi', n)

  def wait(self) -> None:
    """
    Calls Qt's 'void QLatch::wait()'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#wait
    """
    #  void QLatch::wait()
    self.uglySide.call('ritual_ZN6QLatch4waitEv')

  @overload()
  @overload(int)
  def arriveAndWait(self, n: int = 1) -> None:
    """
    Calls Qt's 'void QLatch::arriveAndWait(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#arriveAndWait

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLatch::arriveAndWait(int n)
    self.uglySide.call('ritual_ZN6QLatch13arriveAndWaitEi', n)

  @overload()
  @overload(int)
  def count_down(self, n: int = 1) -> None:
    """
    Calls Qt's 'void QLatch::count_down(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#count_down

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLatch::count_down(int n)
    self.uglySide.call('ritual_ZN6QLatch10count_downEi', n)

  @overload()
  @overload(int)
  def arrive_and_wait(self, n: int = 1) -> None:
    """
    Calls Qt's 'void QLatch::arrive_and_wait(int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#arrive_and_wait

    Parameters
    ----------

    n : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  void QLatch::arrive_and_wait(int n)
    self.uglySide.call('ritual_ZN6QLatch15arrive_and_waitEi', n)

  @overload(int)
  def waitInternal(self, current: int) -> None:
    """
    Calls Qt's 'void QLatch::waitInternal(int current)'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#waitInternal

    Parameters
    ----------

    current : int
      Passed on as it is.
    """
    #  void QLatch::waitInternal(int current)
    self.uglySide.call('ritual_ZN6QLatch12waitInternalEi', current)

  def wakeUp(self) -> None:
    """
    Calls Qt's 'void QLatch::wakeUp()'.

    Qt's own words: https://doc.qt.io/qt-6/qlatch.html#wakeUp
    """
    #  void QLatch::wakeUp()
    self.uglySide.call('ritual_ZN6QLatch6wakeUpEv')
