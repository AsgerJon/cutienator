//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qabstractsocket_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qabstractsocket.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qabstractsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qhostinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QAbstractSocketPrivate that Python can take functions over in. Every QAbstractSocketPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractSocketPrivateCall0)(const void *, int *);
typedef void (*CuteQAbstractSocketPrivateCall1)(const void *, int *);
typedef void (*CuteQAbstractSocketPrivateCall2)(const void *, int *);
typedef void (*CuteQAbstractSocketPrivateCall3)(const void *, int *);
typedef void (*CuteQAbstractSocketPrivateCall4)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQAbstractSocketPrivateCall5)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQAbstractSocketPrivateCall6)(const void *, const QHostAddress *, quint16, int, const QNetworkInterface *, int *);
typedef bool (*CuteQAbstractSocketPrivateCall7)(const void *, int *);
typedef bool (*CuteQAbstractSocketPrivateCall8)(const void *, int *);
typedef void (*CuteQAbstractSocketPrivateCall9)(const void *, int *);
typedef bool (*CuteQAbstractSocketPrivateCall10)(const void *, int *);
typedef bool (*CuteQAbstractSocketPrivateCall11)(const void *, char, int *);
typedef const QByteArray * (*CuteQAbstractSocketPrivateCall12)(const void *, qint64, int *);
class CuteQAbstractSocketPrivate : public QAbstractSocketPrivate {
public:
  using QAbstractSocketPrivate::QAbstractSocketPrivate;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver16readNotificationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17writeNotificationEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17closeNotificationEv")) {
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
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate19canReadNotificationEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate5flushEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate22configureCreatedSocketEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate13writeToSocketEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  void QAbstractSocketPrivate::readNotification()
  void readNotification() override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall0 call = reinterpret_cast<CuteQAbstractSocketPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::readNotification();
  }

  //  void QAbstractSocketPrivate::writeNotification()
  void writeNotification() override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall1 call = reinterpret_cast<CuteQAbstractSocketPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::writeNotification();
  }

  //  void QAbstractSocketPrivate::exceptionNotification()
  void exceptionNotification() override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall2 call = reinterpret_cast<CuteQAbstractSocketPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::exceptionNotification();
  }

  //  void QAbstractSocketPrivate::closeNotification()
  void closeNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall3 call = reinterpret_cast<CuteQAbstractSocketPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::closeNotification();
  }

  //  void QAbstractSocketPrivate::connectionNotification()
  void connectionNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall4 call = reinterpret_cast<CuteQAbstractSocketPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::connectionNotification();
  }

