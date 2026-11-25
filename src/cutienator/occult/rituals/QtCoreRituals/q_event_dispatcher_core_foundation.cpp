//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_cf_p.h, Qt 6.12.0, as
//  the Qt of macOS installs it. Kept as it is when the generator runs
//  again.
//  A 'CFRunLoopTimerRef' is passed as an address. Not written, as for
//  'QEventDispatcherUNIX': 'registerTimer', 'remainingTime' and
//  'timersForObject'; and 'handleRunLoopActivity', whose
//  'CFRunLoopActivity' the SDKs of Apple spell in more than one way.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_DARWIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_cf_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  Only a class built on QEventDispatcherCoreFoundation may call these
//  functions of it. This one is, and makes them free for the rituals to
//  call.
struct OwnQEventDispatcherCoreFoundation : QEventDispatcherCoreFoundation {
  using QEventDispatcherCoreFoundation::processPostedEvents;
};

//  A QEventDispatcherCoreFoundation that Python can take functions over in. Every
//  QEventDispatcherCoreFoundation Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef void (*CuteQEventDispatcherCoreFoundationCall0)(const void *, int *);
typedef bool (*CuteQEventDispatcherCoreFoundationCall1)(const void *, int, int *);
typedef void (*CuteQEventDispatcherCoreFoundationCall2)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQEventDispatcherCoreFoundationCall3)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQEventDispatcherCoreFoundationCall4)(const void *, int *);
typedef void (*CuteQEventDispatcherCoreFoundationCall5)(const void *, int *);
typedef bool (*CuteQEventDispatcherCoreFoundationCall6)(const void *, int *);
typedef void (*CuteQEventDispatcherCoreFoundationCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherCoreFoundationCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherCoreFoundationCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherCoreFoundationCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherCoreFoundationCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherCoreFoundationCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherCoreFoundationCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherCoreFoundationCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQEventDispatcherCoreFoundation : public QEventDispatcherCoreFoundation {
public:
  using QEventDispatcherCoreFoundation::QEventDispatcherCoreFoundation;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher22registerSocketNotifierEP15QSocketNotifier")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher24unregisterSocketNotifierEP15QSocketNotifier")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher6wakeUpEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher9interruptEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN30QEventDispatcherCoreFoundation19processPostedEventsEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QEventDispatcherCoreFoundation::startingUp()
  void startingUp() override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall0 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherCoreFoundation::startingUp();
  }

  //  bool QEventDispatcherCoreFoundation::processEvents(QEventLoop::ProcessE
  //      ventsFlags flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall1 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QEventDispatcherCoreFoundation::processEvents(flags);
  }

  //  void
  //      QEventDispatcherCoreFoundation::registerSocketNotifier(QSocketNotif
  //      ier *notifier)
  void registerSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[2]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall2 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall2>(taken[2]);
      call(this, notifier, &handled);
      if (handled) return;
    }
    QEventDispatcherCoreFoundation::registerSocketNotifier(notifier);
  }

  //  void QEventDispatcherCoreFoundation::unregisterSocketNotifier(QSocketNo
  //      tifier *notifier)
  void unregisterSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[3]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall3 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall3>(taken[3]);
      call(this, notifier, &handled);
      if (handled) return;
    }
    QEventDispatcherCoreFoundation::unregisterSocketNotifier(notifier);
  }

  //  void QEventDispatcherCoreFoundation::wakeUp()
  void wakeUp() override {
    if (taken[4]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall4 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherCoreFoundation::wakeUp();
  }

  //  void QEventDispatcherCoreFoundation::interrupt()
  void interrupt() override {
    if (taken[5]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall5 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherCoreFoundation::interrupt();
  }

  //  bool QEventDispatcherCoreFoundation::processPostedEvents()
  bool processPostedEvents() override {
    if (taken[6]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall6 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QEventDispatcherCoreFoundation::processPostedEvents();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[7]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall7 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall8 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall9 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall10 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall11 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall12 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall13 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQEventDispatcherCoreFoundationCall14 call = reinterpret_cast<CuteQEventDispatcherCoreFoundationCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QEventDispatcherCoreFoundation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK30QEventDispatcherCoreFoundation10metaObjectEv(
    const QEventDispatcherCoreFoundation *self) {
  return self->metaObject();
}

//  QString QEventDispatcherCoreFoundation::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QEventDispatcherCoreFoundation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventDispatcherCoreFoundation::tr(s, c, n));
}

//  QEventDispatcherCoreFoundation::QEventDispatcherCoreFoundation(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QEventDispatcherCoreFoundation *ritual_ZN30QEventDispatcherCoreFoundationC1EP7QObject(
    QObject *parent) {
  return new CuteQEventDispatcherCoreFoundation(parent);
}

//  void QEventDispatcherCoreFoundation::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation10startingUpEv(
    QEventDispatcherCoreFoundation *self) {
  self->startingUp();
}

//  QEventDispatcherCoreFoundation::~QEventDispatcherCoreFoundation()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundationD1Ev(
    QEventDispatcherCoreFoundation *self) {
  delete self;
}

