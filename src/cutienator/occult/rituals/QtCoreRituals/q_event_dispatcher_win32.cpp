//  Written by hand on 2026-11-25 from
//  QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h, Qt 6.12.0, as
//  the Qt of Windows installs it. Kept as it is when the generator runs
//  again. A handle of Windows, as 'HWND', is passed as an address. Not
//  written, as for 'QEventDispatcherUNIX': 'registerTimer' and
//  'remainingTime', which pass a 'Duration', and 'timersForObject',
//  which gives a list of 'TimerInfoV2'; and the constructor taking a
//  'QEventDispatcherWin32Private &'.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtCore/6.12.0/QtCore/private/qeventdispatcher_win_p.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <cstring>

//  Only a class built on QEventDispatcherWin32 may call these functions
//  of it. This one is, and makes them free for the rituals to call.
struct OwnQEventDispatcherWin32 : QEventDispatcherWin32 {
  using QEventDispatcherWin32::sendPostedEvents;
};

//  A QEventDispatcherWin32 that Python can take functions over in. Every
//  QEventDispatcherWin32 Python makes is one. Each function below asks
//  the Python function handed over for it, and runs Qt's own without
//  one.
typedef bool (*CuteQEventDispatcherWin32Call0)(const void *, int, int *);
typedef void (*CuteQEventDispatcherWin32Call1)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQEventDispatcherWin32Call2)(const void *, QSocketNotifier *, int *);
typedef void (*CuteQEventDispatcherWin32Call3)(const void *, int *);
typedef void (*CuteQEventDispatcherWin32Call4)(const void *, int *);
typedef void (*CuteQEventDispatcherWin32Call5)(const void *, int *);
typedef void (*CuteQEventDispatcherWin32Call6)(const void *, int *);
typedef bool (*CuteQEventDispatcherWin32Call7)(const void *, QEvent *, int *);
typedef void (*CuteQEventDispatcherWin32Call8)(const void *, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQEventDispatcherWin32Call9)(const void *, int, const QDeadlineTimer *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQEventDispatcherWin32Call10)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQEventDispatcherWin32Call11)(const void *, QTimerEvent *, int *);
typedef void (*CuteQEventDispatcherWin32Call12)(const void *, QChildEvent *, int *);
typedef void (*CuteQEventDispatcherWin32Call13)(const void *, QEvent *, int *);
typedef void (*CuteQEventDispatcherWin32Call14)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQEventDispatcherWin32Call15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQEventDispatcherWin32 : public QEventDispatcherWin32 {
public:
  using QEventDispatcherWin32::QEventDispatcherWin32;
  void *taken[16] = {};

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
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher6wakeUpEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher9interruptEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher10startingUpEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QAbstractEventDispatcher11closingDownEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QEventDispatcherWin3216sendPostedEventsEv")) {
      taken[8] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN26QAbstractEventDispatcherV225processEventsWithDeadlineE6QFlagsIN10QEventLoop17ProcessEventsFlagEE14QDeadlineTimer")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QEventDispatcherWin32::processEvents(QEventLoop::ProcessEventsFlags
  //      flags)
  bool processEvents(QEventLoop::ProcessEventsFlags flags) override {
    if (taken[0]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call0 call = reinterpret_cast<CuteQEventDispatcherWin32Call0>(taken[0]);
      bool given = call(this, static_cast<int>(flags.toInt()), &handled);
      if (handled) return given;
    }
    return QEventDispatcherWin32::processEvents(flags);
  }

  //  void QEventDispatcherWin32::registerSocketNotifier(QSocketNotifier
  //      *notifier)
  void registerSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[1]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call1 call = reinterpret_cast<CuteQEventDispatcherWin32Call1>(taken[1]);
      call(this, notifier, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::registerSocketNotifier(notifier);
  }

  //  void QEventDispatcherWin32::unregisterSocketNotifier(QSocketNotifier
  //      *notifier)
  void unregisterSocketNotifier(QSocketNotifier *notifier) override {
    if (taken[2]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call2 call = reinterpret_cast<CuteQEventDispatcherWin32Call2>(taken[2]);
      call(this, notifier, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::unregisterSocketNotifier(notifier);
  }

  //  void QEventDispatcherWin32::wakeUp()
  void wakeUp() override {
    if (taken[3]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call3 call = reinterpret_cast<CuteQEventDispatcherWin32Call3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::wakeUp();
  }

  //  void QEventDispatcherWin32::interrupt()
  void interrupt() override {
    if (taken[4]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call4 call = reinterpret_cast<CuteQEventDispatcherWin32Call4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::interrupt();
  }

  //  void QEventDispatcherWin32::startingUp()
  void startingUp() override {
    if (taken[5]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call5 call = reinterpret_cast<CuteQEventDispatcherWin32Call5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::startingUp();
  }

  //  void QEventDispatcherWin32::closingDown()
  void closingDown() override {
    if (taken[6]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call6 call = reinterpret_cast<CuteQEventDispatcherWin32Call6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::closingDown();
  }

  //  bool QEventDispatcherWin32::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call7 call = reinterpret_cast<CuteQEventDispatcherWin32Call7>(taken[7]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QEventDispatcherWin32::event(e);
  }

  //  void QEventDispatcherWin32::sendPostedEvents()
  void sendPostedEvents() override {
    if (taken[8]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call8 call = reinterpret_cast<CuteQEventDispatcherWin32Call8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QEventDispatcherWin32::sendPostedEvents();
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QAbstractEventDispatcherV2::processEventsWithDeadline(QEventLoop
  //      ::ProcessEventsFlags flags, QDeadlineTimer deadline)
  bool processEventsWithDeadline(
      QEventLoop::ProcessEventsFlags flags,
      QDeadlineTimer deadline) override {
    if (taken[9]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call9 call = reinterpret_cast<CuteQEventDispatcherWin32Call9>(taken[9]);
      bool given = call(this, static_cast<int>(flags.toInt()), &deadline, &handled);
      if (handled) return given;
    }
    return QAbstractEventDispatcherV2::processEventsWithDeadline(flags, deadline);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call10 call = reinterpret_cast<CuteQEventDispatcherWin32Call10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call11 call = reinterpret_cast<CuteQEventDispatcherWin32Call11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call12 call = reinterpret_cast<CuteQEventDispatcherWin32Call12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call13 call = reinterpret_cast<CuteQEventDispatcherWin32Call13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call14 call = reinterpret_cast<CuteQEventDispatcherWin32Call14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQEventDispatcherWin32Call15 call = reinterpret_cast<CuteQEventDispatcherWin32Call15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QEventDispatcherWin32::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QEventDispatcherWin3210metaObjectEv(
    const QEventDispatcherWin32 *self) {
  return self->metaObject();
}

//  QString QEventDispatcherWin32::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QEventDispatcherWin322trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QEventDispatcherWin32::tr(s, c, n));
}

//  QEventDispatcherWin32Private *QEventDispatcherWin32::d_func()
extern "C" Q_DECL_EXPORT
QEventDispatcherWin32Private *ritual_ZN21QEventDispatcherWin326d_funcEv(
    QEventDispatcherWin32 *self) {
  return self->d_func();
}

//  const QEventDispatcherWin32Private *QEventDispatcherWin32::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QEventDispatcherWin32Private *ritual_ZNK21QEventDispatcherWin326d_funcEv(
    const QEventDispatcherWin32 *self) {
  return self->d_func();
}

//  QEventDispatcherWin32::QEventDispatcherWin32(QObject *parent)
extern "C" Q_DECL_EXPORT
QEventDispatcherWin32 *ritual_ZN21QEventDispatcherWin32C1EP7QObject(
    QObject *parent) {
  return new CuteQEventDispatcherWin32(parent);
}

//  QEventDispatcherWin32::~QEventDispatcherWin32()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin32D1Ev(QEventDispatcherWin32 *self) {
  delete self;
}

//  bool QEventDispatcherWin32::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QEventDispatcherWin3213processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherWin32 *self,
    int flags) {
  return self->processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventDispatcherWin32::registerSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin3222registerSocketNotifierEP15QSocketNotifier(
    QEventDispatcherWin32 *self,
    QSocketNotifier *notifier) {
  self->registerSocketNotifier(notifier);
}

//  void QEventDispatcherWin32::unregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin3224unregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherWin32 *self,
    QSocketNotifier *notifier) {
  self->unregisterSocketNotifier(notifier);
}

//  bool QEventDispatcherWin32::unregisterTimer(Qt::TimerId timerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QEventDispatcherWin3215unregisterTimerEN2Qt7TimerIdE(
    QEventDispatcherWin32 *self,
    Qt::TimerId timerId) {
  return self->unregisterTimer(timerId);
}

//  bool QEventDispatcherWin32::unregisterTimers(QObject *object)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QEventDispatcherWin3216unregisterTimersEP7QObject(
    QEventDispatcherWin32 *self,
    QObject *object) {
  return self->unregisterTimers(object);
}

//  void QEventDispatcherWin32::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin326wakeUpEv(QEventDispatcherWin32 *self) {
  self->wakeUp();
}

//  void QEventDispatcherWin32::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin329interruptEv(
    QEventDispatcherWin32 *self) {
  self->interrupt();
}

//  void QEventDispatcherWin32::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin3210startingUpEv(
    QEventDispatcherWin32 *self) {
  self->startingUp();
}

//  void QEventDispatcherWin32::closingDown()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin3211closingDownEv(
    QEventDispatcherWin32 *self) {
  self->closingDown();
}

