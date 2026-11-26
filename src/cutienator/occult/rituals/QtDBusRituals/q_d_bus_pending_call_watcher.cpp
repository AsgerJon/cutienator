//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbuspendingcall.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbuspendingcall.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDBusPendingCallWatcher that Python can take functions over in. Every QDBusPendingCallWatcher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPendingCallWatcherCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusPendingCallWatcherCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusPendingCallWatcherCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusPendingCallWatcher : public QDBusPendingCallWatcher {
public:
  using QDBusPendingCallWatcher::QDBusPendingCallWatcher;
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
      CuteQDBusPendingCallWatcherCall0 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall0>(taken[0]);
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
      CuteQDBusPendingCallWatcherCall1 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall1>(taken[1]);
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
      CuteQDBusPendingCallWatcherCall2 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall2>(taken[2]);
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
      CuteQDBusPendingCallWatcherCall3 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall3>(taken[3]);
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
      CuteQDBusPendingCallWatcherCall4 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall4>(taken[4]);
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
      CuteQDBusPendingCallWatcherCall5 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall5>(taken[5]);
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
      CuteQDBusPendingCallWatcherCall6 call = reinterpret_cast<CuteQDBusPendingCallWatcherCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusPendingCallWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QDBusPendingCallWatcher10metaObjectEv(
    const QDBusPendingCallWatcher *self) {
  return self->metaObject();
}

//  void *QDBusPendingCallWatcher::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN23QDBusPendingCallWatcher11qt_metacastEPKc(
    QDBusPendingCallWatcher *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusPendingCallWatcher::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN23QDBusPendingCallWatcher11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusPendingCallWatcher *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDBusPendingCallWatcher::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QDBusPendingCallWatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusPendingCallWatcher::tr(s, c, n));
}

//  QDBusPendingCallWatcher::QDBusPendingCallWatcher(const QDBusPendingCall
//      &call, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusPendingCallWatcher *ritual_ZN23QDBusPendingCallWatcherC1ERK16QDBusPendingCallP7QObject(
    const QDBusPendingCall *call,
    QObject *parent) {
  return new CuteQDBusPendingCallWatcher(*call, parent);
}

//  QDBusPendingCallWatcher::~QDBusPendingCallWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallWatcherD1Ev(QDBusPendingCallWatcher *self) {
  delete self;
}

//  void QDBusPendingCallWatcher::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallWatcher15waitForFinishedEv(
    QDBusPendingCallWatcher *self) {
  self->waitForFinished();
}

//  void QDBusPendingCallWatcher::finished(QDBusPendingCallWatcher *self_)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QDBusPendingCallWatcher8finishedEPS_(
    QDBusPendingCallWatcher *self,
    QDBusPendingCallWatcher *self_) {
  self->finished(self_);
}

//  QDBusPendingCallWatcher as the QDBusPendingCall it is built on
extern "C" Q_DECL_EXPORT
QDBusPendingCall *ritual_cast_QDBusPendingCallWatcher_QDBusPendingCall(
    QDBusPendingCallWatcher *self) {
  return static_cast<QDBusPendingCall *>(self);
}

//  a Python function taken by a CuteQDBusPendingCallWatcher, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusPendingCallWatcher(
    QDBusPendingCallWatcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusPendingCallWatcher *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
