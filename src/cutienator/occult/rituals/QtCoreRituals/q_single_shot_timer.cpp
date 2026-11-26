//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsingleshottimer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsingleshottimer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qsingleshottimer_p.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/private/qmetaobject_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/qthread.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/corelib/kernel/qsingleshottimer.cpp, line 67, as _ZN16QSingleShotTimer10timerEventEP11QTimerEvent
inline void QSingleShotTimer::timerEvent(QTimerEvent *event)
{
    if (event->id() == Qt::TimerId::Invalid) {
        StartTimerEvent *startTimerEvent = static_cast<StartTimerEvent *>(event);
        Q_UNUSED(startTimerEvent->timer.release()); // it's the same as "this"
        const QDeadlineTimer &deadline = startTimerEvent->deadline;
        if (deadline.hasExpired()) {
            timerFinished();
        } else {
            timer.start(deadline.remainingTimeAsDuration(), deadline.timerType(), this);
            // we are now definitely in a thread that has an event dispatcher
            setParent(QThread::currentThread()->eventDispatcher());
        }
    } else {
        // need to kill the timer _before_ we emit timeout() in case the
        // slot connected to timeout calls processEvents()
        timer.stop();

        timerFinished();
    }
}

//  from src/corelib/kernel/qsingleshottimer.cpp, line 61, as _ZN16QSingleShotTimer13timerFinishedEv
inline void QSingleShotTimer::timerFinished()
{
    Q_EMIT timeout();
    delete this;
}

//  from src/corelib/kernel/qsingleshottimer.cpp, line 42, as _ZN16QSingleShotTimer21startTimerForReceiverENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObject
inline void QSingleShotTimer::startTimerForReceiver(Duration interval, Qt::TimerType timerType,
                                             const QObject *receiver)
{
    if (receiver && receiver->thread() != thread()) {
        QObjectPrivate *d_ptr = QObjectPrivate::get(this);
        d_ptr->sendChildEvents = false;

        setParent(nullptr);
        moveToThread(receiver->thread());

        QCoreApplication::postEvent(this,
                                    new StartTimerEvent(this, QDeadlineTimer(interval, timerType)));
        // the event owns "this" and is handled concurrently, so unsafe to
        // access "this" beyond this point
    } else {
        timer.start(interval, timerType, this);
    }
}
//  -----------------------------------------------------------------------

//  A QSingleShotTimer that Python can take functions over in. Every QSingleShotTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSingleShotTimerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSingleShotTimerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSingleShotTimerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSingleShotTimer : public QSingleShotTimer {
public:
  using QSingleShotTimer::QSingleShotTimer;
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
  //  void QSingleShotTimer::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSingleShotTimerCall0 call = reinterpret_cast<CuteQSingleShotTimerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QSingleShotTimer::timerEvent(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSingleShotTimerCall1 call = reinterpret_cast<CuteQSingleShotTimerCall1>(taken[1]);
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
      CuteQSingleShotTimerCall2 call = reinterpret_cast<CuteQSingleShotTimerCall2>(taken[2]);
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
      CuteQSingleShotTimerCall3 call = reinterpret_cast<CuteQSingleShotTimerCall3>(taken[3]);
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
      CuteQSingleShotTimerCall4 call = reinterpret_cast<CuteQSingleShotTimerCall4>(taken[4]);
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
      CuteQSingleShotTimerCall5 call = reinterpret_cast<CuteQSingleShotTimerCall5>(taken[5]);
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
      CuteQSingleShotTimerCall6 call = reinterpret_cast<CuteQSingleShotTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSingleShotTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QSingleShotTimer10metaObjectEv(
    const QSingleShotTimer *self) {
  return self->metaObject();
}

//  void *QSingleShotTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN16QSingleShotTimer11qt_metacastEPKc(
    QSingleShotTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSingleShotTimer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN16QSingleShotTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSingleShotTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QSingleShotTimer::~QSingleShotTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimerD1Ev(QSingleShotTimer *self) {
  delete self;
}

//  void QSingleShotTimer::startTimerForReceiver(Duration interval,
//      Qt::TimerType timerType, const QObject *receiver)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer21startTimerForReceiverENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObject(
    QSingleShotTimer *self,
    long long interval,
    Qt::TimerType timerType,
    const QObject *receiver) {
  self->startTimerForReceiver(
      QSingleShotTimer::Duration(interval),
      timerType,
      receiver);
}

//  void QSingleShotTimer::timeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer7timeoutEv(QSingleShotTimer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QSingleShotTimer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "timeout()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "timeout()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QSingleShotTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSingleShotTimer10timerEventEP11QTimerEvent(
    QSingleShotTimer *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  a Python function taken by a CuteQSingleShotTimer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSingleShotTimer(
    QSingleShotTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSingleShotTimer *>(self)->take(key, call);
}
