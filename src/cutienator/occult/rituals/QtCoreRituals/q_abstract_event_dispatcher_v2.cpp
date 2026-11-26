//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>
#include <QtCore/QAbstractEventDispatcher>

//  A QAbstractEventDispatcherV2 that Python can take functions over in. Every QAbstractEventDispatcherV2
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQAbstractEventDispatcherV2Call0)(const void *, int, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQAbstractEventDispatcherV2Call1)(const void *, int, const QDeadlineTimer *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQAbstractEventDispatcherV2Call2)(const void *, int, int *);
typedef void (*CuteQAbstractEventDispatcherV2Call3)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQAbstractEventDispatcherV2Call4)(const void *, QSocketNotifier *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQAbstractEventDispatcherV2Call5)(const void *, QObject *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQAbstractEventDispatcherV2Call6)(const void *, int *);
typedef void (*CuteQAbstractEventDispatcherV2Call7)(const void *, int *);
typedef void (*CuteQAbstractEventDispatcherV2Call8)(const void *, int *);
typedef void (*CuteQAbstractEventDispatcherV2Call9)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractEventDispatcherV2Call10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractEventDispatcherV2Call11)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherV2Call12)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherV2Call13)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherV2Call14)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherV2Call15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherV2Call16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractEventDispatcherV2 : public QAbstractEventDispatcherV2 {
public:
  using QAbstractEventDispatcherV2::QAbstractEventDispatcherV2;
  void *taken[17] = {};

  bool take(const char *key, void *call) {
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher15unregisterTimerEN2Qt7TimerIdE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher22registerSocketNotifierEP15QSocketNotifier")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher24unregisterSocketNotifierEP15QSocketNotifier")) {
      taken[4] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher16unregisterTimersEP7QObject")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher6wakeUpEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher9interruptEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[9] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::unregisterTimer(Qt::TimerId timerId)
  bool unregisterTimer(Qt::TimerId timerId) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call0 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call0>(taken[0]);
      bool given = call(this, static_cast<int>(timerId), &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop
  //      ::ProcessEventsFlags flags, QDeadlineTimer deadline)
  bool processEventsWithDeadline(
      QEventLoop::ProcessEventsFlags flags,
      QDeadlineTimer deadline) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call1 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &deadline, &handled);
      if (handled) return given;
    }
    return QAbstractEventDispatcherV2::processEventsWithDeadline(flags, deadline);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  bool QAbstractEventDispatcher::processEvents(QEventLoop::ProcessEvent
  //      sFlags flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call2 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call2>(taken[2]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAbstractEventDispatcher::registerSocketNotifier(QSocketNotifier
  //      *notifier)
  void registerSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call3 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call3>(taken[3]);
      call(this, notifier, &handled);
      if (handled) return;
    }
  }

  //  void
  //      QAbstractEventDispatcher::unregisterSocketNotifier(QSocketNotifie
  //      r *notifier)
  void unregisterSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call4 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call4>(taken[4]);
      call(this, notifier, &handled);
      if (handled) return;
    }
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcher::unregisterTimers(QObject *object)
  bool unregisterTimers(QObject *object) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call5 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call5>(taken[5]);
      bool given = call(this, object, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QAbstractEventDispatcher::wakeUp()
  void wakeUp() override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call6 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractEventDispatcher::interrupt()
  void interrupt() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call7 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractEventDispatcher::startingUp()
  void startingUp() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call8 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::startingUp();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call9 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call10 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call10>(taken[10]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call11 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call11>(taken[11]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call12 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call13 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call14 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call15 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractEventDispatcherV2Call16 call = reinterpret_cast<CuteQAbstractEventDispatcherV2Call16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractEventDispatcherV2::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QAbstractEventDispatcherV210metaObjectEv(
    const QAbstractEventDispatcherV2 *self) {
  return self->metaObject();
}

//  void *QAbstractEventDispatcherV2::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN26QAbstractEventDispatcherV211qt_metacastEPKc(
    QAbstractEventDispatcherV2 *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractEventDispatcherV2::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QAbstractEventDispatcherV211qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractEventDispatcherV2 *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractEventDispatcherV2::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QAbstractEventDispatcherV22trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractEventDispatcherV2::tr(s, c, n));
}

//  QAbstractEventDispatcherPrivate *QAbstractEventDispatcherV2::d_func()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcherPrivate *ritual_ZN26QAbstractEventDispatcherV26d_funcEv(
    QAbstractEventDispatcherV2 *self) {
  return self->d_func();
}

//  const QAbstractEventDispatcherPrivate
//      *QAbstractEventDispatcherV2::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractEventDispatcherPrivate *ritual_ZNK26QAbstractEventDispatcherV26d_funcEv(
    const QAbstractEventDispatcherV2 *self) {
  return self->d_func();
}

