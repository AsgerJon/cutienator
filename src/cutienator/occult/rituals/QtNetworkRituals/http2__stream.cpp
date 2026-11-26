//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/http2streams_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/http2streams_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#include <QtNetwork/private/http2streams_p.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 183, as _ZN19QHttpNetworkRequestC1ERKS_
inline QHttpNetworkRequest::QHttpNetworkRequest(const QHttpNetworkRequest &other)
    : QHttpNetworkHeader(other), d(other.d)
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 311, as _ZNK19QHttpNetworkRequest8priorityEv
inline QHttpNetworkRequest::Priority QHttpNetworkRequest::priority() const
{
    return d->priority;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 376, as _ZNK19QHttpNetworkRequest16uploadByteDeviceEv
inline QNonContiguousByteDevice* QHttpNetworkRequest::uploadByteDevice() const
{
    return d->uploadByteDevice;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttpnetworkheader.cpp, line 9, as _ZN18QHttpNetworkHeaderD2Ev
inline QHttpNetworkHeader::~QHttpNetworkHeader()
    = default;

//  from src/network/access/qhttpnetworkrequest.cpp, line 264, as _ZN19QHttpNetworkRequest14setHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkRequest::setHeaderField(const QByteArray &name, const QByteArray &data)
{
    d->setHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 249, as _ZN19QHttpNetworkRequest16setContentLengthEx
inline void QHttpNetworkRequest::setContentLength(qint64 length)
{
    d->setContentLength(length);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 196, as _ZN19QHttpNetworkRequest6setUrlERK4QUrl
inline void QHttpNetworkRequest::setUrl(const QUrl &url)
{
    d->url = url;
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 45, as _ZN26QHttpNetworkRequestPrivateD1Ev
inline QHttpNetworkRequestPrivate::~QHttpNetworkRequestPrivate()
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 259, as _ZNK19QHttpNetworkRequest11headerFieldE14QByteArrayViewRK10QByteArray
inline QByteArray QHttpNetworkRequest::headerField(QByteArrayView name, const QByteArray &defaultValue) const
{
    return d->headerField(name, defaultValue);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 381, as _ZNK19QHttpNetworkRequest12majorVersionEv
inline int QHttpNetworkRequest::majorVersion() const
{
    return 1;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 386, as _ZNK19QHttpNetworkRequest12minorVersionEv
inline int QHttpNetworkRequest::minorVersion() const
{
    return 1;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 244, as _ZNK19QHttpNetworkRequest13contentLengthEv
inline qint64 QHttpNetworkRequest::contentLength() const
{
    return d->contentLength();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 192, as _ZNK19QHttpNetworkRequest3urlEv
inline QUrl QHttpNetworkRequest::url() const
{
    return d->url;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 254, as _ZNK19QHttpNetworkRequest6headerEv
inline QHttpHeaders QHttpNetworkRequest::header() const
{
    return d->parser.headers();
}

//  from src/network/access/http2/http2streams.cpp, line 38, as _ZNK5Http26Stream5replyEv
namespace Http2 {
inline QHttpNetworkReply *Stream::reply() const
{
    return httpPair.second;
}
}  // namespace Http2

//  from src/network/access/http2/http2streams.cpp, line 48, as _ZN5Http26Stream7requestEv
namespace Http2 {
inline QHttpNetworkRequest &Stream::request()
{
    return httpPair.first;
}
}  // namespace Http2

//  from src/network/access/http2/http2streams.cpp, line 53, as _ZNK5Http26Stream8priorityEv
namespace Http2 {
inline QHttpNetworkRequest::Priority Stream::priority() const
{
    return httpPair.first.priority();
}
}  // namespace Http2

//  from src/network/access/http2/http2streams.cpp, line 58, as _ZNK5Http26Stream6weightEv
namespace Http2 {
inline uchar Stream::weight() const
{
    switch (priority()) {
    case QHttpNetworkRequest::LowPriority:
        return 0;
    case QHttpNetworkRequest::NormalPriority:
        return 127;
    case QHttpNetworkRequest::HighPriority:
    default:
        return 255;
    }
}
}  // namespace Http2

//  from src/network/access/http2/http2streams.cpp, line 71, as _ZNK5Http26Stream4dataEv
namespace Http2 {
inline QNonContiguousByteDevice *Stream::data() const
{
    return httpPair.first.uploadByteDevice();
}
}  // namespace Http2
//  -----------------------------------------------------------------------

//  QHttpNetworkReply *Http2::Stream::reply() const
extern "C" Q_DECL_EXPORT
QHttpNetworkReply *ritual_ZNK5Http26Stream5replyEv(
    const Http2::Stream *self) {
  return self->reply();
}

//  QHttpNetworkRequest &Http2::Stream::request()
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest *ritual_ZN5Http26Stream7requestEv(Http2::Stream *self) {
  return &(self->request());
}

//  QHttpNetworkRequest::Priority Http2::Stream::priority() const
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest::Priority ritual_ZNK5Http26Stream8priorityEv(
    const Http2::Stream *self) {
  return self->priority();
}

//  uchar Http2::Stream::weight() const
extern "C" Q_DECL_EXPORT
uchar ritual_ZNK5Http26Stream6weightEv(const Http2::Stream *self) {
  return self->weight();
}

//  QNonContiguousByteDevice *Http2::Stream::data() const
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZNK5Http26Stream4dataEv(
    const Http2::Stream *self) {
  return self->data();
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
