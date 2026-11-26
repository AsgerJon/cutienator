//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfsfileengine_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if !defined(QT_NO_FSFILEENGINE)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfsfileengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/qdir.h>
#include <QtCore/private/qdir_p.h>
#include <QtCore/qfile.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef Q_OS_WIN
#include <QtCore/qstringbuilder.h>
#endif
#include <QtCore/private/qabstractfileengine_p.h>
#include <QtCore/private/qfsfileengine_p.h>
#ifdef QT_BUILD_CORE_LIB
#include <QtCore/private/qresource_p.h>
#endif
#include <QtCore/qdatetime.h>
#include <QtCore/qreadwritelock.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdirlisting.h>
#include <QtCore/qstringbuilder.h>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/private/qfilesystemmetadata_p.h>
#include <QtCore/private/qfilesystemengine_p.h>
#include "qplatformdefs.h"
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qstorageinfo.h>
#include <QtCore/qurl.h>
#include <QtCore/qoperatingsystemversion.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/private/qfiledevice_p.h>
#include <QtCore/private/qfunctions_p.h>
#include <QtCore/qvarlengtharray.h>
#ifndef QT_BOOTSTRAPPED
# include <QtCore/qstandardpaths.h>
# include <QtCore/private/qtemporaryfile_p.h>
#endif
#include <grp.h>
#include <pwd.h>
#include <stdlib.h> // for realpath()
#include <unistd.h>
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
# include <UniformTypeIdentifiers/UTType.h>
# include <UniformTypeIdentifiers/UTCoreTypes.h>
# include <Foundation/Foundation.h>
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
#include <QtCore/private/qfsfileengine_p.h>
#include <QtCore/private/qfsfileengine_iterator_p.h>
#include <QtCore/private/qfilesystemengine_p.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qset.h>
#include <QtCore/qdebug.h>
#ifndef QT_NO_FSFILEENGINE
#include <errno.h>
#if defined(Q_OS_UNIX)
#include <QtCore/private/qcore_unix_p.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#if defined(Q_OS_DARWIN)
# include <QtCore/private/qcore_mac_p.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 299, as local:qfilesystemengine_unix.cpp:flagsFromStMode
#if defined(Q_OS_LINUX)
static QFileSystemMetaData::MetaDataFlags
flagsFromStMode(mode_t mode, [[maybe_unused]] quint64 attributes)
{
    // inode exists
    QFileSystemMetaData::MetaDataFlags entryFlags = QFileSystemMetaData::ExistsAttribute;

    if (mode & S_IRUSR)
        entryFlags |= QFileSystemMetaData::OwnerReadPermission;
    if (mode & S_IWUSR)
        entryFlags |= QFileSystemMetaData::OwnerWritePermission;
    if (mode & S_IXUSR)
        entryFlags |= QFileSystemMetaData::OwnerExecutePermission;

    if (mode & S_IRGRP)
        entryFlags |= QFileSystemMetaData::GroupReadPermission;
    if (mode & S_IWGRP)
        entryFlags |= QFileSystemMetaData::GroupWritePermission;
    if (mode & S_IXGRP)
        entryFlags |= QFileSystemMetaData::GroupExecutePermission;

    if (mode & S_IROTH)
        entryFlags |= QFileSystemMetaData::OtherReadPermission;
    if (mode & S_IWOTH)
        entryFlags |= QFileSystemMetaData::OtherWritePermission;
    if (mode & S_IXOTH)
        entryFlags |= QFileSystemMetaData::OtherExecutePermission;

    // Type
    Q_ASSERT(!S_ISLNK(mode));   // can only happen with lstat()
    if ((mode & S_IFMT) == S_IFREG)
        entryFlags |= QFileSystemMetaData::FileType;
    else if ((mode & S_IFMT) == S_IFDIR)
        entryFlags |= QFileSystemMetaData::DirectoryType;
    else if ((mode & S_IFMT) != S_IFBLK)    // char devices, sockets, FIFOs
        entryFlags |= QFileSystemMetaData::SequentialType;

    // OS-specific flags
    // Potential flags for the future:
    // UF_APPEND and STATX_ATTR_APPEND
    // UF_COMPRESSED and STATX_ATTR_COMPRESSED
    // UF_IMMUTABLE and STATX_ATTR_IMMUTABLE
    // UF_NODUMP and STATX_ATTR_NODUMP

#if defined(Q_OS_VXWORKS) && __has_include(<dosFsLib.h>)
    if (attributes & DOS_ATTR_RDONLY) {
        // on a DOS FS, stat() always returns 0777 bits set in st_mode
        // when DOS FS is read only the write permissions are removed
        entryFlags &= ~QFileSystemMetaData::OwnerWritePermission;
        entryFlags &= ~QFileSystemMetaData::GroupWritePermission;
        entryFlags &= ~QFileSystemMetaData::OtherWritePermission;
    }
#endif
    return entryFlags;
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 355, as local:qfilesystemengine_unix.cpp:qt_real_statx
#if defined(STATX_BASIC_STATS)
static int qt_real_statx(int fd, const char *pathname, int flags, struct statx *statxBuffer)
{
    unsigned mask = STATX_BASIC_STATS | STATX_BTIME;
    int ret = statx(fd, pathname, flags | AT_NO_AUTOMOUNT, mask, statxBuffer);
    return ret == -1 ? -errno : 0;
}
#endif  // defined(STATX_BASIC_STATS)

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 372, as local:qfilesystemengine_unix.cpp:qt_fstatx
#if defined(STATX_BASIC_STATS)
static int qt_fstatx(int fd, struct statx *statxBuffer)
{
    return qt_real_statx(fd, "", AT_EMPTY_PATH, statxBuffer);
}
#endif  // defined(STATX_BASIC_STATS)

//  from src/corelib/io/qfsfileengine.cpp, line 49, as local:qfsfileengine.cpp:SignedIOType
#if !defined(QT_NO_FSFILEENGINE)
#if defined(Q_OS_WIN)
typedef int SignedIOType;
#endif  // defined(Q_OS_WIN)
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 50, as local:qfsfileengine.cpp:UnsignedIOType
#if !defined(QT_NO_FSFILEENGINE)
#if defined(Q_OS_WIN)
typedef unsigned int UnsignedIOType;
#endif  // defined(Q_OS_WIN)
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine_unix.cpp, line 31, as local:qfsfileengine_unix.cpp:msgOpenDirectory
#if !defined(QT_NO_FSFILEENGINE)
static inline QString msgOpenDirectory()
{
    const char message[] = QT_TRANSLATE_NOOP("QIODevice", "file to open is a directory");
#if QT_CONFIG(translation)
    return QIODevice::tr(message);
#else
    return QLatin1StringView(message);
#endif
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

//  from src/corelib/io/qabstractfileengine.cpp, line 36, as _ZN26QAbstractFileEnginePrivateD2Ev
inline QAbstractFileEnginePrivate::~QAbstractFileEnginePrivate()
    = default;

//  from src/corelib/io/qfilesystemengine_unix.cpp, line 415, as _ZN17QFileSystemEngine12fillMetaDataEiR19QFileSystemMetaData
inline bool QFileSystemEngine::fillMetaData(int fd, QFileSystemMetaData &data)
{
    auto getSizeForBlockDev = [&](mode_t st_mode) {
#ifdef BLKGETSIZE64
        // Linux
        if (quint64 sz; (st_mode & S_IFMT) == S_IFBLK && ioctl(fd, BLKGETSIZE64, &sz) == 0)
            data.size_ = sz;        // returns byte count
#elif defined(BLKGETSIZE)
        // older Linux
        if (ulong sz; (st_mode & S_IFMT) == S_IFBLK && ioctl(fd, BLKGETSIZE, &sz) == 0)
            data.size_ = sz * 512;  // returns 512-byte sector count
#elif defined(DKIOCGETBLOCKCOUNT)
        // Apple Darwin
        qint32 blksz;
        if (quint64 count; (st_mode & S_IFMT) == S_IFBLK
                && ioctl(fd, DKIOCGETBLOCKCOUNT, &count) == 0
                && ioctl(fd, DKIOCGETBLOCKSIZE, &blksz) == 0)
            data.size_ = count * blksz;
#elif defined(DIOCGMEDIASIZE)
        // FreeBSD
        // see Linux-compat implementation in
        // http://fxr.watson.org/fxr/source/compat/linux/linux_ioctl.c?v=FREEBSD-13-STABLE#L282
        // S_IFCHR is correct: FreeBSD doesn't have block devices any more
        if (QT_OFF_T sz; (st_mode & S_IFMT) == S_IFCHR && ioctl(fd, DIOCGMEDIASIZE, &sz) == 0)
            data.size_ = sz;        // returns byte count
#else
        Q_UNUSED(st_mode);
#endif
    };
    data.entryFlags &= ~QFileSystemMetaData::PosixStatFlags;
    data.knownFlagsMask |= QFileSystemMetaData::PosixStatFlags;

    struct statx statxBuffer;

    int ret = qt_fstatx(fd, &statxBuffer);
    if (ret != -ENOSYS) {
        if (ret == 0) {
            data.fillFromStatxBuf(statxBuffer);
            getSizeForBlockDev(statxBuffer.stx_mode);
            return true;
        }
        return false;
    }

    QT_STATBUF statBuffer;

    if (QT_FSTAT(fd, &statBuffer) == 0) {
        data.fillFromStatBuf(statBuffer);
        getSizeForBlockDev(statBuffer.st_mode);
        return true;
    }

    return false;
}

//  from src/corelib/io/qfilesystementry.cpp, line 106, as _ZNK16QFileSystemEntry14nativeFilePathEv
inline QFileSystemEntry::NativePath QFileSystemEntry::nativeFilePath() const
{
    resolveNativeFilePath();
    return m_nativeFilePath;
}

//  from src/corelib/io/qfsfileengine.cpp, line 260, as _ZN20QFSFileEnginePrivate6openFhE6QFlagsIN13QIODeviceBase12OpenModeFlagEEP8_IO_FILE
#if !defined(QT_NO_FSFILEENGINE)
inline bool QFSFileEnginePrivate::openFh(QIODevice::OpenMode openMode, FILE *fh)
{
    Q_ASSERT_X(openMode & QIODevice::Unbuffered, "QFSFileEngine::open",
               "QFSFileEngine no longer supports buffered mode; upper layer must buffer");

    Q_Q(QFSFileEngine);
    this->fh = fh;
    fd = -1;

    // Seek to the end when in Append mode.
    if (openMode & QIODevice::Append) {
        int ret;
        do {
            ret = QT_FSEEK(fh, 0, SEEK_END);
        } while (ret != 0 && errno == EINTR);

        if (ret != 0) {
            q->setError(errno == EMFILE ? QFile::ResourceError : QFile::OpenError,
                        QSystemError::stdString(errno));

            this->openMode = QIODevice::NotOpen;
            this->fh = nullptr;

            return false;
        }
    }

    return true;
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 320, as _ZN20QFSFileEnginePrivate6openFdE6QFlagsIN13QIODeviceBase12OpenModeFlagEEi
#if !defined(QT_NO_FSFILEENGINE)
inline bool QFSFileEnginePrivate::openFd(QIODevice::OpenMode openMode, int fd)
{
    Q_Q(QFSFileEngine);
    this->fd = fd;
    fh = nullptr;

    // Seek to the end when in Append mode.
    if (openMode & QFile::Append) {
        QT_OFF_T ret;
        do {
            ret = QT_LSEEK(fd, 0, SEEK_END);
        } while (ret == -1 && errno == EINTR);

        if (ret == -1) {
            q->setError(errno == EMFILE ? QFile::ResourceError : QFile::OpenError,
                        QSystemError::stdString(errno));

            this->openMode = QIODevice::NotOpen;
            this->fd = -1;

            return false;
        }
    }

    return true;
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 360, as _ZN20QFSFileEnginePrivate9closeFdFhEv
#if !defined(QT_NO_FSFILEENGINE)
inline bool QFSFileEnginePrivate::closeFdFh()
{
    Q_Q(QFSFileEngine);
    if (fd == -1 && !fh)
        return false;

    // Flush the file if it's buffered, and if the last flush didn't fail.
    bool flushed = !fh || (!lastFlushFailed && q->flush());
    bool closed = true;
    tried_stat = 0;

    // Close the file if we created the handle.
    if (closeFileHandle) {
        int ret;

        if (fh) {
            // Close buffered file.
            ret = fclose(fh);
        } else {
            // Close unbuffered file.
            ret = QT_CLOSE(fd);
        }

        // We must reset these guys regardless; calling close again after a
        // failed close causes crashes on some systems.
        fh = nullptr;
        fd = -1;
        closed = (ret == 0);
    }

    // Report errors.
    if (!flushed || !closed) {
        if (flushed) {
            // If not flushed, we want the flush error to fall through.
            q->setError(QFile::UnspecifiedError, QSystemError::stdString(errno));
        }
        return false;
    }

    return true;
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 430, as _ZN20QFSFileEnginePrivate7flushFhEv
#if !defined(QT_NO_FSFILEENGINE)
inline bool QFSFileEnginePrivate::flushFh()
{
    Q_Q(QFSFileEngine);

    // Never try to flush again if the last flush failed. Otherwise you can
    // get crashes on some systems (AIX).
    if (lastFlushFailed)
        return false;

    int ret = fflush(fh);

    lastFlushFailed = (ret != 0);
    lastIOCommand = QFSFileEnginePrivate::IOFlushCommand;

    if (ret != 0) {
        q->setError(errno == ENOSPC ? QFile::ResourceError : QFile::WriteError,
                    QSystemError::stdString(errno));
        return false;
    }
    return true;
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 502, as _ZNK20QFSFileEnginePrivate7posFdFhEv
#if !defined(QT_NO_FSFILEENGINE)
inline qint64 QFSFileEnginePrivate::posFdFh() const
{
    if (fh)
        return qint64(QT_FTELL(fh));
    return QT_LSEEK(fd, 0, SEEK_CUR);
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 540, as _ZN20QFSFileEnginePrivate8seekFdFhEx
#if !defined(QT_NO_FSFILEENGINE)
inline bool QFSFileEnginePrivate::seekFdFh(qint64 pos)
{
    Q_Q(QFSFileEngine);

    // On Windows' stdlib implementation, the results of calling fread and
    // fwrite are undefined if not called either in sequence, or if preceded
    // with a call to fflush().
    if (lastIOCommand != QFSFileEnginePrivate::IOFlushCommand && !q->flush())
        return false;

    if (pos < 0 || pos != qint64(QT_OFF_T(pos)))
        return false;

    if (fh) {
        // Buffered stdlib mode.
        int ret;
        do {
            ret = QT_FSEEK(fh, QT_OFF_T(pos), SEEK_SET);
        } while (ret != 0 && errno == EINTR);

        if (ret != 0) {
            q->setError(QFile::ReadError, QSystemError::stdString(errno));
            return false;
        }
    } else {
        // Unbuffered stdio mode.
        if (QT_LSEEK(fd, QT_OFF_T(pos), SEEK_SET) == -1) {
            q->setError(QFile::PositionError, QSystemError::stdString(errno));
            qWarning("QFile::at: Cannot set file position %lld", pos);
            return false;
        }
    }
    return true;
}
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 682, as _ZN20QFSFileEnginePrivate12readLineFdFhEPcx
#if !defined(QT_NO_FSFILEENGINE)
#if defined(Q_OS_LINUX)
inline qint64 QFSFileEnginePrivate::readLineFdFh(char *data, qint64 maxlen)
{
    Q_Q(QFSFileEngine);
    if (!fh)
        return q->QAbstractFileEngine::readLine(data, maxlen);

    QT_OFF_T oldPos = 0;
#ifdef Q_OS_WIN
    bool seq = q->isSequential();
    if (!seq)
#endif
        oldPos = QT_FTELL(fh);

    // QIODevice::readLine() passes maxlen - 1 to QFile::readLineData()
    // because it has made space for the '\0' at the end of data.  But fgets
    // does the same, so we'd get two '\0' at the end - passing maxlen + 1
    // solves this.
    if (!fgets(data, int(maxlen + 1), fh)) {
        if (!feof(fh)) // Doesn't change errno
            q->setError(QFile::ReadError, QSystemError::stdString(errno));
        return -1;              // error
    }

#ifdef Q_OS_WIN
    if (seq)
        return qstrlen(data);
#endif

    qint64 lineLength = QT_FTELL(fh) - oldPos;
    return lineLength > 0 ? lineLength : qstrlen(data);
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_NO_FSFILEENGINE)

//  from src/corelib/io/qfsfileengine.cpp, line 89, as _ZN20QFSFileEnginePrivate4initEv
#if !defined(QT_NO_FSFILEENGINE)
#if defined(Q_OS_LINUX)
inline void QFSFileEnginePrivate::init()
{
    is_sequential = 0;
    tried_stat = 0;
    need_lstat = 1;
    is_link = 0;
    openMode = QIODevice::NotOpen;
    fd = -1;
    fh = nullptr;
    lastIOCommand = IOFlushCommand;
    lastFlushFailed = false;
    closeFileHandle = false;
#ifdef Q_OS_WIN
    fileAttrib = INVALID_FILE_ATTRIBUTES;
    fileHandle = INVALID_HANDLE_VALUE;
    mapHandle = NULL;
    cachedFd = -1;
#endif
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_NO_FSFILEENGINE)
//  -----------------------------------------------------------------------

//  QFSFileEngine *QFSFileEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFSFileEngine *ritual_ZN20QFSFileEnginePrivate6q_funcEv(
    QFSFileEnginePrivate *self) {
  return self->q_func();
}

//  const QFSFileEngine *QFSFileEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFSFileEngine *ritual_ZNK20QFSFileEnginePrivate6q_funcEv(
    const QFSFileEnginePrivate *self) {
  return self->q_func();
}

#if !defined(QT_NO_FSFILEENGINE)
//  bool QFSFileEnginePrivate::openFh(QIODevice::OpenMode flags, FILE *fh)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFSFileEnginePrivate6openFhE6QFlagsIN13QIODeviceBase12OpenModeFlagEEP8_IO_FILE(
    QFSFileEnginePrivate *self,
    int flags,
    FILE *fh) {
  return self->openFh(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      fh);
}
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
//  bool QFSFileEnginePrivate::openFd(QIODevice::OpenMode flags, int fd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFSFileEnginePrivate6openFdE6QFlagsIN13QIODeviceBase12OpenModeFlagEEi(
    QFSFileEnginePrivate *self,
    int flags,
    int fd) {
  return self->openFd(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      fd);
}
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
//  bool QFSFileEnginePrivate::closeFdFh()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFSFileEnginePrivate9closeFdFhEv(
    QFSFileEnginePrivate *self) {
  return self->closeFdFh();
}
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
//  bool QFSFileEnginePrivate::flushFh()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFSFileEnginePrivate7flushFhEv(QFSFileEnginePrivate *self) {
  return self->flushFh();
}
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
//  qint64 QFSFileEnginePrivate::posFdFh() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK20QFSFileEnginePrivate7posFdFhEv(
    const QFSFileEnginePrivate *self) {
  return self->posFdFh();
}
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
//  bool QFSFileEnginePrivate::seekFdFh(qint64 a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFSFileEnginePrivate8seekFdFhEx(
    QFSFileEnginePrivate *self,
    qint64 a0) {
  return self->seekFdFh(a0);
}
#endif  // !defined(QT_NO_FSFILEENGINE)

