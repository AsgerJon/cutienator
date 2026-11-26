//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaauthenticationinformation.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtOpcUa/qopcuaauthenticationinformation.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  QOpcUaAuthenticationInformation::QOpcUaAuthenticationInformation()
extern "C" Q_DECL_EXPORT
QOpcUaAuthenticationInformation *ritual_ZN31QOpcUaAuthenticationInformationC1Ev() {
  return new QOpcUaAuthenticationInformation();
}

//  QOpcUaAuthenticationInformation::QOpcUaAuthenticationInformation(const
//      QOpcUaAuthenticationInformation &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAuthenticationInformation *ritual_ZN31QOpcUaAuthenticationInformationC1ERKS_(
    const QOpcUaAuthenticationInformation *a0) {
  return new QOpcUaAuthenticationInformation(*a0);
}

//  QOpcUaAuthenticationInformation
//      &QOpcUaAuthenticationInformation::operator=(const
//      QOpcUaAuthenticationInformation &a0)
extern "C" Q_DECL_EXPORT
QOpcUaAuthenticationInformation *ritual_ZN31QOpcUaAuthenticationInformationaSERKS_(
    QOpcUaAuthenticationInformation *self,
    const QOpcUaAuthenticationInformation *a0) {
  return &(self->operator=(*a0));
}

//  bool QOpcUaAuthenticationInformation::operator==(const
//      QOpcUaAuthenticationInformation &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK31QOpcUaAuthenticationInformationeqERKS_(
    const QOpcUaAuthenticationInformation *self,
    const QOpcUaAuthenticationInformation *rhs) {
  return self->operator==(*rhs);
}

//  QOpcUaAuthenticationInformation::~QOpcUaAuthenticationInformation()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaAuthenticationInformationD1Ev(
    QOpcUaAuthenticationInformation *self) {
  delete self;
}

//  void QOpcUaAuthenticationInformation::setAnonymousAuthentication()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaAuthenticationInformation26setAnonymousAuthenticationEv(
    QOpcUaAuthenticationInformation *self) {
  self->setAnonymousAuthentication();
}

//  void QOpcUaAuthenticationInformation::setUsernameAuthentication(const
//      QString &username, const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaAuthenticationInformation25setUsernameAuthenticationERK7QStringS2_(
    QOpcUaAuthenticationInformation *self,
    const QString *username,
    const QString *password) {
  self->setUsernameAuthentication(*username, *password);
}

//  void QOpcUaAuthenticationInformation::setCertificateAuthentication()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaAuthenticationInformation28setCertificateAuthenticationEv(
    QOpcUaAuthenticationInformation *self) {
  self->setCertificateAuthentication();
}

//  void QOpcUaAuthenticationInformation::setCertificateAuthentication(const
//      QString &certificatePath, const QString &privateKeyPath)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QOpcUaAuthenticationInformation28setCertificateAuthenticationERK7QStringS2_(
    QOpcUaAuthenticationInformation *self,
    const QString *certificatePath,
    const QString *privateKeyPath) {
  self->setCertificateAuthentication(*certificatePath, *privateKeyPath);
}

//  const QVariant &QOpcUaAuthenticationInformation::authenticationData()
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK31QOpcUaAuthenticationInformation18authenticationDataEv(
    const QOpcUaAuthenticationInformation *self) {
  return new QVariant(self->authenticationData());
}

//  QOpcUaUserTokenPolicy::TokenType
//      QOpcUaAuthenticationInformation::authenticationType() const
extern "C" Q_DECL_EXPORT
QOpcUaUserTokenPolicy::TokenType ritual_ZNK31QOpcUaAuthenticationInformation18authenticationTypeEv(
    const QOpcUaAuthenticationInformation *self) {
  return self->authenticationType();
}
