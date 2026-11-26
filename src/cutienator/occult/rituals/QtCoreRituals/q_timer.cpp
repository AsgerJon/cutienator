//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if !defined(QT_NO_QOBJECT)
#include <QtCore/qtimer.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QBindable>
#include <QtCore/Qt>

//  Only a class built on QTimer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTimer : QTimer {
  using QTimer::timerEvent;
};

//  A QTimer that Python can take functions over in. Every QTimer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimerCall0)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTimerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTimerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTimerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTimer : public QTimer {
public:
  using QTimer::QTimer;
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
      CuteQTimerCall0 call = reinterpret_cast<CuteQTimerCall0>(taken[0]);
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
      CuteQTimerCall1 call = reinterpret_cast<CuteQTimerCall1>(taken[1]);
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
      CuteQTimerCall2 call = reinterpret_cast<CuteQTimerCall2>(taken[2]);
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
      CuteQTimerCall3 call = reinterpret_cast<CuteQTimerCall3>(taken[3]);
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
      CuteQTimerCall4 call = reinterpret_cast<CuteQTimerCall4>(taken[4]);
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
      CuteQTimerCall5 call = reinterpret_cast<CuteQTimerCall5>(taken[5]);
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
      CuteQTimerCall6 call = reinterpret_cast<CuteQTimerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTimer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK6QTimer10metaObjectEv(const QTimer *self) {
  return self->metaObject();
}

//  void *QTimer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN6QTimer11qt_metacastEPKc(QTimer *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTimer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QTimer11qt_metacallEN11QMetaObject4CallEiPPv(
    QTimer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTimer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN6QTimer2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QTimer::tr(s, c, n));
}

//  QTimer::QTimer(QObject *parent)
extern "C" Q_DECL_EXPORT
QTimer *ritual_ZN6QTimerC1EP7QObject(QObject *parent) {
  return new CuteQTimer(parent);
}

//  QTimer::~QTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimerD1Ev(QTimer *self) {
  delete self;
}

//  bool QTimer::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QTimer8isActiveEv(const QTimer *self) {
  return self->isActive();
}

//  QBindable<bool> QTimer::bindableActive()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN6QTimer14bindableActiveEv(QTimer *self) {
  return new QBindable<bool>(self->bindableActive());
}

//  int QTimer::timerId() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QTimer7timerIdEv(const QTimer *self) {
  return self->timerId();
}

//  Qt::TimerId QTimer::id() const
extern "C" Q_DECL_EXPORT
Qt::TimerId ritual_ZNK6QTimer2idEv(const QTimer *self) {
  return self->id();
}

//  void QTimer::setInterval(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer11setIntervalEi(QTimer *self, int msec) {
  self->setInterval(msec);
}

//  int QTimer::interval() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QTimer8intervalEv(const QTimer *self) {
  return self->interval();
}

//  QBindable<int> QTimer::bindableInterval()
extern "C" Q_DECL_EXPORT
QBindable<int> *ritual_ZN6QTimer16bindableIntervalEv(QTimer *self) {
  return new QBindable<int>(self->bindableInterval());
}

//  int QTimer::remainingTime() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QTimer13remainingTimeEv(const QTimer *self) {
  return self->remainingTime();
}

//  void QTimer::setTimerType(Qt::TimerType atype)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer12setTimerTypeEN2Qt9TimerTypeE(
    QTimer *self,
    Qt::TimerType atype) {
  self->setTimerType(atype);
}

//  Qt::TimerType QTimer::timerType() const
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZNK6QTimer9timerTypeEv(const QTimer *self) {
  return self->timerType();
}

//  QBindable<Qt::TimerType> QTimer::bindableTimerType()
extern "C" Q_DECL_EXPORT
QBindable<Qt::TimerType> *ritual_ZN6QTimer17bindableTimerTypeEv(
    QTimer *self) {
  return new QBindable<Qt::TimerType>(self->bindableTimerType());
}

//  void QTimer::setSingleShot(bool singleShot)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer13setSingleShotEb(QTimer *self, bool singleShot) {
  self->setSingleShot(singleShot);
}

//  bool QTimer::isSingleShot() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QTimer12isSingleShotEv(const QTimer *self) {
  return self->isSingleShot();
}

//  QBindable<bool> QTimer::bindableSingleShot()
extern "C" Q_DECL_EXPORT
QBindable<bool> *ritual_ZN6QTimer18bindableSingleShotEv(QTimer *self) {
  return new QBindable<bool>(self->bindableSingleShot());
}

//  void QTimer::singleShot(int msec, const QObject *receiver, const char
//      *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10singleShotEiPK7QObjectPKc(
    int msec,
    const QObject *receiver,
    const char *member) {
  QTimer::singleShot(msec, receiver, member);
}

//  void QTimer::singleShot(int msec, Qt::TimerType timerType, const QObject
//      *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10singleShotEiN2Qt9TimerTypeEPK7QObjectPKc(
    int msec,
    Qt::TimerType timerType,
    const QObject *receiver,
    const char *member) {
  QTimer::singleShot(msec, timerType, receiver, member);
}

//  void QTimer::start(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer5startEi(QTimer *self, int msec) {
  self->start(msec);
}

//  void QTimer::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer5startEv(QTimer *self) {
  self->start();
}

//  void QTimer::stop()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer4stopEv(QTimer *self) {
  self->stop();
}

//  void QTimer::timeout(QPrivateSignal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer7timeoutENS_14QPrivateSignalE(QTimer *self) {
  self->timeout(QTimer::QPrivateSignal());
}

