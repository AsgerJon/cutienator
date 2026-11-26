//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQmlNetwork/qtqmlnetworkexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(qml_ssl)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlNetwork/QtQmlNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#if QT_CONFIG(qml_ssl)
#include <QtQmlNetwork/QtQmlNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlNetwork/6.12.0/QtQmlNetwork/private/qqmlsslkey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qlist.h>
#include <QtCore/QList>
#include <QtNetwork/QSsl>

//  void QQmlSslConfiguration::setCertificateFiles(const QStringList
//      &certificateFiles)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration19setCertificateFilesERK5QListI7QStringE(
    QQmlSslConfiguration *self,
    const QList<QString> *certificateFiles) {
  self->setCertificateFiles(*certificateFiles);
}

//  void QQmlSslConfiguration::setPrivateKey(const QQmlSslKey &privateKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration13setPrivateKeyERK10QQmlSslKey(
    QQmlSslConfiguration *self,
    const QQmlSslKey *privateKey) {
  self->setPrivateKey(*privateKey);
}

//  QString QQmlSslConfiguration::ciphers() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlSslConfiguration7ciphersEv(
    const QQmlSslConfiguration *self) {
  return new QString(self->ciphers());
}

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 11)
//  QList<QSsl::SslOption> QQmlSslConfiguration::sslOptions() const
extern "C" Q_DECL_EXPORT
QList<QSsl::SslOption> *ritual_ZNK20QQmlSslConfiguration10sslOptionsEv(
    const QQmlSslConfiguration *self) {
  return new QList<QSsl::SslOption>(self->sslOptions());
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 11)

//  QSsl::SslProtocol QQmlSslConfiguration::protocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK20QQmlSslConfiguration8protocolEv(
    const QQmlSslConfiguration *self) {
  return self->protocol();
}

//  QSslSocket::PeerVerifyMode QQmlSslConfiguration::peerVerifyMode() const
extern "C" Q_DECL_EXPORT
QSslSocket::PeerVerifyMode ritual_ZNK20QQmlSslConfiguration14peerVerifyModeEv(
    const QQmlSslConfiguration *self) {
  return self->peerVerifyMode();
}

//  int QQmlSslConfiguration::peerVerifyDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlSslConfiguration15peerVerifyDepthEv(
    const QQmlSslConfiguration *self) {
  return self->peerVerifyDepth();
}

//  QByteArray QQmlSslConfiguration::sessionTicket() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QQmlSslConfiguration13sessionTicketEv(
    const QQmlSslConfiguration *self) {
  return new QByteArray(self->sessionTicket());
}

//  QSsl::SslOptions QQmlSslConfiguration::sslOptionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QQmlSslConfiguration14sslOptionFlagsEv(
    const QQmlSslConfiguration *self) {
  return static_cast<int>(self->sslOptionFlags().toInt());
}

//  const QSslConfiguration QQmlSslConfiguration::configuration()
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZN20QQmlSslConfiguration13configurationEv(
    QQmlSslConfiguration *self) {
  return new QSslConfiguration(self->configuration());
}

//  void QQmlSslConfiguration::setProtocol(QSsl::SslProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration11setProtocolEN4QSsl11SslProtocolE(
    QQmlSslConfiguration *self,
    QSsl::SslProtocol protocol) {
  self->setProtocol(protocol);
}

//  void QQmlSslConfiguration::setPeerVerifyMode(QSslSocket::PeerVerifyMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration17setPeerVerifyModeEN10QSslSocket14PeerVerifyModeE(
    QQmlSslConfiguration *self,
    QSslSocket::PeerVerifyMode mode) {
  self->setPeerVerifyMode(mode);
}

//  void QQmlSslConfiguration::setPeerVerifyDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration18setPeerVerifyDepthEi(
    QQmlSslConfiguration *self,
    int depth) {
  self->setPeerVerifyDepth(depth);
}

//  void QQmlSslConfiguration::setCiphers(const QString &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration10setCiphersERK7QString(
    QQmlSslConfiguration *self,
    const QString *ciphers) {
  self->setCiphers(*ciphers);
}

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 11)
//  void QQmlSslConfiguration::setSslOptions(const QList<QSsl::SslOption>
//      &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration13setSslOptionsERK5QListIN4QSsl9SslOptionEE(
    QQmlSslConfiguration *self,
    const QList<QSsl::SslOption> *options) {
  self->setSslOptions(*options);
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 11)

//  void QQmlSslConfiguration::setSessionTicket(const QByteArray
//      &sessionTicket)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration16setSessionTicketERK10QByteArray(
    QQmlSslConfiguration *self,
    const QByteArray *sessionTicket) {
  self->setSessionTicket(*sessionTicket);
}

//  void QQmlSslConfiguration::setSslOptionFlags(QSsl::SslOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration17setSslOptionFlagsE6QFlagsIN4QSsl9SslOptionEE(
    QQmlSslConfiguration *self,
    int options) {
  self->setSslOptionFlags(QFlags<QSsl::SslOption>::fromInt(options));
}

//  bool operator==(const QQmlSslConfiguration &lval, const
//      QQmlSslConfiguration &rval)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK20QQmlSslConfigurationS1_(
    const QQmlSslConfiguration *lval,
    const QQmlSslConfiguration *rval) {
  return operator==(*lval, *rval);
}

//  bool operator!=(const QQmlSslConfiguration &lval, const
//      QQmlSslConfiguration &rval)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK20QQmlSslConfigurationS1_(
    const QQmlSslConfiguration *lval,
    const QQmlSslConfiguration *rval) {
  return operator!=(*lval, *rval);
}

#if QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 11)
//  void QQmlSslConfiguration::setSslOptionsList(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration17setSslOptionsListERK17QSslConfiguration(
    QQmlSslConfiguration *self,
    const QSslConfiguration *configuration) {
  self->setSslOptionsList(*configuration);
}
#endif  // QT_REMOVAL_QT7_DEPRECATED_SINCE(6, 11)

//  void QQmlSslConfiguration::setCiphersList(const QSslConfiguration
//      &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfiguration14setCiphersListERK17QSslConfiguration(
    QQmlSslConfiguration *self,
    const QSslConfiguration *configuration) {
  self->setCiphersList(*configuration);
}

//  QQmlSslConfiguration::~QQmlSslConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlSslConfigurationD1Ev(QQmlSslConfiguration *self) {
  delete self;
}

//  a QList<QSsl::SslOption> a ritual of QQmlSslConfiguration gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlSslConfiguration__QList_QSsl_SslOption(
    QList<QSsl::SslOption> *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_ssl)
