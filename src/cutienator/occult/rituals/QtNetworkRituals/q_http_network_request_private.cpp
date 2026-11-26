//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkheader.cpp, line 12, as _ZN25QHttpNetworkHeaderPrivateC2ERK4QUrl
inline QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const QUrl &newUrl)
    :url(newUrl)
{
}

//  from src/network/access/qhttpnetworkheader.cpp, line 68, as _ZNK25QHttpNetworkHeaderPrivateeqERKS_
inline bool QHttpNetworkHeaderPrivate::operator==(const QHttpNetworkHeaderPrivate &other) const
{
   return (url == other.url);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 72, as _ZNK19QHttpNetworkRequest10methodNameEv
inline QByteArray QHttpNetworkRequest::methodName() const
{
    switch (d->operation) {
    case QHttpNetworkRequest::Get:
        return "GET";
    case QHttpNetworkRequest::Head:
        return "HEAD";
    case QHttpNetworkRequest::Post:
        return "POST";
    case QHttpNetworkRequest::Options:
        return "OPTIONS";
    case QHttpNetworkRequest::Put:
        return "PUT";
    case QHttpNetworkRequest::Delete:
        return "DELETE";
    case QHttpNetworkRequest::Trace:
        return "TRACE";
    case QHttpNetworkRequest::Connect:
        return "CONNECT";
    case QHttpNetworkRequest::Custom:
        return d->customVerb;
    default:
        break;
    }
    return QByteArray();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 99, as _ZNK19QHttpNetworkRequest3uriEb
inline QByteArray QHttpNetworkRequest::uri(bool throughProxy) const
{
    QUrl::FormattingOptions format(QUrl::RemoveFragment | QUrl::RemoveUserInfo | QUrl::FullyEncoded);

    // for POST, query data is sent as content
    if (d->operation == QHttpNetworkRequest::Post && !d->uploadByteDevice)
        format |= QUrl::RemoveQuery;
    // for requests through proxy, the Request-URI contains full url
    if (!throughProxy)
        format |= QUrl::RemoveScheme | QUrl::RemoveAuthority;
    QUrl copy = d->url;
    if (copy.path().isEmpty())
        copy.setPath(QStringLiteral("/"));
    else
        format |= QUrl::NormalizePathSegments;
    QByteArray uri = copy.toEncoded(format);
    return uri;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 14, as _ZN26QHttpNetworkRequestPrivateC1EN19QHttpNetworkRequest9OperationENS0_8PriorityERK4QUrl
inline QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(QHttpNetworkRequest::Operation op,
        QHttpNetworkRequest::Priority pri, const QUrl &newUrl)
    : QHttpNetworkHeaderPrivate(newUrl), operation(op), priority(pri), uploadByteDevice(nullptr),
      autoDecompress(false), pipeliningAllowed(false), http2Allowed(true),
      http2Direct(false), withCredentials(true), preConnect(false), redirectCount(0),
      redirectPolicy(QNetworkRequest::ManualRedirectPolicy)
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 23, as _ZN26QHttpNetworkRequestPrivateC1ERKS_
inline QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(const QHttpNetworkRequestPrivate &other) // = default
    : QHttpNetworkHeaderPrivate(other),
      operation(other.operation),
      customVerb(other.customVerb),
      fullLocalServerName(other.fullLocalServerName),
      priority(other.priority),
      uploadByteDevice(other.uploadByteDevice),
      autoDecompress(other.autoDecompress),
      pipeliningAllowed(other.pipeliningAllowed),
      http2Allowed(other.http2Allowed),
      http2Direct(other.http2Direct),
      h2cAllowed(other.h2cAllowed),
      withCredentials(other.withCredentials),
      ssl(other.ssl),
      preConnect(other.preConnect),
      needResendWithCredentials(other.needResendWithCredentials),
      redirectCount(other.redirectCount),
      redirectPolicy(other.redirectPolicy),
      peerVerifyName(other.peerVerifyName)
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 45, as _ZN26QHttpNetworkRequestPrivateD1Ev
inline QHttpNetworkRequestPrivate::~QHttpNetworkRequestPrivate()
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 49, as _ZNK26QHttpNetworkRequestPrivateeqERKS_
inline bool QHttpNetworkRequestPrivate::operator==(const QHttpNetworkRequestPrivate &other) const
{
    return QHttpNetworkHeaderPrivate::operator==(other)
        && (operation == other.operation)
        && (fullLocalServerName == other.fullLocalServerName)
        && (priority == other.priority)
        && (uploadByteDevice == other.uploadByteDevice)
        && (autoDecompress == other.autoDecompress)
        && (pipeliningAllowed == other.pipeliningAllowed)
        && (http2Allowed == other.http2Allowed)
        && (http2Direct == other.http2Direct)
        && (h2cAllowed == other.h2cAllowed)
        // we do not clear the customVerb in setOperation
        && (operation != QHttpNetworkRequest::Custom || (customVerb == other.customVerb))
        && (withCredentials == other.withCredentials)
        && (ssl == other.ssl)
        && (preConnect == other.preConnect)
        && (redirectPolicy == other.redirectPolicy)
        && (peerVerifyName == other.peerVerifyName)
        && (needResendWithCredentials == other.needResendWithCredentials)
        ;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 118, as _ZN26QHttpNetworkRequestPrivate6headerERK19QHttpNetworkRequestb
inline QByteArray QHttpNetworkRequestPrivate::header(const QHttpNetworkRequest &request, bool throughProxy)
{
    const QHttpHeaders headers = request.header();
    QByteArray ba;
    ba.reserve(40 + headers.size() * 25); // very rough lower bound estimation

    ba += request.methodName();
    ba += ' ';
    ba += request.uri(throughProxy);

    ba += " HTTP/";
    ba += QByteArray::number(request.majorVersion());
    ba += '.';
    ba += QByteArray::number(request.minorVersion());
    ba += "\r\n";

    constexpr auto titlecase = [](QByteArrayView name) {
        std::string n;
        n.reserve(size_t(name.size()));
        bool toUpperNext = true;
        for (char c : name) {
            n += toUpperNext ? QtMiscUtils::toAsciiUpper(c) : c;
            toUpperNext = c == '-';
        }
        return n;
    };

    for (qsizetype i = 0; i < headers.size(); ++i) {
        ba += titlecase(headers.nameAt(i));
        ba += ": ";
        ba += headers.valueAt(i);
        ba += "\r\n";
    }
    if (request.d->operation == QHttpNetworkRequest::Post) {
        // add content type, if not set in the request
        if (request.headerField("content-type").isEmpty() && ((request.d->uploadByteDevice && request.d->uploadByteDevice->size() > 0) || request.d->url.hasQuery())) {
            //Content-Type is mandatory. We can't say anything about the encoding, but x-www-form-urlencoded is the most likely to work.
            //This warning indicates a bug in application code not setting a required header.
            //Note that if using QHttpMultipart, the content-type is set in QNetworkAccessManagerPrivate::prepareMultipart already
            qWarning("content-type missing in HTTP POST, defaulting to application/x-www-form-urlencoded. Use QNetworkRequest::setHeader() to fix this problem.");
            ba += "Content-Type: application/x-www-form-urlencoded\r\n";
        }
        if (!request.d->uploadByteDevice && request.d->url.hasQuery()) {
            QByteArray query = request.d->url.query(QUrl::FullyEncoded).toLatin1();
            ba += "Content-Length: ";
            ba += QByteArray::number(query.size());
            ba += "\r\n\r\n";
            ba += query;
        } else {
            ba += "\r\n";
        }
    } else {
        ba += "\r\n";
    }
     return ba;
}
//  -----------------------------------------------------------------------

//  QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(QHttpNetworkReques
//      t::Operation op, QHttpNetworkRequest::Priority pri, const QUrl
//      &newUrl)
extern "C" Q_DECL_EXPORT
QHttpNetworkRequestPrivate *ritual_ZN26QHttpNetworkRequestPrivateC1EN19QHttpNetworkRequest9OperationENS0_8PriorityERK4QUrl(
    QHttpNetworkRequest::Operation op,
    QHttpNetworkRequest::Priority pri,
    const QUrl *newUrl) {
  return new QHttpNetworkRequestPrivate(op, pri, *newUrl);
}

//  QHttpNetworkRequestPrivate::QHttpNetworkRequestPrivate(const
//      QHttpNetworkRequestPrivate &other)
extern "C" Q_DECL_EXPORT
QHttpNetworkRequestPrivate *ritual_ZN26QHttpNetworkRequestPrivateC1ERKS_(
    const QHttpNetworkRequestPrivate *other) {
  return new QHttpNetworkRequestPrivate(*other);
}

//  QHttpNetworkRequestPrivate::~QHttpNetworkRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHttpNetworkRequestPrivateD1Ev(
    QHttpNetworkRequestPrivate *self) {
  delete self;
}

//  bool QHttpNetworkRequestPrivate::operator==(const
//      QHttpNetworkRequestPrivate &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QHttpNetworkRequestPrivateeqERKS_(
    const QHttpNetworkRequestPrivate *self,
    const QHttpNetworkRequestPrivate *other) {
  return self->operator==(*other);
}

//  QByteArray QHttpNetworkRequestPrivate::header(const QHttpNetworkRequest
//      &request, bool throughProxy)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN26QHttpNetworkRequestPrivate6headerERK19QHttpNetworkRequestb(
    const QHttpNetworkRequest *request,
    bool throughProxy) {
  return new QByteArray(
      QHttpNetworkRequestPrivate::header(
          *request,
          throughProxy));
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
