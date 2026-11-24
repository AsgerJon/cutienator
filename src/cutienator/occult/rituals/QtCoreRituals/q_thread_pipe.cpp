//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include "qcoreapplication.h"
#include "qhash.h"
#include "qsocketnotifier.h"
#include "qthread.h"
#include "qeventdispatcher_unix_p.h"
#include <private/qthread_p.h>
#include <private/qcoreapplication_p.h>
#include <private/qcore_unix_p.h>
#include <cstdio>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#if __has_include(<sys/eventfd.h>)
#  include <sys/eventfd.h>
#else
#endif
#if defined(Q_OS_VXWORKS)
#  include <taskLib.h>
#if QT_CONFIG(vxpipedrv)
#  include "qbytearray.h"
#  include "qdatetime.h"
#  include "qdir.h" // to get application name
#  include "qrandom.h"
#  include <pipeDrv.h>
#  include <selectLib.h>
#  include <rtpLib.h>
#  include <sysLib.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qeventdispatcher_unix.cpp, line 64, as _ZN11QThreadPipeC1Ev
inline QThreadPipe::QThreadPipe()
{
}

//  from src/corelib/kernel/qeventdispatcher_unix.cpp, line 154, as _ZN11QThreadPipe6wakeUpEv
inline void QThreadPipe::wakeUp()
{
    if ((wakeUps.fetchAndOrAcquire(1) & 1) == 0) {
#  ifdef EFD_CLOEXEC
        eventfd_write(fds[0], 1);
        return;
#endif
        char c = 0;
        qt_safe_write(fds[1], &c, 1);
    }
}
//  -----------------------------------------------------------------------

//  QThreadPipe::QThreadPipe()
extern "C" Q_DECL_EXPORT
QThreadPipe *ritual_ZN11QThreadPipeC1Ev() {
  return new QThreadPipe();
}

//  void QThreadPipe::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPipe6wakeUpEv(QThreadPipe *self) {
  self->wakeUp();
}
