"""
QLockFile binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlockfile.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QLockFilePrivate


class QLockFile(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QLockFile: a plain Python object standing in front of
  one C++ QLockFile.

  What exists
  -----------

  Every function of Qt's QLockFile that has a ritual and that Python can call
  so far, 10 names in all: 'fileName', 'lock', 'tryLock', 'unlock',
  'setStaleLockTime', 'staleLockTime', 'isLocked', 'removeStaleLockFile',
  'error', 'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QLockFile::~QLockFile()': the destructor: Python never removes a
    C++ QLockFile.
  - Qt's 'bool QLockFile::tryLock(std::chrono::milliseconds timeout)': takes
    a type Python has no way to hand over yet.
  - Qt's 'void QLockFile::setStaleLockTime(std::chrono::milliseconds value)':
    takes a type Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds QLockFile::staleLockTimeAsDuration()
    const': gives a type Python has no way to take yet.
  - Qt's 'bool QLockFile::getLockInfo(qint64 *pid, QString *hostname, QString
    *appname) const': takes a number to change where it is.
  - Qt's 'const QLockFilePrivate *QLockFile::d_func() const': takes in Python
    what 'QLockFilePrivate *QLockFile::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QLockFile is created at the first use, not by 'QLockFile(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QLockFile.
  - Each name of Qt's QLockFile that has no cute function yet, 'getLockInfo',
    'staleLockTimeAsDuration', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QLockFile, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class LockError(CuteNum):
    """
    The enum 'QLockFile::LockError' of Qt, with the 4 names Qt gives in it.
    """

    NoError = Kee[int](0)
    LockFailedError = Kee[int](1)
    PermissionError = Kee[int](2)
    UnknownError = Kee[int](3)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QLockFile'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QLockFile::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QLockFile::fileName() const
    return self.uglySide.call('ritual_ZNK9QLockFile8fileNameEv')

  def staleLockTime(self) -> int:
    """
    Calls Qt's 'int QLockFile::staleLockTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#staleLockTime
    """
    #  int QLockFile::staleLockTime() const
    return self.uglySide.call('ritual_ZNK9QLockFile13staleLockTimeEv')

  def isLocked(self) -> bool:
    """
    Calls Qt's 'bool QLockFile::isLocked() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#isLocked
    """
    #  bool QLockFile::isLocked() const
    return self.uglySide.call('ritual_ZNK9QLockFile8isLockedEv')

  def error(self) -> LockError:
    """
    Calls Qt's 'LockError QLockFile::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#error

    Returns
    -------

    LockError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'LockError(number)' gives.
    """
    #  LockError QLockFile::error() const
    return QLockFile.LockError(self.uglySide.call(
        'ritual_ZNK9QLockFile5errorEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setStaleLockTime(self, a0: int) -> None:
    """
    Calls Qt's 'void QLockFile::setStaleLockTime(int a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#setStaleLockTime

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QLockFile::setStaleLockTime(int a0)
    self.uglySide.call('ritual_ZN9QLockFile16setStaleLockTimeEi', a0)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def __init__(self, fileName: str) -> None:
    """
    Notes what was given, for Qt's 'QLockFile::QLockFile(const QString
    &fileName)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#QLockFile

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QLockFile::QLockFile(const QString &fileName)
    self._noteCreation(QLockFile, lambda: Rituals.call(
        'ritual_ZN9QLockFileC1ERK7QString', fileName,
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

  def lock(self) -> bool:
    """
    Calls Qt's 'bool QLockFile::lock()'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#lock
    """
    #  bool QLockFile::lock()
    return self.uglySide.call('ritual_ZN9QLockFile4lockEv')

  @overload(int)
  def tryLock(self, timeout: int) -> bool:
    """
    Calls Qt's 'bool QLockFile::tryLock(int timeout)'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#tryLock

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  bool QLockFile::tryLock(int timeout)
    return self.uglySide.call('ritual_ZN9QLockFile7tryLockEi', timeout)

  def unlock(self) -> None:
    """
    Calls Qt's 'void QLockFile::unlock()'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#unlock
    """
    #  void QLockFile::unlock()
    self.uglySide.call('ritual_ZN9QLockFile6unlockEv')

  def removeStaleLockFile(self) -> bool:
    """
    Calls Qt's 'bool QLockFile::removeStaleLockFile()'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#removeStaleLockFile
    """
    #  bool QLockFile::removeStaleLockFile()
    return self.uglySide.call('ritual_ZN9QLockFile19removeStaleLockFileEv')

  def d_func(self) -> Optional[QLockFilePrivate]:
    """
    Calls Qt's 'QLockFilePrivate *QLockFile::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qlockfile.html#d_func

    Returns
    -------

    Optional[QLockFilePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QLockFilePrivate *QLockFile::d_func()
    address = self.uglySide.call('ritual_ZN9QLockFile6d_funcEv')
    from . import QLockFilePrivate
    return QLockFilePrivate._cuteAt(address)

  @staticmethod
  def getLockInfo(*__, **_) -> Never:
    """
    Qt's 'bool QLockFile::getLockInfo(qint64 *pid, QString *hostname, QString
    *appname) const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QLockFile.getLockInfo' has no cute function yet. Qt's 'bool "
        "QLockFile::getLockInfo(qint64 *pid, QString *hostname, QString "
        "*appname) const': takes a number to change where it is.")

  @staticmethod
  def staleLockTimeAsDuration(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QLockFile::staleLockTimeAsDuration()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QLockFile.staleLockTimeAsDuration' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QLockFile::staleLockTimeAsDuration() "
        "const': gives a type Python has no way to take yet.")
