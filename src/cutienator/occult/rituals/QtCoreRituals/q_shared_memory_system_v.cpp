//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(sharedmemory)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsharedmemory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qtipccommon.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsharedmemory.h>
#include <QtCore/private/qsharedmemory_p.h>
#include <QtCore/private/qtipccommon_p.h>
#include <QtCore/qsystemsemaphore.h>
#include <QtCore/q20memory.h>
#include <QtCore/qdebug.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#include <errno.h>
#include <QtCore/qsharedmemory.h>
#include <QtCore/private/qsharedmemory_p.h>
#include <QtCore/private/qtipccommon_p.h>
#include <QtCore/qdir.h>
#include <QtCore/qdebug.h>
#include <errno.h>
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/mman.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <QtCore/private/qcore_unix_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/private/qcore_mac_p.h>
#endif
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

//  from src/corelib/ipc/qsharedmemory.cpp, line 646, as _ZN20QSharedMemoryPrivate18setUnixErrorStringE13QLatin1String
#if QT_CONFIG(sharedmemory)
inline void QSharedMemoryPrivate::setUnixErrorString(QLatin1StringView function)
{
    // EINVAL is handled in functions so they can give better error strings
    switch (errno) {
    case EACCES:
        errorString = QSharedMemory::tr("%1: permission denied").arg(function);
        error = QSharedMemory::PermissionDenied;
        break;
    case EEXIST:
        errorString = QSharedMemory::tr("%1: already exists").arg(function);
        error = QSharedMemory::AlreadyExists;
        break;
    case ENOENT:
        errorString = QSharedMemory::tr("%1: doesn't exist").arg(function);
        error = QSharedMemory::NotFound;
        break;
    case EMFILE:
    case ENOMEM:
    case ENOSPC:
        errorString = QSharedMemory::tr("%1: out of resources").arg(function);
        error = QSharedMemory::OutOfResources;
        break;
    default:
        errorString = QSharedMemory::tr("%1: unknown error: %2")
                .arg(function, qt_error_string(errno));
        error = QSharedMemory::UnknownError;
#if defined QSHAREDMEMORY_DEBUG
        qDebug() << errorString << "key" << key << "errno" << errno << EINVAL;
#endif
    }
}
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_systemv.cpp, line 35, as _ZN20QSharedMemorySystemV19runtimeSupportCheckEv
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
#if defined(Q_OS_LINUX)
inline bool QSharedMemorySystemV::runtimeSupportCheck()
{
#if defined(Q_OS_DARWIN)
    if (qt_apple_isSandboxed())
        return false;
#endif
    static const bool result = []() {
        (void)shmget(IPC_PRIVATE, ~size_t(0), 0);     // this will fail
        return errno != ENOSYS;
    }();
    return result;
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_systemv.cpp, line 61, as _ZN20QSharedMemorySystemV6handleEP20QSharedMemoryPrivate
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
inline key_t QSharedMemorySystemV::handle(QSharedMemoryPrivate *self)
{
    // already made
    if (unix_key)
        return unix_key;

    // don't allow making handles on empty keys
    if (nativeKeyFile.isEmpty())
        updateNativeKeyFile(self->nativeKey);
    if (nativeKeyFile.isEmpty()) {
        self->setError(QSharedMemory::KeyError,
                       QSharedMemory::tr("%1: key is empty")
                       .arg("QSharedMemory::handle:"_L1));
        return 0;
    }

    unix_key = ftok(nativeKeyFile, int(self->nativeKey.type()));
    if (unix_key < 0) {
        self->setUnixErrorString("QSharedMemory::handle"_L1);
        nativeKeyFile.clear();
        unix_key = 0;
    }
    return unix_key;
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_systemv.cpp, line 86, as _ZN20QSharedMemorySystemV11cleanHandleEP20QSharedMemoryPrivate
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
inline bool QSharedMemorySystemV::cleanHandle(QSharedMemoryPrivate *self)
{
    if (unix_key == 0)
        return true;

    // Get the number of current attachments
    struct shmid_ds shmid_ds;
    QByteArray keyfile = std::exchange(nativeKeyFile, QByteArray());

    int id = shmget(unix_key, 0, 0400);
    unix_key = 0;
    if (shmctl(id, IPC_STAT, &shmid_ds))
        return errno != EINVAL;

    // If there are still attachments, keep the keep file and shm
    if (shmid_ds.shm_nattch != 0)
        return true;

    if (shmctl(id, IPC_RMID, &shmid_ds) < 0) {
        if (errno != EINVAL) {
            self->setUnixErrorString("QSharedMemory::remove"_L1);
            return false;
        }
    };

    // remove file
    return unlink(keyfile) == 0;
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_systemv.cpp, line 158, as _ZN20QSharedMemorySystemV6attachEP20QSharedMemoryPrivateN13QSharedMemory10AccessModeE
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
inline bool QSharedMemorySystemV::attach(QSharedMemoryPrivate *self, QSharedMemory::AccessMode mode)
{
    // grab the shared memory segment id
    int id = shmget(unix_key, 0, (mode == QSharedMemory::ReadOnly ? 0400 : 0600));
    if (-1 == id) {
        self->setUnixErrorString("QSharedMemory::attach (shmget)"_L1);
        unix_key = 0;
        nativeKeyFile.clear();
        return false;
    }

    // grab the memory
    self->memory = shmat(id, nullptr, (mode == QSharedMemory::ReadOnly ? SHM_RDONLY : 0));
    if (self->memory == MAP_FAILED) {
        self->memory = nullptr;
        self->setUnixErrorString("QSharedMemory::attach (shmat)"_L1);
        return false;
    }

    // grab the size
    shmid_ds shmid_ds;
    if (!shmctl(id, IPC_STAT, &shmid_ds)) {
        self->size = (qsizetype)shmid_ds.shm_segsz;
    } else {
        self->setUnixErrorString("QSharedMemory::attach (shmctl)"_L1);
        return false;
    }

    return true;
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_systemv.cpp, line 189, as _ZN20QSharedMemorySystemV6detachEP20QSharedMemoryPrivate
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
inline bool QSharedMemorySystemV::detach(QSharedMemoryPrivate *self)
{
    // detach from the memory segment
    if (shmdt(self->memory) < 0) {
        const auto function = "QSharedMemory::detach"_L1;
        switch (errno) {
        case EINVAL:
            self->setError(QSharedMemory::NotFound,
                           QSharedMemory::tr("%1: not attached").arg(function));
            break;
        default:
            self->setUnixErrorString(function);
        }
        return false;
    }
    self->memory = nullptr;
    self->size = 0;

    return cleanHandle(self);
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_systemv.cpp, line 49, as _ZN20QSharedMemorySystemV19updateNativeKeyFileERK13QNativeIpcKey
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
inline void QSharedMemorySystemV::updateNativeKeyFile(const QNativeIpcKey &nativeKey)
{
    Q_ASSERT(nativeKeyFile.isEmpty() );
    if (!nativeKey.nativeKey().isEmpty())
        nativeKeyFile = QFile::encodeName(nativeKey.nativeKey());
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)
//  -----------------------------------------------------------------------

//  bool QSharedMemorySystemV::supports(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemorySystemV8supportsEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSharedMemorySystemV::supports(type);
}

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(sysv_shm)
#if defined(Q_OS_LINUX)
//  bool QSharedMemorySystemV::runtimeSupportCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemorySystemV19runtimeSupportCheckEv() {
  return QSharedMemorySystemV::runtimeSupportCheck();
}
#endif  // defined(Q_OS_LINUX)
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sysv_shm)
#if QT_CONFIG(sharedmemory)
//  key_t QSharedMemorySystemV::handle(QSharedMemoryPrivate *self_)
extern "C" Q_DECL_EXPORT
key_t *ritual_ZN20QSharedMemorySystemV6handleEP20QSharedMemoryPrivate(
    QSharedMemorySystemV *self,
    QSharedMemoryPrivate *self_) {
  return new key_t(self->handle(self_));
}
#endif  // QT_CONFIG(sharedmemory)
#endif  // QT_CONFIG(sysv_shm)

#if QT_CONFIG(sysv_shm)
#if QT_CONFIG(sharedmemory)
//  bool QSharedMemorySystemV::cleanHandle(QSharedMemoryPrivate *self_)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemorySystemV11cleanHandleEP20QSharedMemoryPrivate(
    QSharedMemorySystemV *self,
    QSharedMemoryPrivate *self_) {
  return self->cleanHandle(self_);
}
#endif  // QT_CONFIG(sharedmemory)
#endif  // QT_CONFIG(sysv_shm)

#if QT_CONFIG(sysv_shm)
#if QT_CONFIG(sharedmemory)
//  bool QSharedMemorySystemV::attach(QSharedMemoryPrivate *self_,
//      QSharedMemory::AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemorySystemV6attachEP20QSharedMemoryPrivateN13QSharedMemory10AccessModeE(
    QSharedMemorySystemV *self,
    QSharedMemoryPrivate *self_,
    QSharedMemory::AccessMode mode) {
  return self->attach(self_, mode);
}
#endif  // QT_CONFIG(sharedmemory)
#endif  // QT_CONFIG(sysv_shm)

