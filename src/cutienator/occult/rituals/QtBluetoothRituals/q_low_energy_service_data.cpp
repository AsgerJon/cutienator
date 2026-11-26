//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qlowenergyservicedata.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qlowenergyservicedata.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qlowenergyservice.h>
#include <QtBluetooth/qlowenergycharacteristicdata.h>
#include <QtCore/qlist.h>

//  QLowEnergyServiceData::QLowEnergyServiceData()
extern "C" Q_DECL_EXPORT
QLowEnergyServiceData *ritual_ZN21QLowEnergyServiceDataC1Ev() {
  return new QLowEnergyServiceData();
}

//  QLowEnergyServiceData::QLowEnergyServiceData(const QLowEnergyServiceData
//      &other)
extern "C" Q_DECL_EXPORT
QLowEnergyServiceData *ritual_ZN21QLowEnergyServiceDataC1ERKS_(
    const QLowEnergyServiceData *other) {
  return new QLowEnergyServiceData(*other);
}

//  QLowEnergyServiceData::~QLowEnergyServiceData()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceDataD1Ev(QLowEnergyServiceData *self) {
  delete self;
}

//  QLowEnergyServiceData &QLowEnergyServiceData::operator=(const
//      QLowEnergyServiceData &other)
extern "C" Q_DECL_EXPORT
QLowEnergyServiceData *ritual_ZN21QLowEnergyServiceDataaSERKS_(
    QLowEnergyServiceData *self,
    const QLowEnergyServiceData *other) {
  return &(self->operator=(*other));
}

//  bool operator==(const QLowEnergyServiceData &a, const
//      QLowEnergyServiceData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK21QLowEnergyServiceDataS1_(
    const QLowEnergyServiceData *a,
    const QLowEnergyServiceData *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QLowEnergyServiceData &a, const
//      QLowEnergyServiceData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK21QLowEnergyServiceDataS1_(
    const QLowEnergyServiceData *a,
    const QLowEnergyServiceData *b) {
  return operator!=(*a, *b);
}

//  ServiceType QLowEnergyServiceData::type() const
extern "C" Q_DECL_EXPORT
QLowEnergyServiceData::ServiceType ritual_ZNK21QLowEnergyServiceData4typeEv(
    const QLowEnergyServiceData *self) {
  return self->type();
}

//  void QLowEnergyServiceData::setType(ServiceType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData7setTypeENS_11ServiceTypeE(
    QLowEnergyServiceData *self,
    QLowEnergyServiceData::ServiceType type) {
  self->setType(type);
}

//  QBluetoothUuid QLowEnergyServiceData::uuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK21QLowEnergyServiceData4uuidEv(
    const QLowEnergyServiceData *self) {
  return new QBluetoothUuid(self->uuid());
}

//  void QLowEnergyServiceData::setUuid(const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData7setUuidERK14QBluetoothUuid(
    QLowEnergyServiceData *self,
    const QBluetoothUuid *uuid) {
  self->setUuid(*uuid);
}

//  QList<QLowEnergyService *> QLowEnergyServiceData::includedServices()
//      const
extern "C" Q_DECL_EXPORT
QList<QLowEnergyService *> *ritual_ZNK21QLowEnergyServiceData16includedServicesEv(
    const QLowEnergyServiceData *self) {
  return new QList<QLowEnergyService *>(self->includedServices());
}

//  void QLowEnergyServiceData::setIncludedServices(const
//      QList<QLowEnergyService *> &services)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData19setIncludedServicesERK5QListIP17QLowEnergyServiceE(
    QLowEnergyServiceData *self,
    const QList<QLowEnergyService *> *services) {
  self->setIncludedServices(*services);
}

//  void QLowEnergyServiceData::addIncludedService(QLowEnergyService
//      *service)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData18addIncludedServiceEP17QLowEnergyService(
    QLowEnergyServiceData *self,
    QLowEnergyService *service) {
  self->addIncludedService(service);
}

//  QList<QLowEnergyCharacteristicData>
//      QLowEnergyServiceData::characteristics() const
extern "C" Q_DECL_EXPORT
QList<QLowEnergyCharacteristicData> *ritual_ZNK21QLowEnergyServiceData15characteristicsEv(
    const QLowEnergyServiceData *self) {
  return new QList<QLowEnergyCharacteristicData>(self->characteristics());
}

//  void QLowEnergyServiceData::setCharacteristics(const
//      QList<QLowEnergyCharacteristicData> &characteristics)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData18setCharacteristicsERK5QListI28QLowEnergyCharacteristicDataE(
    QLowEnergyServiceData *self,
    const QList<QLowEnergyCharacteristicData> *characteristics) {
  self->setCharacteristics(*characteristics);
}

//  void QLowEnergyServiceData::addCharacteristic(const
//      QLowEnergyCharacteristicData &characteristic)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData17addCharacteristicERK28QLowEnergyCharacteristicData(
    QLowEnergyServiceData *self,
    const QLowEnergyCharacteristicData *characteristic) {
  self->addCharacteristic(*characteristic);
}

//  bool QLowEnergyServiceData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QLowEnergyServiceData7isValidEv(
    const QLowEnergyServiceData *self) {
  return self->isValid();
}

//  void QLowEnergyServiceData::swap(QLowEnergyServiceData &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QLowEnergyServiceData4swapERS_(
    QLowEnergyServiceData *self,
    QLowEnergyServiceData *other) {
  self->swap(*other);
}

//  bool QLowEnergyServiceData::equals(const QLowEnergyServiceData &a, const
//      QLowEnergyServiceData &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QLowEnergyServiceData6equalsERKS_S1_(
    const QLowEnergyServiceData *a,
    const QLowEnergyServiceData *b) {
  return QLowEnergyServiceData::equals(*a, *b);
}
