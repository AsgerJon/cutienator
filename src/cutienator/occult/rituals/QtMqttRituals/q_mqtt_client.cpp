//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttclient.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqttclient.h>
#include <QtCore/qstring.h>
#include <QtMqtt/qmqtttopicfilter.h>
#include <QtMqtt/qmqttsubscriptionproperties.h>
#include <QtMqtt/qmqtttopicname.h>
#include <QtCore/qbytearray.h>
#include <QtMqtt/qmqttpublishproperties.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtMqtt/qmqttconnectionproperties.h>
#include <QtMqtt/qmqttauthenticationproperties.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QMqttClient that Python can take functions over in. Every QMqttClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMqttClientCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMqttClientCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttClientCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttClientCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttClientCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMqttClientCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMqttClient : public QMqttClient {
public:
  using QMqttClient::QMqttClient;
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
      CuteQMqttClientCall0 call = reinterpret_cast<CuteQMqttClientCall0>(taken[0]);
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
      CuteQMqttClientCall1 call = reinterpret_cast<CuteQMqttClientCall1>(taken[1]);
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
      CuteQMqttClientCall2 call = reinterpret_cast<CuteQMqttClientCall2>(taken[2]);
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
      CuteQMqttClientCall3 call = reinterpret_cast<CuteQMqttClientCall3>(taken[3]);
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
      CuteQMqttClientCall4 call = reinterpret_cast<CuteQMqttClientCall4>(taken[4]);
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
      CuteQMqttClientCall5 call = reinterpret_cast<CuteQMqttClientCall5>(taken[5]);
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
      CuteQMqttClientCall6 call = reinterpret_cast<CuteQMqttClientCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMqttClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QMqttClient10metaObjectEv(
    const QMqttClient *self) {
  return self->metaObject();
}

//  QString QMqttClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QMqttClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMqttClient::tr(s, c, n));
}

//  QMqttClient::QMqttClient(QObject *parent)
extern "C" Q_DECL_EXPORT
QMqttClient *ritual_ZN11QMqttClientC1EP7QObject(QObject *parent) {
  return new CuteQMqttClient(parent);
}

//  QMqttClient::~QMqttClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClientD1Ev(QMqttClient *self) {
  delete self;
}

//  void QMqttClient::setTransport(QIODevice *device, TransportType
//      transport)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient12setTransportEP9QIODeviceNS_13TransportTypeE(
    QMqttClient *self,
    QIODevice *device,
    QMqttClient::TransportType transport) {
  self->setTransport(device, transport);
}

//  QIODevice *QMqttClient::transport() const
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZNK11QMqttClient9transportEv(const QMqttClient *self) {
  return self->transport();
}

//  QMqttSubscription *QMqttClient::subscribe(const QMqttTopicFilter &topic,
//      quint8 qos)
extern "C" Q_DECL_EXPORT
QMqttSubscription *ritual_ZN11QMqttClient9subscribeERK16QMqttTopicFilterh(
    QMqttClient *self,
    const QMqttTopicFilter *topic,
    quint8 qos) {
  return self->subscribe(*topic, qos);
}

//  QMqttSubscription *QMqttClient::subscribe(const QMqttTopicFilter &topic,
//      const QMqttSubscriptionProperties &properties, quint8 qos)
extern "C" Q_DECL_EXPORT
QMqttSubscription *ritual_ZN11QMqttClient9subscribeERK16QMqttTopicFilterRK27QMqttSubscriptionPropertiesh(
    QMqttClient *self,
    const QMqttTopicFilter *topic,
    const QMqttSubscriptionProperties *properties,
    quint8 qos) {
  return self->subscribe(*topic, *properties, qos);
}

//  void QMqttClient::unsubscribe(const QMqttTopicFilter &topic)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient11unsubscribeERK16QMqttTopicFilter(
    QMqttClient *self,
    const QMqttTopicFilter *topic) {
  self->unsubscribe(*topic);
}

//  void QMqttClient::unsubscribe(const QMqttTopicFilter &topic, const
//      QMqttUnsubscriptionProperties &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient11unsubscribeERK16QMqttTopicFilterRK29QMqttUnsubscriptionProperties(
    QMqttClient *self,
    const QMqttTopicFilter *topic,
    const QMqttUnsubscriptionProperties *properties) {
  self->unsubscribe(*topic, *properties);
}

//  qint32 QMqttClient::publish(const QMqttTopicName &topic, const QByteArray
//      &message, quint8 qos, bool retain)
extern "C" Q_DECL_EXPORT
qint32 ritual_ZN11QMqttClient7publishERK14QMqttTopicNameRK10QByteArrayhb(
    QMqttClient *self,
    const QMqttTopicName *topic,
    const QByteArray *message,
    quint8 qos,
    bool retain) {
  return self->publish(*topic, *message, qos, retain);
}

