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
#include <QtNetwork/private/qhttpnetworkheader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/access/qhttpnetworkconnectionchannel.cpp, line 35, as local:qhttpnetworkconnectionchannel.cpp:reconnectAttemptsDefault
static const int reconnectAttemptsDefault = 3;

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

//  from src/network/access/qhttpnetworkreply.cpp, line 513, as _ZN24QHttpNetworkReplyPrivate24isConnectionCloseEnabledEv
inline bool QHttpNetworkReplyPrivate::isConnectionCloseEnabled()
{
    return connectionCloseEnabled || forceConnectionCloseEnabled;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 178, as _ZN19QHttpNetworkRequestC1ERK4QUrlNS_9OperationENS_8PriorityE
inline QHttpNetworkRequest::QHttpNetworkRequest(const QUrl &url, Operation operation, Priority priority)
    : d(new QHttpNetworkRequestPrivate(operation, priority, url))
{
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

//  from src/network/access/qhttpnetworkreply.cpp, line 759, as _ZN24QHttpNetworkReplyPrivate9eraseDataEv
inline void QHttpNetworkReplyPrivate::eraseData()
{
    responseData.clear();
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

//  from src/network/access/qabstractprotocolhandler.cpp, line 22, as _ZN24QAbstractProtocolHandler8setReplyEP17QHttpNetworkReply
inline void QAbstractProtocolHandler::setReply(QHttpNetworkReply *reply)
{
    m_reply = reply;
}

//  from src/network/access/qhttpnetworkrequest.cpp, line 411, as _ZNK19QHttpNetworkRequest18methodIsIdempotentEv
inline bool QHttpNetworkRequest::methodIsIdempotent() const
{
    using Op = Operation;
    constexpr auto knownSafe = std::array{ Op::Get, Op::Head, Op::Put, Op::Trace, Op::Options };
    return std::any_of(knownSafe.begin(), knownSafe.end(),
                       [currentOp = d->operation](auto op) { return op == currentOp; });
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

//  from src/network/access/qhttpnetworkrequest.cpp, line 311, as _ZNK19QHttpNetworkRequest8priorityEv
inline QHttpNetworkRequest::Priority QHttpNetworkRequest::priority() const
{
    return d->priority;
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

//  from src/network/access/qhttpnetworkconnection.cpp, line 156, as _ZNK29QHttpNetworkConnectionPrivate7indexOfEP9QIODevice
inline int QHttpNetworkConnectionPrivate::indexOf(QIODevice *socket) const
{
    for (int i = 0; i < activeChannelCount; ++i)
        if (channels[i].socket == socket)
            return i;

    qFatal("Called with unknown socket object.");
    return 0;
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

#endif  // QT_CONFIG(http)
#endif  // QT_CONFIG(http)
