//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthread_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/QtCore>
#include <QtCore/6.12.0/QtCore/private/qthread_p.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include "qthread.h"
#include "qthread_p.h"
#include "qabstracteventdispatcher.h"
#include "qbindingstorage.h"
#include "private/qcoreapplication_p.h"
#include "qeventloop.h"
#include "qmutex.h"

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/corelib/thread/qthread.cpp, line 130, as _ZN14QAdoptedThreadD1Ev
inline QAdoptedThread::~QAdoptedThread()
{
    // fprintf(stderr, "~QAdoptedThread = %p\n", this);
}

//  from src/corelib/thread/qthread.cpp, line 136, as _ZN14QAdoptedThread3runEv
inline void QAdoptedThread::run()
{
    // this function should never be called
    qFatal("QAdoptedThread::run(): Internal error, this implementation should never be called.");
}
//  -----------------------------------------------------------------------

//  A QAdoptedThread that Python can take functions over in. Every QAdoptedThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAdoptedThreadCall0)(const void *, int *);
typedef bool (*CuteQAdoptedThreadCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQAdoptedThreadCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQAdoptedThreadCall3)(const void *, QTimerEvent *, int *);
typedef void (*CuteQAdoptedThreadCall4)(const void *, QChildEvent *, int *);
typedef void (*CuteQAdoptedThreadCall5)(const void *, QEvent *, int *);
typedef void (*CuteQAdoptedThreadCall6)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQAdoptedThreadCall7)(const void *, const QMetaMethod *, int *);
class CuteQAdoptedThread : public QAdoptedThread {
public:
  using QAdoptedThread::QAdoptedThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

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
};

//  QAdoptedThread::~QAdoptedThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAdoptedThreadD1Ev(QAdoptedThread *self) {
  delete self;
}

//  void QAdoptedThread::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QAdoptedThread3runEv(QAdoptedThread *self) {
  self->run();
}

//  a Python function taken by a CuteQAdoptedThread, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAdoptedThread(
    QAdoptedThread *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAdoptedThread *>(self)->take(key, call);
}

//  void QAdoptedThread::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QAdoptedThread3runEv(QAdoptedThread *self) {
  self->QAdoptedThread::run();
}
