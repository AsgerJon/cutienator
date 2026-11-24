//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth2_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qabstractoauth2.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 365, as _ZN21QAbstractOAuthPrivate11createQueryERK9QMultiMapI7QString8QVariantE
inline QUrlQuery QAbstractOAuthPrivate::createQuery(const QMultiMap<QString, QVariant> &parameters)
{
    QUrlQuery query;
    for (auto it = parameters.begin(), end = parameters.end(); it != end; ++it)
        query.addQueryItem(it.key(), it.value().toString());
    return query;
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 891, as _ZN22QAbstractOAuth2Private26callNetworkRequestModifierER15QNetworkRequestN14QAbstractOAuth5StageE
inline void QAbstractOAuth2Private::callNetworkRequestModifier(QNetworkRequest &request,
                                                       QAbstractOAuth::Stage stage)
{
    if (networkRequestModifier.contextObject && networkRequestModifier.slot) {
        if (!verifyThreadAffinity(networkRequestModifier.contextObject)) {
            Q_Q(QAbstractOAuth2);
            q->clearNetworkRequestModifier();
            return;
        }
        void *argv[] = { nullptr, &request, &stage};
        networkRequestModifier.slot->call(
            const_cast<QObject*>(networkRequestModifier.contextObject.get()), argv);
    }
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 581, as _ZN22QAbstractOAuth2Private13generateNonceEv
inline QString QAbstractOAuth2Private::generateNonce()
{
    // There is no strict minimum or maximum size for nonce, but
    // generating a 32-character base64 URL string provides
    // ~192 bits of entropy (32 characters * 6 bits per character).
    return QString::fromLatin1(QAbstractOAuthPrivate::generateRandomBase64String(32));
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 669, as _ZNK22QAbstractOAuth2Private31authorizationShouldIncludeNonceEv
inline bool QAbstractOAuth2Private::authorizationShouldIncludeNonce() const
{
    switch (nonceMode) {
    case QAbstractOAuth2::NonceMode::Enabled:
        return true;
    case QAbstractOAuth2::NonceMode::Disabled:
        return false;
    case QAbstractOAuth2::NonceMode::Automatic:
        return requestedScopeTokens.contains("openid");
    };
    return false;
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 835, as _ZN22QAbstractOAuth2Private27createRefreshRequestAndBodyERK4QUrl
inline QAbstractOAuth2Private::RequestAndBody QAbstractOAuth2Private::createRefreshRequestAndBody(
    const QUrl &url)
{
    RequestAndBody result;
    result.request.setUrl(url);

    QMultiMap<QString, QVariant> parameters;
#ifndef QT_NO_SSL
    if (sslConfiguration && !sslConfiguration->isNull())
        result.request.setSslConfiguration(*sslConfiguration);
#endif
    QUrlQuery query;
    parameters.insert(QtOAuth2RfcKeywords::grantType, QStringLiteral("refresh_token"));
    parameters.insert(QtOAuth2RfcKeywords::refreshToken, refreshToken);
    parameters.insert(QtOAuth2RfcKeywords::clientIdentifier, clientIdentifier);
    parameters.insert(QtOAuth2RfcKeywords::clientSharedSecret, clientIdentifierSharedKey);
    if (modifyParametersFunction)
        modifyParametersFunction(QAbstractOAuth::Stage::RefreshingAccessToken, &parameters);
    query = QAbstractOAuthPrivate::createQuery(parameters);
    result.request.setHeader(QNetworkRequest::ContentTypeHeader,
                      QStringLiteral("application/x-www-form-urlencoded"));

    callNetworkRequestModifier(result.request, QAbstractOAuth::Stage::RefreshingAccessToken);
    result.body = query.toString(QUrl::FullyEncoded).toLatin1();

    return result;
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 863, as _ZN22QAbstractOAuth2Private28logAuthorizationStageWarningE13QLatin1String
inline void QAbstractOAuth2Private::logAuthorizationStageWarning(QLatin1StringView message)
{
    static constexpr auto base = "Authorization stage: %s";
    qCWarning(loggingCategory, base, message.latin1());
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 869, as _ZN22QAbstractOAuth2Private28logAuthorizationStageWarningE13QLatin1Stringi
inline void QAbstractOAuth2Private::logAuthorizationStageWarning(QLatin1StringView message, int detail)
{
    static constexpr auto base = "Authorization stage: %s: %d";
    qCWarning(loggingCategory, base, message.latin1(), detail);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 875, as _ZN22QAbstractOAuth2Private20logTokenStageWarningE13QLatin1String
inline void QAbstractOAuth2Private::logTokenStageWarning(QLatin1StringView message)
{
    static constexpr auto base = "Token stage: %s";
    qCWarning(loggingCategory, base, message.latin1());
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 881, as _ZN22QAbstractOAuth2Private20verifyThreadAffinityEPK7QObject
inline bool QAbstractOAuth2Private::verifyThreadAffinity(const QObject *contextObject)
{
    Q_Q(QAbstractOAuth2);
    if (contextObject && (contextObject->thread() != q->thread())) {
        qCWarning(loggingCategory, "Context object must reside in the same thread");
        return false;
    }
    return true;
}
//  -----------------------------------------------------------------------

//  QAbstractOAuth2 *QAbstractOAuth2Private::q_func()
extern "C" Q_DECL_EXPORT
QAbstractOAuth2 *ritual_ZN22QAbstractOAuth2Private6q_funcEv(
    QAbstractOAuth2Private *self) {
  return self->q_func();
}

//  const QAbstractOAuth2 *QAbstractOAuth2Private::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractOAuth2 *ritual_ZNK22QAbstractOAuth2Private6q_funcEv(
    const QAbstractOAuth2Private *self) {
  return self->q_func();
}

//  void QAbstractOAuth2Private::setExpiresAt(const QDateTime &expiration)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private12setExpiresAtERK9QDateTime(
    QAbstractOAuth2Private *self,
    const QDateTime *expiration) {
  self->setExpiresAt(*expiration);
}

//  QString QAbstractOAuth2Private::generateRandomState()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QAbstractOAuth2Private19generateRandomStateEv() {
  return new QString(QAbstractOAuth2Private::generateRandomState());
}

//  QString QAbstractOAuth2Private::generateNonce()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QAbstractOAuth2Private13generateNonceEv() {
  return new QString(QAbstractOAuth2Private::generateNonce());
}

//  bool QAbstractOAuth2Private::authorizationShouldIncludeNonce() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QAbstractOAuth2Private31authorizationShouldIncludeNonceEv(
    const QAbstractOAuth2Private *self) {
  return self->authorizationShouldIncludeNonce();
}

//  void QAbstractOAuth2Private::setIdToken(const QString &token)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private10setIdTokenERK7QString(
    QAbstractOAuth2Private *self,
    const QString *token) {
  self->setIdToken(*token);
}

//  void QAbstractOAuth2Private::_q_tokenRequestFailed(QAbstractOAuth::Error
//      error, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private21_q_tokenRequestFailedEN14QAbstractOAuth5ErrorERK7QString(
    QAbstractOAuth2Private *self,
    QAbstractOAuth::Error error,
    const QString *errorString) {
  self->_q_tokenRequestFailed(error, *errorString);
}

//  bool QAbstractOAuth2Private::handleRfcErrorResponseIfPresent(const
//      QVariantMap &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractOAuth2Private31handleRfcErrorResponseIfPresentERK4QMapI7QString8QVariantE(
    QAbstractOAuth2Private *self,
    const QMap<QString, QVariant> *data) {
  return self->handleRfcErrorResponseIfPresent(*data);
}

