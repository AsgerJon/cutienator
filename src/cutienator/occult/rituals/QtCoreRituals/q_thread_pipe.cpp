//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-27: code taken from Qt's qeventdispatcher_unix.cpp
//  stands under defined(Q_OS_UNIX), as Qt builds that file, not
//  defined(Q_OS_LINUX). Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qplatformdefs.h"
#include <QtCore/qcoreapplication.h>
#include <QtCore/qhash.h>
#include <QtCore/qsocketnotifier.h>
#include <QtCore/qthread.h>
#include <QtCore/private/qeventdispatcher_unix_p.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/private/qcore_unix_p.h>
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
#  include <QtCore/qbytearray.h>
#  include <QtCore/qdatetime.h>
#  include <QtCore/qdir.h> // to get application name
#  include <QtCore/qrandom.h>
#  include <pipeDrv.h>
#  include <selectLib.h>
#  include <rtpLib.h>
#  include <sysLib.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qeventdispatcher_unix.cpp, line 26, as local:qeventdispatcher_unix.cpp:UsingEventfd
#if __has_include(<sys/eventfd.h>)
static constexpr bool UsingEventfd = true;
#endif  // __has_include(<sys/eventfd.h>)

//  from src/corelib/kernel/qeventdispatcher_unix.cpp, line 64, as _ZN11QThreadPipeC1Ev
inline QThreadPipe::QThreadPipe()
{
}

//  from src/corelib/kernel/qeventdispatcher_unix.cpp, line 68, as _ZN11QThreadPipeD1Ev
#if defined(Q_OS_UNIX)
inline QThreadPipe::~QThreadPipe()
{
    if (fds[0] >= 0)
        close(fds[0]);

    if (!UsingEventfd && fds[1] >= 0)
        close(fds[1]);

#if defined(Q_OS_VXWORKS) && QT_CONFIG(vxpipedrv)
    pipeDevDelete(name, true);
#endif
}
#endif  // defined(Q_OS_UNIX)

//  from src/corelib/kernel/qeventdispatcher_unix.cpp, line 149, as _ZNK11QThreadPipe7prepareEv
inline pollfd QThreadPipe::prepare() const
{
    return qt_make_pollfd(fds[0], POLLIN);
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

//  QThreadPipe::~QThreadPipe()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPipeD1Ev(QThreadPipe *self) {
  delete self;
}

//  pollfd QThreadPipe::prepare() const
extern "C" Q_DECL_EXPORT
pollfd *ritual_ZNK11QThreadPipe7prepareEv(const QThreadPipe *self) {
  return new pollfd(self->prepare());
}

//  void QThreadPipe::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPipe6wakeUpEv(QThreadPipe *self) {
  self->wakeUp();
}

//  a pollfd a ritual of QThreadPipe gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QThreadPipe__pollfd(pollfd *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX) && !defined(Q_OS_WASM)
