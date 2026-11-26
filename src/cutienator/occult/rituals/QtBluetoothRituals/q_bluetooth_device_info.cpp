//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothdeviceinfo.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtCore/QMultiHash>
#include <QtCore/QByteArray>
#include <QtBluetooth/QBluetoothUuid>

//  QBluetoothDeviceInfo::QBluetoothDeviceInfo()
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_ZN20QBluetoothDeviceInfoC1Ev() {
  return new QBluetoothDeviceInfo();
}

//  QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothAddress
//      &address, const QString &name, quint32 classOfDevice)
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_ZN20QBluetoothDeviceInfoC1ERK17QBluetoothAddressRK7QStringj(
    const QBluetoothAddress *address,
    const QString *name,
    quint32 classOfDevice) {
  return new QBluetoothDeviceInfo(*address, *name, classOfDevice);
}

//  QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothUuid &uuid,
//      const QString &name, quint32 classOfDevice)
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_ZN20QBluetoothDeviceInfoC1ERK14QBluetoothUuidRK7QStringj(
    const QBluetoothUuid *uuid,
    const QString *name,
    quint32 classOfDevice) {
  return new QBluetoothDeviceInfo(*uuid, *name, classOfDevice);
}

//  QBluetoothDeviceInfo::QBluetoothDeviceInfo(const QBluetoothDeviceInfo
//      &other)
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_ZN20QBluetoothDeviceInfoC1ERKS_(
    const QBluetoothDeviceInfo *other) {
  return new QBluetoothDeviceInfo(*other);
}

//  QBluetoothDeviceInfo::~QBluetoothDeviceInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfoD1Ev(QBluetoothDeviceInfo *self) {
  delete self;
}

//  bool QBluetoothDeviceInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QBluetoothDeviceInfo7isValidEv(
    const QBluetoothDeviceInfo *self) {
  return self->isValid();
}

//  bool QBluetoothDeviceInfo::isCached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QBluetoothDeviceInfo8isCachedEv(
    const QBluetoothDeviceInfo *self) {
  return self->isCached();
}

//  void QBluetoothDeviceInfo::setCached(bool cached)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfo9setCachedEb(
    QBluetoothDeviceInfo *self,
    bool cached) {
  self->setCached(cached);
}

//  QBluetoothDeviceInfo &QBluetoothDeviceInfo::operator=(const
//      QBluetoothDeviceInfo &other)
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_ZN20QBluetoothDeviceInfoaSERKS_(
    QBluetoothDeviceInfo *self,
    const QBluetoothDeviceInfo *other) {
  return &(self->operator=(*other));
}

//  bool operator==(const QBluetoothDeviceInfo &a, const QBluetoothDeviceInfo
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QBluetoothDeviceInfoS1_(
    const QBluetoothDeviceInfo *a,
    const QBluetoothDeviceInfo *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QBluetoothDeviceInfo &a, const QBluetoothDeviceInfo
//      &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QBluetoothDeviceInfoS1_(
    const QBluetoothDeviceInfo *a,
    const QBluetoothDeviceInfo *b) {
  return operator!=(*a, *b);
}

//  QBluetoothAddress QBluetoothDeviceInfo::address() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK20QBluetoothDeviceInfo7addressEv(
    const QBluetoothDeviceInfo *self) {
  return new QBluetoothAddress(self->address());
}

//  QString QBluetoothDeviceInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QBluetoothDeviceInfo4nameEv(
    const QBluetoothDeviceInfo *self) {
  return new QString(self->name());
}

//  void QBluetoothDeviceInfo::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfo7setNameERK7QString(
    QBluetoothDeviceInfo *self,
    const QString *name) {
  self->setName(*name);
}

//  ServiceClasses QBluetoothDeviceInfo::serviceClasses() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QBluetoothDeviceInfo14serviceClassesEv(
    const QBluetoothDeviceInfo *self) {
  return static_cast<int>(self->serviceClasses().toInt());
}

//  MajorDeviceClass QBluetoothDeviceInfo::majorDeviceClass() const
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo::MajorDeviceClass ritual_ZNK20QBluetoothDeviceInfo16majorDeviceClassEv(
    const QBluetoothDeviceInfo *self) {
  return self->majorDeviceClass();
}

