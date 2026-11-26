//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfileinfo_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfileinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QFile>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/qfile.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef Q_OS_WIN
#include <QtCore/qstringbuilder.h>
#endif
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qdir.h>
#include <QtCore/qset.h>
#include <QtCore/qstringbuilder.h>
#include <QtCore/private/qabstractfileengine_p.h>
#ifdef QT_BUILD_CORE_LIB
#include <QtCore/private/qresource_p.h>
#endif
#include <QtCore/private/qduplicatetracker_p.h>
#include "qplatformdefs.h"
#include <QtCore/qfileinfo.h>
#include <QtCore/qglobal.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qfileinfo_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystemengine.cpp, line 100, as local:qfilesystemengine.cpp:_q_checkEntry
static inline bool _q_checkEntry(QFileSystemEntry &entry, QFileSystemMetaData &data, bool resolvingEntry)
{
    if (resolvingEntry) {
        if (!QFileSystemEngine::fillMetaData(entry, data, QFileSystemMetaData::ExistsAttribute)
                || !data.exists()) {
            data.clear();
            return false;
        }
    }

    return true;
}

//  from src/corelib/io/qfilesystementry.cpp, line 21, as local:qfilesystementry.cpp:Uninitialized
constexpr int Uninitialized = -2;

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

//  from src/corelib/io/qfilesystemengine.cpp, line 213, as _ZN17QFileSystemEngine15resolveUserNameERK16QFileSystemEntryR19QFileSystemMetaData
#if defined(Q_OS_LINUX)
inline QString QFileSystemEngine::resolveUserName(const QFileSystemEntry &entry, QFileSystemMetaData &metaData)
{
#if defined(Q_OS_WIN)
    Q_UNUSED(metaData);
    return QFileSystemEngine::owner(entry, QAbstractFileEngine::OwnerUser);
#else //(Q_OS_UNIX)
    if (!metaData.hasFlags(QFileSystemMetaData::UserId))
        QFileSystemEngine::fillMetaData(entry, metaData, QFileSystemMetaData::UserId);
    if (!metaData.exists())
        return QString();
    return resolveUserName(metaData.userId());
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystemengine.cpp, line 228, as _ZN17QFileSystemEngine16resolveGroupNameERK16QFileSystemEntryR19QFileSystemMetaData
#if defined(Q_OS_LINUX)
inline QString QFileSystemEngine::resolveGroupName(const QFileSystemEntry &entry, QFileSystemMetaData &metaData)
{
#if defined(Q_OS_WIN)
    Q_UNUSED(metaData);
    return QFileSystemEngine::owner(entry, QAbstractFileEngine::OwnerGroup);
#else //(Q_OS_UNIX)
    if (!metaData.hasFlags(QFileSystemMetaData::GroupId))
        QFileSystemEngine::fillMetaData(entry, metaData, QFileSystemMetaData::GroupId);
    if (!metaData.exists())
        return QString();
    return resolveGroupName(metaData.groupId());
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfileinfo.cpp, line 101, as _ZNK16QFileInfoPrivate12getFileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE
inline uint QFileInfoPrivate::getFileFlags(QAbstractFileEngine::FileFlags request) const
{
    Q_ASSERT(fileEngine); // should never be called when using the native FS
    // We split the testing into tests for for LinkType, BundleType, PermsMask
    // and the rest.
    // Tests for file permissions on Windows can be slow, especially on network
    // paths and NTFS drives.
    // In order to determine if a file is a symlink or not, we have to lstat().
    // If we're not interested in that information, we might as well avoid one
    // extra syscall. Bundle detecton on Mac can be slow, especially on network
    // paths, so we separate out that as well.

    QAbstractFileEngine::FileFlags req;
    uint cachedFlags = 0;

    if (request & (QAbstractFileEngine::FlagsMask | QAbstractFileEngine::TypesMask)) {
        if (!getCachedFlag(CachedFileFlags)) {
            req |= QAbstractFileEngine::FlagsMask;
            req |= QAbstractFileEngine::TypesMask;
            req &= (~QAbstractFileEngine::LinkType);
            req &= (~QAbstractFileEngine::BundleType);

            cachedFlags |= CachedFileFlags;
        }

        if (request & QAbstractFileEngine::LinkType) {
            if (!getCachedFlag(CachedLinkTypeFlag)) {
                req |= QAbstractFileEngine::LinkType;
                cachedFlags |= CachedLinkTypeFlag;
            }
        }

        if (request & QAbstractFileEngine::BundleType) {
            if (!getCachedFlag(CachedBundleTypeFlag)) {
                req |= QAbstractFileEngine::BundleType;
                cachedFlags |= CachedBundleTypeFlag;
            }
        }
    }

    if (request & QAbstractFileEngine::PermsMask) {
        if (!getCachedFlag(CachedPerms)) {
            req |= QAbstractFileEngine::PermsMask;
            cachedFlags |= CachedPerms;
        }
    }

    if (req) {
        if (cache_enabled)
            req &= (~QAbstractFileEngine::Refresh);
        else
            req |= QAbstractFileEngine::Refresh;

        QAbstractFileEngine::FileFlags flags = fileEngine->fileFlags(req);
        fileFlags |= uint(flags.toInt());
        setCachedFlag(cachedFlags);
    }

    return fileFlags & request.toInt();
}

//  from src/corelib/io/qfileinfo.cpp, line 162, as _ZNK16QFileInfoPrivate11getFileTimeEN11QFileDevice8FileTimeE
inline QDateTime &QFileInfoPrivate::getFileTime(QFile::FileTime request) const
{
    Q_ASSERT(fileEngine); // should never be called when using the native FS
    if (!cache_enabled)
        clearFlags();

    uint cf = 0;
    switch (request) {
    case QFile::FileAccessTime:
        cf = CachedATime;
        break;
    case QFile::FileBirthTime:
        cf = CachedBTime;
        break;
    case QFile::FileMetadataChangeTime:
        cf = CachedMCTime;
        break;
    case QFile::FileModificationTime:
        cf = CachedMTime;
        break;
    }

    if (!getCachedFlag(cf)) {
        fileTimes[request] = fileEngine->fileTime(request);
        setCachedFlag(cf);
    }
    return fileTimes[request];
}
//  -----------------------------------------------------------------------

//  QFileInfoPrivate *QFileInfoPrivate::get(QFileInfo *fi)
extern "C" Q_DECL_EXPORT
QFileInfoPrivate *ritual_ZN16QFileInfoPrivate3getEP9QFileInfo(
    QFileInfo *fi) {
  return QFileInfoPrivate::get(fi);
}

//  QFileInfoPrivate::QFileInfoPrivate()
extern "C" Q_DECL_EXPORT
QFileInfoPrivate *ritual_ZN16QFileInfoPrivateC1Ev() {
  return new QFileInfoPrivate();
}

//  void QFileInfoPrivate::clearFlags() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFileInfoPrivate10clearFlagsEv(
    const QFileInfoPrivate *self) {
  self->clearFlags();
}

//  void QFileInfoPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileInfoPrivate5clearEv(QFileInfoPrivate *self) {
  self->clear();
}

//  uint QFileInfoPrivate::getFileFlags(QAbstractFileEngine::FileFlags a0)
//      const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK16QFileInfoPrivate12getFileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE(
    const QFileInfoPrivate *self,
    int a0) {
  return self->getFileFlags(
      QFlags<QAbstractFileEngine::FileFlag>::fromInt(a0));
}

//  QDateTime &QFileInfoPrivate::getFileTime(QFile::FileTime a0) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK16QFileInfoPrivate11getFileTimeEN11QFileDevice8FileTimeE(
    const QFileInfoPrivate *self,
    const QFile::FileTime *a0) {
  return &(self->getFileTime(*a0));
}

//  bool QFileInfoPrivate::getCachedFlag(uint c) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QFileInfoPrivate13getCachedFlagEj(
    const QFileInfoPrivate *self,
    uint c) {
  return self->getCachedFlag(c);
}

//  void QFileInfoPrivate::setCachedFlag(uint c) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QFileInfoPrivate13setCachedFlagEj(
    const QFileInfoPrivate *self,
    uint c) {
  self->setCachedFlag(c);
}

//  QFileInfoPrivate::~QFileInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QFileInfoPrivateD1Ev(QFileInfoPrivate *self) {
  delete self;
}
