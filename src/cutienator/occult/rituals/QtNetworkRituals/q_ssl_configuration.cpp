//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslconfiguration.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if !defined(QT_NO_SSL)
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qsslkey.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslellipticcurve.h>
#include <QtNetwork/qssldiffiehellmanparameters.h>
#include <QtCore/qvariant.h>
#include <QtNetwork/qsslkeyingmaterial.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSslConfiguration::QSslConfiguration()
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZN17QSslConfigurationC1Ev() {
  return new QSslConfiguration();
}

//  QSslConfiguration::QSslConfiguration(const QSslConfiguration &other)
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZN17QSslConfigurationC1ERKS_(
    const QSslConfiguration *other) {
  return new QSslConfiguration(*other);
}

//  QSslConfiguration::~QSslConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfigurationD1Ev(QSslConfiguration *self) {
  delete self;
}

//  bool QSslConfiguration::operator==(const QSslConfiguration &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfigurationeqERKS_(
    const QSslConfiguration *self,
    const QSslConfiguration *other) {
  return self->operator==(*other);
}

//  bool QSslConfiguration::operator!=(const QSslConfiguration &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfigurationneERKS_(
    const QSslConfiguration *self,
    const QSslConfiguration *other) {
  return self->operator!=(*other);
}

//  bool QSslConfiguration::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfiguration6isNullEv(const QSslConfiguration *self) {
  return self->isNull();
}

//  QSsl::SslProtocol QSslConfiguration::protocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK17QSslConfiguration8protocolEv(
    const QSslConfiguration *self) {
  return self->protocol();
}

//  void QSslConfiguration::setProtocol(QSsl::SslProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration11setProtocolEN4QSsl11SslProtocolE(
    QSslConfiguration *self,
    QSsl::SslProtocol protocol) {
  self->setProtocol(protocol);
}

//  QSslSocket::PeerVerifyMode QSslConfiguration::peerVerifyMode() const
extern "C" Q_DECL_EXPORT
QSslSocket::PeerVerifyMode ritual_ZNK17QSslConfiguration14peerVerifyModeEv(
    const QSslConfiguration *self) {
  return self->peerVerifyMode();
}

//  void QSslConfiguration::setPeerVerifyMode(QSslSocket::PeerVerifyMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration17setPeerVerifyModeEN10QSslSocket14PeerVerifyModeE(
    QSslConfiguration *self,
    QSslSocket::PeerVerifyMode mode) {
  self->setPeerVerifyMode(mode);
}

//  int QSslConfiguration::peerVerifyDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSslConfiguration15peerVerifyDepthEv(
    const QSslConfiguration *self) {
  return self->peerVerifyDepth();
}

//  void QSslConfiguration::setPeerVerifyDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration18setPeerVerifyDepthEi(
    QSslConfiguration *self,
    int depth) {
  self->setPeerVerifyDepth(depth);
}

//  QList<QSslCertificate> QSslConfiguration::localCertificateChain() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK17QSslConfiguration21localCertificateChainEv(
    const QSslConfiguration *self) {
  return new QList<QSslCertificate>(self->localCertificateChain());
}

//  void QSslConfiguration::setLocalCertificateChain(const
//      QList<QSslCertificate> &localChain)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration24setLocalCertificateChainERK5QListI15QSslCertificateE(
    QSslConfiguration *self,
    const QList<QSslCertificate> *localChain) {
  self->setLocalCertificateChain(*localChain);
}

//  QSslCertificate QSslConfiguration::localCertificate() const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZNK17QSslConfiguration16localCertificateEv(
    const QSslConfiguration *self) {
  return new QSslCertificate(self->localCertificate());
}

//  void QSslConfiguration::setLocalCertificate(const QSslCertificate
//      &certificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration19setLocalCertificateERK15QSslCertificate(
    QSslConfiguration *self,
    const QSslCertificate *certificate) {
  self->setLocalCertificate(*certificate);
}

//  QSslCertificate QSslConfiguration::peerCertificate() const
extern "C" Q_DECL_EXPORT
QSslCertificate *ritual_ZNK17QSslConfiguration15peerCertificateEv(
    const QSslConfiguration *self) {
  return new QSslCertificate(self->peerCertificate());
}

//  QList<QSslCertificate> QSslConfiguration::peerCertificateChain() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK17QSslConfiguration20peerCertificateChainEv(
    const QSslConfiguration *self) {
  return new QList<QSslCertificate>(self->peerCertificateChain());
}

