//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicksmoothedanimation_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicksmoothedanimation_p.h"
#include "qquicksmoothedanimation_p_p.h"
#include "qquickanimation_p_p.h"
#include "private/qcontinuinganimationgroupjob_p.h"
#include <qmath.h>
#include <qqmlproperty.h>
#include <private/qqmlproperty_p.h>
#include <private/qqmlglobal_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 32, as _ZN23QSmoothedAnimationTimerD1Ev
inline QSmoothedAnimationTimer::~QSmoothedAnimationTimer()
{
}

//  from ../qtdeclarative/src/quick/util/qquicksmoothedanimation.cpp, line 36, as _ZN23QSmoothedAnimationTimer13stopAnimationEv
inline void QSmoothedAnimationTimer::stopAnimation()
{
    m_animation->stop();
}
//  -----------------------------------------------------------------------

//  A QSmoothedAnimationTimer that Python can take functions over in. Every QSmoothedAnimationTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSmoothedAnimationTimerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSmoothedAnimationTimerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSmoothedAnimationTimerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSmoothedAnimationTimer : public QSmoothedAnimationTimer {
public:
  using QSmoothedAnimationTimer::QSmoothedAnimationTimer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
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
  //  void QTimer::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSmoothedAnimationTimerCall0 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QTimer::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSmoothedAnimationTimerCall1 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall1>(taken[1]);
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
      CuteQSmoothedAnimationTimerCall2 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSmoothedAnimationTimerCall3 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall3>(taken[3]);
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
      CuteQSmoothedAnimationTimerCall4 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall4>(taken[4]);
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
      CuteQSmoothedAnimationTimerCall5 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall5>(taken[5]);
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
      CuteQSmoothedAnimationTimerCall6 call = reinterpret_cast<CuteQSmoothedAnimationTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSmoothedAnimationTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QSmoothedAnimationTimer10metaObjectEv(
    const QSmoothedAnimationTimer *self) {
  return self->metaObject();
}

//  QSmoothedAnimationTimer::~QSmoothedAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSmoothedAnimationTimerD1Ev(QSmoothedAnimationTimer *self) {
  delete self;
}

//  void QSmoothedAnimationTimer::stopAnimation()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QSmoothedAnimationTimer13stopAnimationEv(
    QSmoothedAnimationTimer *self) {
  self->stopAnimation();
}

//  a Python function taken by a CuteQSmoothedAnimationTimer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSmoothedAnimationTimer(
    QSmoothedAnimationTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSmoothedAnimationTimer *>(self)->take(key, call);
}
