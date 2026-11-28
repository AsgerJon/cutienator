"""
QtConcurrent::ThreadEngineBarrier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtConcurrent/qtconcurrentthreadengine.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals


class ThreadEngineBarrier(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtConcurrent::ThreadEngineBarrier: a plain Python
  object standing in front of one C++ QtConcurrent::ThreadEngineBarrier.

  What exists
  -----------

  Every function of Qt's QtConcurrent::ThreadEngineBarrier that has a ritual
  and that Python can call so far, 5 names in all: 'acquire', 'release',
  'wait', 'currentCount', 'releaseUnlessLast'. It can be made from Python, in
  1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QtConcurrent::ThreadEngineBarrier is created at the first use,
    not by 'QtConcurrent::ThreadEngineBarrier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QtConcurrent::ThreadEngineBarrier.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtConcurrent::ThreadEngineBarrier'

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
    'QtConcurrent::ThreadEngineBarrier::ThreadEngineBarrier()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebarrier.html
    """
    #  QtConcurrent::ThreadEngineBarrier::ThreadEngineBarrier()
    self._noteCreation(ThreadEngineBarrier, lambda: Rituals.call(
        'ritual_ZN12QtConcurrent19ThreadEngineBarrierC1Ev',
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

  def acquire(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBarrier::acquire()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebarrier.html#acquire
    """
    #  void QtConcurrent::ThreadEngineBarrier::acquire()
    self.uglySide.call(
        'ritual_ZN12QtConcurrent19ThreadEngineBarrier7acquireEv',
    )

  def release(self) -> int:
    """
    Calls Qt's 'int QtConcurrent::ThreadEngineBarrier::release()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebarrier.html#release
    """
    #  int QtConcurrent::ThreadEngineBarrier::release()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent19ThreadEngineBarrier7releaseEv',
    )

  def wait(self) -> None:
    """
    Calls Qt's 'void QtConcurrent::ThreadEngineBarrier::wait()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebarrier.html#wait
    """
    #  void QtConcurrent::ThreadEngineBarrier::wait()
    self.uglySide.call('ritual_ZN12QtConcurrent19ThreadEngineBarrier4waitEv')

  def currentCount(self) -> int:
    """
    Calls Qt's 'int QtConcurrent::ThreadEngineBarrier::currentCount()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebarrier.html#currentCount
    """
    #  int QtConcurrent::ThreadEngineBarrier::currentCount()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent19ThreadEngineBarrier12currentCountEv',
    )

  def releaseUnlessLast(self) -> bool:
    """
    Calls Qt's 'bool QtConcurrent::ThreadEngineBarrier::releaseUnlessLast()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtconcurrent-threadenginebarrier.html
    """
    #  bool QtConcurrent::ThreadEngineBarrier::releaseUnlessLast()
    return self.uglySide.call(
        'ritual_ZN12QtConcurrent19ThreadEngineBarrier17releaseUnlessLastEv',
    )
