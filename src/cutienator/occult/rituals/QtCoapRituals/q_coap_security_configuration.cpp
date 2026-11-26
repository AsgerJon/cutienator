//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapsecurityconfiguration.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCoap/qcoapsecurityconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qlist.h>

//  QCoapSecurityConfiguration::QCoapSecurityConfiguration()
extern "C" Q_DECL_EXPORT
QCoapSecurityConfiguration *ritual_ZN26QCoapSecurityConfigurationC1Ev() {
  return new QCoapSecurityConfiguration();
}

//  QCoapSecurityConfiguration::QCoapSecurityConfiguration(const
//      QCoapSecurityConfiguration &other)
extern "C" Q_DECL_EXPORT
QCoapSecurityConfiguration *ritual_ZN26QCoapSecurityConfigurationC1ERKS_(
    const QCoapSecurityConfiguration *other) {
  return new QCoapSecurityConfiguration(*other);
}

//  QCoapSecurityConfiguration::~QCoapSecurityConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfigurationD1Ev(
    QCoapSecurityConfiguration *self) {
  delete self;
}

//  QCoapSecurityConfiguration::QCoapSecurityConfiguration(QCoapSecurityConfi
//      guration &&other)
extern "C" Q_DECL_EXPORT
QCoapSecurityConfiguration *ritual_ZN26QCoapSecurityConfigurationC1EOS_(
    QCoapSecurityConfiguration *other) {
  return new QCoapSecurityConfiguration(std::move(*other));
}

//  QCoapSecurityConfiguration
//      &QCoapSecurityConfiguration::operator=(QCoapSecurityConfiguration
//      &&other)
extern "C" Q_DECL_EXPORT
QCoapSecurityConfiguration *ritual_ZN26QCoapSecurityConfigurationaSEOS_(
    QCoapSecurityConfiguration *self,
    QCoapSecurityConfiguration *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCoapSecurityConfiguration &QCoapSecurityConfiguration::operator=(const
//      QCoapSecurityConfiguration &other)
extern "C" Q_DECL_EXPORT
QCoapSecurityConfiguration *ritual_ZN26QCoapSecurityConfigurationaSERKS_(
    QCoapSecurityConfiguration *self,
    const QCoapSecurityConfiguration *other) {
  return &(self->operator=(*other));
}

//  void QCoapSecurityConfiguration::swap(QCoapSecurityConfiguration &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration4swapERS_(
    QCoapSecurityConfiguration *self,
    QCoapSecurityConfiguration *other) {
  self->swap(*other);
}

//  void QCoapSecurityConfiguration::setPreSharedKeyIdentity(const QByteArray
//      &preSharedKeyIdentity)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration23setPreSharedKeyIdentityERK10QByteArray(
    QCoapSecurityConfiguration *self,
    const QByteArray *preSharedKeyIdentity) {
  self->setPreSharedKeyIdentity(*preSharedKeyIdentity);
}

//  QByteArray QCoapSecurityConfiguration::preSharedKeyIdentity() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QCoapSecurityConfiguration20preSharedKeyIdentityEv(
    const QCoapSecurityConfiguration *self) {
  return new QByteArray(self->preSharedKeyIdentity());
}

//  void QCoapSecurityConfiguration::setPreSharedKey(const QByteArray
//      &preSharedKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration15setPreSharedKeyERK10QByteArray(
    QCoapSecurityConfiguration *self,
    const QByteArray *preSharedKey) {
  self->setPreSharedKey(*preSharedKey);
}

//  QByteArray QCoapSecurityConfiguration::preSharedKey() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK26QCoapSecurityConfiguration12preSharedKeyEv(
    const QCoapSecurityConfiguration *self) {
  return new QByteArray(self->preSharedKey());
}

//  void QCoapSecurityConfiguration::setDefaultCipherString(const QString
//      &cipherString)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration22setDefaultCipherStringERK7QString(
    QCoapSecurityConfiguration *self,
    const QString *cipherString) {
  self->setDefaultCipherString(*cipherString);
}

//  QString QCoapSecurityConfiguration::defaultCipherString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QCoapSecurityConfiguration19defaultCipherStringEv(
    const QCoapSecurityConfiguration *self) {
  return new QString(self->defaultCipherString());
}

//  void QCoapSecurityConfiguration::setCaCertificates(const
//      QList<QSslCertificate> &certificates)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration17setCaCertificatesERK5QListI15QSslCertificateE(
    QCoapSecurityConfiguration *self,
    const QList<QSslCertificate> *certificates) {
  self->setCaCertificates(*certificates);
}

//  QList<QSslCertificate> QCoapSecurityConfiguration::caCertificates() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK26QCoapSecurityConfiguration14caCertificatesEv(
    const QCoapSecurityConfiguration *self) {
  return new QList<QSslCertificate>(self->caCertificates());
}

//  void QCoapSecurityConfiguration::setLocalCertificateChain(const
//      QList<QSslCertificate> &localChain)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration24setLocalCertificateChainERK5QListI15QSslCertificateE(
    QCoapSecurityConfiguration *self,
    const QList<QSslCertificate> *localChain) {
  self->setLocalCertificateChain(*localChain);
}

//  QList<QSslCertificate>
//      QCoapSecurityConfiguration::localCertificateChain() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK26QCoapSecurityConfiguration21localCertificateChainEv(
    const QCoapSecurityConfiguration *self) {
  return new QList<QSslCertificate>(self->localCertificateChain());
}

//  void QCoapSecurityConfiguration::setPrivateKey(const QCoapPrivateKey
//      &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCoapSecurityConfiguration13setPrivateKeyERK15QCoapPrivateKey(
    QCoapSecurityConfiguration *self,
    const QCoapPrivateKey *key) {
  self->setPrivateKey(*key);
}

//  QCoapPrivateKey QCoapSecurityConfiguration::privateKey() const
extern "C" Q_DECL_EXPORT
QCoapPrivateKey *ritual_ZNK26QCoapSecurityConfiguration10privateKeyEv(
    const QCoapSecurityConfiguration *self) {
  return new QCoapPrivateKey(self->privateKey());
}
