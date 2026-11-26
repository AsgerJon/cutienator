//  Written by dev_tooling.RitualGenerator from the records of
//  QtRemoteObjects/qconnectionfactories.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtRemoteObjects/qconnectionfactories.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QConnectionAbstractServer that Python can take functions over in. Every QConnectionAbstractServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQConnectionAbstractServerCall0)(const void *, int *);
typedef const QUrl * (*CuteQConnectionAbstractServerCall1)(const void *, int *);
typedef bool (*CuteQConnectionAbstractServerCall2)(const void *, const QUrl *, int *);
typedef int (*CuteQConnectionAbstractServerCall3)(const void *, int *);
typedef void (*CuteQConnectionAbstractServerCall4)(const void *, int *);
typedef void * (*CuteQConnectionAbstractServerCall5)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQConnectionAbstractServerCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQConnectionAbstractServerCall7)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConnectionAbstractServerCall8)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConnectionAbstractServerCall9)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConnectionAbstractServerCall10)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConnectionAbstractServerCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQConnectionAbstractServerCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQConnectionAbstractServer : public QConnectionAbstractServer {
public:
  using QConnectionAbstractServer::QConnectionAbstractServer;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK25QConnectionAbstractServer21hasPendingConnectionsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QConnectionAbstractServer7addressEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QConnectionAbstractServer6listenERK4QUrl")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK25QConnectionAbstractServer11serverErrorEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QConnectionAbstractServer5closeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN25QConnectionAbstractServer22configureNewConnectionEv")) {
      taken[5] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QConnectionAbstractServer::hasPendingConnections() const
  bool hasPendingConnections() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall0 call = reinterpret_cast<CuteQConnectionAbstractServerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QUrl QConnectionAbstractServer::address() const
  QUrl address() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall1 call = reinterpret_cast<CuteQConnectionAbstractServerCall1>(taken[1]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QConnectionAbstractServer::listen(const QUrl &address)
  bool listen(const QUrl &address) override {
    if (taken[2]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall2 call = reinterpret_cast<CuteQConnectionAbstractServerCall2>(taken[2]);
      bool given = call(this, &address, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QAbstractSocket::SocketError QConnectionAbstractServer::serverError()
  //      const
  QAbstractSocket::SocketError serverError() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall3 call = reinterpret_cast<CuteQConnectionAbstractServerCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractSocket::SocketError>(given);
    }
    return {};
  }

  //  void QConnectionAbstractServer::close()
  void close() override {
    if (taken[4]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall4 call = reinterpret_cast<CuteQConnectionAbstractServerCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  QtROServerIoDevice
  //      *QConnectionAbstractServer::configureNewConnection()
  QtROServerIoDevice *configureNewConnection() override {
    if (taken[5]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall5 call = reinterpret_cast<CuteQConnectionAbstractServerCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QtROServerIoDevice *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall6 call = reinterpret_cast<CuteQConnectionAbstractServerCall6>(taken[6]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall7 call = reinterpret_cast<CuteQConnectionAbstractServerCall7>(taken[7]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall8 call = reinterpret_cast<CuteQConnectionAbstractServerCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall9 call = reinterpret_cast<CuteQConnectionAbstractServerCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall10 call = reinterpret_cast<CuteQConnectionAbstractServerCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall11 call = reinterpret_cast<CuteQConnectionAbstractServerCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQConnectionAbstractServerCall12 call = reinterpret_cast<CuteQConnectionAbstractServerCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QConnectionAbstractServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QConnectionAbstractServer10metaObjectEv(
    const QConnectionAbstractServer *self) {
  return self->metaObject();
}

//  void *QConnectionAbstractServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN25QConnectionAbstractServer11qt_metacastEPKc(
    QConnectionAbstractServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QConnectionAbstractServer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN25QConnectionAbstractServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QConnectionAbstractServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QConnectionAbstractServer::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QConnectionAbstractServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QConnectionAbstractServer::tr(s, c, n));
}

//  QConnectionAbstractServer::QConnectionAbstractServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QConnectionAbstractServer *ritual_ZN25QConnectionAbstractServerC1EP7QObject(
    QObject *parent) {
  return new CuteQConnectionAbstractServer(parent);
}

//  QConnectionAbstractServer::~QConnectionAbstractServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QConnectionAbstractServerD1Ev(
    QConnectionAbstractServer *self) {
  delete self;
}

//  bool QConnectionAbstractServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QConnectionAbstractServer21hasPendingConnectionsEv(
    const QConnectionAbstractServer *self) {
  return self->hasPendingConnections();
}

//  QtROServerIoDevice *QConnectionAbstractServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QtROServerIoDevice *ritual_ZN25QConnectionAbstractServer21nextPendingConnectionEv(
    QConnectionAbstractServer *self) {
  return self->nextPendingConnection();
}

//  QUrl QConnectionAbstractServer::address() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK25QConnectionAbstractServer7addressEv(
    const QConnectionAbstractServer *self) {
  return new QUrl(self->address());
}

//  bool QConnectionAbstractServer::listen(const QUrl &address)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QConnectionAbstractServer6listenERK4QUrl(
    QConnectionAbstractServer *self,
    const QUrl *address) {
  return self->listen(*address);
}

//  QAbstractSocket::SocketError QConnectionAbstractServer::serverError()
//      const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK25QConnectionAbstractServer11serverErrorEv(
    const QConnectionAbstractServer *self) {
  return self->serverError();
}

//  void QConnectionAbstractServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QConnectionAbstractServer5closeEv(
    QConnectionAbstractServer *self) {
  self->close();
}

//  QtROServerIoDevice *QConnectionAbstractServer::configureNewConnection()
extern "C" Q_DECL_EXPORT
QtROServerIoDevice *ritual_ZN25QConnectionAbstractServer22configureNewConnectionEv(
    QConnectionAbstractServer *self) {
  return self->configureNewConnection();
}

//  void QConnectionAbstractServer::newConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QConnectionAbstractServer13newConnectionEv(
    QConnectionAbstractServer *self) {
  self->newConnection();
}

//  a Python function taken by a CuteQConnectionAbstractServer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QConnectionAbstractServer(
    QConnectionAbstractServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQConnectionAbstractServer *>(self)->take(key, call);
}
