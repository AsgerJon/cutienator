//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergydescriptordata.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qlowenergydescriptordata.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>

//  QLowEnergyDescriptorData::QLowEnergyDescriptorData()
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptorData *ritual_ZN24QLowEnergyDescriptorDataC1Ev() {
  return new QLowEnergyDescriptorData();
}

//  QLowEnergyDescriptorData::QLowEnergyDescriptorData(const QBluetoothUuid
//      &uuid, const QByteArray &value)
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptorData *ritual_ZN24QLowEnergyDescriptorDataC1ERK14QBluetoothUuidRK10QByteArray(
    const QBluetoothUuid *uuid,
    const QByteArray *value) {
  return new QLowEnergyDescriptorData(*uuid, *value);
}

//  QLowEnergyDescriptorData::QLowEnergyDescriptorData(const
//      QLowEnergyDescriptorData &other)
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptorData *ritual_ZN24QLowEnergyDescriptorDataC1ERKS_(
    const QLowEnergyDescriptorData *other) {
  return new QLowEnergyDescriptorData(*other);
}

//  QLowEnergyDescriptorData::~QLowEnergyDescriptorData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyDescriptorDataD1Ev(
    QLowEnergyDescriptorData *self) {
  delete self;
}

//  bool operator==(const QLowEnergyDescriptorData &a, const
//      QLowEnergyDescriptorData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QLowEnergyDescriptorDataS1_(
    const QLowEnergyDescriptorData *a,
    const QLowEnergyDescriptorData *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyDescriptorData &a, const
//      QLowEnergyDescriptorData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QLowEnergyDescriptorDataS1_(
    const QLowEnergyDescriptorData *a,
    const QLowEnergyDescriptorData *b) {
  return operator!=(*a, *b);
}

//  QByteArray QLowEnergyDescriptorData::value() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK24QLowEnergyDescriptorData5valueEv(
    const QLowEnergyDescriptorData *self) {
  return new QByteArray(self->value());
}

//  void QLowEnergyDescriptorData::setValue(const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyDescriptorData8setValueERK10QByteArray(
    QLowEnergyDescriptorData *self,
    const QByteArray *value) {
  self->setValue(*value);
}

//  QBluetoothUuid QLowEnergyDescriptorData::uuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK24QLowEnergyDescriptorData4uuidEv(
    const QLowEnergyDescriptorData *self) {
  return new QBluetoothUuid(self->uuid());
}

//  void QLowEnergyDescriptorData::setUuid(const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyDescriptorData7setUuidERK14QBluetoothUuid(
    QLowEnergyDescriptorData *self,
    const QBluetoothUuid *uuid) {
  self->setUuid(*uuid);
}

//  bool QLowEnergyDescriptorData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QLowEnergyDescriptorData7isValidEv(
    const QLowEnergyDescriptorData *self) {
  return self->isValid();
}

//  void QLowEnergyDescriptorData::setReadPermissions(bool readable,
//      QBluetooth::AttAccessConstraints constraints)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyDescriptorData18setReadPermissionsEb6QFlagsIN10QBluetooth19AttAccessConstraintEE(
    QLowEnergyDescriptorData *self,
    bool readable,
    int constraints) {
  self->setReadPermissions(
      readable,
      QFlags<QBluetooth::AttAccessConstraint>::fromInt(constraints));
}

//  bool QLowEnergyDescriptorData::isReadable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QLowEnergyDescriptorData10isReadableEv(
    const QLowEnergyDescriptorData *self) {
  return self->isReadable();
}

//  QBluetooth::AttAccessConstraints
//      QLowEnergyDescriptorData::readConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QLowEnergyDescriptorData15readConstraintsEv(
    const QLowEnergyDescriptorData *self) {
  return static_cast<int>(self->readConstraints().toInt());
}

//  void QLowEnergyDescriptorData::setWritePermissions(bool writable,
//      QBluetooth::AttAccessConstraints constraints)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyDescriptorData19setWritePermissionsEb6QFlagsIN10QBluetooth19AttAccessConstraintEE(
    QLowEnergyDescriptorData *self,
    bool writable,
    int constraints) {
  self->setWritePermissions(
      writable,
      QFlags<QBluetooth::AttAccessConstraint>::fromInt(constraints));
}

//  bool QLowEnergyDescriptorData::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QLowEnergyDescriptorData10isWritableEv(
    const QLowEnergyDescriptorData *self) {
  return self->isWritable();
}

//  QBluetooth::AttAccessConstraints
//      QLowEnergyDescriptorData::writeConstraints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QLowEnergyDescriptorData16writeConstraintsEv(
    const QLowEnergyDescriptorData *self) {
  return static_cast<int>(self->writeConstraints().toInt());
}

//  bool QLowEnergyDescriptorData::equals(const QLowEnergyDescriptorData &a,
//      const QLowEnergyDescriptorData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QLowEnergyDescriptorData6equalsERKS_S1_(
    const QLowEnergyDescriptorData *a,
    const QLowEnergyDescriptorData *b) {
  return QLowEnergyDescriptorData::equals(*a, *b);
}

//  QList<QLowEnergyDescriptorData>::QList()
extern "C" Q_DECL_EXPORT
QList<QLowEnergyDescriptorData> *ritual_list_make_QLowEnergyDescriptorData() {
  return new QList<QLowEnergyDescriptorData>();
}

//  void QList<QLowEnergyDescriptorData>::append(const
//      QLowEnergyDescriptorData &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QLowEnergyDescriptorData(
    QList<QLowEnergyDescriptorData> *self,
    const QLowEnergyDescriptorData *element) {
  self->append(*element);
}

//  qsizetype QList<QLowEnergyDescriptorData>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QLowEnergyDescriptorData(
    const QList<QLowEnergyDescriptorData> *self) {
  return self->size();
}

//  const QLowEnergyDescriptorData
//      &QList<QLowEnergyDescriptorData>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QLowEnergyDescriptorData *ritual_list_at_QLowEnergyDescriptorData(
    const QList<QLowEnergyDescriptorData> *self,
    long long index) {
  return new QLowEnergyDescriptorData(self->at(index));
}

//  QList<QLowEnergyDescriptorData>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QLowEnergyDescriptorData(
    QList<QLowEnergyDescriptorData> *self) {
  delete self;
}
