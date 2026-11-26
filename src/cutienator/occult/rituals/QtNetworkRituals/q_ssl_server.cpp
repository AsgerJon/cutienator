//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslserver.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslserver.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QSslServer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQSslServer : QSslServer {
  using QSslServer::incomingConnection;
};

//  A QSslServer that Python can take functions over in. Every QSslServer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(ssl)
typedef void (*CuteQSslServerCall0)(const void *, qintptr, int *);
#endif  // QT_CONFIG(ssl)
typedef bool (*CuteQSslServerCall1)(const void *, int *);
typedef void * (*CuteQSslServerCall2)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSslServerCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSslServerCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslServerCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslServerCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslServerCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslServerCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSslServerCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSslServer : public QSslServer {
public:
  using QSslServer::QSslServer;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN10QTcpServer18incomingConnectionEx")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK10QTcpServer21hasPendingConnectionsEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QTcpServer21nextPendingConnectionEv")) {
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

#if QT_CONFIG(ssl)
  //  void QSslServer::incomingConnection(qintptr socket)
  void incomingConnection(qintptr socket) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSslServerCall0 call = reinterpret_cast<CuteQSslServerCall0>(taken[0]);
      call(this, socket, &handled);
      if (handled) return;
    }
    QSslServer::incomingConnection(socket);
  }
#endif  // QT_CONFIG(ssl)

  //  bool QTcpServer::hasPendingConnections() const
  bool hasPendingConnections() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSslServerCall1 call = reinterpret_cast<CuteQSslServerCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTcpServer::hasPendingConnections();
  }

  //  QTcpSocket *QTcpServer::nextPendingConnection()
  QTcpSocket *nextPendingConnection() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSslServerCall2 call = reinterpret_cast<CuteQSslServerCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QTcpSocket *>(given);
    }
    return QTcpServer::nextPendingConnection();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSslServerCall3 call = reinterpret_cast<CuteQSslServerCall3>(taken[3]);
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
      CuteQSslServerCall4 call = reinterpret_cast<CuteQSslServerCall4>(taken[4]);
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
      CuteQSslServerCall5 call = reinterpret_cast<CuteQSslServerCall5>(taken[5]);
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
      CuteQSslServerCall6 call = reinterpret_cast<CuteQSslServerCall6>(taken[6]);
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
      CuteQSslServerCall7 call = reinterpret_cast<CuteQSslServerCall7>(taken[7]);
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
      CuteQSslServerCall8 call = reinterpret_cast<CuteQSslServerCall8>(taken[8]);
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
      CuteQSslServerCall9 call = reinterpret_cast<CuteQSslServerCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSslServer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QSslServer10metaObjectEv(
    const QSslServer *self) {
  return self->metaObject();
}

//  void *QSslServer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10QSslServer11qt_metacastEPKc(
    QSslServer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSslServer::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10QSslServer11qt_metacallEN11QMetaObject4CallEiPPv(
    QSslServer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QSslServer::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QSslServer2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSslServer::tr(s, c, n));
}

//  QSslServer::QSslServer(QObject *parent)
extern "C" Q_DECL_EXPORT
QSslServer *ritual_ZN10QSslServerC1EP7QObject(QObject *parent) {
  return new CuteQSslServer(parent);
}

//  QSslServer::~QSslServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServerD1Ev(QSslServer *self) {
  delete self;
}

//  void QSslServer::setSslConfiguration(const QSslConfiguration
//      &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer19setSslConfigurationERK17QSslConfiguration(
    QSslServer *self,
    const QSslConfiguration *sslConfiguration) {
  self->setSslConfiguration(*sslConfiguration);
}

//  QSslConfiguration QSslServer::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK10QSslServer16sslConfigurationEv(
    const QSslServer *self) {
  return new QSslConfiguration(self->sslConfiguration());
}

//  void QSslServer::setHandshakeTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer19setHandshakeTimeoutEi(
    QSslServer *self,
    int timeout) {
  self->setHandshakeTimeout(timeout);
}

//  int QSslServer::handshakeTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSslServer16handshakeTimeoutEv(const QSslServer *self) {
  return self->handshakeTimeout();
}

