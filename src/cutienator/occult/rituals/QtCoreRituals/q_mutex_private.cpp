//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmutex_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: the code taken from qmutex_unix.cpp,
//  its lines pulling in 'sys/time.h' and 'qcore_unix_p.h', and the
//  ritual of the destructor, which that code is, stand under
//  '!defined(QT_ALWAYS_USE_FUTEX)', with Qt's 'qfutex_p.h' pulled in to
//  say it, as Qt's qmutex.cpp has them: Qt defines 'QT_ALWAYS_USE_FUTEX'
//  on Linux, macOS, FreeBSD and Windows, where it builds no
//  QMutexPrivate and no destructor of it, and Windows has neither
//  header. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(thread)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmutex_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qmutex.h>
#include <QtCore/qstring.h>
#include <QtCore/qatomic.h>
#include <QtCore/private/qmutex_p.h>
#include <QtCore/private/qfutex_p.h>
#include <errno.h>
#if !defined(QT_ALWAYS_USE_FUTEX)
#include <sys/time.h>
#endif  // !defined(QT_ALWAYS_USE_FUTEX)
#include <time.h>
#if !defined(QT_ALWAYS_USE_FUTEX)
#include <QtCore/private/qcore_unix_p.h>
#endif  // !defined(QT_ALWAYS_USE_FUTEX)
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/thread/qmutex_unix.cpp, line 22, as local:qmutex_unix.cpp:qt_report_error
#if !defined(QT_ALWAYS_USE_FUTEX)
static void qt_report_error(int code, const char *where, const char *what)
{
    if (code != 0)
        qErrnoWarning(code, "%s: %s failure", where, what);
}

//  from src/corelib/thread/qmutex_unix.cpp, line 33, as _ZN13QMutexPrivateD1Ev
inline QMutexPrivate::~QMutexPrivate()
{

    qt_report_error(sem_destroy(&semaphore), "QMutex", "sem_destroy");
}
#endif  // !defined(QT_ALWAYS_USE_FUTEX)
//  -----------------------------------------------------------------------

#if !defined(QT_ALWAYS_USE_FUTEX)
//  QMutexPrivate::~QMutexPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMutexPrivateD1Ev(QMutexPrivate *self) {
  delete self;
}
#endif  // !defined(QT_ALWAYS_USE_FUTEX)

//  bool QMutexPrivate::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMutexPrivate3refEv(QMutexPrivate *self) {
  return self->ref();
}

#endif  // QT_CONFIG(thread)
