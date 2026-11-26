//  Edited by hand on 2026-11-25: 'fillFromDirEnt' takes Qt's
//  'QT_DIRENT', which on Linux is 'struct dirent64', not 'struct
//  dirent': its ritual takes a 'const QT_DIRENT *', and is named by
//  'dirent64' as Qt's Linux library names it. Kept as it is when the
//  generator runs again.
//  Edited by hand again on 2026-11-26: the lines pulling in Unix's
//  headers 'qcore_unix_p.h', 'grp.h', 'pwd.h' and 'unistd.h' stand
//  under 'defined(Q_OS_UNIX)', for Windows has none of them, and the
//  lines pulling in the Objective-C headers 'UTType.h',
//  'UTCoreTypes.h' and 'Foundation.h' under '__OBJC__', as
//  'Foundation.h' does in Qt's 'qcore_mac_p.h', for Qt compiles
//  qfilesystemengine_unix.cpp, where they come from, as Objective-C++
//  on Apple and a ritual file is C++. Kept as it is when the generator
//  runs again.
//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemmetadata_p.h, Qt 6.12.0.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemmetadata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qstorageinfo.h>
#include <QtCore/qurl.h>
#include <QtCore/qoperatingsystemversion.h>
#if defined(Q_OS_UNIX)
#include <QtCore/private/qcore_unix_p.h>
#endif  // defined(Q_OS_UNIX)
#include <QtCore/private/qfiledevice_p.h>
#include <QtCore/private/qfunctions_p.h>
#include <QtCore/qvarlengtharray.h>
#ifndef QT_BOOTSTRAPPED
# include <QtCore/qstandardpaths.h>
# include <QtCore/private/qtemporaryfile_p.h>
#endif
#if defined(Q_OS_UNIX)
#include <grp.h>
#include <pwd.h>
#endif  // defined(Q_OS_UNIX)
#include <stdlib.h> // for realpath()
#if defined(Q_OS_UNIX)
#include <unistd.h>
#endif  // defined(Q_OS_UNIX)
#include <stdio.h>
#include <errno.h>
#include <chrono>
#if __has_include(<paths.h>)
# include <paths.h>
#endif
#if __has_include(<sys/disk.h>)
# include <sys/disk.h>
#endif
#if defined(Q_OS_DARWIN)
# include <QtCore/private/qcore_mac_p.h>
# include <CoreFoundation/CFBundle.h>
# ifdef __OBJC__
#  include <UniformTypeIdentifiers/UTType.h>
#  include <UniformTypeIdentifiers/UTCoreTypes.h>
#  include <Foundation/Foundation.h>
# endif  // __OBJC__
# include <copyfile.h>
#endif
#ifdef Q_OS_MACOS
#include <CoreServices/CoreServices.h>
#endif
#if defined(QT_PLATFORM_UIKIT)
#include <MobileCoreServices/MobileCoreServices.h>
#endif
#if defined(Q_OS_LINUX)
#  include <sys/ioctl.h>
#  include <sys/sendfile.h>
#  include <linux/fs.h>
#endif
#if defined(Q_OS_VXWORKS)
# include <sys/statfs.h>
# if __has_include(<dosFsLib.h>)
#  include <dosFsLib.h>
# endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 517, as _ZN19QFileSystemMetaData14fillFromDirEntERK6dirent
#if defined(Q_OS_LINUX)
inline void QFileSystemMetaData::fillFromDirEnt(const QT_DIRENT &entry)
{
#if defined(_DEXTRA_FIRST)
    knownFlagsMask = {};
    entryFlags = {};
    for (dirent_extra *extra = _DEXTRA_FIRST(&entry); _DEXTRA_VALID(extra, &entry);
         extra = _DEXTRA_NEXT(extra)) {
        if (extra->d_type == _DTYPE_STAT || extra->d_type == _DTYPE_LSTAT) {

            const struct dirent_extra_stat * const extra_stat =
                    reinterpret_cast<struct dirent_extra_stat *>(extra);

            // Remember whether this was a link or not, this saves an lstat() call later.
            if (extra->d_type == _DTYPE_LSTAT) {
                knownFlagsMask |= QFileSystemMetaData::LinkType;
                if (S_ISLNK(extra_stat->d_stat.st_mode))
                    entryFlags |= QFileSystemMetaData::LinkType;
            }

            // For symlinks, the extra type _DTYPE_LSTAT doesn't work for filling out the meta data,
            // as we need the stat() information there, not the lstat() information.
            // In this case, don't use the extra information.
            // Unfortunately, readdir() never seems to return extra info of type _DTYPE_STAT, so for
            // symlinks, we always incur the cost of an extra stat() call later.
            if (S_ISLNK(extra_stat->d_stat.st_mode) && extra->d_type == _DTYPE_LSTAT)
                continue;

#if defined(QT_USE_XOPEN_LFS_EXTENSIONS) && defined(QT_LARGEFILE_SUPPORT)
            // Even with large file support, d_stat is always of type struct stat, not struct stat64,
            // so it needs to be converted
            struct stat64 statBuf;
            fillStat64fromStat32(&statBuf, extra_stat->d_stat);
            fillFromStatBuf(statBuf);
#else
            fillFromStatBuf(extra_stat->d_stat);
#endif
            knownFlagsMask |= QFileSystemMetaData::PosixStatFlags;
            if (!S_ISLNK(extra_stat->d_stat.st_mode)) {
                knownFlagsMask |= QFileSystemMetaData::ExistsAttribute;
                entryFlags |= QFileSystemMetaData::ExistsAttribute;
            }
        }
    }
#elif defined(_DIRENT_HAVE_D_TYPE) || defined(Q_OS_BSD4)
    // BSD4 includes OS X and iOS

    // ### This will clear all entry flags and knownFlagsMask
    switch (entry.d_type)
    {
    case DT_DIR:
        knownFlagsMask = QFileSystemMetaData::LinkType
            | QFileSystemMetaData::FileType
            | QFileSystemMetaData::DirectoryType
            | QFileSystemMetaData::SequentialType
            | QFileSystemMetaData::ExistsAttribute;

        entryFlags = QFileSystemMetaData::DirectoryType
            | QFileSystemMetaData::ExistsAttribute;

        break;

    case DT_BLK:
        knownFlagsMask = QFileSystemMetaData::LinkType
            | QFileSystemMetaData::FileType
            | QFileSystemMetaData::DirectoryType
            | QFileSystemMetaData::BundleType
            | QFileSystemMetaData::AliasType
            | QFileSystemMetaData::SequentialType
            | QFileSystemMetaData::ExistsAttribute;

        entryFlags = QFileSystemMetaData::ExistsAttribute;

        break;

    case DT_CHR:
    case DT_FIFO:
    case DT_SOCK:
        // ### System attribute
        knownFlagsMask = QFileSystemMetaData::LinkType
            | QFileSystemMetaData::FileType
            | QFileSystemMetaData::DirectoryType
            | QFileSystemMetaData::BundleType
            | QFileSystemMetaData::AliasType
            | QFileSystemMetaData::SequentialType
            | QFileSystemMetaData::ExistsAttribute;

        entryFlags = QFileSystemMetaData::SequentialType
            | QFileSystemMetaData::ExistsAttribute;

        break;

    case DT_LNK:
        knownFlagsMask = QFileSystemMetaData::LinkType;
        entryFlags = QFileSystemMetaData::LinkType;
        break;

    case DT_REG:
        knownFlagsMask = QFileSystemMetaData::LinkType
            | QFileSystemMetaData::FileType
            | QFileSystemMetaData::DirectoryType
            | QFileSystemMetaData::BundleType
            | QFileSystemMetaData::SequentialType
            | QFileSystemMetaData::ExistsAttribute;

        entryFlags = QFileSystemMetaData::FileType
            | QFileSystemMetaData::ExistsAttribute;

        break;

    case DT_UNKNOWN:
    default:
        clear();
    }
#else
    Q_UNUSED(entry);
#endif
}
#endif  // defined(Q_OS_LINUX)
//  -----------------------------------------------------------------------

