//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qwindowsguieventdispatcher_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qwindowsguieventdispatcher_p.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  A QWindowsGuiEventDispatcher that Python can take functions over in. Every
//  QWindowsGuiEventDispatcher Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef bool (*CuteQWindowsGuiEventDispatcherCall0)(const void *, int, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall1)(const void *, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall2)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall3)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall4)(const void *, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall5)(const void *, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall6)(const void *, int *);
typedef void (*CuteQWindowsGuiEventDispatcherCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsGuiEventDispatcherCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWindowsGuiEventDispatcherCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsGuiEventDispatcherCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsGuiEventDispatcherCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsGuiEventDispatcherCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsGuiEventDispatcherCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWindowsGuiEventDispatcherCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWindowsGuiEventDispatcher : public QWindowsGuiEventDispatcher {
public:
  using QWindowsGuiEventDispatcher::QWindowsGuiEventDispatcher;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QEventDispatcherWin3216sendPostedEventsEv")) {
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
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
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

  //  bool QWindowsGuiEventDispatcher::processEvents(QEventLoop::ProcessEvent
  //      sFlags flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall0 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QWindowsGuiEventDispatcher::processEvents(flags);
  }

  //  void QWindowsGuiEventDispatcher::sendPostedEvents()
  void sendPostedEvents() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall1 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWindowsGuiEventDispatcher::sendPostedEvents();
  }

  //  void QEventDispatcherWin32::registerSocketNotifier(QSocketNotifier
  //      *notifier)
  void registerSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall2 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall2>(taken[2]);
      call(this, notifier, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::registerSocketNotifier(notifier);
  }

  //  void QEventDispatcherWin32::unregisterSocketNotifier(QSocketNotifier
  //      *notifier)
  void unregisterSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall3 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall3>(taken[3]);
      call(this, notifier, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::unregisterSocketNotifier(notifier);
  }

  //  void QEventDispatcherWin32::wakeUp()
  void wakeUp() override {
    if (taken[4]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall4 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::wakeUp();
  }

  //  void QEventDispatcherWin32::interrupt()
  void interrupt() override {
    if (taken[5]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall5 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::interrupt();
  }

  //  void QEventDispatcherWin32::startingUp()
  void startingUp() override {
    if (taken[6]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall6 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::startingUp();
  }

  //  void QEventDispatcherWin32::closingDown()
  void closingDown() override {
    if (taken[7]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall7 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::closingDown();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QEventDispatcherWin32::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall8 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall8>(taken[8]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QEventDispatcherWin32::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWindowsGuiEventDispatcherCall9 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall9>(taken[9]);
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
      CuteQWindowsGuiEventDispatcherCall10 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall10>(taken[10]);
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
      CuteQWindowsGuiEventDispatcherCall11 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall11>(taken[11]);
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
      CuteQWindowsGuiEventDispatcherCall12 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall12>(taken[12]);
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
      CuteQWindowsGuiEventDispatcherCall13 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall13>(taken[13]);
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
      CuteQWindowsGuiEventDispatcherCall14 call = reinterpret_cast<CuteQWindowsGuiEventDispatcherCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWindowsGuiEventDispatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK26QWindowsGuiEventDispatcher10metaObjectEv(
    const QWindowsGuiEventDispatcher *self) {
  return self->metaObject();
}

//  QString QWindowsGuiEventDispatcher::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN26QWindowsGuiEventDispatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWindowsGuiEventDispatcher::tr(s, c, n));
}

//  QWindowsGuiEventDispatcher::QWindowsGuiEventDispatcher(QObject *parent)
extern "C" Q_DECL_EXPORT
QWindowsGuiEventDispatcher *ritual_ZN26QWindowsGuiEventDispatcherC1EP7QObject(
    QObject *parent) {
  return new CuteQWindowsGuiEventDispatcher(parent);
}

//  const char *QWindowsGuiEventDispatcher::windowsMessageName(UINT msg)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN26QWindowsGuiEventDispatcher18windowsMessageNameEj(
    UINT msg) {
  return QWindowsGuiEventDispatcher::windowsMessageName(msg);
}

//  bool
//      QWindowsGuiEventDispatcher::processEvents(QEventLoop::ProcessEventsFl
//      ags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN26QWindowsGuiEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QWindowsGuiEventDispatcher *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QWindowsGuiEventDispatcher::sendPostedEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QWindowsGuiEventDispatcher16sendPostedEventsEv(
    QWindowsGuiEventDispatcher *self) {
  self->sendPostedEvents();
}

//  a Python function taken by a CuteQWindowsGuiEventDispatcher, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWindowsGuiEventDispatcher(
    QWindowsGuiEventDispatcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWindowsGuiEventDispatcher *>(self)->take(key, call);
}

//  bool
//      QWindowsGuiEventDispatcher::processEvents(QEventLoop::ProcessEventsFl
//      ags flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN26QWindowsGuiEventDispatcher13processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QWindowsGuiEventDispatcher *self,
    int flags) {
  return self->QWindowsGuiEventDispatcher::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QWindowsGuiEventDispatcher::sendPostedEvents()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QWindowsGuiEventDispatcher16sendPostedEventsEv(
    QWindowsGuiEventDispatcher *self) {
  self->QWindowsGuiEventDispatcher::sendPostedEvents();
}

#endif  // defined(Q_OS_WIN)
