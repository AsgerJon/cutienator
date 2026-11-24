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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  QSystemSemaphorePosix::~QSystemSemaphorePosix()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSystemSemaphorePosixD1Ev(QSystemSemaphorePosix *self) {
  delete self;
}

#endif  // QT_CONFIG(systemsemaphore)