#if !defined(QT_NO_NETWORKPROXY)
  //  void QAbstractSocketPrivate::proxyAuthenticationRequired(const
  //      QNetworkProxy &proxy, QAuthenticator *authenticator)
  void proxyAuthenticationRequired(
      const QNetworkProxy &proxy,
      QAuthenticator *authenticator) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall5 call = reinterpret_cast<CuteQAbstractSocketPrivateCall5>(taken[5]);
      call(this, &proxy, authenticator, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::proxyAuthenticationRequired(proxy, authenticator);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)

  //  bool QAbstractSocketPrivate::bind(const QHostAddress &address,
  //      quint16 port, QAbstractSocket::BindMode mode, const
  //      QNetworkInterface *iface)
  bool bind(
      const QHostAddress &address,
      quint16 port,
      QAbstractSocket::BindMode mode,
      const QNetworkInterface *iface) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall6 call = reinterpret_cast<CuteQAbstractSocketPrivateCall6>(taken[6]);
      bool given = call(this, &address, port, static_cast<int>(mode.toInt()), iface, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::bind(address, port, mode, iface);
  }

  //  bool QAbstractSocketPrivate::canReadNotification()
  bool canReadNotification() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall7 call = reinterpret_cast<CuteQAbstractSocketPrivateCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::canReadNotification();
  }

  //  bool QAbstractSocketPrivate::flush()
  bool flush() override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall8 call = reinterpret_cast<CuteQAbstractSocketPrivateCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::flush();
  }

  //  void QAbstractSocketPrivate::configureCreatedSocket()
  void configureCreatedSocket() override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall9 call = reinterpret_cast<CuteQAbstractSocketPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::configureCreatedSocket();
  }

  //  bool QAbstractSocketPrivate::writeToSocket()
  bool writeToSocket() override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall10 call = reinterpret_cast<CuteQAbstractSocketPrivateCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::writeToSocket();
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall11 call = reinterpret_cast<CuteQAbstractSocketPrivateCall11>(taken[11]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractSocketPrivateCall12 call = reinterpret_cast<CuteQAbstractSocketPrivateCall12>(taken[12]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QAbstractSocket *QAbstractSocketPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractSocket *ritual_ZN22QAbstractSocketPrivate6q_funcEv(
    QAbstractSocketPrivate *self) {
  return self->q_func();
}

//  const QAbstractSocket *QAbstractSocketPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSocket *ritual_ZNK22QAbstractSocketPrivate6q_funcEv(
    const QAbstractSocketPrivate *self) {
  return self->q_func();
}

//  QAbstractSocketPrivate::QAbstractSocketPrivate(decltype(QObjectPrivateVer
//      sion) version)
extern "C" Q_DECL_EXPORT
QAbstractSocketPrivate *ritual_ZN22QAbstractSocketPrivateC1E16QtPrivate_6_12_0(
    decltype(QObjectPrivateVersion) version) {
  return new CuteQAbstractSocketPrivate(version);
}

//  QAbstractSocketPrivate::~QAbstractSocketPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivateD1Ev(QAbstractSocketPrivate *self) {
  delete self;
}

//  void QAbstractSocketPrivate::readNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate16readNotificationEv(
    QAbstractSocketPrivate *self) {
  self->readNotification();
}

//  void QAbstractSocketPrivate::writeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate17writeNotificationEv(
    QAbstractSocketPrivate *self) {
  self->writeNotification();
}

//  void QAbstractSocketPrivate::exceptionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate21exceptionNotificationEv(
    QAbstractSocketPrivate *self) {
  self->exceptionNotification();
}

//  void QAbstractSocketPrivate::closeNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate17closeNotificationEv(
    QAbstractSocketPrivate *self) {
  self->closeNotification();
}

//  void QAbstractSocketPrivate::connectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate22connectionNotificationEv(
    QAbstractSocketPrivate *self) {
  self->connectionNotification();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocketPrivate::proxyAuthenticationRequired(const
//      QNetworkProxy &proxy, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QAbstractSocketPrivate *self,
    const QNetworkProxy *proxy,
    QAuthenticator *authenticator) {
  self->proxyAuthenticationRequired(*proxy, authenticator);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  bool QAbstractSocketPrivate::bind(const QHostAddress &address, quint16
//      port, QAbstractSocket::BindMode mode, const QNetworkInterface *iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface(
    QAbstractSocketPrivate *self,
    const QHostAddress *address,
    quint16 port,
    int mode,
    const QNetworkInterface *iface) {
  return self->bind(
      *address,
      port,
      QFlags<QAbstractSocket::BindFlag>::fromInt(mode),
      iface);
}

//  bool QAbstractSocketPrivate::canReadNotification()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate19canReadNotificationEv(
    QAbstractSocketPrivate *self) {
  return self->canReadNotification();
}

//  bool QAbstractSocketPrivate::canWriteNotification()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate20canWriteNotificationEv(
    QAbstractSocketPrivate *self) {
  return self->canWriteNotification();
}

//  void QAbstractSocketPrivate::canCloseNotification()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate20canCloseNotificationEv(
    QAbstractSocketPrivate *self) {
  self->canCloseNotification();
}

//  void QAbstractSocketPrivate::_q_connectToNextAddress()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate23_q_connectToNextAddressEv(
    QAbstractSocketPrivate *self) {
  self->_q_connectToNextAddress();
}

