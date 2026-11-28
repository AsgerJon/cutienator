"""
QFileSystemMetaData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qfilesystemmetadata_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QFileSystemMetaData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute
from ..occult import Rituals
from . import QAbstractFileEngine, QFileDevice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QDateTime


class QFileSystemMetaData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFileSystemMetaData: a plain Python object standing
  in front of one C++ QFileSystemMetaData.

  C++ hands a QFileSystemMetaData around as a copy, so every C++
  QFileSystemMetaData behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFileSystemMetaData that has a ritual and that
  Python can call so far, 28 names in all: 'hasFlags', 'missingFlags',
  'clear', 'clearFlags', 'exists', 'isLink', 'isFile', 'isDirectory',
  'isBundle', 'isAlias', 'isLegacyLink', 'isSequential', 'isHidden',
  'wasDeleted', 'isLnkFile', 'isJunction', 'size', 'setPermissions',
  'accessTime', 'birthTime', 'metadataChangeTime', 'modificationTime',
  'userId', 'groupId', 'ownerId', 'isReadable', 'isWritable', 'isExecutable'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFile::Permissions QFileSystemMetaData::permissions() const': gives
    a type Python has no way to take yet.
  - Qt's 'QDateTime QFileSystemMetaData::fileTime(QFile::FileTime time)
    const': takes a type Python has no way to hand over yet.
  - Qt's 'void QFileSystemMetaData::fillFromDirEnt(const struct dirent
    &statBuffer)': takes a type Python has no way to hand over yet.
  - Qt's 'QFileSystemMetaData::~QFileSystemMetaData()': the destructor:
    Python removes its C++ QFileSystemMetaData by it, and has no other use
    for it.

  What has no ritual
  ------------------

  2 of the 35 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied; 1 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QFileSystemMetaData is created at the first use, not by
    'QFileSystemMetaData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFileSystemMetaData back gives a copy the ritual made
    for Python, in a new cute QFileSystemMetaData.
  - Each name of Qt's QFileSystemMetaData that has no cute function yet,
    'fileTime', 'fillFromDirEnt', 'fillFromStatBuf', 'fillFromStatxBuf',
    'permissions', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QFileSystemMetaData, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class MetaDataFlag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QFileSystemMetaData::MetaDataFlag' of Qt, with the 46
    names Qt gives in it. Qt names the type of its combinations
    'QFileSystemMetaData::MetaDataFlags'.
    """

    OtherReadPermission = 0x4
    OtherWritePermission = 0x2
    OtherExecutePermission = 0x1
    GroupReadPermission = 0x40
    GroupWritePermission = 0x20
    GroupExecutePermission = 0x10
    UserReadPermission = 0x400
    UserWritePermission = 0x200
    UserExecutePermission = 0x100
    OwnerReadPermission = 0x4000
    OwnerWritePermission = 0x2000
    OwnerExecutePermission = 0x1000
    OtherPermissions = 0x7
    GroupPermissions = 0x70
    UserPermissions = 0x700
    OwnerPermissions = 0x7000
    ReadPermissions = 0x4444
    WritePermissions = 0x2222
    ExecutePermissions = 0x1111
    Permissions = 0x7777
    LinkType = 0x10000
    FileType = 0x20000
    DirectoryType = 0x40000
    BundleType = 0x0
    AliasType = 0x0
    JunctionType = 0x0
    WinLnkType = 0x0
    SequentialType = 0x800000
    LegacyLinkType = 0x10000
    Type = 0x870000
    HiddenAttribute = 0x100000
    SizeAttribute = 0x200000
    ExistsAttribute = 0x400000
    WasDeletedAttribute = 0x40000000
    Attributes = 0x40700000
    AccessTime = 0x2000000
    BirthTime = 0x2000000
    MetadataChangeTime = 0x2000000
    ModificationTime = 0x2000000
    Times = 0x2000000
    UserId = 0x10000000
    GroupId = 0x20000000
    CaseSensitive = 0x80000000
    OwnerIds = 0x30000000
    PosixStatFlags = 0x72a67077
    AllMetaDataFlags = 0xffffffff

  MetaDataFlags = MetaDataFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileSystemMetaData'

  #  Qt's '~QFileSystemMetaData()'. Naming it makes this a value class:
  #  Python owns every C++ QFileSystemMetaData behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QFileSystemMetaDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(MetaDataFlags)
  def hasFlags(self, flags: MetaDataFlags) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::hasFlags(MetaDataFlags flags)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#hasFlags

    Parameters
    ----------

    flags : MetaDataFlags
      Passed on as its number.
    """
    #  bool QFileSystemMetaData::hasFlags(MetaDataFlags flags) const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData8hasFlagsE6QFlagsINS_12MetaDataFlag'
        'EE',
        flags.value,
    )

  def exists(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::exists() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#exists
    """
    #  bool QFileSystemMetaData::exists() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData6existsEv')

  def isLink(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#isLink
    """
    #  bool QFileSystemMetaData::isLink() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData6isLinkEv')

  def isFile(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#isFile
    """
    #  bool QFileSystemMetaData::isFile() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData6isFileEv')

  def isDirectory(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isDirectory() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isDirectory
    """
    #  bool QFileSystemMetaData::isDirectory() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData11isDirectoryEv',
    )

  def isBundle(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isBundle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#isBundle
    """
    #  bool QFileSystemMetaData::isBundle() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData8isBundleEv')

  def isAlias(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#isAlias
    """
    #  bool QFileSystemMetaData::isAlias() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData7isAliasEv')

  def isLegacyLink(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isLegacyLink() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isLegacyLink
    """
    #  bool QFileSystemMetaData::isLegacyLink() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData12isLegacyLinkEv',
    )

  def isSequential(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isSequential() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isSequential
    """
    #  bool QFileSystemMetaData::isSequential() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData12isSequentialEv',
    )

  def isHidden(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#isHidden
    """
    #  bool QFileSystemMetaData::isHidden() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData8isHiddenEv')

  def wasDeleted(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::wasDeleted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#wasDeleted
    """
    #  bool QFileSystemMetaData::wasDeleted() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData10wasDeletedEv',
    )

  def isLnkFile(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isLnkFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#isLnkFile
    """
    #  bool QFileSystemMetaData::isLnkFile() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData9isLnkFileEv')

  def isJunction(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isJunction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isJunction
    """
    #  bool QFileSystemMetaData::isJunction() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData10isJunctionEv',
    )

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QFileSystemMetaData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#size
    """
    #  qint64 QFileSystemMetaData::size() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData4sizeEv')

  def accessTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileSystemMetaData::accessTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#accessTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileSystemMetaData::accessTime() const
    address = self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData10accessTimeEv',
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def birthTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileSystemMetaData::birthTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#birthTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileSystemMetaData::birthTime() const
    address = self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData9birthTimeEv',
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def metadataChangeTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileSystemMetaData::metadataChangeTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#metadataChangeTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileSystemMetaData::metadataChangeTime() const
    address = self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData18metadataChangeTimeEv',
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def modificationTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileSystemMetaData::modificationTime() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#modificationTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileSystemMetaData::modificationTime() const
    address = self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData16modificationTimeEv',
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def userId(self) -> int:
    """
    Calls Qt's 'uint QFileSystemMetaData::userId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#userId
    """
    #  uint QFileSystemMetaData::userId() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData6userIdEv')

  def groupId(self) -> int:
    """
    Calls Qt's 'uint QFileSystemMetaData::groupId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#groupId
    """
    #  uint QFileSystemMetaData::groupId() const
    return self.uglySide.call('ritual_ZNK19QFileSystemMetaData7groupIdEv')

  @overload(QAbstractFileEngine.FileOwner)
  def ownerId(self, owner: QAbstractFileEngine.FileOwner) -> int:
    """
    Calls Qt's 'uint
    QFileSystemMetaData::ownerId(QAbstractFileEngine::FileOwner owner)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#ownerId

    Parameters
    ----------

    owner : QAbstractFileEngine.FileOwner
      Passed on as its number.
    """
    #  uint QFileSystemMetaData::ownerId(QAbstractFileEngine::FileOwner
    #      owner) const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData7ownerIdEN19QAbstractFileEngine9Fil'
        'eOwnerE',
        owner.value,
    )

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isReadable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isReadable
    """
    #  bool QFileSystemMetaData::isReadable() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData10isReadableEv',
    )

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isWritable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isWritable
    """
    #  bool QFileSystemMetaData::isWritable() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData10isWritableEv',
    )

  def isExecutable(self) -> bool:
    """
    Calls Qt's 'bool QFileSystemMetaData::isExecutable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#isExecutable
    """
    #  bool QFileSystemMetaData::isExecutable() const
    return self.uglySide.call(
        'ritual_ZNK19QFileSystemMetaData12isExecutableEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QFileDevice.Permissions)
  def setPermissions(self, permissions: QFileDevice.Permissions) -> None:
    """
    Calls Qt's 'void QFileSystemMetaData::setPermissions(QFile::Permissions
    permissions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#setPermissions

    Parameters
    ----------

    permissions : QFileDevice.Permissions
      Passed on as its number.
    """
    #  void QFileSystemMetaData::setPermissions(QFile::Permissions
    #      permissions)
    self.uglySide.call(
        'ritual_ZN19QFileSystemMetaData14setPermissionsE6QFlagsIN11QFileDev'
        'ice10PermissionEE',
        permissions.value,
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QFileSystemMetaData::QFileSystemMetaData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#QFileSystemMetaData
    """
    #  QFileSystemMetaData::QFileSystemMetaData()
    self._noteCreation(QFileSystemMetaData, lambda: Rituals.call(
        'ritual_ZN19QFileSystemMetaDataC1Ev',
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

  @overload(MetaDataFlags)
  def missingFlags(self, flags: MetaDataFlags) -> MetaDataFlags:
    """
    Calls Qt's 'MetaDataFlags QFileSystemMetaData::missingFlags(MetaDataFlags
    flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#missingFlags

    Parameters
    ----------

    flags : MetaDataFlags
      Passed on as its number.

    Returns
    -------

    MetaDataFlags
      The value standing for the combination Qt gave back.
    """
    #  MetaDataFlags QFileSystemMetaData::missingFlags(MetaDataFlags flags)
    return QFileSystemMetaData.MetaDataFlags(self.uglySide.call(
        'ritual_ZN19QFileSystemMetaData12missingFlagsE6QFlagsINS_12MetaData'
        'FlagEE',
        flags.value,
    ))

  def clear(self) -> None:
    """
    Calls Qt's 'void QFileSystemMetaData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qfilesystemmetadata.html#clear
    """
    #  void QFileSystemMetaData::clear()
    self.uglySide.call('ritual_ZN19QFileSystemMetaData5clearEv')

  @overload()
  @overload(MetaDataFlags)
  def clearFlags(
      self,
      flags: MetaDataFlags = MetaDataFlags.AllMetaDataFlags,
  ) -> None:
    """
    Calls Qt's 'void QFileSystemMetaData::clearFlags(MetaDataFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qfilesystemmetadata.html#clearFlags

    Parameters
    ----------

    flags : MetaDataFlags
      Passed on as its number. May be left out, as in Qt: it is then
      MetaDataFlags.AllMetaDataFlags.
    """
    #  void QFileSystemMetaData::clearFlags(MetaDataFlags flags)
    self.uglySide.call(
        'ritual_ZN19QFileSystemMetaData10clearFlagsE6QFlagsINS_12MetaDataFl'
        'agEE',
        flags.value,
    )

  @staticmethod
  def fileTime(*__, **_) -> Never:
    """
    Qt's 'QDateTime QFileSystemMetaData::fileTime(QFile::FileTime time)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileSystemMetaData.fileTime' has no cute function yet. Qt's "
        "'QDateTime QFileSystemMetaData::fileTime(QFile::FileTime time) "
        "const': takes a type Python has no way to hand over yet.")

  @staticmethod
  def fillFromDirEnt(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemMetaData::fillFromDirEnt(const struct dirent
    &statBuffer)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QFileSystemMetaData.fillFromDirEnt' has no cute function yet. "
        "Qt's 'void QFileSystemMetaData::fillFromDirEnt(const struct dirent "
        "&statBuffer)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def fillFromStatBuf(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemMetaData::fillFromStatBuf(const struct stat
    &statBuffer)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'GetFileTimes'.
    """
    raise NotImplementedError(
        "'QFileSystemMetaData.fillFromStatBuf' has no cute function yet. "
        "Qt's 'void QFileSystemMetaData::fillFromStatBuf(const struct stat "
        "&statBuffer)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'GetFileTimes'.")

  @staticmethod
  def fillFromStatxBuf(*__, **_) -> Never:
    """
    Qt's 'void QFileSystemMetaData::fillFromStatxBuf(const struct statx
    &statBuffer)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QFileSystemMetaData.fillFromStatxBuf' has no cute function yet. "
        "Qt's 'void QFileSystemMetaData::fillFromStatxBuf(const struct "
        "statx &statBuffer)': cannot be called and cannot be called through "
        "the meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def permissions(*__, **_) -> Never:
    """
    Qt's 'QFile::Permissions QFileSystemMetaData::permissions() const': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QFileSystemMetaData.permissions' has no cute function yet. Qt's "
        "'QFile::Permissions QFileSystemMetaData::permissions() const': "
        "gives a type Python has no way to take yet.")
