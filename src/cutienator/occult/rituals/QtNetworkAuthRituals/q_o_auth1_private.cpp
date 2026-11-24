//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth1_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauth1.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth1_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetworkAuth/qoauth1signature.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qoauth1.h"
#include "qoauth1_p.h"
#include "qoauth1signature.h"
#include "qoauthhttpserverreplyhandler.h"
#include <QtCore/qmap.h>
#include <QtCore/qlist.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmessageauthenticationcode.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 199, as _ZNK14QOAuth1Private21signatureMethodStringEv
inline QString QOAuth1Private::signatureMethodString() const
{
    switch (signatureMethod) { // No default: intended
    case QOAuth1::SignatureMethod::PlainText:
        return QStringLiteral("PLAINTEXT");
    case QOAuth1::SignatureMethod::Hmac_Sha1:
        return QStringLiteral("HMAC-SHA1");
    case QOAuth1::SignatureMethod::Rsa_Sha1:
        qFatal("RSA-SHA1 signature method not supported");
        return QStringLiteral("RSA-SHA1");
    }
    qFatal("Invalid signature method");
    return QString();
}

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 239, as _ZNK14QOAuth1Private15formatSignatureERK16QOAuth1Signature
inline QByteArray QOAuth1Private::formatSignature(const QOAuth1Signature &signature) const
{
    switch (signatureMethod) {
    case QOAuth1::SignatureMethod::Hmac_Sha1:
        return signature.hmacSha1().toBase64();
    case QOAuth1::SignatureMethod::PlainText:
        return signature.plainText();
    default:
        qFatal("QOAuth1Private::generateSignature: Signature method not supported");
        return QByteArray();
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 286, as _ZN14QOAuth1Private22_q_onTokenRequestErrorEN13QNetworkReply12NetworkErrorE
inline void QOAuth1Private::_q_onTokenRequestError(QNetworkReply::NetworkError error)
{
    Q_Q(QOAuth1);
    Q_UNUSED(error);
    Q_EMIT q->requestFailed(QAbstractOAuth::Error::NetworkError);
}
//  -----------------------------------------------------------------------

//  QOAuth1 *QOAuth1Private::q_func()
extern "C" Q_DECL_EXPORT
QOAuth1 *ritual_ZN14QOAuth1Private6q_funcEv(QOAuth1Private *self) {
  return self->q_func();
}

//  const QOAuth1 *QOAuth1Private::q_func() const
extern "C" Q_DECL_EXPORT
const QOAuth1 *ritual_ZNK14QOAuth1Private6q_funcEv(
    const QOAuth1Private *self) {
  return self->q_func();
}

//  QString QOAuth1Private::signatureMethodString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOAuth1Private21signatureMethodStringEv(
    const QOAuth1Private *self) {
  return new QString(self->signatureMethodString());
}

//  QByteArray QOAuth1Private::formatSignature(const QOAuth1Signature
//      &signature) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QOAuth1Private15formatSignatureERK16QOAuth1Signature(
    const QOAuth1Private *self,
    const QOAuth1Signature *signature) {
  return new QByteArray(self->formatSignature(*signature));
}

//  void QOAuth1Private::_q_onTokenRequestError(QNetworkReply::NetworkError
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOAuth1Private22_q_onTokenRequestErrorEN13QNetworkReply12NetworkErrorE(
    QOAuth1Private *self,
    QNetworkReply::NetworkError error) {
  self->_q_onTokenRequestError(error);
}