#if !defined(QT_NO_FSFILEENGINE)
#if defined(Q_OS_LINUX)
//  qint64 QFSFileEnginePrivate::readLineFdFh(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN20QFSFileEnginePrivate12readLineFdFhEPcx(
    QFSFileEnginePrivate *self,
    char *data,
    qint64 maxlen) {
  return self->readLineFdFh(data, maxlen);
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_NO_FSFILEENGINE)

//  bool QFSFileEnginePrivate::openModeCanCreate(QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFSFileEnginePrivate17openModeCanCreateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    int openMode) {
  return QFSFileEnginePrivate::openModeCanCreate(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

#if defined(Q_OS_UNIX)
//  int QFSFileEnginePrivate::openModeToOpenFlags(QIODevice::OpenMode mode)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QFSFileEnginePrivate19openModeToOpenFlagsE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    int mode) {
  return QFSFileEnginePrivate::openModeToOpenFlags(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(mode));
}
#endif  // defined(Q_OS_UNIX)

#if !defined(QT_NO_FSFILEENGINE)
#if defined(Q_OS_LINUX)
//  void QFSFileEnginePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFSFileEnginePrivate4initEv(QFSFileEnginePrivate *self) {
  self->init();
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_NO_FSFILEENGINE)

//  QFSFileEnginePrivate::~QFSFileEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFSFileEnginePrivateD1Ev(QFSFileEnginePrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_FSFILEENGINE)
