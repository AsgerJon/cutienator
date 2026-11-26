//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttsubscriptionproperties.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtMqtt/qmqttsubscriptionproperties.h>
#include <QtMqtt/qmqtttype.h>

//  QMqttUnsubscriptionProperties::QMqttUnsubscriptionProperties()
extern "C" Q_DECL_EXPORT
QMqttUnsubscriptionProperties *ritual_ZN29QMqttUnsubscriptionPropertiesC1Ev() {
  return new QMqttUnsubscriptionProperties();
}

//  QMqttUnsubscriptionProperties::QMqttUnsubscriptionProperties(const
//      QMqttUnsubscriptionProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttUnsubscriptionProperties *ritual_ZN29QMqttUnsubscriptionPropertiesC1ERKS_(
    const QMqttUnsubscriptionProperties *a0) {
  return new QMqttUnsubscriptionProperties(*a0);
}

//  QMqttUnsubscriptionProperties
//      &QMqttUnsubscriptionProperties::operator=(const
//      QMqttUnsubscriptionProperties &rhs)
extern "C" Q_DECL_EXPORT
QMqttUnsubscriptionProperties *ritual_ZN29QMqttUnsubscriptionPropertiesaSERKS_(
    QMqttUnsubscriptionProperties *self,
    const QMqttUnsubscriptionProperties *rhs) {
  return &(self->operator=(*rhs));
}

//  QMqttUnsubscriptionProperties::~QMqttUnsubscriptionProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttUnsubscriptionPropertiesD1Ev(
    QMqttUnsubscriptionProperties *self) {
  delete self;
}

//  QMqttUserProperties QMqttUnsubscriptionProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK29QMqttUnsubscriptionProperties14userPropertiesEv(
    const QMqttUnsubscriptionProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}

//  void QMqttUnsubscriptionProperties::setUserProperties(const
//      QMqttUserProperties &user)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QMqttUnsubscriptionProperties17setUserPropertiesERK19QMqttUserProperties(
    QMqttUnsubscriptionProperties *self,
    const QMqttUserProperties *user) {
  self->setUserProperties(*user);
}
