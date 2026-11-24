//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qhttp2configuration.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtcpkeepaliveconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QHttpNetworkConnection that Python can take functions over in. Every QHttpNetworkConnection
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpNetworkConnectionCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHttpNetworkConnectionCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkConnectionCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkConnectionCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkConnectionCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkConnectionCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHttpNetworkConnectionCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHttpNetworkConnection : public QHttpNetworkConnection {
public:
  using QHttpNetworkConnection::QHttpNetworkConnection;
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
      CuteQHttpNetworkConnectionCall0 call = reinterpret_cast<CuteQHttpNetworkConnectionCall0>(taken[0]);
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
      CuteQHttpNetworkConnectionCall1 call = reinterpret_cast<CuteQHttpNetworkConnectionCall1>(taken[1]);
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
      CuteQHttpNetworkConnectionCall2 call = reinterpret_cast<CuteQHttpNetworkConnectionCall2>(taken[2]);
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
      CuteQHttpNetworkConnectionCall3 call = reinterpret_cast<CuteQHttpNetworkConnectionCall3>(taken[3]);
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
      CuteQHttpNetworkConnectionCall4 call = reinterpret_cast<CuteQHttpNetworkConnectionCall4>(taken[4]);
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
      CuteQHttpNetworkConnectionCall5 call = reinterpret_cast<CuteQHttpNetworkConnectionCall5>(taken[5]);
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
      CuteQHttpNetworkConnectionCall6 call = reinterpret_cast<CuteQHttpNetworkConnectionCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHttpNetworkConnection::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QHttpNetworkConnection10metaObjectEv(
    const QHttpNetworkConnection *self) {
  return self->metaObject();
}

//  QString QHttpNetworkConnection::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QHttpNetworkConnection2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHttpNetworkConnection::tr(s, c, n));
}

//  QHttpNetworkConnection::QHttpNetworkConnection(quint16 channelCount,
//      const QString &hostName, quint16 port, bool encrypt, bool
//      isLocalSocket, QObject *parent, ConnectionType connectionType)
extern "C" Q_DECL_EXPORT
QHttpNetworkConnection *ritual_ZN22QHttpNetworkConnectionC1EtRK7QStringtbbP7QObjectNS_14ConnectionTypeE(
    quint16 channelCount,
    const QString *hostName,
    quint16 port,
    bool encrypt,
    bool isLocalSocket,
    QObject *parent,
    QHttpNetworkConnection::ConnectionType connectionType) {
  return new CuteQHttpNetworkConnection(
      channelCount,
      *hostName,
      port,
      encrypt,
      isLocalSocket,
      parent,
      connectionType);
}

//  QHttpNetworkConnection::~QHttpNetworkConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnectionD1Ev(QHttpNetworkConnection *self) {
  delete self;
}

//  QString QHttpNetworkConnection::hostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHttpNetworkConnection8hostNameEv(
    const QHttpNetworkConnection *self) {
  return new QString(self->hostName());
}

//  quint16 QHttpNetworkConnection::port() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK22QHttpNetworkConnection4portEv(
    const QHttpNetworkConnection *self) {
  return self->port();
}

//  QHttpNetworkReply *QHttpNetworkConnection::sendRequest(const
//      QHttpNetworkRequest &request)
extern "C" Q_DECL_EXPORT
QHttpNetworkReply *ritual_ZN22QHttpNetworkConnection11sendRequestERK19QHttpNetworkRequest(
    QHttpNetworkConnection *self,
    const QHttpNetworkRequest *request) {
  return self->sendRequest(*request);
}

