"""
QFileDevice binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfiledevice.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QFileDeviceFileError, QFileDeviceFileHandleFlag
from . import QFileDeviceFileTime, QFileDeviceMemoryMapFlag
from . import QFileDevicePermission, QIODevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDateTime, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDateTime = WAIT['QDateTime']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QFileDevice(QIODevice):
  """
  The cute side of Qt's QFileDevice: a plain Python object standing in front
  of one C++ QFileDevice.

  It is built on the cute 'QIODevice', as Qt's QFileDevice is built on Qt's
  QIODevice, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QFileDevice that has a ritual and that Python can
  call so far, 18 names in all: 'metaObject', 'tr', 'error', 'unsetError',
  'close', 'isSequential', 'handle', 'fileName', 'pos', 'seek', 'atEnd',
  'flush', 'size', 'resize', 'permissions', 'setPermissions', 'fileTime',
  'setFileTime'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileDevice::~QFileDevice()': the destructor: Python never removes
    a C++ QFileDevice.
  - Qt's 'bool QFileDevice::unmap(uchar *address)': takes a number to change
    where it is.

  What has no ritual
  ------------------

  15 of the 35 functions Qt declares: 6 protected; 3 takes or gives a type
  that cannot be passed yet; 3 private; 2 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QFileDevice is created at the first use, not by
    'QFileDevice(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QFileDevice.
  - Qt tells when it has removed the C++ QFileDevice. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QFileDevice, and the names Qt has for the
  #  combinations of its flags enums.
  FileError = QFileDeviceFileError
  FileHandleFlag = QFileDeviceFileHandleFlag
  FileHandleFlags = QFileDeviceFileHandleFlag
  FileTime = QFileDeviceFileTime
  MemoryMapFlag = QFileDeviceMemoryMapFlag
  MemoryMapFlags = QFileDeviceMemoryMapFlag
  Permission = QFileDevicePermission
  Permissions = QFileDevicePermission

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString QFileDevice::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDevice::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QFileDevice2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileDevice'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QFileDevice::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QFileDevice::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QFileDevice10metaObjectEv')
    from . import QMetaObject
    return QMetaObject._cuteAt(address)

  def error(self) -> FileError:
    """
    Calls Qt's 'FileError QFileDevice::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#error

    Returns
    -------

    FileError
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FileError(number)' gives.
    """
    #  FileError QFileDevice::error() const
    return QFileDevice.FileError(self.uglySide.call(
        'ritual_ZNK11QFileDevice5errorEv',
    ))

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QFileDevice::isSequential() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#isSequential
    """
    #  bool QFileDevice::isSequential() const
    return self.uglySide.call('ritual_ZNK11QFileDevice12isSequentialEv')

  def handle(self) -> int:
    """
    Calls Qt's 'int QFileDevice::handle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#handle
    """
    #  int QFileDevice::handle() const
    return self.uglySide.call('ritual_ZNK11QFileDevice6handleEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QFileDevice::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileDevice::fileName() const
    return self.uglySide.call('ritual_ZNK11QFileDevice8fileNameEv')

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QFileDevice::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#pos
    """
    #  qint64 QFileDevice::pos() const
    return self.uglySide.call('ritual_ZNK11QFileDevice3posEv')

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QFileDevice::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#atEnd
    """
    #  bool QFileDevice::atEnd() const
    return self.uglySide.call('ritual_ZNK11QFileDevice5atEndEv')

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QFileDevice::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#size
    """
    #  qint64 QFileDevice::size() const
    return self.uglySide.call('ritual_ZNK11QFileDevice4sizeEv')

  def permissions(self) -> Permissions:
    """
    Calls Qt's 'Permissions QFileDevice::permissions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#permissions

    Returns
    -------

    Permissions
      The value standing for the combination Qt gave back.
    """
    #  Permissions QFileDevice::permissions() const
    return QFileDevice.Permissions(self.uglySide.call(
        'ritual_ZNK11QFileDevice11permissionsEv',
    ))

  @overload(FileTime)
  def fileTime(self, time: FileTime) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileDevice::fileTime(QFileDevice::FileTime time)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#fileTime

    Parameters
    ----------

    time : FileTime
      Passed on as its number.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileDevice::fileTime(QFileDevice::FileTime time) const
    address = self.uglySide.call(
        'ritual_ZNK11QFileDevice8fileTimeENS_8FileTimeE', time.value,
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Permissions)
  def setPermissions(self, permissionSpec: Permissions) -> bool:
    """
    Calls Qt's 'bool QFileDevice::setPermissions(Permissions
    permissionSpec)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#setPermissions

    Parameters
    ----------

    permissionSpec : Permissions
      Passed on as its number.
    """
    #  bool QFileDevice::setPermissions(Permissions permissionSpec)
    return self.uglySide.call(
        'ritual_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE',
        permissionSpec.value,
    )

  @overload(QDateTime, FileTime)
  def setFileTime(self, newDate: QDateTime, fileTime: FileTime) -> bool:
    """
    Calls Qt's 'bool QFileDevice::setFileTime(const QDateTime &newDate,
    QFileDevice::FileTime fileTime)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#setFileTime

    Parameters
    ----------

    newDate : QDateTime
      Passed on as a value: Qt reads the C++ QDateTime, which stays Python's
      own.

    fileTime : FileTime
      Passed on as its number.
    """
    #  bool QFileDevice::setFileTime(const QDateTime &newDate,
    #      QFileDevice::FileTime fileTime)
    return self.uglySide.call(
        'ritual_ZN11QFileDevice11setFileTimeERK9QDateTimeNS_8FileTimeE',
        self._valueOf(newDate), fileTime.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  def unsetError(self) -> None:
    """
    Calls Qt's 'void QFileDevice::unsetError()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#unsetError
    """
    #  void QFileDevice::unsetError()
    self.uglySide.call('ritual_ZN11QFileDevice10unsetErrorEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QFileDevice::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#close
    """
    #  void QFileDevice::close()
    self.uglySide.call('ritual_ZN11QFileDevice5closeEv')

  @overload(int)
  def seek(self, offset: int) -> bool:
    """
    Calls Qt's 'bool QFileDevice::seek(qint64 offset)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#seek

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  bool QFileDevice::seek(qint64 offset)
    return self.uglySide.call('ritual_ZN11QFileDevice4seekEx', offset)

  def flush(self) -> bool:
    """
    Calls Qt's 'bool QFileDevice::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#flush
    """
    #  bool QFileDevice::flush()
    return self.uglySide.call('ritual_ZN11QFileDevice5flushEv')

  @overload(int)
  def resize(self, sz: int) -> bool:
    """
    Calls Qt's 'bool QFileDevice::resize(qint64 sz)'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#resize

    Parameters
    ----------

    sz : int
      Passed on as it is.
    """
    #  bool QFileDevice::resize(qint64 sz)
    return self.uglySide.call('ritual_ZN11QFileDevice6resizeEx', sz)
