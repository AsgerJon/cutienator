//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qfilesystemwatcher.h>
#include <QtCore/private/qfilesystemwatcher_win_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qset.h>
#include <QtCore/qscopeguard.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdir.h>
#include <QtCore/qtextstream.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qt_windows.h>
#  include <QtCore/qabstractnativeeventfilter.h>
#  include <QtCore/qcoreapplication.h>
#  include <QtCore/qdir.h>
#  include <QtCore/private/qeventdispatcher_win_p.h>
#  include <QtCore/private/qthread_p.h>
#  include <dbt.h>
#  include <algorithm>
#  include <vector>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystemwatcher_win.cpp, line 293, as _ZN31QWindowsFileSystemWatcherEngine6HandleC1Ev
inline QWindowsFileSystemWatcherEngine::Handle::Handle()
    : handle(INVALID_HANDLE_VALUE), flags(0u)
{
}
//  -----------------------------------------------------------------------

//  QWindowsFileSystemWatcherEngine::Handle::Handle()
extern "C" Q_DECL_EXPORT
QWindowsFileSystemWatcherEngine::Handle *ritual_ZN31QWindowsFileSystemWatcherEngine6HandleC1Ev() {
  return new QWindowsFileSystemWatcherEngine::Handle();
}

//  QWindowsFileSystemWatcherEngine::Handle::~Handle()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsFileSystemWatcherEngine6HandleD1Ev(
    QWindowsFileSystemWatcherEngine::Handle *self) {
  delete self;
}

#endif  // QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
