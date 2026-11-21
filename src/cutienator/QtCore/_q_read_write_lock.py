"""
QReadWriteLock binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteNum
from ..occult import Rituals
from . import QBasicReadWriteLock


class QReadWriteLock(QBasicReadWriteLock):
  """
  The cute side of Qt's QReadWriteLock: a plain Python object standing in
  front of one C++ QReadWriteLock.

  It is built on the cute 'QBasicReadWriteLock', as Qt's QReadWriteLock is
  built on Qt's QBasicReadWriteLock, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QReadWriteLock that has a ritual and that Python can
  call so far, 2 names in all: 'tryLockForRead', 'tryLockForWrite'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QReadWriteLock::~QReadWriteLock()': the destructor: Python never
    removes a C++ QReadWriteLock.

  What has no ritual
  ------------------

  4 of the 8 functions Qt declares: 4 private.

  What to expect
  --------------

  - The C++ QReadWriteLock is created at the first use, not by
    'QReadWriteLock(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QReadWriteLock.
  """

  #  The enums Qt writes inside QReadWriteLock, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class RecursionMode(CuteNum):
    """
    The enum 'QReadWriteLock::RecursionMode' of Qt, with the 2 names Qt gives
    in it.
    """

    NonRecursive = Kee[int](0)
    Recursive = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QReadWriteLock'

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
  @overload(RecursionMode)
  def __init__(
      self,
      recursionMode: RecursionMode = RecursionMode.NonRecursive,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QReadWriteLock::QReadWriteLock(RecursionMode recursionMode)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qreadwritelock.html#QReadWriteLock

    Parameters
    ----------

    recursionMode : RecursionMode
      Passed on as its number. May be left out, as in Qt: it is then
      RecursionMode.NonRecursive.
    """
    #  QReadWriteLock::QReadWriteLock(RecursionMode recursionMode)
    self._noteCreation(QReadWriteLock, lambda: Rituals.call(
        'ritual_ZN14QReadWriteLockC1ENS_13RecursionModeE',
        recursionMode.value,
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

  @overload(int)
  def tryLockForRead(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QReadWriteLock::tryLockForRead(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qreadwritelock.html#tryLockForRead

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QReadWriteLock::tryLockForRead(int timeout)
    return self.uglySide.call(
        'ritual_ZN14QReadWriteLock14tryLockForReadEi', timeout,
    )

  @overload(int)
  def tryLockForWrite(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QReadWriteLock::tryLockForWrite(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qreadwritelock.html#tryLockForWrite

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QReadWriteLock::tryLockForWrite(int timeout)
    return self.uglySide.call(
        'ritual_ZN14QReadWriteLock15tryLockForWriteEi', timeout,
    )
