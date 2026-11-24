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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  QSystemSemaphoreSystemV::~QSystemSemaphoreSystemV()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSystemSemaphoreSystemVD1Ev(QSystemSemaphoreSystemV *self) {
  delete self;
}

#endif  // QT_CONFIG(systemsemaphore)