//  void QSslServer::sslErrors(QSslSocket *socket, const QList<QSslError>
//      &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer9sslErrorsEP10QSslSocketRK5QListI9QSslErrorE(
    QSslServer *self,
    QSslSocket *socket,
    const QList<QSslError> *errors) {
  self->sslErrors(socket, *errors);
}

//  void QSslServer::peerVerifyError(QSslSocket *socket, const QSslError
//      &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer15peerVerifyErrorEP10QSslSocketRK9QSslError(
    QSslServer *self,
    QSslSocket *socket,
    const QSslError *error) {
  self->peerVerifyError(socket, *error);
}

//  void QSslServer::errorOccurred(QSslSocket *socket,
//      QAbstractSocket::SocketError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer13errorOccurredEP10QSslSocketN15QAbstractSocket11SocketErrorE(
    QSslServer *self,
    QSslSocket *socket,
    QAbstractSocket::SocketError error) {
  self->errorOccurred(socket, error);
}

//  void QSslServer::preSharedKeyAuthenticationRequired(QSslSocket *socket,
//      QSslPreSharedKeyAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer34preSharedKeyAuthenticationRequiredEP10QSslSocketP29QSslPreSharedKeyAuthenticator(
    QSslServer *self,
    QSslSocket *socket,
    QSslPreSharedKeyAuthenticator *authenticator) {
  self->preSharedKeyAuthenticationRequired(socket, authenticator);
}

//  void QSslServer::alertSent(QSslSocket *socket, QSsl::AlertLevel level,
//      QSsl::AlertType type, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer9alertSentEP10QSslSocketN4QSsl10AlertLevelENS2_9AlertTypeERK7QString(
    QSslServer *self,
    QSslSocket *socket,
    QSsl::AlertLevel level,
    QSsl::AlertType type,
    const QString *description) {
  self->alertSent(socket, level, type, *description);
}

//  void QSslServer::alertReceived(QSslSocket *socket, QSsl::AlertLevel
//      level, QSsl::AlertType type, const QString &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer13alertReceivedEP10QSslSocketN4QSsl10AlertLevelENS2_9AlertTypeERK7QString(
    QSslServer *self,
    QSslSocket *socket,
    QSsl::AlertLevel level,
    QSsl::AlertType type,
    const QString *description) {
  self->alertReceived(socket, level, type, *description);
}

//  void QSslServer::handshakeInterruptedOnError(QSslSocket *socket, const
//      QSslError &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer27handshakeInterruptedOnErrorEP10QSslSocketRK9QSslError(
    QSslServer *self,
    QSslSocket *socket,
    const QSslError *error) {
  self->handshakeInterruptedOnError(socket, *error);
}

//  void QSslServer::startedEncryptionHandshake(QSslSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer26startedEncryptionHandshakeEP10QSslSocket(
    QSslServer *self,
    QSslSocket *socket) {
  self->startedEncryptionHandshake(socket);
}

//  void QSslServer::incomingConnection(qintptr socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSslServer18incomingConnectionEx(
    QSslServer *self,
    qintptr socket) {
  self->incomingConnection(socket);
}

//  QSslServerPrivate *QSslServer::d_func()
extern "C" Q_DECL_EXPORT
QSslServerPrivate *ritual_ZN10QSslServer6d_funcEv(QSslServer *self) {
  return self->d_func();
}

//  const QSslServerPrivate *QSslServer::d_func() const
extern "C" Q_DECL_EXPORT
const QSslServerPrivate *ritual_ZNK10QSslServer6d_funcEv(
    const QSslServer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSslServer, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSslServer(QSslServer *self, const char *key, void *call) {
  return static_cast<CuteQSslServer *>(self)->take(key, call);
}

//  void QSslServer::incomingConnection(qintptr socket)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10QSslServer18incomingConnectionEx(
    QSslServer *self,
    qintptr socket) {
  static_cast<OwnQSslServer *>(self)->OwnQSslServer::incomingConnection(
      socket);
}

#endif  // QT_CONFIG(ssl)
#endif  // QT_CONFIG(ssl)
