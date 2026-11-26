//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaendpointdescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuaendpointdescription.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaapplicationdescription.h>
#include <QtCore/qbytearray.h>
#include <QtOpcUa/qopcuausertokenpolicy.h>
#include <QtCore/qlist.h>

//  QOpcUaEndpointDescription::QOpcUaEndpointDescription()
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription *ritual_ZN25QOpcUaEndpointDescriptionC1Ev() {
  return new QOpcUaEndpointDescription();
}

//  QOpcUaEndpointDescription::QOpcUaEndpointDescription(const
//      QOpcUaEndpointDescription &a0)
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription *ritual_ZN25QOpcUaEndpointDescriptionC1ERKS_(
    const QOpcUaEndpointDescription *a0) {
  return new QOpcUaEndpointDescription(*a0);
}

//  QOpcUaEndpointDescription &QOpcUaEndpointDescription::operator=(const
//      QOpcUaEndpointDescription &a0)
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription *ritual_ZN25QOpcUaEndpointDescriptionaSERKS_(
    QOpcUaEndpointDescription *self,
    const QOpcUaEndpointDescription *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaEndpointDescription::operator==(const
//      QOpcUaEndpointDescription &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QOpcUaEndpointDescriptioneqERKS_(
    const QOpcUaEndpointDescription *self,
    const QOpcUaEndpointDescription *a0) {
  return self->operator==(*a0);
}

//  QOpcUaEndpointDescription::~QOpcUaEndpointDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescriptionD1Ev(
    QOpcUaEndpointDescription *self) {
  delete self;
}

//  QString QOpcUaEndpointDescription::endpointUrl() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaEndpointDescription11endpointUrlEv(
    const QOpcUaEndpointDescription *self) {
  return new QString(self->endpointUrl());
}

//  void QOpcUaEndpointDescription::setEndpointUrl(const QString
//      &endpointUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription14setEndpointUrlERK7QString(
    QOpcUaEndpointDescription *self,
    const QString *endpointUrl) {
  self->setEndpointUrl(*endpointUrl);
}

//  QOpcUaApplicationDescription QOpcUaEndpointDescription::server() const
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription *ritual_ZNK25QOpcUaEndpointDescription6serverEv(
    const QOpcUaEndpointDescription *self) {
  return new QOpcUaApplicationDescription(self->server());
}

//  QOpcUaApplicationDescription &QOpcUaEndpointDescription::serverRef()
extern "C" Q_DECL_EXPORT
QOpcUaApplicationDescription *ritual_ZN25QOpcUaEndpointDescription9serverRefEv(
    QOpcUaEndpointDescription *self) {
  return &(self->serverRef());
}

//  void QOpcUaEndpointDescription::setServer(const
//      QOpcUaApplicationDescription &server)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription9setServerERK28QOpcUaApplicationDescription(
    QOpcUaEndpointDescription *self,
    const QOpcUaApplicationDescription *server) {
  self->setServer(*server);
}

//  QByteArray QOpcUaEndpointDescription::serverCertificate() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK25QOpcUaEndpointDescription17serverCertificateEv(
    const QOpcUaEndpointDescription *self) {
  return new QByteArray(self->serverCertificate());
}

//  void QOpcUaEndpointDescription::setServerCertificate(const QByteArray
//      &serverCertificate)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription20setServerCertificateERK10QByteArray(
    QOpcUaEndpointDescription *self,
    const QByteArray *serverCertificate) {
  self->setServerCertificate(*serverCertificate);
}

//  QOpcUaEndpointDescription::MessageSecurityMode
//      QOpcUaEndpointDescription::securityMode() const
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription::MessageSecurityMode ritual_ZNK25QOpcUaEndpointDescription12securityModeEv(
    const QOpcUaEndpointDescription *self) {
  return self->securityMode();
}

//  void QOpcUaEndpointDescription::setSecurityMode(QOpcUaEndpointDescription
//      ::MessageSecurityMode securityMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription15setSecurityModeENS_19MessageSecurityModeE(
    QOpcUaEndpointDescription *self,
    QOpcUaEndpointDescription::MessageSecurityMode securityMode) {
  self->setSecurityMode(securityMode);
}