//  QSslCipher QSslConfiguration::sessionCipher() const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZNK17QSslConfiguration13sessionCipherEv(
    const QSslConfiguration *self) {
  return new QSslCipher(self->sessionCipher());
}

//  QSsl::SslProtocol QSslConfiguration::sessionProtocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK17QSslConfiguration15sessionProtocolEv(
    const QSslConfiguration *self) {
  return self->sessionProtocol();
}

//  QSslKey QSslConfiguration::privateKey() const
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZNK17QSslConfiguration10privateKeyEv(
    const QSslConfiguration *self) {
  return new QSslKey(self->privateKey());
}

//  void QSslConfiguration::setPrivateKey(const QSslKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration13setPrivateKeyERK7QSslKey(
    QSslConfiguration *self,
    const QSslKey *key) {
  self->setPrivateKey(*key);
}

//  QList<QSslCipher> QSslConfiguration::ciphers() const
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZNK17QSslConfiguration7ciphersEv(
    const QSslConfiguration *self) {
  return new QList<QSslCipher>(self->ciphers());
}

//  void QSslConfiguration::setCiphers(const QList<QSslCipher> &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration10setCiphersERK5QListI10QSslCipherE(
    QSslConfiguration *self,
    const QList<QSslCipher> *ciphers) {
  self->setCiphers(*ciphers);
}

//  void QSslConfiguration::setCiphers(const QString &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration10setCiphersERK7QString(
    QSslConfiguration *self,
    const QString *ciphers) {
  self->setCiphers(*ciphers);
}

//  QList<QSslCipher> QSslConfiguration::supportedCiphers()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZN17QSslConfiguration16supportedCiphersEv() {
  return new QList<QSslCipher>(QSslConfiguration::supportedCiphers());
}

//  QList<QSslCertificate> QSslConfiguration::caCertificates() const
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZNK17QSslConfiguration14caCertificatesEv(
    const QSslConfiguration *self) {
  return new QList<QSslCertificate>(self->caCertificates());
}

//  void QSslConfiguration::setCaCertificates(const QList<QSslCertificate>
//      &certificates)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration17setCaCertificatesERK5QListI15QSslCertificateE(
    QSslConfiguration *self,
    const QList<QSslCertificate> *certificates) {
  self->setCaCertificates(*certificates);
}

//  bool QSslConfiguration::addCaCertificates(const QString &path,
//      QSsl::EncodingFormat format, QSslCertificate::PatternSyntax syntax)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslConfiguration17addCaCertificatesERK7QStringN4QSsl14EncodingFormatEN15QSslCertificate13PatternSyntaxE(
    QSslConfiguration *self,
    const QString *path,
    QSsl::EncodingFormat format,
    QSslCertificate::PatternSyntax syntax) {
  return self->addCaCertificates(*path, format, syntax);
}

//  void QSslConfiguration::addCaCertificate(const QSslCertificate
//      &certificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration16addCaCertificateERK15QSslCertificate(
    QSslConfiguration *self,
    const QSslCertificate *certificate) {
  self->addCaCertificate(*certificate);
}

//  void QSslConfiguration::addCaCertificates(const QList<QSslCertificate>
//      &certificates)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration17addCaCertificatesERK5QListI15QSslCertificateE(
    QSslConfiguration *self,
    const QList<QSslCertificate> *certificates) {
  self->addCaCertificates(*certificates);
}

//  QList<QSslCertificate> QSslConfiguration::systemCaCertificates()
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN17QSslConfiguration20systemCaCertificatesEv() {
  return new QList<QSslCertificate>(
      QSslConfiguration::systemCaCertificates());
}

//  void QSslConfiguration::setSslOption(QSsl::SslOption option, bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration12setSslOptionEN4QSsl9SslOptionEb(
    QSslConfiguration *self,
    QSsl::SslOption option,
    bool on) {
  self->setSslOption(option, on);
}

//  bool QSslConfiguration::testSslOption(QSsl::SslOption option) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfiguration13testSslOptionEN4QSsl9SslOptionE(
    const QSslConfiguration *self,
    QSsl::SslOption option) {
  return self->testSslOption(option);
}

//  QByteArray QSslConfiguration::sessionTicket() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QSslConfiguration13sessionTicketEv(
    const QSslConfiguration *self) {
  return new QByteArray(self->sessionTicket());
}

//  void QSslConfiguration::setSessionTicket(const QByteArray &sessionTicket)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration16setSessionTicketERK10QByteArray(
    QSslConfiguration *self,
    const QByteArray *sessionTicket) {
  self->setSessionTicket(*sessionTicket);
}

