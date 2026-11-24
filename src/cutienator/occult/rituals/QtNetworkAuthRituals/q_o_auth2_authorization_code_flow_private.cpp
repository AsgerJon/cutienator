//  Written by dev_tooling.RitualGenerator from the records of QtNetworkAuth/
//  6.12.0/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauth2authorizationcodeflow.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qabstractoauth.h>
#include <qabstractoauthreplyhandler.h>
#include <private/qabstractoauth_p.h>
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
#include <qoauth2authorizationcodeflow.h>
#include <private/qoauth2authorizationcodeflow_p.h>
#include <qmap.h>
#include <qurl.h>
#include <qvariant.h>
#include <qurlquery.h>
#include <qjsonobject.h>
#include <qjsondocument.h>
#include <qauthenticator.h>
#include <qoauthhttpserverreplyhandler.h>
#include <QtCore/qcryptographichash.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 297, as _ZN21QAbstractOAuthPrivate26generateRandomBase64StringEh
inline QByteArray QAbstractOAuthPrivate::generateRandomBase64String(quint8 length)
{
    // We'll use QByteArray::toBase64() to create a random-looking string from
    // pure random data. In Base64 encoding, we get 6 bits of randomness per
    // character, so at most 255 * 6 bits are needed in this function.
    using Word = QRandomGenerator::result_type;
    auto wordCountForLength = [](int len) constexpr {
        constexpr int BitsPerWord = std::numeric_limits<Word>::digits;
        int bitcount = len * 6;
        return (bitcount + BitsPerWord - 1) / BitsPerWord;
    };
    constexpr int RandomBufferLength = wordCountForLength(std::numeric_limits<quint8>::max());
    Word randomdata[RandomBufferLength];

    qsizetype randomlen = wordCountForLength(length);
    QRandomGenerator::system()->fillRange(randomdata, randomlen);
    QByteArray ba = QByteArray::fromRawData(reinterpret_cast<char *>(randomdata),
                                            randomlen * sizeof(quint32))
            .toBase64(QByteArray::Base64UrlEncoding);
    ba.truncate(length);        // toBase64 output length has fixed lengths: 6, 11, 16, 22, 27...
    return ba;
}

//  from ../qtnetworkauth/src/oauth/qoauth2authorizationcodeflow.cpp, line 129, as _ZN35QOAuth2AuthorizationCodeFlowPrivate15_q_authenticateEP13QNetworkReplyP14QAuthenticator
inline void QOAuth2AuthorizationCodeFlowPrivate::_q_authenticate(QNetworkReply *reply,
                                                          QAuthenticator *authenticator)
{
    if (reply == currentReply){
        const auto url = reply->url();
        if (url == tokenUrl) {
            authenticator->setUser(clientIdentifier);
            authenticator->setPassword(QString());
        }
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth2authorizationcodeflow.cpp, line 155, as _ZN35QOAuth2AuthorizationCodeFlowPrivate19createPKCEChallengeEv
inline QByteArray QOAuth2AuthorizationCodeFlowPrivate::createPKCEChallenge()
{
    switch (pkceMethod) {
    case QOAuth2AuthorizationCodeFlow::PkceMethod::None:
        pkceCodeVerifier.clear();
        return {};
    case QOAuth2AuthorizationCodeFlow::PkceMethod::Plain:
        // RFC 7636 4.2, plain
        // code_challenge = code_verifier
        pkceCodeVerifier = generateRandomBase64String(pkceVerifierLength);
        return pkceCodeVerifier;
    case QOAuth2AuthorizationCodeFlow::PkceMethod::S256:
        // RFC 7636 4.2, S256
        // code_challenge = BASE64URL-ENCODE(SHA256(ASCII(code_verifier)))
        pkceCodeVerifier = generateRandomBase64String(pkceVerifierLength);
        // RFC 7636 3. Terminology:
        // "with all trailing '=' characters omitted"
        return QCryptographicHash::hash(pkceCodeVerifier, QCryptographicHash::Algorithm::Sha256)
                        .toBase64(QByteArray::Base64Option::Base64UrlEncoding
                                  | QByteArray::Base64Option::OmitTrailingEquals);
    };
    Q_UNREACHABLE_RETURN({});
}
//  -----------------------------------------------------------------------

//  QOAuth2AuthorizationCodeFlow
//      *QOAuth2AuthorizationCodeFlowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlow *ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate6q_funcEv(
    QOAuth2AuthorizationCodeFlowPrivate *self) {
  return self->q_func();
}

//  const QOAuth2AuthorizationCodeFlow
//      *QOAuth2AuthorizationCodeFlowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOAuth2AuthorizationCodeFlow *ritual_ZNK35QOAuth2AuthorizationCodeFlowPrivate6q_funcEv(
    const QOAuth2AuthorizationCodeFlowPrivate *self) {
  return self->q_func();
}

//  void QOAuth2AuthorizationCodeFlowPrivate::_q_authenticate(QNetworkReply
//      *reply, QAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate15_q_authenticateEP13QNetworkReplyP14QAuthenticator(
    QOAuth2AuthorizationCodeFlowPrivate *self,
    QNetworkReply *reply,
    QAuthenticator *authenticator) {
  self->_q_authenticate(reply, authenticator);
}

//  QByteArray QOAuth2AuthorizationCodeFlowPrivate::createPKCEChallenge()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate19createPKCEChallengeEv(
    QOAuth2AuthorizationCodeFlowPrivate *self) {
  return new QByteArray(self->createPKCEChallenge());
}
