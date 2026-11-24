//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtcpserver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qtcpserver.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtcpserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>

//  A QTcpServerPrivate that Python can take functions over in. Every QTcpServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQTcpServerPrivateCall0)(const void *, int *);
typedef int (*CuteQTcpServerPrivateCall1)(const void *, int *);
typedef void (*CuteQTcpServerPrivateCall2)(const void *, int *);
typedef void (*CuteQTcpServerPrivateCall3)(const void *, int *);
typedef void (*CuteQTcpServerPrivateCall4)(const void *, int *);
typedef void (*CuteQTcpServerPrivateCall5)(const void *, int *);
typedef void (*CuteQTcpServerPrivateCall6)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQTcpServerPrivateCall7)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
class CuteQTcpServerPrivate : public QTcpServerPrivate {
public:
  using QTcpServerPrivate::QTcpServerPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QTcpServerPrivate22configureCreatedSocketEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QTcpServerPrivate23totalPendingConnectionsEv")) {
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

  //  void QTcpServerPrivate::configureCreatedSocket()
  void configureCreatedSocket() override {
    if (taken[0]) {
      int handled = 0;
      CuteQTcpServerPrivateCall0 call = reinterpret_cast<CuteQTcpServerPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::configureCreatedSocket();
  }

  //  int QTcpServerPrivate::totalPendingConnections() const
  int totalPendingConnections() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTcpServerPrivateCall1 call = reinterpret_cast<CuteQTcpServerPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QTcpServerPrivate::totalPendingConnections();
  }

  //  void QTcpServerPrivate::readNotification()
  void readNotification() override {
    if (taken[2]) {
      int handled = 0;
      CuteQTcpServerPrivateCall2 call = reinterpret_cast<CuteQTcpServerPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::readNotification();
  }

  //  void QTcpServerPrivate::closeNotification()
  void closeNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTcpServerPrivateCall3 call = reinterpret_cast<CuteQTcpServerPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::closeNotification();
  }

  //  void QTcpServerPrivate::writeNotification()
  void writeNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQTcpServerPrivateCall4 call = reinterpret_cast<CuteQTcpServerPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::writeNotification();
  }

  //  void QTcpServerPrivate::exceptionNotification()
  void exceptionNotification() override {
    if (taken[5]) {
      int handled = 0;
      CuteQTcpServerPrivateCall5 call = reinterpret_cast<CuteQTcpServerPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::exceptionNotification();
  }

  //  void QTcpServerPrivate::connectionNotification()
  void connectionNotification() override {
    if (taken[6]) {
      int handled = 0;
      CuteQTcpServerPrivateCall6 call = reinterpret_cast<CuteQTcpServerPrivateCall6>(taken[6]);
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
      CuteQTcpServerPrivateCall7 call = reinterpret_cast<CuteQTcpServerPrivateCall7>(taken[7]);
      call(this, &a0, a1, &handled);
      if (handled) return;
    }
    QTcpServerPrivate::proxyAuthenticationRequired(a0, a1);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
};

//  QTcpServer *QTcpServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTcpServer *ritual_ZN17QTcpServerPrivate6q_funcEv(QTcpServerPrivate *self) {
  return self->q_func();
}

//  const QTcpServer *QTcpServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTcpServer *ritual_ZNK17QTcpServerPrivate6q_funcEv(
    const QTcpServerPrivate *self) {
  return self->q_func();
}

//  QTcpServerPrivate::QTcpServerPrivate()
extern "C" Q_DECL_EXPORT
QTcpServerPrivate *ritual_ZN17QTcpServerPrivateC1Ev() {
  return new CuteQTcpServerPrivate();
}

//  QTcpServerPrivate::~QTcpServerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivateD1Ev(QTcpServerPrivate *self) {
  delete self;
}

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QTcpServerPrivate::resolveProxy(const QHostAddress
//      &address, quint16 port)
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZN17QTcpServerPrivate12resolveProxyERK12QHostAddresst(
    QTcpServerPrivate *self,
    const QHostAddress *address,
    quint16 port) {
  return new QNetworkProxy(self->resolveProxy(*address, port));
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QTcpServerPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate22configureCreatedSocketEv(
    QTcpServerPrivate *self) {
  self->configureCreatedSocket();
}

//  int QTcpServerPrivate::totalPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTcpServerPrivate23totalPendingConnectionsEv(
    const QTcpServerPrivate *self) {
  return self->totalPendingConnections();
}

//  void QTcpServerPrivate::readNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate16readNotificationEv(
    QTcpServerPrivate *self) {
  self->readNotification();
}

//  void QTcpServerPrivate::closeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate17closeNotificationEv(
    QTcpServerPrivate *self) {
  self->closeNotification();
}

//  void QTcpServerPrivate::writeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate17writeNotificationEv(
    QTcpServerPrivate *self) {
  self->writeNotification();
}

//  void QTcpServerPrivate::exceptionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate21exceptionNotificationEv(
    QTcpServerPrivate *self) {
  self->exceptionNotification();
}

//  void QTcpServerPrivate::connectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate22connectionNotificationEv(
    QTcpServerPrivate *self) {
  self->connectionNotification();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QTcpServerPrivate::proxyAuthenticationRequired(const QNetworkProxy
//      &a0, QAuthenticator *a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTcpServerPrivate27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QTcpServerPrivate *self,
    const QNetworkProxy *a0,
    QAuthenticator *a1) {
  self->proxyAuthenticationRequired(*a0, a1);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  QTcpServerPrivate as the QAbstractSocketEngineReceiver it is built on
extern "C" Q_DECL_EXPORT
QAbstractSocketEngineReceiver *ritual_cast_QTcpServerPrivate_QAbstractSocketEngineReceiver(
    QTcpServerPrivate *self) {
  return static_cast<QAbstractSocketEngineReceiver *>(self);
}

//  a Python function taken by a CuteQTcpServerPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTcpServerPrivate(
    QTcpServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTcpServerPrivate *>(self)->take(key, call);
}

//  void QTcpServerPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate22configureCreatedSocketEv(
    QTcpServerPrivate *self) {
  self->QTcpServerPrivate::configureCreatedSocket();
}

//  int QTcpServerPrivate::totalPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QTcpServerPrivate23totalPendingConnectionsEv(
    const QTcpServerPrivate *self) {
  return self->QTcpServerPrivate::totalPendingConnections();
}

//  void QTcpServerPrivate::readNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate16readNotificationEv(
    QTcpServerPrivate *self) {
  self->QTcpServerPrivate::readNotification();
}

//  void QTcpServerPrivate::closeNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate17closeNotificationEv(
    QTcpServerPrivate *self) {
  self->QTcpServerPrivate::closeNotification();
}

//  void QTcpServerPrivate::writeNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate17writeNotificationEv(
    QTcpServerPrivate *self) {
  self->QTcpServerPrivate::writeNotification();
}

//  void QTcpServerPrivate::exceptionNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate21exceptionNotificationEv(
    QTcpServerPrivate *self) {
  self->QTcpServerPrivate::exceptionNotification();
}

//  void QTcpServerPrivate::connectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate22connectionNotificationEv(
    QTcpServerPrivate *self) {
  self->QTcpServerPrivate::connectionNotification();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QTcpServerPrivate::proxyAuthenticationRequired(const QNetworkProxy
//      &a0, QAuthenticator *a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QTcpServerPrivate27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QTcpServerPrivate *self,
    const QNetworkProxy *a0,
    QAuthenticator *a1) {
  self->QTcpServerPrivate::proxyAuthenticationRequired(*a0, a1);
}
#endif  // !defined(QT_NO_NETWORKPROXY)
