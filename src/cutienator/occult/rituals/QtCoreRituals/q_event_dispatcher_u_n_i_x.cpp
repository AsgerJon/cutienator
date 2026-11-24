//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_unix_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QEventDispatcherUNIX that Python can take functions over in. Every QEventDispatcherUNIX
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQEventDispatcherUNIXCall0)(const void *, int, int *);
typedef void (*CuteQEventDispatcherUNIXCall1)(const void *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQEventDispatcherUNIXCall2)(const void *, int, const QDeadlineTimer *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQEventDispatcherUNIXCall3)(const void *, int *);
typedef void (*CuteQEventDispatcherUNIXCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherUNIXCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherUNIXCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherUNIXCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherUNIXCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherUNIXCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherUNIXCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherUNIXCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQEventDispatcherUNIX : public QEventDispatcherUNIX {
public:
  using QEventDispatcherUNIX::QEventDispatcherUNIX;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher6wakeUpEv")) {
      taken[1] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool
  //      QEventDispatcherUNIX::processEvents(QEventLoop::ProcessEventsFlag
  //      s flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall0 call = reinterpret_cast<CuteQEventDispatcherUNIXCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QEventDispatcherUNIX::processEvents(flags);
  }

  //  void QEventDispatcherUNIX::wakeUp()
  void wakeUp() override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall1 call = reinterpret_cast<CuteQEventDispatcherUNIXCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherUNIX::wakeUp();
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop
  //      ::ProcessEventsFlags flags, QDeadlineTimer deadline)
  bool processEventsWithDeadline(
      QEventLoop::ProcessEventsFlags flags,
      QDeadlineTimer deadline) override {
    if (taken[2]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall2 call = reinterpret_cast<CuteQEventDispatcherUNIXCall2>(taken[2]);
      bool given = call(this, static_cast<int>(flags.toInt()), &deadline, &handled);
      if (handled) return given;
    }
    return QAbstractEventDispatcherV2::processEventsWithDeadline(flags, deadline);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QAbstractEventDispatcher::startingUp()
  void startingUp() override {
    if (taken[3]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall3 call = reinterpret_cast<CuteQEventDispatcherUNIXCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::startingUp();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[4]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall4 call = reinterpret_cast<CuteQEventDispatcherUNIXCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall5 call = reinterpret_cast<CuteQEventDispatcherUNIXCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall6 call = reinterpret_cast<CuteQEventDispatcherUNIXCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall7 call = reinterpret_cast<CuteQEventDispatcherUNIXCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall8 call = reinterpret_cast<CuteQEventDispatcherUNIXCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall9 call = reinterpret_cast<CuteQEventDispatcherUNIXCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall10 call = reinterpret_cast<CuteQEventDispatcherUNIXCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQEventDispatcherUNIXCall11 call = reinterpret_cast<CuteQEventDispatcherUNIXCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QEventDispatcherUNIX::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QEventDispatcherUNIX10metaObjectEv(
    const QEventDispatcherUNIX *self) {
  return self->metaObject();
}

//  QString QEventDispatcherUNIX::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QEventDispatcherUNIX2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventDispatcherUNIX::tr(s, c, n));
}

//  QEventDispatcherUNIXPrivate *QEventDispatcherUNIX::d_func()
extern "C" Q_DECL_EXPORT
QEventDispatcherUNIXPrivate *ritual_ZN20QEventDispatcherUNIX6d_funcEv(
    QEventDispatcherUNIX *self) {
  return self->d_func();
}

//  const QEventDispatcherUNIXPrivate *QEventDispatcherUNIX::d_func() const
extern "C" Q_DECL_EXPORT
const QEventDispatcherUNIXPrivate *ritual_ZNK20QEventDispatcherUNIX6d_funcEv(
    const QEventDispatcherUNIX *self) {
  return self->d_func();
}

//  QEventDispatcherUNIX::QEventDispatcherUNIX(QObject *parent)
extern "C" Q_DECL_EXPORT
QEventDispatcherUNIX *ritual_ZN20QEventDispatcherUNIXC1EP7QObject(
    QObject *parent) {
  return new CuteQEventDispatcherUNIX(parent);
}

//  QEventDispatcherUNIX::~QEventDispatcherUNIX()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherUNIXD1Ev(QEventDispatcherUNIX *self) {
  delete self;
}

//  bool QEventDispatcherUNIX::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherUNIX13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherUNIX *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventDispatcherUNIX::registerSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherUNIX22registerSocketNotifierEP15QSocketNotifier(
    QEventDispatcherUNIX *self,
    QSocketNotifier *notifier) {
  self->registerSocketNotifier(notifier);
}

//  void QEventDispatcherUNIX::unregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherUNIX24unregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherUNIX *self,
    QSocketNotifier *notifier) {
  self->unregisterSocketNotifier(notifier);
}

//  bool QEventDispatcherUNIX::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherUNIX15unregisterTimerEN2Qt7TimerIdE(
    QEventDispatcherUNIX *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QEventDispatcherUNIX::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherUNIX16unregisterTimersEP7QObject(
    QEventDispatcherUNIX *self,
    QObject *object) {
  return self->unregisterTimers(object);
}

//  void QEventDispatcherUNIX::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherUNIX6wakeUpEv(QEventDispatcherUNIX *self) {
  self->wakeUp();
}

//  void QEventDispatcherUNIX::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherUNIX9interruptEv(
    QEventDispatcherUNIX *self) {
  self->interrupt();
}

//  a Python function taken by a CuteQEventDispatcherUNIX, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventDispatcherUNIX(
    QEventDispatcherUNIX *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEventDispatcherUNIX *>(self)->take(key, call);
}

//  bool QEventDispatcherUNIX::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QEventDispatcherUNIX13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherUNIX *self,
    int flags) {
  return self->QEventDispatcherUNIX::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventDispatcherUNIX::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QEventDispatcherUNIX6wakeUpEv(
    QEventDispatcherUNIX *self) {
  self->QEventDispatcherUNIX::wakeUp();
}
