//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtCore/qsystemsemaphore.h>
#include <QtCore/private/qsystemsemaphore_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtCore/qcoreapplication.h>
#if QT_CONFIG(sysv_sem)
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <fcntl.h>
#include <errno.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/private/qcore_mac_p.h>
#endif
#include <QtCore/private/qcore_unix_p.h>
#endif
#include <QtCore/qsystemsemaphore.h>
#include <QtCore/private/qsystemsemaphore_p.h>
#if QT_CONFIG(systemsemaphore)
#include <QtCore/q20memory.h>
#include <errno.h>
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

//  from src/corelib/ipc/qsystemsemaphore_systemv.cpp, line 55, as _ZN23QSystemSemaphoreSystemV6handleEP23QSystemSemaphorePrivateN16QSystemSemaphore10AccessModeE
#if QT_CONFIG(sysv_sem)
#if defined(Q_OS_LINUX)
inline key_t QSystemSemaphoreSystemV::handle(QSystemSemaphorePrivate *self, QSystemSemaphore::AccessMode mode)
{
    if (unix_key != -1)
        return unix_key;  // we already have a semaphore

#if defined(Q_OS_DARWIN)
    if (qt_apple_isSandboxed()) {
        // attempting to use System V semaphores will get us a SIGSYS
        self->setError(QSystemSemaphore::PermissionDenied,
                       QSystemSemaphore::tr("%1: System V semaphores are not available for "
                                            "sandboxed applications. Please build Qt with "
                                            "-feature-ipc_posix")
                       .arg("QSystemSemaphore::handle:"_L1));
        return -1;
    }
#endif

    nativeKeyFile = QFile::encodeName(self->nativeKey.nativeKey());
    if (nativeKeyFile.isEmpty()) {
        self->setError(QSystemSemaphore::KeyError,
                       QSystemSemaphore::tr("%1: key is empty")
                       .arg("QSystemSemaphore::handle:"_L1));
        return -1;
    }

    // ftok requires that an actual file exists somewhere
    int built = QtIpcCommon::createUnixKeyFile(nativeKeyFile);
    if (-1 == built) {
        self->setError(QSystemSemaphore::KeyError,
                       QSystemSemaphore::tr("%1: unable to make key")
                       .arg("QSystemSemaphore::handle:"_L1));

        return -1;
    }
    createdFile = (1 == built);

    // Get the unix key for the created file
    unix_key = ftok(nativeKeyFile, int(self->nativeKey.type()));
    if (-1 == unix_key) {
        self->setError(QSystemSemaphore::KeyError,
                       QSystemSemaphore::tr("%1: ftok failed")
                       .arg("QSystemSemaphore::handle:"_L1));
        return -1;
    }

    // Get semaphore
    semaphore = semget(unix_key, 1, 0600 | IPC_CREAT | IPC_EXCL);
    if (-1 == semaphore) {
        if (errno == EEXIST)
            semaphore = semget(unix_key, 1, 0600 | IPC_CREAT);
        if (-1 == semaphore) {
            self->setUnixErrorString("QSystemSemaphore::handle"_L1);
            cleanHandle(self);
            return -1;
        }
    } else {
        createdSemaphore = true;
        // Force cleanup of file, it is possible that it can be left over from a crash
        createdFile = true;
    }

    if (mode == QSystemSemaphore::Create) {
        createdSemaphore = true;
        createdFile = true;
    }

    // Created semaphore so initialize its value.
    if (createdSemaphore && self->initialValue >= 0) {
        qt_semun init_op;
        init_op.val = self->initialValue;
        if (-1 == semctl(semaphore, 0, SETVAL, init_op)) {
            self->setUnixErrorString("QSystemSemaphore::handle"_L1);
            cleanHandle(self);
            return -1;
        }
    }

    return unix_key;
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(sysv_sem)

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

//  from src/corelib/ipc/qsystemsemaphore_systemv.cpp, line 140, as _ZN23QSystemSemaphoreSystemV11cleanHandleEP23QSystemSemaphorePrivate
#if QT_CONFIG(sysv_sem)
inline void QSystemSemaphoreSystemV::cleanHandle(QSystemSemaphorePrivate *self)
{
    unix_key = -1;

    // remove the file if we made it
    if (createdFile) {
        unlink(nativeKeyFile.constData());
        createdFile = false;
    }

    if (createdSemaphore) {
        if (-1 != semaphore) {
            if (-1 == semctl(semaphore, 0, IPC_RMID, 0)) {
                self->setUnixErrorString("QSystemSemaphore::cleanHandle"_L1);
#if defined QSYSTEMSEMAPHORE_DEBUG
                qDebug("QSystemSemaphoreSystemV::cleanHandle semctl failed.");
#endif
            }
            semaphore = -1;
        }
        createdSemaphore = false;
    }
}
#endif  // QT_CONFIG(sysv_sem)

//  from src/corelib/ipc/qsystemsemaphore_posix.cpp, line 121, as _ZN21QSystemSemaphorePosix15modifySemaphoreEP23QSystemSemaphorePrivatei
#if QT_CONFIG(posix_sem)
#if defined(Q_OS_LINUX)
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
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(posix_sem)

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

//  from src/corelib/ipc/qsystemsemaphore.cpp, line 17, as _ZN23QSystemSemaphorePrivate16constructBackendEv
#if QT_CONFIG(systemsemaphore)
inline void QSystemSemaphorePrivate::constructBackend()
{
    visit([](auto p) { q20::construct_at(p); });
}
#endif  // QT_CONFIG(systemsemaphore)

//  from src/corelib/ipc/qsystemsemaphore.cpp, line 22, as _ZN23QSystemSemaphorePrivate15destructBackendEv
#if QT_CONFIG(systemsemaphore)
inline void QSystemSemaphorePrivate::destructBackend()
{
    visit([](auto p) { std::destroy_at(p); });
}
#endif  // QT_CONFIG(systemsemaphore)
//  -----------------------------------------------------------------------

#if QT_CONFIG(systemsemaphore)
//  QSystemSemaphorePrivate::QSystemSemaphorePrivate(QNativeIpcKey::Type
//      type)
extern "C" Q_DECL_EXPORT
QSystemSemaphorePrivate *ritual_ZN23QSystemSemaphorePrivateC1EN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return new QSystemSemaphorePrivate(type);
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  QSystemSemaphorePrivate::~QSystemSemaphorePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivateD1Ev(QSystemSemaphorePrivate *self) {
  delete self;
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePrivate::setUnixErrorString(QLatin1StringView
//      function)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate18setUnixErrorStringE13QLatin1String(
    QSystemSemaphorePrivate *self,
    const QLatin1String *function) {
  self->setUnixErrorString(*function);
}
#endif  // QT_CONFIG(systemsemaphore)

//  void
//      QSystemSemaphorePrivate::setError(QSystemSemaphore::SystemSemaphoreEr
//      ror e, const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate8setErrorEN16QSystemSemaphore20SystemSemaphoreErrorERK7QString(
    QSystemSemaphorePrivate *self,
    QSystemSemaphore::SystemSemaphoreError e,
    const QString *message) {
  self->setError(e, *message);
}

//  void QSystemSemaphorePrivate::clearError()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate10clearErrorEv(
    QSystemSemaphorePrivate *self) {
  self->clearError();
}

