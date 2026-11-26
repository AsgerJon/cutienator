//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttp2protocolhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttp2protocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtNetwork/private/qabstractsocket_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qnetworkrequest_p.h>
#include <QtCore/private/qobject_p.h>
#include <QtNetwork/private/qauthenticator_p.h>
#include <QtNetwork/private/qhostinfo_p.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qauthenticator.h>
#include <QtCore/qcoreapplication.h>
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qdebug.h>
#include <QtCore/qspan.h>
#include <QtCore/qvarlengtharray.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#    include <QtNetwork/qsslerror.h>
#endif
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#endif
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/qdebug.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtNetwork/private/qhttpprotocolhandler_p.h>
#include <QtNetwork/private/http2protocol_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#endif
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <memory>
#include <utility>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtNetwork/private/qhttp2protocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#include <QtNetwork/qabstractsocket.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qendian.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qhttp2configuration.h>
#ifndef QT_NO_NETWORKPROXY
#  include <QtNetwork/qnetworkproxy.h>
#endif
#include <QtCore/qcoreapplication.h>
#include <algorithm>
#include <vector>
#include <optional>
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhttp2protocolhandler.cpp, line 43, as local:qhttp2protocolhandler.cpp:build_headers
namespace {
inline HPack::HttpHeader build_headers(const QHttpNetworkRequest &request, quint32 maxHeaderListSize,
                                bool useProxy)
{
    using namespace HPack;

    HttpHeader header;
    header.reserve(300);

    // 1. Before anything - mandatory fields, if they do not fit into maxHeaderList -
    // then stop immediately with error.
    const auto auth = request.url().authority(QUrl::FullyEncoded | QUrl::RemoveUserInfo).toLatin1();
    header.emplace_back(":authority", auth);
    header.emplace_back(":method", request.methodName());
    header.emplace_back(":path", request.uri(useProxy));
    header.emplace_back(":scheme", request.url().scheme().toLatin1());

    HeaderSize size = header_size(header);
    if (!size.first) // Ooops!
        return HttpHeader();

    if (size.second > maxHeaderListSize)
        return HttpHeader(); // Bad, we cannot send this request ...

    const QHttpHeaders requestHeader = request.header();
    for (qsizetype i = 0; i < requestHeader.size(); ++i) {
        const auto name = requestHeader.nameAt(i);
        const auto value = requestHeader.valueAt(i);
        const HeaderSize delta = entry_size(name, value);
        if (!delta.first) // Overflow???
            break;
        if (std::numeric_limits<quint32>::max() - delta.second < size.second)
            break;
        size.second += delta.second;
        if (size.second > maxHeaderListSize)
            break;

        if (name == "connection"_L1 || name == "host"_L1 || name == "keep-alive"_L1
            || name == "proxy-connection"_L1 || name == "transfer-encoding"_L1) {
            continue; // Those headers are not valid (section 3.2.1) - from QSpdyProtocolHandler
        }
        // TODO: verify with specs, which fields are valid to send ....
        //
        // Note: RFC 7450 8.1.2 (HTTP/2) states that header field names must be lower-cased
        // prior to their encoding in HTTP/2; header name fields in QHttpHeaders are already
        // lower-cased
        header.emplace_back(QByteArray{name.data(), name.size()},
                            QByteArray{value.data(), value.size()});
    }

    return header;
}
}  // namespace

//  from src/network/access/qhttp2protocolhandler.cpp, line 95, as local:qhttp2protocolhandler.cpp:urlkey_from_request
namespace {
inline QUrl urlkey_from_request(const QHttpNetworkRequest &request)
{
    QUrl url;

    url.setScheme(request.url().scheme());
    url.setAuthority(request.url().authority(QUrl::FullyEncoded | QUrl::RemoveUserInfo));
    url.setPath(QLatin1StringView(request.uri(false)));

    return url;
}
}  // namespace

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

