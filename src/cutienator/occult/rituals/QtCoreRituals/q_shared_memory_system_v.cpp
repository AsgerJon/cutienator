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

#endif  // QT_CONFIG(sharedmemory)
