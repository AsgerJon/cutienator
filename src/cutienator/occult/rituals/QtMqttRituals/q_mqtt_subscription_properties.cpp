//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttsubscriptionproperties.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMqtt/qmqttsubscriptionproperties.h>
#include <QtMqtt/qmqtttype.h>

//  QMqttSubscriptionProperties::QMqttSubscriptionProperties()
extern "C" Q_DECL_EXPORT
QMqttSubscriptionProperties *ritual_ZN27QMqttSubscriptionPropertiesC1Ev() {
  return new QMqttSubscriptionProperties();
}

//  QMqttSubscriptionProperties::QMqttSubscriptionProperties(const
//      QMqttSubscriptionProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttSubscriptionProperties *ritual_ZN27QMqttSubscriptionPropertiesC1ERKS_(
    const QMqttSubscriptionProperties *a0) {
  return new QMqttSubscriptionProperties(*a0);
}

//  QMqttSubscriptionProperties &QMqttSubscriptionProperties::operator=(const
//      QMqttSubscriptionProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttSubscriptionProperties *ritual_ZN27QMqttSubscriptionPropertiesaSERKS_(
    QMqttSubscriptionProperties *self,
    const QMqttSubscriptionProperties *a0) {
  return &(self->operator=(*a0));
}

//  QMqttSubscriptionProperties::~QMqttSubscriptionProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMqttSubscriptionPropertiesD1Ev(
    QMqttSubscriptionProperties *self) {
  delete self;
}

//  QMqttUserProperties QMqttSubscriptionProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK27QMqttSubscriptionProperties14userPropertiesEv(
    const QMqttSubscriptionProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  void QMqttSubscriptionProperties::setUserProperties(const
//      QMqttUserProperties &user)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMqttSubscriptionProperties17setUserPropertiesERK19QMqttUserProperties(
    QMqttSubscriptionProperties *self,
    const QMqttUserProperties *user) {
  self->setUserProperties(*user);
}

//  quint32 QMqttSubscriptionProperties::subscriptionIdentifier() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK27QMqttSubscriptionProperties22subscriptionIdentifierEv(
    const QMqttSubscriptionProperties *self) {
  return self->subscriptionIdentifier();
}

//  void QMqttSubscriptionProperties::setSubscriptionIdentifier(quint32 id)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMqttSubscriptionProperties25setSubscriptionIdentifierEj(
    QMqttSubscriptionProperties *self,
    quint32 id) {
  self->setSubscriptionIdentifier(id);
}

//  bool QMqttSubscriptionProperties::noLocal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QMqttSubscriptionProperties7noLocalEv(
    const QMqttSubscriptionProperties *self) {
  return self->noLocal();
}

//  void QMqttSubscriptionProperties::setNoLocal(bool noloc)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QMqttSubscriptionProperties10setNoLocalEb(
    QMqttSubscriptionProperties *self,
    bool noloc) {
  self->setNoLocal(noloc);
}