//  bool QEventDispatcherWin32::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QEventDispatcherWin325eventEP6QEvent(
    QEventDispatcherWin32 *self,
    QEvent *e) {
  return self->event(e);
}

//  HWND QEventDispatcherWin32::internalHwnd()
extern "C" Q_DECL_EXPORT
HWND ritual_ZN21QEventDispatcherWin3212internalHwndEv(
    QEventDispatcherWin32 *self) {
  return self->internalHwnd();
}

//  void QEventDispatcherWin32::sendPostedEvents()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin3216sendPostedEventsEv(
    QEventDispatcherWin32 *self) {
  self->sendPostedEvents();
}

//  void QEventDispatcherWin32::doUnregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QEventDispatcherWin3226doUnregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherWin32 *self,
    QSocketNotifier *notifier) {
  self->doUnregisterSocketNotifier(notifier);
}

//  a Python function taken by a CuteQEventDispatcherWin32, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QEventDispatcherWin32(
    QEventDispatcherWin32 *self,
    const char *key,
    void *call) {
  return static_cast<CuteQEventDispatcherWin32 *>(self)->take(key, call);
}

//  bool QEventDispatcherWin32::processEvents(QEventLoop::ProcessEventsFlags
//      flags)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QEventDispatcherWin3213processEventsE6QFlagsIN10QEventLoop17ProcessEventsFlagEE(
    QEventDispatcherWin32 *self,
    int flags) {
  return self->QEventDispatcherWin32::processEvents(
      QFlags<QEventLoop::ProcessEventsFlag>::fromInt(flags));
}

