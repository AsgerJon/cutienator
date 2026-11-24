//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsharedmemory_p.h, Qt 6.12.0. Changes made
//  here are lost.
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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
