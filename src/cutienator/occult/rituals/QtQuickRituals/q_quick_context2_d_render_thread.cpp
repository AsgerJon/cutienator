//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_canvas)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickcanvasitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <private/qsgadaptationlayer_p.h>
#include "qquickcanvasitem_p.h"
#include <private/qquickitem_p.h>
#include <private/qquickcanvascontext_p.h>
#include <private/qquickcontext2d_p.h>
#include <private/qquickcontext2dtexture_p.h>
#include <private/qsgadaptationlayer_p.h>
#include <qsgtextureprovider.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtGui/QGuiApplication>
#include <qsgtextureprovider.h>
#include <qqmlinfo.h>
#include <private/qqmlengine_p.h>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/qdatetime.h>
#include <private/qv4value_p.h>
#include <private/qv4functionobject_p.h>
#include <private/qv4scopedvalue_p.h>
#include <private/qv4jscall_p.h>
#include <private/qv4qobjectwrapper_p.h>
#include <private/qjsvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/context2d/qquickcanvasitem.cpp, line 102, as _ZN27QQuickContext2DRenderThreadD1Ev
inline QQuickContext2DRenderThread::~QQuickContext2DRenderThread()
{
    renderThreadsMutex.lock();
    renderThreads.remove(m_engine);
    renderThreadsMutex.unlock();

    m_eventLoopQuitHack->deleteLater();
    wait();
}
//  -----------------------------------------------------------------------

//  A QQuickContext2DRenderThread that Python can take functions over in. Every QQuickContext2DRenderThread
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContext2DRenderThreadCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DRenderThreadCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickContext2DRenderThreadCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DRenderThreadCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DRenderThreadCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DRenderThreadCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DRenderThreadCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickContext2DRenderThreadCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickContext2DRenderThread : public QQuickContext2DRenderThread {
public:
  using QQuickContext2DRenderThread::QQuickContext2DRenderThread;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QThread3runEv")) {
      taken[1] = call;
      return true;
    }
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

#if !defined(QT_NO_QOBJECT)
  //  bool QThread::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickContext2DRenderThreadCall0 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QThread::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QThread::run()
  void run() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickContext2DRenderThreadCall1 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QThread::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickContext2DRenderThreadCall2 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall2>(taken[2]);
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
      CuteQQuickContext2DRenderThreadCall3 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall3>(taken[3]);
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
      CuteQQuickContext2DRenderThreadCall4 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall4>(taken[4]);
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
      CuteQQuickContext2DRenderThreadCall5 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall5>(taken[5]);
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
      CuteQQuickContext2DRenderThreadCall6 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall6>(taken[6]);
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
      CuteQQuickContext2DRenderThreadCall7 call = reinterpret_cast<CuteQQuickContext2DRenderThreadCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickContext2DRenderThread::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QQuickContext2DRenderThread10metaObjectEv(
    const QQuickContext2DRenderThread *self) {
  return self->metaObject();
}

//  QQuickContext2DRenderThread::~QQuickContext2DRenderThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickContext2DRenderThreadD1Ev(
    QQuickContext2DRenderThread *self) {
  delete self;
}

//  a Python function taken by a CuteQQuickContext2DRenderThread, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickContext2DRenderThread(
    QQuickContext2DRenderThread *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickContext2DRenderThread *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_canvas)
