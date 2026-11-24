//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusdeviceidentification.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtSerialBus/qmodbusdeviceidentification.h>
#include <QtCore/qbytearray.h>

//  QModbusDeviceIdentification::QModbusDeviceIdentification()
extern "C" Q_DECL_EXPORT
QModbusDeviceIdentification *ritual_ZN27QModbusDeviceIdentificationC1Ev() {
  return new QModbusDeviceIdentification();
}

//  bool QModbusDeviceIdentification::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QModbusDeviceIdentification7isValidEv(
    const QModbusDeviceIdentification *self) {
  return self->isValid();
}

//  void QModbusDeviceIdentification::remove(uint objectId)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QModbusDeviceIdentification6removeEj(
    QModbusDeviceIdentification *self,
    uint objectId) {
  self->remove(objectId);
}

//  bool QModbusDeviceIdentification::contains(uint objectId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QModbusDeviceIdentification8containsEj(
    const QModbusDeviceIdentification *self,
    uint objectId) {
  return self->contains(objectId);
}

//  bool QModbusDeviceIdentification::insert(uint objectId, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN27QModbusDeviceIdentification6insertEjRK10QByteArray(
    QModbusDeviceIdentification *self,
    uint objectId,
    const QByteArray *data) {
  return self->insert(objectId, *data);
}

//  QByteArray QModbusDeviceIdentification::value(uint objectId) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK27QModbusDeviceIdentification5valueEj(
    const QModbusDeviceIdentification *self,
    uint objectId) {
  return new QByteArray(self->value(objectId));
}

//  ConformityLevel QModbusDeviceIdentification::conformityLevel() const
extern "C" Q_DECL_EXPORT
QModbusDeviceIdentification::ConformityLevel ritual_ZNK27QModbusDeviceIdentification15conformityLevelEv(
    const QModbusDeviceIdentification *self) {
  return self->conformityLevel();
}

//  void QModbusDeviceIdentification::setConformityLevel(ConformityLevel
//      level)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QModbusDeviceIdentification18setConformityLevelENS_15ConformityLevelE(
    QModbusDeviceIdentification *self,
    QModbusDeviceIdentification::ConformityLevel level) {
  self->setConformityLevel(level);
}

//  QModbusDeviceIdentification
//      QModbusDeviceIdentification::fromByteArray(const QByteArray &ba)
extern "C" Q_DECL_EXPORT
QModbusDeviceIdentification *ritual_ZN27QModbusDeviceIdentification13fromByteArrayERK10QByteArray(
    const QByteArray *ba) {
  return new QModbusDeviceIdentification(
      QModbusDeviceIdentification::fromByteArray(
          *ba));
}

//  QModbusDeviceIdentification::~QModbusDeviceIdentification()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QModbusDeviceIdentificationD1Ev(
    QModbusDeviceIdentification *self) {
  delete self;
}
