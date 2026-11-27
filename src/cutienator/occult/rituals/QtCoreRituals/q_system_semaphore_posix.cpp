//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-27: code taken from Qt's source no longer stands under
//  defined(Q_OS_LINUX), which Qt does not write there; its rituals no longer
//  stand under defined(Q_OS_LINUX), as the code taken from Qt they call no
//  longer does. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsystemsemaphore.h>
#include <QtCore/private/qsystemsemaphore_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/q20memory.h>
#include <errno.h>
#endif
#include <QtCore/qsystemsemaphore.h>
#include <QtCore/private/qsystemsemaphore_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtCore/qcoreapplication.h>
#if QT_CONFIG(posix_sem)
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>
#ifdef Q_OS_UNIX
#  include <QtCore/private/qcore_unix_p.h>
#else
#endif
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

using namespace Qt::StringLiterals;

//  from src/corelib/ipc/qsystemsemaphore.cpp, line 342, as _ZN23QSystemSemaphorePrivate18setUnixErrorStringE13QLatin1String
#if QT_CONFIG(systemsemaphore)
inline void QSystemSemaphorePrivate::setUnixErrorString(QLatin1StringView function)
{
    // EINVAL is handled in functions so they can give better error strings
    switch (errno) {
    case EPERM:
    case EACCES:
        errorString = QSystemSemaphore::tr("%1: permission denied").arg(function);
        error = QSystemSemaphore::PermissionDenied;
        break;
    case EEXIST:
        errorString = QSystemSemaphore::tr("%1: already exists").arg(function);
        error = QSystemSemaphore::AlreadyExists;
        break;
    case ENOENT:
        errorString = QSystemSemaphore::tr("%1: does not exist").arg(function);
        error = QSystemSemaphore::NotFound;
        break;
    case ERANGE:
    case ENOSPC:
    case EMFILE:
        errorString = QSystemSemaphore::tr("%1: out of resources").arg(function);
        error = QSystemSemaphore::OutOfResources;
        break;
    case ENAMETOOLONG:
        errorString = QSystemSemaphore::tr("%1: key too long").arg(function);
        error = QSystemSemaphore::KeyError;
        break;
    default:
        errorString = QSystemSemaphore::tr("%1: unknown error: %2")
                .arg(function, qt_error_string(errno));
        error = QSystemSemaphore::UnknownError;
#if defined QSYSTEMSEMAPHORE_DEBUG
        qDebug() << errorString << "key" << key << "errno" << errno << EINVAL;
#endif
    }
}
#endif  // QT_CONFIG(systemsemaphore)

//  from src/corelib/ipc/qsystemsemaphore_posix.cpp, line 39, as _ZN21QSystemSemaphorePosix19runtimeSupportCheckEv
#if QT_CONFIG(posix_sem)
inline bool QSystemSemaphorePosix::runtimeSupportCheck()
{
    static const bool result = []() {
        sem_open("/", 0, 0, 0);     // this WILL fail
        return errno != ENOSYS;
    }();
    return result;
}
#endif  // QT_CONFIG(posix_sem)

//  from src/corelib/ipc/qsystemsemaphore_posix.cpp, line 48, as _ZN21QSystemSemaphorePosix6handleEP23QSystemSemaphorePrivateN16QSystemSemaphore10AccessModeE
#if QT_CONFIG(posix_sem)
inline bool QSystemSemaphorePosix::handle(QSystemSemaphorePrivate *self, QSystemSemaphore::AccessMode mode)
{
    if (semaphore != SEM_FAILED)
        return true;  // we already have a semaphore

    const QByteArray semName = QFile::encodeName(self->nativeKey.nativeKey());
    if (semName.isEmpty()) {
        self->setError(QSystemSemaphore::KeyError,
                       QSystemSemaphore::tr("%1: key is empty")
                       .arg("QSystemSemaphore::handle"_L1));
        return false;
    }

    // Always try with O_EXCL so we know whether we created the semaphore.
    int oflag = O_CREAT | O_EXCL;
    for (int tryNum = 0, maxTries = 1; tryNum < maxTries; ++tryNum) {
        do {
            semaphore = ::sem_open(semName.constData(), oflag, 0600, self->initialValue);
        } while (semaphore == SEM_FAILED && errno == EINTR);
        if (semaphore == SEM_FAILED && errno == EEXIST) {
            if (mode == QSystemSemaphore::Create) {
                if (::sem_unlink(semName.constData()) == -1 && errno != ENOENT) {
                    self->setUnixErrorString("QSystemSemaphore::handle (sem_unlink)"_L1);
                    return false;
                }
                // Race condition: the semaphore might be recreated before
                // we call sem_open again, so we'll retry several times.
                maxTries = 3;
            } else {
                // Race condition: if it no longer exists at the next sem_open
                // call, we won't realize we created it, so we'll leak it later.
                oflag &= ~O_EXCL;
                maxTries = 2;
            }
        } else {
            break;
        }
    }

    if (semaphore == SEM_FAILED) {
        self->setUnixErrorString("QSystemSemaphore::handle"_L1);
        return false;
    }

    createdSemaphore = (oflag & O_EXCL) != 0;

    return true;
}
#endif  // QT_CONFIG(posix_sem)

