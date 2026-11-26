//  Written by dev_tooling.RitualGenerator from the records of QtHttpServer/6
//  .12.0/QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhttpheaders.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/private/qhttpserverstream_p.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
#include <QtNetwork/qtcpsocket.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslsocket.h>
#endif
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalsocket.h>
#endif
#include <QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qthread.h>
#include <QtCore/qpointer.h>
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/qhttpserverresponse.h>
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalsocket.h>
#endif
#include <QtNetwork/qtcpsocket.h>
#include <QtHttpServer/private/qabstracthttpserver_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtCore/qbytearray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 28, as local:qhttpserverhttp1protocolhandler.cpp:statusString
Q_STATIC_LOGGING_CATEGORY(lcHttpServerHttp1Handler, "qt.httpserver.http1handler")

// https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
static const std::map<QHttpServerResponder::StatusCode, QByteArray> statusString{
#define XX(name, string) { QHttpServerResponder::StatusCode::name, QByteArrayLiteral(string) }
    XX(Continue, "Continue"),
    XX(SwitchingProtocols, "Switching Protocols"),
    XX(Processing, "Processing"),
    XX(Ok, "OK"),
    XX(Created, "Created"),
    XX(Accepted, "Accepted"),
    XX(NonAuthoritativeInformation, "Non-Authoritative Information"),
    XX(NoContent, "No Content"),
    XX(ResetContent, "Reset Content"),
    XX(PartialContent, "Partial Content"),
    XX(MultiStatus, "Multi-Status"),
    XX(AlreadyReported, "Already Reported"),
    XX(IMUsed, "I'm Used"),
    XX(MultipleChoices, "Multiple Choices"),
    XX(MovedPermanently, "Moved Permanently"),
    XX(Found, "Found"),
    XX(SeeOther, "See Other"),
    XX(NotModified, "Not Modified"),
    XX(UseProxy, "Use Proxy"),
    XX(TemporaryRedirect, "Temporary Redirect"),
    XX(PermanentRedirect, "Permanent Redirect"),
    XX(BadRequest, "Bad Request"),
    XX(Unauthorized, "Unauthorized"),
    XX(PaymentRequired, "Payment Required"),
    XX(Forbidden, "Forbidden"),
    XX(NotFound, "Not Found"),
    XX(MethodNotAllowed, "Method Not Allowed"),
    XX(NotAcceptable, "Not Acceptable"),
    XX(ProxyAuthenticationRequired, "Proxy Authentication Required"),
    XX(RequestTimeout, "Request Timeout"),
    XX(Conflict, "Conflict"),
    XX(Gone, "Gone"),
    XX(LengthRequired, "Length Required"),
    XX(PreconditionFailed, "Precondition Failed"),
    XX(PayloadTooLarge, "Request Entity Too Large"),
    XX(UriTooLong, "Request-URI Too Long"),
    XX(UnsupportedMediaType, "Unsupported Media Type"),
    XX(RequestRangeNotSatisfiable, "Requested Range Not Satisfiable"),
    XX(ExpectationFailed, "Expectation Failed"),
    XX(ImATeapot, "I'm a teapot"),
    XX(MisdirectedRequest, "Misdirected Request"),
    XX(UnprocessableEntity, "Unprocessable Entity"),
    XX(Locked, "Locked"),
    XX(FailedDependency, "Failed Dependency"),
    XX(UpgradeRequired, "Upgrade Required"),
    XX(PreconditionRequired, "Precondition Required"),
    XX(TooManyRequests, "Too Many Requests"),
    XX(RequestHeaderFieldsTooLarge, "Request Header Fields Too Large"),
    XX(UnavailableForLegalReasons, "Unavailable For Legal Reasons"),
    XX(InternalServerError, "Internal Server Error"),
    XX(NotImplemented, "Not Implemented"),
    XX(BadGateway, "Bad Gateway"),
    XX(ServiceUnavailable, "Service Unavailable"),
    XX(GatewayTimeout, "Gateway Timeout"),
    XX(HttpVersionNotSupported, "HTTP Version Not Supported"),
    XX(VariantAlsoNegotiates, "Variant Also Negotiates"),
    XX(InsufficientStorage, "Insufficient Storage"),
    XX(LoopDetected, "Loop Detected"),
    XX(NotExtended, "Not Extended"),
    XX(NetworkAuthenticationRequired, "Network Authentication Required"),
    XX(NetworkConnectTimeoutError, "Network Connect Timeout Error"),
#undef XX
};

