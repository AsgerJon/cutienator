//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaapplicationdescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuaapplicationdescription.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qlist.h>

//  QOpcUaApplicationDescription::QOpcUaApplicationDescription()
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription *ritual_ZN28QOpcUaApplicationDescriptionC1Ev() {
  return new QOpcUaApplicationDescription();
}

//  QOpcUaApplicationDescription::QOpcUaApplicationDescription(const
//      QOpcUaApplicationDescription &a0)
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription *ritual_ZN28QOpcUaApplicationDescriptionC1ERKS_(
    const QOpcUaApplicationDescription *a0) {
  return new QOpcUaApplicationDescription(*a0);
}

//  QOpcUaApplicationDescription
//      &QOpcUaApplicationDescription::operator=(const
//      QOpcUaApplicationDescription &a0)
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription *ritual_ZN28QOpcUaApplicationDescriptionaSERKS_(
    QOpcUaApplicationDescription *self,
    const QOpcUaApplicationDescription *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaApplicationDescription::operator==(const
//      QOpcUaApplicationDescription &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QOpcUaApplicationDescriptioneqERKS_(
    const QOpcUaApplicationDescription *self,
    const QOpcUaApplicationDescription *a0) {
  return self->operator==(*a0);
}

//  QOpcUaApplicationDescription::~QOpcUaApplicationDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescriptionD1Ev(
    QOpcUaApplicationDescription *self) {
  delete self;
}

//  QString QOpcUaApplicationDescription::applicationUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaApplicationDescription14applicationUriEv(
    const QOpcUaApplicationDescription *self) {
  return new QString(self->applicationUri());
}

//  void QOpcUaApplicationDescription::setApplicationUri(const QString
//      &applicationUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription17setApplicationUriERK7QString(
    QOpcUaApplicationDescription *self,
    const QString *applicationUri) {
  self->setApplicationUri(*applicationUri);
}

//  QString QOpcUaApplicationDescription::productUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaApplicationDescription10productUriEv(
    const QOpcUaApplicationDescription *self) {
  return new QString(self->productUri());
}

//  void QOpcUaApplicationDescription::setProductUri(const QString
//      &productUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription13setProductUriERK7QString(
    QOpcUaApplicationDescription *self,
    const QString *productUri) {
  self->setProductUri(*productUri);
}

//  QOpcUaLocalizedText QOpcUaApplicationDescription::applicationName() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK28QOpcUaApplicationDescription15applicationNameEv(
    const QOpcUaApplicationDescription *self) {
  return new QOpcUaLocalizedText(self->applicationName());
}

//  void QOpcUaApplicationDescription::setApplicationName(const
//      QOpcUaLocalizedText &applicationName)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription18setApplicationNameERK19QOpcUaLocalizedText(
    QOpcUaApplicationDescription *self,
    const QOpcUaLocalizedText *applicationName) {
  self->setApplicationName(*applicationName);
}

//  QOpcUaApplicationDescription::ApplicationType
//      QOpcUaApplicationDescription::applicationType() const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription::ApplicationType ritual_ZNK28QOpcUaApplicationDescription15applicationTypeEv(
    const QOpcUaApplicationDescription *self) {
  return self->applicationType();
}

//  void QOpcUaApplicationDescription::setApplicationType(QOpcUaApplicationDe
//      scription::ApplicationType applicationType)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription18setApplicationTypeENS_15ApplicationTypeE(
    QOpcUaApplicationDescription *self,
    QOpcUaApplicationDescription::ApplicationType applicationType) {
  self->setApplicationType(applicationType);
}

//  QString QOpcUaApplicationDescription::gatewayServerUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaApplicationDescription16gatewayServerUriEv(
    const QOpcUaApplicationDescription *self) {
  return new QString(self->gatewayServerUri());
}

//  void QOpcUaApplicationDescription::setGatewayServerUri(const QString
//      &gatewayServerUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription19setGatewayServerUriERK7QString(
    QOpcUaApplicationDescription *self,
    const QString *gatewayServerUri) {
  self->setGatewayServerUri(*gatewayServerUri);
}

//  QString QOpcUaApplicationDescription::discoveryProfileUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QOpcUaApplicationDescription19discoveryProfileUriEv(
    const QOpcUaApplicationDescription *self) {
  return new QString(self->discoveryProfileUri());
}

//  void QOpcUaApplicationDescription::setDiscoveryProfileUri(const QString
//      &discoveryProfileUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription22setDiscoveryProfileUriERK7QString(
    QOpcUaApplicationDescription *self,
    const QString *discoveryProfileUri) {
  self->setDiscoveryProfileUri(*discoveryProfileUri);
}

//  QList<QString> QOpcUaApplicationDescription::discoveryUrls() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QOpcUaApplicationDescription13discoveryUrlsEv(
    const QOpcUaApplicationDescription *self) {
  return new QList<QString>(self->discoveryUrls());
}

//  QList<QString> &QOpcUaApplicationDescription::discoveryUrlsRef()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN28QOpcUaApplicationDescription16discoveryUrlsRefEv(
    QOpcUaApplicationDescription *self) {
  return &(self->discoveryUrlsRef());
}

//  void QOpcUaApplicationDescription::setDiscoveryUrls(const QList<QString>
//      &discoveryUrls)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QOpcUaApplicationDescription16setDiscoveryUrlsERK5QListI7QStringE(
    QOpcUaApplicationDescription *self,
    const QList<QString> *discoveryUrls) {
  self->setDiscoveryUrls(*discoveryUrls);
}

//  QList<QOpcUaApplicationDescription>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaApplicationDescription> *ritual_list_make_QOpcUaApplicationDescription() {
  return new QList<QOpcUaApplicationDescription>();
}

//  void QList<QOpcUaApplicationDescription>::append(const
//      QOpcUaApplicationDescription &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaApplicationDescription(
    QList<QOpcUaApplicationDescription> *self,
    const QOpcUaApplicationDescription *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaApplicationDescription>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaApplicationDescription(
    const QList<QOpcUaApplicationDescription> *self) {
  return self->size();
}

//  const QOpcUaApplicationDescription
//      &QList<QOpcUaApplicationDescription>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription *ritual_list_at_QOpcUaApplicationDescription(
    const QList<QOpcUaApplicationDescription> *self,
    long long index) {
  return new QOpcUaApplicationDescription(self->at(index));
}

//  QList<QOpcUaApplicationDescription>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaApplicationDescription(
    QList<QOpcUaApplicationDescription> *self) {
  delete self;
}
