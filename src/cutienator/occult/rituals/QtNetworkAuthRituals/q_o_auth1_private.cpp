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
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtNetworkAuth/qoauth1signature.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/qabstractoauth.h>
#include <QtNetworkAuth/qabstractoauthreplyhandler.h>
#include <QtNetworkAuth/private/qabstractoauth_p.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qmessageauthenticationcode.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtCore/qrandom.h>
#include <QtCore/private/qlocking_p.h>
#include <QtNetworkAuth/qoauth1.h>
#include <QtNetworkAuth/private/qoauth1_p.h>
#include <QtNetworkAuth/qoauth1signature.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
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

using namespace Qt::StringLiterals;

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 75, as local:qoauth1.cpp:OAuth1
using OAuth1 = QOAuth1Private::OAuth1KeyString;

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 264, as _ZN21QAbstractOAuthPrivateC2EPKcRK4QUrlRK7QStringP21QNetworkAccessManager
inline QAbstractOAuthPrivate::QAbstractOAuthPrivate(const char *loggingCategory,
                                             const QUrl &authorizationUrl,
                                             const QString &clientIdentifier,
                                             QNetworkAccessManager *manager) :
    loggingCategory(loggingCategory),
    clientIdentifier(clientIdentifier),
    authorizationUrl(authorizationUrl),
    defaultReplyHandler(new QOAuthOobReplyHandler),
    networkAccessManagerPointer(manager)
{}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 275, as _ZN21QAbstractOAuthPrivateD2Ev
inline QAbstractOAuthPrivate::~QAbstractOAuthPrivate()
{}

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 88, as _ZN14QOAuth1PrivateC1ERKSt4pairI7QStringS1_EP21QNetworkAccessManager
inline QOAuth1Private::QOAuth1Private(const std::pair<QString, QString> &clientCredentials,
                               QNetworkAccessManager *networkAccessManager) :
    QAbstractOAuthPrivate("qt.networkauth.oauth1",
                          QUrl(),
                          clientCredentials.first,
                          networkAccessManager),
    clientIdentifierSharedKey(clientCredentials.second)
{
    qRegisterMetaType<QNetworkReply::NetworkError>("QNetworkReply::NetworkError");
    qRegisterMetaType<QOAuth1::SignatureMethod>("QOAuth1::SignatureMethod");
}

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

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 214, as _ZNK14QOAuth1Private17generateSignatureERK9QMultiMapI7QString8QVariantERK4QUrlN21QNetworkAccessManager9OperationE
inline QByteArray QOAuth1Private::generateSignature(const QMultiMap<QString, QVariant> &parameters,
                                             const QUrl &url,
                                             QNetworkAccessManager::Operation operation) const
{
    QOAuth1Signature signature(url,
                               clientIdentifierSharedKey,
                               tokenSecret,
                               static_cast<QOAuth1Signature::HttpRequestMethod>(operation),
                               parameters);
    return formatSignature(signature);
}

//  from ../qtnetworkauth/src/oauth/qoauth1.cpp, line 226, as _ZNK14QOAuth1Private17generateSignatureERK9QMultiMapI7QString8QVariantERK4QUrlRK10QByteArray
inline QByteArray QOAuth1Private::generateSignature(const QMultiMap<QString, QVariant> &parameters,
                                             const QUrl &url,
                                             const QByteArray &verb) const
{
    QOAuth1Signature signature(url,
                               clientIdentifierSharedKey,
                               tokenSecret,
                               QOAuth1Signature::HttpRequestMethod::Custom,
                               parameters);
    signature.setCustomMethodString(verb);
    return formatSignature(signature);
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

//  QOAuth1Private::QOAuth1Private(const std::pair<QString, QString>
//      &clientCredentials, QNetworkAccessManager *networkAccessManager)
extern "C" Q_DECL_EXPORT
QOAuth1Private *ritual_ZN14QOAuth1PrivateC1ERKSt4pairI7QStringS1_EP21QNetworkAccessManager(
    const std::pair<QString, QString> *clientCredentials,
    QNetworkAccessManager *networkAccessManager) {
  return new QOAuth1Private(*clientCredentials, networkAccessManager);
}

//  QString QOAuth1Private::signatureMethodString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOAuth1Private21signatureMethodStringEv(
    const QOAuth1Private *self) {
  return new QString(self->signatureMethodString());
}

//  QByteArray QOAuth1Private::generateSignature(const QMultiMap<QString,
//      QVariant> &parameters, const QUrl &url,
//      QNetworkAccessManager::Operation operation) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QOAuth1Private17generateSignatureERK9QMultiMapI7QString8QVariantERK4QUrlN21QNetworkAccessManager9OperationE(
    const QOAuth1Private *self,
    const QMultiMap<QString, QVariant> *parameters,
    const QUrl *url,
    QNetworkAccessManager::Operation operation) {
  return new QByteArray(
      self->generateSignature(
          *parameters,
          *url,
          operation));
}

//  QByteArray QOAuth1Private::generateSignature(const QMultiMap<QString,
//      QVariant> &parameters, const QUrl &url, const QByteArray &verb) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK14QOAuth1Private17generateSignatureERK9QMultiMapI7QString8QVariantERK4QUrlRK10QByteArray(
    const QOAuth1Private *self,
    const QMultiMap<QString, QVariant> *parameters,
    const QUrl *url,
    const QByteArray *verb) {
  return new QByteArray(self->generateSignature(*parameters, *url, *verb));
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
