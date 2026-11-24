//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaapplicationrecorddatatype.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtOpcUa/qopcuaapplicationrecorddatatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qlist.h>

//  QOpcUaApplicationRecordDataType::QOpcUaApplicationRecordDataType()
extern "C" Q_DECL_EXPORT
QOpcUaApplicationRecordDataType *ritual_ZN31QOpcUaApplicationRecordDataTypeC1Ev() {
  return new QOpcUaApplicationRecordDataType();
}

//  QOpcUaApplicationRecordDataType::QOpcUaApplicationRecordDataType(const
//      QOpcUaApplicationRecordDataType &a0)
extern "C" Q_DECL_EXPORT
QOpcUaApplicationRecordDataType *ritual_ZN31QOpcUaApplicationRecordDataTypeC1ERKS_(
    const QOpcUaApplicationRecordDataType *a0) {
  return new QOpcUaApplicationRecordDataType(*a0);
}

//  bool QOpcUaApplicationRecordDataType::operator==(const
//      QOpcUaApplicationRecordDataType &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QOpcUaApplicationRecordDataTypeeqERKS_(
    const QOpcUaApplicationRecordDataType *self,
    const QOpcUaApplicationRecordDataType *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaApplicationRecordDataType::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK31QOpcUaApplicationRecordDataTypecv8QVariantEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaApplicationRecordDataType::~QOpcUaApplicationRecordDataType()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataTypeD1Ev(
    QOpcUaApplicationRecordDataType *self) {
  delete self;
}

//  void QOpcUaApplicationRecordDataType::setApplicationId(const QString
//      &nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType16setApplicationIdERK7QString(
    QOpcUaApplicationRecordDataType *self,
    const QString *nodeId) {
  self->setApplicationId(*nodeId);
}

//  const QString &QOpcUaApplicationRecordDataType::applicationId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QOpcUaApplicationRecordDataType13applicationIdEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QString(self->applicationId());
}

//  void QOpcUaApplicationRecordDataType::setApplicationType(QOpcUaApplicatio
//      nDescription::ApplicationType applicationType)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType18setApplicationTypeEN28QOpcUaApplicationDescription15ApplicationTypeE(
    QOpcUaApplicationRecordDataType *self,
    QOpcUaApplicationDescription::ApplicationType applicationType) {
  self->setApplicationType(applicationType);
}

//  QOpcUaApplicationDescription::ApplicationType
//      QOpcUaApplicationRecordDataType::applicationType() const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription::ApplicationType ritual_ZNK31QOpcUaApplicationRecordDataType15applicationTypeEv(
    const QOpcUaApplicationRecordDataType *self) {
  return self->applicationType();
}

//  void QOpcUaApplicationRecordDataType::setApplicationUri(const QString
//      &applicationUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType17setApplicationUriERK7QString(
    QOpcUaApplicationRecordDataType *self,
    const QString *applicationUri) {
  self->setApplicationUri(*applicationUri);
}

//  const QString &QOpcUaApplicationRecordDataType::applicationUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QOpcUaApplicationRecordDataType14applicationUriEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QString(self->applicationUri());
}

//  void QOpcUaApplicationRecordDataType::setApplicationNames(const
//      QList<QOpcUaLocalizedText> &applicationNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType19setApplicationNamesERK5QListI19QOpcUaLocalizedTextE(
    QOpcUaApplicationRecordDataType *self,
    const QList<QOpcUaLocalizedText> *applicationNames) {
  self->setApplicationNames(*applicationNames);
}

//  const QList<QOpcUaLocalizedText>
//      &QOpcUaApplicationRecordDataType::applicationNames() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaLocalizedText> *ritual_ZNK31QOpcUaApplicationRecordDataType16applicationNamesEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QList<QOpcUaLocalizedText>(self->applicationNames());
}

//  void QOpcUaApplicationRecordDataType::setProductUri(const QString
//      &productUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType13setProductUriERK7QString(
    QOpcUaApplicationRecordDataType *self,
    const QString *productUri) {
  self->setProductUri(*productUri);
}

//  const QString &QOpcUaApplicationRecordDataType::productUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK31QOpcUaApplicationRecordDataType10productUriEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QString(self->productUri());
}

//  void QOpcUaApplicationRecordDataType::setDiscoveryUrls(const
//      QList<QString> &discoveryUrls)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType16setDiscoveryUrlsERK5QListI7QStringE(
    QOpcUaApplicationRecordDataType *self,
    const QList<QString> *discoveryUrls) {
  self->setDiscoveryUrls(*discoveryUrls);
}

//  const QList<QString> &QOpcUaApplicationRecordDataType::discoveryUrls()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK31QOpcUaApplicationRecordDataType13discoveryUrlsEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QList<QString>(self->discoveryUrls());
}

//  void
//      QOpcUaApplicationRecordDataType::setServerCapabilityIdentifiers(const
//      QList<QString> &serverCapabilityIdentifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaApplicationRecordDataType30setServerCapabilityIdentifiersERK5QListI7QStringE(
    QOpcUaApplicationRecordDataType *self,
    const QList<QString> *serverCapabilityIdentifiers) {
  self->setServerCapabilityIdentifiers(*serverCapabilityIdentifiers);
}

//  const QList<QString>
//      &QOpcUaApplicationRecordDataType::serverCapabilityIdentifiers() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK31QOpcUaApplicationRecordDataType27serverCapabilityIdentifiersEv(
    const QOpcUaApplicationRecordDataType *self) {
  return new QList<QString>(self->serverCapabilityIdentifiers());
}
