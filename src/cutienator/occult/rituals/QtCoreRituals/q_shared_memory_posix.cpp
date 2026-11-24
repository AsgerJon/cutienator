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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qsharedmemory.h"
#include "qsharedmemory_p.h"
#include "qtipccommon_p.h"
#include <qfile.h>
#include <errno.h>
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "private/qcore_unix_p.h"
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/ipc/qsharedmemory_posix.cpp, line 29, as _ZN18QSharedMemoryPosix19runtimeSupportCheckEv
#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
inline bool QSharedMemoryPosix::runtimeSupportCheck()
{
    static const bool result = []() {
        (void)shm_open("", 0, 0);         // this WILL fail
        return errno != ENOSYS;
    }();
    return result;
}
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

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
//  -----------------------------------------------------------------------

//  bool QSharedMemoryPosix::supports(QNativeIpcKey::Type type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSharedMemoryPosix8supportsEN13QNativeIpcKey4TypeE(
    QNativeIpcKey::Type type) {
  return QSharedMemoryPosix::supports(type);
}

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
//  bool QSharedMemoryPosix::runtimeSupportCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSharedMemoryPosix19runtimeSupportCheckEv() {
  return QSharedMemoryPosix::runtimeSupportCheck();
}
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

#if QT_CONFIG(sharedmemory)
#if QT_CONFIG(posix_shm)
//  bool QSharedMemoryPosix::cleanHandle(QSharedMemoryPrivate *self_)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QSharedMemoryPosix11cleanHandleEP20QSharedMemoryPrivate(
    QSharedMemoryPosix *self,
    QSharedMemoryPrivate *self_) {
  return self->cleanHandle(self_);
}
#endif  // QT_CONFIG(posix_shm)
#endif  // QT_CONFIG(sharedmemory)

//  QSharedMemoryPosix::~QSharedMemoryPosix()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QSharedMemoryPosixD1Ev(QSharedMemoryPosix *self) {
  delete self;
}

#endif  // QT_CONFIG(sharedmemory)