//  QFileSystemMetaData::QFileSystemMetaData()
extern "C" Q_DECL_EXPORT
QFileSystemMetaData *ritual_ZN19QFileSystemMetaDataC1Ev() {
  return new QFileSystemMetaData();
}

//  bool QFileSystemMetaData::hasFlags(MetaDataFlags flags) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData8hasFlagsE6QFlagsINS_12MetaDataFlagEE(
    const QFileSystemMetaData *self,
    int flags) {
  return self->hasFlags(
      QFlags<QFileSystemMetaData::MetaDataFlag>::fromInt(flags));
}

//  MetaDataFlags QFileSystemMetaData::missingFlags(MetaDataFlags flags)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QFileSystemMetaData12missingFlagsE6QFlagsINS_12MetaDataFlagEE(
    QFileSystemMetaData *self,
    int flags) {
  return static_cast<int>(
      self->missingFlags(
          QFlags<QFileSystemMetaData::MetaDataFlag>::fromInt(flags)).toInt());
}

//  void QFileSystemMetaData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData5clearEv(QFileSystemMetaData *self) {
  self->clear();
}

//  void QFileSystemMetaData::clearFlags(MetaDataFlags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData10clearFlagsE6QFlagsINS_12MetaDataFlagEE(
    QFileSystemMetaData *self,
    int flags) {
  self->clearFlags(
      QFlags<QFileSystemMetaData::MetaDataFlag>::fromInt(flags));
}

