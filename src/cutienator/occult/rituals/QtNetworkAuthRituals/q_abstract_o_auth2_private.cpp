//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth2_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qabstractoauth2.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth2_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlatin1stringview.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QSet>
#include <QtCore/QByteArray>
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

using namespace Qt::StringLiterals;

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

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 349, as _ZN21QAbstractOAuthPrivate21addContentTypeHeadersEP15QNetworkRequest
inline void QAbstractOAuthPrivate::addContentTypeHeaders(QNetworkRequest *request)
{
    Q_ASSERT(request);

    switch (contentType) {
    case QAbstractOAuth::ContentType::WwwFormUrlEncoded:
        request->setHeader(QNetworkRequest::ContentTypeHeader,
                           QStringLiteral("application/x-www-form-urlencoded"));
        break;
    case QAbstractOAuth::ContentType::Json:
        request->setHeader(QNetworkRequest::ContentTypeHeader,
                           QStringLiteral("application/json"));
        break;
    }
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 320, as _ZN21QAbstractOAuthPrivate14setExtraTokensERK4QMapI7QString8QVariantE
inline void QAbstractOAuthPrivate::setExtraTokens(const QVariantMap &tokens)
{
    if (extraTokens == tokens)
        return;
    Q_Q(QAbstractOAuth);
    extraTokens = tokens;
    emit q->extraTokensChanged(extraTokens);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 365, as _ZN21QAbstractOAuthPrivate11createQueryERK9QMultiMapI7QString8QVariantE
inline QUrlQuery QAbstractOAuthPrivate::createQuery(const QMultiMap<QString, QVariant> &parameters)
{
    QUrlQuery query;
    for (auto it = parameters.begin(), end = parameters.end(); it != end; ++it)
        query.addQueryItem(it.key(), it.value().toString());
    return query;
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 444, as _ZN22QAbstractOAuth2PrivateC1ERKSt4pairI7QStringS1_ERK4QUrlP21QNetworkAccessManager
inline QAbstractOAuth2Private::QAbstractOAuth2Private(const std::pair<QString, QString> &clientCredentials,
                                               const QUrl &authorizationUrl,
                                               QNetworkAccessManager *manager) :
    QAbstractOAuthPrivate("qt.networkauth.oauth2",
                          authorizationUrl,
                          clientCredentials.first,
                          manager),
    clientIdentifierSharedKey(clientCredentials.second)
{}

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 454, as _ZN22QAbstractOAuth2PrivateD1Ev
inline QAbstractOAuth2Private::~QAbstractOAuth2Private()
{}

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

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 476, as _ZN22QAbstractOAuth2Private11joinedScopeERK4QSetI10QByteArrayE
inline QString QAbstractOAuth2Private::joinedScope(const QSet<QByteArray> &scopeTokens)
{
    QString result;
    auto separator = ""_L1;
    for (const auto &token : scopeTokens) {
        result += separator;
        result += QLatin1StringView{token};
        separator = " "_L1;
    }
    return result;
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth2.cpp, line 589, as _ZN22QAbstractOAuth2Private13createRequestE4QUrlPK4QMapI7QString8QVariantE
inline QNetworkRequest QAbstractOAuth2Private::createRequest(QUrl url, const QVariantMap *parameters)
{
    QUrlQuery query(url.query());

    QNetworkRequest request;
    if (parameters) {
        for (auto it = parameters->begin(), end = parameters->end(); it != end; ++it)
            query.addQueryItem(it.key(), it.value().toString());
        url.setQuery(query);
    } else { // POST, PUT request
        addContentTypeHeaders(&request);
    }

    request.setUrl(url);
    request.setHeader(QNetworkRequest::UserAgentHeader, userAgent);
    const QString bearer = bearerFormat.arg(token);
    request.setRawHeader("Authorization", bearer.toUtf8());
    return request;
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

//  QAbstractOAuth2Private::QAbstractOAuth2Private(const std::pair<QString,
//      QString> &clientCredentials, const QUrl &authorizationUrl,
//      QNetworkAccessManager *manager)
extern "C" Q_DECL_EXPORT
QAbstractOAuth2Private *ritual_ZN22QAbstractOAuth2PrivateC1ERKSt4pairI7QStringS1_ERK4QUrlP21QNetworkAccessManager(
    const std::pair<QString, QString> *clientCredentials,
    const QUrl *authorizationUrl,
    QNetworkAccessManager *manager) {
  return new QAbstractOAuth2Private(
      *clientCredentials,
      *authorizationUrl,
      manager);
}

//  QAbstractOAuth2Private::~QAbstractOAuth2Private()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2PrivateD1Ev(QAbstractOAuth2Private *self) {
  delete self;
}

//  void QAbstractOAuth2Private::setExpiresAt(const QDateTime &expiration)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private12setExpiresAtERK9QDateTime(
    QAbstractOAuth2Private *self,
    const QDateTime *expiration) {
  self->setExpiresAt(*expiration);
}

//  void QAbstractOAuth2Private::setGrantedScopeTokens(const QSet<QByteArray>
//      &tokens)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private21setGrantedScopeTokensERK4QSetI10QByteArrayE(
    QAbstractOAuth2Private *self,
    const QSet<QByteArray> *tokens) {
  self->setGrantedScopeTokens(*tokens);
}

//  QString QAbstractOAuth2Private::joinedScope(const QSet<QByteArray>
//      &scopeTokens)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QAbstractOAuth2Private11joinedScopeERK4QSetI10QByteArrayE(
    const QSet<QByteArray> *scopeTokens) {
  return new QString(QAbstractOAuth2Private::joinedScope(*scopeTokens));
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

//  QNetworkRequest QAbstractOAuth2Private::createRequest(QUrl url, const
//      QVariantMap *parameters)
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZN22QAbstractOAuth2Private13createRequestE4QUrlPK4QMapI7QString8QVariantE(
    QAbstractOAuth2Private *self,
    const QUrl *url,
    const QVariantMap *parameters) {
  return new QNetworkRequest(self->createRequest(*url, parameters));
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

//  void QAbstractOAuth2Private::callNetworkRequestModifier(QNetworkRequest
//      &request, QAbstractOAuth::Stage stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QAbstractOAuth2Private26callNetworkRequestModifierER15QNetworkRequestN14QAbstractOAuth5StageE(
    QAbstractOAuth2Private *self,
    QNetworkRequest *request,
    QAbstractOAuth::Stage stage) {
  self->callNetworkRequestModifier(*request, stage);
}

//  bool QAbstractOAuth2Private::verifyThreadAffinity(const QObject
//      *contextObject)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QAbstractOAuth2Private20verifyThreadAffinityEPK7QObject(
    QAbstractOAuth2Private *self,
    const QObject *contextObject) {
  return self->verifyThreadAffinity(contextObject);
}

//  a QSet<QByteArray> a ritual of QAbstractOAuth2Private gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractOAuth2Private__QSet_QByteArray(
    QSet<QByteArray> *self) {
  delete self;
}
