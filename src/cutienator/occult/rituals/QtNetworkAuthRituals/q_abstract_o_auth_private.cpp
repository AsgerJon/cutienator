//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qabstractoauth.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qabstractoauth_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 278, as _ZN21QAbstractOAuthPrivate20networkAccessManagerEv
inline QNetworkAccessManager *QAbstractOAuthPrivate::networkAccessManager()
{
    Q_Q(QAbstractOAuth);
    if (!networkAccessManagerPointer)
        networkAccessManagerPointer = new QNetworkAccessManager(q);
    return networkAccessManagerPointer.data();
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

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 320, as _ZN21QAbstractOAuthPrivate14setExtraTokensERK4QMapI7QString8QVariantE
inline void QAbstractOAuthPrivate::setExtraTokens(const QVariantMap &tokens)
{
    if (extraTokens == tokens)
        return;
    Q_Q(QAbstractOAuth);
    extraTokens = tokens;
    emit q->extraTokensChanged(extraTokens);
}

//  from ../qtnetworkauth/src/oauth/qabstractoauth.cpp, line 330, as _ZN21QAbstractOAuthPrivate17convertParametersERK4QMapI7QString8QVariantE
inline QByteArray QAbstractOAuthPrivate::convertParameters(const QVariantMap &parameters)
{
    QByteArray data;
    switch (contentType) {
    case QAbstractOAuth::ContentType::Json:
        data = QJsonDocument::fromVariant(QVariant(parameters)).toJson();
        break;
    case QAbstractOAuth::ContentType::WwwFormUrlEncoded: {
        QUrlQuery query;
        for (auto it = parameters.begin(), end = parameters.end(); it != end; ++it)
            query.addQueryItem(it.key(), it->toString());
        data = query.toString(QUrl::FullyEncoded).toLatin1();
        break;
    }
    }
    return data;
}

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
//  -----------------------------------------------------------------------

//  QAbstractOAuth *QAbstractOAuthPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractOAuth *ritual_ZN21QAbstractOAuthPrivate6q_funcEv(
    QAbstractOAuthPrivate *self) {
  return self->q_func();
}

//  const QAbstractOAuth *QAbstractOAuthPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractOAuth *ritual_ZNK21QAbstractOAuthPrivate6q_funcEv(
    const QAbstractOAuthPrivate *self) {
  return self->q_func();
}

//  QNetworkAccessManager *QAbstractOAuthPrivate::networkAccessManager()
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZN21QAbstractOAuthPrivate20networkAccessManagerEv(
    QAbstractOAuthPrivate *self) {
  return self->networkAccessManager();
}

//  void QAbstractOAuthPrivate::setStatus(QAbstractOAuth::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractOAuthPrivate9setStatusEN14QAbstractOAuth6StatusE(
    QAbstractOAuthPrivate *self,
    QAbstractOAuth::Status status) {
  self->setStatus(status);
}

//  QByteArray QAbstractOAuthPrivate::generateRandomBase64String(quint8
//      length)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN21QAbstractOAuthPrivate26generateRandomBase64StringEh(
    quint8 length) {
  return new QByteArray(
      QAbstractOAuthPrivate::generateRandomBase64String(
          length));
}

//  void QAbstractOAuthPrivate::setExtraTokens(const QVariantMap &tokens)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractOAuthPrivate14setExtraTokensERK4QMapI7QString8QVariantE(
    QAbstractOAuthPrivate *self,
    const QMap<QString, QVariant> *tokens) {
  self->setExtraTokens(*tokens);
}

//  QByteArray QAbstractOAuthPrivate::convertParameters(const QVariantMap
//      &parameters)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN21QAbstractOAuthPrivate17convertParametersERK4QMapI7QString8QVariantE(
    QAbstractOAuthPrivate *self,
    const QMap<QString, QVariant> *parameters) {
  return new QByteArray(self->convertParameters(*parameters));
}

//  void QAbstractOAuthPrivate::addContentTypeHeaders(QNetworkRequest
//      *request)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractOAuthPrivate21addContentTypeHeadersEP15QNetworkRequest(
    QAbstractOAuthPrivate *self,
    QNetworkRequest *request) {
  self->addContentTypeHeaders(request);
}