//  from src/network/access/qhttpnetworkconnection.cpp, line 590, as _ZN29QHttpNetworkConnectionPrivate19createAuthorizationEP9QIODeviceR19QHttpNetworkRequest
inline void QHttpNetworkConnectionPrivate::createAuthorization(QIODevice *socket, QHttpNetworkRequest &request)
{
    Q_ASSERT(socket);

    QHttpNetworkConnectionChannel &channel = channels[indexOf(socket)];

    QAuthenticator *authenticator = &channel.authenticator;
    QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(*authenticator);
    // Send "Authorization" header, but not if it's NTLM and the socket is already authenticated.
    if (priv && priv->method != QAuthenticatorPrivate::None) {
        const bool ntlmNego = priv->method == QAuthenticatorPrivate::Ntlm
                || priv->method == QAuthenticatorPrivate::Negotiate;
        const bool authNeeded = channel.lastStatus == 401;
        const bool ntlmNegoOk = ntlmNego && authNeeded
                && (priv->phase != QAuthenticatorPrivate::Done
                    || !channel.authenticationCredentialsSent);
        const bool otherOk =
                !ntlmNego && (authNeeded || request.headerField("Authorization").isEmpty());
        if (ntlmNegoOk || otherOk) {
            QByteArray response = priv->calculateResponse(request.methodName(), request.uri(false),
                                                          request.url().host());
            request.setHeaderField("Authorization", response);
            channel.authenticationCredentialsSent = true;
        }
    }

#if QT_CONFIG(networkproxy)
    authenticator = &channel.proxyAuthenticator;
    priv = QAuthenticatorPrivate::getPrivate(*authenticator);
    // Send "Proxy-Authorization" header, but not if it's NTLM and the socket is already authenticated.
    if (priv && priv->method != QAuthenticatorPrivate::None) {
        const bool ntlmNego = priv->method == QAuthenticatorPrivate::Ntlm
                || priv->method == QAuthenticatorPrivate::Negotiate;
        const bool proxyAuthNeeded = channel.lastStatus == 407;
        const bool ntlmNegoOk = ntlmNego && proxyAuthNeeded
                && (priv->phase != QAuthenticatorPrivate::Done || !channel.proxyCredentialsSent);
        const bool otherOk = !ntlmNego;
        if (ntlmNegoOk || otherOk) {
            QByteArray response = priv->calculateResponse(request.methodName(), request.uri(false),
                                                          networkProxy.hostName());
            request.setHeaderField("Proxy-Authorization", response);
            channel.proxyCredentialsSent = true;
        }
    }
#endif // QT_CONFIG(networkproxy)
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 376, as _ZNK19QHttpNetworkRequest16uploadByteDeviceEv
inline QNonContiguousByteDevice* QHttpNetworkRequest::uploadByteDevice() const
{
    return d->uploadByteDevice;
}

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

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttpnetworkreply.cpp, line 732, as _ZN24QHttpNetworkReplyPrivate17shouldEmitSignalsEv
inline bool QHttpNetworkReplyPrivate::shouldEmitSignals()
{
    // for 401 & 407 don't emit the data signals. Content along with these
    // responses are sent only if the authentication fails.
    return parser.getStatusCode() != 401 && parser.getStatusCode() != 407;
}

//  from src/network/access/http2/http2protocol.cpp, line 23, as _Z8QT_HTTP2v
inline const QLoggingCategory &QT_HTTP2()
{
    static const QLoggingCategory category("qt.network.http2");
    return category;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 186, as _ZN29QHttpNetworkConnectionChannel5closeEv
inline void QHttpNetworkConnectionChannel::close()
{
    if (state == QHttpNetworkConnectionChannel::ClosingState)
        return;

    if (!socket)
        state = QHttpNetworkConnectionChannel::IdleState;
    else if (QSocketAbstraction::socketState(socket) == QAbstractSocket::UnconnectedState)
        state = QHttpNetworkConnectionChannel::IdleState;
    else
        state = QHttpNetworkConnectionChannel::ClosingState;

    // pendingEncrypt must only be true in between connected and encrypted states
    pendingEncrypt = false;

    if (socket) {
        // socket can be 0 since the host lookup is done from qhttpnetworkconnection.cpp while
        // there is no socket yet.
        socket->close();
    }
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 169, as _ZN21QHttp2ProtocolHandler12_q_readyReadEv
inline void QHttp2ProtocolHandler::_q_readyRead()
{
    _q_receiveReply();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 174, as _ZN21QHttp2ProtocolHandler15_q_receiveReplyEv
inline void QHttp2ProtocolHandler::_q_receiveReply()
{
    // not using QObject::connect because the QHttpNetworkConnectionChannel
    // already handles the signals we care about, so we just call the slot
    // directly.
    Q_ASSERT(h2Connection);
    h2Connection->handleReadyRead();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 183, as _ZN21QHttp2ProtocolHandler11sendRequestEv
inline bool QHttp2ProtocolHandler::sendRequest()
{
    if (isGoingAway())
        return false;

    // Process 'fake' (created by QNetworkAccessManager::connectToHostEncrypted())
    // requests first:
    auto &requests = m_channel->h2RequestsToSend;
    for (auto it = requests.begin(), endIt = requests.end(); it != endIt;) {
        const auto &pair = *it;
        if (pair.first.isPreConnect()) {
            m_connection->preConnectFinished();
            emit pair.second->finished();
            it = requests.erase(it);
            if (requests.empty()) {
                // Normally, after a connection was established and H2
                // was negotiated, we send a client preface. connectToHostEncrypted
                // though is not meant to send any data, it's just a 'preconnect'.
                // Thus we return early:
                return true;
            }
        } else {
            ++it;
        }
    }

    if (requests.empty())
        return true;

    m_channel->state = QHttpNetworkConnectionChannel::WritingState;
    // Check what was promised/pushed, maybe we do not have to send a request
    // and have a response already?

    for (auto it = requests.begin(), end = requests.end(); it != end;) {
        HttpMessagePair &httpPair = *it;

        QUrl promiseKey = urlkey_from_request(httpPair.first);
        if (h2Connection->promisedStream(promiseKey) != nullptr) {
            // There's a PUSH_PROMISE for this request, so we don't send one
            initReplyFromPushPromise(httpPair, promiseKey);
            it = requests.erase(it);
            continue;
        }

        QHttp2Stream *stream = createNewStream(httpPair);
        if (!stream) { // There was an issue creating the stream
            // Check if it was unrecoverable, ie. the reply is errored out and finished:
            if (httpPair.second->isFinished()) {
                it = requests.erase(it);
            }
            // ... either way we stop looping:
            break;
        }

        QHttpNetworkRequest &request = requestReplyPairs[stream].first;
        if (!sendHEADERS(stream, request)) {
            finishStreamWithError(stream, QNetworkReply::UnknownNetworkError,
                    "failed to send HEADERS frame(s)"_L1);
            continue;
        }
        if (request.uploadByteDevice()) {
            if (!sendDATA(stream, httpPair.second)) {
                finishStreamWithError(stream, QNetworkReply::UnknownNetworkError,
                                      "failed to send DATA frame(s)"_L1);
                continue;
            }
        }
        it = requests.erase(it);
    }

    m_channel->state = QHttpNetworkConnectionChannel::IdleState;

    return true;
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 266, as _ZN21QHttp2ProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply
inline bool QHttp2ProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
{
    QHttp2Stream *stream = streamIDs.take(reply);
    if (stream) {
        stream->sendRST_STREAM(stream->isUploadingDATA() ? Http2::CANCEL : Http2::HTTP2_NO_ERROR);
        clearStreamState(stream);
        stream->deleteLater();
        return true;
    }
    return false;
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

//  from src/network/access/qhttp2protocolhandler.cpp, line 278, as _ZN21QHttp2ProtocolHandler11sendHEADERSEP12QHttp2StreamR19QHttpNetworkRequest
inline bool QHttp2ProtocolHandler::sendHEADERS(QHttp2Stream *stream, QHttpNetworkRequest &request)
{
    using namespace HPack;

    bool useProxy = false;
#ifndef QT_NO_NETWORKPROXY
    useProxy = m_connection->d_func()->networkProxy.type() != QNetworkProxy::NoProxy;
#endif
    if (request.withCredentials()) {
        m_connection->d_func()->createAuthorization(m_socket, request);
        request.d->needResendWithCredentials = false;
    }
    const auto headers = build_headers(request, h2Connection->maxHeaderListSize(), useProxy);
    if (headers.empty()) // nothing fits into maxHeaderListSize
        return false;

    bool mustUploadData = request.uploadByteDevice();
    return stream->sendHEADERS(headers, !mustUploadData);
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 145, as _ZNK21QHttp2ProtocolHandler11isGoingAwayEv
inline bool QHttp2ProtocolHandler::isGoingAway() const noexcept
{
    return h2Connection && h2Connection->isGoingAway();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 298, as _ZN21QHttp2ProtocolHandler8sendDATAEP12QHttp2StreamP17QHttpNetworkReply
inline bool QHttp2ProtocolHandler::sendDATA(QHttp2Stream *stream, QHttpNetworkReply *reply)
{
    Q_ASSERT(reply);
    QHttpNetworkReplyPrivate *replyPrivate = reply->d_func();
    Q_ASSERT(replyPrivate);
    QHttpNetworkRequest &request = replyPrivate->request;
    Q_ASSERT(request.uploadByteDevice());

    bool startedSending = stream->sendDATA(request.uploadByteDevice(), true);
    return startedSending && !stream->wasReset();
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 761, as _ZN21QHttp2ProtocolHandler12closeSessionEv
inline void QHttp2ProtocolHandler::closeSession()
{
    m_channel->close();
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QHttp2ProtocolHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QHttp2ProtocolHandler10metaObjectEv(
    const QHttp2ProtocolHandler *self) {
  return self->metaObject();
}

//  void *QHttp2ProtocolHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QHttp2ProtocolHandler11qt_metacastEPKc(
    QHttp2ProtocolHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttp2ProtocolHandler::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QHttp2ProtocolHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttp2ProtocolHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QHttp2ProtocolHandler::handleConnectionClosure()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler23handleConnectionClosureEv(
    QHttp2ProtocolHandler *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "handleConnectionClosure()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "handleConnectionClosure()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QHttp2ProtocolHandler::isGoingAway() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QHttp2ProtocolHandler11isGoingAwayEv(
    const QHttp2ProtocolHandler *self) {
  return self->isGoingAway();
}

//  void QHttp2ProtocolHandler::_q_uploadDataDestroyed(QObject *uploadData)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler22_q_uploadDataDestroyedEP7QObject(
    QHttp2ProtocolHandler *self,
    QObject *uploadData) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QHttp2ProtocolHandler")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "_q_uploadDataDestroyed(QObject *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "_q_uploadDataDestroyed(QObject *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&uploadData)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QHttp2ProtocolHandler::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler12_q_readyReadEv(
    QHttp2ProtocolHandler *self) {
  self->_q_readyRead();
}

//  void QHttp2ProtocolHandler::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler15_q_receiveReplyEv(
    QHttp2ProtocolHandler *self) {
  self->_q_receiveReply();
}

//  bool QHttp2ProtocolHandler::sendRequest()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHttp2ProtocolHandler11sendRequestEv(
    QHttp2ProtocolHandler *self) {
  return self->sendRequest();
}

//  bool QHttp2ProtocolHandler::tryRemoveReply(QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHttp2ProtocolHandler14tryRemoveReplyEP17QHttpNetworkReply(
    QHttp2ProtocolHandler *self,
    QHttpNetworkReply *reply) {
  return self->tryRemoveReply(reply);
}

//  bool QHttp2ProtocolHandler::sendDATA(QHttp2Stream *stream,
//      QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QHttp2ProtocolHandler8sendDATAEP12QHttp2StreamP17QHttpNetworkReply(
    QHttp2ProtocolHandler *self,
    QHttp2Stream *stream,
    QHttpNetworkReply *reply) {
  return self->sendDATA(stream, reply);
}

//  void QHttp2ProtocolHandler::closeSession()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QHttp2ProtocolHandler12closeSessionEv(
    QHttp2ProtocolHandler *self) {
  self->closeSession();
}

//  QHttp2ProtocolHandler as the QAbstractProtocolHandler it is built on
extern "C" Q_DECL_EXPORT
QAbstractProtocolHandler *ritual_cast_QHttp2ProtocolHandler_QAbstractProtocolHandler(
    QHttp2ProtocolHandler *self) {
  return static_cast<QAbstractProtocolHandler *>(self);
}

//  void QHttp2ProtocolHandler::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QHttp2ProtocolHandler12_q_readyReadEv(
    QHttp2ProtocolHandler *self) {
  self->QHttp2ProtocolHandler::_q_readyRead();
}

//  void QHttp2ProtocolHandler::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QHttp2ProtocolHandler15_q_receiveReplyEv(
    QHttp2ProtocolHandler *self) {
  self->QHttp2ProtocolHandler::_q_receiveReply();
}

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