//  QString QOpcUaEndpointDescription::securityPolicy() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaEndpointDescription14securityPolicyEv(
    const QOpcUaEndpointDescription *self) {
  return new QString(self->securityPolicy());
}

//  void QOpcUaEndpointDescription::setSecurityPolicy(const QString
//      &securityPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription17setSecurityPolicyERK7QString(
    QOpcUaEndpointDescription *self,
    const QString *securityPolicy) {
  self->setSecurityPolicy(*securityPolicy);
}

//  QList<QOpcUaUserTokenPolicy>
//      QOpcUaEndpointDescription::userIdentityTokens() const
extern "C" Q_DECL_EXPORT
QList<QOpcUaUserTokenPolicy> *ritual_ZNK25QOpcUaEndpointDescription18userIdentityTokensEv(
    const QOpcUaEndpointDescription *self) {
  return new QList<QOpcUaUserTokenPolicy>(self->userIdentityTokens());
}

//  QList<QOpcUaUserTokenPolicy>
//      &QOpcUaEndpointDescription::userIdentityTokensRef()
extern "C" Q_DECL_EXPORT
QList<QOpcUaUserTokenPolicy> *ritual_ZN25QOpcUaEndpointDescription21userIdentityTokensRefEv(
    QOpcUaEndpointDescription *self) {
  return &(self->userIdentityTokensRef());
}

//  void QOpcUaEndpointDescription::setUserIdentityTokens(const
//      QList<QOpcUaUserTokenPolicy> &userIdentityTokens)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription21setUserIdentityTokensERK5QListI21QOpcUaUserTokenPolicyE(
    QOpcUaEndpointDescription *self,
    const QList<QOpcUaUserTokenPolicy> *userIdentityTokens) {
  self->setUserIdentityTokens(*userIdentityTokens);
}

//  QString QOpcUaEndpointDescription::transportProfileUri() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QOpcUaEndpointDescription19transportProfileUriEv(
    const QOpcUaEndpointDescription *self) {
  return new QString(self->transportProfileUri());
}

//  void QOpcUaEndpointDescription::setTransportProfileUri(const QString
//      &transportProfileUri)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription22setTransportProfileUriERK7QString(
    QOpcUaEndpointDescription *self,
    const QString *transportProfileUri) {
  self->setTransportProfileUri(*transportProfileUri);
}

//  quint8 QOpcUaEndpointDescription::securityLevel() const
extern "C" Q_DECL_EXPORT
quint8 ritual_ZNK25QOpcUaEndpointDescription13securityLevelEv(
    const QOpcUaEndpointDescription *self) {
  return self->securityLevel();
}

//  void QOpcUaEndpointDescription::setSecurityLevel(quint8 securityLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QOpcUaEndpointDescription16setSecurityLevelEh(
    QOpcUaEndpointDescription *self,
    quint8 securityLevel) {
  self->setSecurityLevel(securityLevel);
}

//  QList<QOpcUaEndpointDescription>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaEndpointDescription> *ritual_list_make_QOpcUaEndpointDescription() {
  return new QList<QOpcUaEndpointDescription>();
}

//  void QList<QOpcUaEndpointDescription>::append(const
//      QOpcUaEndpointDescription &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaEndpointDescription(
    QList<QOpcUaEndpointDescription> *self,
    const QOpcUaEndpointDescription *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaEndpointDescription>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaEndpointDescription(
    const QList<QOpcUaEndpointDescription> *self) {
  return self->size();
}

//  const QOpcUaEndpointDescription
//      &QList<QOpcUaEndpointDescription>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaEndpointDescription *ritual_list_at_QOpcUaEndpointDescription(
    const QList<QOpcUaEndpointDescription> *self,
    long long index) {
  return new QOpcUaEndpointDescription(self->at(index));
}

//  QList<QOpcUaEndpointDescription>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaEndpointDescription(
    QList<QOpcUaEndpointDescription> *self) {
  delete self;
}
