//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qchronotimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(QT_NO_QOBJECT)
#include <QtCore/qchronotimer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>
#include <chrono>
#include <QtCore/Qt>

//  Only a class built on QChronoTimer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQChronoTimer : QChronoTimer {
  using QChronoTimer::timerEvent;
};

//  A QChronoTimer that Python can take functions over in. Every QChronoTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChronoTimerCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQChronoTimerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQChronoTimerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChronoTimerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChronoTimerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChronoTimerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQChronoTimerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQChronoTimer : public QChronoTimer {
public:
  using QChronoTimer::QChronoTimer;
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
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
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QChronoTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QChronoTimer10metaObjectEv(
    const QChronoTimer *self) {
  return self->metaObject();
}

//  void *QChronoTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QChronoTimer11qt_metacastEPKc(
    QChronoTimer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QChronoTimer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QChronoTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QChronoTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QChronoTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QChronoTimer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QChronoTimer::tr(s, c, n));
}

//  QChronoTimer::QChronoTimer(std::chrono::nanoseconds nsec, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QChronoTimer *ritual_ZN12QChronoTimerC1ENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEP7QObject(
    long long nsec,
    QObject *parent) {
  return new CuteQChronoTimer(std::chrono::nanoseconds(nsec), parent);
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

//  QBindable<bool> QChronoTimer::bindableActive()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN12QChronoTimer14bindableActiveEv(
    QChronoTimer *self) {
  return new QBindable<bool>(self->bindableActive());
}

//  Qt::TimerId QChronoTimer::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK12QChronoTimer2idEv(const QChronoTimer *self) {
  return self->id();
}

//  void QChronoTimer::setInterval(std::chrono::nanoseconds nsec)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer11setIntervalENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEE(
    QChronoTimer *self,
    long long nsec) {
  self->setInterval(std::chrono::nanoseconds(nsec));
}

//  std::chrono::nanoseconds QChronoTimer::interval() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK12QChronoTimer8intervalEv(const QChronoTimer *self) {
  return static_cast<long long>(self->interval().count());
}

//  QBindable<std::chrono::nanoseconds> QChronoTimer::bindableInterval()
extern "C" Q_DECL_EXPORT
QBindable<std::chrono::nanoseconds> *ritual_ZN12QChronoTimer16bindableIntervalEv(
    QChronoTimer *self) {
  return new QBindable<std::chrono::nanoseconds>(self->bindableInterval());
}

//  std::chrono::nanoseconds QChronoTimer::remainingTime() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK12QChronoTimer13remainingTimeEv(
    const QChronoTimer *self) {
  return static_cast<long long>(self->remainingTime().count());
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

//  QBindable<Qt::TimerType> QChronoTimer::bindableTimerType()
extern "C" Q_DECL_EXPORT
QBindable<Qt::TimerType> *ritual_ZN12QChronoTimer17bindableTimerTypeEv(
    QChronoTimer *self) {
  return new QBindable<Qt::TimerType>(self->bindableTimerType());
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

//  QBindable<bool> QChronoTimer::bindableSingleShot()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN12QChronoTimer18bindableSingleShotEv(
    QChronoTimer *self) {
  return new QBindable<bool>(self->bindableSingleShot());
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

//  void QChronoTimer::timeout(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer7timeoutENS_14QPrivateSignalE(
    QChronoTimer *self) {
  self->timeout(QChronoTimer::QPrivateSignal());
}

//  void QChronoTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QChronoTimer10timerEventEP11QTimerEvent(
    QChronoTimer *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  QTimerPrivate *QChronoTimer::d_func()
extern "C" Q_DECL_EXPORT
QTimerPrivate *ritual_ZN12QChronoTimer6d_funcEv(QChronoTimer *self) {
  return self->d_func();
}

//  const QTimerPrivate *QChronoTimer::d_func() const
extern "C" Q_DECL_EXPORT
const QTimerPrivate *ritual_ZNK12QChronoTimer6d_funcEv(
    const QChronoTimer *self) {
  return self->d_func();
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

//  a QBindable<bool> a ritual of QChronoTimer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QChronoTimer__QBindable_bool(QBindable<bool> *self) {
  delete self;
}

//  a QBindable<std::chrono::nanoseconds> a ritual of QChronoTimer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QChronoTimer__QBindable_std_chrono_nanoseconds(
    QBindable<std::chrono::nanoseconds> *self) {
  delete self;
}

//  a QBindable<Qt::TimerType> a ritual of QChronoTimer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QChronoTimer__QBindable_Qt_TimerType(
    QBindable<Qt::TimerType> *self) {
  delete self;
}

#endif  // !defined(QT_NO_QOBJECT)