//  void QTimer::setInterval(std::chrono::milliseconds value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer11setIntervalENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QTimer *self,
    long long value) {
  self->setInterval(std::chrono::milliseconds(value));
}

//  std::chrono::milliseconds QTimer::intervalAsDuration() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK6QTimer18intervalAsDurationEv(const QTimer *self) {
  return static_cast<long long>(self->intervalAsDuration().count());
}

//  std::chrono::milliseconds QTimer::remainingTimeAsDuration() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK6QTimer23remainingTimeAsDurationEv(const QTimer *self) {
  return static_cast<long long>(self->remainingTimeAsDuration().count());
}

//  void QTimer::singleShot(std::chrono::nanoseconds value, const QObject
//      *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10singleShotENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEPK7QObjectPKc(
    long long value,
    const QObject *receiver,
    const char *member) {
  QTimer::singleShot(std::chrono::nanoseconds(value), receiver, member);
}

//  void QTimer::singleShot(std::chrono::nanoseconds interval, Qt::TimerType
//      timerType, const QObject *receiver, const char *member)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10singleShotENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObjectPKc(
    long long interval,
    Qt::TimerType timerType,
    const QObject *receiver,
    const char *member) {
  QTimer::singleShot(
      std::chrono::nanoseconds(interval),
      timerType,
      receiver,
      member);
}

//  void QTimer::start(std::chrono::milliseconds value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer5startENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    QTimer *self,
    long long value) {
  self->start(std::chrono::milliseconds(value));
}

//  void QTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer10timerEventEP11QTimerEvent(
    QTimer *self,
    QTimerEvent *a0) {
  self->timerEvent(a0);
}

//  QTimerPrivate *QTimer::d_func()
extern "C" Q_DECL_EXPORT
QTimerPrivate *ritual_ZN6QTimer6d_funcEv(QTimer *self) {
  return self->d_func();
}

//  const QTimerPrivate *QTimer::d_func() const
extern "C" Q_DECL_EXPORT
const QTimerPrivate *ritual_ZNK6QTimer6d_funcEv(const QTimer *self) {
  return self->d_func();
}

//  std::chrono::nanoseconds QTimer::from_msecs(std::chrono::milliseconds a0)
extern "C" Q_DECL_EXPORT
long long ritual_ZN6QTimer10from_msecsENSt6chrono8durationIlSt5ratioILl1ELl1000EEEE(
    long long a0) {
  return static_cast<long long>(
      QTimer::from_msecs(
          std::chrono::milliseconds(a0)).count());
}

//  std::chrono::nanoseconds QTimer::toDuration(int msecs)
extern "C" Q_DECL_EXPORT
long long ritual_ZN6QTimer10toDurationEi(int msecs) {
  return static_cast<long long>(QTimer::toDuration(msecs).count());
}

//  std::chrono::nanoseconds QTimer::toDuration(std::chrono::nanoseconds ns)
extern "C" Q_DECL_EXPORT
long long ritual_ZN6QTimer10toDurationENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEE(
    long long ns) {
  return static_cast<long long>(
      QTimer::toDuration(
          std::chrono::nanoseconds(ns)).count());
}

//  int QTimer::startTimer(int a0)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QTimer10startTimerEi(QTimer *self, int a0) {
  return self->startTimer(a0);
}

//  void QTimer::killTimer(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer9killTimerEi(QTimer *self, int a0) {
  self->killTimer(a0);
}

//  Qt::TimerType QTimer::defaultTypeFor(int msecs)
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZN6QTimer14defaultTypeForEi(int msecs) {
  return QTimer::defaultTypeFor(msecs);
}

//  Qt::TimerType QTimer::defaultTypeFor(std::chrono::nanoseconds interval)
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZN6QTimer14defaultTypeForENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEE(
    long long interval) {
  return QTimer::defaultTypeFor(std::chrono::nanoseconds(interval));
}

//  void QTimer::singleShotImpl(std::chrono::nanoseconds interval,
//      Qt::TimerType timerType, const QObject *receiver,
//      QtPrivate::QSlotObjectBase *slotObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QTimer14singleShotImplENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEEN2Qt9TimerTypeEPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    long long interval,
    Qt::TimerType timerType,
    const QObject *receiver,
    QtPrivate::QSlotObjectBase *slotObj) {
  QTimer::singleShotImpl(
      std::chrono::nanoseconds(interval),
      timerType,
      receiver,
      slotObj);
}

//  a Python function taken by a CuteQTimer, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTimer(QTimer *self, const char *key, void *call) {
  return static_cast<CuteQTimer *>(self)->take(key, call);
}

//  void QTimer::timerEvent(QTimerEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN6QTimer10timerEventEP11QTimerEvent(
    QTimer *self,
    QTimerEvent *a0) {
  static_cast<OwnQTimer *>(self)->OwnQTimer::timerEvent(a0);
}

//  a QBindable<bool> a ritual of QTimer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimer__QBindable_bool(QBindable<bool> *self) {
  delete self;
}

//  a QBindable<int> a ritual of QTimer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimer__QBindable_int(QBindable<int> *self) {
  delete self;
}

//  a QBindable<Qt::TimerType> a ritual of QTimer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTimer__QBindable_Qt_TimerType(
    QBindable<Qt::TimerType> *self) {
  delete self;
}

#endif  // !defined(QT_NO_QOBJECT)
