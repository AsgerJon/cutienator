//  Written by dev_tooling.RitualGenerator from the records of
//  QtMqtt/qmqttpublishproperties.h, Qt 6.12.0. Changes made here are lost.
#include <QtMqtt/qmqttpublishproperties.h>
#include <QtCore/qstring.h>
#include <QtMqtt/qmqtttype.h>

//  QMqttMessageStatusProperties::QMqttMessageStatusProperties()
extern "C" Q_DECL_EXPORT
QMqttMessageStatusProperties *ritual_ZN28QMqttMessageStatusPropertiesC1Ev() {
  return new QMqttMessageStatusProperties();
}

//  QMqttMessageStatusProperties::QMqttMessageStatusProperties(const
//      QMqttMessageStatusProperties &a0)
extern "C" Q_DECL_EXPORT
QMqttMessageStatusProperties *ritual_ZN28QMqttMessageStatusPropertiesC1ERKS_(
    const QMqttMessageStatusProperties *a0) {
  return new QMqttMessageStatusProperties(*a0);
}

//  QMqttMessageStatusProperties::~QMqttMessageStatusProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QMqttMessageStatusPropertiesD1Ev(
    QMqttMessageStatusProperties *self) {
  delete self;
}

//  QMqtt::ReasonCode QMqttMessageStatusProperties::reasonCode() const
extern "C" Q_DECL_EXPORT
QMqtt::ReasonCode ritual_ZNK28QMqttMessageStatusProperties10reasonCodeEv(
    const QMqttMessageStatusProperties *self) {
  return self->reasonCode();
}

//  QString QMqttMessageStatusProperties::reason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QMqttMessageStatusProperties6reasonEv(
    const QMqttMessageStatusProperties *self) {
  return new QString(self->reason());
}

//  QMqttUserProperties QMqttMessageStatusProperties::userProperties() const
extern "C" Q_DECL_EXPORT
QMqttUserProperties *ritual_ZNK28QMqttMessageStatusProperties14userPropertiesEv(
    const QMqttMessageStatusProperties *self) {
  return new QMqttUserProperties(self->userProperties());
}
