//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttconnectionproperties.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMqtt/qmqttconnectionproperties.h>
#include <QtMqtt/qmqtttype.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QMqttConnectionProperties::QMqttConnectionProperties()
extern "C" Q_DECL_EXPORT
QMqttConnectionProperties *ritual_ZN25QMqttConnectionPropertiesC1Ev() {
  return new QMqttConnectionProperties();
}

//  QMqttConnectionProperties::QMqttConnectionProperties(const
//      QMqttConnectionProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttConnectionProperties *ritual_ZN25QMqttConnectionPropertiesC1ERKS_(
    const QMqttConnectionProperties *a0) {
  return new QMqttConnectionProperties(*a0);
}

//  QMqttConnectionProperties::~QMqttConnectionProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionPropertiesD1Ev(
    QMqttConnectionProperties *self) {
  delete self;
}

//  quint32 QMqttConnectionProperties::sessionExpiryInterval() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK25QMqttConnectionProperties21sessionExpiryIntervalEv(
    const QMqttConnectionProperties *self) {
  return self->sessionExpiryInterval();
}

//  quint16 QMqttConnectionProperties::maximumReceive() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK25QMqttConnectionProperties14maximumReceiveEv(
    const QMqttConnectionProperties *self) {
  return self->maximumReceive();
}

//  quint32 QMqttConnectionProperties::maximumPacketSize() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK25QMqttConnectionProperties17maximumPacketSizeEv(
    const QMqttConnectionProperties *self) {
  return self->maximumPacketSize();
}

//  quint16 QMqttConnectionProperties::maximumTopicAlias() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK25QMqttConnectionProperties17maximumTopicAliasEv(
    const QMqttConnectionProperties *self) {
  return self->maximumTopicAlias();
}

//  bool QMqttConnectionProperties::requestResponseInformation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QMqttConnectionProperties26requestResponseInformationEv(
    const QMqttConnectionProperties *self) {
  return self->requestResponseInformation();
}

//  bool QMqttConnectionProperties::requestProblemInformation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QMqttConnectionProperties25requestProblemInformationEv(
    const QMqttConnectionProperties *self) {
  return self->requestProblemInformation();
}

//  QMqttUserProperties QMqttConnectionProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK25QMqttConnectionProperties14userPropertiesEv(
    const QMqttConnectionProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  QString QMqttConnectionProperties::authenticationMethod() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QMqttConnectionProperties20authenticationMethodEv(
    const QMqttConnectionProperties *self) {
  return new QString(self->authenticationMethod());
}

//  QByteArray QMqttConnectionProperties::authenticationData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QMqttConnectionProperties18authenticationDataEv(
    const QMqttConnectionProperties *self) {
  return new QByteArray(self->authenticationData());
}

//  void QMqttConnectionProperties::setSessionExpiryInterval(quint32 expiry)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties24setSessionExpiryIntervalEj(
    QMqttConnectionProperties *self,
    quint32 expiry) {
  self->setSessionExpiryInterval(expiry);
}

//  void QMqttConnectionProperties::setMaximumReceive(quint16 maximumReceive)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties17setMaximumReceiveEt(
    QMqttConnectionProperties *self,
    quint16 maximumReceive) {
  self->setMaximumReceive(maximumReceive);
}

//  void QMqttConnectionProperties::setMaximumPacketSize(quint32 packetSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties20setMaximumPacketSizeEj(
    QMqttConnectionProperties *self,
    quint32 packetSize) {
  self->setMaximumPacketSize(packetSize);
}

//  void QMqttConnectionProperties::setMaximumTopicAlias(quint16 alias)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties20setMaximumTopicAliasEt(
    QMqttConnectionProperties *self,
    quint16 alias) {
  self->setMaximumTopicAlias(alias);
}

//  void QMqttConnectionProperties::setRequestResponseInformation(bool
//      response)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties29setRequestResponseInformationEb(
    QMqttConnectionProperties *self,
    bool response) {
  self->setRequestResponseInformation(response);
}

//  void QMqttConnectionProperties::setRequestProblemInformation(bool
//      problem)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties28setRequestProblemInformationEb(
    QMqttConnectionProperties *self,
    bool problem) {
  self->setRequestProblemInformation(problem);
}

//  void QMqttConnectionProperties::setUserProperties(const
//      QMqttUserProperties &properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties17setUserPropertiesERK19QMqttUserProperties(
    QMqttConnectionProperties *self,
    const QMqttUserProperties *properties) {
  self->setUserProperties(*properties);
}

//  void QMqttConnectionProperties::setAuthenticationMethod(const QString
//      &authMethod)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties23setAuthenticationMethodERK7QString(
    QMqttConnectionProperties *self,
    const QString *authMethod) {
  self->setAuthenticationMethod(*authMethod);
}

//  void QMqttConnectionProperties::setAuthenticationData(const QByteArray
//      &authData)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QMqttConnectionProperties21setAuthenticationDataERK10QByteArray(
    QMqttConnectionProperties *self,
    const QByteArray *authData) {
  self->setAuthenticationData(*authData);
}
