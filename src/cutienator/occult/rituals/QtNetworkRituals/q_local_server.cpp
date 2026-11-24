//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qlocalserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalserver.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QLocalServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQLocalServer : QLocalServer {
  using QLocalServer::incomingConnection;
};

//  A QLocalServer that Python can take functions over in. Every QLocalServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(localserver)
typedef bool (*CuteQLocalServerCall0)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef void * (*CuteQLocalServerCall1)(const void *, int *);
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
typedef void (*CuteQLocalServerCall2)(const void *, quintptr, int *);
#endif  // QT_CONFIG(localserver)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLocalServerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQLocalServerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalServerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalServerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalServerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQLocalServerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQLocalServer : public QLocalServer {
public:
  using QLocalServer::QLocalServer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZNK12QLocalServer21hasPendingConnectionsEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN12QLocalServer21nextPendingConnectionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
#if QT_CONFIG(localserver)
    if (!std::strcmp(key, "_ZN12QLocalServer18incomingConnectionEy")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(localserver)
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

#if QT_CONFIG(localserver)
  //  bool QLocalServer::hasPendingConnections() const
  bool hasPendingConnections() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQLocalServerCall0 call = reinterpret_cast<CuteQLocalServerCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QLocalServer::hasPendingConnections();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  QLocalSocket *QLocalServer::nextPendingConnection()
  QLocalSocket *nextPendingConnection() override {
    if (taken[1]) {
      int handled = 0;
      CuteQLocalServerCall1 call = reinterpret_cast<CuteQLocalServerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QLocalSocket *>(given);
    }
    return QLocalServer::nextPendingConnection();
  }
#endif  // QT_CONFIG(localserver)

#if QT_CONFIG(localserver)
  //  void QLocalServer::incomingConnection(quintptr socketDescriptor)
  void incomingConnection(quintptr socketDescriptor) override {
    if (taken[2]) {
      int handled = 0;
      CuteQLocalServerCall2 call = reinterpret_cast<CuteQLocalServerCall2>(taken[2]);
      call(this, socketDescriptor, &handled);
      if (handled) return;
    }
    QLocalServer::incomingConnection(socketDescriptor);
  }
#endif  // QT_CONFIG(localserver)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQLocalServerCall3 call = reinterpret_cast<CuteQLocalServerCall3>(taken[3]);
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
      CuteQLocalServerCall4 call = reinterpret_cast<CuteQLocalServerCall4>(taken[4]);
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
      CuteQLocalServerCall5 call = reinterpret_cast<CuteQLocalServerCall5>(taken[5]);
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
      CuteQLocalServerCall6 call = reinterpret_cast<CuteQLocalServerCall6>(taken[6]);
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
      CuteQLocalServerCall7 call = reinterpret_cast<CuteQLocalServerCall7>(taken[7]);
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
      CuteQLocalServerCall8 call = reinterpret_cast<CuteQLocalServerCall8>(taken[8]);
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
      CuteQLocalServerCall9 call = reinterpret_cast<CuteQLocalServerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QLocalServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QLocalServer10metaObjectEv(
    const QLocalServer *self) {
  return self->metaObject();
}

//  QString QLocalServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QLocalServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QLocalServer::tr(s, c, n));
}

//  QLocalServerPrivate *QLocalServer::d_func()
extern "C" Q_DECL_EXPORT
QLocalServerPrivate *ritual_ZN12QLocalServer6d_funcEv(QLocalServer *self) {
  return self->d_func();
}

//  const QLocalServerPrivate *QLocalServer::d_func() const
extern "C" Q_DECL_EXPORT
const QLocalServerPrivate *ritual_ZNK12QLocalServer6d_funcEv(
    const QLocalServer *self) {
  return self->d_func();
}

//  QLocalServer::QLocalServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QLocalServer *ritual_ZN12QLocalServerC1EP7QObject(QObject *parent) {
  return new CuteQLocalServer(parent);
}

//  QLocalServer::~QLocalServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServerD1Ev(QLocalServer *self) {
  delete self;
}

//  void QLocalServer::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServer5closeEv(QLocalServer *self) {
  self->close();
}

//  QString QLocalServer::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QLocalServer11errorStringEv(const QLocalServer *self) {
  return new QString(self->errorString());
}

//  bool QLocalServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLocalServer21hasPendingConnectionsEv(
    const QLocalServer *self) {
  return self->hasPendingConnections();
}

