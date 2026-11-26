//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(animation)
#if QT_CONFIG(animation)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractAnimationTimer that Python can take functions over in. Every QAbstractAnimationTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
typedef void (*CuteQAbstractAnimationTimerCall0)(const void *, qint64, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef void (*CuteQAbstractAnimationTimerCall1)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
typedef qsizetype (*CuteQAbstractAnimationTimerCall2)(const void *, int *);
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAnimationTimerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractAnimationTimerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationTimerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationTimerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationTimerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationTimerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractAnimationTimerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractAnimationTimer : public QAbstractAnimationTimer {
public:
  using QAbstractAnimationTimer::QAbstractAnimationTimer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer21restartAnimationTimerEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
    if (!std::strcmp(key, "_ZNK23QAbstractAnimationTimer21runningAnimationCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(animation)
  //  void QAbstractAnimationTimer::updateAnimationsTime(qint64 delta)
  void updateAnimationsTime(qint64 delta) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall0 call = reinterpret_cast<CuteQAbstractAnimationTimerCall0>(taken[0]);
      call(this, delta, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  void QAbstractAnimationTimer::restartAnimationTimer()
  void restartAnimationTimer() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall1 call = reinterpret_cast<CuteQAbstractAnimationTimerCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
  //  qsizetype QAbstractAnimationTimer::runningAnimationCount() const
  qsizetype runningAnimationCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall2 call = reinterpret_cast<CuteQAbstractAnimationTimerCall2>(taken[2]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall3 call = reinterpret_cast<CuteQAbstractAnimationTimerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall4 call = reinterpret_cast<CuteQAbstractAnimationTimerCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall5 call = reinterpret_cast<CuteQAbstractAnimationTimerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall6 call = reinterpret_cast<CuteQAbstractAnimationTimerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall7 call = reinterpret_cast<CuteQAbstractAnimationTimerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall8 call = reinterpret_cast<CuteQAbstractAnimationTimerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractAnimationTimerCall9 call = reinterpret_cast<CuteQAbstractAnimationTimerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractAnimationTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QAbstractAnimationTimer10metaObjectEv(
    const QAbstractAnimationTimer *self) {
  return self->metaObject();
}

//  void *QAbstractAnimationTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QAbstractAnimationTimer11qt_metacastEPKc(
    QAbstractAnimationTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractAnimationTimer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QAbstractAnimationTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractAnimationTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractAnimationTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QAbstractAnimationTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractAnimationTimer::tr(s, c, n));
}

//  QAbstractAnimationTimer::QAbstractAnimationTimer()
extern "C" Q_DECL_EXPORT
QAbstractAnimationTimer *ritual_ZN23QAbstractAnimationTimerC1Ev() {
  return new CuteQAbstractAnimationTimer();
}

//  QAbstractAnimationTimer::~QAbstractAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractAnimationTimerD1Ev(QAbstractAnimationTimer *self) {
  delete self;
}

//  void QAbstractAnimationTimer::updateAnimationsTime(qint64 delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx(
    QAbstractAnimationTimer *self,
    qint64 delta) {
  self->updateAnimationsTime(delta);
}

//  void QAbstractAnimationTimer::restartAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QAbstractAnimationTimer21restartAnimationTimerEv(
    QAbstractAnimationTimer *self) {
  self->restartAnimationTimer();
}

//  qsizetype QAbstractAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK23QAbstractAnimationTimer21runningAnimationCountEv(
    const QAbstractAnimationTimer *self) {
  return self->runningAnimationCount();
}

//  a Python function taken by a CuteQAbstractAnimationTimer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractAnimationTimer(
    QAbstractAnimationTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractAnimationTimer *>(self)->take(key, call);
}

#endif  // QT_CONFIG(animation)
#endif  // QT_CONFIG(animation)
