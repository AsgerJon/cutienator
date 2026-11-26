//  Written by dev_tooling.RitualGenerator from the records of QtNetworkAuth/
//  6.12.0/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qloggingcategory.h>
#include <QtNetworkAuth/qabstractoauth.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtNetworkAuth/private/qabstractoauthreplyhandler_p.h>
#include <QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h>
#include <QtCore/qurl.h>
#include <QtCore/qurlquery.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/private/qlocale_p.h>
#ifndef QT_NO_SSL
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qsslserver.h>
#include <QtNetwork/qsslsocket.h>
#endif
#include <QtNetwork/qtcpsocket.h>
#include <QtNetwork/qnetworkreply.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtnetworkauth/src/oauth/qabstractoauthreplyhandler.cpp, line 9, as _Z14lcReplyHandlerv
inline const QLoggingCategory &lcReplyHandler()
{
    static const QLoggingCategory category("qt.networkauth.replyhandler");
    return category;
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 378, as _ZN35QOAuthHttpServerReplyHandlerPrivate12QHttpRequest10readHeaderEP10QTcpSocket
inline bool QOAuthHttpServerReplyHandlerPrivate::QHttpRequest::readHeader(QTcpSocket *socket)
{
    while (socket->bytesAvailable()) {
        char c;
        socket->getChar(&c);
        fragment += c;
        if (fragment.endsWith("\r\n")) {
            if (fragment == "\r\n") {
                state = State::ReadingBody;
                fragment.clear();
                return true;
            } else {
                fragment.chop(2);
                const int index = fragment.indexOf(':');
                if (index == -1)
                    return false;

                const QByteArray key = fragment.mid(0, index).trimmed();
                const QByteArray value = fragment.mid(index + 1).trimmed();
                headers.insert(key, value);
                fragment.clear();
            }
        }
    }
    return false;
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 293, as _ZN35QOAuthHttpServerReplyHandlerPrivate12QHttpRequest10readMethodEP10QTcpSocket
inline bool QOAuthHttpServerReplyHandlerPrivate::QHttpRequest::readMethod(QTcpSocket *socket)
{
    bool finished = false;
    while (socket->bytesAvailable() && !finished) {
        char c;
        socket->getChar(&c);
        if (std::isupper(c) && fragment.size() < 6)
            fragment += c;
        else
            finished = true;
    }
    if (finished) {
        if (fragment == "HEAD")
            method = Method::Head;
        else if (fragment == "GET")
            method = Method::Get;
        else if (fragment == "PUT")
            method = Method::Put;
        else if (fragment == "POST")
            method = Method::Post;
        else if (fragment == "DELETE")
            method = Method::Delete;
        else
            qCWarning(lcReplyHandler, "Invalid operation %s", fragment.data());

        state = State::ReadingUrl;
        fragment.clear();

        return method != Method::Unknown;
    }
    return true;
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 352, as _ZN35QOAuthHttpServerReplyHandlerPrivate12QHttpRequest10readStatusEP10QTcpSocket
inline bool QOAuthHttpServerReplyHandlerPrivate::QHttpRequest::readStatus(QTcpSocket *socket)
{
    bool finished = false;
    while (socket->bytesAvailable() && !finished) {
        char c;
        socket->getChar(&c);
        fragment += c;
        if (fragment.endsWith("\r\n")) {
            finished = true;
            fragment.resize(fragment.size() - 2);
        }
    }
    if (finished) {
        if (!std::isdigit(fragment.at(fragment.size() - 3)) ||
                !std::isdigit(fragment.at(fragment.size() - 1))) {
            qCWarning(lcReplyHandler, "Invalid version");
            return false;
        }
        version = std::make_pair(fragment.at(fragment.size() - 3) - '0',
                            fragment.at(fragment.size() - 1) - '0');
        state = State::ReadingHeader;
        fragment.clear();
    }
    return true;
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 326, as _ZN35QOAuthHttpServerReplyHandlerPrivate12QHttpRequest7readUrlEP10QTcpSocket
inline bool QOAuthHttpServerReplyHandlerPrivate::QHttpRequest::readUrl(QTcpSocket *socket)
{
    bool finished = false;
    while (socket->bytesAvailable() && !finished) {
        char c;
        socket->getChar(&c);
        if (ascii_isspace(c))
            finished = true;
        else
            fragment += c;
    }
    if (finished) {
        url = QUrl::fromEncoded(fragment);
        state = State::ReadingStatus;

        if (!fragment.startsWith(u'/') || !url.isValid() || !url.scheme().isNull()
                || !url.host().isNull()) {
            qCWarning(lcReplyHandler, "Invalid request: invalid request-target");
            return false;
        }
        fragment.clear();
        return true;
    }
    return true;
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 133, as _ZN35QOAuthHttpServerReplyHandlerPrivateC1EP28QOAuthHttpServerReplyHandler
inline QOAuthHttpServerReplyHandlerPrivate::QOAuthHttpServerReplyHandlerPrivate(
        QOAuthHttpServerReplyHandler *p) :
    text(QObject::tr("Callback received. Feel free to close this page.")), path(u'/'), q_ptr(p)
{
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 139, as _ZN35QOAuthHttpServerReplyHandlerPrivateD1Ev
inline QOAuthHttpServerReplyHandlerPrivate::~QOAuthHttpServerReplyHandlerPrivate()
{
    if (httpServer->isListening())
        httpServer->close();
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 145, as _ZNK35QOAuthHttpServerReplyHandlerPrivate8callbackEv
inline QString QOAuthHttpServerReplyHandlerPrivate::callback() const
{
    QUrl url;
#ifndef QT_NO_SSL
    if (qobject_cast<QSslServer*>(httpServer))
        url.setScheme(u"https"_s);
    else
        url.setScheme(u"http"_s);
#else
    url.setScheme(u"http"_s);
#endif
    url.setPort(callbackPort);
    url.setPath(path);
    url.setHost(callbackHost());
    return url.toString(QUrl::EncodeSpaces | QUrl::EncodeUnicode | QUrl::EncodeDelimiters
                            | QUrl::EncodeReserved);
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 163, as _ZNK35QOAuthHttpServerReplyHandlerPrivate12callbackHostEv
inline QString QOAuthHttpServerReplyHandlerPrivate::callbackHost() const
{
    QString host;
    if (!callbackHostname.isEmpty()) {
        // Use application-provided hostname
        host = callbackHostname;
    } else if (callbackAddress == QHostAddress::AnyIPv4 || callbackAddress == QHostAddress::Any
               || callbackAddress == QHostAddress::AnyIPv6) {
        // Convert Any addresses to "localhost"
        host = u"localhost"_s;
    } else {
        // For other than Any addresses, use QHostAddress::toString() which returns an
        // IP literal. This includes user-provided addresses, as well as special addresses
        // such as LocalHost (127.0.0.1) and LocalHostIPv6 (::1)
        host = callbackAddress.toString();
    }
    return host;
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 182, as _ZN35QOAuthHttpServerReplyHandlerPrivate18_q_clientConnectedEv
inline void QOAuthHttpServerReplyHandlerPrivate::_q_clientConnected()
{
    QTcpSocket *socket = httpServer->nextPendingConnection();

    QObject::connect(socket, &QTcpSocket::disconnected, socket, &QTcpSocket::deleteLater);
    QObject::connect(socket, &QTcpSocket::readyRead, q_ptr,
                     [this, socket]() { _q_readData(socket); });
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 191, as _ZN35QOAuthHttpServerReplyHandlerPrivate11_q_readDataEP10QTcpSocket
inline void QOAuthHttpServerReplyHandlerPrivate::_q_readData(QTcpSocket *socket)
{
    QHttpRequest *request = nullptr;
    if (auto it = clients.find(socket); it == clients.end()) {
        request = &clients[socket];     // insert it
        request->port = httpServer->serverPort();
    } else {
        request = &*it;
    }

    bool error = false;

    if (Q_LIKELY(request->state == QHttpRequest::State::ReadingMethod))
        if (Q_UNLIKELY(error = !request->readMethod(socket)))
            qCWarning(lcReplyHandler, "Invalid Method");

    if (Q_LIKELY(!error && request->state == QHttpRequest::State::ReadingUrl))
        if (Q_UNLIKELY(error = !request->readUrl(socket)))
            qCWarning(lcReplyHandler, "Invalid URL");

    if (Q_LIKELY(!error && request->state == QHttpRequest::State::ReadingStatus))
        if (Q_UNLIKELY(error = !request->readStatus(socket)))
            qCWarning(lcReplyHandler, "Invalid Status");

    if (Q_LIKELY(!error && request->state == QHttpRequest::State::ReadingHeader))
        if (Q_UNLIKELY(error = !request->readHeader(socket)))
            qCWarning(lcReplyHandler, "Invalid Header");

    if (error) {
        socket->disconnectFromHost();
        clients.remove(socket);
    } else if (!request->url.isEmpty()) {
        Q_ASSERT(request->state != QHttpRequest::State::ReadingUrl);
        _q_answerClient(socket, request->url);
        clients.remove(socket);
    }
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 229, as _ZN35QOAuthHttpServerReplyHandlerPrivate15_q_answerClientEP10QTcpSocketRK4QUrl
inline void QOAuthHttpServerReplyHandlerPrivate::_q_answerClient(QTcpSocket *socket, const QUrl &url)
{
    Q_Q(QOAuthHttpServerReplyHandler);
    if (url.path() != path) {
        qCWarning(lcReplyHandler, "Invalid request: URL path doesn't match");
    } else {
        Q_EMIT q->callbackDataReceived(QUrl(callback()).resolved(url).toEncoded());

        QVariantMap receivedData;
        const QUrlQuery query(url.query());
        const auto items = query.queryItems();
        for (auto it = items.begin(), end = items.end(); it != end; ++it)
            receivedData.insert(it->first, it->second);
        Q_EMIT q->callbackReceived(receivedData);

        const QByteArray html = QByteArrayLiteral("<html><head><title>") +
                qApp->applicationName().toUtf8() +
                QByteArrayLiteral("</title></head><body>") +
                text.toUtf8() +
                QByteArrayLiteral("</body></html>");

        const QByteArray htmlSize = QByteArray::number(html.size());
        const QByteArray replyMessage = QByteArrayLiteral("HTTP/1.0 200 OK \r\n"
                                                          "Content-Type: text/html; "
                                                          "charset=\"utf-8\"\r\n"
                                                          "Content-Length: ") + htmlSize +
                QByteArrayLiteral("\r\n\r\n") +
                html;

        socket->write(replyMessage);
    }
    socket->disconnectFromHost();
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 263, as _ZN35QOAuthHttpServerReplyHandlerPrivate21initializeLocalServerEv
inline void QOAuthHttpServerReplyHandlerPrivate::initializeLocalServer()
{
    Q_Q(QOAuthHttpServerReplyHandler);
    QObject::connect(httpServer, &QTcpServer::pendingConnectionAvailable, q, [this]() {
        _q_clientConnected();
    });
}

//  from ../qtnetworkauth/src/oauth/qoauthhttpserverreplyhandler.cpp, line 271, as _ZN35QOAuthHttpServerReplyHandlerPrivate6listenERK12QHostAddresst
inline bool QOAuthHttpServerReplyHandlerPrivate::listen(const QHostAddress &address, quint16 port)
{
    Q_ASSERT(httpServer);
    bool success = false;

    if (address.isNull()) {
        // try IPv4 first, for greatest compatibility
        success = httpServer->listen(QHostAddress::LocalHost, port);
        if (!success)
            success = httpServer->listen(QHostAddress::LocalHostIPv6, port);
    }
    if (!success)
        success = httpServer->listen(address, port);

    if (success) {
        // Callback ('redirect_uri') value may be needed after this handler is closed
        callbackAddress = httpServer->serverAddress();
        callbackPort = httpServer->serverPort();
    }
    return success;
}
//  -----------------------------------------------------------------------

//  QOAuthHttpServerReplyHandler
//      *QOAuthHttpServerReplyHandlerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QOAuthHttpServerReplyHandler *ritual_ZN35QOAuthHttpServerReplyHandlerPrivate6q_funcEv(
    QOAuthHttpServerReplyHandlerPrivate *self) {
  return self->q_func();
}

//  const QOAuthHttpServerReplyHandler
//      *QOAuthHttpServerReplyHandlerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QOAuthHttpServerReplyHandler *ritual_ZNK35QOAuthHttpServerReplyHandlerPrivate6q_funcEv(
    const QOAuthHttpServerReplyHandlerPrivate *self) {
  return self->q_func();
}

//  QOAuthHttpServerReplyHandlerPrivate::QOAuthHttpServerReplyHandlerPrivate(
//      QOAuthHttpServerReplyHandler *p)
extern "C" Q_DECL_EXPORT
QOAuthHttpServerReplyHandlerPrivate *ritual_ZN35QOAuthHttpServerReplyHandlerPrivateC1EP28QOAuthHttpServerReplyHandler(
    QOAuthHttpServerReplyHandler *p) {
  return new QOAuthHttpServerReplyHandlerPrivate(p);
}

//  QOAuthHttpServerReplyHandlerPrivate::~QOAuthHttpServerReplyHandlerPrivate
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuthHttpServerReplyHandlerPrivateD1Ev(
    QOAuthHttpServerReplyHandlerPrivate *self) {
  delete self;
}

//  QString QOAuthHttpServerReplyHandlerPrivate::callback() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK35QOAuthHttpServerReplyHandlerPrivate8callbackEv(
    const QOAuthHttpServerReplyHandlerPrivate *self) {
  return new QString(self->callback());
}

//  QString QOAuthHttpServerReplyHandlerPrivate::callbackHost() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK35QOAuthHttpServerReplyHandlerPrivate12callbackHostEv(
    const QOAuthHttpServerReplyHandlerPrivate *self) {
  return new QString(self->callbackHost());
}

//  void QOAuthHttpServerReplyHandlerPrivate::_q_clientConnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuthHttpServerReplyHandlerPrivate18_q_clientConnectedEv(
    QOAuthHttpServerReplyHandlerPrivate *self) {
  self->_q_clientConnected();
}

//  void QOAuthHttpServerReplyHandlerPrivate::_q_readData(QTcpSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuthHttpServerReplyHandlerPrivate11_q_readDataEP10QTcpSocket(
    QOAuthHttpServerReplyHandlerPrivate *self,
    QTcpSocket *socket) {
  self->_q_readData(socket);
}

//  void QOAuthHttpServerReplyHandlerPrivate::_q_answerClient(QTcpSocket
//      *socket, const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuthHttpServerReplyHandlerPrivate15_q_answerClientEP10QTcpSocketRK4QUrl(
    QOAuthHttpServerReplyHandlerPrivate *self,
    QTcpSocket *socket,
    const QUrl *url) {
  self->_q_answerClient(socket, *url);
}

//  void QOAuthHttpServerReplyHandlerPrivate::initializeLocalServer()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QOAuthHttpServerReplyHandlerPrivate21initializeLocalServerEv(
    QOAuthHttpServerReplyHandlerPrivate *self) {
  self->initializeLocalServer();
}

//  bool QOAuthHttpServerReplyHandlerPrivate::listen(const QHostAddress
//      &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QOAuthHttpServerReplyHandlerPrivate6listenERK12QHostAddresst(
    QOAuthHttpServerReplyHandlerPrivate *self,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}
