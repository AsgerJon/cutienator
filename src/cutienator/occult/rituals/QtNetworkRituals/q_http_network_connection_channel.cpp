//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnectionchannel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtNetwork/private/qhttpprotocolhandler_p.h>
#include <QtCore/private/qnoncontiguousbytedevice_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
#include <QtNetwork/private/qsocketabstraction_p.h>
#include <QtNetwork/private/qabstractprotocolhandler_p.h>
#include <QtNetwork/private/qhttpnetworkconnectionchannel_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttp2protocolhandler.cpp, line 145, as _ZNK21QHttp2ProtocolHandler11isGoingAwayEv
inline bool QHttp2ProtocolHandler::isGoingAway() const noexcept
{
    return h2Connection && h2Connection->isGoingAway();
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 188, as _ZN19QHttpNetworkRequestD1Ev
inline QHttpNetworkRequest::~QHttpNetworkRequest()
{
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

//  from src/network/access/qhttpnetworkreply.cpp, line 513, as _ZN24QHttpNetworkReplyPrivate24isConnectionCloseEnabledEv
inline bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()
{
    return connectionCloseEnabled || forceConnectionCloseEnabled;
}

//  from src/network/access/qhttpprotocolhandler.cpp, line 15, as _ZN20QHttpProtocolHandlerC1EP29QHttpNetworkConnectionChannel
inline QHttpProtocolHandler::QHttpProtocolHandler(QHttpNetworkConnectionChannel *channel)
    : QAbstractProtocolHandler(channel)
{
}

//  from src/network/access/qhttp2protocolhandler.cpp, line 150, as _ZN21QHttp2ProtocolHandler23handleConnectionClosureEv
inline void QHttp2ProtocolHandler::handleConnectionClosure()
{
    // The channel has just received RemoteHostClosedError and since it will
    // not try (for HTTP/2) to re-connect, it's time to finish all replies
    // with error.

    // Maybe we still have some data to read and can successfully finish
    // a stream/request?
    _q_receiveReply();
    h2Connection->handleConnectionClosure();
}

//  from src/network/access/qabstractprotocolhandler.cpp, line 22, as _ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply
inline void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
{
    m_reply = reply;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 739, as _ZN24QHttpNetworkReplyPrivate13expectContentEv
inline bool QHttpNetworkReplyPrivate::expectContent()
{
    int statusCode = parser.getStatusCode();
    // check whether we can expect content after the headers (rfc 2616, sec4.4)
    if ((statusCode >= 100 && statusCode < 200)
        || statusCode == 204 || statusCode == 304)
        return false;
    if (request.operation() == QHttpNetworkRequest::Head)
        return false; // no body expected for HEAD request
    qint64 expectedContentLength = contentLength();
    if (expectedContentLength == 0)
        return false;
    if (expectedContentLength == -1 && bodyLength == 0) {
        // The content-length header was stripped, but its value was 0.
        // This would be the case for an explicitly zero-length compressed response.
        return false;
    }
    return true;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 508, as _ZN24QHttpNetworkReplyPrivate9isChunkedEv
inline bool QHttpNetworkReplyPrivate::isChunked()
{
    return chunkedTransferEncoding;
}

//  from src/network/access/qhttpnetworkreply.cpp, line 759, as _ZN24QHttpNetworkReplyPrivate9eraseDataEv
inline void QHttpNetworkReplyPrivate::eraseData()
{
    responseData.clear();
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

//  from src/network/access/qhttpnetworkconnection.cpp, line 170, as _ZN29QHttpNetworkConnectionPrivate22shouldEmitChannelErrorEP9QIODevice
inline bool QHttpNetworkConnectionPrivate::shouldEmitChannelError(QIODevice *socket)
{
    Q_Q(QHttpNetworkConnection);

    bool emitError = true;
    int i = indexOf(socket);
    int otherSocket = (i == 0 ? 1 : 0);

    // If the IPv4 connection still isn't started we need to start it now.
    if (delayedConnectionTimer.isActive()) {
        delayedConnectionTimer.stop();
        channels[otherSocket].ensureConnection();
    }

    if (activeChannelCount < channelCount) {
        if (networkLayerState == HostLookupPending || networkLayerState == IPv4or6)
            networkLayerState = QHttpNetworkConnectionPrivate::Unknown;
        channels[0].close();
        emitError = true;
    } else {
        if (networkLayerState == HostLookupPending || networkLayerState == IPv4or6) {
            if (channels[otherSocket].isSocketBusy() && (channels[otherSocket].state != QHttpNetworkConnectionChannel::ClosingState)) {
                // this was the first socket to fail.
                channels[i].close();
                emitError = false;
            }
            else {
                // Both connection attempts has failed.
                networkLayerState = QHttpNetworkConnectionPrivate::Unknown;
                channels[i].close();
                emitError = true;
            }
        } else {
            if (((networkLayerState == QHttpNetworkConnectionPrivate::IPv4) && (channels[i].networkLayerPreference != QAbstractSocket::IPv4Protocol))
                || ((networkLayerState == QHttpNetworkConnectionPrivate::IPv6) && (channels[i].networkLayerPreference != QAbstractSocket::IPv6Protocol))) {
                // First connection worked so this is the second one to complete and it failed.
                channels[i].close();
                QMetaObject::invokeMethod(q, "_q_startNextRequest", Qt::QueuedConnection);
                emitError = false;
            }
            if (networkLayerState == QHttpNetworkConnectionPrivate::Unknown)
                qWarning("We got a connection error when networkLayerState is Unknown");
        }
    }
    return emitError;
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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 843, as _ZNK29QHttpNetworkConnectionChannel17h2ProtocolHandlerEv
inline QHttp2ProtocolHandler *QHttpNetworkConnectionChannel::h2ProtocolHandler() const noexcept
{
    if (!protocolHandler)
        return nullptr;
    const auto type = connection->connectionType();
    if (type == QHttpNetworkConnection::ConnectionTypeHTTP2Direct
        || (type == QHttpNetworkConnection::ConnectionTypeHTTP2 && switchedToHttp2)) {
        return static_cast<QHttp2ProtocolHandler *>(protocolHandler.get());
    }
    return nullptr;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 861, as _ZNK29QHttpNetworkConnectionChannel18isPendingReconnectEv
inline bool QHttpNetworkConnectionChannel::isPendingReconnect() const noexcept
{
    // A closing socket will emit disconnected(), which restarts the request queue.
    if (QSocketAbstraction::socketState(socket) == QAbstractSocket::ClosingState)
        return true;
    if (auto *h2 = h2ProtocolHandler())
        return h2->isGoingAway();
    // HTTP1 protocol handler is created early and never un-set so we can do this short test to see
    // if HTTP2 is currently un-set and needs to be re-created:
    return !protocolHandler;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 878, as _ZN29QHttpNetworkConnectionChannel21clearPendingReconnectEv
inline bool QHttpNetworkConnectionChannel::clearPendingReconnect()
{
    // Only an HTTP/2 session is dropped here. The HTTP/1 handler is created once and never
    // recreated, so dropping it would leave protocolHandler null for the next sendRequest().
    if (auto *h2 = h2ProtocolHandler(); !h2 || !h2->isGoingAway())
        return false;
    // We can be called from within the handler's own call chain, so destroy it in a queued
    // call rather than under its own stack frame. Moving from the unique_ptr already
    // clears the pending-reconnect state.
    QMetaObject::invokeMethod(this, [oldHandler = std::move(protocolHandler)]() mutable {
        oldHandler.reset();
    }, Qt::QueuedConnection);
    return true;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 731, as _ZN29QHttpNetworkConnectionChannel15ignoreSslErrorsEv
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::ignoreSslErrors()
{
    // AXIVION DISABLE Qt-Security-QSslSocketIgnoreSslErrors: intentional behavior
    if (socket)
        static_cast<QSslSocket *>(socket)->ignoreSslErrors();
    // AXIVION ENABLE Qt-Security-QSslSocketIgnoreSslErrors

    ignoreAllSslErrors = true;
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 742, as _ZN29QHttpNetworkConnectionChannel15ignoreSslErrorsERK5QListI9QSslErrorE
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::ignoreSslErrors(const QList<QSslError> &errors)
{
    // AXIVION DISABLE Qt-Security-QSslSocketIgnoreSslErrors: intentional behavior
    if (socket)
        static_cast<QSslSocket *>(socket)->ignoreSslErrors(errors);
    // AXIVION ENABLE Qt-Security-QSslSocketIgnoreSslErrors

    ignoreSslErrorsList = errors;
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 752, as _ZN29QHttpNetworkConnectionChannel19setSslConfigurationERK17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::setSslConfiguration(const QSslConfiguration &config)
{
    if (socket)
        static_cast<QSslSocket *>(socket)->setSslConfiguration(config);

    if (sslConfiguration)
        *sslConfiguration = config;
    else
        sslConfiguration = QSslConfiguration(config);
}
#endif  // !defined(QT_NO_SSL)

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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 587, as _ZN29QHttpNetworkConnectionChannel23detectPipeliningSupportEv
inline void QHttpNetworkConnectionChannel::detectPipeliningSupport()
{
    Q_ASSERT(reply);
    // detect HTTP Pipelining support
    QByteArray serverHeaderField;
    if (
            // check for HTTP/1.1
            (reply->majorVersion() == 1 && reply->minorVersion() == 1)
            // check for not having connection close
            && (!reply->d_func()->isConnectionCloseEnabled())
            // check if it is still connected
            && (QSocketAbstraction::socketState(socket) == QAbstractSocket::ConnectedState)
            // check for broken servers in server reply header
            // this is adapted from http://mxr.mozilla.org/firefox/ident?i=SupportsPipelining
            && (serverHeaderField = reply->headerField("Server"), !serverHeaderField.contains("Microsoft-IIS/4."))
            && (!serverHeaderField.contains("Microsoft-IIS/5."))
            && (!serverHeaderField.contains("Netscape-Enterprise/3."))
            // this is adpoted from the knowledge of the Nokia 7.x browser team (DEF143319)
            && (!serverHeaderField.contains("WebLogic"))
            && (!serverHeaderField.startsWith("Rocket")) // a Python Web Server, see Web2py.com
            ) {
        pipeliningSupported = QHttpNetworkConnectionChannel::PipeliningProbablySupported;
    } else {
        pipeliningSupported = QHttpNetworkConnectionChannel::PipeliningSupportUnknown;
    }
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1494, as _ZN29QHttpNetworkConnectionChannel13setConnectionEP22QHttpNetworkConnection
inline void QHttpNetworkConnectionChannel::setConnection(QHttpNetworkConnection *c)
{
    // Inlining this function in the header leads to compiler error on
    // release-armv5, on at least timebox 9.2 and 10.1.
    connection = c;
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 719, as _ZN29QHttpNetworkConnectionChannel8setProxyERK13QNetworkProxy
#if !defined(QT_NO_NETWORKPROXY)
inline void QHttpNetworkConnectionChannel::setProxy(const QNetworkProxy &networkProxy)
{
    if (auto *s = qobject_cast<QAbstractSocket *>(socket))
        s->setProxy(networkProxy);

    proxy = networkProxy;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 250, as _ZN29QHttpNetworkConnectionChannel18sendRequestDelayedEv
inline void QHttpNetworkConnectionChannel::sendRequestDelayed()
{
    QMetaObject::invokeMethod(this, [this] {
        if (reply)
            sendRequest();
    }, Qt::ConnectionType::QueuedConnection);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1404, as _ZN29QHttpNetworkConnectionChannel27checkAndResumeCommunicationEv
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::checkAndResumeCommunication()
{
    Q_ASSERT(connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2
             || connection->connectionType() == QHttpNetworkConnection::ConnectionTypeHTTP2Direct);

    // Because HTTP/2 requires that we send a SETTINGS frame as the first thing we do, and respond
    // to a SETTINGS frame with an ACK, we need to delay any handling until we can ensure that any
    // effects from emitting encrypted() have been processed.
    // This function is called after encrypted() was emitted, so check for changes.

    if (!reply && h2RequestsToSend.isEmpty())
        abort();
    waitingForPotentialAbort = false;
    if (needInvokeReadyRead)
        _q_readyRead();
    if (needInvokeReceiveReply)
        _q_receiveReply();
    if (needInvokeSendRequest)
        sendRequest();
}
#endif  // !defined(QT_NO_SSL)

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 823, as _ZNK29QHttpNetworkConnectionChannel12isSocketBusyEv
inline bool QHttpNetworkConnectionChannel::isSocketBusy() const
{
    return (state & QHttpNetworkConnectionChannel::BusyState);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 828, as _ZNK29QHttpNetworkConnectionChannel15isSocketWritingEv
inline bool QHttpNetworkConnectionChannel::isSocketWriting() const
{
    return (state & QHttpNetworkConnectionChannel::WritingState);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 833, as _ZNK29QHttpNetworkConnectionChannel15isSocketWaitingEv
inline bool QHttpNetworkConnectionChannel::isSocketWaiting() const
{
    return (state & QHttpNetworkConnectionChannel::WaitingState);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 838, as _ZNK29QHttpNetworkConnectionChannel15isSocketReadingEv
inline bool QHttpNetworkConnectionChannel::isSocketReading() const
{
    return (state & QHttpNetworkConnectionChannel::ReadingState);
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 258, as _ZN29QHttpNetworkConnectionChannel15_q_receiveReplyEv
inline void QHttpNetworkConnectionChannel::_q_receiveReply()
{
    Q_ASSERT(protocolHandler);
    if (waitingForPotentialAbort) {
        needInvokeReceiveReply = true;
        return;
    }
    protocolHandler->_q_receiveReply();
}

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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1271, as _ZN29QHttpNetworkConnectionChannel22_q_uploadDataReadyReadEv
inline void QHttpNetworkConnectionChannel::_q_uploadDataReadyRead()
{
    if (reply)
        sendRequest();
}

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1483, as _ZN29QHttpNetworkConnectionChannel24_q_encryptedBytesWrittenEx
#if !defined(QT_NO_SSL)
inline void QHttpNetworkConnectionChannel::_q_encryptedBytesWritten(qint64 bytes)
{
    Q_UNUSED(bytes);
    // bytes have been written to the socket. write even more of them :)
    if (isSocketWriting())
        sendRequest();
    // otherwise we do nothing
}
#endif  // !defined(QT_NO_SSL)
//  -----------------------------------------------------------------------

//  QHttp2ProtocolHandler *QHttpNetworkConnectionChannel::h2ProtocolHandler()
//      const
extern "C" Q_DECL_EXPORT
QHttp2ProtocolHandler *ritual_ZNK29QHttpNetworkConnectionChannel17h2ProtocolHandlerEv(
    const QHttpNetworkConnectionChannel *self) {
  return self->h2ProtocolHandler();
}

//  bool QHttpNetworkConnectionChannel::isPendingReconnect() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QHttpNetworkConnectionChannel18isPendingReconnectEv(
    const QHttpNetworkConnectionChannel *self) {
  return self->isPendingReconnect();
}

//  bool QHttpNetworkConnectionChannel::clearPendingReconnect()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QHttpNetworkConnectionChannel21clearPendingReconnectEv(
    QHttpNetworkConnectionChannel *self) {
  return self->clearPendingReconnect();
}

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnectionChannel::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel15ignoreSslErrorsEv(
    QHttpNetworkConnectionChannel *self) {
  self->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnectionChannel::ignoreSslErrors(const
//      QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel15ignoreSslErrorsERK5QListI9QSslErrorE(
    QHttpNetworkConnectionChannel *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnectionChannel::setSslConfiguration(const
//      QSslConfiguration &config)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel19setSslConfigurationERK17QSslConfiguration(
    QHttpNetworkConnectionChannel *self,
    const QSslConfiguration *config) {
  self->setSslConfiguration(*config);
}
#endif  // !defined(QT_NO_SSL)

//  void QHttpNetworkConnectionChannel::pipelineFlush()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel13pipelineFlushEv(
    QHttpNetworkConnectionChannel *self) {
  self->pipelineFlush();
}

//  void QHttpNetworkConnectionChannel::detectPipeliningSupport()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel23detectPipeliningSupportEv(
    QHttpNetworkConnectionChannel *self) {
  self->detectPipeliningSupport();
}

//  void QHttpNetworkConnectionChannel::setConnection(QHttpNetworkConnection
//      *c)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel13setConnectionEP22QHttpNetworkConnection(
    QHttpNetworkConnectionChannel *self,
    QHttpNetworkConnection *c) {
  self->setConnection(c);
}

#if !defined(QT_NO_NETWORKPROXY)
//  void QHttpNetworkConnectionChannel::setProxy(const QNetworkProxy
//      &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel8setProxyERK13QNetworkProxy(
    QHttpNetworkConnectionChannel *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QHttpNetworkConnectionChannel::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel5closeEv(
    QHttpNetworkConnectionChannel *self) {
  self->close();
}

//  void QHttpNetworkConnectionChannel::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel5abortEv(
    QHttpNetworkConnectionChannel *self) {
  self->abort();
}

//  void QHttpNetworkConnectionChannel::sendRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel11sendRequestEv(
    QHttpNetworkConnectionChannel *self) {
  self->sendRequest();
}

//  void QHttpNetworkConnectionChannel::sendRequestDelayed()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel18sendRequestDelayedEv(
    QHttpNetworkConnectionChannel *self) {
  self->sendRequestDelayed();
}

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnectionChannel::checkAndResumeCommunication()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel27checkAndResumeCommunicationEv(
    QHttpNetworkConnectionChannel *self) {
  self->checkAndResumeCommunication();
}
#endif  // !defined(QT_NO_SSL)

//  bool QHttpNetworkConnectionChannel::isSocketBusy() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QHttpNetworkConnectionChannel12isSocketBusyEv(
    const QHttpNetworkConnectionChannel *self) {
  return self->isSocketBusy();
}

//  bool QHttpNetworkConnectionChannel::isSocketWriting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QHttpNetworkConnectionChannel15isSocketWritingEv(
    const QHttpNetworkConnectionChannel *self) {
  return self->isSocketWriting();
}

//  bool QHttpNetworkConnectionChannel::isSocketWaiting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QHttpNetworkConnectionChannel15isSocketWaitingEv(
    const QHttpNetworkConnectionChannel *self) {
  return self->isSocketWaiting();
}

//  bool QHttpNetworkConnectionChannel::isSocketReading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK29QHttpNetworkConnectionChannel15isSocketReadingEv(
    const QHttpNetworkConnectionChannel *self) {
  return self->isSocketReading();
}

//  void QHttpNetworkConnectionChannel::_q_receiveReply()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel15_q_receiveReplyEv(
    QHttpNetworkConnectionChannel *self) {
  self->_q_receiveReply();
}

//  void QHttpNetworkConnectionChannel::_q_bytesWritten(qint64 bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel15_q_bytesWrittenEx(
    QHttpNetworkConnectionChannel *self,
    qint64 bytes) {
  self->_q_bytesWritten(bytes);
}

//  void QHttpNetworkConnectionChannel::_q_readyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel12_q_readyReadEv(
    QHttpNetworkConnectionChannel *self) {
  self->_q_readyRead();
}

//  void QHttpNetworkConnectionChannel::_q_uploadDataReadyRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel22_q_uploadDataReadyReadEv(
    QHttpNetworkConnectionChannel *self) {
  self->_q_uploadDataReadyRead();
}

#if !defined(QT_NO_SSL)
//  void QHttpNetworkConnectionChannel::_q_encryptedBytesWritten(qint64
//      bytes)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QHttpNetworkConnectionChannel24_q_encryptedBytesWrittenEx(
    QHttpNetworkConnectionChannel *self,
    qint64 bytes) {
  self->_q_encryptedBytesWritten(bytes);
}
#endif  // !defined(QT_NO_SSL)

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
