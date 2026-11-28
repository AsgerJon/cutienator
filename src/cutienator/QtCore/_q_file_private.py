"""
QFilePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfile_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QFilePrivate to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QFileDevice, QFileDevicePrivate, QIODeviceBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QAbstractFileEngine, QFile


class QFilePrivate(QFileDevicePrivate):
  """
  The cute side of Qt's QFilePrivate: a plain Python object standing in front
  of one C++ QFilePrivate.

  It is built on the cute 'QFileDevicePrivate', as Qt's QFilePrivate is built
  on Qt's QFileDevicePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFilePrivate that has a ritual and that Python can
  call so far, 3 names in all: 'q_func', 'openExternalFile', 'engine'. None
  can be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QFile *QFilePrivate::q_func() const': takes in Python what
    'QFile *QFilePrivate::q_func()' takes.
  - Qt's 'QFilePrivate::~QFilePrivate()': the destructor: Python never
    removes a C++ QFilePrivate.
  - Qt's 'bool QFilePrivate::openExternalFile(QIODevice::OpenMode flags, FILE
    *fh, QFile::FileHandleFlags handleFlags)': names 'FILE', which has no
    cute class yet.
  - Qt's 'void QFilePrivate::writeToDebugStream(QDebug &a0) const': takes a
    type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 9 functions Qt declares: 2 leans on 'QFileDevicePrivate.

  What to expect
  --------------

  - The C++ QFilePrivate is created at the first use, not by
    'QFilePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFilePrivate.
  - Each name of Qt's QFilePrivate that has no cute function yet, '__init__',
    'copy', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFilePrivate'

  #  A C++ QFilePrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFilePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def engine(self) -> Optional[QAbstractFileEngine]:
    """
    Calls Qt's 'QAbstractFileEngine *QFilePrivate::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileprivate.html#engine

    Returns
    -------

    Optional[QAbstractFileEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAbstractFileEngine *QFilePrivate::engine() const
    ritual = 'ritual_ZNK12QFilePrivate6engineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QFilePrivate6engineEv'
    address = self.uglySide.call(ritual)
    from . import QAbstractFileEngine
    return QAbstractFileEngine._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QFilePrivate::QFilePrivate()': leans on
    'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QFilePrivate.__init__' has no cute function yet. Qt's "
        "'QFilePrivate::QFilePrivate()': leans on "
        "'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[QFile]:
    """
    Calls Qt's 'QFile *QFilePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileprivate.html#q_func

    Returns
    -------

    Optional[QFile]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QFile *QFilePrivate::q_func()
    address = self.uglySide.call('ritual_ZN12QFilePrivate6q_funcEv')
    from . import QFile
    return QFile._cuteAt(address)

  @overload(QIODeviceBase.OpenMode, int, QFileDevice.FileHandleFlags)
  def openExternalFile(
      self,
      flags: QIODeviceBase.OpenMode,
      fd: int,
      handleFlags: QFileDevice.FileHandleFlags,
  ) -> bool:
    """
    Calls Qt's 'bool QFilePrivate::openExternalFile(QIODevice::OpenMode
    flags, int fd, QFile::FileHandleFlags handleFlags)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileprivate.html#openExternalFile

    Parameters
    ----------

    flags : QIODeviceBase.OpenMode
      Passed on as its number.

    fd : int
      Passed on as it is.

    handleFlags : QFileDevice.FileHandleFlags
      Passed on as its number.
    """
    #  bool QFilePrivate::openExternalFile(QIODevice::OpenMode flags, int fd,
    #      QFile::FileHandleFlags handleFlags)
    return self.uglySide.call(
        'ritual_ZN12QFilePrivate16openExternalFileE6QFlagsIN13QIODeviceBase'
        '12OpenModeFlagEEiS0_IN11QFileDevice14FileHandleFlagEE',
        flags.value, fd, handleFlags.value,
    )

  @staticmethod
  def copy(*__, **_) -> Never:
    """
    Qt's 'bool QFilePrivate::copy(const QString &newName,
    QFileDevice::Permissions permissions)': leans on
    'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QFilePrivate.copy' has no cute function yet. Qt's 'bool "
        "QFilePrivate::copy(const QString &newName, "
        "QFileDevice::Permissions permissions)': leans on "
        "'QFileDevicePrivate::setError(QFileDevice::FileError, QString)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