//  bool QLocalServer::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QLocalServer11isListeningEv(const QLocalServer *self) {
  return self->isListening();
}

//  bool QLocalServer::listen(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalServer6listenERK7QString(
    QLocalServer *self,
    const QString *name) {
  return self->listen(*name);
}

//  bool QLocalServer::listen(qintptr socketDescriptor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalServer6listenEx(
    QLocalServer *self,
    qintptr socketDescriptor) {
  return self->listen(socketDescriptor);
}

//  int QLocalServer::maxPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLocalServer21maxPendingConnectionsEv(
    const QLocalServer *self) {
  return self->maxPendingConnections();
}

//  QLocalSocket *QLocalServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QLocalSocket *ritual_ZN12QLocalServer21nextPendingConnectionEv(
    QLocalServer *self) {
  return self->nextPendingConnection();
}

//  QString QLocalServer::serverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QLocalServer10serverNameEv(const QLocalServer *self) {
  return new QString(self->serverName());
}

//  QString QLocalServer::fullServerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QLocalServer14fullServerNameEv(
    const QLocalServer *self) {
  return new QString(self->fullServerName());
}

//  bool QLocalServer::removeServer(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalServer12removeServerERK7QString(const QString *name) {
  return QLocalServer::removeServer(*name);
}

//  QAbstractSocket::SocketError QLocalServer::serverError() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketError ritual_ZNK12QLocalServer11serverErrorEv(
    const QLocalServer *self) {
  return self->serverError();
}

//  void QLocalServer::setMaxPendingConnections(int numConnections)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServer24setMaxPendingConnectionsEi(
    QLocalServer *self,
    int numConnections) {
  self->setMaxPendingConnections(numConnections);
}

//  bool QLocalServer::waitForNewConnection(int msec, bool *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLocalServer20waitForNewConnectionEiPb(
    QLocalServer *self,
    int msec,
    bool *timedOut) {
  return self->waitForNewConnection(msec, timedOut);
}

//  void QLocalServer::setListenBacklogSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServer20setListenBacklogSizeEi(
    QLocalServer *self,
    int size) {
  self->setListenBacklogSize(size);
}

//  int QLocalServer::listenBacklogSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLocalServer17listenBacklogSizeEv(const QLocalServer *self) {
  return self->listenBacklogSize();
}

//  void QLocalServer::setSocketOptions(SocketOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServer16setSocketOptionsE6QFlagsINS_12SocketOptionEE(
    QLocalServer *self,
    int options) {
  self->setSocketOptions(
      QFlags<QLocalServer::SocketOption>::fromInt(options));
}

//  SocketOptions QLocalServer::socketOptions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QLocalServer13socketOptionsEv(const QLocalServer *self) {
  return static_cast<int>(self->socketOptions().toInt());
}

//  qintptr QLocalServer::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK12QLocalServer16socketDescriptorEv(
    const QLocalServer *self) {
  return self->socketDescriptor();
}

//  void QLocalServer::incomingConnection(quintptr socketDescriptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServer18incomingConnectionEy(
    QLocalServer *self,
    quintptr socketDescriptor) {
  self->incomingConnection(socketDescriptor);
}

//  void QLocalServer::addPendingConnection(QLocalSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QLocalServer20addPendingConnectionEP12QLocalSocket(
    QLocalServer *self,
    QLocalSocket *socket) {
  self->addPendingConnection(socket);
}

//  a Python function taken by a CuteQLocalServer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QLocalServer(
    QLocalServer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQLocalServer *>(self)->take(key, call);
}

//  bool QLocalServer::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK12QLocalServer21hasPendingConnectionsEv(
    const QLocalServer *self) {
  return self->QLocalServer::hasPendingConnections();
}

//  QLocalSocket *QLocalServer::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QLocalSocket *ritual_own_ZN12QLocalServer21nextPendingConnectionEv(
    QLocalServer *self) {
  return self->QLocalServer::nextPendingConnection();
}

//  void QLocalServer::incomingConnection(quintptr socketDescriptor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QLocalServer18incomingConnectionEy(
    QLocalServer *self,
    quintptr socketDescriptor) {
  static_cast<OwnQLocalServer *>(self)->OwnQLocalServer::incomingConnection(
      socketDescriptor);
}

#endif  // QT_CONFIG(localserver)
