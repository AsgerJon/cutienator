//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the code taken from Qt's source for 'run'
//  is left out, with the ritual of Qt's own 'run', which calls that code,
//  because the code uses the macro 'DEBUG' and the function
//  'msgFindNextFailed', which only Qt's 'qfilesystemwatcher_win.cpp'
//  defines, so it compiles on no system. 'tr' and the constructor are taken
//  out too, with the code taken for the constructor: Qt's library offers
//  nothing of this class, and 'tr' needs its 'staticMetaObject', while a
//  Cute object made by the constructor needs its table of virtual functions,
//  Qt's 'run' among them. Kept as it is when the generator runs again.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qfilesystemwatcher_win_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/io/qfilesystemwatcher_win.cpp, line 577, as _ZN37QWindowsFileSystemWatcherEngineThreadD1Ev
inline QWindowsFileSystemWatcherEngineThread::~QWindowsFileSystemWatcherEngineThread()
{
    CloseHandle(handles.at(0));
    handles[0] = INVALID_HANDLE_VALUE;

    for (HANDLE h : std::as_const(handles)) {
        if (h == INVALID_HANDLE_VALUE)
            continue;
        FindCloseChangeNotification(h);
    }
}

//  from src/corelib/io/qfilesystemwatcher_win.cpp, line 697, as _ZN37QWindowsFileSystemWatcherEngineThread4stopEv
inline void QWindowsFileSystemWatcherEngineThread::stop()
{
    msg = 'q';
    SetEvent(handles.at(0));
}

//  from src/corelib/io/qfilesystemwatcher_win.cpp, line 703, as _ZN37QWindowsFileSystemWatcherEngineThread6wakeupEv
inline void QWindowsFileSystemWatcherEngineThread::wakeup()
{
    msg = '@';
    SetEvent(handles.at(0));
}
//  -----------------------------------------------------------------------

//  A QWindowsFileSystemWatcherEngineThread that Python can take functions over in. Every QWindowsFileSystemWatcherEngineThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWindowsFileSystemWatcherEngineThreadCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsFileSystemWatcherEngineThreadCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsFileSystemWatcherEngineThreadCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineThreadCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineThreadCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineThreadCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineThreadCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineThreadCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowsFileSystemWatcherEngineThread : public QWindowsFileSystemWatcherEngineThread {
public:
  using QWindowsFileSystemWatcherEngineThread::QWindowsFileSystemWatcherEngineThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWindowsFileSystemWatcherEngineThread::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall0 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsFileSystemWatcherEngineThread::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall1 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall2 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall3 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall4 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall5 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall6 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineThreadCall7 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineThreadCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowsFileSystemWatcherEngineThread::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK37QWindowsFileSystemWatcherEngineThread10metaObjectEv(
    const QWindowsFileSystemWatcherEngineThread *self) {
  return self->metaObject();
}

//  QWindowsFileSystemWatcherEngineThread::~QWindowsFileSystemWatcherEngineTh
//      read()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QWindowsFileSystemWatcherEngineThreadD1Ev(
    QWindowsFileSystemWatcherEngineThread *self) {
  delete self;
}

//  void QWindowsFileSystemWatcherEngineThread::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QWindowsFileSystemWatcherEngineThread3runEv(
    QWindowsFileSystemWatcherEngineThread *self) {
  self->run();
}

//  void QWindowsFileSystemWatcherEngineThread::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QWindowsFileSystemWatcherEngineThread4stopEv(
    QWindowsFileSystemWatcherEngineThread *self) {
  self->stop();
}

//  void QWindowsFileSystemWatcherEngineThread::wakeup()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QWindowsFileSystemWatcherEngineThread6wakeupEv(
    QWindowsFileSystemWatcherEngineThread *self) {
  self->wakeup();
}

//  a Python function taken by a CuteQWindowsFileSystemWatcherEngineThread,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsFileSystemWatcherEngineThread(
    QWindowsFileSystemWatcherEngineThread *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsFileSystemWatcherEngineThread *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