//  quint8 QBluetoothDeviceInfo::minorDeviceClass() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK20QBluetoothDeviceInfo16minorDeviceClassEv(
    const QBluetoothDeviceInfo *self) {
  return self->minorDeviceClass();
}

//  qint16 QBluetoothDeviceInfo::rssi() const
extern "C" Q_DECL_EXPORT
qint16 ritual_ZNK20QBluetoothDeviceInfo4rssiEv(
    const QBluetoothDeviceInfo *self) {
  return self->rssi();
}

//  void QBluetoothDeviceInfo::setRssi(qint16 signal)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfo7setRssiEs(
    QBluetoothDeviceInfo *self,
    qint16 signal) {
  self->setRssi(signal);
}

//  QList<QBluetoothUuid> QBluetoothDeviceInfo::serviceUuids() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK20QBluetoothDeviceInfo12serviceUuidsEv(
    const QBluetoothDeviceInfo *self) {
  return new QList<QBluetoothUuid>(self->serviceUuids());
}

//  void QBluetoothDeviceInfo::setServiceUuids(const QList<QBluetoothUuid>
//      &uuids)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfo15setServiceUuidsERK5QListI14QBluetoothUuidE(
    QBluetoothDeviceInfo *self,
    const QList<QBluetoothUuid> *uuids) {
  self->setServiceUuids(*uuids);
}

//  QList<quint16> QBluetoothDeviceInfo::manufacturerIds() const
extern "C" Q_DECL_EXPORT
QList<quint16> *ritual_ZNK20QBluetoothDeviceInfo15manufacturerIdsEv(
    const QBluetoothDeviceInfo *self) {
  return new QList<quint16>(self->manufacturerIds());
}

//  QByteArray QBluetoothDeviceInfo::manufacturerData(quint16 manufacturerId)
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QBluetoothDeviceInfo16manufacturerDataEt(
    const QBluetoothDeviceInfo *self,
    quint16 manufacturerId) {
  return new QByteArray(self->manufacturerData(manufacturerId));
}

//  bool QBluetoothDeviceInfo::setManufacturerData(quint16 manufacturerId,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QBluetoothDeviceInfo19setManufacturerDataEtRK10QByteArray(
    QBluetoothDeviceInfo *self,
    quint16 manufacturerId,
    const QByteArray *data) {
  return self->setManufacturerData(manufacturerId, *data);
}

//  QMultiHash<quint16, QByteArray> QBluetoothDeviceInfo::manufacturerData()
//      const
extern "C" Q_DECL_EXPORT
QMultiHash<quint16, QByteArray> *ritual_ZNK20QBluetoothDeviceInfo16manufacturerDataEv(
    const QBluetoothDeviceInfo *self) {
  return new QMultiHash<quint16, QByteArray>(self->manufacturerData());
}

//  QList<QBluetoothUuid> QBluetoothDeviceInfo::serviceIds() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK20QBluetoothDeviceInfo10serviceIdsEv(
    const QBluetoothDeviceInfo *self) {
  return new QList<QBluetoothUuid>(self->serviceIds());
}

//  QByteArray QBluetoothDeviceInfo::serviceData(const QBluetoothUuid
//      &serviceId) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QBluetoothDeviceInfo11serviceDataERK14QBluetoothUuid(
    const QBluetoothDeviceInfo *self,
    const QBluetoothUuid *serviceId) {
  return new QByteArray(self->serviceData(*serviceId));
}

//  bool QBluetoothDeviceInfo::setServiceData(const QBluetoothUuid
//      &serviceId, const QByteArray &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QBluetoothDeviceInfo14setServiceDataERK14QBluetoothUuidRK10QByteArray(
    QBluetoothDeviceInfo *self,
    const QBluetoothUuid *serviceId,
    const QByteArray *data) {
  return self->setServiceData(*serviceId, *data);
}

//  QMultiHash<QBluetoothUuid, QByteArray>
//      QBluetoothDeviceInfo::serviceData() const
extern "C" Q_DECL_EXPORT
QMultiHash<QBluetoothUuid, QByteArray> *ritual_ZNK20QBluetoothDeviceInfo11serviceDataEv(
    const QBluetoothDeviceInfo *self) {
  return new QMultiHash<QBluetoothUuid, QByteArray>(self->serviceData());
}

