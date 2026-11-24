//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/qwebsocketserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebSockets/qwebsocketserver.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWebSocketServer that Python can take functions over in. Every QWebSocketServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQWebSocketServerCall0)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketServerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketServerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketServerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketServerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketServerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketServerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketServerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebSocketServer : public QWebSocketServer {
public:
  using QWebSocketServer::QWebSocketServer;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QWebSocketServer21nextPendingConnectionEv")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QWebSocket *QWebSocketServer::nextPendingConnection()
  QWebSocket *nextPendingConnection() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebSocketServerCall0 call = reinterpret_cast<CuteQWebSocketServerCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWebSocket *>(given);
    }
    return QWebSocketServer::nextPendingConnection();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQWebSocketServerCall1 call = reinterpret_cast<CuteQWebSocketServerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWebSocketServerCall2 call = reinterpret_cast<CuteQWebSocketServerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWebSocketServerCall3 call = reinterpret_cast<CuteQWebSocketServerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQWebSocketServerCall4 call = reinterpret_cast<CuteQWebSocketServerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWebSocketServerCall5 call = reinterpret_cast<CuteQWebSocketServerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWebSocketServerCall6 call = reinterpret_cast<CuteQWebSocketServerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWebSocketServerCall7 call = reinterpret_cast<CuteQWebSocketServerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebSocketServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QWebSocketServer10metaObjectEv(
    const QWebSocketServer *self) {
  return self->metaObject();
}

//  QString QWebSocketServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QWebSocketServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebSocketServer::tr(s, c, n));
}

//  QWebSocketServerPrivate *QWebSocketServer::d_func()
extern "C" Q_DECL_EXPORT
QWebSocketServerPrivate *ritual_ZN16QWebSocketServer6d_funcEv(
    QWebSocketServer *self) {
  return self->d_func();
}

//  const QWebSocketServerPrivate *QWebSocketServer::d_func() const
extern "C" Q_DECL_EXPORT
const QWebSocketServerPrivate *ritual_ZNK16QWebSocketServer6d_funcEv(
    const QWebSocketServer *self) {
  return self->d_func();
}

//  QWebSocketServer::QWebSocketServer(const QString &serverName, SslMode
//      secureMode, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebSocketServer *ritual_ZN16QWebSocketServerC1ERK7QStringNS_7SslModeEP7QObject(
    const QString *serverName,
    QWebSocketServer::SslMode secureMode,
    QObject *parent) {
  return new CuteQWebSocketServer(*serverName, secureMode, parent);
}

//  QWebSocketServer::~QWebSocketServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServerD1Ev(QWebSocketServer *self) {
  delete self;
}

//  bool QWebSocketServer::listen(const QHostAddress &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QWebSocketServer6listenERK12QHostAddresst(
    QWebSocketServer *self,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}

//  void QWebSocketServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer5closeEv(QWebSocketServer *self) {
  self->close();
}

//  bool QWebSocketServer::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebSocketServer11isListeningEv(
    const QWebSocketServer *self) {
  return self->isListening();
}

//  void QWebSocketServer::setMaxPendingConnections(int numConnections)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer24setMaxPendingConnectionsEi(
    QWebSocketServer *self,
    int numConnections) {
  self->setMaxPendingConnections(numConnections);
}

//  int QWebSocketServer::maxPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWebSocketServer21maxPendingConnectionsEv(
    const QWebSocketServer *self) {
  return self->maxPendingConnections();
}

//  void QWebSocketServer::setHandshakeTimeout(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer19setHandshakeTimeoutEi(
    QWebSocketServer *self,
    int msec) {
  self->setHandshakeTimeout(msec);
}

//  int QWebSocketServer::handshakeTimeoutMS() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QWebSocketServer18handshakeTimeoutMSEv(
    const QWebSocketServer *self) {
  return self->handshakeTimeoutMS();
}

//  quint16 QWebSocketServer::serverPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK16QWebSocketServer10serverPortEv(
    const QWebSocketServer *self) {
  return self->serverPort();
}

//  QHostAddress QWebSocketServer::serverAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK16QWebSocketServer13serverAddressEv(
    const QWebSocketServer *self) {
  return new QHostAddress(self->serverAddress());
}

//  QUrl QWebSocketServer::serverUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK16QWebSocketServer9serverUrlEv(
    const QWebSocketServer *self) {
  return new QUrl(self->serverUrl());
}