//  void QHttpNetworkConnection::fillHttp2Queue()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection14fillHttp2QueueEv(
    QHttpNetworkConnection *self) {
  self->fillHttp2Queue();
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpNetworkConnection::setCacheProxy(const QNetworkProxy
//      &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection13setCacheProxyERK13QNetworkProxy(
    QHttpNetworkConnection *self,
    const QNetworkProxy *networkProxy) {
  self->setCacheProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QHttpNetworkConnection::cacheProxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK22QHttpNetworkConnection10cacheProxyEv(
    const QHttpNetworkConnection *self) {
  return new QNetworkProxy(self->cacheProxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpNetworkConnection::setTransparentProxy(const QNetworkProxy
//      &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection19setTransparentProxyERK13QNetworkProxy(
    QHttpNetworkConnection *self,
    const QNetworkProxy *networkProxy) {
  self->setTransparentProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QHttpNetworkConnection::transparentProxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK22QHttpNetworkConnection16transparentProxyEv(
    const QHttpNetworkConnection *self) {
  return new QNetworkProxy(self->transparentProxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  bool QHttpNetworkConnection::isSsl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QHttpNetworkConnection5isSslEv(
    const QHttpNetworkConnection *self) {
  return self->isSsl();
}

//  QHttpNetworkConnectionChannel *QHttpNetworkConnection::channels() const
extern "C" Q_DECL_EXPORT
QHttpNetworkConnectionChannel *ritual_ZNK22QHttpNetworkConnection8channelsEv(
    const QHttpNetworkConnection *self) {
  return self->channels();
}

//  ConnectionType QHttpNetworkConnection::connectionType() const
extern "C" Q_DECL_EXPORT
QHttpNetworkConnection::ConnectionType ritual_ZNK22QHttpNetworkConnection14connectionTypeEv(
    const QHttpNetworkConnection *self) {
  return self->connectionType();
}

//  void QHttpNetworkConnection::setConnectionType(ConnectionType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection17setConnectionTypeENS_14ConnectionTypeE(
    QHttpNetworkConnection *self,
    QHttpNetworkConnection::ConnectionType type) {
  self->setConnectionType(type);
}

//  QHttp2Configuration QHttpNetworkConnection::http2Parameters() const
extern "C" Q_DECL_EXPORT
QHttp2Configuration *ritual_ZNK22QHttpNetworkConnection15http2ParametersEv(
    const QHttpNetworkConnection *self) {
  return new QHttp2Configuration(self->http2Parameters());
}

//  void QHttpNetworkConnection::setHttp2Parameters(const QHttp2Configuration
//      &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection18setHttp2ParametersERK19QHttp2Configuration(
    QHttpNetworkConnection *self,
    const QHttp2Configuration *params) {
  self->setHttp2Parameters(*params);
}

//  QTcpKeepAliveConfiguration
//      QHttpNetworkConnection::tcpKeepAliveParameters() const
extern "C" Q_DECL_EXPORT
QTcpKeepAliveConfiguration *ritual_ZNK22QHttpNetworkConnection22tcpKeepAliveParametersEv(
    const QHttpNetworkConnection *self) {
  return new QTcpKeepAliveConfiguration(self->tcpKeepAliveParameters());
}

//  void QHttpNetworkConnection::setTcpKeepAliveParameters(QTcpKeepAliveConfi
//      guration config)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection25setTcpKeepAliveParametersE26QTcpKeepAliveConfiguration(
    QHttpNetworkConnection *self,
    const QTcpKeepAliveConfiguration *config) {
  self->setTcpKeepAliveParameters(*config);
}

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnection::setSslConfiguration(const QSslConfiguration
//      &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection19setSslConfigurationERK17QSslConfiguration(
    QHttpNetworkConnection *self,
    const QSslConfiguration *config) {
  self->setSslConfiguration(*config);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnection::ignoreSslErrors(int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection15ignoreSslErrorsEi(
    QHttpNetworkConnection *self,
    int channel) {
  self->ignoreSslErrors(channel);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnection::ignoreSslErrors(const QList<QSslError>
//      &errors, int channel)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection15ignoreSslErrorsERK5QListI9QSslErrorEi(
    QHttpNetworkConnection *self,
    const QList<QSslError> *errors,
    int channel) {
  self->ignoreSslErrors(*errors, channel);
}
#endif  // !defined(QT_NO_SSL)

//  void QHttpNetworkConnection::preConnectFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection18preConnectFinishedEv(
    QHttpNetworkConnection *self) {
  self->preConnectFinished();
}

//  QString QHttpNetworkConnection::peerVerifyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QHttpNetworkConnection14peerVerifyNameEv(
    const QHttpNetworkConnection *self) {
  return new QString(self->peerVerifyName());
}

//  void QHttpNetworkConnection::setPeerVerifyName(const QString &peerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection17setPeerVerifyNameERK7QString(
    QHttpNetworkConnection *self,
    const QString *peerName) {
  self->setPeerVerifyName(*peerName);
}

//  void QHttpNetworkConnection::onlineStateChanged(bool isOnline)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QHttpNetworkConnection18onlineStateChangedEb(
    QHttpNetworkConnection *self,
    bool isOnline) {
  self->onlineStateChanged(isOnline);
}

//  QHttpNetworkConnectionPrivate *QHttpNetworkConnection::d_func()
extern "C" Q_DECL_EXPORT
QHttpNetworkConnectionPrivate *ritual_ZN22QHttpNetworkConnection6d_funcEv(
    QHttpNetworkConnection *self) {
  return self->d_func();
}

//  const QHttpNetworkConnectionPrivate *QHttpNetworkConnection::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QHttpNetworkConnectionPrivate *ritual_ZNK22QHttpNetworkConnection6d_funcEv(
    const QHttpNetworkConnection *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQHttpNetworkConnection, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpNetworkConnection(
    QHttpNetworkConnection *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpNetworkConnection *>(self)->take(key, call);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
