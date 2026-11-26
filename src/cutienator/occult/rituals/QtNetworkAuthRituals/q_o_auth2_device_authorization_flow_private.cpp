//  Written by dev_tooling.RitualGenerator from the records of QtNetworkAuth/
//  6.12.0/QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauth2deviceauthorizationflow.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
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
#include <QtNetworkAuth/private/qoauth2deviceauthorizationflow_p.h>
#include <QtNetworkAuth/qoauth2deviceauthorizationflow.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qmap.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qvariant.h>
#include <QtNetwork/qrestaccessmanager.h>
#include <QtNetwork/qrestreply.h>
#include <functional>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 26, as local:qoauth2deviceauthorizationflow.cpp:Error
using Error = QAbstractOAuth::Error;

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 27, as local:qoauth2deviceauthorizationflow.cpp:Status
using Status = QAbstractOAuth::Status;

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

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 166, as _ZN37QOAuth2DeviceAuthorizationFlowPrivateD1Ev
inline QOAuth2DeviceAuthorizationFlowPrivate::~QOAuth2DeviceAuthorizationFlowPrivate()
{
    resetCurrentAuthorizationReply();
    resetCurrentTokenReply();
    tokenPollingTimer.stop();
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 708, as _ZN22QAbstractOAuth2Private23_q_tokenRequestFinishedERK4QMapI7QString8QVariantE
inline void QAbstractOAuth2Private::_q_tokenRequestFinished(const QVariantMap &values)
{
    Q_Q(QAbstractOAuth2);

    if (values.contains(QtOAuth2RfcKeywords::error)) {
        const QString error = values.value(QtOAuth2RfcKeywords::error).toString();

        // RFC 6749 section 5.2: error keyword is required to contain a value
        if (error.isEmpty()) {
            _q_tokenRequestFailed(QAbstractOAuth::Error::ServerError,
                                  u"Received an empty OAuth error code"_s);
            return;
        }

        // A failed refresh does not necessarily invalidate an existing
        // access token. Restore the status before reporting the error.
        if (status == QAbstractOAuth::Status::RefreshingToken) {
            if (!q->token().isEmpty())
                setStatus(QAbstractOAuth::Status::Granted);
            else
                setStatus(QAbstractOAuth::Status::NotAuthenticated);
        }
        (void)handleRfcErrorResponseIfPresent(values);
        return;
    }

    bool ok;
    const QString accessToken = values.value(QtOAuth2RfcKeywords::accessToken).toString();
    tokenType = values.value(QtOAuth2RfcKeywords::tokenType).toString();
    tokenLifetime = values.value(QtOAuth2RfcKeywords::expiresIn).toLongLong(&ok);
    if (!ok)
        tokenLifetime = 0;
    if (values.value(QtOAuth2RfcKeywords::refreshToken).isValid())
        q->setRefreshToken(values.value(QtOAuth2RfcKeywords::refreshToken).toString());

    if (accessToken.isEmpty()) {
        _q_tokenRequestFailed(QAbstractOAuth::Error::OAuthTokenNotFoundError,
                                    "Access token not received"_L1);
        return;
    }
    q->setToken(accessToken);

    // RFC 6749 section 5.1 https://datatracker.ietf.org/doc/html/rfc6749#section-5.1
    // If the requested scope and granted scopes differ, server is REQUIRED to return
    // the scope. If OTOH the scopes match, the server MAY omit the scope in the response,
    // in which case we assume that the granted scope matches the requested scope.
    //
    // Note: 'scope' variable has two roles: requested scope, and later granted scope.
    // Therefore 'scope' needs to be set if the granted scope differs from 'scope'.
    QString receivedGrantedScope = values.value(QtOAuth2RfcKeywords::scope).toString();
    const QSet<QByteArray> splitGrantedScope = splitScope(receivedGrantedScope);
    if (splitGrantedScope.isEmpty()) {
        setGrantedScopeTokens(requestedScopeTokens);
    } else {
        setGrantedScopeTokens(splitGrantedScope);
#ifndef QOAUTH2_NO_LEGACY_SCOPE
        if (receivedGrantedScope != legacyScope) {
            legacyScope = std::move(receivedGrantedScope);
            QT_IGNORE_DEPRECATIONS(Q_EMIT q->scopeChanged(legacyScope);)
        }
#endif
    }

    // An id_token must be included if this was an OIDC request and the server granted it.
    // https://openid.net/specs/openid-connect-core-1_0-final.html#AuthRequest (cf. 'scope')
    // https://openid.net/specs/openid-connect-core-1_0-final.html#TokenResponse
    //
    // However token refresh responses 'might not' contain an id_token
    // https://openid.net/specs/openid-connect-core-1_0-final.html#RefreshTokenResponse
    const QString receivedIdToken = values.value(QtOAuth2RfcKeywords::idToken).toString();
    if (requestedScopeTokens.contains("openid") && grantedScopeTokens.contains("openid")
        && receivedIdToken.isEmpty() && status != QAbstractOAuth::Status::RefreshingToken) {
        setIdToken({});
        _q_tokenRequestFailed(QAbstractOAuth::Error::OAuthTokenNotFoundError,
                              "'openid' scope requested and granted but ID token not received"_L1);
        return;
    }

    // Update the id_token. However if we were refreshing tokens and didn't receive a new
    // id_token, keep the original
    if (status != QAbstractOAuth::Status::RefreshingToken || !receivedIdToken.isEmpty())
        setIdToken(receivedIdToken);

    if (tokenLifetime > 0)
        setExpiresAt(QDateTime::currentDateTimeUtc().addSecs(tokenLifetime));
    else
        setExpiresAt(QDateTime());

    QVariantMap copy(values);
    copy.remove(QtOAuth2RfcKeywords::accessToken);
    copy.remove(QtOAuth2RfcKeywords::expiresIn);
    copy.remove(QtOAuth2RfcKeywords::refreshToken);
    copy.remove(QtOAuth2RfcKeywords::scope);
    copy.remove(QtOAuth2RfcKeywords::tokenType);
    copy.remove(QtOAuth2RfcKeywords::idToken);
    QVariantMap newExtraTokens = extraTokens;
    newExtraTokens.insert(copy);
    setExtraTokens(newExtraTokens);

    setStatus(QAbstractOAuth::Status::Granted);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 691, as _ZN22QAbstractOAuth2Private21_q_tokenRequestFailedEN14QAbstractOAuth5ErrorERK7QString
inline void QAbstractOAuth2Private::_q_tokenRequestFailed(QAbstractOAuth::Error error,
                                                const QString& errorString)
{
    Q_Q(QAbstractOAuth);
    qCWarning(loggingCategory) << "Token request failed:" << errorString;
    // If we were refreshing, reset status to Granted if we have an access token.
    // The access token might still be valid, and even if it wouldn't be,
    // refreshing can be attempted again.
    if (q->status() == QAbstractOAuth::Status::RefreshingToken) {
        if (!q->token().isEmpty())
            setStatus(QAbstractOAuth::Status::Granted);
        else
            setStatus(QAbstractOAuth::Status::NotAuthenticated);
    }
    emit q->requestFailed(error);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 278, as _ZN21QAbstractOAuthPrivate20networkAccessManagerEv
inline QNetworkAccessManager *QAbstractOAuthPrivate::networkAccessManager()
{
    Q_Q(QAbstractOAuth);
    if (!networkAccessManagerPointer)
        networkAccessManagerPointer = new QNetworkAccessManager(q);
    return networkAccessManagerPointer.data();
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 682, as _ZN22QAbstractOAuth2Private10setIdTokenERK7QString
inline void QAbstractOAuth2Private::setIdToken(const QString &token)
{
    Q_Q(QAbstractOAuth2);
    if (idToken == token)
        return;
    idToken = token;
    emit q->idTokenChanged(idToken);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 488, as _ZN22QAbstractOAuth2Private10splitScopeE11QStringView
inline QSet<QByteArray> QAbstractOAuth2Private::splitScope(QStringView scope)
{
    QSet<QByteArray> result;
    for (auto token : scope.tokenize(u' ', Qt::SkipEmptyParts)) {
        warnOnInvalidScopeToken(token);
        result.insert(token.toUtf8());
    }
    return result;
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 457, as _ZN22QAbstractOAuth2Private12setExpiresAtERK9QDateTime
inline void QAbstractOAuth2Private::setExpiresAt(const QDateTime &expiration)
{
    Q_ASSERT(!expiration.isValid() || expiration.timeSpec() == Qt::TimeSpec::UTC);
    if (expiresAtUtc == expiration)
        return;
    Q_Q(QAbstractOAuth2);
    expiresAtUtc = expiration;
    emit q->expirationAtChanged(expiresAtUtc.toLocalTime());
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 467, as _ZN22QAbstractOAuth2Private21setGrantedScopeTokensERK4QSetI10QByteArrayE
inline void QAbstractOAuth2Private::setGrantedScopeTokens(const QSet<QByteArray> &tokens)
{
    if (tokens == grantedScopeTokens)
        return;
    Q_Q(QAbstractOAuth2);
    grantedScopeTokens = tokens;
    Q_EMIT q->grantedScopeTokensChanged(grantedScopeTokens);
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

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 160, as _ZN37QOAuth2DeviceAuthorizationFlowPrivateC1EP21QNetworkAccessManager
inline QOAuth2DeviceAuthorizationFlowPrivate::QOAuth2DeviceAuthorizationFlowPrivate(
    QNetworkAccessManager *manager)
    : QAbstractOAuth2Private(std::make_pair(QString(), QString()), QUrl(), manager)
{
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 333, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate22tokenAcquisitionFailedEN14QAbstractOAuth5ErrorERK7QString
inline void QOAuth2DeviceAuthorizationFlowPrivate::tokenAcquisitionFailed(QAbstractOAuth::Error error,
                                                                   const QString &errorString)
{
    _q_tokenRequestFailed(error, errorString);
    stopTokenPolling();
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 340, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate11setUserCodeERK7QString
inline void QOAuth2DeviceAuthorizationFlowPrivate::setUserCode(const QString &code)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (userCode == code)
        return;
    userCode = code;
    emit q->userCodeChanged(userCode);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 349, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate18setVerificationUrlERK4QUrl
inline void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrl(const QUrl &url)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (verificationUrl == url)
        return;
    verificationUrl = url;
    emit q->verificationUrlChanged(verificationUrl);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 358, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate26setVerificationUrlCompleteERK4QUrl
inline void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrlComplete(const QUrl &url)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (completeVerificationUrl == url)
        return;
    completeVerificationUrl = url;
    emit q->completeVerificationUrlChanged(completeVerificationUrl);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 367, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate21setUserCodeExpirationERK9QDateTime
inline void QOAuth2DeviceAuthorizationFlowPrivate::setUserCodeExpiration(const QDateTime &expiration)
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    Q_ASSERT(!expiration.isValid() || expiration.timeSpec() == Qt::TimeSpec::UTC);
    if (userCodeExpirationUtc == expiration)
        return;
    userCodeExpirationUtc = expiration;
    emit q->userCodeExpirationAtChanged(userCodeExpirationUtc.toLocalTime());
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 408, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate16stopTokenPollingEv
inline void QOAuth2DeviceAuthorizationFlowPrivate::stopTokenPolling()
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (!q->isPolling())
        return;

    qCDebug(loggingCategory, "Token stage: Stopping token polling");
    resetCurrentTokenReply();
    tokenPollingTimer.stop();
    emit q->pollingChanged(false);
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 496, as _ZNK37QOAuth2DeviceAuthorizationFlowPrivate25isNextPollAfterExpirationEv
inline bool QOAuth2DeviceAuthorizationFlowPrivate::isNextPollAfterExpiration() const
{
    if (!userCodeExpirationUtc.isValid())
        return true;

    const QDateTime nextPoll = QDateTime::currentDateTimeUtc().addDuration(
        std::chrono::duration_cast<std::chrono::milliseconds>(tokenPollingTimer.interval()));

    return nextPoll > userCodeExpirationUtc;
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 507, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate22resetCurrentTokenReplyEv
inline void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentTokenReply()
{
    if (currentTokenReply) {
        const auto reply = currentTokenReply.get();
        // Clear current reply before abort to avoid handling the finished signal
        currentTokenReply.clear();
        reply->abort();
        reply->deleteLater();
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 518, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate30resetCurrentAuthorizationReplyEv
inline void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentAuthorizationReply()
{
    if (currentAuthorizationReply) {
        const auto reply = currentAuthorizationReply.get();
        // Clear current reply before abort to avoid handling the finished signal
        currentAuthorizationReply.clear();
        reply->abort();
        reply->deleteLater();
    }
}

//  from ../qtnetworkauth/src/oauth/qoauth2deviceauthorizationflow.cpp, line 529, as _ZN37QOAuth2DeviceAuthorizationFlowPrivate7networkEv
inline QRestAccessManager *QOAuth2DeviceAuthorizationFlowPrivate::network()
{
    Q_Q(QOAuth2DeviceAuthorizationFlow);
    if (!restAccessManager) {
        // First usage, create
        restAccessManager = new QRestAccessManager(networkAccessManager(), q);
    } else if (restAccessManager->networkAccessManager() != networkAccessManager()) {
        // QNetworkAccessManager has changed, re-create
        resetCurrentAuthorizationReply();
        resetCurrentTokenReply();
        delete restAccessManager;
        restAccessManager = new QRestAccessManager(networkAccessManager(), q);
    }
    return restAccessManager;
}
//  -----------------------------------------------------------------------

//  QOAuth2DeviceAuthorizationFlow
//      *QOAuth2DeviceAuthorizationFlowPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlow *ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate6q_funcEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->q_func();
}

//  const QOAuth2DeviceAuthorizationFlow
//      *QOAuth2DeviceAuthorizationFlowPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOAuth2DeviceAuthorizationFlow *ritual_ZNK37QOAuth2DeviceAuthorizationFlowPrivate6q_funcEv(
    const QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->q_func();
}

//  QOAuth2DeviceAuthorizationFlowPrivate::QOAuth2DeviceAuthorizationFlowPriv
//      ate(QNetworkAccessManager *manager)
extern "C" Q_DECL_EXPORT
QOAuth2DeviceAuthorizationFlowPrivate *ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivateC1EP21QNetworkAccessManager(
    QNetworkAccessManager *manager) {
  return new QOAuth2DeviceAuthorizationFlowPrivate(manager);
}

//  QOAuth2DeviceAuthorizationFlowPrivate::~QOAuth2DeviceAuthorizationFlowPri
//      vate()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivateD1Ev(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  delete self;
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::tokenAcquisitionFailed(QAbstr
//      actOAuth::Error error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate22tokenAcquisitionFailedEN14QAbstractOAuth5ErrorERK7QString(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    QAbstractOAuth::Error error,
    const QString *errorString) {
  self->tokenAcquisitionFailed(error, *errorString);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::setUserCode(const QString
//      &code)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate11setUserCodeERK7QString(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QString *code) {
  self->setUserCode(*code);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrl(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate18setVerificationUrlERK4QUrl(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QUrl *url) {
  self->setVerificationUrl(*url);
}

//  void
//      QOAuth2DeviceAuthorizationFlowPrivate::setVerificationUrlComplete(con
//      st QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate26setVerificationUrlCompleteERK4QUrl(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QUrl *url) {
  self->setVerificationUrlComplete(*url);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::setUserCodeExpiration(const
//      QDateTime &expiration)
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate21setUserCodeExpirationERK9QDateTime(
    QOAuth2DeviceAuthorizationFlowPrivate *self,
    const QDateTime *expiration) {
  self->setUserCodeExpiration(*expiration);
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::stopTokenPolling()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate16stopTokenPollingEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  self->stopTokenPolling();
}

//  bool QOAuth2DeviceAuthorizationFlowPrivate::isNextPollAfterExpiration()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK37QOAuth2DeviceAuthorizationFlowPrivate25isNextPollAfterExpirationEv(
    const QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->isNextPollAfterExpiration();
}

//  void QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentTokenReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate22resetCurrentTokenReplyEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  self->resetCurrentTokenReply();
}

//  void
//      QOAuth2DeviceAuthorizationFlowPrivate::resetCurrentAuthorizationReply
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate30resetCurrentAuthorizationReplyEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  self->resetCurrentAuthorizationReply();
}

//  QRestAccessManager *QOAuth2DeviceAuthorizationFlowPrivate::network()
extern "C" Q_DECL_EXPORT
QRestAccessManager *ritual_ZN37QOAuth2DeviceAuthorizationFlowPrivate7networkEv(
    QOAuth2DeviceAuthorizationFlowPrivate *self) {
  return self->network();
}
