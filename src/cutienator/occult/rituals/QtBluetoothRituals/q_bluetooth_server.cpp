//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtBluetooth/qbluetoothserver.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QBluetoothServer that Python can take functions over in. Every QBluetoothServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothServerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQBluetoothServerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQBluetoothServerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQBluetoothServer : public QBluetoothServer {
public:
  using QBluetoothServer::QBluetoothServer;
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
      CuteQBluetoothServerCall0 call = reinterpret_cast<CuteQBluetoothServerCall0>(taken[0]);
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
      CuteQBluetoothServerCall1 call = reinterpret_cast<CuteQBluetoothServerCall1>(taken[1]);
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
      CuteQBluetoothServerCall2 call = reinterpret_cast<CuteQBluetoothServerCall2>(taken[2]);
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
      CuteQBluetoothServerCall3 call = reinterpret_cast<CuteQBluetoothServerCall3>(taken[3]);
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
      CuteQBluetoothServerCall4 call = reinterpret_cast<CuteQBluetoothServerCall4>(taken[4]);
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
      CuteQBluetoothServerCall5 call = reinterpret_cast<CuteQBluetoothServerCall5>(taken[5]);
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
      CuteQBluetoothServerCall6 call = reinterpret_cast<CuteQBluetoothServerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QBluetoothServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QBluetoothServer10metaObjectEv(
    const QBluetoothServer *self) {
  return self->metaObject();
}

//  QString QBluetoothServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QBluetoothServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QBluetoothServer::tr(s, c, n));
}

//  QBluetoothServer::QBluetoothServer(QBluetoothServiceInfo::Protocol
//      serverType, QObject *parent)
extern "C" Q_DECL_EXPORT
QBluetoothServer *ritual_ZN16QBluetoothServerC1EN21QBluetoothServiceInfo8ProtocolEP7QObject(
    QBluetoothServiceInfo::Protocol serverType,
    QObject *parent) {
  return new CuteQBluetoothServer(serverType, parent);
}

//  QBluetoothServer::~QBluetoothServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothServerD1Ev(QBluetoothServer *self) {
  delete self;
}

//  void QBluetoothServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothServer5closeEv(QBluetoothServer *self) {
  self->close();
}

//  bool QBluetoothServer::listen(const QBluetoothAddress &address, quint16
//      port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QBluetoothServer6listenERK17QBluetoothAddresst(
    QBluetoothServer *self,
    const QBluetoothAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}

//  QBluetoothServiceInfo QBluetoothServer::listen(const QBluetoothUuid
//      &uuid, const QString &serviceName)
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo *ritual_ZN16QBluetoothServer6listenERK14QBluetoothUuidRK7QString(
    QBluetoothServer *self,
    const QBluetoothUuid *uuid,
    const QString *serviceName) {
  return new QBluetoothServiceInfo(self->listen(*uuid, *serviceName));
}

//  bool QBluetoothServer::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QBluetoothServer11isListeningEv(
    const QBluetoothServer *self) {
  return self->isListening();
}

//  void QBluetoothServer::setMaxPendingConnections(int numConnections)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothServer24setMaxPendingConnectionsEi(
    QBluetoothServer *self,
    int numConnections) {
  self->setMaxPendingConnections(numConnections);
}

//  int QBluetoothServer::maxPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QBluetoothServer21maxPendingConnectionsEv(
    const QBluetoothServer *self) {
  return self->maxPendingConnections();
}

//  bool QBluetoothServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QBluetoothServer21hasPendingConnectionsEv(
    const QBluetoothServer *self) {
  return self->hasPendingConnections();
}

//  QBluetoothSocket *QBluetoothServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QBluetoothSocket *ritual_ZN16QBluetoothServer21nextPendingConnectionEv(
    QBluetoothServer *self) {
  return self->nextPendingConnection();
}

//  QBluetoothAddress QBluetoothServer::serverAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK16QBluetoothServer13serverAddressEv(
    const QBluetoothServer *self) {
  return new QBluetoothAddress(self->serverAddress());
}

//  quint16 QBluetoothServer::serverPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK16QBluetoothServer10serverPortEv(
    const QBluetoothServer *self) {
  return self->serverPort();
}

//  void QBluetoothServer::setSecurityFlags(QBluetooth::SecurityFlags
//      security)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QBluetoothServer16setSecurityFlagsE6QFlagsIN10QBluetooth8SecurityEE(
    QBluetoothServer *self,
    int security) {
  self->setSecurityFlags(QFlags<QBluetooth::Security>::fromInt(security));
}

//  QBluetooth::SecurityFlags QBluetoothServer::securityFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QBluetoothServer13securityFlagsEv(
    const QBluetoothServer *self) {
  return static_cast<int>(self->securityFlags().toInt());
}

//  QBluetoothServiceInfo::Protocol QBluetoothServer::serverType() const
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Protocol ritual_ZNK16QBluetoothServer10serverTypeEv(
    const QBluetoothServer *self) {
  return self->serverType();
}

//  Error QBluetoothServer::error() const
extern "C" Q_DECL_EXPORT
QBluetoothServer::Error ritual_ZNK16QBluetoothServer5errorEv(
    const QBluetoothServer *self) {
  return self->error();
}

//  QBluetoothServerPrivate *QBluetoothServer::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothServerPrivate *ritual_ZN16QBluetoothServer6d_funcEv(
    QBluetoothServer *self) {
  return self->d_func();
}

//  const QBluetoothServerPrivate *QBluetoothServer::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothServerPrivate *ritual_ZNK16QBluetoothServer6d_funcEv(
    const QBluetoothServer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQBluetoothServer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBluetoothServer(
    QBluetoothServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBluetoothServer *>(self)->take(key, call);
}
