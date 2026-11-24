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

//  from src/corelib/io/qfilesystementry.cpp, line 46, as _ZN16QFileSystemEntryC1Ev
inline QFileSystemEntry::QFileSystemEntry()
    : m_lastSeparator(-1),
    m_firstDotInFileName(-1),
    m_lastDotInFileName(-1)
{
}

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