//  void QAbstractSocketPrivate::_q_startConnecting(const QHostInfo
//      &hostInfo)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate18_q_startConnectingERK9QHostInfo(
    QAbstractSocketPrivate *self,
    const QHostInfo *hostInfo) {
  self->_q_startConnecting(*hostInfo);
}

//  void QAbstractSocketPrivate::_q_testConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate17_q_testConnectionEv(
    QAbstractSocketPrivate *self) {
  self->_q_testConnection();
}

//  void QAbstractSocketPrivate::_q_abortConnectionAttempt()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate25_q_abortConnectionAttemptEv(
    QAbstractSocketPrivate *self) {
  self->_q_abortConnectionAttempt();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocketPrivate::resolveProxy(const QString &hostName,
//      quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate12resolveProxyERK7QStringt(
    QAbstractSocketPrivate *self,
    const QString *hostName,
    quint16 port) {
  self->resolveProxy(*hostName, port);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QAbstractSocketPrivate::resolveProxy(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate12resolveProxyEt(
    QAbstractSocketPrivate *self,
    quint16 port) {
  self->resolveProxy(port);
}

//  void QAbstractSocketPrivate::resetSocketLayer()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate16resetSocketLayerEv(
    QAbstractSocketPrivate *self) {
  self->resetSocketLayer();
}

//  bool QAbstractSocketPrivate::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate5flushEv(
    QAbstractSocketPrivate *self) {
  return self->flush();
}

//  bool QAbstractSocketPrivate::initSocketLayer(QAbstractSocket::NetworkLaye
//      rProtocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate15initSocketLayerEN15QAbstractSocket20NetworkLayerProtocolE(
    QAbstractSocketPrivate *self,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  return self->initSocketLayer(protocol);
}

//  void QAbstractSocketPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate22configureCreatedSocketEv(
    QAbstractSocketPrivate *self) {
  self->configureCreatedSocket();
}

//  void QAbstractSocketPrivate::startConnectingByName(const QString &host)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate21startConnectingByNameERK7QString(
    QAbstractSocketPrivate *self,
    const QString *host) {
  self->startConnectingByName(*host);
}

//  void QAbstractSocketPrivate::fetchConnectionParameters()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate25fetchConnectionParametersEv(
    QAbstractSocketPrivate *self) {
  self->fetchConnectionParameters();
}

//  bool QAbstractSocketPrivate::readFromSocket()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate14readFromSocketEv(
    QAbstractSocketPrivate *self) {
  return self->readFromSocket();
}

//  bool QAbstractSocketPrivate::writeToSocket()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractSocketPrivate13writeToSocketEv(
    QAbstractSocketPrivate *self) {
  return self->writeToSocket();
}

//  void QAbstractSocketPrivate::emitReadyRead(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate13emitReadyReadEi(
    QAbstractSocketPrivate *self,
    int channel) {
  self->emitReadyRead(channel);
}

//  void QAbstractSocketPrivate::emitBytesWritten(qint64 bytes, int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate16emitBytesWrittenExi(
    QAbstractSocketPrivate *self,
    qint64 bytes,
    int channel) {
  self->emitBytesWritten(bytes, channel);
}

//  void QAbstractSocketPrivate::setError(QAbstractSocket::SocketError
//      errorCode, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate8setErrorEN15QAbstractSocket11SocketErrorERK7QString(
    QAbstractSocketPrivate *self,
    QAbstractSocket::SocketError errorCode,
    const QString *errorString) {
  self->setError(errorCode, *errorString);
}

//  void QAbstractSocketPrivate::setErrorAndEmit(QAbstractSocket::SocketError
//      errorCode, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate15setErrorAndEmitEN15QAbstractSocket11SocketErrorERK7QString(
    QAbstractSocketPrivate *self,
    QAbstractSocket::SocketError errorCode,
    const QString *errorString) {
  self->setErrorAndEmit(errorCode, *errorString);
}

//  void QAbstractSocketPrivate::pauseSocketNotifiers(QAbstractSocket *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate20pauseSocketNotifiersEP15QAbstractSocket(
    QAbstractSocket *a0) {
  QAbstractSocketPrivate::pauseSocketNotifiers(a0);
}