//  from ../qthttpserver/src/httpserver/qhttpserverstream.cpp, line 65, as _ZN17QHttpServerStream19disconnectResponderEj
inline void QHttpServerStream::disconnectResponder(quint32 streamId)
{
    auto connection = responderConnections.take(streamId);
    if (connection)
        disconnect(connection);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 344, as _ZN31QHttpServerHttp1ProtocolHandler15handleReadyReadEv
inline void QHttpServerHttp1ProtocolHandler::handleReadyRead()
{
    if (handlingRequest || state != TransferState::Ready)
        return;

    lastActiveTimer.restart();

    if (!socket->isTransactionStarted())
        socket->startTransaction();

    auto requestReceived = parser.parse(socket);
    if (!requestReceived) {
        if (tcpSocket)
            tcpSocket->disconnectFromHost();
#if QT_CONFIG(localserver)
        else if (localSocket)
            localSocket->disconnectFromServer();
#endif
        return;
    }

#if QT_CONFIG(ssl)
    auto request = QHttpServerRequest::create(parser, sslConfiguration);
#else
    auto request = QHttpServerRequest::create(parser);
#endif

    if (parser.state != QHttpServerParser::State::AllDone)
        return; // Partial read

    qCDebug(lcHttpServerHttp1Handler) << "Request:" << request;
    useHttp1_1 = request.d->minorVersion == 1;
    auto connectionHeader =
            QByteArray(request.headers().value(QHttpHeaders::WellKnownHeader::Connection,
                                               useHttp1_1 ? "keep-alive" : "close")).toLower();
    keepAlive = connectionHeader.contains("keep-alive");

    QHttpServerResponder responder(this);
    connectResponder(responder.d_ptr);

#if defined(QT_WEBSOCKETS_LIB)
    if (auto *tcpSocket = qobject_cast<QTcpSocket*>(socket)) {
        if (parser.upgrade) { // Upgrade
            const auto &upgradeValue = request.value(QByteArrayLiteral("upgrade"));
            if (upgradeValue.compare(QByteArrayLiteral("websocket"), Qt::CaseInsensitive) == 0) {
                const auto upgradeResponse = server->verifyWebSocketUpgrade(request);
                static const auto signal =
                        QMetaMethod::fromSignal(&QAbstractHttpServer::newWebSocketConnection);
                if (server->isSignalConnected(signal)
                    && upgradeResponse.type()
                            != QHttpServerWebSocketUpgradeResponse::ResponseType::PassToNext) {
                    if (upgradeResponse.type()
                        == QHttpServerWebSocketUpgradeResponse::ResponseType::Accept) {
                        // Socket will now be managed by websocketServer
                        protocolChanged = true;
                        socket->disconnect();
                        socket->rollbackTransaction();
                        socket->setParent(nullptr);
                        server->d_func()->websocketServer.handleConnection(tcpSocket);
                        Q_EMIT socket->readyRead();
                    } else {
                        qCDebug(lcHttpServerHttp1Handler, "WebSocket upgrade denied: %ls",
                                qUtf16Printable(QLatin1StringView(upgradeResponse.denyMessage())));
                        QByteArray buffer;
                        buffer.append("HTTP/1.1 ");
                        buffer.append(QByteArray::number(quint32(upgradeResponse.denyStatus())));
                        buffer.append(" ");
                        buffer.append(upgradeResponse.denyMessage());
                        buffer.append("\r\n\r\n");
                        tcpSocket->write(buffer);
                    }
                } else {
                    if (!server->isSignalConnected(signal)) {
                        qCWarning(lcHttpServerHttp1Handler,
                                  "WebSocket received but no slots connected to "
                                  "QWebSocketServer::newConnection");
                    }
                    server->missingHandler(request, responder);
                    tcpSocket->disconnectFromHost();
                }
                return;
            }
        }
    }
#endif // QT_WEBSOCKETS_LIB

    socket->commitTransaction();

    QHostAddress peerAddress = tcpSocket ? tcpSocket->peerAddress()
                                         : QHostAddress::LocalHost;
    if (!m_filter->isRequestAllowed(peerAddress)) {
        responder.sendResponse(
                QHttpServerResponse(QHttpServerResponder::StatusCode::Forbidden));
    }
    if (!m_filter->isRequestWithinRate(peerAddress)) {
        responder.sendResponse(
                QHttpServerResponse(QHttpServerResponder::StatusCode::TooManyRequests));
    } else if (!server->handleRequest(request, responder)) {
        server->missingHandler(request, responder);
    }

    if (handlingRequest || state != TransferState::Ready)
        disconnect(socket, &QIODevice::readyRead, this, &QHttpServerHttp1ProtocolHandler::handleReadyRead);
    else if (socket->bytesAvailable() > 0)
        QMetaObject::invokeMethod(socket, &QIODevice::readyRead, Qt::QueuedConnection);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 584, as _ZN31QHttpServerHttp1ProtocolHandler21writeStatusAndHeadersEN20QHttpServerResponder10StatusCodeERK12QHttpHeaders
inline void QHttpServerHttp1ProtocolHandler::writeStatusAndHeaders(QHttpServerResponder::StatusCode status,
                                                        const QHttpHeaders &headers)
{
    Q_ASSERT(state == TransferState::Ready);
    QByteArray payload;
    payload.append(useHttp1_1 ? "HTTP/1.1 " : "HTTP/1.0 ");
    payload.append(QByteArray::number(quint32(status)));
    const auto it = statusString.find(status);
    if (it != statusString.end()) {
        payload.append(" ");
        payload.append(statusString.at(status));
    }
    payload.append("\r\n");

    for (qsizetype i = 0; i < headers.size(); ++i) {
        const auto name = headers.nameAt(i);
        payload.append(QByteArrayView(name.data(), name.size()) + ": "
                       + headers.valueAt(i).toByteArray() + "\r\n");
    }
    payload.append("\r\n");
    write(payload);
    state = TransferState::HeadersSent;
}

//  from ../qthttpserver/src/httpserver/qhttpserverliterals.cpp, line 15, as _ZN19QHttpServerLiterals17contentTypeXEmptyEv
inline QByteArray QHttpServerLiterals::contentTypeXEmpty()
{
    static QByteArray ba("application/x-empty");
    return ba;
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 333, as _ZN31QHttpServerHttp1ProtocolHandler20startHandlingRequestEv
inline void QHttpServerHttp1ProtocolHandler::startHandlingRequest()
{
    handlingRequest = true;
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 338, as _ZN31QHttpServerHttp1ProtocolHandler18socketDisconnectedEv
inline void QHttpServerHttp1ProtocolHandler::socketDisconnected()
{
    if (!handlingRequest)
        deleteLater();
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 451, as _ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj
inline void QHttpServerHttp1ProtocolHandler::write(const QByteArray &body, const QHttpHeaders &headers,
                                        QHttpServerResponder::StatusCode status, quint32 streamId)
{
    Q_UNUSED(streamId);
    Q_ASSERT(state == TransferState::Ready);
    QHttpHeaders allHeaders(headers);
    addConnectionAndKeepAliveHeaders(allHeaders);
    writeStatusAndHeaders(status, allHeaders);
    write(body);
    state = TransferState::Ready;
    if (!keepAlive)
        closeConnection();
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 465, as _ZN31QHttpServerHttp1ProtocolHandler5writeEN20QHttpServerResponder10StatusCodeEj
inline void QHttpServerHttp1ProtocolHandler::write(QHttpServerResponder::StatusCode status, quint32 streamId)
{
    Q_UNUSED(streamId);
    Q_ASSERT(state == TransferState::Ready);
    QHttpHeaders headers;
    headers.append(QHttpHeaders::WellKnownHeader::ContentType,
                   QHttpServerLiterals::contentTypeXEmpty());
    headers.append(QHttpHeaders::WellKnownHeader::ContentLength, "0");
    addConnectionAndKeepAliveHeaders(headers);
    writeStatusAndHeaders(status, headers);
    state = TransferState::Ready;
    if (!keepAlive)
        closeConnection();
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 523, as _ZN31QHttpServerHttp1ProtocolHandler17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj
inline void QHttpServerHttp1ProtocolHandler::writeBeginChunked(const QHttpHeaders &headers,
                                                    QHttpServerResponder::StatusCode status,
                                                    quint32 streamId)
{
    Q_UNUSED(streamId);
    Q_ASSERT(state == TransferState::Ready);
    QHttpHeaders allHeaders(headers);
    if (useHttp1_1)
        allHeaders.append(QHttpHeaders::WellKnownHeader::TransferEncoding, "chunked");
    else
        keepAlive = false;

    addConnectionAndKeepAliveHeaders(allHeaders);
    writeStatusAndHeaders(status, allHeaders);
    state = TransferState::ChunkedTransferBegun;
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 608, as _ZN31QHttpServerHttp1ProtocolHandler11writeHeaderERK10QByteArrayS2_
inline void QHttpServerHttp1ProtocolHandler::writeHeader(const QByteArray &key, const QByteArray &value)
{
    write(key + ": " + value + "\r\n");
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 613, as _ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArray
inline void QHttpServerHttp1ProtocolHandler::write(const QByteArray &ba)
{
    Q_ASSERT(QThread::currentThread() == thread());
    socket->write(ba);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 619, as _ZN31QHttpServerHttp1ProtocolHandler5writeEPKcx
inline void QHttpServerHttp1ProtocolHandler::write(const char *body, qint64 size)
{
    Q_ASSERT(QThread::currentThread() == thread());
    socket->write(body, size);
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 636, as _ZN31QHttpServerHttp1ProtocolHandler32addConnectionAndKeepAliveHeadersER12QHttpHeaders
inline void QHttpServerHttp1ProtocolHandler::addConnectionAndKeepAliveHeaders(QHttpHeaders &headers)
{
    if (keepAlive) {
        headers.append(QHttpHeaders::WellKnownHeader::Connection, "keep-alive");
        headers.append(QHttpHeaders::WellKnownHeader::KeepAlive,
                       u"timeout=%1"_s.arg(m_configuration->keepAliveTimeout().count()));
    } else {
        headers.append(QHttpHeaders::WellKnownHeader::Connection, "close");
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 647, as _ZN31QHttpServerHttp1ProtocolHandler21checkKeepAliveTimeoutEv
inline void QHttpServerHttp1ProtocolHandler::checkKeepAliveTimeout()
{
    if (handlingRequest || state != TransferState::Ready)
        return;

    if (lastActiveTimer.durationElapsed() > server->configuration().keepAliveTimeout()) {
        if (tcpSocket)
            tcpSocket->abort();
#if QT_CONFIG(localserver)
        else if (localSocket)
            localSocket->abort();
#endif
    }
}

//  from ../qthttpserver/src/httpserver/qhttpserverhttp1protocolhandler.cpp, line 662, as _ZN31QHttpServerHttp1ProtocolHandler15closeConnectionEv
inline void QHttpServerHttp1ProtocolHandler::closeConnection()
{
    if (tcpSocket) {
        QMetaObject::invokeMethod(tcpSocket, &QTcpSocket::disconnectFromHost, Qt::QueuedConnection);
#if QT_CONFIG(localserver)
    } else if (localSocket) {
        QMetaObject::invokeMethod(localSocket, &QLocalSocket::disconnectFromServer,
                                  Qt::QueuedConnection);
#endif
    }
}
//  -----------------------------------------------------------------------

//  const QMetaObject *QHttpServerHttp1ProtocolHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QHttpServerHttp1ProtocolHandler10metaObjectEv(
    const QHttpServerHttp1ProtocolHandler *self) {
  return self->metaObject();
}

//  void *QHttpServerHttp1ProtocolHandler::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN31QHttpServerHttp1ProtocolHandler11qt_metacastEPKc(
    QHttpServerHttp1ProtocolHandler *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHttpServerHttp1ProtocolHandler::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN31QHttpServerHttp1ProtocolHandler11qt_metacallEN11QMetaObject4CallEiPPv(
    QHttpServerHttp1ProtocolHandler *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QHttpServerHttp1ProtocolHandler::startHandlingRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler20startHandlingRequestEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->startHandlingRequest();
}

//  void QHttpServerHttp1ProtocolHandler::socketDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler18socketDisconnectedEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->socketDisconnected();
}

//  void QHttpServerHttp1ProtocolHandler::write(const QByteArray &body, const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
//      quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArrayRK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerHttp1ProtocolHandler *self,
    const QByteArray *body,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(*body, *headers, status, streamId);
}

//  void
//      QHttpServerHttp1ProtocolHandler::write(QHttpServerResponder::StatusCo
//      de status, quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler5writeEN20QHttpServerResponder10StatusCodeEj(
    QHttpServerHttp1ProtocolHandler *self,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->write(status, streamId);
}

//  void QHttpServerHttp1ProtocolHandler::writeBeginChunked(const
//      QHttpHeaders &headers, QHttpServerResponder::StatusCode status,
//      quint32 streamId)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler17writeBeginChunkedERK12QHttpHeadersN20QHttpServerResponder10StatusCodeEj(
    QHttpServerHttp1ProtocolHandler *self,
    const QHttpHeaders *headers,
    QHttpServerResponder::StatusCode status,
    quint32 streamId) {
  self->writeBeginChunked(*headers, status, streamId);
}

//  void QHttpServerHttp1ProtocolHandler::writeHeader(const QByteArray &key,
//      const QByteArray &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler11writeHeaderERK10QByteArrayS2_(
    QHttpServerHttp1ProtocolHandler *self,
    const QByteArray *key,
    const QByteArray *value) {
  self->writeHeader(*key, *value);
}

//  void QHttpServerHttp1ProtocolHandler::write(const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler5writeERK10QByteArray(
    QHttpServerHttp1ProtocolHandler *self,
    const QByteArray *data) {
  self->write(*data);
}

//  void QHttpServerHttp1ProtocolHandler::write(const char *body, qint64
//      size)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler5writeEPKcx(
    QHttpServerHttp1ProtocolHandler *self,
    const char *body,
    qint64 size) {
  self->write(body, size);
}

//  void QHttpServerHttp1ProtocolHandler::addConnectionAndKeepAliveHeaders(QH
//      ttpHeaders &headers)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler32addConnectionAndKeepAliveHeadersER12QHttpHeaders(
    QHttpServerHttp1ProtocolHandler *self,
    QHttpHeaders *headers) {
  self->addConnectionAndKeepAliveHeaders(*headers);
}

//  void QHttpServerHttp1ProtocolHandler::checkKeepAliveTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler21checkKeepAliveTimeoutEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->checkKeepAliveTimeout();
}

//  void QHttpServerHttp1ProtocolHandler::closeConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QHttpServerHttp1ProtocolHandler15closeConnectionEv(
    QHttpServerHttp1ProtocolHandler *self) {
  self->closeConnection();
}
