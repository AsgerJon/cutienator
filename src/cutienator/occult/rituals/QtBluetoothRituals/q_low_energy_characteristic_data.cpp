//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergycharacteristicdata.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtBluetooth/qlowenergycharacteristicdata.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergydescriptordata.h>
#include <QtCore/qlist.h>

//  QLowEnergyCharacteristicData::QLowEnergyCharacteristicData()
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristicData *ritual_ZN28QLowEnergyCharacteristicDataC1Ev() {
  return new QLowEnergyCharacteristicData();
}

//  QLowEnergyCharacteristicData::QLowEnergyCharacteristicData(const
//      QLowEnergyCharacteristicData &other)
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristicData *ritual_ZN28QLowEnergyCharacteristicDataC1ERKS_(
    const QLowEnergyCharacteristicData *other) {
  return new QLowEnergyCharacteristicData(*other);
}

//  QLowEnergyCharacteristicData::~QLowEnergyCharacteristicData()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicDataD1Ev(
    QLowEnergyCharacteristicData *self) {
  delete self;
}

//  bool operator==(const QLowEnergyCharacteristicData &a, const
//      QLowEnergyCharacteristicData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK28QLowEnergyCharacteristicDataS1_(
    const QLowEnergyCharacteristicData *a,
    const QLowEnergyCharacteristicData *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyCharacteristicData &a, const
//      QLowEnergyCharacteristicData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK28QLowEnergyCharacteristicDataS1_(
    const QLowEnergyCharacteristicData *a,
    const QLowEnergyCharacteristicData *b) {
  return operator!=(*a, *b);
}

//  QBluetoothUuid QLowEnergyCharacteristicData::uuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK28QLowEnergyCharacteristicData4uuidEv(
    const QLowEnergyCharacteristicData *self) {
  return new QBluetoothUuid(self->uuid());
}

//  void QLowEnergyCharacteristicData::setUuid(const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData7setUuidERK14QBluetoothUuid(
    QLowEnergyCharacteristicData *self,
    const QBluetoothUuid *uuid) {
  self->setUuid(*uuid);
}

//  QByteArray QLowEnergyCharacteristicData::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK28QLowEnergyCharacteristicData5valueEv(
    const QLowEnergyCharacteristicData *self) {
  return new QByteArray(self->value());
}

//  void QLowEnergyCharacteristicData::setValue(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData8setValueERK10QByteArray(
    QLowEnergyCharacteristicData *self,
    const QByteArray *value) {
  self->setValue(*value);
}

//  QLowEnergyCharacteristic::PropertyTypes
//      QLowEnergyCharacteristicData::properties() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QLowEnergyCharacteristicData10propertiesEv(
    const QLowEnergyCharacteristicData *self) {
  return static_cast<int>(self->properties().toInt());
}

//  void QLowEnergyCharacteristicData::setProperties(QLowEnergyCharacteristic
//      ::PropertyTypes properties)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData13setPropertiesE6QFlagsIN24QLowEnergyCharacteristic12PropertyTypeEE(
    QLowEnergyCharacteristicData *self,
    int properties) {
  self->setProperties(
      QFlags<QLowEnergyCharacteristic::PropertyType>::fromInt(properties));
}

//  QList<QLowEnergyDescriptorData>
//      QLowEnergyCharacteristicData::descriptors() const
extern "C" Q_DECL_EXPORT
QList<QLowEnergyDescriptorData> *ritual_ZNK28QLowEnergyCharacteristicData11descriptorsEv(
    const QLowEnergyCharacteristicData *self) {
  return new QList<QLowEnergyDescriptorData>(self->descriptors());
}

//  void QLowEnergyCharacteristicData::setDescriptors(const
//      QList<QLowEnergyDescriptorData> &descriptors)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData14setDescriptorsERK5QListI24QLowEnergyDescriptorDataE(
    QLowEnergyCharacteristicData *self,
    const QList<QLowEnergyDescriptorData> *descriptors) {
  self->setDescriptors(*descriptors);
}

