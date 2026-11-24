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
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qfilesystemwatcher.h"
#include "qfilesystemwatcher_win_p.h"
#include <qdebug.h>
#include <qfileinfo.h>
#include <qstringlist.h>
#include <qset.h>
#include <qscopeguard.h>
#include <qdatetime.h>
#include <qdir.h>
#include <qtextstream.h>
#include <private/qlocking_p.h>
#include <qt_windows.h>
#  include <qabstractnativeeventfilter.h>
#  include <qcoreapplication.h>
#  include <qdir.h>
#  include <private/qeventdispatcher_win_p.h>
#  include <private/qthread_p.h>
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

//  from src/corelib/io/qfilesystemwatcher_win.cpp, line 298, as _ZN31QWindowsFileSystemWatcherEngineC1EP7QObject
inline QWindowsFileSystemWatcherEngine::QWindowsFileSystemWatcherEngine(QObject *parent)
    : QFileSystemWatcherEngine(parent)
{
    if (QAbstractEventDispatcher *eventDispatcher = QAbstractEventDispatcher::instance()) {
        m_driveListener = new QWindowsRemovableDriveListener(this);
        eventDispatcher->installNativeEventFilter(m_driveListener);
        parent->setProperty("_q_driveListener",
                            QVariant::fromValue(static_cast<QObject *>(m_driveListener)));
        QObject::connect(m_driveListener, &QWindowsRemovableDriveListener::driveLockForRemoval,
                         this, &QWindowsFileSystemWatcherEngine::driveLockForRemoval);
        QObject::connect(m_driveListener, &QWindowsRemovableDriveListener::driveLockForRemovalFailed,
                         this, &QWindowsFileSystemWatcherEngine::driveLockForRemovalFailed);
        QObject::connect(m_driveListener,
                         QOverload<const QString &>::of(&QWindowsRemovableDriveListener::driveRemoved),
                         this, &QWindowsFileSystemWatcherEngine::driveRemoved);
    } else {
        qWarning("QFileSystemWatcher: Removable drive notification will not work"
                 " if there is no QCoreApplication instance.");
    }
}

//  from src/corelib/io/qfilesystemwatcher_win.cpp, line 319, as _ZN31QWindowsFileSystemWatcherEngineD1Ev
inline QWindowsFileSystemWatcherEngine::~QWindowsFileSystemWatcherEngine()
{
    for (auto *thread : std::as_const(threads))
        thread->stop();
    for (auto *thread : std::as_const(threads))
        thread->wait();
    qDeleteAll(threads);
}
//  -----------------------------------------------------------------------

//  A QWindowsFileSystemWatcherEngine that Python can take functions over in. Every QWindowsFileSystemWatcherEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsFileSystemWatcherEngineCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsFileSystemWatcherEngineCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsFileSystemWatcherEngineCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowsFileSystemWatcherEngine : public QWindowsFileSystemWatcherEngine {
public:
  using QWindowsFileSystemWatcherEngine::QWindowsFileSystemWatcherEngine;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall0 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall1 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall2 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall3 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall4 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall5 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsFileSystemWatcherEngineCall6 call = reinterpret_cast<CuteQWindowsFileSystemWatcherEngineCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowsFileSystemWatcherEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QWindowsFileSystemWatcherEngine10metaObjectEv(
    const QWindowsFileSystemWatcherEngine *self) {
  return self->metaObject();
}

//  QString QWindowsFileSystemWatcherEngine::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QWindowsFileSystemWatcherEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowsFileSystemWatcherEngine::tr(s, c, n));
}

//  QWindowsFileSystemWatcherEngine::QWindowsFileSystemWatcherEngine(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QWindowsFileSystemWatcherEngine *ritual_ZN31QWindowsFileSystemWatcherEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQWindowsFileSystemWatcherEngine(parent);
}

//  QWindowsFileSystemWatcherEngine::~QWindowsFileSystemWatcherEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QWindowsFileSystemWatcherEngineD1Ev(
    QWindowsFileSystemWatcherEngine *self) {
  delete self;
}

//  a Python function taken by a CuteQWindowsFileSystemWatcherEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsFileSystemWatcherEngine(
    QWindowsFileSystemWatcherEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsFileSystemWatcherEngine *>(self)->take(key, call);
}

#endif  // QT_CONFIG(filesystemwatcher) && defined(Q_OS_WIN)
