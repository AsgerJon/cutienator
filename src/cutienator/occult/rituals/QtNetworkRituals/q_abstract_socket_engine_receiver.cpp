//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qabstractsocketenginereceiver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qabstractsocketenginereceiver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <cstring>

//  A QAbstractSocketEngineReceiver that Python can take functions over in. Every QAbstractSocketEngineReceiver
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractSocketEngineReceiverCall0)(const void *, int *);
typedef void (*CuteQAbstractSocketEngineReceiverCall1)(const void *, int *);
typedef void (*CuteQAbstractSocketEngineReceiverCall2)(const void *, int *);
typedef void (*CuteQAbstractSocketEngineReceiverCall3)(const void *, int *);
typedef void (*CuteQAbstractSocketEngineReceiverCall4)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQAbstractSocketEngineReceiverCall5)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
class CuteQAbstractSocketEngineReceiver : public QAbstractSocketEngineReceiver {
public:
  using QAbstractSocketEngineReceiver::QAbstractSocketEngineReceiver;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver16readNotificationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17writeNotificationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17closeNotificationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver22connectionNotificationEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
    return false;
  }

  //  void QAbstractSocketEngineReceiver::readNotification()
  void readNotification() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSocketEngineReceiverCall0 call = reinterpret_cast<CuteQAbstractSocketEngineReceiverCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSocketEngineReceiver::writeNotification()
  void writeNotification() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSocketEngineReceiverCall1 call = reinterpret_cast<CuteQAbstractSocketEngineReceiverCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSocketEngineReceiver::closeNotification()
  void closeNotification() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSocketEngineReceiverCall2 call = reinterpret_cast<CuteQAbstractSocketEngineReceiverCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSocketEngineReceiver::exceptionNotification()
  void exceptionNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSocketEngineReceiverCall3 call = reinterpret_cast<CuteQAbstractSocketEngineReceiverCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractSocketEngineReceiver::connectionNotification()
  void connectionNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSocketEngineReceiverCall4 call = reinterpret_cast<CuteQAbstractSocketEngineReceiverCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_NETWORKPROXY)
  //  void QAbstractSocketEngineReceiver::proxyAuthenticationRequired(const
  //      QNetworkProxy &proxy, QAuthenticator *authenticator)
  void proxyAuthenticationRequired(
      const QNetworkProxy &proxy,
      QAuthenticator *authenticator) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSocketEngineReceiverCall5 call = reinterpret_cast<CuteQAbstractSocketEngineReceiverCall5>(taken[5]);
      call(this, &proxy, authenticator, &handled);
      if (handled) return;
    }
  }
#endif  // !defined(QT_NO_NETWORKPROXY)
};

//  QAbstractSocketEngineReceiver::~QAbstractSocketEngineReceiver()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiverD1Ev(
    QAbstractSocketEngineReceiver *self) {
  delete self;
}

//  void QAbstractSocketEngineReceiver::readNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiver16readNotificationEv(
    QAbstractSocketEngineReceiver *self) {
  self->readNotification();
}

//  void QAbstractSocketEngineReceiver::writeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiver17writeNotificationEv(
    QAbstractSocketEngineReceiver *self) {
  self->writeNotification();
}

//  void QAbstractSocketEngineReceiver::closeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiver17closeNotificationEv(
    QAbstractSocketEngineReceiver *self) {
  self->closeNotification();
}

//  void QAbstractSocketEngineReceiver::exceptionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv(
    QAbstractSocketEngineReceiver *self) {
  self->exceptionNotification();
}

//  void QAbstractSocketEngineReceiver::connectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiver22connectionNotificationEv(
    QAbstractSocketEngineReceiver *self) {
  self->connectionNotification();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocketEngineReceiver::proxyAuthenticationRequired(const
//      QNetworkProxy &proxy, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QAbstractSocketEngineReceiver27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QAbstractSocketEngineReceiver *self,
    const QNetworkProxy *proxy,
    QAuthenticator *authenticator) {
  self->proxyAuthenticationRequired(*proxy, authenticator);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  a Python function taken by a CuteQAbstractSocketEngineReceiver, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSocketEngineReceiver(
    QAbstractSocketEngineReceiver *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSocketEngineReceiver *>(self)->take(key, call);
}
