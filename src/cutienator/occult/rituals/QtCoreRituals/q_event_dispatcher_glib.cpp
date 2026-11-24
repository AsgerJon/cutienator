//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_glib_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_glib_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QEventDispatcherGlib that Python can take functions over in. Every QEventDispatcherGlib
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQEventDispatcherGlibCall0)(const void *, int, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQEventDispatcherGlibCall1)(const void *, int, const QDeadlineTimer *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQEventDispatcherGlibCall2)(const void *, int *);
typedef void (*CuteQEventDispatcherGlibCall3)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherGlibCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherGlibCall5)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherGlibCall6)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherGlibCall7)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherGlibCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherGlibCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQEventDispatcherGlibCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQEventDispatcherGlib : public QEventDispatcherGlib {
public:
  using QEventDispatcherGlib::QEventDispatcherGlib;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[0] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[3] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool
  //      QEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlag
  //      s flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall0 call = reinterpret_cast<CuteQEventDispatcherGlibCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QEventDispatcherGlib::processEvents(flags);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop
  //      ::ProcessEventsFlags flags, QDeadlineTimer deadline)
  bool processEventsWithDeadline(
      QEventLoop::ProcessEventsFlags flags,
      QDeadlineTimer deadline) override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall1 call = reinterpret_cast<CuteQEventDispatcherGlibCall1>(taken[1]);
      bool given = call(this, static_cast<int>(flags.toInt()), &deadline, &handled);
      if (handled) return given;
    }
    return QAbstractEventDispatcherV2::processEventsWithDeadline(flags, deadline);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QAbstractEventDispatcher::startingUp()
  void startingUp() override {
    if (taken[2]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall2 call = reinterpret_cast<CuteQEventDispatcherGlibCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::startingUp();
  }

  //  void QAbstractEventDispatcher::closingDown()
  void closingDown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall3 call = reinterpret_cast<CuteQEventDispatcherGlibCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractEventDispatcher::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall4 call = reinterpret_cast<CuteQEventDispatcherGlibCall4>(taken[4]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall5 call = reinterpret_cast<CuteQEventDispatcherGlibCall5>(taken[5]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall6 call = reinterpret_cast<CuteQEventDispatcherGlibCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall7 call = reinterpret_cast<CuteQEventDispatcherGlibCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall8 call = reinterpret_cast<CuteQEventDispatcherGlibCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall9 call = reinterpret_cast<CuteQEventDispatcherGlibCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQEventDispatcherGlibCall10 call = reinterpret_cast<CuteQEventDispatcherGlibCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QEventDispatcherGlib::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QEventDispatcherGlib10metaObjectEv(
    const QEventDispatcherGlib *self) {
  return self->metaObject();
}

//  QString QEventDispatcherGlib::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QEventDispatcherGlib2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventDispatcherGlib::tr(s, c, n));
}

//  QEventDispatcherGlibPrivate *QEventDispatcherGlib::d_func()
extern "C" Q_DECL_EXPORT
QEventDispatcherGlibPrivate *ritual_ZN20QEventDispatcherGlib6d_funcEv(
    QEventDispatcherGlib *self) {
  return self->d_func();
}

//  const QEventDispatcherGlibPrivate *QEventDispatcherGlib::d_func() const
extern "C" Q_DECL_EXPORT
const QEventDispatcherGlibPrivate *ritual_ZNK20QEventDispatcherGlib6d_funcEv(
    const QEventDispatcherGlib *self) {
  return self->d_func();
}

//  QEventDispatcherGlib::QEventDispatcherGlib(QObject *parent)
extern "C" Q_DECL_EXPORT
QEventDispatcherGlib *ritual_ZN20QEventDispatcherGlibC1EP7QObject(
    QObject *parent) {
  return new CuteQEventDispatcherGlib(parent);
}

//  QEventDispatcherGlib::~QEventDispatcherGlib()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherGlibD1Ev(QEventDispatcherGlib *self) {
  delete self;
}

//  bool QEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherGlib13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherGlib *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventDispatcherGlib::registerSocketNotifier(QSocketNotifier
//      *socketNotifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherGlib22registerSocketNotifierEP15QSocketNotifier(
    QEventDispatcherGlib *self,
    QSocketNotifier *socketNotifier) {
  self->registerSocketNotifier(socketNotifier);
}

//  void QEventDispatcherGlib::unregisterSocketNotifier(QSocketNotifier
//      *socketNotifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherGlib24unregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherGlib *self,
    QSocketNotifier *socketNotifier) {
  self->unregisterSocketNotifier(socketNotifier);
}

//  bool QEventDispatcherGlib::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherGlib15unregisterTimerEN2Qt7TimerIdE(
    QEventDispatcherGlib *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QEventDispatcherGlib::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherGlib16unregisterTimersEP7QObject(
    QEventDispatcherGlib *self,
    QObject *object) {
  return self->unregisterTimers(object);
}

//  void QEventDispatcherGlib::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherGlib6wakeUpEv(QEventDispatcherGlib *self) {
  self->wakeUp();
}

//  void QEventDispatcherGlib::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QEventDispatcherGlib9interruptEv(
    QEventDispatcherGlib *self) {
  self->interrupt();
}

//  bool QEventDispatcherGlib::versionSupported()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QEventDispatcherGlib16versionSupportedEv() {
  return QEventDispatcherGlib::versionSupported();
}

//  a Python function taken by a CuteQEventDispatcherGlib, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventDispatcherGlib(
    QEventDispatcherGlib *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEventDispatcherGlib *>(self)->take(key, call);
}

//  bool QEventDispatcherGlib::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QEventDispatcherGlib13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherGlib *self,
    int flags) {
  return self->QEventDispatcherGlib::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}
