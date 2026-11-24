//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuausertokenpolicy.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuausertokenpolicy.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QOpcUaUserTokenPolicy::QOpcUaUserTokenPolicy()
extern "C" Q_DECL_EXPORT
QOpcUaUserTokenPolicy *ritual_ZN21QOpcUaUserTokenPolicyC1Ev() {
  return new QOpcUaUserTokenPolicy();
}

//  QOpcUaUserTokenPolicy::QOpcUaUserTokenPolicy(const QOpcUaUserTokenPolicy
//      &a0)
extern "C" Q_DECL_EXPORT
QOpcUaUserTokenPolicy *ritual_ZN21QOpcUaUserTokenPolicyC1ERKS_(
    const QOpcUaUserTokenPolicy *a0) {
  return new QOpcUaUserTokenPolicy(*a0);
}

//  bool QOpcUaUserTokenPolicy::operator==(const QOpcUaUserTokenPolicy &a0)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QOpcUaUserTokenPolicyeqERKS_(
    const QOpcUaUserTokenPolicy *self,
    const QOpcUaUserTokenPolicy *a0) {
  return self->operator==(*a0);
}

//  QOpcUaUserTokenPolicy::~QOpcUaUserTokenPolicy()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaUserTokenPolicyD1Ev(QOpcUaUserTokenPolicy *self) {
  delete self;
}

//  QString QOpcUaUserTokenPolicy::policyId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QOpcUaUserTokenPolicy8policyIdEv(
    const QOpcUaUserTokenPolicy *self) {
  return new QString(self->policyId());
}

//  void QOpcUaUserTokenPolicy::setPolicyId(const QString &policyId)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaUserTokenPolicy11setPolicyIdERK7QString(
    QOpcUaUserTokenPolicy *self,
    const QString *policyId) {
  self->setPolicyId(*policyId);
}

//  QOpcUaUserTokenPolicy::TokenType QOpcUaUserTokenPolicy::tokenType() const
extern "C" Q_DECL_EXPORT
QOpcUaUserTokenPolicy::TokenType ritual_ZNK21QOpcUaUserTokenPolicy9tokenTypeEv(
    const QOpcUaUserTokenPolicy *self) {
  return self->tokenType();
}

//  void QOpcUaUserTokenPolicy::setTokenType(QOpcUaUserTokenPolicy::TokenType
//      tokenType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaUserTokenPolicy12setTokenTypeENS_9TokenTypeE(
    QOpcUaUserTokenPolicy *self,
    QOpcUaUserTokenPolicy::TokenType tokenType) {
  self->setTokenType(tokenType);
}

//  QString QOpcUaUserTokenPolicy::issuedTokenType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QOpcUaUserTokenPolicy15issuedTokenTypeEv(
    const QOpcUaUserTokenPolicy *self) {
  return new QString(self->issuedTokenType());
}

//  void QOpcUaUserTokenPolicy::setIssuedTokenType(const QString
//      &issuedTokenType)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaUserTokenPolicy18setIssuedTokenTypeERK7QString(
    QOpcUaUserTokenPolicy *self,
    const QString *issuedTokenType) {
  self->setIssuedTokenType(*issuedTokenType);
}

//  QString QOpcUaUserTokenPolicy::issuerEndpointUrl() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QOpcUaUserTokenPolicy17issuerEndpointUrlEv(
    const QOpcUaUserTokenPolicy *self) {
  return new QString(self->issuerEndpointUrl());
}

//  void QOpcUaUserTokenPolicy::setIssuerEndpointUrl(const QString
//      &issuerEndpointUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaUserTokenPolicy20setIssuerEndpointUrlERK7QString(
    QOpcUaUserTokenPolicy *self,
    const QString *issuerEndpointUrl) {
  self->setIssuerEndpointUrl(*issuerEndpointUrl);
}

//  QString QOpcUaUserTokenPolicy::securityPolicy() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QOpcUaUserTokenPolicy14securityPolicyEv(
    const QOpcUaUserTokenPolicy *self) {
  return new QString(self->securityPolicy());
}

//  void QOpcUaUserTokenPolicy::setSecurityPolicy(const QString
//      &securityPolicy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QOpcUaUserTokenPolicy17setSecurityPolicyERK7QString(
    QOpcUaUserTokenPolicy *self,
    const QString *securityPolicy) {
  self->setSecurityPolicy(*securityPolicy);
}

//  QList<QOpcUaUserTokenPolicy>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaUserTokenPolicy> *ritual_list_make_QOpcUaUserTokenPolicy() {
  return new QList<QOpcUaUserTokenPolicy>();
}

//  void QList<QOpcUaUserTokenPolicy>::append(const QOpcUaUserTokenPolicy
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaUserTokenPolicy(
    QList<QOpcUaUserTokenPolicy> *self,
    const QOpcUaUserTokenPolicy *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaUserTokenPolicy>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaUserTokenPolicy(
    const QList<QOpcUaUserTokenPolicy> *self) {
  return self->size();
}

//  const QOpcUaUserTokenPolicy &QList<QOpcUaUserTokenPolicy>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QOpcUaUserTokenPolicy *ritual_list_at_QOpcUaUserTokenPolicy(
    const QList<QOpcUaUserTokenPolicy> *self,
    long long index) {
  return new QOpcUaUserTokenPolicy(self->at(index));
}

//  QList<QOpcUaUserTokenPolicy>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaUserTokenPolicy(
    QList<QOpcUaUserTokenPolicy> *self) {
  delete self;
}