#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePrivate::constructBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate16constructBackendEv(
    QSystemSemaphorePrivate *self) {
  self->constructBackend();
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphorePrivate::destructBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate15destructBackendEv(
    QSystemSemaphorePrivate *self) {
  self->destructBackend();
}
#endif  // QT_CONFIG(systemsemaphore)

#if QT_CONFIG(posix_sem)
#if QT_CONFIG(systemsemaphore)
#if QT_CONFIG(sysv_sem)
#if defined(Q_OS_LINUX)
//  void QSystemSemaphorePrivate::handle(QSystemSemaphore::AccessMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate6handleEN16QSystemSemaphore10AccessModeE(
    QSystemSemaphorePrivate *self,
    QSystemSemaphore::AccessMode mode) {
  self->handle(mode);
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(sysv_sem)
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(posix_sem)

#if QT_CONFIG(posix_sem)
#if QT_CONFIG(systemsemaphore)
#if QT_CONFIG(sysv_sem)
//  void QSystemSemaphorePrivate::cleanHandle()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphorePrivate11cleanHandleEv(
    QSystemSemaphorePrivate *self) {
  self->cleanHandle();
}
#endif  // QT_CONFIG(sysv_sem)
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(posix_sem)

#endif  // QT_CONFIG(systemsemaphore)
