//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothserviceinfo.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtCore/qvariant.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qstring.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QBluetoothServiceInfo::QBluetoothServiceInfo()
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo *ritual_ZN21QBluetoothServiceInfoC1Ev() {
  return new QBluetoothServiceInfo();
}

//  QBluetoothServiceInfo::QBluetoothServiceInfo(const QBluetoothServiceInfo
//      &other)
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo *ritual_ZN21QBluetoothServiceInfoC1ERKS_(
    const QBluetoothServiceInfo *other) {
  return new QBluetoothServiceInfo(*other);
}

//  QBluetoothServiceInfo::~QBluetoothServiceInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfoD1Ev(QBluetoothServiceInfo *self) {
  delete self;
}

//  bool QBluetoothServiceInfo::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QBluetoothServiceInfo7isValidEv(
    const QBluetoothServiceInfo *self) {
  return self->isValid();
}

//  bool QBluetoothServiceInfo::isComplete() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QBluetoothServiceInfo10isCompleteEv(
    const QBluetoothServiceInfo *self) {
  return self->isComplete();
}

//  void QBluetoothServiceInfo::setDevice(const QBluetoothDeviceInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo9setDeviceERK20QBluetoothDeviceInfo(
    QBluetoothServiceInfo *self,
    const QBluetoothDeviceInfo *info) {
  self->setDevice(*info);
}

//  QBluetoothDeviceInfo QBluetoothServiceInfo::device() const
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfo *ritual_ZNK21QBluetoothServiceInfo6deviceEv(
    const QBluetoothServiceInfo *self) {
  return new QBluetoothDeviceInfo(self->device());
}

//  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
//      QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo12setAttributeEtRK8QVariant(
    QBluetoothServiceInfo *self,
    quint16 attributeId,
    const QVariant *value) {
  self->setAttribute(attributeId, *value);
}

//  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
//      QBluetoothUuid &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo12setAttributeEtRK14QBluetoothUuid(
    QBluetoothServiceInfo *self,
    quint16 attributeId,
    const QBluetoothUuid *value) {
  self->setAttribute(attributeId, *value);
}

//  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
//      QBluetoothServiceInfo::Sequence &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo12setAttributeEtRKNS_8SequenceE(
    QBluetoothServiceInfo *self,
    quint16 attributeId,
    const QBluetoothServiceInfo::Sequence *value) {
  self->setAttribute(attributeId, *value);
}

//  void QBluetoothServiceInfo::setAttribute(quint16 attributeId, const
//      QBluetoothServiceInfo::Alternative &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo12setAttributeEtRKNS_11AlternativeE(
    QBluetoothServiceInfo *self,
    quint16 attributeId,
    const QBluetoothServiceInfo::Alternative *value) {
  self->setAttribute(attributeId, *value);
}

//  QVariant QBluetoothServiceInfo::attribute(quint16 attributeId) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QBluetoothServiceInfo9attributeEt(
    const QBluetoothServiceInfo *self,
    quint16 attributeId) {
  return new QVariant(self->attribute(attributeId));
}

//  bool QBluetoothServiceInfo::contains(quint16 attributeId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QBluetoothServiceInfo8containsEt(
    const QBluetoothServiceInfo *self,
    quint16 attributeId) {
  return self->contains(attributeId);
}

//  void QBluetoothServiceInfo::removeAttribute(quint16 attributeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo15removeAttributeEt(
    QBluetoothServiceInfo *self,
    quint16 attributeId) {
  self->removeAttribute(attributeId);
}

//  void QBluetoothServiceInfo::setServiceName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo14setServiceNameERK7QString(
    QBluetoothServiceInfo *self,
    const QString *name) {
  self->setServiceName(*name);
}

//  QString QBluetoothServiceInfo::serviceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QBluetoothServiceInfo11serviceNameEv(
    const QBluetoothServiceInfo *self) {
  return new QString(self->serviceName());
}

//  void QBluetoothServiceInfo::setServiceDescription(const QString
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo21setServiceDescriptionERK7QString(
    QBluetoothServiceInfo *self,
    const QString *description) {
  self->setServiceDescription(*description);
}

//  QString QBluetoothServiceInfo::serviceDescription() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QBluetoothServiceInfo18serviceDescriptionEv(
    const QBluetoothServiceInfo *self) {
  return new QString(self->serviceDescription());
}

//  void QBluetoothServiceInfo::setServiceProvider(const QString &provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo18setServiceProviderERK7QString(
    QBluetoothServiceInfo *self,
    const QString *provider) {
  self->setServiceProvider(*provider);
}

//  QString QBluetoothServiceInfo::serviceProvider() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QBluetoothServiceInfo15serviceProviderEv(
    const QBluetoothServiceInfo *self) {
  return new QString(self->serviceProvider());
}