//  int QSslConfiguration::sessionTicketLifeTimeHint() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QSslConfiguration25sessionTicketLifeTimeHintEv(
    const QSslConfiguration *self) {
  return self->sessionTicketLifeTimeHint();
}

//  QSslKey QSslConfiguration::ephemeralServerKey() const
extern "C" Q_DECL_EXPORT
QSslKey *ritual_ZNK17QSslConfiguration18ephemeralServerKeyEv(
    const QSslConfiguration *self) {
  return new QSslKey(self->ephemeralServerKey());
}

//  QList<QSslEllipticCurve> QSslConfiguration::ellipticCurves() const
extern "C" Q_DECL_EXPORT
QList<QSslEllipticCurve> *ritual_ZNK17QSslConfiguration14ellipticCurvesEv(
    const QSslConfiguration *self) {
  return new QList<QSslEllipticCurve>(self->ellipticCurves());
}

//  void QSslConfiguration::setEllipticCurves(const QList<QSslEllipticCurve>
//      &curves)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration17setEllipticCurvesERK5QListI17QSslEllipticCurveE(
    QSslConfiguration *self,
    const QList<QSslEllipticCurve> *curves) {
  self->setEllipticCurves(*curves);
}

//  QList<QSslEllipticCurve> QSslConfiguration::supportedEllipticCurves()
extern "C" Q_DECL_EXPORT
QList<QSslEllipticCurve> *ritual_ZN17QSslConfiguration23supportedEllipticCurvesEv() {
  return new QList<QSslEllipticCurve>(
      QSslConfiguration::supportedEllipticCurves());
}

//  QByteArray QSslConfiguration::preSharedKeyIdentityHint() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QSslConfiguration24preSharedKeyIdentityHintEv(
    const QSslConfiguration *self) {
  return new QByteArray(self->preSharedKeyIdentityHint());
}

//  void QSslConfiguration::setPreSharedKeyIdentityHint(const QByteArray
//      &hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration27setPreSharedKeyIdentityHintERK10QByteArray(
    QSslConfiguration *self,
    const QByteArray *hint) {
  self->setPreSharedKeyIdentityHint(*hint);
}

//  QSslDiffieHellmanParameters QSslConfiguration::diffieHellmanParameters()
//      const
extern "C" Q_DECL_EXPORT
QSslDiffieHellmanParameters *ritual_ZNK17QSslConfiguration23diffieHellmanParametersEv(
    const QSslConfiguration *self) {
  return new QSslDiffieHellmanParameters(self->diffieHellmanParameters());
}

//  void QSslConfiguration::setDiffieHellmanParameters(const
//      QSslDiffieHellmanParameters &dhparams)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration26setDiffieHellmanParametersERK27QSslDiffieHellmanParameters(
    QSslConfiguration *self,
    const QSslDiffieHellmanParameters *dhparams) {
  self->setDiffieHellmanParameters(*dhparams);
}

//  void QSslConfiguration::setBackendConfigurationOption(const QByteArray
//      &name, const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration29setBackendConfigurationOptionERK10QByteArrayRK8QVariant(
    QSslConfiguration *self,
    const QByteArray *name,
    const QVariant *value) {
  self->setBackendConfigurationOption(*name, *value);
}

//  QSslConfiguration QSslConfiguration::defaultConfiguration()
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZN17QSslConfiguration20defaultConfigurationEv() {
  return new QSslConfiguration(QSslConfiguration::defaultConfiguration());
}

//  void QSslConfiguration::setDefaultConfiguration(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration23setDefaultConfigurationERKS_(
    const QSslConfiguration *configuration) {
  QSslConfiguration::setDefaultConfiguration(*configuration);
}

#if QT_CONFIG(dtls) || defined(Q_QDOC)
//  bool QSslConfiguration::dtlsCookieVerificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfiguration29dtlsCookieVerificationEnabledEv(
    const QSslConfiguration *self) {
  return self->dtlsCookieVerificationEnabled();
}
#endif  // QT_CONFIG(dtls) || defined(Q_QDOC)

#if QT_CONFIG(dtls) || defined(Q_QDOC)
//  void QSslConfiguration::setDtlsCookieVerificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration32setDtlsCookieVerificationEnabledEb(
    QSslConfiguration *self,
    bool enable) {
  self->setDtlsCookieVerificationEnabled(enable);
}
#endif  // QT_CONFIG(dtls) || defined(Q_QDOC)