#if QT_CONFIG(sysv_shm)
#if QT_CONFIG(sharedmemory)
//  bool QSharedMemorySystemV::detach(QSharedMemoryPrivate *self_)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemorySystemV6detachEP20QSharedMemoryPrivate(
    QSharedMemorySystemV *self,
    QSharedMemoryPrivate *self_) {
  return self->detach(self_);
}
#endif  // QT_CONFIG(sharedmemory)
#endif  // QT_CONFIG(sysv_shm)

#if QT_CONFIG(sysv_shm)
#if QT_CONFIG(sharedmemory)
//  void QSharedMemorySystemV::updateNativeKeyFile(const QNativeIpcKey
//      &nativeKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemorySystemV19updateNativeKeyFileERK13QNativeIpcKey(
    QSharedMemorySystemV *self,
    const QNativeIpcKey *nativeKey) {
  self->updateNativeKeyFile(*nativeKey);
}
#endif  // QT_CONFIG(sharedmemory)
#endif  // QT_CONFIG(sysv_shm)

//  QSharedMemorySystemV::~QSharedMemorySystemV()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemorySystemVD1Ev(QSharedMemorySystemV *self) {
  delete self;
}

//  a key_t a ritual of QSharedMemorySystemV gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSharedMemorySystemV__key_t(key_t *self) {
  delete self;
}

#endif  // QT_CONFIG(sharedmemory)
