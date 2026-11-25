//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemengine_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the lines pulling in Unix's headers
//  'qcore_unix_p.h', 'grp.h', 'pwd.h' and 'unistd.h', and the code
//  taken for 'id(int)', which Qt declares on Unix only, stand under
//  'defined(Q_OS_UNIX)', for Windows has none of them, and the lines
//  pulling in the Objective-C headers 'UTType.h', 'UTCoreTypes.h' and
//  'Foundation.h' stand under '__OBJC__', as 'Foundation.h' does in
//  Qt's 'qcore_mac_p.h', for Qt compiles this source as Objective-C++
//  on Apple and a ritual file is C++. Kept as it is when the generator
//  runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystementry_p.h>
#include <QtCore/6.12.0/QtCore/private/qfilesystemmetadata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
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
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qdir.h>
#include <QtCore/qset.h>
#include <QtCore/qstringbuilder.h>
#include <QtCore/private/qabstractfileengine_p.h>
#ifdef QT_BUILD_CORE_LIB
#include <QtCore/private/qresource_p.h>
#endif
#include <QtCore/private/qduplicatetracker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 810, as _ZN17QFileSystemEngine15resolveUserNameEj
#if defined(Q_OS_LINUX)
inline QString QFileSystemEngine::resolveUserName(uint userId)
{
#if QT_CONFIG(thread) && defined(_POSIX_THREAD_SAFE_FUNCTIONS) && !defined(Q_OS_OPENBSD)
    long size_max = sysconf(_SC_GETPW_R_SIZE_MAX);
    if (size_max == -1)
        size_max = 1024;
    QVarLengthArray<char, 1024> buf(size_max);
#endif

#if !defined(Q_OS_INTEGRITY) && !defined(Q_OS_WASM)
    struct passwd *pw = nullptr;
#if QT_CONFIG(thread) && defined(_POSIX_THREAD_SAFE_FUNCTIONS) && !defined(Q_OS_OPENBSD) && !defined(Q_OS_VXWORKS)
    struct passwd entry;
    getpwuid_r(userId, &entry, buf.data(), buf.size(), &pw);
#else
    pw = getpwuid(userId);
#endif
    if (pw)
        return QFile::decodeName(QByteArray(pw->pw_name));
#else // Integrity || WASM
    Q_UNUSED(userId);
#endif
    return QString();
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 836, as _ZN17QFileSystemEngine16resolveGroupNameEj
#if defined(Q_OS_LINUX)
inline QString QFileSystemEngine::resolveGroupName(uint groupId)
{
#if QT_CONFIG(thread) && defined(_POSIX_THREAD_SAFE_FUNCTIONS) && !defined(Q_OS_OPENBSD)
    long size_max = sysconf(_SC_GETPW_R_SIZE_MAX);
    if (size_max == -1)
        size_max = 1024;
    QVarLengthArray<char, 1024> buf(size_max);
#endif

#if !defined(Q_OS_INTEGRITY) && !defined(Q_OS_WASM)
    struct group *gr = nullptr;
#if QT_CONFIG(thread) && defined(_POSIX_THREAD_SAFE_FUNCTIONS) && !defined(Q_OS_OPENBSD) && !defined(Q_OS_VXWORKS) && (!defined(Q_OS_ANDROID) || defined(Q_OS_ANDROID) && (__ANDROID_API__ >= 24))
    size_max = sysconf(_SC_GETGR_R_SIZE_MAX);
    if (size_max == -1)
        size_max = 1024;
    buf.resize(size_max);
    struct group entry;
    // Some large systems have more members than the POSIX max size
    // Loop over by doubling the buffer size (upper limit 250k)
    for (long size = size_max; size < 256000; size += size)
    {
        buf.resize(size);
        // ERANGE indicates that the buffer was too small
        if (!getgrgid_r(groupId, &entry, buf.data(), buf.size(), &gr)
            || errno != ERANGE)
            break;
    }
#else
    gr = getgrgid(groupId);
#endif
    if (gr)
        return QFile::decodeName(QByteArray(gr->gr_name));
#else // Integrity || WASM || VxWorks
    Q_UNUSED(groupId);
#endif
    return QString();
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 1142, as _ZN17QFileSystemEngine9cloneFileEiiRK19QFileSystemMetaData
#if defined(Q_OS_LINUX)
inline auto QFileSystemEngine::cloneFile(int srcfd, int dstfd, const QFileSystemMetaData &knownData) -> TriStateResult
{
    QT_STATBUF statBuffer;
    if (knownData.hasFlags(QFileSystemMetaData::PosixStatFlags) &&
            knownData.isFile()) {
        statBuffer.st_mode = S_IFREG;
    } else if (knownData.hasFlags(QFileSystemMetaData::PosixStatFlags) &&
               knownData.isDirectory()) {
        errno = EISDIR;
        return TriStateResult::Failed;   // fcopyfile(3) returns success on directories
    } else if (QT_FSTAT(srcfd, &statBuffer) == -1) {
        // errno was set
        return TriStateResult::Failed;
    } else if (!S_ISREG((statBuffer.st_mode))) {
        // not a regular file, let QFile do the copy
        return TriStateResult::NotSupported;
    }

    [[maybe_unused]] auto destinationIsEmpty = [dstfd]() {
        QT_STATBUF statBuffer;
        return QT_FSTAT(dstfd, &statBuffer) == 0 && statBuffer.st_size == 0;
    };
    Q_ASSERT(destinationIsEmpty());

#if defined(Q_OS_LINUX)
    // first, try FICLONE (only works on regular files and only on certain fs)
    if (::ioctl(dstfd, FICLONE, srcfd) == 0)
        return TriStateResult::Success;
#elif defined(Q_OS_DARWIN)
    // try fcopyfile
    if (fcopyfile(srcfd, dstfd, nullptr, COPYFILE_DATA | COPYFILE_STAT) == 0)
        return TriStateResult::Success;
    switch (errno) {
    case ENOTSUP:
    case ENOMEM:
        return TriStateResult::NotSupported;    // let QFile try
    }
    return TriStateResult::Failed;
#endif

#if QT_CONFIG(copy_file_range)
    // Second, try copy_file_range. Tested on Linux & FreeBSD: FreeBSD can copy
    // across mountpoints, Linux currently (6.12) can only if the source and
    // destination mountpoints are the same filesystem type.
    QT_OFF_T srcoffset = 0;
    ssize_t copied;
    do {
        copied = ::copy_file_range(srcfd, &srcoffset, dstfd, nullptr, SSIZE_MAX, 0);
    } while (copied > 0 || (copied < 0 && errno == EINTR));
    if (copied == 0)
        return TriStateResult::Success;         // EOF -> success
    if (srcoffset) {
        // some bytes were copied, so this is a real error (like ENOSPC).
        copied = ftruncate(dstfd, 0);
        return TriStateResult::Failed;
    }

    // We failed with no bytes copied, so is this a real filesystem failure
    // that will remain with sendfile() or the copy pump? Or is it a
    // copy_file_range() condition?
    switch (errno) {
    case EINVAL: // observed with some obscure filesystem combinations
    case EXDEV: // Linux can't do xdev file copies (FreeBSD can)
    case ENOSYS: // caused by some containers wrongly filtering the system call
        break;

    default:
        return TriStateResult::Failed;
    }
#endif

#if defined(Q_OS_LINUX)
    // For Linux, try sendfile (it can send to some special types too).
    // sendfile(2) is limited in the kernel to 2G - 4k
    const size_t SendfileSize = 0x7ffff000;

    ssize_t n = ::sendfile(dstfd, srcfd, nullptr, SendfileSize);
    if (n == -1) {
        switch (errno) {
        case ENOSPC:
        case EIO:
            return TriStateResult::Failed;
        }

        // if we got an error here, give up and try at an upper layer
        return TriStateResult::NotSupported;
    }

    while (n) {
        n = ::sendfile(dstfd, srcfd, nullptr, SendfileSize);
        if (n == -1) {
            // uh oh, this is probably a real error (like ENOSPC)
            n = ftruncate(dstfd, 0);
            n = lseek(srcfd, 0, SEEK_SET);
            n = lseek(dstfd, 0, SEEK_SET);
            return TriStateResult::Failed;
        }
    }

    return TriStateResult::Success;
#else
    Q_UNUSED(dstfd);
    return TriStateResult::NotSupported;
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 796, as _ZN17QFileSystemEngine2idEi
#if defined(Q_OS_UNIX)
inline QByteArray QFileSystemEngine::id(int fd)
{
    QT_STATBUF statResult;
    if (QT_FSTAT(fd, &statResult)) {
        qErrnoWarning("fstat() failed for fd %d", fd);
        return QByteArray();
    }
    QByteArray result = QByteArray::number(quint64(statResult.st_dev), 16);
    result += ':';
    result += QByteArray::number(quint64(statResult.st_ino));
    return result;
}
#endif  // defined(Q_OS_UNIX)

//  from src/corelib/io/qfilesystemengine.cpp, line 49, as _ZN17QFileSystemEngine17slowCanonicalizedERK7QString
#if defined(Q_OS_LINUX)
inline QString QFileSystemEngine::slowCanonicalized(const QString &path)
{
    if (path.isEmpty())
        return path;

    QFileInfo fi;
    const QChar slash(u'/');
    QString tmpPath = path;
    qsizetype separatorPos = 0;
    QSet<QString> nonSymlinks;
    QDuplicateTracker<QString> known;

    (void)known.hasSeen(path);
    do {
#ifdef Q_OS_WIN
        if (separatorPos == 0) {
            if (tmpPath.size() >= 2 && tmpPath.at(0) == slash && tmpPath.at(1) == slash) {
                // UNC, skip past the first two elements
                separatorPos = tmpPath.indexOf(slash, 2);
            } else if (tmpPath.size() >= 3 && tmpPath.at(1) == u':' && tmpPath.at(2) == slash) {
                // volume root, skip since it can not be a symlink
                separatorPos = 2;
            }
        }
        if (separatorPos != -1)
#endif
        separatorPos = tmpPath.indexOf(slash, separatorPos + 1);
        QString prefix = separatorPos == -1 ? tmpPath : tmpPath.left(separatorPos);
        if (!nonSymlinks.contains(prefix)) {
            fi.setFile(prefix);
            if (fi.isSymLink()) {
                QString target = fi.symLinkTarget();
                if (separatorPos != -1) {
                    if (fi.isDir() && !target.endsWith(slash))
                        target.append(slash);
                    target.append(QStringView{tmpPath}.mid(separatorPos));
                }
                tmpPath = QDir::cleanPath(target);
                separatorPos = 0;

                if (known.hasSeen(tmpPath))
                    return QString();
            } else {
                nonSymlinks.insert(prefix);
            }
        }
    } while (separatorPos != -1);

    return QDir::cleanPath(tmpPath);
}
#endif  // defined(Q_OS_LINUX)
//  -----------------------------------------------------------------------

#if defined(Q_OS_UNIX)
#if defined(Q_OS_LINUX)
//  QString QFileSystemEngine::resolveUserName(uint userId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFileSystemEngine15resolveUserNameEj(uint userId) {
  return new QString(QFileSystemEngine::resolveUserName(userId));
}
#endif  // defined(Q_OS_LINUX)
#endif  // defined(Q_OS_UNIX)

#if defined(Q_OS_UNIX)
#if defined(Q_OS_LINUX)
//  QString QFileSystemEngine::resolveGroupName(uint groupId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFileSystemEngine16resolveGroupNameEj(uint groupId) {
  return new QString(QFileSystemEngine::resolveGroupName(groupId));
}
#endif  // defined(Q_OS_LINUX)
#endif  // defined(Q_OS_UNIX)

#if !(defined(Q_OS_DARWIN))
//  QString QFileSystemEngine::bundleName(const QFileSystemEntry &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFileSystemEngine10bundleNameERK16QFileSystemEntry(
    const QFileSystemEntry *a0) {
  return new QString(QFileSystemEngine::bundleName(*a0));
}
#endif  // !(defined(Q_OS_DARWIN))