//  from src/corelib/ipc/qsystemsemaphore_posix.cpp, line 97, as _ZN21QSystemSemaphorePosix11cleanHandleEP23QSystemSemaphorePrivate
#if QT_CONFIG(posix_sem)
inline void QSystemSemaphorePosix::cleanHandle(QSystemSemaphorePrivate *self)
{
    if (semaphore != SEM_FAILED) {
        if (::sem_close(semaphore) == -1) {
            self->setUnixErrorString("QSystemSemaphore::cleanHandle (sem_close)"_L1);
#if defined QSYSTEMSEMAPHORE_DEBUG
            qDebug("QSystemSemaphore::cleanHandle sem_close failed.");
#endif
        }
        semaphore = SEM_FAILED;
    }

    if (createdSemaphore) {
        const QByteArray semName = QFile::encodeName(self->nativeKey.nativeKey());
        if (::sem_unlink(semName) == -1 && errno != ENOENT) {
            self->setUnixErrorString("QSystemSemaphore::cleanHandle (sem_unlink)"_L1);
#if defined QSYSTEMSEMAPHORE_DEBUG
            qDebug("QSystemSemaphorePosix::cleanHandle sem_unlink failed.");
#endif
        }
        createdSemaphore = false;
    }
}
#endif  // QT_CONFIG(posix_sem)

//  from src/corelib/ipc/qsystemsemaphore_posix.cpp, line 121, as _ZN21QSystemSemaphorePosix15modifySemaphoreEP23QSystemSemaphorePrivatei
#if QT_CONFIG(posix_sem)
inline bool QSystemSemaphorePosix::modifySemaphore(QSystemSemaphorePrivate *self, int count)
{
    if (!handle(self, QSystemSemaphore::Open))
        return false;

    if (count > 0) {
        int cnt = count;
        do {
            if (::sem_post(semaphore) == -1) {
#if defined(Q_OS_VXWORKS)
                if (errno == EINVAL) {
                    semaphore = SEM_FAILED;
                    return modifySemaphore(self, cnt);
                }
#endif
                self->setUnixErrorString("QSystemSemaphore::modifySemaphore (sem_post)"_L1);
#if defined QSYSTEMSEMAPHORE_DEBUG
                qDebug("QSystemSemaphorePosix::modify sem_post failed %d %d", count, errno);
#endif
                // rollback changes to preserve the SysV semaphore behavior
                for ( ; cnt < count; ++cnt) {
                    int res;
                    QT_EINTR_LOOP(res, ::sem_wait(semaphore));
                }
                return false;
            }
            --cnt;
        } while (cnt > 0);
    } else {
        int res;
        QT_EINTR_LOOP(res, ::sem_wait(semaphore));
        if (res == -1) {
            // If the semaphore was removed be nice and create it and then modifySemaphore again
            if (errno == EINVAL || errno == EIDRM) {
                semaphore = SEM_FAILED;
                return modifySemaphore(self, count);
            }
            self->setUnixErrorString("QSystemSemaphore::modifySemaphore (sem_wait)"_L1);
#if defined QSYSTEMSEMAPHORE_DEBUG
            qDebug("QSystemSemaphorePosix::modify sem_wait failed %d %d", count, errno);
#endif
            return false;
        }
    }

    self->clearError();
    return true;
}
#endif  // QT_CONFIG(posix_sem)
//  -----------------------------------------------------------------------

//  bool QSystemSemaphorePosix::supports(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSystemSemaphorePosix8supportsEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSystemSemaphorePosix::supports(type);
}

#if QT_CONFIG(posix_sem)
//  bool QSystemSemaphorePosix::runtimeSupportCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSystemSemaphorePosix19runtimeSupportCheckEv() {
  return QSystemSemaphorePosix::runtimeSupportCheck();
}
#endif  // QT_CONFIG(posix_sem)

#if QT_CONFIG(posix_sem)
#if QT_CONFIG(systemsemaphore)
//  bool QSystemSemaphorePosix::handle(QSystemSemaphorePrivate *self_,
//      QSystemSemaphore::AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSystemSemaphorePosix6handleEP23QSystemSemaphorePrivateN16QSystemSemaphore10AccessModeE(
    QSystemSemaphorePosix *self,
    QSystemSemaphorePrivate *self_,
    QSystemSemaphore::AccessMode mode) {
  return self->handle(self_, mode);
}
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(posix_sem)

#if QT_CONFIG(posix_sem)
#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePosix::cleanHandle(QSystemSemaphorePrivate *self_)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSystemSemaphorePosix11cleanHandleEP23QSystemSemaphorePrivate(
    QSystemSemaphorePosix *self,
    QSystemSemaphorePrivate *self_) {
  self->cleanHandle(self_);
}
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(posix_sem)

#if QT_CONFIG(posix_sem)
#if QT_CONFIG(systemsemaphore)
//  bool QSystemSemaphorePosix::modifySemaphore(QSystemSemaphorePrivate
//      *self_, int count)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSystemSemaphorePosix15modifySemaphoreEP23QSystemSemaphorePrivatei(
    QSystemSemaphorePosix *self,
    QSystemSemaphorePrivate *self_,
    int count) {
  return self->modifySemaphore(self_, count);
}
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(posix_sem)

//  QSystemSemaphorePosix::~QSystemSemaphorePosix()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSystemSemaphorePosixD1Ev(QSystemSemaphorePosix *self) {
  delete self;
}

#endif  // QT_CONFIG(systemsemaphore)
