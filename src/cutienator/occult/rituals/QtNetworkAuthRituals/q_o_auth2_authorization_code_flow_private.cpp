//  Written by dev_tooling.RitualGenerator from the records of QtNetworkAuth/
//  6.12.0/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauth2authorizationcodeflow.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/qabstractoauth2.h>
#include <QtNetworkAuth/private/qabstractoauth2_p.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmessageauthenticationcode.h>
#include <QtNetwork/qnetworkreply.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtNetwork/qhttpmultipart.h>
#ifndef QT_NO_SSL
#include <QtNetwork/qsslconfiguration.h>
#endif
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
#include <QtNetworkAuth/qoauth2authorizationcodeflow.h>
#include <QtNetworkAuth/private/qoauth2authorizationcodeflow_p.h>
#include <QtCore/qmap.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qjsondocument.h>
#include <QtNetwork/qauthenticator.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtCore/qcryptographichash.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtnetworkauth/src/oauth/qoauth2authorizationcodeflow.cpp, line 79, as local:qoauth2authorizationcodeflow.cpp:fromUrlFormEncoding
static QString fromUrlFormEncoding(const QString &source)
{
    QByteArray decoded = source.toUtf8();
    decoded = QByteArray::fromPercentEncoding(decoded.replace("+"," "));
    return QString::fromUtf8(decoded);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 444, as _ZN22QAbstractOAuth2PrivateC2ERKSt4pairI7QStringS1_ERK4QUrlP21QNetworkAccessManager
inline QAbstractOAuth2Private::QAbstractOAuth2Private(const std::pair<QString, QString> &clientCredentials,
                                               const QUrl &authorizationUrl,
                                               QNetworkAccessManager *manager) :
    QAbstractOAuthPrivate("qt.networkauth.oauth2",
                          authorizationUrl,
                          clientCredentials.first,
                          manager),
    clientIdentifierSharedKey(clientCredentials.second)
{}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 454, as _ZN22QAbstractOAuth2PrivateD2Ev
inline QAbstractOAuth2Private::~QAbstractOAuth2Private()
{}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 320, as _ZN21QAbstractOAuthPrivate14setExtraTokensERK4QMapI7QString8QVariantE
inline void QAbstractOAuthPrivate::setExtraTokens(const QVariantMap &tokens)
{
    if (extraTokens == tokens)
        return;
    Q_Q(QAbstractOAuth);
    extraTokens = tokens;
    emit q->extraTokensChanged(extraTokens);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 286, as _ZN21QAbstractOAuthPrivate9setStatusEN14QAbstractOAuth6StatusE
inline void QAbstractOAuthPrivate::setStatus(QAbstractOAuth::Status newStatus)
{
    Q_Q(QAbstractOAuth);
    if (status != newStatus) {
        status = newStatus;
        Q_EMIT q->statusChanged(status);
        if (status == QAbstractOAuth::Status::Granted)
            Q_EMIT q->granted();
    }
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 810, as _ZN22QAbstractOAuth2Private31handleRfcErrorResponseIfPresentERK4QMapI7QString8QVariantE
inline bool QAbstractOAuth2Private::handleRfcErrorResponseIfPresent(const QVariantMap &data)
{
    Q_Q(QAbstractOAuth2);
    const QString error = data.value(QtOAuth2RfcKeywords::error).toString();

    if (error.size()) {
        // RFC 6749, Section 5.2 Error Response
        const QString uri = data.value(QtOAuth2RfcKeywords::errorUri).toString();
        const QString description = data.value(QtOAuth2RfcKeywords::errorDescription).toString();
        qCWarning(loggingCategory, "Authorization stage: AuthenticationError: %ls(%ls): %ls",
                  qUtf16Printable(error), qUtf16Printable(uri), qUtf16Printable(description));

        const QUrl url = QUrl{uri};
#if QT_DEPRECATED_SINCE(6, 13)
        QT_IGNORE_DEPRECATIONS(Q_EMIT q->error(error, description, url);)
#endif
        Q_EMIT q->serverReportedErrorOccurred(error, description, url);

        // Emit also requestFailed() so that it is a signal for all errors
        emit q->requestFailed(QAbstractOAuth::Error::ServerError);
        return true;
    }
    return false;
}

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

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 571, as _ZN22QAbstractOAuth2Private19generateRandomStateEv
inline QString QAbstractOAuth2Private::generateRandomState()
{
    // There is no strict minimum or maximum size for state, but
    // generating a 32-character base64 URL string provides
    // ~192 bits of entropy (32 characters * 6 bits per character), which is
    // a common minimum size and meets OAuth 2 recommendation for secrets:
    // https://datatracker.ietf.org/doc/html/rfc6819#section-5.1.4.2.2
    return QString::fromLatin1(QAbstractOAuthPrivate::generateRandomBase64String(32));
}

//  from ../qtnetworkauth/src/oauth/qoauth2authorizationcodeflow.cpp, line 60, as _ZN35QOAuth2AuthorizationCodeFlowPrivateC1ERK4QUrlS2_RK7QStringP21QNetworkAccessManager
inline QOAuth2AuthorizationCodeFlowPrivate::QOAuth2AuthorizationCodeFlowPrivate(
        const QUrl &authorizationUrl, const QUrl &accessTokenUrl, const QString &clientIdentifier,
        QNetworkAccessManager *manager) :
    QAbstractOAuth2Private(std::make_pair(clientIdentifier, QString()), authorizationUrl, manager)
{
    tokenUrl = accessTokenUrl;
    responseType = QStringLiteral("code");
}

//  from ../qtnetworkauth/src/oauth/qoauth2authorizationcodeflow.cpp, line 86, as _ZN35QOAuth2AuthorizationCodeFlowPrivate17_q_handleCallbackERK4QMapI7QString8QVariantE
inline void QOAuth2AuthorizationCodeFlowPrivate::_q_handleCallback(const QVariantMap &data)
{
    Q_Q(QOAuth2AuthorizationCodeFlow);

    if (status != QAbstractOAuth::Status::NotAuthenticated) {
        qCWarning(loggingCategory) << "Authorization stage: callback in unexpected status:"
                                   << static_cast<int>(status) << ", ignoring the callback";
        return;
    }

    Q_ASSERT(!state.isEmpty());

    if (handleRfcErrorResponseIfPresent(data))
        return;

    const QString code = data.value(QtOAuth2RfcKeywords::code).toString();
    if (code.isEmpty()) {
        qCWarning(loggingCategory, "Authorization stage: Code not received");
        emit q->requestFailed(QAbstractOAuth::Error::OAuthTokenNotFoundError);
        return;
    }
    const QString receivedState =
        fromUrlFormEncoding(data.value(QtOAuth2RfcKeywords::state).toString());
    if (receivedState.isEmpty()) {
        qCWarning(loggingCategory, "Authorization stage: State not received");
        emit q->requestFailed(QAbstractOAuth::Error::ServerError);
        return;
    }
    if (state != receivedState) {
        qCWarning(loggingCategory) << "Authorization stage: State mismatch";
        emit q->requestFailed(QAbstractOAuth::Error::ServerError);
        return;
    }

    setStatus(QAbstractOAuth::Status::TemporaryCredentialsReceived);

    QVariantMap copy(data);
    copy.remove(QtOAuth2RfcKeywords::code);
    copy.remove(QtOAuth2RfcKeywords::state);
    setExtraTokens(copy);
    q->requestAccessToken(code);
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

//  QOAuth2AuthorizationCodeFlowPrivate::QOAuth2AuthorizationCodeFlowPrivate(
//      const QUrl &authorizationUrl, const QUrl &accessTokenUrl, const
//      QString &clientIdentifier, QNetworkAccessManager *manager)
extern "C" Q_DECL_EXPORT
QOAuth2AuthorizationCodeFlowPrivate *ritual_ZN35QOAuth2AuthorizationCodeFlowPrivateC1ERK4QUrlS2_RK7QStringP21QNetworkAccessManager(
    const QUrl *authorizationUrl,
    const QUrl *accessTokenUrl,
    const QString *clientIdentifier,
    QNetworkAccessManager *manager) {
  return new QOAuth2AuthorizationCodeFlowPrivate(
      *authorizationUrl,
      *accessTokenUrl,
      *clientIdentifier,
      manager);
}

//  void QOAuth2AuthorizationCodeFlowPrivate::_q_handleCallback(const
//      QVariantMap &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuth2AuthorizationCodeFlowPrivate17_q_handleCallbackERK4QMapI7QString8QVariantE(
    QOAuth2AuthorizationCodeFlowPrivate *self,
    const QMap<QString, QVariant> *data) {
  self->_q_handleCallback(*data);
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