//  bool QFileSystemMetaData::exists() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData6existsEv(
    const QFileSystemMetaData *self) {
  return self->exists();
}

//  bool QFileSystemMetaData::isLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData6isLinkEv(
    const QFileSystemMetaData *self) {
  return self->isLink();
}

//  bool QFileSystemMetaData::isFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData6isFileEv(
    const QFileSystemMetaData *self) {
  return self->isFile();
}

//  bool QFileSystemMetaData::isDirectory() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData11isDirectoryEv(
    const QFileSystemMetaData *self) {
  return self->isDirectory();
}

//  bool QFileSystemMetaData::isBundle() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData8isBundleEv(
    const QFileSystemMetaData *self) {
  return self->isBundle();
}

//  bool QFileSystemMetaData::isAlias() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData7isAliasEv(
    const QFileSystemMetaData *self) {
  return self->isAlias();
}

//  bool QFileSystemMetaData::isLegacyLink() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData12isLegacyLinkEv(
    const QFileSystemMetaData *self) {
  return self->isLegacyLink();
}

//  bool QFileSystemMetaData::isSequential() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData12isSequentialEv(
    const QFileSystemMetaData *self) {
  return self->isSequential();
}

//  bool QFileSystemMetaData::isHidden() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData8isHiddenEv(
    const QFileSystemMetaData *self) {
  return self->isHidden();
}

//  bool QFileSystemMetaData::wasDeleted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10wasDeletedEv(
    const QFileSystemMetaData *self) {
  return self->wasDeleted();
}

#if !(defined(Q_OS_WIN))
//  bool QFileSystemMetaData::isLnkFile() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData9isLnkFileEv(
    const QFileSystemMetaData *self) {
  return self->isLnkFile();
}
#endif  // !(defined(Q_OS_WIN))

#if !(defined(Q_OS_WIN))
//  bool QFileSystemMetaData::isJunction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10isJunctionEv(
    const QFileSystemMetaData *self) {
  return self->isJunction();
}
#endif  // !(defined(Q_OS_WIN))

//  qint64 QFileSystemMetaData::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QFileSystemMetaData4sizeEv(
    const QFileSystemMetaData *self) {
  return self->size();
}

//  void QFileSystemMetaData::setPermissions(QFile::Permissions permissions)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData14setPermissionsE6QFlagsIN11QFileDevice10PermissionEE(
    QFileSystemMetaData *self,
    int permissions) {
  self->setPermissions(
      QFlags<QFileDevice::Permission>::fromInt(permissions));
}

//  QDateTime QFileSystemMetaData::accessTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData10accessTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->accessTime());
}

//  QDateTime QFileSystemMetaData::birthTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData9birthTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->birthTime());
}

//  QDateTime QFileSystemMetaData::metadataChangeTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData18metadataChangeTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->metadataChangeTime());
}

//  QDateTime QFileSystemMetaData::modificationTime() const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QFileSystemMetaData16modificationTimeEv(
    const QFileSystemMetaData *self) {
  return new QDateTime(self->modificationTime());
}

//  uint QFileSystemMetaData::userId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QFileSystemMetaData6userIdEv(
    const QFileSystemMetaData *self) {
  return self->userId();
}

//  uint QFileSystemMetaData::groupId() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QFileSystemMetaData7groupIdEv(
    const QFileSystemMetaData *self) {
  return self->groupId();
}

//  uint QFileSystemMetaData::ownerId(QAbstractFileEngine::FileOwner owner)
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QFileSystemMetaData7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QFileSystemMetaData *self,
    QAbstractFileEngine::FileOwner owner) {
  return self->ownerId(owner);
}

//  bool QFileSystemMetaData::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10isReadableEv(
    const QFileSystemMetaData *self) {
  return self->isReadable();
}

//  bool QFileSystemMetaData::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData10isWritableEv(
    const QFileSystemMetaData *self) {
  return self->isWritable();
}

//  bool QFileSystemMetaData::isExecutable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFileSystemMetaData12isExecutableEv(
    const QFileSystemMetaData *self) {
  return self->isExecutable();
}

#if defined(Q_OS_UNIX)
#if defined(Q_OS_LINUX)
//  void QFileSystemMetaData::fillFromDirEnt(const QT_DIRENT &statBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaData14fillFromDirEntERK8dirent64(
    QFileSystemMetaData *self,
    const QT_DIRENT *statBuffer) {
  self->fillFromDirEnt(*statBuffer);
}
#endif  // defined(Q_OS_LINUX)
#endif  // defined(Q_OS_UNIX)

//  QFileSystemMetaData::~QFileSystemMetaData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileSystemMetaDataD1Ev(QFileSystemMetaData *self) {
  delete self;
}