//  QBluetoothServiceInfo::Protocol QBluetoothServiceInfo::socketProtocol()
//      const
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Protocol ritual_ZNK21QBluetoothServiceInfo14socketProtocolEv(
    const QBluetoothServiceInfo *self) {
  return self->socketProtocol();
}

//  int QBluetoothServiceInfo::protocolServiceMultiplexer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QBluetoothServiceInfo26protocolServiceMultiplexerEv(
    const QBluetoothServiceInfo *self) {
  return self->protocolServiceMultiplexer();
}

//  int QBluetoothServiceInfo::serverChannel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QBluetoothServiceInfo13serverChannelEv(
    const QBluetoothServiceInfo *self) {
  return self->serverChannel();
}

//  QBluetoothServiceInfo::Sequence
//      QBluetoothServiceInfo::protocolDescriptor(QBluetoothUuid::ProtocolUui
//      d protocol) const
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Sequence *ritual_ZNK21QBluetoothServiceInfo18protocolDescriptorEN14QBluetoothUuid12ProtocolUuidE(
    const QBluetoothServiceInfo *self,
    QBluetoothUuid::ProtocolUuid protocol) {
  return new QBluetoothServiceInfo::Sequence(
      self->protocolDescriptor(
          protocol));
}

//  void QBluetoothServiceInfo::setServiceAvailability(quint8 availability)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo22setServiceAvailabilityEh(
    QBluetoothServiceInfo *self,
    quint8 availability) {
  self->setServiceAvailability(availability);
}

//  quint8 QBluetoothServiceInfo::serviceAvailability() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK21QBluetoothServiceInfo19serviceAvailabilityEv(
    const QBluetoothServiceInfo *self) {
  return self->serviceAvailability();
}

//  void QBluetoothServiceInfo::setServiceUuid(const QBluetoothUuid &uuid)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo14setServiceUuidERK14QBluetoothUuid(
    QBluetoothServiceInfo *self,
    const QBluetoothUuid *uuid) {
  self->setServiceUuid(*uuid);
}

//  QBluetoothUuid QBluetoothServiceInfo::serviceUuid() const
extern "C" Q_DECL_EXPORT
QBluetoothUuid *ritual_ZNK21QBluetoothServiceInfo11serviceUuidEv(
    const QBluetoothServiceInfo *self) {
  return new QBluetoothUuid(self->serviceUuid());
}

//  QList<QBluetoothUuid> QBluetoothServiceInfo::serviceClassUuids() const
extern "C" Q_DECL_EXPORT
QList<QBluetoothUuid> *ritual_ZNK21QBluetoothServiceInfo17serviceClassUuidsEv(
    const QBluetoothServiceInfo *self) {
  return new QList<QBluetoothUuid>(self->serviceClassUuids());
}

//  bool QBluetoothServiceInfo::isRegistered() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QBluetoothServiceInfo12isRegisteredEv(
    const QBluetoothServiceInfo *self) {
  return self->isRegistered();
}

//  bool QBluetoothServiceInfo::registerService(const QBluetoothAddress
//      &localAdapter)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBluetoothServiceInfo15registerServiceERK17QBluetoothAddress(
    QBluetoothServiceInfo *self,
    const QBluetoothAddress *localAdapter) {
  return self->registerService(*localAdapter);
}

//  bool QBluetoothServiceInfo::unregisterService()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QBluetoothServiceInfo17unregisterServiceEv(
    QBluetoothServiceInfo *self) {
  return self->unregisterService();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug d, const QBluetoothServiceInfo &i)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK21QBluetoothServiceInfo(
    const QDebug *d,
    const QBluetoothServiceInfo *i) {
  return new QDebug(operator<<(*d, *i));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug QBluetoothServiceInfo::streamingOperator(QDebug a0, const
//      QBluetoothServiceInfo &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_ZN21QBluetoothServiceInfo17streamingOperatorE6QDebugRKS_(
    const QDebug *a0,
    const QBluetoothServiceInfo *a1) {
  return new QDebug(QBluetoothServiceInfo::streamingOperator(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QBluetoothServiceInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QBluetoothServiceInfo> *ritual_list_make_QBluetoothServiceInfo() {
  return new QList<QBluetoothServiceInfo>();
}

//  void QList<QBluetoothServiceInfo>::append(const QBluetoothServiceInfo
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QBluetoothServiceInfo(
    QList<QBluetoothServiceInfo> *self,
    const QBluetoothServiceInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QBluetoothServiceInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QBluetoothServiceInfo(
    const QList<QBluetoothServiceInfo> *self) {
  return self->size();
}

//  const QBluetoothServiceInfo &QList<QBluetoothServiceInfo>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo *ritual_list_at_QBluetoothServiceInfo(
    const QList<QBluetoothServiceInfo> *self,
    long long index) {
  return new QBluetoothServiceInfo(self->at(index));
}

//  QList<QBluetoothServiceInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QBluetoothServiceInfo(
    QList<QBluetoothServiceInfo> *self) {
  delete self;
}
