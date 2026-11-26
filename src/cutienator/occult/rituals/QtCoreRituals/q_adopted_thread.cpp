//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qthread.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qbindingstorage.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtCore/qeventloop.h>
#include <QtCore/qmutex.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/thread/qthread.cpp, line 46, as _ZN11QThreadDataD1Ev
inline QThreadData::~QThreadData()
{
#if QT_CONFIG(thread)
    Q_ASSERT(_ref.loadRelaxed() == 0);
#endif

    if (threadId.loadAcquire() == QCoreApplicationPrivate::theMainThreadId.loadAcquire()) {
        QCoreApplicationPrivate::theMainThread.storeRelease(nullptr);
        QCoreApplicationPrivate::theMainThreadId.storeRelaxed(nullptr);
        QThreadData::clearCurrentThreadData();
    }

    // ~QThread() sets thread to nullptr, so if it isn't null here, it's
    // because we're being run before the main object itself. This can only
    // happen for QAdoptedThread. Note that both ~QThreadPrivate() and
    // ~QObjectPrivate() will deref this object again, but that is acceptable
    // because this destructor is still running (the _ref sub-object has not
    // been destroyed) and there's no reentrancy. The refcount will become
    // negative, but that's acceptable.
    QThread *t = thread.loadAcquire();
    thread.storeRelease(nullptr);
    delete t;

    clearEvents();

    // fprintf(stderr, "QThreadData %p destroyed\n", this);
}

//  from src/corelib/thread/qthread.cpp, line 136, as _ZN14QAdoptedThread3runEv
#if QT_CONFIG(thread)
inline void QAdoptedThread::run()
{
    // this function should never be called
    qFatal("QAdoptedThread::run(): Internal error, this implementation should never be called.");
}
#endif  // QT_CONFIG(thread)

//  from src/corelib/thread/qthread.cpp, line 130, as _ZN14QAdoptedThreadD1Ev
inline QAdoptedThread::~QAdoptedThread()
{
    // fprintf(stderr, "~QAdoptedThread = %p\n", this);
}
//  -----------------------------------------------------------------------

//  A QAdoptedThread that Python can take functions over in. Every QAdoptedThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(thread)
typedef void (*CuteQAdoptedThreadCall0)(const void *, int *);
#endif  // QT_CONFIG(thread)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAdoptedThreadCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAdoptedThreadCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAdoptedThreadCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAdoptedThreadCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAdoptedThreadCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAdoptedThreadCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAdoptedThreadCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAdoptedThread : public QAdoptedThread {
public:
  using QAdoptedThread::QAdoptedThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(thread)
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(thread)
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

#if QT_CONFIG(thread)
  //  void QAdoptedThread::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAdoptedThreadCall0 call = reinterpret_cast<CuteQAdoptedThreadCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAdoptedThread::run();
  }
#endif  // QT_CONFIG(thread)

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAdoptedThreadCall1 call = reinterpret_cast<CuteQAdoptedThreadCall1>(taken[1]);
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
      CuteQAdoptedThreadCall2 call = reinterpret_cast<CuteQAdoptedThreadCall2>(taken[2]);
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
      CuteQAdoptedThreadCall3 call = reinterpret_cast<CuteQAdoptedThreadCall3>(taken[3]);
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
      CuteQAdoptedThreadCall4 call = reinterpret_cast<CuteQAdoptedThreadCall4>(taken[4]);
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
      CuteQAdoptedThreadCall5 call = reinterpret_cast<CuteQAdoptedThreadCall5>(taken[5]);
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
      CuteQAdoptedThreadCall6 call = reinterpret_cast<CuteQAdoptedThreadCall6>(taken[6]);
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
      CuteQAdoptedThreadCall7 call = reinterpret_cast<CuteQAdoptedThreadCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QThreadPrivate *QAdoptedThread::d_func()
extern "C" Q_DECL_EXPORT
QThreadPrivate *ritual_ZN14QAdoptedThread6d_funcEv(QAdoptedThread *self) {
  return self->d_func();
}

//  const QThreadPrivate *QAdoptedThread::d_func() const
extern "C" Q_DECL_EXPORT
const QThreadPrivate *ritual_ZNK14QAdoptedThread6d_funcEv(
    const QAdoptedThread *self) {
  return self->d_func();
}

//  QAdoptedThread::~QAdoptedThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAdoptedThreadD1Ev(QAdoptedThread *self) {
  delete self;
}

#if QT_CONFIG(thread)
//  void QAdoptedThread::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAdoptedThread3runEv(QAdoptedThread *self) {
  self->run();
}
#endif  // QT_CONFIG(thread)

//  a Python function taken by a CuteQAdoptedThread, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAdoptedThread(
    QAdoptedThread *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAdoptedThread *>(self)->take(key, call);
}

#if QT_CONFIG(thread)
//  void QAdoptedThread::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QAdoptedThread3runEv(QAdoptedThread *self) {
  self->QAdoptedThread::run();
}
#endif  // QT_CONFIG(thread)
