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
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qbytearrayview.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <cstring>
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

//  from src/network/access/qhttpnetworkheader.cpp, line 53, as _ZN25QHttpNetworkHeaderPrivate18prependHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkHeaderPrivate::prependHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.prependHeaderField(name, data);
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

//  from src/network/access/qhttpnetworkheader.cpp, line 63, as _ZN25QHttpNetworkHeaderPrivate12clearHeadersEv
inline void QHttpNetworkHeaderPrivate::clearHeaders()
{
    parser.clearHeaders();
}

//  from src/network/access/qhttpnetworkheader.cpp, line 17, as _ZNK25QHttpNetworkHeaderPrivate13contentLengthEv
inline qint64 QHttpNetworkHeaderPrivate::contentLength() const
{
    bool ok = false;
    // We are not using the headerField() method here because servers might send us multiple content-length
    // headers which is crap (see QTBUG-15311). Therefore just take the first content-length header field.
    QByteArray value = parser.firstHeaderField("content-length");
    qint64 length = value.toULongLong(&ok);
    if (ok)
        return length;
    return -1; // the header field is not set
}

//  from src/network/access/qhttpnetworkheader.cpp, line 29, as _ZN25QHttpNetworkHeaderPrivate16setContentLengthEx
inline void QHttpNetworkHeaderPrivate::setContentLength(qint64 length)
{
    setHeaderField("Content-Length", QByteArray::number(length));
}

//  from src/network/access/qhttpnetworkheader.cpp, line 34, as _ZNK25QHttpNetworkHeaderPrivate11headerFieldE14QByteArrayViewRK10QByteArray
inline QByteArray QHttpNetworkHeaderPrivate::headerField(QByteArrayView name, const QByteArray &defaultValue) const
{
    QList<QByteArray> allValues = headerFieldValues(name);
    if (allValues.isEmpty())
        return defaultValue;
    else
        return allValues.join(", ");
}

