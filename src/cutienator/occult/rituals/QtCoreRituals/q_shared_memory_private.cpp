//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-27: code taken from Qt's source no longer stands under
//  defined(Q_OS_LINUX), which Qt does not write there; its rituals no longer
//  stand under defined(Q_OS_LINUX), as the code taken from Qt they call no
//  longer does. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(sharedmemory)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qsharedmemory.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsharedmemory_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlatin1stringview.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsharedmemory.h>
#include <QtCore/private/qsharedmemory_p.h>
#include <QtCore/private/qtipccommon_p.h>
#include <QtCore/qfile.h>
#include <errno.h>
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <QtCore/private/qcore_unix_p.h>
#endif
#endif
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

//  from src/corelib/ipc/qsharedmemory_posix.cpp, line 50, as _ZN18QSharedMemoryPosix11cleanHandleEP20QSharedMemoryPrivate
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
inline bool QSharedMemoryPosix::cleanHandle(QSharedMemoryPrivate *)
{
    if (hand != -1)
        qt_safe_close(hand);
    hand = -1;

    return true;
}
#endif  // QT_CONFIG(posix_shm)
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

//  from src/corelib/ipc/qsharedmemory_posix.cpp, line 38, as _ZN18QSharedMemoryPosix6handleEP20QSharedMemoryPrivate
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
inline bool QSharedMemoryPosix::handle(QSharedMemoryPrivate *self)
{
    // don't allow making handles on empty keys
    if (self->nativeKey.isEmpty()) {
        self->setError(QSharedMemory::KeyError,
                       QSharedMemory::tr("%1: key is empty").arg("QSharedMemory::handle"_L1));
        return false;
    }

    return true;
}
#endif  // QT_CONFIG(posix_shm)
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

//  from src/corelib/ipc/qsharedmemory_posix.cpp, line 59, as _ZN18QSharedMemoryPosix6createEP20QSharedMemoryPrivatex
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
inline bool QSharedMemoryPosix::create(QSharedMemoryPrivate *self, qsizetype size)
{
    if (!handle(self))
        return false;

    const QByteArray shmName = QFile::encodeName(self->nativeKey.nativeKey());

    int fd;
    QT_EINTR_LOOP(fd, ::shm_open(shmName.constData(), O_RDWR | O_CREAT | O_EXCL, 0600));
    if (fd == -1) {
        const int errorNumber = errno;
        const auto function = "QSharedMemory::attach (shm_open)"_L1;
        switch (errorNumber) {
        case EINVAL:
            self->setError(QSharedMemory::KeyError,
                           QSharedMemory::tr("%1: bad name").arg(function));
            break;
        default:
            self->setUnixErrorString(function);
        }
        return false;
    }

    // the size may only be set once
    int ret;
    QT_EINTR_LOOP(ret, QT_FTRUNCATE(fd, size));
    if (ret == -1) {
        self->setUnixErrorString("QSharedMemory::create (ftruncate)"_L1);
        qt_safe_close(fd);
        return false;
    }

    qt_safe_close(fd);

    return true;
}
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory_posix.cpp, line 96, as _ZN18QSharedMemoryPosix6attachEP20QSharedMemoryPrivateN13QSharedMemory10AccessModeE
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
inline bool QSharedMemoryPosix::attach(QSharedMemoryPrivate *self, QSharedMemory::AccessMode mode)
{
    const QByteArray shmName = QFile::encodeName(self->nativeKey.nativeKey());

    const int oflag = (mode == QSharedMemory::ReadOnly ? O_RDONLY : O_RDWR);
    const mode_t omode = (mode == QSharedMemory::ReadOnly ? 0400 : 0600);

    QT_EINTR_LOOP(hand, ::shm_open(shmName.constData(), oflag, omode));
    if (hand == -1) {
        const int errorNumber = errno;
        const auto function = "QSharedMemory::attach (shm_open)"_L1;
        switch (errorNumber) {
        case EINVAL:
            self->setError(QSharedMemory::KeyError,
                           QSharedMemory::tr("%1: bad name").arg(function));
            break;
        default:
            self->setUnixErrorString(function);
        }
        hand = -1;
        return false;
    }

    // grab the size
    QT_STATBUF st;
    if (QT_FSTAT(hand, &st) == -1) {
        self->setUnixErrorString("QSharedMemory::attach (fstat)"_L1);
        cleanHandle(self);
        return false;
    }
    self->size = qsizetype(st.st_size);

    // grab the memory
    const int mprot = (mode == QSharedMemory::ReadOnly ? PROT_READ : PROT_READ | PROT_WRITE);
    self->memory = QT_MMAP(0, size_t(self->size), mprot, MAP_SHARED, hand, 0);
    if (self->memory == MAP_FAILED || !self->memory) {
        self->setUnixErrorString("QSharedMemory::attach (mmap)"_L1);
        cleanHandle(self);
        self->memory = 0;
        self->size = 0;
        return false;
    }

#ifdef F_ADD_SEALS
    // Make sure the shared memory region will not shrink
    // otherwise someone could cause SIGBUS on us.
    // (see http://lwn.net/Articles/594919/)
    fcntl(hand, F_ADD_SEALS, F_SEAL_SHRINK);
#endif

    return true;
}
#endif  // QT_CONFIG(posix_shm)
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

