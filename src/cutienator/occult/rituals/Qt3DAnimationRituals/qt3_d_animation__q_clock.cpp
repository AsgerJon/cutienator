//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qclock.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qclock.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DAnimation::QClock that Python can take functions over in. Every Qt3DAnimation::QClock
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QClockCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DAnimation_QClockCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClockCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClockCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClockCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClockCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DAnimation_QClockCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DAnimation_QClock : public Qt3DAnimation::QClock {
public:
  using Qt3DAnimation::QClock::QClock;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QClockCall0 call = reinterpret_cast<CuteQt3DAnimation_QClockCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QClockCall1 call = reinterpret_cast<CuteQt3DAnimation_QClockCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_QClockCall2 call = reinterpret_cast<CuteQt3DAnimation_QClockCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DAnimation_QClockCall3 call = reinterpret_cast<CuteQt3DAnimation_QClockCall3>(taken[3]);
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
      CuteQt3DAnimation_QClockCall4 call = reinterpret_cast<CuteQt3DAnimation_QClockCall4>(taken[4]);
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
      CuteQt3DAnimation_QClockCall5 call = reinterpret_cast<CuteQt3DAnimation_QClockCall5>(taken[5]);
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
      CuteQt3DAnimation_QClockCall6 call = reinterpret_cast<CuteQt3DAnimation_QClockCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DAnimation::QClock::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13Qt3DAnimation6QClock10metaObjectEv(
    const Qt3DAnimation::QClock *self) {
  return self->metaObject();
}

//  void *Qt3DAnimation::QClock::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13Qt3DAnimation6QClock11qt_metacastEPKc(
    Qt3DAnimation::QClock *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DAnimation::QClock::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13Qt3DAnimation6QClock11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DAnimation::QClock *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DAnimation::QClock::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13Qt3DAnimation6QClock2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DAnimation::QClock::tr(s, c, n));
}

//  Qt3DAnimation::QClock::QClock(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClock *ritual_ZN13Qt3DAnimation6QClockC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QClock(parent);
}

//  Qt3DAnimation::QClock::~QClock()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation6QClockD1Ev(Qt3DAnimation::QClock *self) {
  delete self;
}

//  double Qt3DAnimation::QClock::playbackRate() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation6QClock12playbackRateEv(
    const Qt3DAnimation::QClock *self) {
  return self->playbackRate();
}

//  void Qt3DAnimation::QClock::setPlaybackRate(double playbackRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation6QClock15setPlaybackRateEd(
    Qt3DAnimation::QClock *self,
    double playbackRate) {
  self->setPlaybackRate(playbackRate);
}

//  void Qt3DAnimation::QClock::playbackRateChanged(double playbackRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation6QClock19playbackRateChangedEd(
    Qt3DAnimation::QClock *self,
    double playbackRate) {
  self->playbackRateChanged(playbackRate);
}

//  Qt3DAnimation::QClock::QClock(QClockPrivate &dd, Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClock *ritual_ZN13Qt3DAnimation6QClockC1ERNS_13QClockPrivateEPN8Qt3DCore5QNodeE(
    Qt3DAnimation::QClockPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DAnimation_QClock(*dd, parent);
}

//  QClockPrivate *Qt3DAnimation::QClock::d_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QClockPrivate *ritual_ZN13Qt3DAnimation6QClock6d_funcEv(
    Qt3DAnimation::QClock *self) {
  return self->d_func();
}

//  const QClockPrivate *Qt3DAnimation::QClock::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QClockPrivate *ritual_ZNK13Qt3DAnimation6QClock6d_funcEv(
    const Qt3DAnimation::QClock *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DAnimation_QClock, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QClock(
    Qt3DAnimation::QClock *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QClock *>(self)->take(key, call);
}
