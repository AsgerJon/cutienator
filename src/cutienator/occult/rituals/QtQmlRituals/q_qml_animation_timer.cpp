//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_animation)
#if QT_CONFIG(qml_animation)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qabstractanimationjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QQmlAnimationTimer that Python can take functions over in. Every QQmlAnimationTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQmlAnimationTimerCall0)(const void *, int *);
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
typedef void (*CuteQQmlAnimationTimerCall1)(const void *, qint64, int *);
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
#if defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
typedef qsizetype (*CuteQQmlAnimationTimerCall2)(const void *, int *);
#endif  // defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAnimationTimerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQmlAnimationTimerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAnimationTimerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAnimationTimerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAnimationTimerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAnimationTimerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQmlAnimationTimerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQmlAnimationTimer : public QQmlAnimationTimer {
public:
  using QQmlAnimationTimer::QQmlAnimationTimer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer21restartAnimationTimerEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
    if (!std::strcmp(key, "_ZN23QAbstractAnimationTimer20updateAnimationsTimeEx")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)
#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
#if defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
    if (!std::strcmp(key, "_ZNK23QAbstractAnimationTimer21runningAnimationCountEv")) {
      taken[2] = call;
      return true;
    }
#endif  // defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
#endif  // QT_CONFIG(qml_animation)
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
#if QT_CONFIG(qml_animation)
  //  void QQmlAnimationTimer::restartAnimationTimer()
  void restartAnimationTimer() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlAnimationTimerCall0 call = reinterpret_cast<CuteQQmlAnimationTimerCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlAnimationTimer::restartAnimationTimer();
  }
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
  //  void QQmlAnimationTimer::updateAnimationsTime(qint64 timeStep)
  void updateAnimationsTime(qint64 timeStep) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlAnimationTimerCall1 call = reinterpret_cast<CuteQQmlAnimationTimerCall1>(taken[1]);
      call(this, timeStep, &handled);
      if (handled) return;
    }
    QQmlAnimationTimer::updateAnimationsTime(timeStep);
  }
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
#if QT_CONFIG(qml_animation)
#if defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
  //  qsizetype QQmlAnimationTimer::runningAnimationCount() const
  qsizetype runningAnimationCount() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlAnimationTimerCall2 call = reinterpret_cast<CuteQQmlAnimationTimerCall2>(taken[2]);
      qsizetype given = call(this, &handled);
      if (handled) return given;
    }
    return QQmlAnimationTimer::runningAnimationCount();
  }
#endif  // defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(animation)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlAnimationTimerCall3 call = reinterpret_cast<CuteQQmlAnimationTimerCall3>(taken[3]);
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
      CuteQQmlAnimationTimerCall4 call = reinterpret_cast<CuteQQmlAnimationTimerCall4>(taken[4]);
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
      CuteQQmlAnimationTimerCall5 call = reinterpret_cast<CuteQQmlAnimationTimerCall5>(taken[5]);
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
      CuteQQmlAnimationTimerCall6 call = reinterpret_cast<CuteQQmlAnimationTimerCall6>(taken[6]);
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
      CuteQQmlAnimationTimerCall7 call = reinterpret_cast<CuteQQmlAnimationTimerCall7>(taken[7]);
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
      CuteQQmlAnimationTimerCall8 call = reinterpret_cast<CuteQQmlAnimationTimerCall8>(taken[8]);
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
      CuteQQmlAnimationTimerCall9 call = reinterpret_cast<CuteQQmlAnimationTimerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQmlAnimationTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QQmlAnimationTimer10metaObjectEv(
    const QQmlAnimationTimer *self) {
  return self->metaObject();
}

//  void *QQmlAnimationTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QQmlAnimationTimer11qt_metacastEPKc(
    QQmlAnimationTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQmlAnimationTimer::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQmlAnimationTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQmlAnimationTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQmlAnimationTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QQmlAnimationTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlAnimationTimer::tr(s, c, n));
}

//  QQmlAnimationTimer::QQmlAnimationTimer()
extern "C" Q_DECL_EXPORT
QQmlAnimationTimer *ritual_ZN18QQmlAnimationTimerC1Ev() {
  return new CuteQQmlAnimationTimer();
}

//  QQmlAnimationTimer::~QQmlAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimerD1Ev(QQmlAnimationTimer *self) {
  delete self;
}

//  QQmlAnimationTimer *QQmlAnimationTimer::instance()
extern "C" Q_DECL_EXPORT
QQmlAnimationTimer *ritual_ZN18QQmlAnimationTimer8instanceEv() {
  return QQmlAnimationTimer::instance();
}