//  void QBluetoothDeviceInfo::setCoreConfigurations(QBluetoothDeviceInfo::Co
//      reConfigurations coreConfigs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfo21setCoreConfigurationsE6QFlagsINS_17CoreConfigurationEE(
    QBluetoothDeviceInfo *self,
    int coreConfigs) {
  self->setCoreConfigurations(
      QFlags<QBluetoothDeviceInfo::CoreConfiguration>::fromInt(coreConfigs));
}

//  QBluetoothDeviceInfo::CoreConfigurations
//      QBluetoothDeviceInfo::coreConfigurations() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QBluetoothDeviceInfo18coreConfigurationsEv(
    const QBluetoothDeviceInfo *self) {
  return static_cast<int>(self->coreConfigurations().toInt());
}

//  void QBluetoothDeviceInfo::setDeviceUuid(const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothDeviceInfo13setDeviceUuidERK14QBluetoothUuid(
    QBluetoothDeviceInfo *self,
    const QBluetoothUuid *uuid) {
  self->setDeviceUuid(*uuid);
}

//  QBluetoothUuid QBluetoothDeviceInfo::deviceUuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK20QBluetoothDeviceInfo10deviceUuidEv(
    const QBluetoothDeviceInfo *self) {
  return new QBluetoothUuid(self->deviceUuid());
}

//  bool QBluetoothDeviceInfo::equals(const QBluetoothDeviceInfo &a, const
//      QBluetoothDeviceInfo &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QBluetoothDeviceInfo6equalsERKS_S1_(
    const QBluetoothDeviceInfo *a,
    const QBluetoothDeviceInfo *b) {
  return QBluetoothDeviceInfo::equals(*a, *b);
}

//  QBluetoothDeviceInfoPrivate *QBluetoothDeviceInfo::d_func()
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfoPrivate *ritual_ZN20QBluetoothDeviceInfo6d_funcEv(
    QBluetoothDeviceInfo *self) {
  return self->d_func();
}

//  const QBluetoothDeviceInfoPrivate *QBluetoothDeviceInfo::d_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothDeviceInfoPrivate *ritual_ZNK20QBluetoothDeviceInfo6d_funcEv(
    const QBluetoothDeviceInfo *self) {
  return self->d_func();
}

//  QList<QBluetoothDeviceInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QBluetoothDeviceInfo> *ritual_list_make_QBluetoothDeviceInfo() {
  return new QList<QBluetoothDeviceInfo>();
}

//  void QList<QBluetoothDeviceInfo>::append(const QBluetoothDeviceInfo
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBluetoothDeviceInfo(
    QList<QBluetoothDeviceInfo> *self,
    const QBluetoothDeviceInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QBluetoothDeviceInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBluetoothDeviceInfo(
    const QList<QBluetoothDeviceInfo> *self) {
  return self->size();
}

//  const QBluetoothDeviceInfo &QList<QBluetoothDeviceInfo>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_list_at_QBluetoothDeviceInfo(
    const QList<QBluetoothDeviceInfo> *self,
    long long index) {
  return new QBluetoothDeviceInfo(self->at(index));
}

//  QList<QBluetoothDeviceInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBluetoothDeviceInfo(
    QList<QBluetoothDeviceInfo> *self) {
  delete self;
}

//  a QList<quint16> a ritual of QBluetoothDeviceInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBluetoothDeviceInfo__QList_quint16(QList<quint16> *self) {
  delete self;
}

//  a QMultiHash<quint16, QByteArray> a ritual of QBluetoothDeviceInfo gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBluetoothDeviceInfo__QMultiHash_quint16_QByteArray(
    QMultiHash<quint16, QByteArray> *self) {
  delete self;
}

//  a QMultiHash<QBluetoothUuid, QByteArray> a ritual of QBluetoothDeviceInfo
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QBluetoothDeviceInfo__QMultiHash_QBluetoothUuid_QByteArray(
    QMultiHash<QBluetoothUuid, QByteArray> *self) {
  delete self;
}
