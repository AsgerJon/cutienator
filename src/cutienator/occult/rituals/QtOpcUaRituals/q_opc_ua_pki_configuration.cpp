//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuapkiconfiguration.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuapkiconfiguration.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaapplicationidentity.h>

//  QOpcUaPkiConfiguration::QOpcUaPkiConfiguration()
extern "C" Q_DECL_EXPORT
QOpcUaPkiConfiguration *ritual_ZN22QOpcUaPkiConfigurationC1Ev() {
  return new QOpcUaPkiConfiguration();
}

//  QOpcUaPkiConfiguration::~QOpcUaPkiConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfigurationD1Ev(QOpcUaPkiConfiguration *self) {
  delete self;
}

//  QOpcUaPkiConfiguration::QOpcUaPkiConfiguration(const
//      QOpcUaPkiConfiguration &other)
extern "C" Q_DECL_EXPORT
QOpcUaPkiConfiguration *ritual_ZN22QOpcUaPkiConfigurationC1ERKS_(
    const QOpcUaPkiConfiguration *other) {
  return new QOpcUaPkiConfiguration(*other);
}

//  QString QOpcUaPkiConfiguration::clientCertificateFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaPkiConfiguration21clientCertificateFileEv(
    const QOpcUaPkiConfiguration *self) {
  return new QString(self->clientCertificateFile());
}

//  void QOpcUaPkiConfiguration::setClientCertificateFile(const QString
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfiguration24setClientCertificateFileERK7QString(
    QOpcUaPkiConfiguration *self,
    const QString *value) {
  self->setClientCertificateFile(*value);
}

//  QString QOpcUaPkiConfiguration::privateKeyFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaPkiConfiguration14privateKeyFileEv(
    const QOpcUaPkiConfiguration *self) {
  return new QString(self->privateKeyFile());
}

//  void QOpcUaPkiConfiguration::setPrivateKeyFile(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfiguration17setPrivateKeyFileERK7QString(
    QOpcUaPkiConfiguration *self,
    const QString *value) {
  self->setPrivateKeyFile(*value);
}

//  QString QOpcUaPkiConfiguration::trustListDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaPkiConfiguration18trustListDirectoryEv(
    const QOpcUaPkiConfiguration *self) {
  return new QString(self->trustListDirectory());
}

//  void QOpcUaPkiConfiguration::setTrustListDirectory(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfiguration21setTrustListDirectoryERK7QString(
    QOpcUaPkiConfiguration *self,
    const QString *value) {
  self->setTrustListDirectory(*value);
}

//  QString QOpcUaPkiConfiguration::revocationListDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaPkiConfiguration23revocationListDirectoryEv(
    const QOpcUaPkiConfiguration *self) {
  return new QString(self->revocationListDirectory());
}

//  void QOpcUaPkiConfiguration::setRevocationListDirectory(const QString
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfiguration26setRevocationListDirectoryERK7QString(
    QOpcUaPkiConfiguration *self,
    const QString *value) {
  self->setRevocationListDirectory(*value);
}

//  QString QOpcUaPkiConfiguration::issuerListDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaPkiConfiguration19issuerListDirectoryEv(
    const QOpcUaPkiConfiguration *self) {
  return new QString(self->issuerListDirectory());
}

//  void QOpcUaPkiConfiguration::setIssuerListDirectory(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfiguration22setIssuerListDirectoryERK7QString(
    QOpcUaPkiConfiguration *self,
    const QString *value) {
  self->setIssuerListDirectory(*value);
}

//  QString QOpcUaPkiConfiguration::issuerRevocationListDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QOpcUaPkiConfiguration29issuerRevocationListDirectoryEv(
    const QOpcUaPkiConfiguration *self) {
  return new QString(self->issuerRevocationListDirectory());
}

//  void QOpcUaPkiConfiguration::setIssuerRevocationListDirectory(const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QOpcUaPkiConfiguration32setIssuerRevocationListDirectoryERK7QString(
    QOpcUaPkiConfiguration *self,
    const QString *value) {
  self->setIssuerRevocationListDirectory(*value);
}

//  QOpcUaApplicationIdentity QOpcUaPkiConfiguration::applicationIdentity()
//      const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationIdentity *ritual_ZNK22QOpcUaPkiConfiguration19applicationIdentityEv(
    const QOpcUaPkiConfiguration *self) {
  return new QOpcUaApplicationIdentity(self->applicationIdentity());
}

//  bool QOpcUaPkiConfiguration::isPkiValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QOpcUaPkiConfiguration10isPkiValidEv(
    const QOpcUaPkiConfiguration *self) {
  return self->isPkiValid();
}

//  bool QOpcUaPkiConfiguration::isKeyAndCertificateFileSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QOpcUaPkiConfiguration26isKeyAndCertificateFileSetEv(
    const QOpcUaPkiConfiguration *self) {
  return self->isKeyAndCertificateFileSet();
}