//  void QEventDispatcherWin32::registerSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin3222registerSocketNotifierEP15QSocketNotifier(
    QEventDispatcherWin32 *self,
    QSocketNotifier *notifier) {
  self->QEventDispatcherWin32::registerSocketNotifier(notifier);
}

//  void QEventDispatcherWin32::unregisterSocketNotifier(QSocketNotifier
//      *notifier)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin3224unregisterSocketNotifierEP15QSocketNotifier(
    QEventDispatcherWin32 *self,
    QSocketNotifier *notifier) {
  self->QEventDispatcherWin32::unregisterSocketNotifier(notifier);
}

//  void QEventDispatcherWin32::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin326wakeUpEv(
    QEventDispatcherWin32 *self) {
  self->QEventDispatcherWin32::wakeUp();
}

//  void QEventDispatcherWin32::interrupt()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin329interruptEv(
    QEventDispatcherWin32 *self) {
  self->QEventDispatcherWin32::interrupt();
}

//  void QEventDispatcherWin32::startingUp()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin3210startingUpEv(
    QEventDispatcherWin32 *self) {
  self->QEventDispatcherWin32::startingUp();
}

//  void QEventDispatcherWin32::closingDown()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin3211closingDownEv(
    QEventDispatcherWin32 *self) {
  self->QEventDispatcherWin32::closingDown();
}

//  bool QEventDispatcherWin32::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QEventDispatcherWin325eventEP6QEvent(
    QEventDispatcherWin32 *self,
    QEvent *e) {
  return self->QEventDispatcherWin32::event(e);
}

//  void QEventDispatcherWin32::sendPostedEvents()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QEventDispatcherWin3216sendPostedEventsEv(
    QEventDispatcherWin32 *self) {
  static_cast<OwnQEventDispatcherWin32 *>(self)->OwnQEventDispatcherWin32::sendPostedEvents();
}

#endif  // defined(Q_OS_WIN)
