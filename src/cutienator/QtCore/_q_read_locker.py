"""
QReadLocker binding of the Qt C++
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


class QReadLocker(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QReadLocker: a plain Python object standing in front
  of one C++ QReadLocker.

  What exists
  -----------

  Every function of Qt's QReadLocker that has a ritual and that Python can
  call so far, 3 names in all: 'unlock', 'relock', 'readWriteLock'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QReadLocker::~QReadLocker()': the destructor: Python never removes
    a C++ QReadLocker.

  What has no ritual
  ------------------

  2 of the 7 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QReadLocker is created at the first use, not by
    'QReadLocker(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QReadLocker.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QReadLocker'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def readWriteLock(self) -> Optional[QReadWriteLock]:
    """
    Calls Qt's 'QReadWriteLock *QReadLocker::readWriteLock() const'.

    Qt's own words: https://doc.qt.io/qt-6/qreadlocker.html#readWriteLock

    Returns
    -------

    Optional[QReadWriteLock]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QReadWriteLock *QReadLocker::readWriteLock() const
    address = self.uglySide.call('ritual_ZNK11QReadLocker13readWriteLockEv')
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
    Notes what was given, for Qt's 'QReadLocker::QReadLocker(QReadWriteLock
    *readWriteLock)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qreadlocker.html#QReadLocker

    Parameters
    ----------

    readWriteLock : Optional[QReadWriteLock]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QReadLocker::QReadLocker(QReadWriteLock *readWriteLock)
    self._noteCreation(QReadLocker, lambda: Rituals.call(
        'ritual_ZN11QReadLockerC1EP14QReadWriteLock',
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
    Calls Qt's 'void QReadLocker::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qreadlocker.html#unlock
    """
    #  void QReadLocker::unlock()
    self.uglySide.call('ritual_ZN11QReadLocker6unlockEv')

  def relock(self) -> None:
    """
    Calls Qt's 'void QReadLocker::relock()'.

    Qt's own words: https://doc.qt.io/qt-6/qreadlocker.html#relock
    """
    #  void QReadLocker::relock()
    self.uglySide.call('ritual_ZN11QReadLocker6relockEv')