//  RequestAndBody QAbstractOAuth2Private::createRefreshRequestAndBody(const
//      QUrl &url)
extern "C" Q_DECL_EXPORT
QAbstractOAuth2Private::RequestAndBody *ritual_ZN22QAbstractOAuth2Private27createRefreshRequestAndBodyERK4QUrl(
    QAbstractOAuth2Private *self,
    const QUrl *url) {
  return new QAbstractOAuth2Private::RequestAndBody(
      self->createRefreshRequestAndBody(
          *url));
}

//  void
//      QAbstractOAuth2Private::logAuthorizationStageWarning(QLatin1StringVie
//      w message)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private28logAuthorizationStageWarningE13QLatin1String(
    QAbstractOAuth2Private *self,
    const QLatin1String *message) {
  self->logAuthorizationStageWarning(*message);
}

//  void
//      QAbstractOAuth2Private::logAuthorizationStageWarning(QLatin1StringVie
//      w message, int detail)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private28logAuthorizationStageWarningE13QLatin1Stringi(
    QAbstractOAuth2Private *self,
    const QLatin1String *message,
    int detail) {
  self->logAuthorizationStageWarning(*message, detail);
}

//  void QAbstractOAuth2Private::logTokenStageWarning(QLatin1StringView
//      message)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private20logTokenStageWarningE13QLatin1String(
    QAbstractOAuth2Private *self,
    const QLatin1String *message) {
  self->logTokenStageWarning(*message);
}

//  bool QAbstractOAuth2Private::verifyThreadAffinity(const QObject
//      *contextObject)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractOAuth2Private20verifyThreadAffinityEPK7QObject(
    QAbstractOAuth2Private *self,
    const QObject *contextObject) {
  return self->verifyThreadAffinity(contextObject);
}
