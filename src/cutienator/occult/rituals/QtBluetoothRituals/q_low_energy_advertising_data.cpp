//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergyadvertisingdata.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qlowenergyadvertisingdata.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qlist.h>

//  QLowEnergyAdvertisingData::QLowEnergyAdvertisingData()
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingData *ritual_ZN25QLowEnergyAdvertisingDataC1Ev() {
  return new QLowEnergyAdvertisingData();
}

//  QLowEnergyAdvertisingData::QLowEnergyAdvertisingData(const
//      QLowEnergyAdvertisingData &other)
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingData *ritual_ZN25QLowEnergyAdvertisingDataC1ERKS_(
    const QLowEnergyAdvertisingData *other) {
  return new QLowEnergyAdvertisingData(*other);
}

//  QLowEnergyAdvertisingData::~QLowEnergyAdvertisingData()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingDataD1Ev(
    QLowEnergyAdvertisingData *self) {
  delete self;
}

//  QLowEnergyAdvertisingData &QLowEnergyAdvertisingData::operator=(const
//      QLowEnergyAdvertisingData &other)
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingData *ritual_ZN25QLowEnergyAdvertisingDataaSERKS_(
    QLowEnergyAdvertisingData *self,
    const QLowEnergyAdvertisingData *other) {
  return &(self->operator=(*other));
}

//  bool operator==(const QLowEnergyAdvertisingData &a, const
//      QLowEnergyAdvertisingData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK25QLowEnergyAdvertisingDataS1_(
    const QLowEnergyAdvertisingData *a,
    const QLowEnergyAdvertisingData *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyAdvertisingData &a, const
//      QLowEnergyAdvertisingData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK25QLowEnergyAdvertisingDataS1_(
    const QLowEnergyAdvertisingData *a,
    const QLowEnergyAdvertisingData *b) {
  return operator!=(*a, *b);
}

//  void QLowEnergyAdvertisingData::setLocalName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData12setLocalNameERK7QString(
    QLowEnergyAdvertisingData *self,
    const QString *name) {
  self->setLocalName(*name);
}

//  QString QLowEnergyAdvertisingData::localName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QLowEnergyAdvertisingData9localNameEv(
    const QLowEnergyAdvertisingData *self) {
  return new QString(self->localName());
}

//  quint16 QLowEnergyAdvertisingData::invalidManufacturerId()
extern "C" Q_DECL_EXPORT
quint16 ritual_ZN25QLowEnergyAdvertisingData21invalidManufacturerIdEv() {
  return QLowEnergyAdvertisingData::invalidManufacturerId();
}

//  void QLowEnergyAdvertisingData::setManufacturerData(quint16 id, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData19setManufacturerDataEtRK10QByteArray(
    QLowEnergyAdvertisingData *self,
    quint16 id,
    const QByteArray *data) {
  self->setManufacturerData(id, *data);
}

//  quint16 QLowEnergyAdvertisingData::manufacturerId() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK25QLowEnergyAdvertisingData14manufacturerIdEv(
    const QLowEnergyAdvertisingData *self) {
  return self->manufacturerId();
}

//  QByteArray QLowEnergyAdvertisingData::manufacturerData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QLowEnergyAdvertisingData16manufacturerDataEv(
    const QLowEnergyAdvertisingData *self) {
  return new QByteArray(self->manufacturerData());
}

//  void QLowEnergyAdvertisingData::setIncludePowerLevel(bool doInclude)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData20setIncludePowerLevelEb(
    QLowEnergyAdvertisingData *self,
    bool doInclude) {
  self->setIncludePowerLevel(doInclude);
}

//  bool QLowEnergyAdvertisingData::includePowerLevel() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QLowEnergyAdvertisingData17includePowerLevelEv(
    const QLowEnergyAdvertisingData *self) {
  return self->includePowerLevel();
}

//  void QLowEnergyAdvertisingData::setDiscoverability(Discoverability mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData18setDiscoverabilityENS_15DiscoverabilityE(
    QLowEnergyAdvertisingData *self,
    QLowEnergyAdvertisingData::Discoverability mode) {
  self->setDiscoverability(mode);
}

//  Discoverability QLowEnergyAdvertisingData::discoverability() const
extern "C" Q_DECL_EXPORT
QLowEnergyAdvertisingData::Discoverability ritual_ZNK25QLowEnergyAdvertisingData15discoverabilityEv(
    const QLowEnergyAdvertisingData *self) {
  return self->discoverability();
}

//  void QLowEnergyAdvertisingData::setServices(const QList<QBluetoothUuid>
//      &services)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData11setServicesERK5QListI14QBluetoothUuidE(
    QLowEnergyAdvertisingData *self,
    const QList<QBluetoothUuid> *services) {
  self->setServices(*services);
}

//  QList<QBluetoothUuid> QLowEnergyAdvertisingData::services() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK25QLowEnergyAdvertisingData8servicesEv(
    const QLowEnergyAdvertisingData *self) {
  return new QList<QBluetoothUuid>(self->services());
}

//  void QLowEnergyAdvertisingData::setRawData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData10setRawDataERK10QByteArray(
    QLowEnergyAdvertisingData *self,
    const QByteArray *data) {
  self->setRawData(*data);
}

//  QByteArray QLowEnergyAdvertisingData::rawData() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QLowEnergyAdvertisingData7rawDataEv(
    const QLowEnergyAdvertisingData *self) {
  return new QByteArray(self->rawData());
}

//  void QLowEnergyAdvertisingData::swap(QLowEnergyAdvertisingData &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QLowEnergyAdvertisingData4swapERS_(
    QLowEnergyAdvertisingData *self,
    QLowEnergyAdvertisingData *other) {
  self->swap(*other);
}

//  bool QLowEnergyAdvertisingData::equals(const QLowEnergyAdvertisingData
//      &a, const QLowEnergyAdvertisingData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QLowEnergyAdvertisingData6equalsERKS_S1_(
    const QLowEnergyAdvertisingData *a,
    const QLowEnergyAdvertisingData *b) {
  return QLowEnergyAdvertisingData::equals(*a, *b);
}