//  from src/network/access/qhttpnetworkheader.cpp, line 48, as _ZN25QHttpNetworkHeaderPrivate14setHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkHeaderPrivate::setHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.setHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkheader.cpp, line 43, as _ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteArrayView
inline QList<QByteArray> QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name) const
{
    return parser.headerFieldValues(name);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 192, as _ZNK19QHttpNetworkRequest3urlEv
inline QUrl QHttpNetworkRequest::url() const
{
    return d->url;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 196, as _ZN19QHttpNetworkRequest6setUrlERK4QUrl
inline void QHttpNetworkRequest::setUrl(const QUrl &url)
{
    d->url = url;
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 249, as _ZN19QHttpNetworkRequest16setContentLengthEx
inline void QHttpNetworkRequest::setContentLength(qint64 length)
{
    d->setContentLength(length);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 254, as _ZNK19QHttpNetworkRequest6headerEv
inline QHttpHeaders QHttpNetworkRequest::header() const
{
    return d->parser.headers();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 259, as _ZNK19QHttpNetworkRequest11headerFieldE14QByteArrayViewRK10QByteArray
inline QByteArray QHttpNetworkRequest::headerField(QByteArrayView name, const QByteArray &defaultValue) const
{
    return d->headerField(name, defaultValue);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 264, as _ZN19QHttpNetworkRequest14setHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkRequest::setHeaderField(const QByteArray &name, const QByteArray &data)
{
    d->setHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 269, as _ZN19QHttpNetworkRequest18prependHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkRequest::prependHeaderField(const QByteArray &name, const QByteArray &data)
{
    d->prependHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 274, as _ZN19QHttpNetworkRequest12clearHeadersEv
inline void QHttpNetworkRequest::clearHeaders()
{
    d->clearHeaders();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 291, as _ZNK19QHttpNetworkRequest9operationEv
inline QHttpNetworkRequest::Operation QHttpNetworkRequest::operation() const
{
    return d->operation;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 296, as _ZN19QHttpNetworkRequest12setOperationENS_9OperationE
inline void QHttpNetworkRequest::setOperation(Operation operation)
{
    d->operation = operation;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 301, as _ZNK19QHttpNetworkRequest10customVerbEv
inline QByteArray QHttpNetworkRequest::customVerb() const
{
    return d->customVerb;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 306, as _ZN19QHttpNetworkRequest13setCustomVerbERK10QByteArray
inline void QHttpNetworkRequest::setCustomVerb(const QByteArray &customVerb)
{
    d->customVerb = customVerb;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 311, as _ZNK19QHttpNetworkRequest8priorityEv
inline QHttpNetworkRequest::Priority QHttpNetworkRequest::priority() const
{
    return d->priority;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 316, as _ZN19QHttpNetworkRequest11setPriorityENS_8PriorityE
inline void QHttpNetworkRequest::setPriority(Priority priority)
{
    d->priority = priority;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 321, as _ZNK19QHttpNetworkRequest19isPipeliningAllowedEv
inline bool QHttpNetworkRequest::isPipeliningAllowed() const
{
    return d->pipeliningAllowed;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 326, as _ZN19QHttpNetworkRequest20setPipeliningAllowedEb
inline void QHttpNetworkRequest::setPipeliningAllowed(bool b)
{
    d->pipeliningAllowed = b;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 331, as _ZNK19QHttpNetworkRequest14isHTTP2AllowedEv
inline bool QHttpNetworkRequest::isHTTP2Allowed() const
{
    return d->http2Allowed;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 336, as _ZN19QHttpNetworkRequest15setHTTP2AllowedEb
inline void QHttpNetworkRequest::setHTTP2Allowed(bool b)
{
    d->http2Allowed = b;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 341, as _ZNK19QHttpNetworkRequest13isHTTP2DirectEv
inline bool QHttpNetworkRequest::isHTTP2Direct() const
{
    return d->http2Direct;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 346, as _ZN19QHttpNetworkRequest14setHTTP2DirectEb
inline void QHttpNetworkRequest::setHTTP2Direct(bool b)
{
    d->http2Direct = b;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 351, as _ZNK19QHttpNetworkRequest12isH2cAllowedEv
inline bool QHttpNetworkRequest::isH2cAllowed() const
{
    return d->h2cAllowed;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 356, as _ZN19QHttpNetworkRequest13setH2cAllowedEb
inline void QHttpNetworkRequest::setH2cAllowed(bool b)
{
    d->h2cAllowed = b;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 361, as _ZNK19QHttpNetworkRequest15withCredentialsEv
inline bool QHttpNetworkRequest::withCredentials() const
{
    return d->withCredentials;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 366, as _ZN19QHttpNetworkRequest18setWithCredentialsEb
inline void QHttpNetworkRequest::setWithCredentials(bool b)
{
    d->withCredentials = b;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 201, as _ZNK19QHttpNetworkRequest5isSslEv
inline bool QHttpNetworkRequest::isSsl() const
{
    return d->ssl;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 205, as _ZN19QHttpNetworkRequest6setSslEb
inline void QHttpNetworkRequest::setSsl(bool s)
{
    d->ssl = s;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 210, as _ZNK19QHttpNetworkRequest12isPreConnectEv
inline bool QHttpNetworkRequest::isPreConnect() const
{
    return d->preConnect;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 214, as _ZN19QHttpNetworkRequest13setPreConnectEb
inline void QHttpNetworkRequest::setPreConnect(bool preConnect)
{
    d->preConnect = preConnect;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 219, as _ZNK19QHttpNetworkRequest17isFollowRedirectsEv
inline bool QHttpNetworkRequest::isFollowRedirects() const
{
    return d->redirectPolicy != QNetworkRequest::ManualRedirectPolicy;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 224, as _ZN19QHttpNetworkRequest17setRedirectPolicyEN15QNetworkRequest14RedirectPolicyE
inline void QHttpNetworkRequest::setRedirectPolicy(QNetworkRequest::RedirectPolicy policy)
{
    d->redirectPolicy = policy;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 229, as _ZNK19QHttpNetworkRequest14redirectPolicyEv
inline QNetworkRequest::RedirectPolicy QHttpNetworkRequest::redirectPolicy() const
{
    return d->redirectPolicy;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 234, as _ZNK19QHttpNetworkRequest13redirectCountEv
inline int QHttpNetworkRequest::redirectCount() const
{
    return d->redirectCount;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 239, as _ZN19QHttpNetworkRequest16setRedirectCountEi
inline void QHttpNetworkRequest::setRedirectCount(int count)
{
    d->redirectCount = count;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 371, as _ZN19QHttpNetworkRequest19setUploadByteDeviceEP24QNonContiguousByteDevice
inline void QHttpNetworkRequest::setUploadByteDevice(QNonContiguousByteDevice *bd)
{
    d->uploadByteDevice = bd;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 376, as _ZNK19QHttpNetworkRequest16uploadByteDeviceEv
inline QNonContiguousByteDevice* QHttpNetworkRequest::uploadByteDevice() const
{
    return d->uploadByteDevice;
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 391, as _ZNK19QHttpNetworkRequest14peerVerifyNameEv
inline QString QHttpNetworkRequest::peerVerifyName() const
{
    return d->peerVerifyName;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 396, as _ZN19QHttpNetworkRequest17setPeerVerifyNameERK7QString
inline void QHttpNetworkRequest::setPeerVerifyName(const QString &peerName)
{
    d->peerVerifyName = peerName;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 401, as _ZNK19QHttpNetworkRequest19fullLocalServerNameEv
inline QString QHttpNetworkRequest::fullLocalServerName() const
{
    return d->fullLocalServerName;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 406, as _ZN19QHttpNetworkRequest22setFullLocalServerNameERK7QString
inline void QHttpNetworkRequest::setFullLocalServerName(const QString &fullServerName)
{
    d->fullLocalServerName = fullServerName;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 411, as _ZNK19QHttpNetworkRequest18methodIsIdempotentEv
inline bool QHttpNetworkRequest::methodIsIdempotent() const
{
    using Op = Operation;
    constexpr auto knownSafe = std::array{ Op::Get, Op::Head, Op::Put, Op::Trace, Op::Options };
    return std::any_of(knownSafe.begin(), knownSafe.end(),
                       [currentOp = d->operation](auto op) { return op == currentOp; });
}
//  -----------------------------------------------------------------------

//  A QHttpNetworkRequest that Python can take functions over in. Every QHttpNetworkRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(http)
typedef const QUrl * (*CuteQHttpNetworkRequestCall0)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkRequestCall1)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef int (*CuteQHttpNetworkRequestCall2)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef int (*CuteQHttpNetworkRequestCall3)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef qint64 (*CuteQHttpNetworkRequestCall4)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkRequestCall5)(const void *, qint64, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef const QHttpHeaders * (*CuteQHttpNetworkRequestCall6)(const void *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef const QByteArray * (*CuteQHttpNetworkRequestCall7)(const void *, const QByteArrayView *, const QByteArray *, int *);
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
typedef void (*CuteQHttpNetworkRequestCall8)(const void *, const QByteArray *, const QByteArray *, int *);
#endif  // QT_CONFIG(http)
class CuteQHttpNetworkRequest : public QHttpNetworkRequest {
public:
  using QHttpNetworkRequest::QHttpNetworkRequest;
  CuteQHttpNetworkRequest(const QHttpNetworkRequest &other) : QHttpNetworkRequest(other) {}
  void *taken[9] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader3urlEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader6setUrlERK4QUrl")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader12majorVersionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader12minorVersionEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader13contentLengthEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader16setContentLengthEx")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader6headerEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZNK18QHttpNetworkHeader11headerFieldE14QByteArrayViewRK10QByteArray")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
#if QT_CONFIG(http)
    if (!std::strcmp(key, "_ZN18QHttpNetworkHeader14setHeaderFieldERK10QByteArrayS2_")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(http)
    return false;
  }

#if QT_CONFIG(http)
  //  QUrl QHttpNetworkRequest::url() const
  QUrl url() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall0 call = reinterpret_cast<CuteQHttpNetworkRequestCall0>(taken[0]);
      const QUrl * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHttpNetworkRequest::url();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkRequest::setUrl(const QUrl &url)
  void setUrl(const QUrl &url) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall1 call = reinterpret_cast<CuteQHttpNetworkRequestCall1>(taken[1]);
      call(this, &url, &handled);
      if (handled) return;
    }
    QHttpNetworkRequest::setUrl(url);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  int QHttpNetworkRequest::majorVersion() const
  int majorVersion() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall2 call = reinterpret_cast<CuteQHttpNetworkRequestCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpNetworkRequest::majorVersion();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  int QHttpNetworkRequest::minorVersion() const
  int minorVersion() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall3 call = reinterpret_cast<CuteQHttpNetworkRequestCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpNetworkRequest::minorVersion();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  qint64 QHttpNetworkRequest::contentLength() const
  qint64 contentLength() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall4 call = reinterpret_cast<CuteQHttpNetworkRequestCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QHttpNetworkRequest::contentLength();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkRequest::setContentLength(qint64 length)
  void setContentLength(qint64 length) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall5 call = reinterpret_cast<CuteQHttpNetworkRequestCall5>(taken[5]);
      call(this, length, &handled);
      if (handled) return;
    }
    QHttpNetworkRequest::setContentLength(length);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  QHttpHeaders QHttpNetworkRequest::header() const
  QHttpHeaders header() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall6 call = reinterpret_cast<CuteQHttpNetworkRequestCall6>(taken[6]);
      const QHttpHeaders * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QHttpNetworkRequest::header();
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  QByteArray QHttpNetworkRequest::headerField(QByteArrayView name,
  //      const QByteArray &defaultValue) const
  QByteArray headerField(
      QByteArrayView name,
      const QByteArray &defaultValue) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall7 call = reinterpret_cast<CuteQHttpNetworkRequestCall7>(taken[7]);
      const QByteArray * given = call(this, &name, &defaultValue, &handled);
      if (handled && given) return *given;
    }
    return QHttpNetworkRequest::headerField(name, defaultValue);
  }
#endif  // QT_CONFIG(http)

#if QT_CONFIG(http)
  //  void QHttpNetworkRequest::setHeaderField(const QByteArray &name,
  //      const QByteArray &data)
  void setHeaderField(
      const QByteArray &name,
      const QByteArray &data) override {
    if (taken[8]) {
      int handled = 0;
      CuteQHttpNetworkRequestCall8 call = reinterpret_cast<CuteQHttpNetworkRequestCall8>(taken[8]);
      call(this, &name, &data, &handled);
      if (handled) return;
    }
    QHttpNetworkRequest::setHeaderField(name, data);
  }
#endif  // QT_CONFIG(http)
};

//  QHttpNetworkRequest::~QHttpNetworkRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequestD1Ev(QHttpNetworkRequest *self) {
  delete self;
}

//  QUrl QHttpNetworkRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK19QHttpNetworkRequest3urlEv(
    const QHttpNetworkRequest *self) {
  return new QUrl(self->url());
}

//  void QHttpNetworkRequest::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest6setUrlERK4QUrl(
    QHttpNetworkRequest *self,
    const QUrl *url) {
  self->setUrl(*url);
}

//  int QHttpNetworkRequest::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QHttpNetworkRequest12majorVersionEv(
    const QHttpNetworkRequest *self) {
  return self->majorVersion();
}

//  int QHttpNetworkRequest::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QHttpNetworkRequest12minorVersionEv(
    const QHttpNetworkRequest *self) {
  return self->minorVersion();
}

//  qint64 QHttpNetworkRequest::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QHttpNetworkRequest13contentLengthEv(
    const QHttpNetworkRequest *self) {
  return self->contentLength();
}

//  void QHttpNetworkRequest::setContentLength(qint64 length)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest16setContentLengthEx(
    QHttpNetworkRequest *self,
    qint64 length) {
  self->setContentLength(length);
}

//  QHttpHeaders QHttpNetworkRequest::header() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_ZNK19QHttpNetworkRequest6headerEv(
    const QHttpNetworkRequest *self) {
  return new QHttpHeaders(self->header());
}

//  QByteArray QHttpNetworkRequest::headerField(QByteArrayView name, const
//      QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QHttpNetworkRequest11headerFieldE14QByteArrayViewRK10QByteArray(
    const QHttpNetworkRequest *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(self->headerField(*name, *defaultValue));
}

//  void QHttpNetworkRequest::setHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest14setHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkRequest *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->setHeaderField(*name, *data);
}

//  void QHttpNetworkRequest::prependHeaderField(const QByteArray &name,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest18prependHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkRequest *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->prependHeaderField(*name, *data);
}

//  void QHttpNetworkRequest::clearHeaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest12clearHeadersEv(
    QHttpNetworkRequest *self) {
  self->clearHeaders();
}

//  Operation QHttpNetworkRequest::operation() const
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest::Operation ritual_ZNK19QHttpNetworkRequest9operationEv(
    const QHttpNetworkRequest *self) {
  return self->operation();
}

//  void QHttpNetworkRequest::setOperation(Operation operation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest12setOperationENS_9OperationE(
    QHttpNetworkRequest *self,
    QHttpNetworkRequest::Operation operation) {
  self->setOperation(operation);
}

//  QByteArray QHttpNetworkRequest::customVerb() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QHttpNetworkRequest10customVerbEv(
    const QHttpNetworkRequest *self) {
  return new QByteArray(self->customVerb());
}

//  void QHttpNetworkRequest::setCustomVerb(const QByteArray
//      &customOperation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest13setCustomVerbERK10QByteArray(
    QHttpNetworkRequest *self,
    const QByteArray *customOperation) {
  self->setCustomVerb(*customOperation);
}

//  Priority QHttpNetworkRequest::priority() const
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest::Priority ritual_ZNK19QHttpNetworkRequest8priorityEv(
    const QHttpNetworkRequest *self) {
  return self->priority();
}

//  void QHttpNetworkRequest::setPriority(Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest11setPriorityENS_8PriorityE(
    QHttpNetworkRequest *self,
    QHttpNetworkRequest::Priority priority) {
  self->setPriority(priority);
}

//  bool QHttpNetworkRequest::isPipeliningAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest19isPipeliningAllowedEv(
    const QHttpNetworkRequest *self) {
  return self->isPipeliningAllowed();
}

//  void QHttpNetworkRequest::setPipeliningAllowed(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest20setPipeliningAllowedEb(
    QHttpNetworkRequest *self,
    bool b) {
  self->setPipeliningAllowed(b);
}

//  bool QHttpNetworkRequest::isHTTP2Allowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest14isHTTP2AllowedEv(
    const QHttpNetworkRequest *self) {
  return self->isHTTP2Allowed();
}

//  void QHttpNetworkRequest::setHTTP2Allowed(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest15setHTTP2AllowedEb(
    QHttpNetworkRequest *self,
    bool b) {
  self->setHTTP2Allowed(b);
}

//  bool QHttpNetworkRequest::isHTTP2Direct() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest13isHTTP2DirectEv(
    const QHttpNetworkRequest *self) {
  return self->isHTTP2Direct();
}

//  void QHttpNetworkRequest::setHTTP2Direct(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest14setHTTP2DirectEb(
    QHttpNetworkRequest *self,
    bool b) {
  self->setHTTP2Direct(b);
}

//  bool QHttpNetworkRequest::isH2cAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest12isH2cAllowedEv(
    const QHttpNetworkRequest *self) {
  return self->isH2cAllowed();
}

//  void QHttpNetworkRequest::setH2cAllowed(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest13setH2cAllowedEb(
    QHttpNetworkRequest *self,
    bool b) {
  self->setH2cAllowed(b);
}

//  bool QHttpNetworkRequest::withCredentials() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest15withCredentialsEv(
    const QHttpNetworkRequest *self) {
  return self->withCredentials();
}

//  void QHttpNetworkRequest::setWithCredentials(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest18setWithCredentialsEb(
    QHttpNetworkRequest *self,
    bool b) {
  self->setWithCredentials(b);
}

//  bool QHttpNetworkRequest::isSsl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest5isSslEv(
    const QHttpNetworkRequest *self) {
  return self->isSsl();
}

//  void QHttpNetworkRequest::setSsl(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest6setSslEb(
    QHttpNetworkRequest *self,
    bool a0) {
  self->setSsl(a0);
}

//  bool QHttpNetworkRequest::isPreConnect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest12isPreConnectEv(
    const QHttpNetworkRequest *self) {
  return self->isPreConnect();
}

//  void QHttpNetworkRequest::setPreConnect(bool preConnect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest13setPreConnectEb(
    QHttpNetworkRequest *self,
    bool preConnect) {
  self->setPreConnect(preConnect);
}

//  bool QHttpNetworkRequest::isFollowRedirects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest17isFollowRedirectsEv(
    const QHttpNetworkRequest *self) {
  return self->isFollowRedirects();
}

//  void
//      QHttpNetworkRequest::setRedirectPolicy(QNetworkRequest::RedirectPolic
//      y policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest17setRedirectPolicyEN15QNetworkRequest14RedirectPolicyE(
    QHttpNetworkRequest *self,
    QNetworkRequest::RedirectPolicy policy) {
  self->setRedirectPolicy(policy);
}

//  QNetworkRequest::RedirectPolicy QHttpNetworkRequest::redirectPolicy()
//      const
extern "C" Q_DECL_EXPORT
QNetworkRequest::RedirectPolicy ritual_ZNK19QHttpNetworkRequest14redirectPolicyEv(
    const QHttpNetworkRequest *self) {
  return self->redirectPolicy();
}

//  int QHttpNetworkRequest::redirectCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QHttpNetworkRequest13redirectCountEv(
    const QHttpNetworkRequest *self) {
  return self->redirectCount();
}

//  void QHttpNetworkRequest::setRedirectCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest16setRedirectCountEi(
    QHttpNetworkRequest *self,
    int count) {
  self->setRedirectCount(count);
}

//  void QHttpNetworkRequest::setUploadByteDevice(QNonContiguousByteDevice
//      *bd)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest19setUploadByteDeviceEP24QNonContiguousByteDevice(
    QHttpNetworkRequest *self,
    QNonContiguousByteDevice *bd) {
  self->setUploadByteDevice(bd);
}

//  QNonContiguousByteDevice *QHttpNetworkRequest::uploadByteDevice() const
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZNK19QHttpNetworkRequest16uploadByteDeviceEv(
    const QHttpNetworkRequest *self) {
  return self->uploadByteDevice();
}

//  QByteArray QHttpNetworkRequest::methodName() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QHttpNetworkRequest10methodNameEv(
    const QHttpNetworkRequest *self) {
  return new QByteArray(self->methodName());
}