//  qint32 QMqttClient::publish(const QMqttTopicName &topic, const
//      QMqttPublishProperties &properties, const QByteArray &message, quint8
//      qos, bool retain)
extern "C" Q_DECL_EXPORT
qint32 ritual_ZN11QMqttClient7publishERK14QMqttTopicNameRK22QMqttPublishPropertiesRK10QByteArrayhb(
    QMqttClient *self,
    const QMqttTopicName *topic,
    const QMqttPublishProperties *properties,
    const QByteArray *message,
    quint8 qos,
    bool retain) {
  return self->publish(*topic, *properties, *message, qos, retain);
}

//  bool QMqttClient::requestPing()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QMqttClient11requestPingEv(QMqttClient *self) {
  return self->requestPing();
}

//  QString QMqttClient::hostname() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMqttClient8hostnameEv(const QMqttClient *self) {
  return new QString(self->hostname());
}

//  quint16 QMqttClient::port() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK11QMqttClient4portEv(const QMqttClient *self) {
  return self->port();
}

//  QString QMqttClient::clientId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMqttClient8clientIdEv(const QMqttClient *self) {
  return new QString(self->clientId());
}

//  quint16 QMqttClient::keepAlive() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK11QMqttClient9keepAliveEv(const QMqttClient *self) {
  return self->keepAlive();
}

//  ProtocolVersion QMqttClient::protocolVersion() const
extern "C" Q_DECL_EXPORT
QMqttClient::ProtocolVersion ritual_ZNK11QMqttClient15protocolVersionEv(
    const QMqttClient *self) {
  return self->protocolVersion();
}

//  void QMqttClient::connectToHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient13connectToHostEv(QMqttClient *self) {
  self->connectToHost();
}

#if !defined(QT_NO_SSL)
//  void QMqttClient::connectToHostEncrypted(const QSslConfiguration &conf)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient22connectToHostEncryptedERK17QSslConfiguration(
    QMqttClient *self,
    const QSslConfiguration *conf) {
  self->connectToHostEncrypted(*conf);
}
#endif  // !defined(QT_NO_SSL)

//  void QMqttClient::connectToHostWebSocket(QWebSocket *webSocket)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient22connectToHostWebSocketEP10QWebSocket(
    QMqttClient *self,
    QWebSocket *webSocket) {
  self->connectToHostWebSocket(webSocket);
}

//  void QMqttClient::connectToHostWebSocketEncrypted(QWebSocket *webSocket)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient31connectToHostWebSocketEncryptedEP10QWebSocket(
    QMqttClient *self,
    QWebSocket *webSocket) {
  self->connectToHostWebSocketEncrypted(webSocket);
}

//  void QMqttClient::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient18disconnectFromHostEv(QMqttClient *self) {
  self->disconnectFromHost();
}

//  ClientState QMqttClient::state() const
extern "C" Q_DECL_EXPORT
QMqttClient::ClientState ritual_ZNK11QMqttClient5stateEv(
    const QMqttClient *self) {
  return self->state();
}

//  ClientError QMqttClient::error() const
extern "C" Q_DECL_EXPORT
QMqttClient::ClientError ritual_ZNK11QMqttClient5errorEv(
    const QMqttClient *self) {
  return self->error();
}

//  QString QMqttClient::username() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMqttClient8usernameEv(const QMqttClient *self) {
  return new QString(self->username());
}

//  QString QMqttClient::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMqttClient8passwordEv(const QMqttClient *self) {
  return new QString(self->password());
}

//  bool QMqttClient::cleanSession() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMqttClient12cleanSessionEv(const QMqttClient *self) {
  return self->cleanSession();
}

//  QString QMqttClient::willTopic() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QMqttClient9willTopicEv(const QMqttClient *self) {
  return new QString(self->willTopic());
}

//  quint8 QMqttClient::willQoS() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK11QMqttClient7willQoSEv(const QMqttClient *self) {
  return self->willQoS();
}

//  QByteArray QMqttClient::willMessage() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QMqttClient11willMessageEv(const QMqttClient *self) {
  return new QByteArray(self->willMessage());
}

//  bool QMqttClient::willRetain() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMqttClient10willRetainEv(const QMqttClient *self) {
  return self->willRetain();
}

//  bool QMqttClient::autoKeepAlive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QMqttClient13autoKeepAliveEv(const QMqttClient *self) {
  return self->autoKeepAlive();
}

//  void QMqttClient::setConnectionProperties(const QMqttConnectionProperties
//      &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient23setConnectionPropertiesERK25QMqttConnectionProperties(
    QMqttClient *self,
    const QMqttConnectionProperties *prop) {
  self->setConnectionProperties(*prop);
}

//  QMqttConnectionProperties QMqttClient::connectionProperties() const
extern "C" Q_DECL_EXPORT
QMqttConnectionProperties *ritual_ZNK11QMqttClient20connectionPropertiesEv(
    const QMqttClient *self) {
  return new QMqttConnectionProperties(self->connectionProperties());
}

//  void QMqttClient::setLastWillProperties(const QMqttLastWillProperties
//      &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient21setLastWillPropertiesERK23QMqttLastWillProperties(
    QMqttClient *self,
    const QMqttLastWillProperties *prop) {
  self->setLastWillProperties(*prop);
}

