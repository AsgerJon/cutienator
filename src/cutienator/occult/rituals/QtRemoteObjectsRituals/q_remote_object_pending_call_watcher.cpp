//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qremoteobjectpendingcall.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtRemoteObjects/qremoteobjectpendingcall.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QRemoteObjectPendingCallWatcher that Python can take functions over in. Every QRemoteObjectPendingCallWatcher
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectPendingCallWatcherCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQRemoteObjectPendingCallWatcherCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQRemoteObjectPendingCallWatcherCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQRemoteObjectPendingCallWatcher : public QRemoteObjectPendingCallWatcher {
public:
  using QRemoteObjectPendingCallWatcher::QRemoteObjectPendingCallWatcher;
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
      CuteQRemoteObjectPendingCallWatcherCall0 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall0>(taken[0]);
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
      CuteQRemoteObjectPendingCallWatcherCall1 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall1>(taken[1]);
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
      CuteQRemoteObjectPendingCallWatcherCall2 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall2>(taken[2]);
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
      CuteQRemoteObjectPendingCallWatcherCall3 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall3>(taken[3]);
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
      CuteQRemoteObjectPendingCallWatcherCall4 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall4>(taken[4]);
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
      CuteQRemoteObjectPendingCallWatcherCall5 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall5>(taken[5]);
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
      CuteQRemoteObjectPendingCallWatcherCall6 call = reinterpret_cast<CuteQRemoteObjectPendingCallWatcherCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QRemoteObjectPendingCallWatcher::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QRemoteObjectPendingCallWatcher10metaObjectEv(
    const QRemoteObjectPendingCallWatcher *self) {
  return self->metaObject();
}

//  QString QRemoteObjectPendingCallWatcher::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN31QRemoteObjectPendingCallWatcher2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRemoteObjectPendingCallWatcher::tr(s, c, n));
}

//  QRemoteObjectPendingCallWatcher::QRemoteObjectPendingCallWatcher(const
//      QRemoteObjectPendingCall &call, QObject *parent)
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCallWatcher *ritual_ZN31QRemoteObjectPendingCallWatcherC1ERK24QRemoteObjectPendingCallP7QObject(
    const QRemoteObjectPendingCall *call,
    QObject *parent) {
  return new CuteQRemoteObjectPendingCallWatcher(*call, parent);
}

//  QRemoteObjectPendingCallWatcher::~QRemoteObjectPendingCallWatcher()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QRemoteObjectPendingCallWatcherD1Ev(
    QRemoteObjectPendingCallWatcher *self) {
  delete self;
}

//  bool QRemoteObjectPendingCallWatcher::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QRemoteObjectPendingCallWatcher10isFinishedEv(
    const QRemoteObjectPendingCallWatcher *self) {
  return self->isFinished();
}

//  void QRemoteObjectPendingCallWatcher::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QRemoteObjectPendingCallWatcher15waitForFinishedEv(
    QRemoteObjectPendingCallWatcher *self) {
  self->waitForFinished();
}

//  QRemoteObjectPendingCallWatcher as the QRemoteObjectPendingCall it is
//      built on
extern "C" Q_DECL_EXPORT
QRemoteObjectPendingCall *ritual_cast_QRemoteObjectPendingCallWatcher_QRemoteObjectPendingCall(
    QRemoteObjectPendingCallWatcher *self) {
  return static_cast<QRemoteObjectPendingCall *>(self);
}

//  a Python function taken by a CuteQRemoteObjectPendingCallWatcher, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRemoteObjectPendingCallWatcher(
    QRemoteObjectPendingCallWatcher *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRemoteObjectPendingCallWatcher *>(self)->take(key, call);
}