//  bool QEventDispatcherCoreFoundation::processEvents(QEventLoop::ProcessEve
//      ntsFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QEventDispatcherCoreFoundation13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherCoreFoundation *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void
//      QEventDispatcherCoreFoundation::registerSocketNotifier(QSocketNotifie
//      r *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation22registerSocketNotifierEP15QSocketNotifier(
    QEventDispatcherCoreFoundation *self,
    QSocketNotifier *notifier) {
  self->registerSocketNotifier(notifier);
}

//  void
//      QEventDispatcherCoreFoundation::unregisterSocketNotifier(QSocketNotif
//      ier *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation24unregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherCoreFoundation *self,
    QSocketNotifier *notifier) {
  self->unregisterSocketNotifier(notifier);
}

//  bool QEventDispatcherCoreFoundation::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QEventDispatcherCoreFoundation15unregisterTimerEN2Qt7TimerIdE(
    QEventDispatcherCoreFoundation *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QEventDispatcherCoreFoundation::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QEventDispatcherCoreFoundation16unregisterTimersEP7QObject(
    QEventDispatcherCoreFoundation *self,
    QObject *object) {
  return self->unregisterTimers(object);
}

//  void QEventDispatcherCoreFoundation::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation6wakeUpEv(
    QEventDispatcherCoreFoundation *self) {
  self->wakeUp();
}

//  void QEventDispatcherCoreFoundation::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation9interruptEv(
    QEventDispatcherCoreFoundation *self) {
  self->interrupt();
}

//  QEventLoop *QEventDispatcherCoreFoundation::currentEventLoop() const
extern "C" Q_DECL_EXPORT
QEventLoop *ritual_ZNK30QEventDispatcherCoreFoundation16currentEventLoopEv(
    const QEventDispatcherCoreFoundation *self) {
  return self->currentEventLoop();
}

//  bool QEventDispatcherCoreFoundation::processPostedEvents()
extern "C" Q_DECL_EXPORT
bool ritual_ZN30QEventDispatcherCoreFoundation19processPostedEventsEv(
    QEventDispatcherCoreFoundation *self) {
  return self->processPostedEvents();
}

//  void QEventDispatcherCoreFoundation::processTimers(CFRunLoopTimerRef a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation13processTimersEP16__CFRunLoopTimer(
    QEventDispatcherCoreFoundation *self,
    CFRunLoopTimerRef a0) {
  self->processTimers(a0);
}

//  void QEventDispatcherCoreFoundation::updateTimers()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation12updateTimersEv(
    QEventDispatcherCoreFoundation *self) {
  self->updateTimers();
}

//  void QEventDispatcherCoreFoundation::invalidateTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QEventDispatcherCoreFoundation15invalidateTimerEv(
    QEventDispatcherCoreFoundation *self) {
  self->invalidateTimer();
}

//  a Python function taken by a CuteQEventDispatcherCoreFoundation, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventDispatcherCoreFoundation(
    QEventDispatcherCoreFoundation *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEventDispatcherCoreFoundation *>(self)->take(key, call);
}

//  void QEventDispatcherCoreFoundation::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QEventDispatcherCoreFoundation10startingUpEv(
    QEventDispatcherCoreFoundation *self) {
  self->QEventDispatcherCoreFoundation::startingUp();
}

//  bool QEventDispatcherCoreFoundation::processEvents(QEventLoop::ProcessEve
//      ntsFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QEventDispatcherCoreFoundation13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherCoreFoundation *self,
    int flags) {
  return self->QEventDispatcherCoreFoundation::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void
//      QEventDispatcherCoreFoundation::registerSocketNotifier(QSocketNotifie
//      r *notifier)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QEventDispatcherCoreFoundation22registerSocketNotifierEP15QSocketNotifier(
    QEventDispatcherCoreFoundation *self,
    QSocketNotifier *notifier) {
  self->QEventDispatcherCoreFoundation::registerSocketNotifier(notifier);
}

//  void
//      QEventDispatcherCoreFoundation::unregisterSocketNotifier(QSocketNotif
//      ier *notifier)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QEventDispatcherCoreFoundation24unregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherCoreFoundation *self,
    QSocketNotifier *notifier) {
  self->QEventDispatcherCoreFoundation::unregisterSocketNotifier(notifier);
}

//  void QEventDispatcherCoreFoundation::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QEventDispatcherCoreFoundation6wakeUpEv(
    QEventDispatcherCoreFoundation *self) {
  self->QEventDispatcherCoreFoundation::wakeUp();
}

//  void QEventDispatcherCoreFoundation::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN30QEventDispatcherCoreFoundation9interruptEv(
    QEventDispatcherCoreFoundation *self) {
  self->QEventDispatcherCoreFoundation::interrupt();
}

//  bool QEventDispatcherCoreFoundation::processPostedEvents()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN30QEventDispatcherCoreFoundation19processPostedEventsEv(
    QEventDispatcherCoreFoundation *self) {
  return static_cast<OwnQEventDispatcherCoreFoundation *>(self)->OwnQEventDispatcherCoreFoundation::processPostedEvents();
}

#endif  // defined(Q_OS_DARWIN)
