//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsystemsemaphore_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: the ritual dropping a 'key_t' stands
//  under 'QT_CONFIG(sysv_sem)', as the ritual of 'handle' that gives one
//  does: Windows has no 'key_t' and no System V semaphores. Kept as it
//  is when the generator runs again.
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

//  from src/corelib/ipc/qsystemsemaphore_systemv.cpp, line 37, as _ZN23QSystemSemaphoreSystemV19runtimeSupportCheckEv
#if QT_CONFIG(sysv_sem)
#if defined(Q_OS_LINUX)
inline bool QSystemSemaphoreSystemV::runtimeSupportCheck()
{
#if defined(Q_OS_DARWIN)
    if (qt_apple_isSandboxed())
        return false;
#endif
    static const bool result = []() {
        (void)semget(IPC_PRIVATE, -1, 0);     // this will fail
        return errno != ENOSYS;
    }();
    return result;
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(sysv_sem)

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
//  -----------------------------------------------------------------------

//  bool QSystemSemaphoreSystemV::supports(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QSystemSemaphoreSystemV8supportsEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSystemSemaphoreSystemV::supports(type);
}

#if QT_CONFIG(sysv_sem)
#if defined(Q_OS_LINUX)
//  bool QSystemSemaphoreSystemV::runtimeSupportCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QSystemSemaphoreSystemV19runtimeSupportCheckEv() {
  return QSystemSemaphoreSystemV::runtimeSupportCheck();
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(sysv_sem)

#if QT_CONFIG(sysv_sem)
#if QT_CONFIG(systemsemaphore)
#if defined(Q_OS_LINUX)
//  key_t QSystemSemaphoreSystemV::handle(QSystemSemaphorePrivate *self_,
//      QSystemSemaphore::AccessMode mode)
extern "C" Q_DECL_EXPORT
key_t *ritual_ZN23QSystemSemaphoreSystemV6handleEP23QSystemSemaphorePrivateN16QSystemSemaphore10AccessModeE(
    QSystemSemaphoreSystemV *self,
    QSystemSemaphorePrivate *self_,
    QSystemSemaphore::AccessMode mode) {
  return new key_t(self->handle(self_, mode));
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(sysv_sem)

#if QT_CONFIG(sysv_sem)
#if QT_CONFIG(systemsemaphore)
//  void QSystemSemaphoreSystemV::cleanHandle(QSystemSemaphorePrivate *self_)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphoreSystemV11cleanHandleEP23QSystemSemaphorePrivate(
    QSystemSemaphoreSystemV *self,
    QSystemSemaphorePrivate *self_) {
  self->cleanHandle(self_);
}
#endif  // QT_CONFIG(systemsemaphore)
#endif  // QT_CONFIG(sysv_sem)

//  QSystemSemaphoreSystemV::~QSystemSemaphoreSystemV()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphoreSystemVD1Ev(QSystemSemaphoreSystemV *self) {
  delete self;
}

#if QT_CONFIG(sysv_sem)
//  a key_t a ritual of QSystemSemaphoreSystemV gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSystemSemaphoreSystemV__key_t(key_t *self) {
  delete self;
}
#endif  // QT_CONFIG(sysv_sem)

#endif  // QT_CONFIG(systemsemaphore)
