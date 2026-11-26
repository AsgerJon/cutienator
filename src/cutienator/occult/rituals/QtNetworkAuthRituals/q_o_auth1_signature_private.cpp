//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth1signature_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth1signature_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/qoauth1signature.h>
#include <QtNetworkAuth/private/qoauth1signature_p.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmessageauthenticationcode.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtnetworkauth/src/oauth/qoauth1signature.cpp, line 71, as _ZN23QOAuth1SignaturePrivateC1ERK4QUrlN16QOAuth1Signature17HttpRequestMethodERK9QMultiMapI7QString8QVariantERKS6_SC_
inline QOAuth1SignaturePrivate::QOAuth1SignaturePrivate(const QUrl &url,
                                                 QOAuth1Signature::HttpRequestMethod method,
                                                 const QMultiMap<QString, QVariant> &parameters,
                                                 const QString &clientSharedKey,
                                                 const QString &tokenSecret) :
    method(method), url(url), clientSharedKey(clientSharedKey), tokenSecret(tokenSecret),
    parameters(parameters)
{}

//  from ../qtnetworkauth/src/oauth/qoauth1signature.cpp, line 127, as _ZNK23QOAuth1SignaturePrivate6secretEv
inline QByteArray QOAuth1SignaturePrivate::secret() const
{
    QByteArray secret;
    secret.append(QUrl::toPercentEncoding(clientSharedKey));
    secret.append('&');
    secret.append(QUrl::toPercentEncoding(tokenSecret));
    return secret;
}
//  -----------------------------------------------------------------------

//  QOAuth1SignaturePrivate::QOAuth1SignaturePrivate()
extern "C" Q_DECL_EXPORT
QOAuth1SignaturePrivate *ritual_ZN23QOAuth1SignaturePrivateC1Ev() {
  return new QOAuth1SignaturePrivate();
}

//  QOAuth1SignaturePrivate::QOAuth1SignaturePrivate(const QUrl &url,
//      QOAuth1Signature::HttpRequestMethod method, const QMultiMap<QString,
//      QVariant> &parameters, const QString &clientSharedKey, const QString
//      &tokenSecret)
extern "C" Q_DECL_EXPORT
QOAuth1SignaturePrivate *ritual_ZN23QOAuth1SignaturePrivateC1ERK4QUrlN16QOAuth1Signature17HttpRequestMethodERK9QMultiMapI7QString8QVariantERKS6_SC_(
    const QUrl *url,
    QOAuth1Signature::HttpRequestMethod method,
    const QMultiMap<QString, QVariant> *parameters,
    const QString *clientSharedKey,
    const QString *tokenSecret) {
  return new QOAuth1SignaturePrivate(
      *url,
      method,
      *parameters,
      *clientSharedKey,
      *tokenSecret);
}

//  QByteArray QOAuth1SignaturePrivate::secret() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK23QOAuth1SignaturePrivate6secretEv(
    const QOAuth1SignaturePrivate *self) {
  return new QByteArray(self->secret());
}

//  QOAuth1SignaturePrivate::~QOAuth1SignaturePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QOAuth1SignaturePrivateD1Ev(QOAuth1SignaturePrivate *self) {
  delete self;
}
