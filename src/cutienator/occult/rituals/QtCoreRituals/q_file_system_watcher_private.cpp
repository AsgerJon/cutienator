//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qfilesystemwatcher.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfilesystemwatcher.h"
#include "qfilesystemwatcher_p.h"
#include <qdatetime.h>
#include <qdir.h>
#include <qfileinfo.h>
#include <qloggingcategory.h>
#include <qset.h>
#include "qfilesystemwatcher_polling_p.h"
#if defined(Q_OS_WIN)
#  include "qfilesystemwatcher_win_p.h"
#elif defined(USE_INOTIFY)
#  include "qfilesystemwatcher_inotify_p.h"
#elif defined(Q_OS_FREEBSD) || defined(Q_OS_NETBSD) || defined(Q_OS_OPENBSD) || defined(QT_PLATFORM_UIKIT)
#  include "qfilesystemwatcher_kqueue_p.h"
#elif defined(Q_OS_MACOS)
#  include "qfilesystemwatcher_fsevents_p.h"
#endif
#include <algorithm>
#include <iterator>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfilesystemwatcher.cpp, line 38, as _ZN25QFileSystemWatcherPrivate18createNativeEngineEP7QObject
inline QFileSystemWatcherEngine *QFileSystemWatcherPrivate::createNativeEngine(QObject *parent)
{
#if defined(Q_OS_WIN)
    return new QWindowsFileSystemWatcherEngine(parent);
#elif defined(USE_INOTIFY)
    // there is a chance that inotify may fail on Linux pre-2.6.13 (August
    // 2005), so we can't just new inotify directly.
    return QInotifyFileSystemWatcherEngine::create(parent);
#elif defined(Q_OS_FREEBSD) || defined(Q_OS_NETBSD) || defined(Q_OS_OPENBSD) || defined(QT_PLATFORM_UIKIT)
    return QKqueueFileSystemWatcherEngine::create(parent);
#elif defined(Q_OS_MACOS)
    return QFseventsFileSystemWatcherEngine::create(parent);
#else
    Q_UNUSED(parent);
    return 0;
#endif
}

//  from src/corelib/io/qfilesystemwatcher.cpp, line 56, as _ZN25QFileSystemWatcherPrivateC1Ev
inline QFileSystemWatcherPrivate::QFileSystemWatcherPrivate()
    : native(nullptr), poller(nullptr)
{
}
//  -----------------------------------------------------------------------

//  QFileSystemWatcher *QFileSystemWatcherPrivate::q_func()
extern "C" Q_DECL_EXPORT
QFileSystemWatcher *ritual_ZN25QFileSystemWatcherPrivate6q_funcEv(
    QFileSystemWatcherPrivate *self) {
  return self->q_func();
}

//  const QFileSystemWatcher *QFileSystemWatcherPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFileSystemWatcher *ritual_ZNK25QFileSystemWatcherPrivate6q_funcEv(
    const QFileSystemWatcherPrivate *self) {
  return self->q_func();
}

//  QFileSystemWatcherEngine
//      *QFileSystemWatcherPrivate::createNativeEngine(QObject *parent)
extern "C" Q_DECL_EXPORT
QFileSystemWatcherEngine *ritual_ZN25QFileSystemWatcherPrivate18createNativeEngineEP7QObject(
    QObject *parent) {
  return QFileSystemWatcherPrivate::createNativeEngine(parent);
}

//  QFileSystemWatcherPrivate::QFileSystemWatcherPrivate()
extern "C" Q_DECL_EXPORT
QFileSystemWatcherPrivate *ritual_ZN25QFileSystemWatcherPrivateC1Ev() {
  return new QFileSystemWatcherPrivate();
}

#endif  // QT_CONFIG(filesystemwatcher)