//  void QLowEnergyCharacteristicData::addDescriptor(const
//      QLowEnergyDescriptorData &descriptor)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData13addDescriptorERK24QLowEnergyDescriptorData(
    QLowEnergyCharacteristicData *self,
    const QLowEnergyDescriptorData *descriptor) {
  self->addDescriptor(*descriptor);
}

//  void QLowEnergyCharacteristicData::setReadConstraints(QBluetooth::AttAcce
//      ssConstraints constraints)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData18setReadConstraintsE6QFlagsIN10QBluetooth19AttAccessConstraintEE(
    QLowEnergyCharacteristicData *self,
    int constraints) {
  self->setReadConstraints(
      QFlags<QBluetooth::AttAccessConstraint>::fromInt(constraints));
}

//  QBluetooth::AttAccessConstraints
//      QLowEnergyCharacteristicData::readConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QLowEnergyCharacteristicData15readConstraintsEv(
    const QLowEnergyCharacteristicData *self) {
  return static_cast<int>(self->readConstraints().toInt());
}

//  void QLowEnergyCharacteristicData::setWriteConstraints(QBluetooth::AttAcc
//      essConstraints constraints)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData19setWriteConstraintsE6QFlagsIN10QBluetooth19AttAccessConstraintEE(
    QLowEnergyCharacteristicData *self,
    int constraints) {
  self->setWriteConstraints(
      QFlags<QBluetooth::AttAccessConstraint>::fromInt(constraints));
}

//  QBluetooth::AttAccessConstraints
//      QLowEnergyCharacteristicData::writeConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QLowEnergyCharacteristicData16writeConstraintsEv(
    const QLowEnergyCharacteristicData *self) {
  return static_cast<int>(self->writeConstraints().toInt());
}

//  void QLowEnergyCharacteristicData::setValueLength(int minimum, int
//      maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QLowEnergyCharacteristicData14setValueLengthEii(
    QLowEnergyCharacteristicData *self,
    int minimum,
    int maximum) {
  self->setValueLength(minimum, maximum);
}

//  int QLowEnergyCharacteristicData::minimumValueLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QLowEnergyCharacteristicData18minimumValueLengthEv(
    const QLowEnergyCharacteristicData *self) {
  return self->minimumValueLength();
}

//  int QLowEnergyCharacteristicData::maximumValueLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QLowEnergyCharacteristicData18maximumValueLengthEv(
    const QLowEnergyCharacteristicData *self) {
  return self->maximumValueLength();
}

//  bool QLowEnergyCharacteristicData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QLowEnergyCharacteristicData7isValidEv(
    const QLowEnergyCharacteristicData *self) {
  return self->isValid();
}

//  bool QLowEnergyCharacteristicData::equals(const
//      QLowEnergyCharacteristicData &a, const QLowEnergyCharacteristicData
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QLowEnergyCharacteristicData6equalsERKS_S1_(
    const QLowEnergyCharacteristicData *a,
    const QLowEnergyCharacteristicData *b) {
  return QLowEnergyCharacteristicData::equals(*a, *b);
}

//  QList<QLowEnergyCharacteristicData>::QList()
extern "C" Q_DECL_EXPORT
QList<QLowEnergyCharacteristicData> *ritual_list_make_QLowEnergyCharacteristicData() {
  return new QList<QLowEnergyCharacteristicData>();
}

//  void QList<QLowEnergyCharacteristicData>::append(const
//      QLowEnergyCharacteristicData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLowEnergyCharacteristicData(
    QList<QLowEnergyCharacteristicData> *self,
    const QLowEnergyCharacteristicData *element) {
  self->append(*element);
}

//  qsizetype QList<QLowEnergyCharacteristicData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLowEnergyCharacteristicData(
    const QList<QLowEnergyCharacteristicData> *self) {
  return self->size();
}

//  const QLowEnergyCharacteristicData
//      &QList<QLowEnergyCharacteristicData>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLowEnergyCharacteristicData *ritual_list_at_QLowEnergyCharacteristicData(
    const QList<QLowEnergyCharacteristicData> *self,
    long long index) {
  return new QLowEnergyCharacteristicData(self->at(index));
}

//  QList<QLowEnergyCharacteristicData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLowEnergyCharacteristicData(
    QList<QLowEnergyCharacteristicData> *self) {
  delete self;
}
