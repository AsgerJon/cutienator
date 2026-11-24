//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractanimation.h"
#include "qanimationgroup.h"
#include <QtCore/qdebug.h>
#include "qabstractanimation_p.h"
#if defined(Q_OS_WASM)
#include <QtCore/private/qwasmanimationdriver_p.h>
#endif
#include <QtCore/qmath.h>
#include <QtCore/qcoreevent.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qpointer.h>
#include <QtCore/qscopedvaluerollback.h>
#include <QtCore/q26numeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/animation/qabstractanimation.cpp, line 890, as _ZN23QDefaultAnimationDriverD1Ev
inline QDefaultAnimationDriver::~QDefaultAnimationDriver()
{
    disconnect(this, &QAnimationDriver::started, this, &QDefaultAnimationDriver::startTimer);
    disconnect(this, &QAnimationDriver::stopped, this, &QDefaultAnimationDriver::stopTimer);
}

//  from src/corelib/animation/qabstractanimation.cpp, line 896, as _ZN23QDefaultAnimationDriver10timerEventEP11QTimerEvent
inline void QDefaultAnimationDriver::timerEvent(QTimerEvent *e)
{
    Q_ASSERT(e->id() == m_timer.id());
    Q_UNUSED(e); // if the assertions are disabled
    advance();
}

//  from src/corelib/animation/qabstractanimation.cpp, line 903, as _ZN23QDefaultAnimationDriver10startTimerEv
inline void QDefaultAnimationDriver::startTimer()
{
    // always use a precise timer to drive animations
    m_timer.start(m_unified_timer->timingInterval, Qt::PreciseTimer, this);
}

//  from src/corelib/animation/qabstractanimation.cpp, line 909, as _ZN23QDefaultAnimationDriver9stopTimerEv
inline void QDefaultAnimationDriver::stopTimer()
{
    m_timer.stop();
}
//  -----------------------------------------------------------------------

//  Only a class built on QDefaultAnimationDriver may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQDefaultAnimationDriver : QDefaultAnimationDriver {
  using QDefaultAnimationDriver::timerEvent;
};

//  A QDefaultAnimationDriver that Python can take functions over in. Every QDefaultAnimationDriver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQDefaultAnimationDriverCall0)(const void *, QTimerEvent *, int *);
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
typedef void (*CuteQDefaultAnimationDriverCall1)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef qint64 (*CuteQDefaultAnimationDriverCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQDefaultAnimationDriverCall3)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQDefaultAnimationDriverCall4)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDefaultAnimationDriverCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDefaultAnimationDriverCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultAnimationDriverCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultAnimationDriverCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultAnimationDriverCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDefaultAnimationDriverCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDefaultAnimationDriver : public QDefaultAnimationDriver {
public:
  using QDefaultAnimationDriver::QDefaultAnimationDriver;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN16QAnimationDriver7advanceEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK16QAnimationDriver7elapsedEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN16QAnimationDriver5startEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN16QAnimationDriver4stopEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
#if QT_CONFIG(animation)
  //  void QDefaultAnimationDriver::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall0 call = reinterpret_cast<CuteQDefaultAnimationDriverCall0>(taken[0]);
      call(this, e, &handled);
      if (handled) return;
    }
    QDefaultAnimationDriver::timerEvent(e);
  }
#endif  // QT_CONFIG(animation)
#endif  // !defined(QT_NO_QOBJECT)

#if QT_CONFIG(animation)
  //  void QAnimationDriver::advance()
  void advance() override {
    if (taken[1]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall1 call = reinterpret_cast<CuteQDefaultAnimationDriverCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::advance();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  qint64 QAnimationDriver::elapsed() const
  qint64 elapsed() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall2 call = reinterpret_cast<CuteQDefaultAnimationDriverCall2>(taken[2]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QAnimationDriver::elapsed();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationDriver::start()
  void start() override {
    if (taken[3]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall3 call = reinterpret_cast<CuteQDefaultAnimationDriverCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::start();
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAnimationDriver::stop()
  void stop() override {
    if (taken[4]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall4 call = reinterpret_cast<CuteQDefaultAnimationDriverCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAnimationDriver::stop();
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall5 call = reinterpret_cast<CuteQDefaultAnimationDriverCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall6 call = reinterpret_cast<CuteQDefaultAnimationDriverCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall7 call = reinterpret_cast<CuteQDefaultAnimationDriverCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall8 call = reinterpret_cast<CuteQDefaultAnimationDriverCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall9 call = reinterpret_cast<CuteQDefaultAnimationDriverCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQDefaultAnimationDriverCall10 call = reinterpret_cast<CuteQDefaultAnimationDriverCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDefaultAnimationDriver::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QDefaultAnimationDriver10metaObjectEv(
    const QDefaultAnimationDriver *self) {
  return self->metaObject();
}

//  QDefaultAnimationDriver::~QDefaultAnimationDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDefaultAnimationDriverD1Ev(QDefaultAnimationDriver *self) {
  delete self;
}

//  void QDefaultAnimationDriver::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDefaultAnimationDriver10timerEventEP11QTimerEvent(
    QDefaultAnimationDriver *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  void QDefaultAnimationDriver::startTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDefaultAnimationDriver10startTimerEv(
    QDefaultAnimationDriver *self) {
  self->startTimer();
}

//  void QDefaultAnimationDriver::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDefaultAnimationDriver9stopTimerEv(
    QDefaultAnimationDriver *self) {
  self->stopTimer();
}

//  a Python function taken by a CuteQDefaultAnimationDriver, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDefaultAnimationDriver(
    QDefaultAnimationDriver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDefaultAnimationDriver *>(self)->take(key, call);
}

//  void QDefaultAnimationDriver::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QDefaultAnimationDriver10timerEventEP11QTimerEvent(
    QDefaultAnimationDriver *self,
    QTimerEvent *e) {
  static_cast<OwnQDefaultAnimationDriver *>(self)->OwnQDefaultAnimationDriver::timerEvent(
      e);
}

#endif  // QT_CONFIG(animation)
