//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapes/
//  6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapegenericrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickshapegenericrenderer_p.h"
#include <QtGui/private/qtriangulator_p.h>
#include <QtGui/private/qtriangulatingstroker_p.h>
#include <rhi/qrhi.h>
#include <QSGVertexColorMaterial>
#include <QSGTextureProvider>
#include <private/qsgplaintexture_p.h>
#include <QtQuick/private/qsggradientcache_p.h>
#if QT_CONFIG(thread)
#include <QThreadPool>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapegenericrenderer.cpp, line 307, as _ZN25QQuickShapeStrokeRunnable3runEv
inline void QQuickShapeStrokeRunnable::run()
{
    QQuickShapeGenericRenderer::triangulateStroke(path, pen, strokeColor, &strokeVertices, clipSize, triangulationScale);
    // Emit done signal on main thread, since connected to lambda there
    QMetaObject::invokeMethod(qApp, [this]() { emit done(this); }, Qt::QueuedConnection);
}
//  -----------------------------------------------------------------------

//  A QQuickShapeStrokeRunnable that Python can take functions over in. Every QQuickShapeStrokeRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickShapeStrokeRunnableCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapeStrokeRunnableCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapeStrokeRunnableCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeStrokeRunnableCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeStrokeRunnableCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeStrokeRunnableCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeStrokeRunnableCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeStrokeRunnableCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShapeStrokeRunnable : public QQuickShapeStrokeRunnable {
public:
  using QQuickShapeStrokeRunnable::QQuickShapeStrokeRunnable;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN9QRunnable3runEv")) {
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

  //  void QQuickShapeStrokeRunnable::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeStrokeRunnableCall0 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShapeStrokeRunnable::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeStrokeRunnableCall1 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapeStrokeRunnableCall2 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall2>(taken[2]);
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
      CuteQQuickShapeStrokeRunnableCall3 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall3>(taken[3]);
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
      CuteQQuickShapeStrokeRunnableCall4 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall4>(taken[4]);
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
      CuteQQuickShapeStrokeRunnableCall5 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall5>(taken[5]);
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
      CuteQQuickShapeStrokeRunnableCall6 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall6>(taken[6]);
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
      CuteQQuickShapeStrokeRunnableCall7 call = reinterpret_cast<CuteQQuickShapeStrokeRunnableCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShapeStrokeRunnable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQuickShapeStrokeRunnable10metaObjectEv(
    const QQuickShapeStrokeRunnable *self) {
  return self->metaObject();
}

//  void QQuickShapeStrokeRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickShapeStrokeRunnable3runEv(
    QQuickShapeStrokeRunnable *self) {
  self->run();
}

//  QQuickShapeStrokeRunnable as the QRunnable it is built on
extern "C" Q_DECL_EXPORT
QRunnable *ritual_cast_QQuickShapeStrokeRunnable_QRunnable(
    QQuickShapeStrokeRunnable *self) {
  return static_cast<QRunnable *>(self);
}

//  a Python function taken by a CuteQQuickShapeStrokeRunnable, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeStrokeRunnable(
    QQuickShapeStrokeRunnable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeStrokeRunnable *>(self)->take(key, call);
}
