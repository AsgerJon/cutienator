//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslserver.h>
#endif
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>

//  A QSslServerPrivate that Python can take functions over in. Every QSslServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSslServerPrivateCall0)(const void *, int *);
typedef void (*CuteQSslServerPrivateCall1)(const void *, int *);
typedef void (*CuteQSslServerPrivateCall2)(const void *, int *);
typedef void (*CuteQSslServerPrivateCall3)(const void *, int *);
typedef void (*CuteQSslServerPrivateCall4)(const void *, int *);
typedef void (*CuteQSslServerPrivateCall5)(const void *, int *);
typedef void (*CuteQSslServerPrivateCall6)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQSslServerPrivateCall7)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
class CuteQSslServerPrivate : public QSslServerPrivate {
public:
  using QSslServerPrivate::QSslServerPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QTcpServerPrivate23totalPendingConnectionsEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QTcpServerPrivate22configureCreatedSocketEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver16readNotificationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17closeNotificationEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17writeNotificationEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver22connectionNotificationEv")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
    return false;
  }

  //  int QSslServerPrivate::totalPendingConnections() const
  int totalPendingConnections() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSslServerPrivateCall0 call = reinterpret_cast<CuteQSslServerPrivateCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSslServerPrivate::totalPendingConnections();
  }

  //  void QTcpServerPrivate::configureCreatedSocket()
  void configureCreatedSocket() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSslServerPrivateCall1 call = reinterpret_cast<CuteQSslServerPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::configureCreatedSocket();
  }

  //  void QTcpServerPrivate::readNotification()
  void readNotification() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSslServerPrivateCall2 call = reinterpret_cast<CuteQSslServerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::readNotification();
  }

  //  void QTcpServerPrivate::closeNotification()
  void closeNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSslServerPrivateCall3 call = reinterpret_cast<CuteQSslServerPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::closeNotification();
  }

  //  void QTcpServerPrivate::writeNotification()
  void writeNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSslServerPrivateCall4 call = reinterpret_cast<CuteQSslServerPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::writeNotification();
  }

  //  void QTcpServerPrivate::exceptionNotification()
  void exceptionNotification() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSslServerPrivateCall5 call = reinterpret_cast<CuteQSslServerPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::exceptionNotification();
  }

  //  void QTcpServerPrivate::connectionNotification()
  void connectionNotification() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSslServerPrivateCall6 call = reinterpret_cast<CuteQSslServerPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::connectionNotification();
  }

#if !defined(QT_NO_NETWORKPROXY)
  //  void QTcpServerPrivate::proxyAuthenticationRequired(const
  //      QNetworkProxy &a0, QAuthenticator *a1)
  void proxyAuthenticationRequired(
      const QNetworkProxy &a0,
      QAuthenticator *a1) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSslServerPrivateCall7 call = reinterpret_cast<CuteQSslServerPrivateCall7>(taken[7]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::proxyAuthenticationRequired(a0, a1);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
};

//  QSslServer *QSslServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSslServer *ritual_ZN17QSslServerPrivate6q_funcEv(QSslServerPrivate *self) {
  return self->q_func();
}

//  const QSslServer *QSslServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSslServer *ritual_ZNK17QSslServerPrivate6q_funcEv(
    const QSslServerPrivate *self) {
  return self->q_func();
}

//  QSslServerPrivate::QSslServerPrivate()
extern "C" Q_DECL_EXPORT
QSslServerPrivate *ritual_ZN17QSslServerPrivateC1Ev() {
  return new CuteQSslServerPrivate();
}

//  void QSslServerPrivate::checkClientHelloAndContinue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslServerPrivate27checkClientHelloAndContinueEv(
    QSslServerPrivate *self) {
  self->checkClientHelloAndContinue();
}

//  void QSslServerPrivate::initializeHandshakeProcess(QSslSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslServerPrivate26initializeHandshakeProcessEP10QSslSocket(
    QSslServerPrivate *self,
    QSslSocket *socket) {
  self->initializeHandshakeProcess(socket);
}

//  void QSslServerPrivate::removeSocketData(quintptr socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslServerPrivate16removeSocketDataEy(
    QSslServerPrivate *self,
    quintptr socket) {
  self->removeSocketData(socket);
}

//  void QSslServerPrivate::handleHandshakeTimedOut(QSslSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslServerPrivate23handleHandshakeTimedOutEP10QSslSocket(
    QSslServerPrivate *self,
    QSslSocket *socket) {
  self->handleHandshakeTimedOut(socket);
}

//  int QSslServerPrivate::totalPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSslServerPrivate23totalPendingConnectionsEv(
    const QSslServerPrivate *self) {
  return self->totalPendingConnections();
}

//  a Python function taken by a CuteQSslServerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSslServerPrivate(
    QSslServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSslServerPrivate *>(self)->take(key, call);
}

//  int QSslServerPrivate::totalPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QSslServerPrivate23totalPendingConnectionsEv(
    const QSslServerPrivate *self) {
  return self->QSslServerPrivate::totalPendingConnections();
}

#endif  // QT_CONFIG(ssl)