#if defined(Q_OS_UNIX)
#if defined(Q_OS_LINUX)
//  TriStateResult QFileSystemEngine::cloneFile(int srcfd, int dstfd, const
//      QFileSystemMetaData &knownData)
extern "C" Q_DECL_EXPORT
QFileSystemEngine::TriStateResult ritual_ZN17QFileSystemEngine9cloneFileEiiRK19QFileSystemMetaData(
    int srcfd,
    int dstfd,
    const QFileSystemMetaData *knownData) {
  return QFileSystemEngine::cloneFile(srcfd, dstfd, *knownData);
}
#endif  // defined(Q_OS_LINUX)
#endif  // defined(Q_OS_UNIX)

#if defined(Q_OS_UNIX)
//  QByteArray QFileSystemEngine::id(int fd)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QFileSystemEngine2idEi(int fd) {
  return new QByteArray(QFileSystemEngine::id(fd));
}
#endif  // defined(Q_OS_UNIX)

#if defined(Q_OS_LINUX)
//  QString QFileSystemEngine::slowCanonicalized(const QString &path)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QFileSystemEngine17slowCanonicalizedERK7QString(
    const QString *path) {
  return new QString(QFileSystemEngine::slowCanonicalized(*path));
}
#endif  // defined(Q_OS_LINUX)

//  QFileSystemEngine::~QFileSystemEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFileSystemEngineD1Ev(QFileSystemEngine *self) {
  delete self;
}
