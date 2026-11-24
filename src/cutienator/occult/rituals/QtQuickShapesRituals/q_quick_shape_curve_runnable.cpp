//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapecurverenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapecurverenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/private/qquickshapecurverenderer_p.h>
#include <QtQuickShapes/private/qquickshapecurverenderer_p_p.h>
#if QT_CONFIG(thread)
#include <QtCore/qthreadpool.h>
#endif
#include <QtGui/qvector2d.h>
#include <QtGui/qvector4d.h>
#include <QtGui/private/qtriangulator_p.h>
#include <QtGui/private/qtriangulatingstroker_p.h>
#include <QtGui/private/qrhi_p.h>
#include <QtQuick/private/qsgcurvefillnode_p.h>
#include <QtQuick/private/qquadpath_p.h>
#include <QtQuick/qsgmaterial.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickshapes/qquickshapecurverenderer.cpp, line 479, as _ZN24QQuickShapeCurveRunnableD1Ev
inline QQuickShapeCurveRunnable::~QQuickShapeCurveRunnable()
{
    qDeleteAll(pathData.fillNodes);
    qDeleteAll(pathData.strokeNodes);
}

//  from ../qtdeclarative/src/quickshapes/qquickshapecurverenderer.cpp, line 485, as _ZN24QQuickShapeCurveRunnable3runEv
inline void QQuickShapeCurveRunnable::run()
{
    QQuickShapeCurveRenderer::processPath(&pathData);
    emit done(this);
}
//  -----------------------------------------------------------------------

//  A QQuickShapeCurveRunnable that Python can take functions over in. Every QQuickShapeCurveRunnable
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickShapeCurveRunnableCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapeCurveRunnableCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickShapeCurveRunnableCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCurveRunnableCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCurveRunnableCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCurveRunnableCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCurveRunnableCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickShapeCurveRunnableCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickShapeCurveRunnable : public QQuickShapeCurveRunnable {
public:
  using QQuickShapeCurveRunnable::QQuickShapeCurveRunnable;
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

  //  void QQuickShapeCurveRunnable::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickShapeCurveRunnableCall0 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickShapeCurveRunnable::run();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapeCurveRunnableCall1 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall1>(taken[1]);
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
      CuteQQuickShapeCurveRunnableCall2 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall2>(taken[2]);
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
      CuteQQuickShapeCurveRunnableCall3 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall3>(taken[3]);
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
      CuteQQuickShapeCurveRunnableCall4 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall4>(taken[4]);
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
      CuteQQuickShapeCurveRunnableCall5 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall5>(taken[5]);
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
      CuteQQuickShapeCurveRunnableCall6 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall6>(taken[6]);
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
      CuteQQuickShapeCurveRunnableCall7 call = reinterpret_cast<CuteQQuickShapeCurveRunnableCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickShapeCurveRunnable::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickShapeCurveRunnable10metaObjectEv(
    const QQuickShapeCurveRunnable *self) {
  return self->metaObject();
}

//  QQuickShapeCurveRunnable::~QQuickShapeCurveRunnable()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRunnableD1Ev(
    QQuickShapeCurveRunnable *self) {
  delete self;
}

//  void QQuickShapeCurveRunnable::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickShapeCurveRunnable3runEv(
    QQuickShapeCurveRunnable *self) {
  self->run();
}

//  QQuickShapeCurveRunnable as the QRunnable it is built on
extern "C" Q_DECL_EXPORT
QRunnable *ritual_cast_QQuickShapeCurveRunnable_QRunnable(
    QQuickShapeCurveRunnable *self) {
  return static_cast<QRunnable *>(self);
}

//  a Python function taken by a CuteQQuickShapeCurveRunnable, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapeCurveRunnable(
    QQuickShapeCurveRunnable *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapeCurveRunnable *>(self)->take(key, call);
}
