//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmutex_p.h, Qt 6.12.0. Changes made here are
//  lost.
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
#include <errno.h>
#include <sys/time.h>
#include <time.h>
#include <QtCore/private/qcore_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/thread/qmutex_unix.cpp, line 22, as local:qmutex_unix.cpp:qt_report_error
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
//  -----------------------------------------------------------------------

//  QMutexPrivate::~QMutexPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QMutexPrivateD1Ev(QMutexPrivate *self) {
  delete self;
}

//  bool QMutexPrivate::ref()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QMutexPrivate3refEv(QMutexPrivate *self) {
  return self->ref();
}

#endif  // QT_CONFIG(thread)