//  QQmlAnimationTimer *QQmlAnimationTimer::instance(bool create)
extern "C" Q_DECL_EXPORT
QQmlAnimationTimer *ritual_ZN18QQmlAnimationTimer8instanceEb(bool create) {
  return QQmlAnimationTimer::instance(create);
}

//  void QQmlAnimationTimer::registerAnimation(QAbstractAnimationJob
//      *animation, bool isTopLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer17registerAnimationEP21QAbstractAnimationJobb(
    QQmlAnimationTimer *self,
    QAbstractAnimationJob *animation,
    bool isTopLevel) {
  self->registerAnimation(animation, isTopLevel);
}

//  void QQmlAnimationTimer::unregisterAnimation(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer19unregisterAnimationEP21QAbstractAnimationJob(
    QQmlAnimationTimer *self,
    QAbstractAnimationJob *animation) {
  self->unregisterAnimation(animation);
}

//  void QQmlAnimationTimer::ensureTimerUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer17ensureTimerUpdateEv(
    QQmlAnimationTimer *self) {
  self->ensureTimerUpdate();
}

//  void QQmlAnimationTimer::updateAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer20updateAnimationTimerEv(
    QQmlAnimationTimer *self) {
  self->updateAnimationTimer();
}

//  void QQmlAnimationTimer::restartAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer21restartAnimationTimerEv(
    QQmlAnimationTimer *self) {
  self->restartAnimationTimer();
}

//  void QQmlAnimationTimer::updateAnimationsTime(qint64 timeStep)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer20updateAnimationsTimeEx(
    QQmlAnimationTimer *self,
    qint64 timeStep) {
  self->updateAnimationsTime(timeStep);
}

#if defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
//  qsizetype QQmlAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK18QQmlAnimationTimer21runningAnimationCountEv(
    const QQmlAnimationTimer *self) {
  return self->runningAnimationCount();
}
#endif  // defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)

//  bool QQmlAnimationTimer::hasStartAnimationPending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QQmlAnimationTimer24hasStartAnimationPendingEv(
    const QQmlAnimationTimer *self) {
  return self->hasStartAnimationPending();
}

//  void QQmlAnimationTimer::startAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer15startAnimationsEv(
    QQmlAnimationTimer *self) {
  self->startAnimations();
}

//  void QQmlAnimationTimer::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer9stopTimerEv(QQmlAnimationTimer *self) {
  self->stopTimer();
}

//  void QQmlAnimationTimer::registerRunningAnimation(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer24registerRunningAnimationEP21QAbstractAnimationJob(
    QQmlAnimationTimer *self,
    QAbstractAnimationJob *animation) {
  self->registerRunningAnimation(animation);
}

//  void QQmlAnimationTimer::unregisterRunningAnimation(QAbstractAnimationJob
//      *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer26unregisterRunningAnimationEP21QAbstractAnimationJob(
    QQmlAnimationTimer *self,
    QAbstractAnimationJob *animation) {
  self->unregisterRunningAnimation(animation);
}

//  void QQmlAnimationTimer::unsetJobTimer(QAbstractAnimationJob *animation)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlAnimationTimer13unsetJobTimerEP21QAbstractAnimationJob(
    QQmlAnimationTimer *self,
    QAbstractAnimationJob *animation) {
  self->unsetJobTimer(animation);
}

//  int QQmlAnimationTimer::closestPauseAnimationTimeToFinish()
extern "C" Q_DECL_EXPORT
int ritual_ZN18QQmlAnimationTimer33closestPauseAnimationTimeToFinishEv(
    QQmlAnimationTimer *self) {
  return self->closestPauseAnimationTimeToFinish();
}

//  a Python function taken by a CuteQQmlAnimationTimer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlAnimationTimer(
    QQmlAnimationTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlAnimationTimer *>(self)->take(key, call);
}

//  void QQmlAnimationTimer::restartAnimationTimer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlAnimationTimer21restartAnimationTimerEv(
    QQmlAnimationTimer *self) {
  self->QQmlAnimationTimer::restartAnimationTimer();
}

//  void QQmlAnimationTimer::updateAnimationsTime(qint64 timeStep)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQmlAnimationTimer20updateAnimationsTimeEx(
    QQmlAnimationTimer *self,
    qint64 timeStep) {
  self->QQmlAnimationTimer::updateAnimationsTime(timeStep);
}

#if defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)
//  qsizetype QQmlAnimationTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_own_ZNK18QQmlAnimationTimer21runningAnimationCountEv(
    const QQmlAnimationTimer *self) {
  return self->QQmlAnimationTimer::runningAnimationCount();
}
#endif  // defined(QT_QAbstractAnimationTimer_runningAnimationCount_IS_CONST)

#endif  // QT_CONFIG(qml_animation)
#endif  // QT_CONFIG(qml_animation)