//  QByteArray QHttpNetworkRequest::uri(bool throughProxy) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QHttpNetworkRequest3uriEb(
    const QHttpNetworkRequest *self,
    bool throughProxy) {
  return new QByteArray(self->uri(throughProxy));
}

//  QString QHttpNetworkRequest::peerVerifyName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QHttpNetworkRequest14peerVerifyNameEv(
    const QHttpNetworkRequest *self) {
  return new QString(self->peerVerifyName());
}

//  void QHttpNetworkRequest::setPeerVerifyName(const QString &peerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest17setPeerVerifyNameERK7QString(
    QHttpNetworkRequest *self,
    const QString *peerName) {
  self->setPeerVerifyName(*peerName);
}

//  QString QHttpNetworkRequest::fullLocalServerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QHttpNetworkRequest19fullLocalServerNameEv(
    const QHttpNetworkRequest *self) {
  return new QString(self->fullLocalServerName());
}

//  void QHttpNetworkRequest::setFullLocalServerName(const QString
//      &fullServerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QHttpNetworkRequest22setFullLocalServerNameERK7QString(
    QHttpNetworkRequest *self,
    const QString *fullServerName) {
  self->setFullLocalServerName(*fullServerName);
}

//  bool QHttpNetworkRequest::methodIsIdempotent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QHttpNetworkRequest18methodIsIdempotentEv(
    const QHttpNetworkRequest *self) {
  return self->methodIsIdempotent();
}

