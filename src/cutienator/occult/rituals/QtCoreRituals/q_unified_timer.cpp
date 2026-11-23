//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qabstractanimation_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/QtCore>
#include <QtCore/6.12.0/QtCore/private/qabstractanimation_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QUnifiedTimer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQUnifiedTimer : QUnifiedTimer {
  using QUnifiedTimer::timerEvent;
};

//  A QUnifiedTimer that Python can take functions over in. Every QUnifiedTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQUnifiedTimerCall0)(const void *, QTimerEvent *, int *);
typedef bool (*CuteQUnifiedTimerCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQUnifiedTimerCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQUnifiedTimerCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQUnifiedTimerCall4)(const void *, QEvent *, int *);
typedef void (*CuteQUnifiedTimerCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQUnifiedTimerCall6)(const void *, const QMetaMethod *, int *);
class CuteQUnifiedTimer : public QUnifiedTimer {
public:
  using QUnifiedTimer::QUnifiedTimer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QUnifiedTimer::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQUnifiedTimerCall0 call = reinterpret_cast<CuteQUnifiedTimerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QUnifiedTimer::timerEvent(a0);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQUnifiedTimerCall1 call = reinterpret_cast<CuteQUnifiedTimerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQUnifiedTimerCall2 call = reinterpret_cast<CuteQUnifiedTimerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQUnifiedTimerCall3 call = reinterpret_cast<CuteQUnifiedTimerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQUnifiedTimerCall4 call = reinterpret_cast<CuteQUnifiedTimerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQUnifiedTimerCall5 call = reinterpret_cast<CuteQUnifiedTimerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQUnifiedTimerCall6 call = reinterpret_cast<CuteQUnifiedTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QUnifiedTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QUnifiedTimer10metaObjectEv(
    const QUnifiedTimer *self) {
  return self->metaObject();
}

//  QString QUnifiedTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QUnifiedTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QUnifiedTimer::tr(s, c, n));
}

//  QUnifiedTimer::QUnifiedTimer()
extern "C" Q_DECL_EXPORT
QUnifiedTimer *ritual_ZN13QUnifiedTimerC1Ev() {
  return new CuteQUnifiedTimer();
}

//  QUnifiedTimer::~QUnifiedTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimerD1Ev(QUnifiedTimer *self) {
  delete self;
}

//  QUnifiedTimer *QUnifiedTimer::instance()
extern "C" Q_DECL_EXPORT
QUnifiedTimer *ritual_ZN13QUnifiedTimer8instanceEv() {
  return QUnifiedTimer::instance();
}

//  QUnifiedTimer *QUnifiedTimer::instance(bool create)
extern "C" Q_DECL_EXPORT
QUnifiedTimer *ritual_ZN13QUnifiedTimer8instanceEb(bool create) {
  return QUnifiedTimer::instance(create);
}

//  void QUnifiedTimer::startAnimationTimer(QAbstractAnimationTimer *timer)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer19startAnimationTimerEP23QAbstractAnimationTimer(
    QAbstractAnimationTimer *timer) {
  QUnifiedTimer::startAnimationTimer(timer);
}

//  void QUnifiedTimer::stopAnimationTimer(QAbstractAnimationTimer *timer)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer18stopAnimationTimerEP23QAbstractAnimationTimer(
    QAbstractAnimationTimer *timer) {
  QUnifiedTimer::stopAnimationTimer(timer);
}

//  void QUnifiedTimer::pauseAnimationTimer(QAbstractAnimationTimer *timer,
//      int duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer19pauseAnimationTimerEP23QAbstractAnimationTimeri(
    QAbstractAnimationTimer *timer,
    int duration) {
  QUnifiedTimer::pauseAnimationTimer(timer, duration);
}

//  void QUnifiedTimer::resumeAnimationTimer(QAbstractAnimationTimer *timer)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer20resumeAnimationTimerEP23QAbstractAnimationTimer(
    QAbstractAnimationTimer *timer) {
  QUnifiedTimer::resumeAnimationTimer(timer);
}

//  void QUnifiedTimer::setTimingInterval(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer17setTimingIntervalEi(
    QUnifiedTimer *self,
    int interval) {
  self->setTimingInterval(interval);
}

