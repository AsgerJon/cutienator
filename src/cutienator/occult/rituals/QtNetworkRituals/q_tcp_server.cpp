//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qtcpserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtcpserver.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QTcpServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTcpServer : QTcpServer {
  using QTcpServer::incomingConnection;
};

//  A QTcpServer that Python can take functions over in. Every QTcpServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTcpServerCall0)(const void *, int *);
typedef void * (*CuteQTcpServerCall1)(const void *, int *);
typedef void (*CuteQTcpServerCall2)(const void *, qintptr, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTcpServerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTcpServerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpServerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpServerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpServerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTcpServerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTcpServer : public QTcpServer {
public:
  using QTcpServer::QTcpServer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10QTcpServer21hasPendingConnectionsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QTcpServer21nextPendingConnectionEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QTcpServer18incomingConnectionEx")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QTcpServer::hasPendingConnections() const
  bool hasPendingConnections() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTcpServerCall0 call = reinterpret_cast<CuteQTcpServerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTcpServer::hasPendingConnections();
  }

  //  QTcpSocket *QTcpServer::nextPendingConnection()
  QTcpSocket *nextPendingConnection() override {
    if (taken[1]) {
      int handled = 0;
      CuteQTcpServerCall1 call = reinterpret_cast<CuteQTcpServerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTcpSocket *>(given);
    }
    return QTcpServer::nextPendingConnection();
  }

  //  void QTcpServer::incomingConnection(qintptr handle)
  void incomingConnection(qintptr handle) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTcpServerCall2 call = reinterpret_cast<CuteQTcpServerCall2>(taken[2]);
      call(this, handle, &handled);
      if (handled) return;
    }
    QTcpServer::incomingConnection(handle);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTcpServerCall3 call = reinterpret_cast<CuteQTcpServerCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTcpServerCall4 call = reinterpret_cast<CuteQTcpServerCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTcpServerCall5 call = reinterpret_cast<CuteQTcpServerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTcpServerCall6 call = reinterpret_cast<CuteQTcpServerCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTcpServerCall7 call = reinterpret_cast<CuteQTcpServerCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQTcpServerCall8 call = reinterpret_cast<CuteQTcpServerCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTcpServerCall9 call = reinterpret_cast<CuteQTcpServerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QTcpServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTcpServer10metaObjectEv(
    const QTcpServer *self) {
  return self->metaObject();
}

//  QString QTcpServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTcpServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTcpServer::tr(s, c, n));
}

//  QTcpServer::QTcpServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QTcpServer *ritual_ZN10QTcpServerC1EP7QObject(QObject *parent) {
  return new CuteQTcpServer(parent);
}

//  QTcpServer::~QTcpServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServerD1Ev(QTcpServer *self) {
  delete self;
}

//  bool QTcpServer::listen(const QHostAddress &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTcpServer6listenERK12QHostAddresst(
    QTcpServer *self,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}

//  void QTcpServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer5closeEv(QTcpServer *self) {
  self->close();
}

//  bool QTcpServer::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTcpServer11isListeningEv(const QTcpServer *self) {
  return self->isListening();
}

//  void QTcpServer::setMaxPendingConnections(int numConnections)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer24setMaxPendingConnectionsEi(
    QTcpServer *self,
    int numConnections) {
  self->setMaxPendingConnections(numConnections);
}

//  int QTcpServer::maxPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTcpServer21maxPendingConnectionsEv(const QTcpServer *self) {
  return self->maxPendingConnections();
}

//  void QTcpServer::setListenBacklogSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer20setListenBacklogSizeEi(
    QTcpServer *self,
    int size) {
  self->setListenBacklogSize(size);
}

//  int QTcpServer::listenBacklogSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTcpServer17listenBacklogSizeEv(const QTcpServer *self) {
  return self->listenBacklogSize();
}

//  quint16 QTcpServer::serverPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK10QTcpServer10serverPortEv(const QTcpServer *self) {
  return self->serverPort();
}

//  QHostAddress QTcpServer::serverAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK10QTcpServer13serverAddressEv(
    const QTcpServer *self) {
  return new QHostAddress(self->serverAddress());
}

//  qintptr QTcpServer::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK10QTcpServer16socketDescriptorEv(const QTcpServer *self) {
  return self->socketDescriptor();
}

//  bool QTcpServer::setSocketDescriptor(qintptr socketDescriptor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTcpServer19setSocketDescriptorEx(
    QTcpServer *self,
    qintptr socketDescriptor) {
  return self->setSocketDescriptor(socketDescriptor);
}

//  bool QTcpServer::waitForNewConnection(int msec, bool *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTcpServer20waitForNewConnectionEiPb(
    QTcpServer *self,
    int msec,
    bool *timedOut) {
  return self->waitForNewConnection(msec, timedOut);
}

//  bool QTcpServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QTcpServer21hasPendingConnectionsEv(
    const QTcpServer *self) {
  return self->hasPendingConnections();
}

//  QTcpSocket *QTcpServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QTcpSocket *ritual_ZN10QTcpServer21nextPendingConnectionEv(
    QTcpServer *self) {
  return self->nextPendingConnection();
}

//  QAbstractSocket::SocketError QTcpServer::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK10QTcpServer11serverErrorEv(
    const QTcpServer *self) {
  return self->serverError();
}

//  QString QTcpServer::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QTcpServer11errorStringEv(const QTcpServer *self) {
  return new QString(self->errorString());
}

//  void QTcpServer::pauseAccepting()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer14pauseAcceptingEv(QTcpServer *self) {
  self->pauseAccepting();
}

//  void QTcpServer::resumeAccepting()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer15resumeAcceptingEv(QTcpServer *self) {
  self->resumeAccepting();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QTcpServer::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer8setProxyERK13QNetworkProxy(
    QTcpServer *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QTcpServer::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK10QTcpServer5proxyEv(const QTcpServer *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QTcpServer::incomingConnection(qintptr handle)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer18incomingConnectionEx(
    QTcpServer *self,
    qintptr handle) {
  self->incomingConnection(handle);
}

//  void QTcpServer::addPendingConnection(QTcpSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTcpServer20addPendingConnectionEP10QTcpSocket(
    QTcpServer *self,
    QTcpSocket *socket) {
  self->addPendingConnection(socket);
}

//  QTcpServerPrivate *QTcpServer::d_func()
extern "C" Q_DECL_EXPORT
QTcpServerPrivate *ritual_ZN10QTcpServer6d_funcEv(QTcpServer *self) {
  return self->d_func();
}

//  const QTcpServerPrivate *QTcpServer::d_func() const
extern "C" Q_DECL_EXPORT
const QTcpServerPrivate *ritual_ZNK10QTcpServer6d_funcEv(
    const QTcpServer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQTcpServer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTcpServer(QTcpServer *self, const char *key, void *call) {
  return static_cast<CuteQTcpServer *>(self)->take(key, call);
}

//  bool QTcpServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK10QTcpServer21hasPendingConnectionsEv(
    const QTcpServer *self) {
  return self->QTcpServer::hasPendingConnections();
}

//  QTcpSocket *QTcpServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QTcpSocket *ritual_own_ZN10QTcpServer21nextPendingConnectionEv(
    QTcpServer *self) {
  return self->QTcpServer::nextPendingConnection();
}

//  void QTcpServer::incomingConnection(qintptr handle)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QTcpServer18incomingConnectionEx(
    QTcpServer *self,
    qintptr handle) {
  static_cast<OwnQTcpServer *>(self)->OwnQTcpServer::incomingConnection(
      handle);
}
