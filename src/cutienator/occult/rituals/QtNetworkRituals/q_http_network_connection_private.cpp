//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpnetworkconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qhttpnetworkconnectionchannel_p.h"
#include "qhttpnetworkconnection_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#include <qdebug.h>
#include <private/qhttp2protocolhandler_p.h>
#include <private/qhttpprotocolhandler_p.h>
#include <private/http2protocol_p.h>
#include <private/qsocketabstraction_p.h>
#ifndef QT_NO_SSL
#    include <private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#endif
#include <QtNetwork/private/qtnetworkglobal_p.h>
#include <memory>
#include <utility>
#include "qhttpnetworkrequest_p.h"
#include "private/qnoncontiguousbytedevice_p.h"
#include <QtCore/private/qtools_p.h>
#include "qhttpnetworkconnection_p.h"
#include <private/qabstractsocket_p.h>
#include "qhttpnetworkconnectionchannel_p.h"
#include <private/qhttp2protocolhandler_p.h>
#include "private/qnoncontiguousbytedevice_p.h"
#include <private/qnetworkrequest_p.h>
#include <private/qobject_p.h>
#include <private/qauthenticator_p.h>
#include "private/qhostinfo_p.h"
#include <qnetworkproxy.h>
#include <qauthenticator.h>
#include <qcoreapplication.h>
#include <private/qdecompresshelper_p.h>
#include <private/qsocketabstraction_p.h>
#include <qbuffer.h>
#include <qdebug.h>
#include <qspan.h>
#include <qvarlengtharray.h>
#ifndef QT_NO_SSL
#    include <private/qsslsocket_p.h>
#    include <QtNetwork/qsslkey.h>
#    include <QtNetwork/qsslcipher.h>
#    include <QtNetwork/qsslconfiguration.h>
#    include <QtNetwork/qsslerror.h>
#endif
#include "qhttpnetworkheader_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 1494, as _ZN29QHttpNetworkConnectionChannel13setConnectionEP22QHttpNetworkConnection
inline void QHttpNetworkConnectionChannel::setConnection(QHttpNetworkConnection *c)
{
    // Inlining this function in the header leads to compiler error on
    // release-armv5, on at least timebox 9.2 and 10.1.
    connection = c;
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 311, as _ZNK19QHttpNetworkRequest8priorityEv
inline QHttpNetworkRequest::Priority QHttpNetworkRequest::priority() const
{
    return d->priority;
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

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 823, as _ZNK29QHttpNetworkConnectionChannel12isSocketBusyEv
inline bool QHttpNetworkConnectionChannel::isSocketBusy() const
{
    return (state & QHttpNetworkConnectionChannel::BusyState);
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

//  from src/network/access/qhttpnetworkconnection.cpp, line 770, as _ZNK29QHttpNetworkConnectionPrivate24predictNextRequestsReplyEv
inline QHttpNetworkReply* QHttpNetworkConnectionPrivate::predictNextRequestsReply() const
{
    if (!highPriorityQueue.isEmpty())
        return highPriorityQueue.last().second;
    if (!lowPriorityQueue.isEmpty())
        return lowPriorityQueue.last().second;
    return nullptr;
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

//  QHttpNetworkReply
//      *QHttpNetworkConnectionPrivate::predictNextRequestsReply() const
extern "C" Q_DECL_EXPORT
QHttpNetworkReply *ritual_ZNK29QHttpNetworkConnectionPrivate24predictNextRequestsReplyEv(
    const QHttpNetworkConnectionPrivate *self) {
  return self->predictNextRequestsReply();
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