#if QT_CONFIG(dtls) || defined(Q_QDOC)
//  QSslConfiguration QSslConfiguration::defaultDtlsConfiguration()
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZN17QSslConfiguration24defaultDtlsConfigurationEv() {
  return new QSslConfiguration(
      QSslConfiguration::defaultDtlsConfiguration());
}
#endif  // QT_CONFIG(dtls) || defined(Q_QDOC)

#if QT_CONFIG(dtls) || defined(Q_QDOC)
//  void QSslConfiguration::setDefaultDtlsConfiguration(const
//      QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration27setDefaultDtlsConfigurationERKS_(
    const QSslConfiguration *configuration) {
  QSslConfiguration::setDefaultDtlsConfiguration(*configuration);
}
#endif  // QT_CONFIG(dtls) || defined(Q_QDOC)

//  bool QSslConfiguration::handshakeMustInterruptOnError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfiguration29handshakeMustInterruptOnErrorEv(
    const QSslConfiguration *self) {
  return self->handshakeMustInterruptOnError();
}

//  void QSslConfiguration::setHandshakeMustInterruptOnError(bool interrupt)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration32setHandshakeMustInterruptOnErrorEb(
    QSslConfiguration *self,
    bool interrupt) {
  self->setHandshakeMustInterruptOnError(interrupt);
}

//  bool QSslConfiguration::missingCertificateIsFatal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfiguration25missingCertificateIsFatalEv(
    const QSslConfiguration *self) {
  return self->missingCertificateIsFatal();
}

//  void QSslConfiguration::setMissingCertificateIsFatal(bool cannotRecover)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration28setMissingCertificateIsFatalEb(
    QSslConfiguration *self,
    bool cannotRecover) {
  self->setMissingCertificateIsFatal(cannotRecover);
}

//  void QSslConfiguration::setOcspStaplingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration22setOcspStaplingEnabledEb(
    QSslConfiguration *self,
    bool enable) {
  self->setOcspStaplingEnabled(enable);
}

//  bool QSslConfiguration::ocspStaplingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslConfiguration19ocspStaplingEnabledEv(
    const QSslConfiguration *self) {
  return self->ocspStaplingEnabled();
}

//  void QSslConfiguration::setAllowedNextProtocols(const QList<QByteArray>
//      &protocols)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration23setAllowedNextProtocolsERK5QListI10QByteArrayE(
    QSslConfiguration *self,
    const QList<QByteArray> *protocols) {
  self->setAllowedNextProtocols(*protocols);
}

//  QList<QByteArray> QSslConfiguration::allowedNextProtocols() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK17QSslConfiguration20allowedNextProtocolsEv(
    const QSslConfiguration *self) {
  return new QList<QByteArray>(self->allowedNextProtocols());
}

//  QByteArray QSslConfiguration::nextNegotiatedProtocol() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QSslConfiguration22nextNegotiatedProtocolEv(
    const QSslConfiguration *self) {
  return new QByteArray(self->nextNegotiatedProtocol());
}

//  NextProtocolNegotiationStatus
//      QSslConfiguration::nextProtocolNegotiationStatus() const
extern "C" Q_DECL_EXPORT
QSslConfiguration::NextProtocolNegotiationStatus ritual_ZNK17QSslConfiguration29nextProtocolNegotiationStatusEv(
    const QSslConfiguration *self) {
  return self->nextProtocolNegotiationStatus();
}

//  QList<QSslKeyingMaterial> QSslConfiguration::takeKeyingMaterial()
extern "C" Q_DECL_EXPORT
QList<QSslKeyingMaterial> *ritual_ZN17QSslConfiguration18takeKeyingMaterialEv(
    QSslConfiguration *self) {
  return new QList<QSslKeyingMaterial>(self->takeKeyingMaterial());
}

//  void QSslConfiguration::setKeyingMaterial(const QList<QSslKeyingMaterial>
//      &keyMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslConfiguration17setKeyingMaterialERK5QListI18QSslKeyingMaterialE(
    QSslConfiguration *self,
    const QList<QSslKeyingMaterial> *keyMaterial) {
  self->setKeyingMaterial(*keyMaterial);
}

//  QSslConfiguration::QSslConfiguration(QSslConfigurationPrivate *dd)
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZN17QSslConfigurationC1EP24QSslConfigurationPrivate(
    QSslConfigurationPrivate *dd) {
  return new QSslConfiguration(dd);
}

#endif  // !defined(QT_NO_SSL)