//  a Python function taken by a CuteQHttpNetworkRequest, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHttpNetworkRequest(
    QHttpNetworkRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHttpNetworkRequest *>(self)->take(key, call);
}

//  QUrl QHttpNetworkRequest::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_own_ZNK19QHttpNetworkRequest3urlEv(
    const QHttpNetworkRequest *self) {
  return new QUrl(self->QHttpNetworkRequest::url());
}

//  void QHttpNetworkRequest::setUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QHttpNetworkRequest6setUrlERK4QUrl(
    QHttpNetworkRequest *self,
    const QUrl *url) {
  self->QHttpNetworkRequest::setUrl(*url);
}

//  int QHttpNetworkRequest::majorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QHttpNetworkRequest12majorVersionEv(
    const QHttpNetworkRequest *self) {
  return self->QHttpNetworkRequest::majorVersion();
}

//  int QHttpNetworkRequest::minorVersion() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QHttpNetworkRequest12minorVersionEv(
    const QHttpNetworkRequest *self) {
  return self->QHttpNetworkRequest::minorVersion();
}

//  qint64 QHttpNetworkRequest::contentLength() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QHttpNetworkRequest13contentLengthEv(
    const QHttpNetworkRequest *self) {
  return self->QHttpNetworkRequest::contentLength();
}