//  QMqttLastWillProperties QMqttClient::lastWillProperties() const
extern "C" Q_DECL_EXPORT
QMqttLastWillProperties *ritual_ZNK11QMqttClient18lastWillPropertiesEv(
    const QMqttClient *self) {
  return new QMqttLastWillProperties(self->lastWillProperties());
}

//  QMqttServerConnectionProperties QMqttClient::serverConnectionProperties()
//      const
extern "C" Q_DECL_EXPORT
QMqttServerConnectionProperties *ritual_ZNK11QMqttClient26serverConnectionPropertiesEv(
    const QMqttClient *self) {
  return new QMqttServerConnectionProperties(
      self->serverConnectionProperties());
}

//  void QMqttClient::authenticate(const QMqttAuthenticationProperties &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient12authenticateERK29QMqttAuthenticationProperties(
    QMqttClient *self,
    const QMqttAuthenticationProperties *prop) {
  self->authenticate(*prop);
}

//  void QMqttClient::setHostname(const QString &hostname)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient11setHostnameERK7QString(
    QMqttClient *self,
    const QString *hostname) {
  self->setHostname(*hostname);
}

//  void QMqttClient::setPort(quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient7setPortEt(QMqttClient *self, quint16 port) {
  self->setPort(port);
}

//  void QMqttClient::setClientId(const QString &clientId)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient11setClientIdERK7QString(
    QMqttClient *self,
    const QString *clientId) {
  self->setClientId(*clientId);
}

//  void QMqttClient::setKeepAlive(quint16 keepAlive)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient12setKeepAliveEt(
    QMqttClient *self,
    quint16 keepAlive) {
  self->setKeepAlive(keepAlive);
}

//  void QMqttClient::setProtocolVersion(ProtocolVersion protocolVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient18setProtocolVersionENS_15ProtocolVersionE(
    QMqttClient *self,
    QMqttClient::ProtocolVersion protocolVersion) {
  self->setProtocolVersion(protocolVersion);
}

//  void QMqttClient::setState(ClientState state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient8setStateENS_11ClientStateE(
    QMqttClient *self,
    QMqttClient::ClientState state) {
  self->setState(state);
}

//  void QMqttClient::setError(ClientError error)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient8setErrorENS_11ClientErrorE(
    QMqttClient *self,
    QMqttClient::ClientError error) {
  self->setError(error);
}

//  void QMqttClient::setUsername(const QString &username)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient11setUsernameERK7QString(
    QMqttClient *self,
    const QString *username) {
  self->setUsername(*username);
}

//  void QMqttClient::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient11setPasswordERK7QString(
    QMqttClient *self,
    const QString *password) {
  self->setPassword(*password);
}

//  void QMqttClient::setCleanSession(bool cleanSession)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient15setCleanSessionEb(
    QMqttClient *self,
    bool cleanSession) {
  self->setCleanSession(cleanSession);
}

//  void QMqttClient::setWillTopic(const QString &willTopic)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient12setWillTopicERK7QString(
    QMqttClient *self,
    const QString *willTopic) {
  self->setWillTopic(*willTopic);
}

//  void QMqttClient::setWillQoS(quint8 willQoS)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient10setWillQoSEh(
    QMqttClient *self,
    quint8 willQoS) {
  self->setWillQoS(willQoS);
}

//  void QMqttClient::setWillMessage(const QByteArray &willMessage)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient14setWillMessageERK10QByteArray(
    QMqttClient *self,
    const QByteArray *willMessage) {
  self->setWillMessage(*willMessage);
}

//  void QMqttClient::setWillRetain(bool willRetain)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient13setWillRetainEb(
    QMqttClient *self,
    bool willRetain) {
  self->setWillRetain(willRetain);
}

//  void QMqttClient::setAutoKeepAlive(bool autoKeepAlive)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient16setAutoKeepAliveEb(
    QMqttClient *self,
    bool autoKeepAlive) {
  self->setAutoKeepAlive(autoKeepAlive);
}

//  void QMqttClient::connectToHost(bool encrypted, const QString
//      &sslPeerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QMqttClient13connectToHostEbRK7QString(
    QMqttClient *self,
    bool encrypted,
    const QString *sslPeerName) {
  self->connectToHost(encrypted, *sslPeerName);
}

//  QMqttClientPrivate *QMqttClient::d_func()
extern "C" Q_DECL_EXPORT
QMqttClientPrivate *ritual_ZN11QMqttClient6d_funcEv(QMqttClient *self) {
  return self->d_func();
}

//  const QMqttClientPrivate *QMqttClient::d_func() const
extern "C" Q_DECL_EXPORT
const QMqttClientPrivate *ritual_ZNK11QMqttClient6d_funcEv(
    const QMqttClient *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQMqttClient, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMqttClient(
    QMqttClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMqttClient *>(self)->take(key, call);
}
