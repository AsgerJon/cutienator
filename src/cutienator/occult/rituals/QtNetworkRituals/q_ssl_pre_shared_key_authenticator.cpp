//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qsslpresharedkeyauthenticator.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslpresharedkeyauthenticator.h>
#include <QtCore/qbytearray.h>

//  QSslPreSharedKeyAuthenticator::QSslPreSharedKeyAuthenticator()
extern "C" Q_DECL_EXPORT
QSslPreSharedKeyAuthenticator *ritual_ZN29QSslPreSharedKeyAuthenticatorC1Ev() {
  return new QSslPreSharedKeyAuthenticator();
}

//  QSslPreSharedKeyAuthenticator::~QSslPreSharedKeyAuthenticator()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSslPreSharedKeyAuthenticatorD1Ev(
    QSslPreSharedKeyAuthenticator *self) {
  delete self;
}

//  QSslPreSharedKeyAuthenticator::QSslPreSharedKeyAuthenticator(const
//      QSslPreSharedKeyAuthenticator &authenticator)
extern "C" Q_DECL_EXPORT
QSslPreSharedKeyAuthenticator *ritual_ZN29QSslPreSharedKeyAuthenticatorC1ERKS_(
    const QSslPreSharedKeyAuthenticator *authenticator) {
  return new QSslPreSharedKeyAuthenticator(*authenticator);
}

//  QSslPreSharedKeyAuthenticator
//      &QSslPreSharedKeyAuthenticator::operator=(const
//      QSslPreSharedKeyAuthenticator &authenticator)
extern "C" Q_DECL_EXPORT
QSslPreSharedKeyAuthenticator *ritual_ZN29QSslPreSharedKeyAuthenticatoraSERKS_(
    QSslPreSharedKeyAuthenticator *self,
    const QSslPreSharedKeyAuthenticator *authenticator) {
  return &(self->operator=(*authenticator));
}

//  QSslPreSharedKeyAuthenticator
//      &QSslPreSharedKeyAuthenticator::operator=(QSslPreSharedKeyAuthenticat
//      or &&other)
extern "C" Q_DECL_EXPORT
QSslPreSharedKeyAuthenticator *ritual_ZN29QSslPreSharedKeyAuthenticatoraSEOS_(
    QSslPreSharedKeyAuthenticator *self,
    QSslPreSharedKeyAuthenticator *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QSslPreSharedKeyAuthenticator::swap(QSslPreSharedKeyAuthenticator
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSslPreSharedKeyAuthenticator4swapERS_(
    QSslPreSharedKeyAuthenticator *self,
    QSslPreSharedKeyAuthenticator *other) {
  self->swap(*other);
}

//  QByteArray QSslPreSharedKeyAuthenticator::identityHint() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK29QSslPreSharedKeyAuthenticator12identityHintEv(
    const QSslPreSharedKeyAuthenticator *self) {
  return new QByteArray(self->identityHint());
}

//  void QSslPreSharedKeyAuthenticator::setIdentity(const QByteArray
//      &identity)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSslPreSharedKeyAuthenticator11setIdentityERK10QByteArray(
    QSslPreSharedKeyAuthenticator *self,
    const QByteArray *identity) {
  self->setIdentity(*identity);
}

//  QByteArray QSslPreSharedKeyAuthenticator::identity() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK29QSslPreSharedKeyAuthenticator8identityEv(
    const QSslPreSharedKeyAuthenticator *self) {
  return new QByteArray(self->identity());
}

//  int QSslPreSharedKeyAuthenticator::maximumIdentityLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QSslPreSharedKeyAuthenticator21maximumIdentityLengthEv(
    const QSslPreSharedKeyAuthenticator *self) {
  return self->maximumIdentityLength();
}

//  void QSslPreSharedKeyAuthenticator::setPreSharedKey(const QByteArray
//      &preSharedKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QSslPreSharedKeyAuthenticator15setPreSharedKeyERK10QByteArray(
    QSslPreSharedKeyAuthenticator *self,
    const QByteArray *preSharedKey) {
  self->setPreSharedKey(*preSharedKey);
}

//  QByteArray QSslPreSharedKeyAuthenticator::preSharedKey() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK29QSslPreSharedKeyAuthenticator12preSharedKeyEv(
    const QSslPreSharedKeyAuthenticator *self) {
  return new QByteArray(self->preSharedKey());
}

//  int QSslPreSharedKeyAuthenticator::maximumPreSharedKeyLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QSslPreSharedKeyAuthenticator25maximumPreSharedKeyLengthEv(
    const QSslPreSharedKeyAuthenticator *self) {
  return self->maximumPreSharedKeyLength();
}

//  bool QSslPreSharedKeyAuthenticator::isEqual(const
//      QSslPreSharedKeyAuthenticator &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QSslPreSharedKeyAuthenticator7isEqualERKS_(
    const QSslPreSharedKeyAuthenticator *self,
    const QSslPreSharedKeyAuthenticator *other) {
  return self->isEqual(*other);
}

//  bool operator==(const QSslPreSharedKeyAuthenticator &lhs, const
//      QSslPreSharedKeyAuthenticator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK29QSslPreSharedKeyAuthenticatorS1_(
    const QSslPreSharedKeyAuthenticator *lhs,
    const QSslPreSharedKeyAuthenticator *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSslPreSharedKeyAuthenticator &lhs, const
//      QSslPreSharedKeyAuthenticator &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK29QSslPreSharedKeyAuthenticatorS1_(
    const QSslPreSharedKeyAuthenticator *lhs,
    const QSslPreSharedKeyAuthenticator *rhs) {
  return operator!=(*lhs, *rhs);
}

#endif  // QT_CONFIG(ssl)
#endif  // QT_CONFIG(ssl)