//  from src/corelib/ipc/qsharedmemory_posix.cpp, line 149, as _ZN18QSharedMemoryPosix6detachEP20QSharedMemoryPrivate
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
inline bool QSharedMemoryPosix::detach(QSharedMemoryPrivate *self)
{
    // detach from the memory segment
    if (::munmap(self->memory, size_t(self->size)) == -1) {
        self->setUnixErrorString("QSharedMemory::detach (munmap)"_L1);
        return false;
    }
    self->memory = 0;
    self->size = 0;

#ifdef Q_OS_QNX
    // On QNX the st_nlink field of struct stat contains the number of
    // active shm_open() connections to the shared memory file, so we
    // can use it to automatically clean up the file once the last
    // user has detached from it.

    // get the number of current attachments
    int shm_nattch = 0;
    QT_STATBUF st;
    if (QT_FSTAT(hand, &st) == 0) {
        // subtract 2 from linkcount: one for our own open and one for the dir entry
        shm_nattch = st.st_nlink - 2;
    }

    cleanHandle(self);

    // if there are no attachments then unlink the shared memory
    if (shm_nattch == 0) {
        const QByteArray shmName = QFile::encodeName(self->nativeKey.nativeKey());
        if (::shm_unlink(shmName.constData()) == -1 && errno != ENOENT)
            self->setUnixErrorString("QSharedMemory::detach (shm_unlink)"_L1);
    }
#else
    // On non-QNX systems (tested Linux and Haiku), the st_nlink field is always 1,
    // so we'll simply leak the shared memory files.
    cleanHandle(self);
#endif

    return true;
}
#endif  // QT_CONFIG(posix_shm)
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

//  from src/corelib/ipc/qsharedmemory.cpp, line 33, as _ZN20QSharedMemoryPrivateD1Ev
#if QT_CONFIG(sharedmemory)
inline QSharedMemoryPrivate::~QSharedMemoryPrivate()
{
    destructBackend();
}
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory.cpp, line 38, as _ZN20QSharedMemoryPrivate16constructBackendEv
#if QT_CONFIG(sharedmemory)
inline void QSharedMemoryPrivate::constructBackend()
{
    using namespace q20;
    visit([](auto p) { construct_at(p); });
}
#endif  // QT_CONFIG(sharedmemory)

//  from src/corelib/ipc/qsharedmemory.cpp, line 44, as _ZN20QSharedMemoryPrivate15destructBackendEv
#if QT_CONFIG(sharedmemory)
inline void QSharedMemoryPrivate::destructBackend()
{
    visit([](auto p) { std::destroy_at(p); });
}
#endif  // QT_CONFIG(sharedmemory)

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
//  -----------------------------------------------------------------------

//  QSharedMemory *QSharedMemoryPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSharedMemory *ritual_ZN20QSharedMemoryPrivate6q_funcEv(
    QSharedMemoryPrivate *self) {
  return self->q_func();
}

//  const QSharedMemory *QSharedMemoryPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSharedMemory *ritual_ZNK20QSharedMemoryPrivate6q_funcEv(
    const QSharedMemoryPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(sharedmemory)
//  QSharedMemoryPrivate::QSharedMemoryPrivate(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
QSharedMemoryPrivate *ritual_ZN20QSharedMemoryPrivateC1EN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return new QSharedMemoryPrivate(type);
}
#endif  // QT_CONFIG(sharedmemory)

//  QSharedMemoryPrivate::~QSharedMemoryPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemoryPrivateD1Ev(QSharedMemoryPrivate *self) {
  delete self;
}

#if QT_CONFIG(sharedmemory)
//  void QSharedMemoryPrivate::constructBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemoryPrivate16constructBackendEv(
    QSharedMemoryPrivate *self) {
  self->constructBackend();
}
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sharedmemory)
//  void QSharedMemoryPrivate::destructBackend()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemoryPrivate15destructBackendEv(
    QSharedMemoryPrivate *self) {
  self->destructBackend();
}
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
#if QT_CONFIG(sysv_shm)
//  bool QSharedMemoryPrivate::handle()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemoryPrivate6handleEv(QSharedMemoryPrivate *self) {
  return self->handle();
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
#if QT_CONFIG(sysv_shm)
//  bool QSharedMemoryPrivate::cleanHandle()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemoryPrivate11cleanHandleEv(
    QSharedMemoryPrivate *self) {
  return self->cleanHandle();
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
#if QT_CONFIG(sysv_shm)
//  bool QSharedMemoryPrivate::attach(QSharedMemory::AccessMode mode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemoryPrivate6attachEN13QSharedMemory10AccessModeE(
    QSharedMemoryPrivate *self,
    QSharedMemory::AccessMode mode) {
  return self->attach(mode);
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
#if QT_CONFIG(sysv_shm)
//  bool QSharedMemoryPrivate::detach()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemoryPrivate6detachEv(QSharedMemoryPrivate *self) {
  return self->detach();
}
#endif  // QT_CONFIG(sysv_shm)
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

//  void QSharedMemoryPrivate::setError(QSharedMemory::SharedMemoryError e,
//      const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemoryPrivate8setErrorEN13QSharedMemory17SharedMemoryErrorERK7QString(
    QSharedMemoryPrivate *self,
    QSharedMemory::SharedMemoryError e,
    const QString *message) {
  self->setError(e, *message);
}

#if QT_CONFIG(sharedmemory)
//  void QSharedMemoryPrivate::setUnixErrorString(QLatin1StringView function)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSharedMemoryPrivate18setUnixErrorStringE13QLatin1String(
    QSharedMemoryPrivate *self,
    const QLatin1String *function) {
  self->setUnixErrorString(*function);
}
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(systemsemaphore)
//  bool QSharedMemoryPrivate::tryLocker(QSharedMemoryLocker *locker, const
//      QString &function)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSharedMemoryPrivate9tryLockerEP19QSharedMemoryLockerRK7QString(
    QSharedMemoryPrivate *self,
    QSharedMemoryLocker *locker,
    const QString *function) {
  return self->tryLocker(locker, *function);
}
#endif  // QT_CONFIG(systemsemaphore)

#endif  // QT_CONFIG(sharedmemory)
