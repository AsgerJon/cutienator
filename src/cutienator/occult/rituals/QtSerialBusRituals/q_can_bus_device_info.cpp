//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qcanbusdeviceinfo.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qcanbusdeviceinfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QCanBusDeviceInfo::QCanBusDeviceInfo(const QCanBusDeviceInfo &other)
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfo *ritual_ZN17QCanBusDeviceInfoC1ERKS_(
    const QCanBusDeviceInfo *other) {
  return new QCanBusDeviceInfo(*other);
}

//  QCanBusDeviceInfo::~QCanBusDeviceInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCanBusDeviceInfoD1Ev(QCanBusDeviceInfo *self) {
  delete self;
}

//  QString QCanBusDeviceInfo::plugin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCanBusDeviceInfo6pluginEv(
    const QCanBusDeviceInfo *self) {
  return new QString(self->plugin());
}

//  QString QCanBusDeviceInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCanBusDeviceInfo4nameEv(
    const QCanBusDeviceInfo *self) {
  return new QString(self->name());
}

//  QString QCanBusDeviceInfo::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCanBusDeviceInfo11descriptionEv(
    const QCanBusDeviceInfo *self) {
  return new QString(self->description());
}

//  QString QCanBusDeviceInfo::serialNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCanBusDeviceInfo12serialNumberEv(
    const QCanBusDeviceInfo *self) {
  return new QString(self->serialNumber());
}

//  QString QCanBusDeviceInfo::alias() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QCanBusDeviceInfo5aliasEv(
    const QCanBusDeviceInfo *self) {
  return new QString(self->alias());
}

//  int QCanBusDeviceInfo::channel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QCanBusDeviceInfo7channelEv(const QCanBusDeviceInfo *self) {
  return self->channel();
}

//  bool QCanBusDeviceInfo::hasFlexibleDataRate() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCanBusDeviceInfo19hasFlexibleDataRateEv(
    const QCanBusDeviceInfo *self) {
  return self->hasFlexibleDataRate();
}

//  bool QCanBusDeviceInfo::isVirtual() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QCanBusDeviceInfo9isVirtualEv(
    const QCanBusDeviceInfo *self) {
  return self->isVirtual();
}

//  QList<QCanBusDeviceInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QCanBusDeviceInfo> *ritual_list_make_QCanBusDeviceInfo() {
  return new QList<QCanBusDeviceInfo>();
}

//  void QList<QCanBusDeviceInfo>::append(const QCanBusDeviceInfo &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QCanBusDeviceInfo(
    QList<QCanBusDeviceInfo> *self,
    const QCanBusDeviceInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QCanBusDeviceInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QCanBusDeviceInfo(
    const QList<QCanBusDeviceInfo> *self) {
  return self->size();
}

//  const QCanBusDeviceInfo &QList<QCanBusDeviceInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfo *ritual_list_at_QCanBusDeviceInfo(
    const QList<QCanBusDeviceInfo> *self,
    long long index) {
  return new QCanBusDeviceInfo(self->at(index));
}

//  QList<QCanBusDeviceInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QCanBusDeviceInfo(QList<QCanBusDeviceInfo> *self) {
  delete self;
}
