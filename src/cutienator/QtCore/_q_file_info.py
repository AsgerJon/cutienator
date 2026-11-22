"""
QFileInfo binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qfileinfo.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QFileDevice, QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from . import QDateTime, QDir, QTimeZone
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDir = WAIT['QDir']
  QTimeZone = WAIT['QTimeZone']


class QFileInfo(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QFileInfo: a plain Python object standing in front of
  one C++ QFileInfo.

  C++ hands a QFileInfo around as a copy, so every C++ QFileInfo behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QFileInfo that has a ritual and that Python can call
  so far, 53 names in all: 'setFile', 'exists', 'refresh', 'filePath',
  'absoluteFilePath', 'canonicalFilePath', 'fileName', 'baseName',
  'completeBaseName', 'suffix', 'bundleName', 'completeSuffix', 'path',
  'absolutePath', 'canonicalPath', 'dir', 'absoluteDir', 'isReadable',
  'isWritable', 'isExecutable', 'isHidden', 'isNativePath', 'isRelative',
  'isAbsolute', 'makeAbsolute', 'isFile', 'isDir', 'isSymLink',
  'isSymbolicLink', 'isOther', 'isShortcut', 'isAlias', 'isJunction',
  'isRoot', 'isBundle', 'symLinkTarget', 'readSymLink', 'junctionTarget',
  'owner', 'ownerId', 'group', 'groupId', 'permission', 'size', 'birthTime',
  'metadataChangeTime', 'lastModified', 'lastRead', 'caching', 'setCaching',
  'stat', '__eq__', '__ne__'. It can be made from Python, in 4 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QFileInfo::~QFileInfo()': the destructor: Python removes its C++
    QFileInfo by it, and has no other use for it.

  What has no ritual
  ------------------

  24 of the 88 functions Qt declares: 19 takes or gives a type that cannot be
  passed yet; 3 a template; 2 private.

  What to expect
  --------------

  - The C++ QFileInfo is created at the first use, not by 'QFileInfo(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QFileInfo back gives a copy the ritual made for
    Python, in a new cute QFileInfo.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QFileInfo'

  #  Qt's '~QFileInfo()'. Naming it makes this a value class: Python owns
  #  every C++ QFileInfo behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN9QFileInfoD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def exists(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::exists() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#exists
    """
    #  bool QFileInfo::exists() const
    return self.uglySide.call('ritual_ZNK9QFileInfo6existsEv')

  @staticmethod
  @overload(str)
  def exists(file: str) -> bool:
    """
    Calls Qt's 'bool QFileInfo::exists(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#exists

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QFileInfo::exists(const QString &file)
    return Rituals.call('ritual_ZN9QFileInfo6existsERK7QString', file)

  def filePath(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::filePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#filePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::filePath() const
    return self.uglySide.call('ritual_ZNK9QFileInfo8filePathEv')

  def absoluteFilePath(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::absoluteFilePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#absoluteFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::absoluteFilePath() const
    return self.uglySide.call('ritual_ZNK9QFileInfo16absoluteFilePathEv')

  def canonicalFilePath(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::canonicalFilePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#canonicalFilePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::canonicalFilePath() const
    return self.uglySide.call('ritual_ZNK9QFileInfo17canonicalFilePathEv')

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::fileName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::fileName() const
    return self.uglySide.call('ritual_ZNK9QFileInfo8fileNameEv')

  def baseName(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::baseName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#baseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::baseName() const
    return self.uglySide.call('ritual_ZNK9QFileInfo8baseNameEv')

  def completeBaseName(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::completeBaseName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#completeBaseName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::completeBaseName() const
    return self.uglySide.call('ritual_ZNK9QFileInfo16completeBaseNameEv')

  def suffix(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::suffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#suffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::suffix() const
    return self.uglySide.call('ritual_ZNK9QFileInfo6suffixEv')

  def bundleName(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::bundleName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#bundleName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::bundleName() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10bundleNameEv')

  def completeSuffix(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::completeSuffix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#completeSuffix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::completeSuffix() const
    return self.uglySide.call('ritual_ZNK9QFileInfo14completeSuffixEv')

  def path(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::path() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#path

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::path() const
    return self.uglySide.call('ritual_ZNK9QFileInfo4pathEv')

  def absolutePath(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::absolutePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#absolutePath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::absolutePath() const
    return self.uglySide.call('ritual_ZNK9QFileInfo12absolutePathEv')

  def canonicalPath(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::canonicalPath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#canonicalPath

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::canonicalPath() const
    return self.uglySide.call('ritual_ZNK9QFileInfo13canonicalPathEv')

  def dir(self) -> QDir:
    """
    Calls Qt's 'QDir QFileInfo::dir() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#dir

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QFileInfo::dir() const
    address = self.uglySide.call('ritual_ZNK9QFileInfo3dirEv')
    from . import QDir
    return QDir._cuteOwning(address)

  def absoluteDir(self) -> QDir:
    """
    Calls Qt's 'QDir QFileInfo::absoluteDir() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#absoluteDir

    Returns
    -------

    QDir
      A new cute QDir around the copy Qt gave back. Python owns it.
    """
    #  QDir QFileInfo::absoluteDir() const
    address = self.uglySide.call('ritual_ZNK9QFileInfo11absoluteDirEv')
    from . import QDir
    return QDir._cuteOwning(address)

  def isReadable(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isReadable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isReadable
    """
    #  bool QFileInfo::isReadable() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10isReadableEv')

  def isWritable(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isWritable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isWritable
    """
    #  bool QFileInfo::isWritable() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10isWritableEv')

  def isExecutable(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isExecutable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isExecutable
    """
    #  bool QFileInfo::isExecutable() const
    return self.uglySide.call('ritual_ZNK9QFileInfo12isExecutableEv')

  def isHidden(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isHidden() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isHidden
    """
    #  bool QFileInfo::isHidden() const
    return self.uglySide.call('ritual_ZNK9QFileInfo8isHiddenEv')

  def isNativePath(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isNativePath() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isNativePath
    """
    #  bool QFileInfo::isNativePath() const
    return self.uglySide.call('ritual_ZNK9QFileInfo12isNativePathEv')

  def isRelative(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isRelative() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isRelative
    """
    #  bool QFileInfo::isRelative() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10isRelativeEv')

  def isAbsolute(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isAbsolute() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isAbsolute
    """
    #  bool QFileInfo::isAbsolute() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10isAbsoluteEv')

  def isFile(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isFile
    """
    #  bool QFileInfo::isFile() const
    return self.uglySide.call('ritual_ZNK9QFileInfo6isFileEv')

  def isDir(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isDir() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isDir
    """
    #  bool QFileInfo::isDir() const
    return self.uglySide.call('ritual_ZNK9QFileInfo5isDirEv')

  def isSymLink(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isSymLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isSymLink
    """
    #  bool QFileInfo::isSymLink() const
    return self.uglySide.call('ritual_ZNK9QFileInfo9isSymLinkEv')

  def isSymbolicLink(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isSymbolicLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isSymbolicLink
    """
    #  bool QFileInfo::isSymbolicLink() const
    return self.uglySide.call('ritual_ZNK9QFileInfo14isSymbolicLinkEv')

  def isOther(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isOther() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isOther
    """
    #  bool QFileInfo::isOther() const
    return self.uglySide.call('ritual_ZNK9QFileInfo7isOtherEv')

  def isShortcut(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isShortcut() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isShortcut
    """
    #  bool QFileInfo::isShortcut() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10isShortcutEv')

  def isAlias(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isAlias() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isAlias
    """
    #  bool QFileInfo::isAlias() const
    return self.uglySide.call('ritual_ZNK9QFileInfo7isAliasEv')

  def isJunction(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isJunction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isJunction
    """
    #  bool QFileInfo::isJunction() const
    return self.uglySide.call('ritual_ZNK9QFileInfo10isJunctionEv')

  def isRoot(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isRoot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isRoot
    """
    #  bool QFileInfo::isRoot() const
    return self.uglySide.call('ritual_ZNK9QFileInfo6isRootEv')

  def isBundle(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::isBundle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#isBundle
    """
    #  bool QFileInfo::isBundle() const
    return self.uglySide.call('ritual_ZNK9QFileInfo8isBundleEv')

  def symLinkTarget(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::symLinkTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#symLinkTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::symLinkTarget() const
    return self.uglySide.call('ritual_ZNK9QFileInfo13symLinkTargetEv')

  def readSymLink(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::readSymLink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#readSymLink

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::readSymLink() const
    return self.uglySide.call('ritual_ZNK9QFileInfo11readSymLinkEv')

  def junctionTarget(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::junctionTarget() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#junctionTarget

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::junctionTarget() const
    return self.uglySide.call('ritual_ZNK9QFileInfo14junctionTargetEv')

  def owner(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::owner() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#owner

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::owner() const
    return self.uglySide.call('ritual_ZNK9QFileInfo5ownerEv')

  def ownerId(self) -> int:
    """
    Calls Qt's 'uint QFileInfo::ownerId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#ownerId
    """
    #  uint QFileInfo::ownerId() const
    return self.uglySide.call('ritual_ZNK9QFileInfo7ownerIdEv')

  def group(self) -> str:
    """
    Calls Qt's 'QString QFileInfo::group() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#group

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QFileInfo::group() const
    return self.uglySide.call('ritual_ZNK9QFileInfo5groupEv')

  def groupId(self) -> int:
    """
    Calls Qt's 'uint QFileInfo::groupId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#groupId
    """
    #  uint QFileInfo::groupId() const
    return self.uglySide.call('ritual_ZNK9QFileInfo7groupIdEv')

  @overload(QFileDevice.Permissions)
  def permission(self, permissions: QFileDevice.Permissions) -> bool:
    """
    Calls Qt's 'bool QFileInfo::permission(QFile::Permissions permissions)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#permission

    Parameters
    ----------

    permissions : QFileDevice.Permissions
      Passed on as its number.
    """
    #  bool QFileInfo::permission(QFile::Permissions permissions) const
    return self.uglySide.call(
        'ritual_ZNK9QFileInfo10permissionE6QFlagsIN11QFileDevice10Permissio'
        'nEE',
        permissions.value,
    )

  def size(self) -> int:
    """
    Calls Qt's 'qint64 QFileInfo::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#size
    """
    #  qint64 QFileInfo::size() const
    return self.uglySide.call('ritual_ZNK9QFileInfo4sizeEv')

  @overload()
  def birthTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::birthTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#birthTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::birthTime() const
    address = self.uglySide.call('ritual_ZNK9QFileInfo9birthTimeEv')
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def birthTime(self, tz: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::birthTime(const QTimeZone &tz) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#birthTime

    Parameters
    ----------

    tz : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::birthTime(const QTimeZone &tz) const
    address = self.uglySide.call(
        'ritual_ZNK9QFileInfo9birthTimeERK9QTimeZone', self._valueOf(tz),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  def metadataChangeTime(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::metadataChangeTime() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#metadataChangeTime

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::metadataChangeTime() const
    address = self.uglySide.call(
        'ritual_ZNK9QFileInfo18metadataChangeTimeEv',
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def metadataChangeTime(self, tz: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::metadataChangeTime(const QTimeZone &tz)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#metadataChangeTime

    Parameters
    ----------

    tz : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::metadataChangeTime(const QTimeZone &tz) const
    address = self.uglySide.call(
        'ritual_ZNK9QFileInfo18metadataChangeTimeERK9QTimeZone',
        self._valueOf(tz),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  def lastModified(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::lastModified() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#lastModified

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::lastModified() const
    address = self.uglySide.call('ritual_ZNK9QFileInfo12lastModifiedEv')
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def lastModified(self, tz: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::lastModified(const QTimeZone &tz)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#lastModified

    Parameters
    ----------

    tz : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::lastModified(const QTimeZone &tz) const
    address = self.uglySide.call(
        'ritual_ZNK9QFileInfo12lastModifiedERK9QTimeZone', self._valueOf(tz),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload()
  def lastRead(self) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::lastRead() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#lastRead

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::lastRead() const
    address = self.uglySide.call('ritual_ZNK9QFileInfo8lastReadEv')
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  @overload(QTimeZone)
  def lastRead(self, tz: QTimeZone) -> QDateTime:
    """
    Calls Qt's 'QDateTime QFileInfo::lastRead(const QTimeZone &tz) const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#lastRead

    Parameters
    ----------

    tz : QTimeZone
      Passed on as a value: Qt reads the C++ QTimeZone, which stays Python's
      own.

    Returns
    -------

    QDateTime
      A new cute QDateTime around the copy Qt gave back. Python owns it.
    """
    #  QDateTime QFileInfo::lastRead(const QTimeZone &tz) const
    address = self.uglySide.call(
        'ritual_ZNK9QFileInfo8lastReadERK9QTimeZone', self._valueOf(tz),
    )
    from . import QDateTime
    return QDateTime._cuteOwning(address)

  def caching(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::caching() const'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#caching
    """
    #  bool QFileInfo::caching() const
    return self.uglySide.call('ritual_ZNK9QFileInfo7cachingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFile(self, file: str) -> None:
    """
    Calls Qt's 'void QFileInfo::setFile(const QString &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#setFile

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileInfo::setFile(const QString &file)
    self.uglySide.call('ritual_ZN9QFileInfo7setFileERK7QString', file)

  @overload(QDir, str)
  def setFile(self, dir: QDir, file: str) -> None:
    """
    Calls Qt's 'void QFileInfo::setFile(const QDir &dir, const QString
    &file)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#setFile

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QFileInfo::setFile(const QDir &dir, const QString &file)
    self.uglySide.call(
        'ritual_ZN9QFileInfo7setFileERK4QDirRK7QString',
        self._valueOf(dir), file,
    )

  @overload(bool)
  def setCaching(self, on: bool) -> None:
    """
    Calls Qt's 'void QFileInfo::setCaching(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#setCaching

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QFileInfo::setCaching(bool on)
    self.uglySide.call('ritual_ZN9QFileInfo10setCachingEb', on)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QFileInfo) -> bool:
    """
    Calls Qt's 'bool operator==(const QFileInfo &lhs, const QFileInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#operator==

    Parameters
    ----------

    rhs : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.
    """
    #  bool operator==(const QFileInfo &lhs, const QFileInfo &rhs)
    return Rituals.call(
        'ritual_ZeqRK9QFileInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QFileInfo) -> bool:
    """
    Calls Qt's 'bool operator!=(const QFileInfo &lhs, const QFileInfo &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#operator!=

    Parameters
    ----------

    rhs : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.
    """
    #  bool operator!=(const QFileInfo &lhs, const QFileInfo &rhs)
    return Rituals.call(
        'ritual_ZneRK9QFileInfoS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QFileInfo::QFileInfo()', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#QFileInfo
    """
    #  QFileInfo::QFileInfo()
    self._noteCreation(QFileInfo, lambda: Rituals.call(
        'ritual_ZN9QFileInfoC1Ev',
    ))

  @overload(str)
  def __init__(self, file: str) -> None:
    """
    Notes what was given, for Qt's 'QFileInfo::QFileInfo(const QString
    &file)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#QFileInfo

    Parameters
    ----------

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFileInfo::QFileInfo(const QString &file)
    self._noteCreation(QFileInfo, lambda: Rituals.call(
        'ritual_ZN9QFileInfoC1ERK7QString', file,
    ))

  @overload(QDir, str)
  def __init__(self, dir: QDir, file: str) -> None:
    """
    Notes what was given, for Qt's 'QFileInfo::QFileInfo(const QDir &dir,
    const QString &file)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#QFileInfo

    Parameters
    ----------

    dir : QDir
      Passed on as a value: Qt reads the C++ QDir, which stays Python's own.

    file : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QFileInfo::QFileInfo(const QDir &dir, const QString &file)
    self._noteCreation(QFileInfo, lambda: Rituals.call(
        'ritual_ZN9QFileInfoC1ERK4QDirRK7QString', self._valueOf(dir), file,
    ))

  @overload(THIS)
  def __init__(self, fileinfo: QFileInfo) -> None:
    """
    Notes what was given, for Qt's 'QFileInfo::QFileInfo(const QFileInfo
    &fileinfo)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#QFileInfo

    Parameters
    ----------

    fileinfo : QFileInfo
      Passed on as a value: Qt reads the C++ QFileInfo, which stays Python's
      own.
    """
    #  QFileInfo::QFileInfo(const QFileInfo &fileinfo)
    self._noteCreation(QFileInfo, lambda: Rituals.call(
        'ritual_ZN9QFileInfoC1ERKS_', self._valueOf(fileinfo),
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

  def refresh(self) -> None:
    """
    Calls Qt's 'void QFileInfo::refresh()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#refresh
    """
    #  void QFileInfo::refresh()
    self.uglySide.call('ritual_ZN9QFileInfo7refreshEv')

  def makeAbsolute(self) -> bool:
    """
    Calls Qt's 'bool QFileInfo::makeAbsolute()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#makeAbsolute
    """
    #  bool QFileInfo::makeAbsolute()
    return self.uglySide.call('ritual_ZN9QFileInfo12makeAbsoluteEv')

  def stat(self) -> None:
    """
    Calls Qt's 'void QFileInfo::stat()'.

    Qt's own words: https://doc.qt.io/qt-6/qfileinfo.html#stat
    """
    #  void QFileInfo::stat()
    self.uglySide.call('ritual_ZN9QFileInfo4statEv')


#  Qt's 'QList<QFileInfo>': the list of QFileInfo, which 'QList[QFileInfo]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QFileInfo. Qt has a name of its own for it.
QFileInfoList = QList.createKind(
    QFileInfo, 'value',
    name='QFileInfoList',
    make='ritual_list_make_QFileInfo',
    add='ritual_list_add_QFileInfo',
    size='ritual_list_size_QFileInfo',
    at='ritual_list_at_QFileInfo',
    drop='ritual_list_drop_QFileInfo',
)
