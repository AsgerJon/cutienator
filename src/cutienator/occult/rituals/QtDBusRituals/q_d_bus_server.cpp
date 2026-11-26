//  Written by dev_tooling.RitualGenerator from the records of
//  QtDBus/qdbusserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtDBus/qtdbusglobal.h>
#if !defined(QT_NO_DBUS)
#include <QtDBus/qdbusserver.h>
#include <QtCore/qstring.h>
#include <QtDBus/qdbuserror.h>
#include <QtDBus/qdbusconnection.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDBusServer that Python can take functions over in. Every QDBusServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusServerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDBusServerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDBusServerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDBusServer : public QDBusServer {
public:
  using QDBusServer::QDBusServer;
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
      CuteQDBusServerCall0 call = reinterpret_cast<CuteQDBusServerCall0>(taken[0]);
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
      CuteQDBusServerCall1 call = reinterpret_cast<CuteQDBusServerCall1>(taken[1]);
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
      CuteQDBusServerCall2 call = reinterpret_cast<CuteQDBusServerCall2>(taken[2]);
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
      CuteQDBusServerCall3 call = reinterpret_cast<CuteQDBusServerCall3>(taken[3]);
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
      CuteQDBusServerCall4 call = reinterpret_cast<CuteQDBusServerCall4>(taken[4]);
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
      CuteQDBusServerCall5 call = reinterpret_cast<CuteQDBusServerCall5>(taken[5]);
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
      CuteQDBusServerCall6 call = reinterpret_cast<CuteQDBusServerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDBusServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QDBusServer10metaObjectEv(
    const QDBusServer *self) {
  return self->metaObject();
}

//  void *QDBusServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN11QDBusServer11qt_metacastEPKc(
    QDBusServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDBusServer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN11QDBusServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QDBusServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDBusServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QDBusServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDBusServer::tr(s, c, n));
}

//  QDBusServer::QDBusServer(const QString &address, QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusServer *ritual_ZN11QDBusServerC1ERK7QStringP7QObject(
    const QString *address,
    QObject *parent) {
  return new CuteQDBusServer(*address, parent);
}

//  QDBusServer::QDBusServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QDBusServer *ritual_ZN11QDBusServerC1EP7QObject(QObject *parent) {
  return new CuteQDBusServer(parent);
}

//  QDBusServer::~QDBusServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDBusServerD1Ev(QDBusServer *self) {
  delete self;
}

//  bool QDBusServer::isConnected() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDBusServer11isConnectedEv(const QDBusServer *self) {
  return self->isConnected();
}

//  QDBusError QDBusServer::lastError() const
extern "C" Q_DECL_EXPORT
QDBusError *ritual_ZNK11QDBusServer9lastErrorEv(const QDBusServer *self) {
  return new QDBusError(self->lastError());
}

//  QString QDBusServer::address() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDBusServer7addressEv(const QDBusServer *self) {
  return new QString(self->address());
}

//  void QDBusServer::setAnonymousAuthenticationAllowed(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDBusServer33setAnonymousAuthenticationAllowedEb(
    QDBusServer *self,
    bool value) {
  self->setAnonymousAuthenticationAllowed(value);
}

//  bool QDBusServer::isAnonymousAuthenticationAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDBusServer32isAnonymousAuthenticationAllowedEv(
    const QDBusServer *self) {
  return self->isAnonymousAuthenticationAllowed();
}

//  void QDBusServer::newConnection(const QDBusConnection &connection)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDBusServer13newConnectionERK15QDBusConnection(
    QDBusServer *self,
    const QDBusConnection *connection) {
  self->newConnection(*connection);
}

//  a Python function taken by a CuteQDBusServer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDBusServer(
    QDBusServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDBusServer *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_DBUS)