//  QAbstractEventDispatcherV2::~QAbstractEventDispatcherV2()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractEventDispatcherV2D1Ev(
    QAbstractEventDispatcherV2 *self) {
  delete self;
}

//  void QAbstractEventDispatcherV2::registerTimer(Qt::TimerId timerId,
//      Duration interval, Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractEventDispatcherV213registerTimerEN2Qt7TimerIdENSt6chrono8durationIlSt5ratioILl1ELl1000000000EEEENS0_9TimerTypeEP7QObject(
    QAbstractEventDispatcherV2 *self,
    Qt::TimerId timerId,
    long long interval,
    Qt::TimerType timerType,
    QObject *object) {
  self->registerTimer(
      timerId,
      QAbstractEventDispatcher::Duration(interval),
      timerType,
      object);
}

//  bool QAbstractEventDispatcherV2::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractEventDispatcherV215unregisterTimerEN2Qt7TimerIdE(
    QAbstractEventDispatcherV2 *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  QList<TimerInfoV2> QAbstractEventDispatcherV2::timersForObject(QObject
//      *object) const
extern "C" Q_DECL_EXPORT
QList<QAbstractEventDispatcher::TimerInfoV2> *ritual_ZNK26QAbstractEventDispatcherV215timersForObjectEP7QObject(
    const QAbstractEventDispatcherV2 *self,
    QObject *object) {
  return new QList<QAbstractEventDispatcher::TimerInfoV2>(
      self->timersForObject(
          object));
}

//  Duration QAbstractEventDispatcherV2::remainingTime(Qt::TimerId timerId)
//      const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK26QAbstractEventDispatcherV213remainingTimeEN2Qt7TimerIdE(
    const QAbstractEventDispatcherV2 *self,
    Qt::TimerId timerId) {
  return static_cast<long long>(self->remainingTime(timerId).count());
}

//  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop::Pr
//      ocessEventsFlags flags, QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer(
    QAbstractEventDispatcherV2 *self,
    int flags,
    const QDeadlineTimer *deadline) {
  return self->processEventsWithDeadline(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}

//  void QAbstractEventDispatcherV2::registerTimer(int timerId, qint64
//      interval, Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractEventDispatcherV213registerTimerEixN2Qt9TimerTypeEP7QObject(
    QAbstractEventDispatcherV2 *self,
    int timerId,
    qint64 interval,
    Qt::TimerType timerType,
    QObject *object) {
  self->registerTimer(timerId, interval, timerType, object);
}

//  bool QAbstractEventDispatcherV2::unregisterTimer(int timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QAbstractEventDispatcherV215unregisterTimerEi(
    QAbstractEventDispatcherV2 *self,
    int timerId) {
  return self->unregisterTimer(timerId);
}

//  QList<TimerInfo> QAbstractEventDispatcherV2::registeredTimers(QObject
//      *object) const
extern "C" Q_DECL_EXPORT
QList<QAbstractEventDispatcher::TimerInfo> *ritual_ZNK26QAbstractEventDispatcherV216registeredTimersEP7QObject(
    const QAbstractEventDispatcherV2 *self,
    QObject *object) {
  return new QList<QAbstractEventDispatcher::TimerInfo>(
      self->registeredTimers(
          object));
}

//  int QAbstractEventDispatcherV2::remainingTime(int timerId)
extern "C" Q_DECL_EXPORT
int ritual_ZN26QAbstractEventDispatcherV213remainingTimeEi(
    QAbstractEventDispatcherV2 *self,
    int timerId) {
  return self->remainingTime(timerId);
}

//  a Python function taken by a CuteQAbstractEventDispatcherV2, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractEventDispatcherV2(
    QAbstractEventDispatcherV2 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractEventDispatcherV2 *>(self)->take(key, call);
}

//  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop::Pr
//      ocessEventsFlags flags, QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer(
    QAbstractEventDispatcherV2 *self,
    int flags,
    const QDeadlineTimer *deadline) {
  return self->QAbstractEventDispatcherV2::processEventsWithDeadline(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags),
      *deadline);
}

//  a QList<QAbstractEventDispatcher::TimerInfoV2> a ritual of
//      QAbstractEventDispatcherV2 gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractEventDispatcherV2__QList_QAbstractEventDispatcher_TimerInfoV2(
    QList<QAbstractEventDispatcher::TimerInfoV2> *self) {
  delete self;
}

//  a QList<QAbstractEventDispatcher::TimerInfo> a ritual of
//      QAbstractEventDispatcherV2 gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractEventDispatcherV2__QList_QAbstractEventDispatcher_TimerInfo(
    QList<QAbstractEventDispatcher::TimerInfo> *self) {
  delete self;
}

#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
