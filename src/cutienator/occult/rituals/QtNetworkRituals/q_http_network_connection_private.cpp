//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-27: code taken from Qt's source no longer
//  stands under defined(Q_OS_LINUX), which Qt does not write there; its
//  rituals no longer stand under defined(Q_OS_LINUX), as the code taken from
//  Qt they call no longer does. Kept as it is when the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qnetworkproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qhttpnetworkrequest_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtCore/private/qtools_p.h>
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
#include <QtNetwork/private/qabstractprotocolhandler_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qhttpnetworkreply_p.h>
#include <QtNetwork/private/qhttpnetworkconnection_p.h>
#ifndef QT_NO_SSL
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#endif
#include <QtNetwork/private/qdecompresshelper_p.h>
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#include <QtNetwork/private/qhttpprotocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhttpnetworkconnection.cpp, line 45, as local:qhttpnetworkconnection.cpp:getPreferredActiveChannelCount
static int getPreferredActiveChannelCount(QHttpNetworkConnection::ConnectionType type,
                                          int defaultValue)
{
    return (type == QHttpNetworkConnection::ConnectionTypeHTTP2
            || type == QHttpNetworkConnection::ConnectionTypeHTTP2Direct)
            ? 1
            : defaultValue;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 228, as local:qhttpnetworkconnection.cpp:makeAcceptLanguage
static QByteArray makeAcceptLanguage()
{
    QString systemLocale = QLocale::system().name();
    if (systemLocale == "C"_L1)
        return "en,*"_ba;
    systemLocale.replace('_'_L1, '-'_L1);
    if (systemLocale.startsWith("en-"_L1))
        return (systemLocale + ",*"_L1).toLatin1();
    return (systemLocale + ",en,*"_L1).toLatin1();
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 239, as local:qhttpnetworkconnection.cpp:removeZoneId
static QStringView removeZoneId(QStringView ipv6HostAddress)
{
    const auto zoneIdentfierIndex = ipv6HostAddress.indexOf(u'%');
    // Only perform a minimal sanity check, as at this point the
    // ipv6HostAddress was already used successfully to establish the connection.
    if (zoneIdentfierIndex == -1) {
        return ipv6HostAddress;
    }

    return ipv6HostAddress.left(zoneIdentfierIndex);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 35, as local:qhttpnetworkconnectionchannel.cpp:reconnectAttemptsDefault
static const int reconnectAttemptsDefault = 3;

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 43, as _ZN29QHttpNetworkConnectionChannelC1Ev
inline QHttpNetworkConnectionChannel::QHttpNetworkConnectionChannel()
    : socket(nullptr)
    , ssl(false)
    , isInitialized(false)
    , state(IdleState)
    , reply(nullptr)
    , written(0)
    , bytesTotal(0)
    , resendCurrent(false)
    , lastStatus(0)
    , pendingEncrypt(false)
    , reconnectAttempts(reconnectAttemptsDefault)
    , authenticationCredentialsSent(false)
    , proxyCredentialsSent(false)
    , protocolHandler(nullptr)
#ifndef QT_NO_SSL
    , ignoreAllSslErrors(false)
#endif
    , pipeliningSupported(PipeliningSupportUnknown)
    , networkLayerPreference(QAbstractSocket::AnyIPProtocol)
    , connection(nullptr)
{
    // Inlining this function in the header leads to compiler error on
    // release-armv5, on at least timebox 9.2 and 10.1.
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1494, as _ZN29QHttpNetworkConnectionChannel13setConnectionEP22QHttpNetworkConnection
inline void QHttpNetworkConnectionChannel::setConnection(QHttpNetworkConnection *c)
{
    // Inlining this function in the header leads to compiler error on
    // release-armv5, on at least timebox 9.2 and 10.1.
    connection = c;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 269, as _ZN19QHttpNetworkRequest18prependHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkRequest::prependHeaderField(const QByteArray &name, const QByteArray &data)
{
    d->prependHeaderField(name, data);
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 279, as _ZN19QHttpNetworkRequestaSERKS_
inline QHttpNetworkRequest &QHttpNetworkRequest::operator=(const QHttpNetworkRequest &other)
{
    QHttpNetworkHeader::operator=(other);
    d = other.d;
    return *this;
}

//  from src/network/access/qabstractprotocolhandler.cpp, line 22, as _ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply
inline void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
{
    m_reply = reply;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 759, as _ZN24QHttpNetworkReplyPrivate9eraseDataEv
inline void QHttpNetworkReplyPrivate::eraseData()
{
    responseData.clear();
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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 232, as _ZN29QHttpNetworkConnectionChannel11sendRequestEv
inline void QHttpNetworkConnectionChannel::sendRequest()
{
    if (waitingForPotentialAbort) {
        needInvokeSendRequest = true;
        return;
    }
    if (isPendingReconnect())
        return;
    Q_ASSERT(protocolHandler);
    protocolHandler->sendRequest();
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 765, as _ZN29QHttpNetworkConnectionChannel12pipelineIntoERSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE
inline void QHttpNetworkConnectionChannel::pipelineInto(HttpMessagePair &pair)
{
    // this is only called for simple GET

    QHttpNetworkRequest &request = pair.first;
    QHttpNetworkReply *reply = pair.second;
    reply->d_func()->clear();
    reply->d_func()->connection = connection;
    reply->d_func()->connectionChannel = this;
    reply->d_func()->autoDecompress = request.d->autoDecompress;
    reply->d_func()->pipeliningUsed = true;

#ifndef QT_NO_NETWORKPROXY
    pipeline.append(QHttpNetworkRequestPrivate::header(request,
                                                           (connection->d_func()->networkProxy.type() != QNetworkProxy::NoProxy)));
#else
    pipeline.append(QHttpNetworkRequestPrivate::header(request, false));
#endif

    alreadyPipelinedRequests.append(pair);

    // pipelineFlush() needs to be called at some point afterwards
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 789, as _ZN29QHttpNetworkConnectionChannel13pipelineFlushEv
inline void QHttpNetworkConnectionChannel::pipelineFlush()
{
    if (pipeline.isEmpty())
        return;

    // The goal of this is so that we have everything in one TCP packet.
    // For the Unbuffered QTcpSocket this is manually needed, the buffered
    // QTcpSocket does it automatically.
    // Also, sometimes the OS does it for us (Nagle's algorithm) but that
    // happens only sometimes.
    socket->write(pipeline);
    pipeline.clear();
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 696, as _ZN29QHttpNetworkConnectionChannel15resetUploadDataEv
inline bool QHttpNetworkConnectionChannel::resetUploadData()
{
    if (!reply) {
        //this happens if server closes connection while QHttpNetworkConnectionPrivate::_q_startNextRequest is pending
        return false;
    }
    if (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2Direct
        || switchedToHttp2) {
        // The else branch doesn't make any sense for HTTP/2, since 1 channel is multiplexed into
        // many streams. And having one stream fail to reset upload data should not completely close
        // the channel. Handled in the http2 protocol handler.
    } else if (QNonContiguousByteDevice *uploadByteDevice = request.uploadByteDevice()) {
        if (!uploadByteDevice->reset()) {
            connection->d_func()->emitReplyError(socket, reply, QNetworkReply::ContentReSendError);
            return false;
        }
        written = 0;
    }
    return true;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 302, as _ZN29QHttpNetworkConnectionChannel16ensureConnectionEv
inline bool QHttpNetworkConnectionChannel::ensureConnection()
{
    if (!isInitialized)
        init();

    QAbstractSocket::SocketState socketState = QSocketAbstraction::socketState(socket);

    // resend this request after we receive the disconnected signal
    // If !socket->isOpen() then we have already called close() on the socket, but there was still a
    // pending connectToHost() for which we hadn't seen a connected() signal, yet. The connected()
    // has now arrived (as indicated by socketState != ClosingState), but we cannot send anything on
    // such a socket anymore.
    if (socketState == QAbstractSocket::ClosingState ||
            (socketState != QAbstractSocket::UnconnectedState && !socket->isOpen())) {
        if (reply)
            resendCurrent = true;
        return false;
    }

    // already trying to connect?
    if (socketState == QAbstractSocket::HostLookupState ||
        socketState == QAbstractSocket::ConnectingState) {
        return false;
    }

    // make sure that this socket is in a connected state, if not initiate
    // connection to the host.
    if (socketState != QAbstractSocket::ConnectedState) {
        // connect to the host if not already connected.
        state = QHttpNetworkConnectionChannel::ConnectingState;
        pendingEncrypt = ssl;

        // reset state
        pipeliningSupported = PipeliningSupportUnknown;
        authenticationCredentialsSent = false;
        proxyCredentialsSent = false;
        authenticator.detach();
        QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(authenticator);
        priv->hasFailed = false;
        proxyAuthenticator.detach();
        priv = QAuthenticatorPrivate::getPrivate(proxyAuthenticator);
        priv->hasFailed = false;

        // This workaround is needed since we use QAuthenticator for NTLM authentication. The "phase == Done"
        // is the usual criteria for emitting authentication signals. The "phase" is set to "Done" when the
        // last header for Authorization is generated by the QAuthenticator. Basic & Digest logic does not
        // check the "phase" for generating the Authorization header. NTLM authentication is a two stage
        // process & needs the "phase". To make sure the QAuthenticator uses the current username/password
        // the phase is reset to Start.
        priv = QAuthenticatorPrivate::getPrivate(authenticator);
        if (priv && priv->phase == QAuthenticatorPrivate::Done)
            priv->phase = QAuthenticatorPrivate::Start;
        priv = QAuthenticatorPrivate::getPrivate(proxyAuthenticator);
        if (priv && priv->phase == QAuthenticatorPrivate::Done)
            priv->phase = QAuthenticatorPrivate::Start;

        QString connectHost = connection->d_func()->hostName;
        quint16 connectPort = connection->d_func()->port;

        QHttpNetworkReply *potentialReply = connection->d_func()->predictNextRequestsReply();
        if (potentialReply) {
            QMetaObject::invokeMethod(potentialReply, "socketStartedConnecting", Qt::QueuedConnection);
        } else if (!h2RequestsToSend.isEmpty()) {
            QMetaObject::invokeMethod(std::as_const(h2RequestsToSend).first().second, "socketStartedConnecting", Qt::QueuedConnection);
        }

#ifndef QT_NO_NETWORKPROXY
        // HTTPS always use transparent proxy.
        if (connection->d_func()->networkProxy.type() != QNetworkProxy::NoProxy && !ssl) {
            connectHost = connection->d_func()->networkProxy.hostName();
            connectPort = connection->d_func()->networkProxy.port();
        }
        if (auto *abSocket = qobject_cast<QAbstractSocket *>(socket);
            abSocket && abSocket->proxy().type() == QNetworkProxy::HttpProxy) {
            // Make user-agent field available to HTTP proxy socket engine (QTBUG-17223)
            QByteArray value;
            // ensureConnection is called before any request has been assigned, but can also be
            // called again if reconnecting
            if (request.url().isEmpty()) {
                if (connection->connectionType()
                            == QHttpNetworkConnection::ConnectionTypeHTTP2Direct
                    || (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2
                        && !h2RequestsToSend.isEmpty())) {
                    value = std::as_const(h2RequestsToSend).first().first.headerField("user-agent");
                } else {
                    value = connection->d_func()->predictNextRequest().headerField("user-agent");
                }
            } else {
                value = request.headerField("user-agent");
            }
            if (!value.isEmpty()) {
                QNetworkProxy proxy(abSocket->proxy());
                auto h = proxy.headers();
                h.replaceOrAppend(QHttpHeaders::WellKnownHeader::UserAgent, value);
                proxy.setHeaders(std::move(h));
                abSocket->setProxy(proxy);
            }
        }
#endif
        if (ssl) {
#ifndef QT_NO_SSL
            QSslSocket *sslSocket = qobject_cast<QSslSocket*>(socket);

            // check whether we can re-use an existing SSL session
            // (meaning another socket in this connection has already
            // performed a full handshake)
            if (auto ctx = connection->sslContext())
                QSslSocketPrivate::checkSettingSslContext(sslSocket, std::move(ctx));

            sslSocket->setPeerVerifyName(connection->d_func()->peerVerifyName);
            sslSocket->connectToHostEncrypted(connectHost, connectPort, QIODevice::ReadWrite, networkLayerPreference);
            // AXIVION DISABLE Qt-Security-QSslSocketIgnoreSslErrors: intentional behavior
            if (ignoreAllSslErrors)
                sslSocket->ignoreSslErrors();
            sslSocket->ignoreSslErrors(ignoreSslErrorsList);
            // AXIVION ENABLE Qt-Security-QSslSocketIgnoreSslErrors

            // limit the socket read buffer size. we will read everything into
            // the QHttpNetworkReply anyway, so let's grow only that and not
            // here and there.
            sslSocket->setReadBufferSize(64*1024);
#else
            // Need to dequeue the request so that we can emit the error.
            if (!reply)
                connection->d_func()->dequeueRequest(socket);
            connection->d_func()->emitReplyError(socket, reply, QNetworkReply::ProtocolUnknownError);
#endif
        } else {
            // In case of no proxy we can use the Unbuffered QTcpSocket
#ifndef QT_NO_NETWORKPROXY
            if (connection->d_func()->networkProxy.type() == QNetworkProxy::NoProxy
                    && connection->cacheProxy().type() == QNetworkProxy::NoProxy
                    && connection->transparentProxy().type() == QNetworkProxy::NoProxy) {
#endif
                if (auto *s = qobject_cast<QAbstractSocket *>(socket)) {
                    s->connectToHost(connectHost, connectPort,
                                     QIODevice::ReadWrite | QIODevice::Unbuffered,
                                     networkLayerPreference);
                    // For an Unbuffered QTcpSocket, the read buffer size has a special meaning.
                    s->setReadBufferSize(1 * 1024);
#if QT_CONFIG(localserver)
                } else if (auto *s = qobject_cast<QLocalSocket *>(socket)) {
                    s->connectToServer(connectHost);
#endif
                }
#ifndef QT_NO_NETWORKPROXY
            } else {
                auto *s = qobject_cast<QAbstractSocket *>(socket);
                Q_ASSERT(s);
                // limit the socket read buffer size. we will read everything into
                // the QHttpNetworkReply anyway, so let's grow only that and not
                // here and there.
                s->connectToHost(connectHost, connectPort, QIODevice::ReadWrite, networkLayerPreference);
                s->setReadBufferSize(64 * 1024);
            }
#endif
        }
        return false;
    }

    // This code path for ConnectedState
    if (pendingEncrypt) {
        // Let's only be really connected when we have received the encrypted() signal. Else the state machine seems to mess up
        // and corrupt the things sent to the server.
        return false;
    }

    return true;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 615, as _ZN29QHttpNetworkConnectionChannel33requeueCurrentlyPipelinedRequestsEv
inline void QHttpNetworkConnectionChannel::requeueCurrentlyPipelinedRequests()
{
    for (int i = 0; i < alreadyPipelinedRequests.size(); i++)
        connection->d_func()->requeueRequest(alreadyPipelinedRequests.at(i));
    alreadyPipelinedRequests.clear();

    // only run when the QHttpNetworkConnection is not currently being destructed, e.g.
    // this function is called from _q_disconnected which is called because
    // of ~QHttpNetworkConnectionPrivate
    if (qobject_cast<QHttpNetworkConnection*>(connection))
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 321, as _ZNK19QHttpNetworkRequest19isPipeliningAllowedEv
inline bool QHttpNetworkRequest::isPipeliningAllowed() const
{
    return d->pipeliningAllowed;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 291, as _ZNK19QHttpNetworkRequest9operationEv
inline QHttpNetworkRequest::Operation QHttpNetworkRequest::operation() const
{
    return d->operation;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 823, as _ZNK29QHttpNetworkConnectionChannel12isSocketBusyEv
inline bool QHttpNetworkConnectionChannel::isSocketBusy() const
{
    return (state & QHttpNetworkConnectionChannel::BusyState);
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

//  from src/network/access/qhttpnetworkreply.cpp, line 513, as _ZN24QHttpNetworkReplyPrivate24isConnectionCloseEnabledEv
inline bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()
{
    return connectionCloseEnabled || forceConnectionCloseEnabled;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 209, as _ZN29QHttpNetworkConnectionChannel5abortEv
inline void QHttpNetworkConnectionChannel::abort()
{
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
        auto callAbort = [](auto *s) {
            s->abort();
        };
        QSocketAbstraction::visit(callAbort, socket);
    }
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 361, as _ZNK19QHttpNetworkRequest15withCredentialsEv
inline bool QHttpNetworkRequest::withCredentials() const
{
    return d->withCredentials;
}

//  from src/network/access/qhttpnetworkheader.cpp, line 43, as _ZNK25QHttpNetworkHeaderPrivate17headerFieldValuesE14QByteArrayView
inline QList<QByteArray> QHttpNetworkHeaderPrivate::headerFieldValues(QByteArrayView name) const
{
    return parser.headerFieldValues(name);
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 234, as _ZNK19QHttpNetworkRequest13redirectCountEv
inline int QHttpNetworkRequest::redirectCount() const
{
    return d->redirectCount;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 229, as _ZNK19QHttpNetworkRequest14redirectPolicyEv
inline QNetworkRequest::RedirectPolicy QHttpNetworkRequest::redirectPolicy() const
{
    return d->redirectPolicy;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 219, as _ZNK19QHttpNetworkRequest17isFollowRedirectsEv
inline bool QHttpNetworkRequest::isFollowRedirects() const
{
    return d->redirectPolicy != QNetworkRequest::ManualRedirectPolicy;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 192, as _ZNK19QHttpNetworkRequest3urlEv
inline QUrl QHttpNetworkRequest::url() const
{
    return d->url;
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 254, as _ZNK19QHttpNetworkRequest6headerEv
inline QHttpHeaders QHttpNetworkRequest::header() const
{
    return d->parser.headers();
}

//  from src/network/access/qhttpnetworkheader.cpp, line 53, as _ZN25QHttpNetworkHeaderPrivate18prependHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkHeaderPrivate::prependHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.prependHeaderField(name, data);
}

//  from src/network/access/qhttpnetworkreply.cpp, line 343, as _ZN24QHttpNetworkReplyPrivate5clearEv
inline void QHttpNetworkReplyPrivate::clear()
{
    connection = nullptr;
    connectionChannel = nullptr;
    autoDecompress = false;
    clearHttpLayerInformation();
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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 69, as _ZN29QHttpNetworkConnectionChannel4initEv
inline void QHttpNetworkConnectionChannel::init()
{
#ifndef QT_NO_SSL
    if (connection->d_func()->encrypt)
        socket = new QSslSocket;
#if QT_CONFIG(localserver)
    else if (connection->d_func()->isLocalSocket)
        socket = new QLocalSocket;
#endif
    else
        socket = new QTcpSocket;
#else
    socket = new QTcpSocket;
#endif
#ifndef QT_NO_NETWORKPROXY
    // Set by QNAM anyway, but let's be safe here
    if (auto s = qobject_cast<QAbstractSocket *>(socket))
        s->setProxy(QNetworkProxy::NoProxy);
#endif

    // After some back and forth in all the last years, this is now a DirectConnection because otherwise
    // the state inside the *Socket classes gets messed up, also in conjunction with the socket notifiers
    // which behave slightly differently on Windows vs Linux
    QObject::connect(socket, &QIODevice::bytesWritten,
                     this, &QHttpNetworkConnectionChannel::_q_bytesWritten,
                     Qt::DirectConnection);
    QObject::connect(socket, &QIODevice::readyRead,
                     this, &QHttpNetworkConnectionChannel::_q_readyRead,
                     Qt::DirectConnection);


    QSocketAbstraction::visit([this](auto *socket){
        using SocketType = std::remove_pointer_t<decltype(socket)>;
        QObject::connect(socket, &SocketType::connected,
                        this, &QHttpNetworkConnectionChannel::_q_connected,
                        Qt::DirectConnection);

        // The disconnected() and error() signals may already come
        // while calling connectToHost().
        // In case of a cached hostname or an IP this
        // will then emit a signal to the user of QNetworkReply
        // but cannot be caught because the user did not have a chance yet
        // to connect to QNetworkReply's signals.
        QObject::connect(socket, &SocketType::disconnected,
                        this, &QHttpNetworkConnectionChannel::_q_disconnected,
                        Qt::DirectConnection);
        if constexpr (std::is_same_v<SocketType, QAbstractSocket>) {
            QObject::connect(socket, &QAbstractSocket::errorOccurred,
                            this, &QHttpNetworkConnectionChannel::_q_error,
                            Qt::DirectConnection);
#if QT_CONFIG(localserver)
        } else if constexpr (std::is_same_v<SocketType, QLocalSocket>) {
            auto convertAndForward = [this](QLocalSocket::LocalSocketError error) {
                _q_error(static_cast<QAbstractSocket::SocketError>(error));
            };
            QObject::connect(socket, &SocketType::errorOccurred,
                            this, std::move(convertAndForward),
                            Qt::DirectConnection);
#endif
        }
    }, socket);



#ifndef QT_NO_NETWORKPROXY
    if (auto *s = qobject_cast<QAbstractSocket *>(socket)) {
        QObject::connect(s, &QAbstractSocket::proxyAuthenticationRequired,
                        this, &QHttpNetworkConnectionChannel::_q_proxyAuthenticationRequired,
                        Qt::DirectConnection);
    }
#endif

#ifndef QT_NO_SSL
    QSslSocket *sslSocket = qobject_cast<QSslSocket*>(socket);
    if (sslSocket) {
        // won't be a sslSocket if encrypt is false
        QObject::connect(sslSocket, &QSslSocket::encrypted,
                         this, &QHttpNetworkConnectionChannel::_q_encrypted,
                         Qt::DirectConnection);
        QObject::connect(sslSocket, &QSslSocket::sslErrors,
                         this, &QHttpNetworkConnectionChannel::_q_sslErrors,
                         Qt::DirectConnection);
        QObject::connect(sslSocket, &QSslSocket::preSharedKeyAuthenticationRequired,
                         this, &QHttpNetworkConnectionChannel::_q_preSharedKeyAuthenticationRequired,
                         Qt::DirectConnection);
        QObject::connect(sslSocket, &QSslSocket::encryptedBytesWritten,
                         this, &QHttpNetworkConnectionChannel::_q_encryptedBytesWritten,
                         Qt::DirectConnection);

        // AXIVION DISABLE Qt-Security-QSslSocketIgnoreSslErrors: intentional behavior
        if (ignoreAllSslErrors)
            sslSocket->ignoreSslErrors();

        if (!ignoreSslErrorsList.isEmpty())
            sslSocket->ignoreSslErrors(ignoreSslErrorsList);
        // AXIVION ENABLE Qt-Security-QSslSocketIgnoreSslErrors

        if (sslConfiguration && !sslConfiguration->isNull())
           sslSocket->setSslConfiguration(*sslConfiguration);
    } else {
#endif // !QT_NO_SSL
        if (connection->connectionType() != QHttpNetworkConnection::ConnectionTypeHTTP2)
            protocolHandler.reset(new QHttpProtocolHandler(this));
#ifndef QT_NO_SSL
    }
#endif

#ifndef QT_NO_NETWORKPROXY
    if (auto *s = qobject_cast<QAbstractSocket *>(socket);
        s && proxy.type() != QNetworkProxy::NoProxy) {
        s->setProxy(proxy);
    }
#endif
    isInitialized = true;
}

//  from src/network/access/qhttpnetworkheader.cpp, line 48, as _ZN25QHttpNetworkHeaderPrivate14setHeaderFieldERK10QByteArrayS2_
inline void QHttpNetworkHeaderPrivate::setHeaderField(const QByteArray &name, const QByteArray &data)
{
    parser.setHeaderField(name, data);
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

//  from src/network/access/qhttpnetworkheader.cpp, line 12, as _ZN25QHttpNetworkHeaderPrivateC2ERK4QUrl
inline QHttpNetworkHeaderPrivate::QHttpNetworkHeaderPrivate(const QUrl &newUrl)
    :url(newUrl)
{
}

//  from src/network/access/qhttpnetworkreply.cpp, line 329, as _ZN24QHttpNetworkReplyPrivate25clearHttpLayerInformationEv
inline void QHttpNetworkReplyPrivate::clearHttpLayerInformation()
{
    state = NothingDoneState;
    bodyLength = 0;
    contentRead = 0;
    totalProgress = 0;
    currentChunkSize = 0;
    currentChunkRead = 0;
    lastChunkRead = false;
    connectionCloseEnabled = true;
    parser.clear();
}

//  from src/network/access/qhttpprotocolhandler.cpp, line 15, as _ZN20QHttpProtocolHandlerC1EP29QHttpNetworkConnectionChannel
inline QHttpProtocolHandler::QHttpProtocolHandler(QHttpNetworkConnectionChannel *channel)
    : QAbstractProtocolHandler(channel)
{
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1064, as _ZN29QHttpNetworkConnectionChannel12_q_connectedEv
inline void QHttpNetworkConnectionChannel::_q_connected()
{
    if (auto *s = qobject_cast<QAbstractSocket *>(socket))
        _q_connected_abstract_socket(s);
#if QT_CONFIG(localserver)
    else if (auto *s = qobject_cast<QLocalSocket *>(socket))
        _q_connected_local_socket(s);
#endif
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1297, as _ZN29QHttpNetworkConnectionChannel12_q_encryptedEv
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::_q_encrypted()
{
    QSslSocket *sslSocket = qobject_cast<QSslSocket *>(socket);
    Q_ASSERT(sslSocket);

    if (!protocolHandler && connection->connectionType() != QHttpNetworkConnection::ConnectionTypeHTTP2Direct) {
        // ConnectionTypeHTTP2Direct does not rely on ALPN/NPN to negotiate HTTP/2,
        // after establishing a secure connection we immediately start sending
        // HTTP/2 frames.
        switch (sslSocket->sslConfiguration().nextProtocolNegotiationStatus()) {
        case QSslConfiguration::NextProtocolNegotiationNegotiated: {
            QByteArray nextProtocol = sslSocket->sslConfiguration().nextNegotiatedProtocol();
            if (nextProtocol == QSslConfiguration::NextProtocolHttp1_1) {
                // fall through to create a QHttpProtocolHandler
            } else if (nextProtocol == QSslConfiguration::ALPNProtocolHTTP2) {
                switchedToHttp2 = true;
                protocolHandler.reset(new QHttp2ProtocolHandler(this));
                connection->setConnectionType(QHttpNetworkConnection::ConnectionTypeHTTP2);
                break;
            } else {
                emitFinishedWithError(QNetworkReply::SslHandshakeFailedError,
                                      "detected unknown Next Protocol Negotiation protocol");
                break;
            }
        }
            Q_FALLTHROUGH();
        case QSslConfiguration::NextProtocolNegotiationUnsupported: // No agreement, try HTTP/1(.1)
        case QSslConfiguration::NextProtocolNegotiationNone: {
            protocolHandler.reset(new QHttpProtocolHandler(this));

            QSslConfiguration newConfiguration = sslSocket->sslConfiguration();
            QList<QByteArray> protocols = newConfiguration.allowedNextProtocols();
            const int nProtocols = protocols.size();
            // Clear the protocol that we failed to negotiate, so we do not try
            // it again on other channels that our connection can create/open.
            if (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2)
                protocols.removeAll(QSslConfiguration::ALPNProtocolHTTP2);

            if (nProtocols > protocols.size()) {
                newConfiguration.setAllowedNextProtocols(protocols);
                const int channelCount = connection->d_func()->channelCount;
                for (int i = 0; i < channelCount; ++i)
                    connection->d_func()->channels[i].setSslConfiguration(newConfiguration);
            }

            connection->setConnectionType(QHttpNetworkConnection::ConnectionTypeHTTP);
            // We use only one channel for HTTP/2, but normally six for
            // HTTP/1.1 - let's restore this number to the reserved number of
            // channels:
            if (connection->d_func()->activeChannelCount < connection->d_func()->channelCount) {
                connection->d_func()->activeChannelCount = connection->d_func()->channelCount;
                // re-queue requests from HTTP/2 queue to HTTP queue, if any
                requeueHttp2Requests();
            }
            break;
        }
        default:
            emitFinishedWithError(QNetworkReply::SslHandshakeFailedError,
                                  "detected unknown Next Protocol Negotiation protocol");
        }
    } else if (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2
               || connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2Direct) {
        // We have to reset QHttp2ProtocolHandler's state machine, it's a new
        // connection and the handler's state is unique per connection.
        protocolHandler.reset(new QHttp2ProtocolHandler(this));
    }

    if (!socket)
        return; // ### error
    state = QHttpNetworkConnectionChannel::IdleState;
    pendingEncrypt = false;

    if (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2 ||
        connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2Direct) {
        if (!h2RequestsToSend.isEmpty()) {
            // Similar to HTTP/1.1 counterpart below:
            const auto &pair = std::as_const(h2RequestsToSend).first();
            waitingForPotentialAbort = true;
            emit pair.second->encrypted();

            // We don't send or handle any received data until any effects from
            // emitting encrypted() have been processed. This is necessary
            // because the user may have called abort(). We may also abort the
            // whole connection if the request has been aborted and there is
            // no more requests to send.
            QMetaObject::invokeMethod(this,
                                      &QHttpNetworkConnectionChannel::checkAndResumeCommunication,
                                      Qt::QueuedConnection);

            // In case our peer has sent us its settings (window size, max concurrent streams etc.)
            // let's give _q_receiveReply a chance to read them first ('invokeMethod', QueuedConnection).
        }
    } else { // HTTP
        if (!reply)
            connection->d_func()->dequeueRequest(socket);
        if (reply) {
            reply->setHttp2WasUsed(false);
            Q_ASSERT(reply->d_func()->connectionChannel == this);
            emit reply->encrypted();
        }
        if (reply)
            sendRequestDelayed();
    }
    QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 268, as _ZN29QHttpNetworkConnectionChannel12_q_readyReadEv
inline void QHttpNetworkConnectionChannel::_q_readyRead()
{
    Q_ASSERT(protocolHandler);
    if (waitingForPotentialAbort) {
        needInvokeReadyRead = true;
        return;
    }
    protocolHandler->_q_readyRead();
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1432, as _ZN29QHttpNetworkConnectionChannel12_q_sslErrorsERK5QListI9QSslErrorE
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::_q_sslErrors(const QList<QSslError> &errors)
{
    if (!socket)
        return;
    //QNetworkReply::NetworkError errorCode = QNetworkReply::ProtocolFailure;
    // Also pause the connection because socket notifiers may fire while an user
    // dialog is displaying
    connection->d_func()->pauseConnection();
    if (pendingEncrypt && !reply)
        connection->d_func()->dequeueRequest(socket);
    if (connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP) {
        if (reply)
            emit reply->sslErrors(errors);
    }
#ifndef QT_NO_SSL
    else { // HTTP/2
        const auto h2RequestsToSendCopy = h2RequestsToSend;
        for (const auto &httpMessagePair : h2RequestsToSendCopy) {
            // emit SSL errors for all replies
            QHttpNetworkReply *currentReply = httpMessagePair.second;
            Q_ASSERT(currentReply);
            emit currentReply->sslErrors(errors);
        }
    }
#endif // QT_NO_SSL
    connection->d_func()->resumeConnection();
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 893, as _ZN29QHttpNetworkConnectionChannel15_q_bytesWrittenEx
inline void QHttpNetworkConnectionChannel::_q_bytesWritten(qint64 bytes)
{
    Q_UNUSED(bytes);
    if (ssl) {
        // In the SSL case we want to send data from encryptedBytesWritten signal since that one
        // is the one going down to the actual network, not only into some SSL buffer.
        return;
    }

    // bytes have been written to the socket. write even more of them :)
    if (isSocketWriting())
        sendRequest();
    // otherwise we do nothing
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 908, as _ZN29QHttpNetworkConnectionChannel15_q_disconnectedEv
inline void QHttpNetworkConnectionChannel::_q_disconnected()
{
    if (state == QHttpNetworkConnectionChannel::ClosingState) {
        state = QHttpNetworkConnectionChannel::IdleState;
        clearPendingReconnect();
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
        return;
    }

    // read the available data before closing (also done in _q_error for other codepaths)
    if ((isSocketWaiting() || isSocketReading()) && socket->bytesAvailable()) {
        if (reply) {
            state = QHttpNetworkConnectionChannel::ReadingState;
            _q_receiveReply();
        }
    } else if (reply && reply->contentLength() == -1 && !reply->d_func()->isChunked()) {
        // There was no content-length header and it's not chunked encoding,
        // so this is a valid way to have the connection closed by the server
        _q_receiveReply();
    } else if (state == QHttpNetworkConnectionChannel::IdleState && resendCurrent) {
        // re-sending request because the socket was in ClosingState
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);
    }
    state = QHttpNetworkConnectionChannel::IdleState;
    if (alreadyPipelinedRequests.size()) {
        // If nothing was in a pipeline, no need in calling
        // _q_startNextRequest (which it does):
        requeueCurrentlyPipelinedRequests();
    }

    // A going-away connection closed without us calling close(), so it was not handled by
    // the ClosingState branch above. Done last, so the reads above still have the handler.
    if (clearPendingReconnect())
        QMetaObject::invokeMethod(connection, "_q_startNextRequest", Qt::QueuedConnection);

    pendingEncrypt = false;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 79, as _ZN29QHttpNetworkConnectionPrivateD1Ev
inline QHttpNetworkConnectionPrivate::~QHttpNetworkConnectionPrivate()
{
    for (int i = 0; i < channelCount; ++i) {
        if (channels[i].socket) {
            QObject::disconnect(channels[i].socket, nullptr, &channels[i], nullptr);
            channels[i].socket->close();
            delete channels[i].socket;
        }
    }
    delete []channels;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 91, as _ZN29QHttpNetworkConnectionPrivate4initEv
inline void QHttpNetworkConnectionPrivate::init()
{
    Q_Q(QHttpNetworkConnection);
    for (int i = 0; i < channelCount; i++) {
        channels[i].setConnection(this->q_func());
        channels[i].ssl = encrypt;
    }

    delayedConnectionTimer.setSingleShot(true);
    QObject::connect(&delayedConnectionTimer, SIGNAL(timeout()), q, SLOT(_q_connectDelayedChannel()));
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 103, as _ZN29QHttpNetworkConnectionPrivate15pauseConnectionEv
inline void QHttpNetworkConnectionPrivate::pauseConnection()
{
    state = PausedState;

    // Disable all socket notifiers
    for (int i = 0; i < activeChannelCount; i++) {
        if (auto *absSocket = qobject_cast<QAbstractSocket *>(channels[i].socket)) {
#ifndef QT_NO_SSL
            if (encrypt)
                QSslSocketPrivate::pauseSocketNotifiers(static_cast<QSslSocket*>(absSocket));
            else
#endif
                QAbstractSocketPrivate::pauseSocketNotifiers(absSocket);
#if QT_CONFIG(localserver)
        } else if (qobject_cast<QLocalSocket *>(channels[i].socket)) {
            // @todo how would we do this?
#if 0 // @todo Enable this when there is a debug category for this
            qDebug() << "Should pause socket but there is no way to do it for local sockets";
#endif
#endif
        }
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 127, as _ZN29QHttpNetworkConnectionPrivate16resumeConnectionEv
inline void QHttpNetworkConnectionPrivate::resumeConnection()
{
    state = RunningState;
    // Enable all socket notifiers
    for (int i = 0; i < activeChannelCount; i++) {
        if (auto *absSocket = qobject_cast<QAbstractSocket *>(channels[i].socket)) {
#ifndef QT_NO_SSL
            if (encrypt)
                QSslSocketPrivate::resumeSocketNotifiers(static_cast<QSslSocket*>(absSocket));
            else
#endif
                QAbstractSocketPrivate::resumeSocketNotifiers(absSocket);

            // Resume pending upload if needed
            if (channels[i].state == QHttpNetworkConnectionChannel::WritingState)
                QMetaObject::invokeMethod(&channels[i], "_q_uploadDataReadyRead", Qt::QueuedConnection);
#if QT_CONFIG(localserver)
        } else if (qobject_cast<QLocalSocket *>(channels[i].socket)) {
#if 0 // @todo Enable this when there is a debug category for this
            qDebug() << "Should resume socket but there is no way to do it for local sockets";
#endif
#endif
        }
    }

    // queue _q_startNextRequest
    QMetaObject::invokeMethod(this->q_func(), "_q_startNextRequest", Qt::QueuedConnection);
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 156, as _ZNK29QHttpNetworkConnectionPrivate7indexOfEP9QIODevice
inline int QHttpNetworkConnectionPrivate::indexOf(QIODevice *socket) const
{
    for (int i = 0; i < activeChannelCount; ++i)
        if (channels[i].socket == socket)
            return i;

    qFatal("Called with unknown socket object.");
    return 0;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 708, as _ZN29QHttpNetworkConnectionPrivate14requeueRequestERKSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE
inline void QHttpNetworkConnectionPrivate::requeueRequest(const HttpMessagePair &pair)
{
    Q_Q(QHttpNetworkConnection);

    QHttpNetworkRequest request = pair.first;
    switch (request.priority()) {
    case QHttpNetworkRequest::HighPriority:
        highPriorityQueue.prepend(pair);
        break;
    case QHttpNetworkRequest::NormalPriority:
    case QHttpNetworkRequest::LowPriority:
        lowPriorityQueue.prepend(pair);
        break;
    }

    QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 689, as _ZN29QHttpNetworkConnectionPrivate14fillHttp2QueueEv
inline void QHttpNetworkConnectionPrivate::fillHttp2Queue()
{
    for (auto &pair : highPriorityQueue) {
        if (!pair.second->d_func()->requestIsPrepared)
            prepareRequest(pair);
        channels[0].h2RequestsToSend.insert(QHttpNetworkRequest::HighPriority, pair);
    }

    highPriorityQueue.clear();

    for (auto &pair : lowPriorityQueue) {
        if (!pair.second->d_func()->requestIsPrepared)
            prepareRequest(pair);
        channels[0].h2RequestsToSend.insert(pair.first.priority(), pair);
    }

    lowPriorityQueue.clear();
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 726, as _ZN29QHttpNetworkConnectionPrivate14dequeueRequestEP9QIODevice
inline bool QHttpNetworkConnectionPrivate::dequeueRequest(QIODevice *socket)
{
    int i = 0;
    if (socket)
        i = indexOf(socket);

    if (!highPriorityQueue.isEmpty()) {
        // remove from queue before sendRequest! else we might pipeline the same request again
        HttpMessagePair messagePair = highPriorityQueue.takeLast();
        if (!messagePair.second->d_func()->requestIsPrepared)
            prepareRequest(messagePair);
        updateChannel(i, messagePair);
        return true;
    }

    if (!lowPriorityQueue.isEmpty()) {
        // remove from queue before sendRequest! else we might pipeline the same request again
        HttpMessagePair messagePair = lowPriorityQueue.takeLast();
        if (!messagePair.second->d_func()->requestIsPrepared)
            prepareRequest(messagePair);
        updateChannel(i, messagePair);
        return true;
    }
    return false;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 251, as _ZN29QHttpNetworkConnectionPrivate14prepareRequestERSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE
inline void QHttpNetworkConnectionPrivate::prepareRequest(HttpMessagePair &messagePair)
{
    QHttpNetworkRequest &request = messagePair.first;
    QHttpNetworkReply *reply = messagePair.second;

    // add missing fields for the request
    QByteArray value;
#ifndef Q_OS_WASM
    // check if Content-Length is provided
    QNonContiguousByteDevice* uploadByteDevice = request.uploadByteDevice();
    if (uploadByteDevice) {
        const qint64 contentLength = request.contentLength();
        const qint64 uploadDeviceSize = uploadByteDevice->size();
        if (contentLength != -1 && uploadDeviceSize != -1) {
            // Both values known: use the smaller one.
            if (uploadDeviceSize < contentLength)
                request.setContentLength(uploadDeviceSize);
        } else if (contentLength == -1 && uploadDeviceSize != -1) {
            // content length not supplied by user, but the upload device knows it
            request.setContentLength(uploadDeviceSize);
        } else if (contentLength != -1 && uploadDeviceSize == -1) {
            // everything OK, the user supplied us the contentLength
        } else if (Q_UNLIKELY(contentLength == -1 && uploadDeviceSize == -1)) {
            qFatal("QHttpNetworkConnectionPrivate: Neither content-length nor upload device size were given");
        }
    }
#endif
    // set the Connection/Proxy-Connection: Keep-Alive headers
#ifndef QT_NO_NETWORKPROXY
    if (networkProxy.type() == QNetworkProxy::HttpCachingProxy)  {
        value = request.headerField("proxy-connection");
        if (value.isEmpty())
            request.setHeaderField("Proxy-Connection", "Keep-Alive");
    } else {
#endif
        value = request.headerField("connection");
        if (value.isEmpty())
            request.setHeaderField("Connection", "Keep-Alive");
#ifndef QT_NO_NETWORKPROXY
    }
#endif

    // If the request had a accept-encoding set, we better not mess
    // with it. If it was not set, we announce that we understand gzip
    // and remember this fact in request.d->autoDecompress so that
    // we can later decompress the HTTP reply if it has such an
    // encoding.
    value = request.headerField("accept-encoding");
    if (value.isEmpty()) {
#ifndef QT_NO_COMPRESS
        const static QByteArray acceptedEncoding = QDecompressHelper::acceptedEncoding().join(", ");
        request.setHeaderField("Accept-Encoding", acceptedEncoding);
        request.d->autoDecompress = true;
#else
        // if zlib is not available set this to false always
        request.d->autoDecompress = false;
#endif
    }

    // some websites mandate an accept-language header and fail
    // if it is not sent. This is a problem with the website and
    // not with us, but we work around this by setting
    // one always.
    value = request.headerField("accept-language");
    if (value.isEmpty())
        request.setHeaderField("Accept-Language", makeAcceptLanguage());

    // set the User Agent
    value = request.headerField("user-agent");
    if (value.isEmpty())
        request.setHeaderField("User-Agent", "Mozilla/5.0");
    // set the host
    value = request.headerField("host");
    if (isLocalSocket && value.isEmpty()) {
        // The local socket connections might have a full file path, and that
        // may not be suitable for the Host header. But we can use whatever the
        // user has set in the URL.
        request.prependHeaderField("Host", request.url().host().toLocal8Bit());
    } else if (value.isEmpty()) {
        QHostAddress add;
        QByteArray host;
        if (add.setAddress(hostName)) {
            if (add.protocol() == QAbstractSocket::IPv6Protocol)
                host = (u'[' + removeZoneId(hostName) + u']').toLatin1(); //format the ipv6 in the standard way
            else
                host = hostName.toLatin1();

        } else {
            host = QUrl::toAce(hostName);
        }

        int port = request.url().port();
        if (port != -1) {
            host += ':';
            host += QByteArray::number(port);
        }

        request.prependHeaderField("Host", host);
    }

    reply->d_func()->requestIsPrepared = true;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 752, as _ZN29QHttpNetworkConnectionPrivate13updateChannelEiRKSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE
inline void QHttpNetworkConnectionPrivate::updateChannel(int i, const HttpMessagePair &messagePair)
{
    channels[i].request = messagePair.first;
    channels[i].reply = messagePair.second;
    // Now that reply is assigned a channel, correct reply to channel association
    // previously set in queueRequest.
    channels[i].reply->d_func()->connectionChannel = &channels[i];
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 761, as _ZNK29QHttpNetworkConnectionPrivate18predictNextRequestEv
inline QHttpNetworkRequest QHttpNetworkConnectionPrivate::predictNextRequest() const
{
    if (!highPriorityQueue.isEmpty())
        return highPriorityQueue.last().first;
    if (!lowPriorityQueue.isEmpty())
        return lowPriorityQueue.last().first;
    return QHttpNetworkRequest();
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 770, as _ZNK29QHttpNetworkConnectionPrivate24predictNextRequestsReplyEv
inline QHttpNetworkReply* QHttpNetworkConnectionPrivate::predictNextRequestsReply() const
{
    if (!highPriorityQueue.isEmpty())
        return highPriorityQueue.last().second;
    if (!lowPriorityQueue.isEmpty())
        return lowPriorityQueue.last().second;
    return nullptr;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 863, as _ZN29QHttpNetworkConnectionPrivate12fillPipelineER5QListISt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyEER29QHttpNetworkConnectionChannel
inline bool QHttpNetworkConnectionPrivate::fillPipeline(QList<HttpMessagePair> &queue, QHttpNetworkConnectionChannel &channel)
{
    if (queue.isEmpty())
        return true;

    for (int i = queue.size() - 1; i >= 0; --i) {
        HttpMessagePair messagePair = queue.at(i);
        const QHttpNetworkRequest &request = messagePair.first;

        // we currently do not support pipelining if HTTP authentication is used
        if (!request.url().userInfo().isEmpty())
            continue;

        // take only GET requests
        if (request.operation() != QHttpNetworkRequest::Get)
            continue;

        if (!request.isPipeliningAllowed())
            continue;

        // remove it from the queue
        queue.takeAt(i);
        // we modify the queue we iterate over here, but since we return from the function
        // afterwards this is fine.

        // actually send it
        if (!messagePair.second->d_func()->requestIsPrepared)
            prepareRequest(messagePair);
        channel.pipelineInto(messagePair);

        // return false because we processed something and need to process again
        return false;
    }

    // return true, the queue has been processed and not changed
    return true;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 1220, as _ZN29QHttpNetworkConnectionPrivate13readMoreLaterEP17QHttpNetworkReply
inline void QHttpNetworkConnectionPrivate::readMoreLater(QHttpNetworkReply *reply)
{
    for (int i = 0 ; i < activeChannelCount; ++i) {
        if (channels[i].reply ==  reply) {
            // emulate a readyRead() from the socket
            QMetaObject::invokeMethod(&channels[i], "_q_readyRead", Qt::QueuedConnection);
            return;
        }
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 388, as _ZN29QHttpNetworkConnectionPrivate15copyCredentialsEiP14QAuthenticatorb
inline void QHttpNetworkConnectionPrivate::copyCredentials(int fromChannel, QAuthenticator *auth, bool isProxy)
{
    Q_ASSERT(auth);

    // NTLM and Negotiate do multi-phase authentication.
    // Copying credentialsbetween authenticators would mess things up.
    if (fromChannel >= 0) {
        QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(*auth);
        if (priv
            && (priv->method == QAuthenticatorPrivate::Ntlm
                || priv->method == QAuthenticatorPrivate::Negotiate)) {
            return;
        }
    }

    // select another channel
    QAuthenticator* otherAuth = nullptr;
    for (int i = 0; i < activeChannelCount; ++i) {
        if (i == fromChannel)
            continue;
        if (isProxy)
            otherAuth = &channels[i].proxyAuthenticator;
        else
            otherAuth = &channels[i].authenticator;
        // if the credentials are different, copy them
        if (otherAuth->user().compare(auth->user()))
            otherAuth->setUser(auth->user());
        if (otherAuth->password().compare(auth->password()))
            otherAuth->setPassword(auth->password());
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 1371, as _ZN29QHttpNetworkConnectionPrivate20networkLayerDetectedEN15QAbstractSocket20NetworkLayerProtocolE
inline void QHttpNetworkConnectionPrivate::networkLayerDetected(QAbstractSocket::NetworkLayerProtocol protocol)
{
    for (int i = 0 ; i < activeChannelCount; ++i) {
        if ((channels[i].networkLayerPreference != protocol) && (channels[i].state == QHttpNetworkConnectionChannel::ConnectingState)) {
            channels[i].close();
        }
    }
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

//  from src/network/access/qhttpnetworkconnection.cpp, line 902, as _ZN29QHttpNetworkConnectionPrivate11errorDetailEN13QNetworkReply12NetworkErrorEP9QIODeviceRK7QString
inline QString QHttpNetworkConnectionPrivate::errorDetail(QNetworkReply::NetworkError errorCode, QIODevice *socket, const QString &extraDetail)
{
    QString errorString;
    switch (errorCode) {
    case QNetworkReply::HostNotFoundError: {
        const QString peerName = socket ? QSocketAbstraction::socketPeerName(socket) : hostName;
        errorString = QCoreApplication::translate("QHttp", "Host %1 not found").arg(peerName);
        break;
    }
    case QNetworkReply::ConnectionRefusedError:
        errorString = QCoreApplication::translate("QHttp", "Connection refused");
        break;
    case QNetworkReply::RemoteHostClosedError:
        errorString = QCoreApplication::translate("QHttp", "Connection closed");
        break;
    case QNetworkReply::TimeoutError:
        errorString = QCoreApplication::translate("QAbstractSocket", "Socket operation timed out");
        break;
    case QNetworkReply::ProxyAuthenticationRequiredError:
        errorString = QCoreApplication::translate("QHttp", "Proxy requires authentication");
        break;
    case QNetworkReply::AuthenticationRequiredError:
        errorString = QCoreApplication::translate("QHttp", "Host requires authentication");
        break;
    case QNetworkReply::ProtocolFailure:
        errorString = QCoreApplication::translate("QHttp", "Data corrupted");
        break;
    case QNetworkReply::ProtocolUnknownError:
        errorString = QCoreApplication::translate("QHttp", "Unknown protocol specified");
        break;
    case QNetworkReply::SslHandshakeFailedError:
        errorString = QCoreApplication::translate("QHttp", "SSL handshake failed");
        if (socket)
            errorString += ": "_L1 + socket->errorString();
        break;
    case QNetworkReply::TooManyRedirectsError:
        errorString = QCoreApplication::translate("QHttp", "Too many redirects");
        break;
    case QNetworkReply::InsecureRedirectError:
        errorString = QCoreApplication::translate("QHttp", "Insecure redirect");
        break;
    default:
        // all other errors are treated as QNetworkReply::UnknownNetworkError
        errorString = extraDetail;
        break;
    }
    return errorString;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 953, as _ZN29QHttpNetworkConnectionPrivate11removeReplyEP17QHttpNetworkReply
inline void QHttpNetworkConnectionPrivate::removeReply(QHttpNetworkReply *reply)
{
    Q_Q(QHttpNetworkConnection);

    // check if the reply is currently being processed or it is pipelined in
    for (int i = 0; i < activeChannelCount; ++i) {
        // is the reply associated the currently processing of this channel?
        if (channels[i].reply == reply) {
            channels[i].reply = nullptr;
            if (channels[i].protocolHandler)
                channels[i].protocolHandler->setReply(nullptr);
            channels[i].request = QHttpNetworkRequest();
            channels[i].resendCurrent = false;

            if (!reply->isFinished() && !channels[i].alreadyPipelinedRequests.isEmpty()) {
                // the reply had to be prematurely removed, e.g. it was not finished
                // therefore we have to requeue the already pipelined requests.
                channels[i].requeueCurrentlyPipelinedRequests();
            }

            // if HTTP mandates we should close
            // or the reply is not finished yet, e.g. it was aborted
            // we have to close that connection
            if (reply->d_func()->isConnectionCloseEnabled() || !reply->isFinished()) {
                if (reply->isAborted()) {
                    channels[i].abort();
                } else {
                    channels[i].close();
                }
            }

            QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
            return;
        }

        // is the reply inside the pipeline of this channel already?
        for (int j = 0; j < channels[i].alreadyPipelinedRequests.size(); j++) {
            if (channels[i].alreadyPipelinedRequests.at(j).second == reply) {
               // Remove that HttpMessagePair
               channels[i].alreadyPipelinedRequests.removeAt(j);

               channels[i].requeueCurrentlyPipelinedRequests();

               // Since some requests had already been pipelined, but we removed
               // one and re-queued the others
               // we must force a connection close after the request that is
               // currently in processing has been finished.
               if (channels[i].reply)
                   channels[i].reply->d_func()->forceConnectionCloseEnabled = true;

               QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
               return;
            }
        }
        // is the reply inside the H2 pipeline of this channel already?
        const auto foundReply = [reply](const HttpMessagePair &pair) {
            return pair.second == reply;
        };
        auto &seq = channels[i].h2RequestsToSend;
        const auto end = seq.cend();
        auto it = std::find_if(seq.cbegin(), end, foundReply);
        if (it != end) {
            seq.erase(it);
            QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
            return;
        }
        // Check if the h2 protocol handler already started processing it
        if ((connectionType == QHttpNetworkConnection::ConnectionTypeHTTP2Direct
             || channels[i].switchedToHttp2)
            && channels[i].protocolHandler) {
            if (channels[i].protocolHandler->tryRemoveReply(reply))
                return;
        }
    }
    // remove from the high priority queue
    if (!highPriorityQueue.isEmpty()) {
        for (int j = highPriorityQueue.size() - 1; j >= 0; --j) {
            HttpMessagePair messagePair = highPriorityQueue.at(j);
            if (messagePair.second == reply) {
                highPriorityQueue.removeAt(j);
                QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
                return;
            }
        }
    }
    // remove from the low priority queue
    if (!lowPriorityQueue.isEmpty()) {
        for (int j = lowPriorityQueue.size() - 1; j >= 0; --j) {
            HttpMessagePair messagePair = lowPriorityQueue.at(j);
            if (messagePair.second == reply) {
                lowPriorityQueue.removeAt(j);
                QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
                return;
            }
        }
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 218, as _ZNK29QHttpNetworkConnectionPrivate26uncompressedBytesAvailableERK17QHttpNetworkReply
inline qint64 QHttpNetworkConnectionPrivate::uncompressedBytesAvailable(const QHttpNetworkReply &reply) const
{
    return reply.d_func()->responseData.byteAmount();
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 223, as _ZNK29QHttpNetworkConnectionPrivate35uncompressedBytesAvailableNextBlockERK17QHttpNetworkReply
inline qint64 QHttpNetworkConnectionPrivate::uncompressedBytesAvailableNextBlock(const QHttpNetworkReply &reply) const
{
    return reply.d_func()->responseData.sizeNextBlock();
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 357, as _ZN29QHttpNetworkConnectionPrivate14emitReplyErrorEP9QIODeviceP17QHttpNetworkReplyN13QNetworkReply12NetworkErrorE
inline void QHttpNetworkConnectionPrivate::emitReplyError(QIODevice *socket,
                                                   QHttpNetworkReply *reply,
                                                   QNetworkReply::NetworkError errorCode)
{
    Q_Q(QHttpNetworkConnection);

    int i = 0;
    if (socket)
        i = indexOf(socket);

    if (reply) {
        // this error matters only to this reply
        reply->d_func()->errorString = errorDetail(errorCode, socket);
        emit reply->finishedWithError(errorCode, reply->d_func()->errorString);
        // remove the corrupt data if any
        reply->d_func()->eraseData();

        // Clean the channel
        channels[i].close();
        channels[i].reply = nullptr;
        if (channels[i].protocolHandler)
            channels[i].protocolHandler->setReply(nullptr);
        channels[i].request = QHttpNetworkRequest();
        if (socket)
            channels[i].requeueCurrentlyPipelinedRequests();

        // send the next request
        QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
    }
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 422, as _ZN29QHttpNetworkConnectionPrivate27handleAuthenticateChallengeEP9QIODeviceP17QHttpNetworkReplybRb
inline bool QHttpNetworkConnectionPrivate::handleAuthenticateChallenge(QIODevice *socket, QHttpNetworkReply *reply,
                                                                bool isProxy, bool &resend)
{
    Q_ASSERT(socket);
    Q_ASSERT(reply);

    resend = false;
    //create the response header to be used with QAuthenticatorPrivate.
    const auto headers = reply->header();

    // Check that any of the proposed authenticate methods are supported
    const QByteArray header = isProxy ? "proxy-authenticate" : "www-authenticate";
    const QByteArrayList &authenticationMethods = reply->d_func()->headerFieldValues(header);
    const bool isSupported = std::any_of(authenticationMethods.begin(), authenticationMethods.end(),
                                         QAuthenticatorPrivate::isMethodSupported);
    if (isSupported) {
        int i = indexOf(socket);
        //Use a single authenticator for all domains. ### change later to use domain/realm
        QAuthenticator *auth = isProxy ? &channels[i].proxyAuthenticator
                                       : &channels[i].authenticator;
        //proceed with the authentication.
        if (auth->isNull())
            auth->detach();
        QAuthenticatorPrivate *priv = QAuthenticatorPrivate::getPrivate(*auth);
        priv->parseHttpResponse(headers, isProxy, reply->url().host());
        // Update method in case it changed
        if (priv->method == QAuthenticatorPrivate::None)
            return false;

        if (priv->phase == QAuthenticatorPrivate::Done ||
                (priv->phase == QAuthenticatorPrivate::Start
                    && (priv->method == QAuthenticatorPrivate::Ntlm
                        || priv->method == QAuthenticatorPrivate::Negotiate))) {
            if (priv->phase == QAuthenticatorPrivate::Start)
                priv->phase = QAuthenticatorPrivate::Phase1;

            pauseConnection();
            if (!isProxy) {
                if (channels[i].authenticationCredentialsSent) {
                    auth->detach();
                    priv = QAuthenticatorPrivate::getPrivate(*auth);
                    priv->hasFailed = true;
                    priv->phase = QAuthenticatorPrivate::Done;
                    channels[i].authenticationCredentialsSent = false;
                }
                emit reply->authenticationRequired(reply->request(), auth);
#ifndef QT_NO_NETWORKPROXY
            } else {
                if (channels[i].proxyCredentialsSent) {
                    auth->detach();
                    priv = QAuthenticatorPrivate::getPrivate(*auth);
                    priv->hasFailed = true;
                    priv->phase = QAuthenticatorPrivate::Done;
                    channels[i].proxyCredentialsSent = false;
                }
                emit reply->proxyAuthenticationRequired(networkProxy, auth);
#endif
            }
            resumeConnection();

            if (priv->phase != QAuthenticatorPrivate::Done) {
                // send any pending requests
                copyCredentials(i,  auth, isProxy);
            }
        } else if (priv->phase == QAuthenticatorPrivate::Start) {
            // If the url's authenticator has a 'user' set we will end up here (phase is only set to 'Done' by
            // parseHttpResponse above if 'user' is empty). So if credentials were supplied with the request,
            // such as in the case of an XMLHttpRequest, this is our only opportunity to cache them.
            emit reply->cacheCredentials(reply->request(), auth);
        }
        // - Changing values in QAuthenticator will reset the 'phase'. Therefore if it is still "Done"
        //   then nothing was filled in by the user or the cache
        // - If withCredentials has been set to false (e.g. by Qt WebKit for a cross-origin XMLHttpRequest) then
        //   we need to bail out if authentication is required.
        if (priv->phase == QAuthenticatorPrivate::Done || !reply->request().withCredentials()) {
            // Reset authenticator so the next request on that channel does not get messed up
            auth = nullptr;
            if (isProxy)
                channels[i].proxyAuthenticator = QAuthenticator();
            else
                channels[i].authenticator = QAuthenticator();

            // authentication is cancelled, send the current contents to the user.
            emit reply->headerChanged();
            emit reply->readyRead();
            QNetworkReply::NetworkError errorCode =
                isProxy
                ? QNetworkReply::ProxyAuthenticationRequiredError
                : QNetworkReply::AuthenticationRequiredError;
            reply->d_func()->errorString = errorDetail(errorCode, socket);
            emit reply->finishedWithError(errorCode, reply->d_func()->errorString);
            // ### at this point the reply could be deleted
            return true;
        }
        //resend the request
        resend = true;
        return true;
    }
    return false;
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 535, as _ZN29QHttpNetworkConnectionPrivate21parseRedirectResponseEP17QHttpNetworkReply
inline QHttpNetworkConnectionPrivate::ParseRedirectResult
QHttpNetworkConnectionPrivate::parseRedirectResponse(QHttpNetworkReply *reply)
{
    if (!reply->request().isFollowRedirects())
        return {{}, QNetworkReply::NoError};

    QUrl redirectUrl;
    const QHttpHeaders fields = reply->header();
    if (const auto h = fields.values(QHttpHeaders::WellKnownHeader::Location); !h.empty()) {
        redirectUrl = QUrl::fromEncoded(h.first());
    }

    // If the location url is invalid/empty, we return ProtocolUnknownError
    if (!redirectUrl.isValid())
        return {{}, QNetworkReply::ProtocolUnknownError};

    // Check if we have exceeded max redirects allowed
    if (reply->request().redirectCount() <= 0)
        return {{}, QNetworkReply::TooManyRedirectsError};

    // Resolve the URL if it's relative
    if (redirectUrl.isRelative())
        redirectUrl = reply->request().url().resolved(redirectUrl);

    // Check redirect url protocol
    const QUrl priorUrl(reply->request().url());
    const QString targetUrlScheme = redirectUrl.scheme();
    if (targetUrlScheme == "http"_L1 || targetUrlScheme == "https"_L1
        || targetUrlScheme.startsWith("unix"_L1)) {
        switch (reply->request().redirectPolicy()) {
        case QNetworkRequest::NoLessSafeRedirectPolicy:
            // Here we could handle https->http redirects as InsecureProtocolError.
            // However, if HSTS is enabled and redirectUrl.host() is a known STS
            // host, then we'll replace its scheme and this won't downgrade protocol,
            // after all.  We cannot access QNAM's STS cache from here, so delegate
            // this check to QNetworkReplyHttpImpl.
            break;
        case QNetworkRequest::SameOriginRedirectPolicy:
            if (priorUrl.host() != redirectUrl.host()
                || priorUrl.scheme() != targetUrlScheme
                || priorUrl.port() != redirectUrl.port()) {
                return {{}, QNetworkReply::InsecureRedirectError};
            }
            break;
        case QNetworkRequest::UserVerifiedRedirectPolicy:
            break;
        default:
            Q_ASSERT(!"Unexpected redirect policy");
        }
    } else {
        return {{}, QNetworkReply::ProtocolUnknownError};
    }
    return {std::move(redirectUrl), QNetworkReply::NoError};
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 524, as _ZN29QHttpNetworkConnectionPrivate21parseRedirectResponseEP9QIODeviceP17QHttpNetworkReply
inline QUrl QHttpNetworkConnectionPrivate::parseRedirectResponse(QIODevice *socket,
                                                          QHttpNetworkReply *reply)
{
    ParseRedirectResult result = parseRedirectResponse(reply);
    if (result.errorCode != QNetworkReply::NoError) {
        emitReplyError(socket, reply, result.errorCode);
        return {};
    }
    return std::move(result.redirectUrl);
}

//  from src/network/access/qhttpnetworkconnection.cpp, line 1608, as _ZN29QHttpNetworkConnectionPrivate31emitProxyAuthenticationRequiredEPK29QHttpNetworkConnectionChannelRK13QNetworkProxyP14QAuthenticator
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpNetworkConnectionPrivate::emitProxyAuthenticationRequired(const QHttpNetworkConnectionChannel *chan, const QNetworkProxy &proxy, QAuthenticator* auth)
{
    // Also pause the connection because socket notifiers may fire while an user
    // dialog is displaying
    pauseConnection();
    QHttpNetworkReply *reply;
    if ((connectionType == QHttpNetworkConnection::ConnectionTypeHTTP2
         && (chan->switchedToHttp2 || chan->h2RequestsToSend.size() > 0))
        || connectionType == QHttpNetworkConnection::ConnectionTypeHTTP2Direct) {
        // we choose the reply to emit the proxyAuth signal from somewhat arbitrarily,
        // but that does not matter because the signal will ultimately be emitted
        // by the QNetworkAccessManager.
        Q_ASSERT(chan->h2RequestsToSend.size() > 0);
        reply = chan->h2RequestsToSend.cbegin().value().second;
    } else { // HTTP
        reply = chan->reply;
    }

    Q_ASSERT(reply);
    emit reply->proxyAuthenticationRequired(proxy, auth);
    resumeConnection();
    int i = indexOf(chan->socket);
    copyCredentials(i, auth, true);
}
#endif  // !defined(QT_NO_NETWORKPROXY)
//  -----------------------------------------------------------------------

//  QHttpNetworkConnection *QHttpNetworkConnectionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHttpNetworkConnection *ritual_ZN29QHttpNetworkConnectionPrivate6q_funcEv(
    QHttpNetworkConnectionPrivate *self) {
  return self->q_func();
}

//  const QHttpNetworkConnection *QHttpNetworkConnectionPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QHttpNetworkConnection *ritual_ZNK29QHttpNetworkConnectionPrivate6q_funcEv(
    const QHttpNetworkConnectionPrivate *self) {
  return self->q_func();
}

//  QHttpNetworkConnectionPrivate::~QHttpNetworkConnectionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivateD1Ev(
    QHttpNetworkConnectionPrivate *self) {
  delete self;
}

//  void QHttpNetworkConnectionPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate4initEv(
    QHttpNetworkConnectionPrivate *self) {
  self->init();
}

//  void QHttpNetworkConnectionPrivate::pauseConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate15pauseConnectionEv(
    QHttpNetworkConnectionPrivate *self) {
  self->pauseConnection();
}

//  void QHttpNetworkConnectionPrivate::resumeConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate16resumeConnectionEv(
    QHttpNetworkConnectionPrivate *self) {
  self->resumeConnection();
}

//  int QHttpNetworkConnectionPrivate::indexOf(QIODevice *socket) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QHttpNetworkConnectionPrivate7indexOfEP9QIODevice(
    const QHttpNetworkConnectionPrivate *self,
    QIODevice *socket) {
  return self->indexOf(socket);
}

//  void QHttpNetworkConnectionPrivate::requeueRequest(const HttpMessagePair
//      &pair)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate14requeueRequestERKSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE(
    QHttpNetworkConnectionPrivate *self,
    const HttpMessagePair *pair) {
  self->requeueRequest(*pair);
}

//  void QHttpNetworkConnectionPrivate::fillHttp2Queue()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate14fillHttp2QueueEv(
    QHttpNetworkConnectionPrivate *self) {
  self->fillHttp2Queue();
}

//  bool QHttpNetworkConnectionPrivate::dequeueRequest(QIODevice *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QHttpNetworkConnectionPrivate14dequeueRequestEP9QIODevice(
    QHttpNetworkConnectionPrivate *self,
    QIODevice *socket) {
  return self->dequeueRequest(socket);
}

//  void QHttpNetworkConnectionPrivate::prepareRequest(HttpMessagePair
//      &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate14prepareRequestERSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE(
    QHttpNetworkConnectionPrivate *self,
    HttpMessagePair *request) {
  self->prepareRequest(*request);
}

//  void QHttpNetworkConnectionPrivate::updateChannel(int i, const
//      HttpMessagePair &messagePair)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate13updateChannelEiRKSt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyE(
    QHttpNetworkConnectionPrivate *self,
    int i,
    const HttpMessagePair *messagePair) {
  self->updateChannel(i, *messagePair);
}

//  QHttpNetworkRequest QHttpNetworkConnectionPrivate::predictNextRequest()
//      const
extern "C" Q_DECL_EXPORT
QHttpNetworkRequest *ritual_ZNK29QHttpNetworkConnectionPrivate18predictNextRequestEv(
    const QHttpNetworkConnectionPrivate *self) {
  return new QHttpNetworkRequest(self->predictNextRequest());
}

//  QHttpNetworkReply
//      *QHttpNetworkConnectionPrivate::predictNextRequestsReply() const
extern "C" Q_DECL_EXPORT
QHttpNetworkReply *ritual_ZNK29QHttpNetworkConnectionPrivate24predictNextRequestsReplyEv(
    const QHttpNetworkConnectionPrivate *self) {
  return self->predictNextRequestsReply();
}

//  bool QHttpNetworkConnectionPrivate::fillPipeline(QList<HttpMessagePair>
//      &queue, QHttpNetworkConnectionChannel &channel)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QHttpNetworkConnectionPrivate12fillPipelineER5QListISt4pairI19QHttpNetworkRequestP17QHttpNetworkReplyEER29QHttpNetworkConnectionChannel(
    QHttpNetworkConnectionPrivate *self,
    QList<HttpMessagePair> *queue,
    QHttpNetworkConnectionChannel *channel) {
  return self->fillPipeline(*queue, *channel);
}

//  void QHttpNetworkConnectionPrivate::readMoreLater(QHttpNetworkReply
//      *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate13readMoreLaterEP17QHttpNetworkReply(
    QHttpNetworkConnectionPrivate *self,
    QHttpNetworkReply *reply) {
  self->readMoreLater(reply);
}

//  void QHttpNetworkConnectionPrivate::copyCredentials(int fromChannel,
//      QAuthenticator *auth, bool isProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate15copyCredentialsEiP14QAuthenticatorb(
    QHttpNetworkConnectionPrivate *self,
    int fromChannel,
    QAuthenticator *auth,
    bool isProxy) {
  self->copyCredentials(fromChannel, auth, isProxy);
}

//  void QHttpNetworkConnectionPrivate::networkLayerDetected(QAbstractSocket:
//      :NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate20networkLayerDetectedEN15QAbstractSocket20NetworkLayerProtocolE(
    QHttpNetworkConnectionPrivate *self,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  self->networkLayerDetected(protocol);
}

//  void QHttpNetworkConnectionPrivate::createAuthorization(QIODevice
//      *socket, QHttpNetworkRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate19createAuthorizationEP9QIODeviceR19QHttpNetworkRequest(
    QHttpNetworkConnectionPrivate *self,
    QIODevice *socket,
    QHttpNetworkRequest *request) {
  self->createAuthorization(socket, *request);
}

//  QString
//      QHttpNetworkConnectionPrivate::errorDetail(QNetworkReply::NetworkErro
//      r errorCode, QIODevice *socket, const QString &extraDetail)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QHttpNetworkConnectionPrivate11errorDetailEN13QNetworkReply12NetworkErrorEP9QIODeviceRK7QString(
    QHttpNetworkConnectionPrivate *self,
    QNetworkReply::NetworkError errorCode,
    QIODevice *socket,
    const QString *extraDetail) {
  return new QString(self->errorDetail(errorCode, socket, *extraDetail));
}

//  void QHttpNetworkConnectionPrivate::removeReply(QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate11removeReplyEP17QHttpNetworkReply(
    QHttpNetworkConnectionPrivate *self,
    QHttpNetworkReply *reply) {
  self->removeReply(reply);
}

//  qint64 QHttpNetworkConnectionPrivate::uncompressedBytesAvailable(const
//      QHttpNetworkReply &reply) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK29QHttpNetworkConnectionPrivate26uncompressedBytesAvailableERK17QHttpNetworkReply(
    const QHttpNetworkConnectionPrivate *self,
    const QHttpNetworkReply *reply) {
  return self->uncompressedBytesAvailable(*reply);
}

//  qint64
//      QHttpNetworkConnectionPrivate::uncompressedBytesAvailableNextBlock(co
//      nst QHttpNetworkReply &reply) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK29QHttpNetworkConnectionPrivate35uncompressedBytesAvailableNextBlockERK17QHttpNetworkReply(
    const QHttpNetworkConnectionPrivate *self,
    const QHttpNetworkReply *reply) {
  return self->uncompressedBytesAvailableNextBlock(*reply);
}

//  void QHttpNetworkConnectionPrivate::emitReplyError(QIODevice *socket,
//      QHttpNetworkReply *reply, QNetworkReply::NetworkError errorCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate14emitReplyErrorEP9QIODeviceP17QHttpNetworkReplyN13QNetworkReply12NetworkErrorE(
    QHttpNetworkConnectionPrivate *self,
    QIODevice *socket,
    QHttpNetworkReply *reply,
    QNetworkReply::NetworkError errorCode) {
  self->emitReplyError(socket, reply, errorCode);
}

//  bool QHttpNetworkConnectionPrivate::handleAuthenticateChallenge(QIODevice
//      *socket, QHttpNetworkReply *reply, bool isProxy, bool &resend)
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QHttpNetworkConnectionPrivate27handleAuthenticateChallengeEP9QIODeviceP17QHttpNetworkReplybRb(
    QHttpNetworkConnectionPrivate *self,
    QIODevice *socket,
    QHttpNetworkReply *reply,
    bool isProxy,
    bool *resend) {
  return self->handleAuthenticateChallenge(socket, reply, isProxy, *resend);
}

//  ParseRedirectResult
//      QHttpNetworkConnectionPrivate::parseRedirectResponse(QHttpNetworkRepl
//      y *reply)
extern "C" Q_DECL_EXPORT
QHttpNetworkConnectionPrivate::ParseRedirectResult *ritual_ZN29QHttpNetworkConnectionPrivate21parseRedirectResponseEP17QHttpNetworkReply(
    QHttpNetworkReply *reply) {
  return new QHttpNetworkConnectionPrivate::ParseRedirectResult(
      QHttpNetworkConnectionPrivate::parseRedirectResponse(
          reply));
}

//  QUrl QHttpNetworkConnectionPrivate::parseRedirectResponse(QIODevice
//      *socket, QHttpNetworkReply *reply)
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZN29QHttpNetworkConnectionPrivate21parseRedirectResponseEP9QIODeviceP17QHttpNetworkReply(
    QHttpNetworkConnectionPrivate *self,
    QIODevice *socket,
    QHttpNetworkReply *reply) {
  return new QUrl(self->parseRedirectResponse(socket, reply));
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpNetworkConnectionPrivate::emitProxyAuthenticationRequired(const
//      QHttpNetworkConnectionChannel *chan, const QNetworkProxy &proxy,
//      QAuthenticator *auth)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionPrivate31emitProxyAuthenticationRequiredEPK29QHttpNetworkConnectionChannelRK13QNetworkProxyP14QAuthenticator(
    QHttpNetworkConnectionPrivate *self,
    const QHttpNetworkConnectionChannel *chan,
    const QNetworkProxy *proxy,
    QAuthenticator *auth) {
  self->emitProxyAuthenticationRequired(chan, *proxy, auth);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
