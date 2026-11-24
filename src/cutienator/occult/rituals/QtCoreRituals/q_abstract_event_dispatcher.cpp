//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstracteventdispatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractEventDispatcher that Python can take functions over in. Every QAbstractEventDispatcher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQAbstractEventDispatcherCall0)(const void *, int, int *);
typedef void (*CuteQAbstractEventDispatcherCall1)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQAbstractEventDispatcherCall2)(const void *, QSocketNotifier *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQAbstractEventDispatcherCall3)(const void *, int, qint64, int, QObject *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQAbstractEventDispatcherCall4)(const void *, int, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQAbstractEventDispatcherCall5)(const void *, QObject *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef int (*CuteQAbstractEventDispatcherCall6)(const void *, int, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQAbstractEventDispatcherCall7)(const void *, int *);
typedef void (*CuteQAbstractEventDispatcherCall8)(const void *, int *);
typedef void (*CuteQAbstractEventDispatcherCall9)(const void *, int *);
typedef void (*CuteQAbstractEventDispatcherCall10)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractEventDispatcherCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractEventDispatcherCall12)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherCall13)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherCall14)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherCall15)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherCall16)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractEventDispatcherCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractEventDispatcher : public QAbstractEventDispatcher {
public:
  using QAbstractEventDispatcher::QAbstractEventDispatcher;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher22registerSocketNotifierEP15QSocketNotifier")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher24unregisterSocketNotifierEP15QSocketNotifier")) {
      taken[2] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13registerTimerEixN2Qt9TimerTypeEP7QObject")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher15unregisterTimerEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher16unregisterTimersEP7QObject")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13remainingTimeEi")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher6wakeUpEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher9interruptEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QAbstractEventDispatcher::processEvents(QEventLoop::ProcessEvent
  //      sFlags flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall0 call = reinterpret_cast<CuteQAbstractEventDispatcherCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAbstractEventDispatcher::registerSocketNotifier(QSocketNotifier
  //      *notifier)
  void registerSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall1 call = reinterpret_cast<CuteQAbstractEventDispatcherCall1>(taken[1]);
      call(this, notifier, &handled);
      if (handled) return;
    }
  }

  //  void
  //      QAbstractEventDispatcher::unregisterSocketNotifier(QSocketNotifie
  //      r *notifier)
  void unregisterSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall2 call = reinterpret_cast<CuteQAbstractEventDispatcherCall2>(taken[2]);
      call(this, notifier, &handled);
      if (handled) return;
    }
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  void QAbstractEventDispatcher::registerTimer(int timerId, qint64
  //      interval, Qt::TimerType timerType, QObject *object)
  void registerTimer(
      int timerId,
      qint64 interval,
      Qt::TimerType timerType,
      QObject *object) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall3 call = reinterpret_cast<CuteQAbstractEventDispatcherCall3>(taken[3]);
      call(this, timerId, interval, static_cast<int>(timerType), object, &handled);
      if (handled) return;
    }
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcher::unregisterTimer(int timerId)
  bool unregisterTimer(int timerId) override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall4 call = reinterpret_cast<CuteQAbstractEventDispatcherCall4>(taken[4]);
      bool given = call(this, timerId, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcher::unregisterTimers(QObject *object)
  bool unregisterTimers(QObject *object) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall5 call = reinterpret_cast<CuteQAbstractEventDispatcherCall5>(taken[5]);
      bool given = call(this, object, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  int QAbstractEventDispatcher::remainingTime(int timerId)
  int remainingTime(int timerId) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall6 call = reinterpret_cast<CuteQAbstractEventDispatcherCall6>(taken[6]);
      int given = call(this, timerId, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QAbstractEventDispatcher::wakeUp()
  void wakeUp() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall7 call = reinterpret_cast<CuteQAbstractEventDispatcherCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractEventDispatcher::interrupt()
  void interrupt() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall8 call = reinterpret_cast<CuteQAbstractEventDispatcherCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractEventDispatcher::startingUp()
  void startingUp() override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall9 call = reinterpret_cast<CuteQAbstractEventDispatcherCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::startingUp();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall10 call = reinterpret_cast<CuteQAbstractEventDispatcherCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall11 call = reinterpret_cast<CuteQAbstractEventDispatcherCall11>(taken[11]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall12 call = reinterpret_cast<CuteQAbstractEventDispatcherCall12>(taken[12]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall13 call = reinterpret_cast<CuteQAbstractEventDispatcherCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall14 call = reinterpret_cast<CuteQAbstractEventDispatcherCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall15 call = reinterpret_cast<CuteQAbstractEventDispatcherCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall16 call = reinterpret_cast<CuteQAbstractEventDispatcherCall16>(taken[16]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractEventDispatcherCall17 call = reinterpret_cast<CuteQAbstractEventDispatcherCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractEventDispatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QAbstractEventDispatcher10metaObjectEv(
    const QAbstractEventDispatcher *self) {
  return self->metaObject();
}

//  QString QAbstractEventDispatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QAbstractEventDispatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractEventDispatcher::tr(s, c, n));
}

//  QAbstractEventDispatcherPrivate *QAbstractEventDispatcher::d_func()
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcherPrivate *ritual_ZN24QAbstractEventDispatcher6d_funcEv(
    QAbstractEventDispatcher *self) {
  return self->d_func();
}

//  const QAbstractEventDispatcherPrivate *QAbstractEventDispatcher::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QAbstractEventDispatcherPrivate *ritual_ZNK24QAbstractEventDispatcher6d_funcEv(
    const QAbstractEventDispatcher *self) {
  return self->d_func();
}

//  QAbstractEventDispatcher::~QAbstractEventDispatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcherD1Ev(
    QAbstractEventDispatcher *self) {
  delete self;
}

//  QAbstractEventDispatcher *QAbstractEventDispatcher::instance(QThread
//      *thread)
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZN24QAbstractEventDispatcher8instanceEP7QThread(
    QThread *thread) {
  return QAbstractEventDispatcher::instance(thread);
}

//  bool
//      QAbstractEventDispatcher::processEvents(QEventLoop::ProcessEventsFlag
//      s flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QAbstractEventDispatcher *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QAbstractEventDispatcher::registerSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher22registerSocketNotifierEP15QSocketNotifier(
    QAbstractEventDispatcher *self,
    QSocketNotifier *notifier) {
  self->registerSocketNotifier(notifier);
}

//  void QAbstractEventDispatcher::unregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher24unregisterSocketNotifierEP15QSocketNotifier(
    QAbstractEventDispatcher *self,
    QSocketNotifier *notifier) {
  self->unregisterSocketNotifier(notifier);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  int QAbstractEventDispatcher::registerTimer(qint64 interval,
//      Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QAbstractEventDispatcher13registerTimerExN2Qt9TimerTypeEP7QObject(
    QAbstractEventDispatcher *self,
    qint64 interval,
    Qt::TimerType timerType,
    QObject *object) {
  return self->registerTimer(interval, timerType, object);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QAbstractEventDispatcher::registerTimer(int timerId, qint64
//      interval, Qt::TimerType timerType, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher13registerTimerEixN2Qt9TimerTypeEP7QObject(
    QAbstractEventDispatcher *self,
    int timerId,
    qint64 interval,
    Qt::TimerType timerType,
    QObject *object) {
  self->registerTimer(timerId, interval, timerType, object);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QAbstractEventDispatcher::unregisterTimer(int timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher15unregisterTimerEi(
    QAbstractEventDispatcher *self,
    int timerId) {
  return self->unregisterTimer(timerId);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QAbstractEventDispatcher::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher16unregisterTimersEP7QObject(
    QAbstractEventDispatcher *self,
    QObject *object) {
  return self->unregisterTimers(object);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  int QAbstractEventDispatcher::remainingTime(int timerId)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QAbstractEventDispatcher13remainingTimeEi(
    QAbstractEventDispatcher *self,
    int timerId) {
  return self->remainingTime(timerId);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QAbstractEventDispatcher::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractEventDispatcher15unregisterTimerEN2Qt7TimerIdE(
    QAbstractEventDispatcher *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QAbstractEventDispatcher::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher6wakeUpEv(
    QAbstractEventDispatcher *self) {
  self->wakeUp();
}

//  void QAbstractEventDispatcher::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher9interruptEv(
    QAbstractEventDispatcher *self) {
  self->interrupt();
}

//  void QAbstractEventDispatcher::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher10startingUpEv(
    QAbstractEventDispatcher *self) {
  self->startingUp();
}

//  void QAbstractEventDispatcher::closingDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher11closingDownEv(
    QAbstractEventDispatcher *self) {
  self->closingDown();
}

//  void QAbstractEventDispatcher::installNativeEventFilter(QAbstractNativeEv
//      entFilter *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher24installNativeEventFilterEP26QAbstractNativeEventFilter(
    QAbstractEventDispatcher *self,
    QAbstractNativeEventFilter *filterObj) {
  self->installNativeEventFilter(filterObj);
}

//  void QAbstractEventDispatcher::removeNativeEventFilter(QAbstractNativeEve
//      ntFilter *filterObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractEventDispatcher23removeNativeEventFilterEP26QAbstractNativeEventFilter(
    QAbstractEventDispatcher *self,
    QAbstractNativeEventFilter *filterObj) {
  self->removeNativeEventFilter(filterObj);
}

//  a Python function taken by a CuteQAbstractEventDispatcher, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractEventDispatcher(
    QAbstractEventDispatcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractEventDispatcher *>(self)->take(key, call);
}

//  void QAbstractEventDispatcher::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractEventDispatcher10startingUpEv(
    QAbstractEventDispatcher *self) {
  self->QAbstractEventDispatcher::startingUp();
}

//  void QAbstractEventDispatcher::closingDown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractEventDispatcher11closingDownEv(
    QAbstractEventDispatcher *self) {
  self->QAbstractEventDispatcher::closingDown();
}
