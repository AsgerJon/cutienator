//  Written by dev_tooling.RitualGenerator from the records of QtNetwork/6.12
//  .0/QtNetwork/private/qnetworkaccessauthenticationmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkaccessauthenticationmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QNetworkAuthenticationCredential::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QNetworkAuthenticationCredential6isNullEv(
    const QNetworkAuthenticationCredential *self) {
  return self->isNull();
}

//  QNetworkAuthenticationCredential::~QNetworkAuthenticationCredential()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QNetworkAuthenticationCredentialD1Ev(
    QNetworkAuthenticationCredential *self) {
  delete self;
}