//  void QUnifiedTimer::setConsistentTiming(bool consistent)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer19setConsistentTimingEb(
    QUnifiedTimer *self,
    bool consistent) {
  self->setConsistentTiming(consistent);
}

//  qreal QUnifiedTimer::getSpeedModifier() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QUnifiedTimer16getSpeedModifierEv(
    const QUnifiedTimer *self) {
  return self->getSpeedModifier();
}

//  void QUnifiedTimer::setSpeedModifier(qreal speed)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer16setSpeedModifierEd(
    QUnifiedTimer *self,
    qreal speed) {
  self->setSpeedModifier(speed);
}

//  void QUnifiedTimer::installAnimationDriver(QAnimationDriver *driver)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer22installAnimationDriverEP16QAnimationDriver(
    QUnifiedTimer *self,
    QAnimationDriver *driver) {
  self->installAnimationDriver(driver);
}

//  void QUnifiedTimer::uninstallAnimationDriver(QAnimationDriver *driver)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer24uninstallAnimationDriverEP16QAnimationDriver(
    QUnifiedTimer *self,
    QAnimationDriver *driver) {
  self->uninstallAnimationDriver(driver);
}

//  bool QUnifiedTimer::canUninstallAnimationDriver(QAnimationDriver *driver)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QUnifiedTimer27canUninstallAnimationDriverEP16QAnimationDriver(
    QUnifiedTimer *self,
    QAnimationDriver *driver) {
  return self->canUninstallAnimationDriver(driver);
}

//  void QUnifiedTimer::restart()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer7restartEv(QUnifiedTimer *self) {
  self->restart();
}

//  void QUnifiedTimer::maybeUpdateAnimationsToCurrentTime()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer34maybeUpdateAnimationsToCurrentTimeEv(
    QUnifiedTimer *self) {
  self->maybeUpdateAnimationsToCurrentTime();
}

//  void QUnifiedTimer::updateAnimationTimers()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer21updateAnimationTimersEv(QUnifiedTimer *self) {
  self->updateAnimationTimers();
}

//  qsizetype QUnifiedTimer::runningAnimationCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QUnifiedTimer21runningAnimationCountEv(
    const QUnifiedTimer *self) {
  return self->runningAnimationCount();
}

//  void QUnifiedTimer::startAnimationDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer20startAnimationDriverEv(QUnifiedTimer *self) {
  self->startAnimationDriver();
}

//  void QUnifiedTimer::stopAnimationDriver()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer19stopAnimationDriverEv(QUnifiedTimer *self) {
  self->stopAnimationDriver();
}

//  qint64 QUnifiedTimer::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QUnifiedTimer7elapsedEv(const QUnifiedTimer *self) {
  return self->elapsed();
}

//  void QUnifiedTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer10timerEventEP11QTimerEvent(
    QUnifiedTimer *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  void QUnifiedTimer::startTimers()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer11startTimersEv(QUnifiedTimer *self) {
  self->startTimers();
}

//  void QUnifiedTimer::stopTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer9stopTimerEv(QUnifiedTimer *self) {
  self->stopTimer();
}

//  void QUnifiedTimer::localRestart()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QUnifiedTimer12localRestartEv(QUnifiedTimer *self) {
  self->localRestart();
}

//  int QUnifiedTimer::closestPausedAnimationTimerTimeToFinish()
extern "C" Q_DECL_EXPORT
int ritual_ZN13QUnifiedTimer39closestPausedAnimationTimerTimeToFinishEv(
    QUnifiedTimer *self) {
  return self->closestPausedAnimationTimerTimeToFinish();
}

//  a Python function taken by a CuteQUnifiedTimer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QUnifiedTimer(
    QUnifiedTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQUnifiedTimer *>(self)->take(key, call);
}

//  void QUnifiedTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QUnifiedTimer10timerEventEP11QTimerEvent(
    QUnifiedTimer *self,
    QTimerEvent *a0) {
  static_cast<OwnQUnifiedTimer *>(self)->OwnQUnifiedTimer::timerEvent(a0);
}
