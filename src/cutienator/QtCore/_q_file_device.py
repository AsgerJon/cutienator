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
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from . import QIODevice

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

  #  The enums Qt writes inside QFileDevice, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class FileError(CuteNum):
    """
    The enum 'QFileDevice::FileError' of Qt, with the 15 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    ReadError = Kee[int](1)
    WriteError = Kee[int](2)
    FatalError = Kee[int](3)
    ResourceError = Kee[int](4)
    OpenError = Kee[int](5)
    AbortError = Kee[int](6)
    TimeOutError = Kee[int](7)
    UnspecifiedError = Kee[int](8)
    RemoveError = Kee[int](9)
    RenameError = Kee[int](10)
    PositionError = Kee[int](11)
    ResizeError = Kee[int](12)
    PermissionsError = Kee[int](13)
    CopyError = Kee[int](14)

  class FileHandleFlag(CuteFlags):
    """
    The flags enum 'QFileDevice::FileHandleFlag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QFileDevice::FileHandleFlags'.
    """

    AutoCloseHandle = 0x1
    DontCloseHandle = 0x0

  FileHandleFlags = FileHandleFlag

  class FileTime(CuteNum):
    """
    The enum 'QFileDevice::FileTime' of Qt, with the 4 names Qt gives in it.
    """

    FileAccessTime = Kee[int](0)
    FileBirthTime = Kee[int](1)
    FileMetadataChangeTime = Kee[int](2)
    FileModificationTime = Kee[int](3)

  class MemoryMapFlag(CuteFlags):
    """
    The flags enum 'QFileDevice::MemoryMapFlag' of Qt, with the 2 names Qt
    gives in it. Qt names the type of its combinations
    'QFileDevice::MemoryMapFlags'.
    """

    NoOptions = 0x0
    MapPrivateOption = 0x1

  MemoryMapFlags = MemoryMapFlag

  class Permission(CuteFlags):
    """
    The flags enum 'QFileDevice::Permission' of Qt, with the 12 names Qt
    gives in it. Qt names the type of its combinations
    'QFileDevice::Permissions'.
    """

    ReadOwner = 0x4000
    WriteOwner = 0x2000
    ExeOwner = 0x1000
    ReadUser = 0x400
    WriteUser = 0x200
    ExeUser = 0x100
    ReadGroup = 0x40
    WriteGroup = 0x20
    ExeGroup = 0x10
    ReadOther = 0x4
    WriteOther = 0x2
    ExeOther = 0x1

  Permissions = Permission

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

  #  A C++ QFileDevice Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QFileDevice'

  #  The functions Qt calls itself that QFileDevice is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'fileName': (
          ('_ZNK11QFileDevice8fileNameEv',
           ('address', 'text', ''),
           ()),
      ),
      'resize': (
          ('_ZN11QFileDevice6resizeEx',
           ('bool', 'number', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'permissions': (
          ('_ZNK11QFileDevice11permissionsEv',
           ('int', 'flags', 'QtCore:QFileDevice.Permission'),
           ()),
      ),
      'setPermissions': (
          ('_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE',
           ('bool', 'number', ''),
           (
               ('int', 'flags', 'QtCore:QFileDevice.Permission'),
           )),
      ),
  }

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
    ritual = 'ritual_ZNK11QFileDevice12isSequentialEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFileDevice12isSequentialEv'
    return self.uglySide.call(ritual)

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
    ritual = 'ritual_ZNK11QFileDevice8fileNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFileDevice8fileNameEv'
    return self.uglySide.call(ritual)

  def pos(self) -> int:
    """
    Calls Qt's 'qint64 QFileDevice::pos() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#pos
    """
    #  qint64 QFileDevice::pos() const
    ritual = 'ritual_ZNK11QFileDevice3posEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFileDevice3posEv'
    return self.uglySide.call(ritual)

  def atEnd(self) -> bool:
    """
    Calls Qt's 'bool QFileDevice::atEnd() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#atEnd
    """
    #  bool QFileDevice::atEnd() const
    ritual = 'ritual_ZNK11QFileDevice5atEndEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFileDevice5atEndEv'
    return self.uglySide.call(ritual)

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QFileDevice::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfiledevice.html#size
    """
    #  qint64 QFileDevice::size() const
    ritual = 'ritual_ZNK11QFileDevice4sizeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFileDevice4sizeEv'
    return self.uglySide.call(ritual)

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
    ritual = 'ritual_ZNK11QFileDevice11permissionsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QFileDevice11permissionsEv'
    return QFileDevice.Permissions(self.uglySide.call(ritual))

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
    ritual = (
        'ritual_ZN11QFileDevice14setPermissionsE6QFlagsINS_10PermissionEE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN11QFileDevice14setPermissionsE6QFlagsINS_10Permissi'
          'onEE')
    return self.uglySide.call(ritual, permissionSpec.value)

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
    ritual = 'ritual_ZN11QFileDevice5closeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFileDevice5closeEv'
    self.uglySide.call(ritual)

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
    ritual = 'ritual_ZN11QFileDevice4seekEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFileDevice4seekEx'
    return self.uglySide.call(ritual, offset)

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
    ritual = 'ritual_ZN11QFileDevice6resizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN11QFileDevice6resizeEx'
    return self.uglySide.call(ritual, sz)