//  SslMode QWebSocketServer::secureMode() const
extern "C" Q_DECL_EXPORT
QWebSocketServer::SslMode ritual_ZNK16QWebSocketServer10secureModeEv(
    const QWebSocketServer *self) {
  return self->secureMode();
}

//  bool QWebSocketServer::setSocketDescriptor(qintptr socketDescriptor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QWebSocketServer19setSocketDescriptorEx(
    QWebSocketServer *self,
    qintptr socketDescriptor) {
  return self->setSocketDescriptor(socketDescriptor);
}

//  qintptr QWebSocketServer::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK16QWebSocketServer16socketDescriptorEv(
    const QWebSocketServer *self) {
  return self->socketDescriptor();
}

#if QT_DEPRECATED_SINCE(6, 2)
//  bool QWebSocketServer::setNativeDescriptor(qintptr descriptor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QWebSocketServer19setNativeDescriptorEx(
    QWebSocketServer *self,
    qintptr descriptor) {
  return self->setNativeDescriptor(descriptor);
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

#if QT_DEPRECATED_SINCE(6, 2)
//  qintptr QWebSocketServer::nativeDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK16QWebSocketServer16nativeDescriptorEv(
    const QWebSocketServer *self) {
  return self->nativeDescriptor();
}
#endif  // QT_DEPRECATED_SINCE(6, 2)

//  bool QWebSocketServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QWebSocketServer21hasPendingConnectionsEv(
    const QWebSocketServer *self) {
  return self->hasPendingConnections();
}

//  QWebSocket *QWebSocketServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_ZN16QWebSocketServer21nextPendingConnectionEv(
    QWebSocketServer *self) {
  return self->nextPendingConnection();
}

//  QWebSocketProtocol::CloseCode QWebSocketServer::error() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK16QWebSocketServer5errorEv(
    const QWebSocketServer *self) {
  return self->error();
}

//  QString QWebSocketServer::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QWebSocketServer11errorStringEv(
    const QWebSocketServer *self) {
  return new QString(self->errorString());
}

//  void QWebSocketServer::pauseAccepting()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer14pauseAcceptingEv(QWebSocketServer *self) {
  self->pauseAccepting();
}

//  void QWebSocketServer::resumeAccepting()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer15resumeAcceptingEv(QWebSocketServer *self) {
  self->resumeAccepting();
}

//  void QWebSocketServer::setServerName(const QString &serverName)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer13setServerNameERK7QString(
    QWebSocketServer *self,
    const QString *serverName) {
  self->setServerName(*serverName);
}

//  QString QWebSocketServer::serverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QWebSocketServer10serverNameEv(
    const QWebSocketServer *self) {
  return new QString(self->serverName());
}

//  void QWebSocketServer::setSupportedSubprotocols(const QStringList
//      &protocols)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer24setSupportedSubprotocolsERK5QListI7QStringE(
    QWebSocketServer *self,
    const QList<QString> *protocols) {
  self->setSupportedSubprotocols(*protocols);
}

//  QStringList QWebSocketServer::supportedSubprotocols() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QWebSocketServer21supportedSubprotocolsEv(
    const QWebSocketServer *self) {
  return new QList<QString>(self->supportedSubprotocols());
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QWebSocketServer::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer8setProxyERK13QNetworkProxy(
    QWebSocketServer *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QWebSocketServer::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK16QWebSocketServer5proxyEv(
    const QWebSocketServer *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_SSL)
//  void QWebSocketServer::setSslConfiguration(const QSslConfiguration
//      &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QWebSocketServer19setSslConfigurationERK17QSslConfiguration(
    QWebSocketServer *self,
    const QSslConfiguration *sslConfiguration) {
  self->setSslConfiguration(*sslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  QSslConfiguration QWebSocketServer::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK16QWebSocketServer16sslConfigurationEv(
    const QWebSocketServer *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

//  void QWebSocketServer::handleConnection(QTcpSocket *socket) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QWebSocketServer16handleConnectionEP10QTcpSocket(
    const QWebSocketServer *self,
    QTcpSocket *socket) {
  self->handleConnection(socket);
}

//  a Python function taken by a CuteQWebSocketServer, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocketServer(
    QWebSocketServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebSocketServer *>(self)->take(key, call);
}

//  QWebSocket *QWebSocketServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_own_ZN16QWebSocketServer21nextPendingConnectionEv(
    QWebSocketServer *self) {
  return self->QWebSocketServer::nextPendingConnection();
}
