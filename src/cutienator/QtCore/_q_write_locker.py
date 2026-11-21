"""
QWriteLocker binding of the Qt C++
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
  from typing import Optional

  from . import QReadWriteLock
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QReadWriteLock = WAIT['QReadWriteLock']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWriteLocker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWriteLocker: a plain Python object standing in front
  of one C++ QWriteLocker.

  What exists
  -----------

  Every function of Qt's QWriteLocker that has a ritual and that Python can
  call so far, 3 names in all: 'unlock', 'relock', 'readWriteLock'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWriteLocker::~QWriteLocker()': the destructor: Python never
    removes a C++ QWriteLocker.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QWriteLocker is created at the first use, not by
    'QWriteLocker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWriteLocker.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWriteLocker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def readWriteLock(self) -> Optional[QReadWriteLock]:
    """
    Calls Qt's 'QReadWriteLock *QWriteLocker::readWriteLock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwritelocker.html#readWriteLock

    Returns
    -------

    Optional[QReadWriteLock]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QReadWriteLock *QWriteLocker::readWriteLock() const
    address = self.uglySide.call('ritual_ZNK12QWriteLocker13readWriteLockEv')
    from . import QReadWriteLock
    return QReadWriteLock._cuteAt(address)

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

  @overload(QReadWriteLock)
  @overload(NoneType)
  def __init__(self, readWriteLock: Optional[QReadWriteLock]) -> None:
    """
    Notes what was given, for Qt's 'QWriteLocker::QWriteLocker(QReadWriteLock
    *readWriteLock)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qwritelocker.html#QWriteLocker

    Parameters
    ----------

    readWriteLock : Optional[QReadWriteLock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWriteLocker::QWriteLocker(QReadWriteLock *readWriteLock)
    self._noteCreation(QWriteLocker, lambda: Rituals.call(
        'ritual_ZN12QWriteLockerC1EP14QReadWriteLock',
        self._addressOf(readWriteLock),
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

  def unlock(self) -> None:
    """
    Calls Qt's 'void QWriteLocker::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qwritelocker.html#unlock
    """
    #  void QWriteLocker::unlock()
    self.uglySide.call('ritual_ZN12QWriteLocker6unlockEv')

  def relock(self) -> None:
    """
    Calls Qt's 'void QWriteLocker::relock()'.

    Qt's own words: https://doc.qt.io/qt-6/qwritelocker.html#relock
    """
    #  void QWriteLocker::relock()
    self.uglySide.call('ritual_ZN12QWriteLocker6relockEv')