//  void QAbstractSocketPrivate::resumeSocketNotifiers(QAbstractSocket *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractSocketPrivate21resumeSocketNotifiersEP15QAbstractSocket(
    QAbstractSocket *a0) {
  QAbstractSocketPrivate::resumeSocketNotifiers(a0);
}

//  QAbstractSocketEngine
//      *QAbstractSocketPrivate::getSocketEngine(QAbstractSocket *a0)
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN22QAbstractSocketPrivate15getSocketEngineEP15QAbstractSocket(
    QAbstractSocket *a0) {
  return QAbstractSocketPrivate::getSocketEngine(a0);
}

//  QAbstractSocketPrivate as the QAbstractSocketEngineReceiver it is built
//      on
extern "C" Q_DECL_EXPORT
QAbstractSocketEngineReceiver *ritual_cast_QAbstractSocketPrivate_QAbstractSocketEngineReceiver(
    QAbstractSocketPrivate *self) {
  return static_cast<QAbstractSocketEngineReceiver *>(self);
}

//  a Python function taken by a CuteQAbstractSocketPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractSocketPrivate(
    QAbstractSocketPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractSocketPrivate *>(self)->take(key, call);
}

//  void QAbstractSocketPrivate::readNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate16readNotificationEv(
    QAbstractSocketPrivate *self) {
  self->QAbstractSocketPrivate::readNotification();
}

//  void QAbstractSocketPrivate::writeNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate17writeNotificationEv(
    QAbstractSocketPrivate *self) {
  self->QAbstractSocketPrivate::writeNotification();
}

//  void QAbstractSocketPrivate::exceptionNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate21exceptionNotificationEv(
    QAbstractSocketPrivate *self) {
  self->QAbstractSocketPrivate::exceptionNotification();
}

//  void QAbstractSocketPrivate::closeNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate17closeNotificationEv(
    QAbstractSocketPrivate *self) {
  self->QAbstractSocketPrivate::closeNotification();
}

//  void QAbstractSocketPrivate::connectionNotification()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate22connectionNotificationEv(
    QAbstractSocketPrivate *self) {
  self->QAbstractSocketPrivate::connectionNotification();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QAbstractSocketPrivate::proxyAuthenticationRequired(const
//      QNetworkProxy &proxy, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator(
    QAbstractSocketPrivate *self,
    const QNetworkProxy *proxy,
    QAuthenticator *authenticator) {
  self->QAbstractSocketPrivate::proxyAuthenticationRequired(
      *proxy,
      authenticator);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  bool QAbstractSocketPrivate::bind(const QHostAddress &address, quint16
//      port, QAbstractSocket::BindMode mode, const QNetworkInterface *iface)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface(
    QAbstractSocketPrivate *self,
    const QHostAddress *address,
    quint16 port,
    int mode,
    const QNetworkInterface *iface) {
  return self->QAbstractSocketPrivate::bind(
      *address,
      port,
      QFlags<QAbstractSocket::BindFlag>::fromInt(mode),
      iface);
}

//  bool QAbstractSocketPrivate::canReadNotification()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QAbstractSocketPrivate19canReadNotificationEv(
    QAbstractSocketPrivate *self) {
  return self->QAbstractSocketPrivate::canReadNotification();
}

//  bool QAbstractSocketPrivate::flush()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QAbstractSocketPrivate5flushEv(
    QAbstractSocketPrivate *self) {
  return self->QAbstractSocketPrivate::flush();
}

//  void QAbstractSocketPrivate::configureCreatedSocket()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QAbstractSocketPrivate22configureCreatedSocketEv(
    QAbstractSocketPrivate *self) {
  self->QAbstractSocketPrivate::configureCreatedSocket();
}

//  bool QAbstractSocketPrivate::writeToSocket()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QAbstractSocketPrivate13writeToSocketEv(
    QAbstractSocketPrivate *self) {
  return self->QAbstractSocketPrivate::writeToSocket();
}