//  void QHttpNetworkRequest::setContentLength(qint64 length)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QHttpNetworkRequest16setContentLengthEx(
    QHttpNetworkRequest *self,
    qint64 length) {
  self->QHttpNetworkRequest::setContentLength(length);
}

//  QHttpHeaders QHttpNetworkRequest::header() const
extern "C" Q_DECL_EXPORT
QHttpHeaders *ritual_own_ZNK19QHttpNetworkRequest6headerEv(
    const QHttpNetworkRequest *self) {
  return new QHttpHeaders(self->QHttpNetworkRequest::header());
}

//  QByteArray QHttpNetworkRequest::headerField(QByteArrayView name, const
//      QByteArray &defaultValue) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK19QHttpNetworkRequest11headerFieldE14QByteArrayViewRK10QByteArray(
    const QHttpNetworkRequest *self,
    const QByteArrayView *name,
    const QByteArray *defaultValue) {
  return new QByteArray(
      self->QHttpNetworkRequest::headerField(
          *name,
          *defaultValue));
}

//  void QHttpNetworkRequest::setHeaderField(const QByteArray &name, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QHttpNetworkRequest14setHeaderFieldERK10QByteArrayS2_(
    QHttpNetworkRequest *self,
    const QByteArray *name,
    const QByteArray *data) {
  self->QHttpNetworkRequest::setHeaderField(*name, *data);
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
