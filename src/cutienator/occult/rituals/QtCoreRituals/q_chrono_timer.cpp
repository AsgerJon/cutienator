//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qchronotimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qchronotimer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QChronoTimer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQChronoTimer : QChronoTimer {
  using QChronoTimer::timerEvent;
};

//  A QChronoTimer that Python can take functions over in. Every QChronoTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQChronoTimerCall0)(const void *, QTimerEvent *, int *);
typedef bool (*CuteQChronoTimerCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQChronoTimerCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQChronoTimerCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQChronoTimerCall4)(const void *, QEvent *, int *);
typedef void (*CuteQChronoTimerCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQChronoTimerCall6)(const void *, const QMetaMethod *, int *);
class CuteQChronoTimer : public QChronoTimer {
public:
  using QChronoTimer::QChronoTimer;
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

  //  void QChronoTimer::timerEvent(QTimerEvent *a0)
  void timerEvent(QTimerEvent *a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQChronoTimerCall0 call = reinterpret_cast<CuteQChronoTimerCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QChronoTimer::timerEvent(a0);
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQChronoTimerCall1 call = reinterpret_cast<CuteQChronoTimerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQChronoTimerCall2 call = reinterpret_cast<CuteQChronoTimerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQChronoTimerCall3 call = reinterpret_cast<CuteQChronoTimerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQChronoTimerCall4 call = reinterpret_cast<CuteQChronoTimerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQChronoTimerCall5 call = reinterpret_cast<CuteQChronoTimerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQChronoTimerCall6 call = reinterpret_cast<CuteQChronoTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QChronoTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QChronoTimer10metaObjectEv(
    const QChronoTimer *self) {
  return self->metaObject();
}

//  QString QChronoTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QChronoTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QChronoTimer::tr(s, c, n));
}

//  QChronoTimer::QChronoTimer(QObject *parent)
extern "C" Q_DECL_EXPORT
QChronoTimer *ritual_ZN12QChronoTimerC1EP7QObject(QObject *parent) {
  return new CuteQChronoTimer(parent);
}

//  QChronoTimer::~QChronoTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimerD1Ev(QChronoTimer *self) {
  delete self;
}

//  bool QChronoTimer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QChronoTimer8isActiveEv(const QChronoTimer *self) {
  return self->isActive();
}

//  Qt::TimerId QChronoTimer::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK12QChronoTimer2idEv(const QChronoTimer *self) {
  return self->id();
}

//  void QChronoTimer::setTimerType(Qt::TimerType atype)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer12setTimerTypeEN2Qt9TimerTypeE(
    QChronoTimer *self,
    Qt::TimerType atype) {
  self->setTimerType(atype);
}

//  Qt::TimerType QChronoTimer::timerType() const
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZNK12QChronoTimer9timerTypeEv(
    const QChronoTimer *self) {
  return self->timerType();
}

//  void QChronoTimer::setSingleShot(bool singleShot)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer13setSingleShotEb(
    QChronoTimer *self,
    bool singleShot) {
  self->setSingleShot(singleShot);
}

//  bool QChronoTimer::isSingleShot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QChronoTimer12isSingleShotEv(const QChronoTimer *self) {
  return self->isSingleShot();
}

//  void QChronoTimer::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer5startEv(QChronoTimer *self) {
  self->start();
}

//  void QChronoTimer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer4stopEv(QChronoTimer *self) {
  self->stop();
}

//  void QChronoTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer10timerEventEP11QTimerEvent(
    QChronoTimer *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  a Python function taken by a CuteQChronoTimer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QChronoTimer(
    QChronoTimer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQChronoTimer *>(self)->take(key, call);
}

//  void QChronoTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QChronoTimer10timerEventEP11QTimerEvent(
    QChronoTimer *self,
    QTimerEvent *a0) {
  static_cast<OwnQChronoTimer *>(self)->OwnQChronoTimer::timerEvent(a0);
}
