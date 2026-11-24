//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttconnectionproperties.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMqtt/qmqttconnectionproperties.h>
#include <QtCore/qstring.h>

//  QMqttServerConnectionProperties::QMqttServerConnectionProperties()
extern "C" Q_DECL_EXPORT
QMqttServerConnectionProperties *ritual_ZN31QMqttServerConnectionPropertiesC1Ev() {
  return new QMqttServerConnectionProperties();
}

//  QMqttServerConnectionProperties::QMqttServerConnectionProperties(const
//      QMqttServerConnectionProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttServerConnectionProperties *ritual_ZN31QMqttServerConnectionPropertiesC1ERKS_(
    const QMqttServerConnectionProperties *a0) {
  return new QMqttServerConnectionProperties(*a0);
}

//  QMqttServerConnectionProperties::~QMqttServerConnectionProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QMqttServerConnectionPropertiesD1Ev(
    QMqttServerConnectionProperties *self) {
  delete self;
}

//  ServerPropertyDetails
//      QMqttServerConnectionProperties::availableProperties() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QMqttServerConnectionProperties19availablePropertiesEv(
    const QMqttServerConnectionProperties *self) {
  return static_cast<int>(self->availableProperties().toInt());
}

//  bool QMqttServerConnectionProperties::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QMqttServerConnectionProperties7isValidEv(
    const QMqttServerConnectionProperties *self) {
  return self->isValid();
}

//  quint8 QMqttServerConnectionProperties::maximumQoS() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK31QMqttServerConnectionProperties10maximumQoSEv(
    const QMqttServerConnectionProperties *self) {
  return self->maximumQoS();
}

//  bool QMqttServerConnectionProperties::retainAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QMqttServerConnectionProperties15retainAvailableEv(
    const QMqttServerConnectionProperties *self) {
  return self->retainAvailable();
}

//  bool QMqttServerConnectionProperties::clientIdAssigned() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QMqttServerConnectionProperties16clientIdAssignedEv(
    const QMqttServerConnectionProperties *self) {
  return self->clientIdAssigned();
}

//  QString QMqttServerConnectionProperties::reason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QMqttServerConnectionProperties6reasonEv(
    const QMqttServerConnectionProperties *self) {
  return new QString(self->reason());
}

//  QMqtt::ReasonCode QMqttServerConnectionProperties::reasonCode() const
extern "C" Q_DECL_EXPORT
QMqtt::ReasonCode ritual_ZNK31QMqttServerConnectionProperties10reasonCodeEv(
    const QMqttServerConnectionProperties *self) {
  return self->reasonCode();
}

//  bool QMqttServerConnectionProperties::wildcardSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QMqttServerConnectionProperties17wildcardSupportedEv(
    const QMqttServerConnectionProperties *self) {
  return self->wildcardSupported();
}

//  bool QMqttServerConnectionProperties::subscriptionIdentifierSupported()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QMqttServerConnectionProperties31subscriptionIdentifierSupportedEv(
    const QMqttServerConnectionProperties *self) {
  return self->subscriptionIdentifierSupported();
}

//  bool QMqttServerConnectionProperties::sharedSubscriptionSupported() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QMqttServerConnectionProperties27sharedSubscriptionSupportedEv(
    const QMqttServerConnectionProperties *self) {
  return self->sharedSubscriptionSupported();
}

//  quint16 QMqttServerConnectionProperties::serverKeepAlive() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK31QMqttServerConnectionProperties15serverKeepAliveEv(
    const QMqttServerConnectionProperties *self) {
  return self->serverKeepAlive();
}

//  QString QMqttServerConnectionProperties::responseInformation() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QMqttServerConnectionProperties19responseInformationEv(
    const QMqttServerConnectionProperties *self) {
  return new QString(self->responseInformation());
}

//  QString QMqttServerConnectionProperties::serverReference() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QMqttServerConnectionProperties15serverReferenceEv(
    const QMqttServerConnectionProperties *self) {
  return new QString(self->serverReference());
}
