//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketserver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/qwebsocketserver.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtWebSockets/QWebSocketProtocol>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/qwebsocketserver.h>
#include <QtWebSockets/private/qwebsocketserver_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/qwebsocket.h>
#include <QtWebSockets/private/qwebsocket_p.h>
#include <QtWebSockets/qwebsocketcorsauthenticator.h>
#include <limits>
#ifndef QT_NO_SSL
#include "QtNetwork/QSslServer"
#endif
#include <QtCore/QTimer>
#include <QtNetwork/QTcpServer>
#include <QtNetwork/QTcpSocket>
#include <QtNetwork/QNetworkProxy>
#include <QtWebSockets/qwebsocket.h>
#include <QtWebSockets/private/qwebsocket_p.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/private/qdefaultmaskgenerator_p.h>
#include <QtCore/QUrl>
#include <QtNetwork/QAuthenticator>
#include <QtNetwork/QTcpSocket>
#include <QtCore/QByteArray>
#include <QtCore/QtEndian>
#include <QtCore/QCryptographicHash>
#include <QtCore/QRegularExpression>
#include <QtCore/QStringList>
#include <QtNetwork/QHostAddress>
#include <QtCore/QStringBuilder>   //for more efficient string concatenation
#ifndef QT_NONETWORKPROXY
#include <QtNetwork/QNetworkProxy>
#endif
#ifndef QT_NO_SSL
#include <QtNetwork/QSslConfiguration>
#include <QtNetwork/QSslError>
#include <QtNetwork/QSslPreSharedKeyAuthenticator>
#endif
#include <QtNetwork/private/qhttpheaderparser_p.h>
#include <QtNetwork/private/qauthenticator_p.h>
#include <QtCore/QDebug>
#include <QtCore/QTimer>
#include <limits>
#include <memory>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QMap>
#include <QtCore/QTextStream>
#include <QtCore/QUrl>
#include <QtCore/QList>
#include <QtCore/QStringList>
#include <functional>   //for std::greater
#include <QtWebSockets/private/qwebsockethandshakeresponse_p.h>
#include <QtWebSockets/private/qwebsockethandshakerequest_p.h>
#include <QtWebSockets/qwebsocketprotocol.h>
#include <QtWebSockets/private/qwebsocketprotocol_p.h>
#include <QtCore/QString>
#include <QtCore/QTextStream>
#include <QtCore/QByteArray>
#include <QtCore/QStringList>
#include <QtCore/QDateTime>
#include <QtCore/QLocale>
#include <QtCore/QCryptographicHash>
#include <QtCore/QSet>
#include <QtCore/QList>
#include <QtCore/QStringBuilder>   //for more efficient string concatenation
#include <algorithm>
#include <functional>   //for std::greater
#include <iterator>
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

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 171, as local:qwebsockethandshakerequest.cpp:readLine
static QByteArrayView readLine(QByteArrayView &header, int maxHeaderLineLength)
{
    qsizetype length = qMin(maxHeaderLineLength, header.size());
    QByteArrayView line = header.first(length);
    qsizetype end = line.indexOf('\n');
    if (end != -1) {
        line = line.first(end);
        if (line.endsWith('\r'))
            line.chop(1);
        header = header.sliced(end + 1);
        return line;
    }
    return QByteArrayView();
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 189, as local:qwebsockethandshakerequest.cpp:appendCommmaSeparatedLineToList
static void appendCommmaSeparatedLineToList(QStringList &list, QByteArrayView line)
{
    for (auto &c : QLatin1String(line).tokenize(QLatin1String(","), Qt::SkipEmptyParts))
        list << c.trimmed().toString();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 205, as _ZN23QWebSocketServerPrivate21nextPendingConnectionEv
inline QWebSocket *QWebSocketServerPrivate::nextPendingConnection()
{
    QWebSocket *pWebSocket = nullptr;
    if (Q_LIKELY(!m_pendingConnections.isEmpty()))
        pWebSocket = m_pendingConnections.dequeue();
    return pWebSocket;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 113, as _ZN23QWebSocketServerPrivateD2Ev
inline QWebSocketServerPrivate::~QWebSocketServerPrivate()
{
}

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 357, as _ZN17QWebSocketPrivate11upgradeFromEP10QTcpSocketRK26QWebSocketHandshakeRequestRK27QWebSocketHandshakeResponseP7QObject
inline QWebSocket *QWebSocketPrivate::upgradeFrom(QTcpSocket *pTcpSocket,
                                           const QWebSocketHandshakeRequest &request,
                                           const QWebSocketHandshakeResponse &response,
                                           QObject *parent)
{
    QWebSocket *pWebSocket = new QWebSocket(pTcpSocket, response.acceptedVersion(), parent);
    if (Q_LIKELY(pWebSocket)) {
        QNetworkRequest netRequest(request.requestUrl());
        netRequest.setHeaders(request.headers());
#ifndef QT_NO_SSL
        if (QSslSocket *sslSock = qobject_cast<QSslSocket *>(pTcpSocket))
            pWebSocket->setSslConfiguration(sslSock->sslConfiguration());
#endif
        QWebSocketHandshakeOptions options;
        options.setSubprotocols(request.protocols());

        pWebSocket->d_func()->setExtension(response.acceptedExtension());
        pWebSocket->d_func()->setOrigin(request.origin());
        pWebSocket->d_func()->setRequest(netRequest, options);
        pWebSocket->d_func()->setProtocol(response.acceptedProtocol());
        pWebSocket->d_func()->setResourceName(request.requestUrl().toString(QUrl::RemoveUserInfo));
        //a server should not send masked frames
        pWebSocket->d_func()->enableMasking(false);
    }

    return pWebSocket;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 23, as _ZN26QWebSocketHandshakeRequestC1Eib
inline QWebSocketHandshakeRequest::QWebSocketHandshakeRequest(int port, bool isSecure) :
    m_port(port),
    m_isSecure(isSecure),
    m_isValid(false),
    m_parser(),
    m_versions(),
    m_key(),
    m_origin(),
    m_protocols(),
    m_extensions(),
    m_requestUrl()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 40, as _ZN26QWebSocketHandshakeRequestD1Ev
inline QWebSocketHandshakeRequest::~QWebSocketHandshakeRequest()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 30, as _ZN27QWebSocketHandshakeResponseC1ERK26QWebSocketHandshakeRequestRK7QStringbRK5QListIN18QWebSocketProtocol7VersionEERKS6_IS3_ESE_
inline QWebSocketHandshakeResponse::QWebSocketHandshakeResponse(
        const QWebSocketHandshakeRequest &request,
        const QString &serverName,
        bool isOriginAllowed,
        const QList<QWebSocketProtocol::Version> &supportedVersions,
        const QList<QString> &supportedProtocols,
        const QList<QString> &supportedExtensions) :
    m_isValid(false),
    m_canUpgrade(false),
    m_response(),
    m_acceptedProtocol(),
    m_acceptedExtension(),
    m_acceptedVersion(QWebSocketProtocol::VersionUnknown),
    m_error(QWebSocketProtocol::CloseCodeNormal),
    m_errorString()
{
    m_response = getHandshakeResponse(request, serverName,
                                      isOriginAllowed, supportedVersions,
                                      supportedProtocols, supportedExtensions);
    m_isValid = true;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 55, as _ZN27QWebSocketHandshakeResponseD1Ev
inline QWebSocketHandshakeResponse::~QWebSocketHandshakeResponse()
{
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 135, as _ZNK26QWebSocketHandshakeRequest6originEv
inline QString QWebSocketHandshakeRequest::origin() const
{
    return m_origin;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakerequest.cpp, line 79, as _ZNK26QWebSocketHandshakeRequest7isValidEv
inline bool QWebSocketHandshakeRequest::isValid() const
{
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 70, as _ZNK27QWebSocketHandshakeResponse10canUpgradeEv
inline bool QWebSocketHandshakeResponse::canUpgrade() const
{
    return m_isValid && m_canUpgrade;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 252, as _ZNK27QWebSocketHandshakeResponse11errorStringEv
inline QString QWebSocketHandshakeResponse::errorString() const
{
    return m_errorString;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 244, as _ZNK27QWebSocketHandshakeResponse5errorEv
inline QWebSocketProtocol::CloseCode QWebSocketHandshakeResponse::error() const
{
    return m_error;
}

//  from ../qtwebsockets/src/websockets/qwebsockethandshakeresponse.cpp, line 62, as _ZNK27QWebSocketHandshakeResponse7isValidEv
inline bool QWebSocketHandshakeResponse::isValid() const
{
    return m_isValid;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 28, as _ZN23QWebSocketServerPrivateC1ERK7QStringNS_7SslModeE
inline QWebSocketServerPrivate::QWebSocketServerPrivate(const QString &serverName,
                                                 QWebSocketServerPrivate::SslMode secureMode) :
    QObjectPrivate(),
    m_pTcpServer(nullptr),
    m_serverName(serverName),
    m_secureMode(secureMode),
    m_pendingConnections(),
    m_error(QWebSocketProtocol::CloseCodeNormal),
    m_errorString(),
    m_maxPendingConnections(30),
    m_handshakeTimeout(10000)
{}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 120, as _ZN23QWebSocketServerPrivate5closeEb
inline void QWebSocketServerPrivate::close(bool aboutToDestroy)
{
    Q_Q(QWebSocketServer);
    m_pTcpServer->close();
    while (!m_pendingConnections.isEmpty()) {
        QWebSocket *pWebSocket = m_pendingConnections.dequeue();
        pWebSocket->close(QWebSocketProtocol::CloseCodeGoingAway,
                          QWebSocketServer::tr("Server closed."));
        pWebSocket->deleteLater();
    }
    if (!aboutToDestroy) {
        //emit signal via the event queue, so the server gets time
        //to process any hanging events, like flushing buffers aso
        QMetaObject::invokeMethod(q, "closed", Qt::QueuedConnection);
    }
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 140, as _ZNK23QWebSocketServerPrivate11errorStringEv
inline QString QWebSocketServerPrivate::errorString() const
{
    if (m_errorString.isEmpty())
        return m_pTcpServer->errorString();
    else
        return m_errorString;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 151, as _ZNK23QWebSocketServerPrivate21hasPendingConnectionsEv
inline bool QWebSocketServerPrivate::hasPendingConnections() const
{
    return !m_pendingConnections.isEmpty();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 159, as _ZNK23QWebSocketServerPrivate11isListeningEv
inline bool QWebSocketServerPrivate::isListening() const
{
    return m_pTcpServer->isListening();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 167, as _ZN23QWebSocketServerPrivate6listenERK12QHostAddresst
inline bool QWebSocketServerPrivate::listen(const QHostAddress &address, quint16 port)
{
    bool success = m_pTcpServer->listen(address, port);
    if (!success)
        setErrorFromSocketError(m_pTcpServer->serverError(), m_pTcpServer->errorString());
    return success;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 178, as _ZNK23QWebSocketServerPrivate21maxPendingConnectionsEv
inline int QWebSocketServerPrivate::maxPendingConnections() const
{
    return m_maxPendingConnections;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 216, as _ZN23QWebSocketServerPrivate14pauseAcceptingEv
inline void QWebSocketServerPrivate::pauseAccepting()
{
    m_pTcpServer->pauseAccepting();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 225, as _ZNK23QWebSocketServerPrivate5proxyEv
#if !defined(QT_NO_NETWORKPROXY)
inline QNetworkProxy QWebSocketServerPrivate::proxy() const
{
    return m_pTcpServer->proxy();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 233, as _ZN23QWebSocketServerPrivate8setProxyERK13QNetworkProxy
#if !defined(QT_NO_NETWORKPROXY)
inline void QWebSocketServerPrivate::setProxy(const QNetworkProxy &networkProxy)
{
    m_pTcpServer->setProxy(networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 241, as _ZN23QWebSocketServerPrivate15resumeAcceptingEv
inline void QWebSocketServerPrivate::resumeAccepting()
{
    m_pTcpServer->resumeAccepting();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 249, as _ZNK23QWebSocketServerPrivate13serverAddressEv
inline QHostAddress QWebSocketServerPrivate::serverAddress() const
{
    return m_pTcpServer->serverAddress();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 257, as _ZNK23QWebSocketServerPrivate11serverErrorEv
inline QWebSocketProtocol::CloseCode QWebSocketServerPrivate::serverError() const
{
    return m_error;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 265, as _ZNK23QWebSocketServerPrivate10serverPortEv
inline quint16 QWebSocketServerPrivate::serverPort() const
{
    return m_pTcpServer->serverPort();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 273, as _ZN23QWebSocketServerPrivate24setMaxPendingConnectionsEi
inline void QWebSocketServerPrivate::setMaxPendingConnections(int numConnections)
{
    if (m_pTcpServer->maxPendingConnections() <= numConnections)
        m_pTcpServer->setMaxPendingConnections(numConnections + 1);
    m_maxPendingConnections = numConnections;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 283, as _ZN23QWebSocketServerPrivate19setHandshakeTimeoutEi
inline void QWebSocketServerPrivate::setHandshakeTimeout(int msec)
{
#if QT_CONFIG(ssl)
    if (auto *server = qobject_cast<QSslServer *>(m_pTcpServer)) {
        int timeout = msec;
        // Since QSslServer doesn't deal with negative numbers we set a very
        // large one instead to keep some level of compatibility:
        if (timeout < 0)
            timeout = std::numeric_limits<int>::max();
        server->setHandshakeTimeout(timeout);
    }
#endif
    m_handshakeTimeout = msec;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 301, as _ZN23QWebSocketServerPrivate19setSocketDescriptorEx
inline bool QWebSocketServerPrivate::setSocketDescriptor(qintptr socketDescriptor)
{
    return m_pTcpServer->setSocketDescriptor(socketDescriptor);
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 309, as _ZNK23QWebSocketServerPrivate16socketDescriptorEv
inline qintptr QWebSocketServerPrivate::socketDescriptor() const
{
    return m_pTcpServer->socketDescriptor();
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 317, as _ZNK23QWebSocketServerPrivate17supportedVersionsEv
inline QList<QWebSocketProtocol::Version> QWebSocketServerPrivate::supportedVersions() const
{
    QList<QWebSocketProtocol::Version> supportedVersions;
    supportedVersions << QWebSocketProtocol::currentVersion();	//we only support V13
    return supportedVersions;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 327, as _ZN23QWebSocketServerPrivate24setSupportedSubprotocolsERK5QListI7QStringE
inline void QWebSocketServerPrivate::setSupportedSubprotocols(const QStringList &protocols)
{
    m_supportedSubprotocols = protocols;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 335, as _ZNK23QWebSocketServerPrivate21supportedSubprotocolsEv
inline QStringList QWebSocketServerPrivate::supportedSubprotocols() const
{
    return m_supportedSubprotocols;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 343, as _ZNK23QWebSocketServerPrivate19supportedExtensionsEv
inline QStringList QWebSocketServerPrivate::supportedExtensions() const
{
    QStringList supportedExtensions;
    return supportedExtensions;	//no extensions are currently supported
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 352, as _ZN23QWebSocketServerPrivate13setServerNameERK7QString
inline void QWebSocketServerPrivate::setServerName(const QString &serverName)
{
    if (m_serverName != serverName)
        m_serverName = serverName;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 361, as _ZNK23QWebSocketServerPrivate10serverNameEv
inline QString QWebSocketServerPrivate::serverName() const
{
    return m_serverName;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 369, as _ZNK23QWebSocketServerPrivate10secureModeEv
inline QWebSocketServerPrivate::SslMode QWebSocketServerPrivate::secureMode() const
{
    return m_secureMode;
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 375, as _ZN23QWebSocketServerPrivate19setSslConfigurationERK17QSslConfiguration
#if !defined(QT_NO_SSL)
inline void QWebSocketServerPrivate::setSslConfiguration(const QSslConfiguration &sslConfiguration)
{
    if (m_secureMode == SecureMode)
        qobject_cast<QSslServer *>(m_pTcpServer)->setSslConfiguration(sslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 381, as _ZNK23QWebSocketServerPrivate16sslConfigurationEv
#if !defined(QT_NO_SSL)
inline QSslConfiguration QWebSocketServerPrivate::sslConfiguration() const
{
    if (m_secureMode == SecureMode)
        return qobject_cast<QSslServer *>(m_pTcpServer)->sslConfiguration();
    else
        return QSslConfiguration::defaultConfiguration();
}
#endif  // !defined(QT_NO_SSL)

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 390, as _ZN23QWebSocketServerPrivate8setErrorEN18QWebSocketProtocol9CloseCodeERK7QString
inline void QWebSocketServerPrivate::setError(QWebSocketProtocol::CloseCode code, const QString &errorString)
{
    if ((m_error != code) || (m_errorString != errorString)) {
        Q_Q(QWebSocketServer);
        m_error = code;
        m_errorString = errorString;
        Q_EMIT q->serverError(code);
    }
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 566, as _ZNK23QWebSocketServerPrivate21startHandshakeTimeoutEP10QTcpSocket
inline void QWebSocketServerPrivate::startHandshakeTimeout(QTcpSocket *pTcpSocket) const
{
    if (m_handshakeTimeout < 0)
        return;

    QTimer *handshakeTimer = new QTimer(pTcpSocket);
    handshakeTimer->setSingleShot(true);
    handshakeTimer->setObjectName(QStringLiteral("handshakeTimer"));
    QObject::connect(handshakeTimer, &QTimer::timeout, pTcpSocket, &QAbstractSocket::close);
    handshakeTimer->start(m_handshakeTimeout);
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 186, as _ZN23QWebSocketServerPrivate20addPendingConnectionEP10QWebSocket
inline void QWebSocketServerPrivate::addPendingConnection(QWebSocket *pWebSocket)
{
    if (m_pendingConnections.size() < maxPendingConnections())
        m_pendingConnections.enqueue(pWebSocket);
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 195, as _ZN23QWebSocketServerPrivate23setErrorFromSocketErrorEN15QAbstractSocket11SocketErrorERK7QString
inline void QWebSocketServerPrivate::setErrorFromSocketError(QAbstractSocket::SocketError error,
                                                      const QString &errorDescription)
{
    Q_UNUSED(error);
    setError(QWebSocketProtocol::CloseCodeAbnormalDisconnection, errorDescription);
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 415, as _ZN23QWebSocketServerPrivate20onSocketDisconnectedEv
inline void QWebSocketServerPrivate::onSocketDisconnected()
{
    Q_Q(QWebSocketServer);
    QObject *sender = q->sender();
    if (Q_LIKELY(sender)) {
        QTcpSocket *pTcpSocket = qobject_cast<QTcpSocket*>(sender);
        if (Q_LIKELY(pTcpSocket)) {
            pTcpSocket->deleteLater();
            m_error = QWebSocketProtocol::CloseCode::CloseCodeNormal;
            m_errorString = QString();
        }
    }
}

//  from ../qtwebsockets/src/websockets/qwebsocketserver_p.cpp, line 578, as _ZN23QWebSocketServerPrivate22finishHandshakeTimeoutEP10QTcpSocket
inline void QWebSocketServerPrivate::finishHandshakeTimeout(QTcpSocket *pTcpSocket)
{
    if (QTimer *handshakeTimer = pTcpSocket->findChild<QTimer *>(QStringLiteral("handshakeTimer"))) {
        handshakeTimer->stop();
        delete handshakeTimer;
    }
}
//  -----------------------------------------------------------------------

//  A QWebSocketServerPrivate that Python can take functions over in. Every QWebSocketServerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQWebSocketServerPrivateCall0)(const void *, int *);
class CuteQWebSocketServerPrivate : public QWebSocketServerPrivate {
public:
  using QWebSocketServerPrivate::QWebSocketServerPrivate;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN23QWebSocketServerPrivate21nextPendingConnectionEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QWebSocket *QWebSocketServerPrivate::nextPendingConnection()
  QWebSocket *nextPendingConnection() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWebSocketServerPrivateCall0 call = reinterpret_cast<CuteQWebSocketServerPrivateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QWebSocket *>(given);
    }
    return QWebSocketServerPrivate::nextPendingConnection();
  }
};

//  QWebSocketServer *QWebSocketServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWebSocketServer *ritual_ZN23QWebSocketServerPrivate6q_funcEv(
    QWebSocketServerPrivate *self) {
  return self->q_func();
}

//  const QWebSocketServer *QWebSocketServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWebSocketServer *ritual_ZNK23QWebSocketServerPrivate6q_funcEv(
    const QWebSocketServerPrivate *self) {
  return self->q_func();
}

//  QWebSocketServerPrivate::QWebSocketServerPrivate(const QString
//      &serverName, SslMode secureMode)
extern "C" Q_DECL_EXPORT
QWebSocketServerPrivate *ritual_ZN23QWebSocketServerPrivateC1ERK7QStringNS_7SslModeE(
    const QString *serverName,
    QWebSocketServerPrivate::SslMode secureMode) {
  return new CuteQWebSocketServerPrivate(*serverName, secureMode);
}

//  QWebSocketServerPrivate::~QWebSocketServerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivateD1Ev(QWebSocketServerPrivate *self) {
  delete self;
}

//  void QWebSocketServerPrivate::close(bool aboutToDestroy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate5closeEb(
    QWebSocketServerPrivate *self,
    bool aboutToDestroy) {
  self->close(aboutToDestroy);
}

//  QString QWebSocketServerPrivate::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebSocketServerPrivate11errorStringEv(
    const QWebSocketServerPrivate *self) {
  return new QString(self->errorString());
}

//  bool QWebSocketServerPrivate::hasPendingConnections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWebSocketServerPrivate21hasPendingConnectionsEv(
    const QWebSocketServerPrivate *self) {
  return self->hasPendingConnections();
}

//  bool QWebSocketServerPrivate::isListening() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWebSocketServerPrivate11isListeningEv(
    const QWebSocketServerPrivate *self) {
  return self->isListening();
}

//  bool QWebSocketServerPrivate::listen(const QHostAddress &address, quint16
//      port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QWebSocketServerPrivate6listenERK12QHostAddresst(
    QWebSocketServerPrivate *self,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}

//  int QWebSocketServerPrivate::maxPendingConnections() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QWebSocketServerPrivate21maxPendingConnectionsEv(
    const QWebSocketServerPrivate *self) {
  return self->maxPendingConnections();
}

//  int QWebSocketServerPrivate::handshakeTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QWebSocketServerPrivate16handshakeTimeoutEv(
    const QWebSocketServerPrivate *self) {
  return self->handshakeTimeout();
}

//  QWebSocket *QWebSocketServerPrivate::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_ZN23QWebSocketServerPrivate21nextPendingConnectionEv(
    QWebSocketServerPrivate *self) {
  return self->nextPendingConnection();
}

//  void QWebSocketServerPrivate::pauseAccepting()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate14pauseAcceptingEv(
    QWebSocketServerPrivate *self) {
  self->pauseAccepting();
}

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QWebSocketServerPrivate::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK23QWebSocketServerPrivate5proxyEv(
    const QWebSocketServerPrivate *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QWebSocketServerPrivate::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate8setProxyERK13QNetworkProxy(
    QWebSocketServerPrivate *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QWebSocketServerPrivate::resumeAccepting()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate15resumeAcceptingEv(
    QWebSocketServerPrivate *self) {
  self->resumeAccepting();
}

//  QHostAddress QWebSocketServerPrivate::serverAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK23QWebSocketServerPrivate13serverAddressEv(
    const QWebSocketServerPrivate *self) {
  return new QHostAddress(self->serverAddress());
}

//  QWebSocketProtocol::CloseCode QWebSocketServerPrivate::serverError()
//      const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK23QWebSocketServerPrivate11serverErrorEv(
    const QWebSocketServerPrivate *self) {
  return self->serverError();
}

//  quint16 QWebSocketServerPrivate::serverPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK23QWebSocketServerPrivate10serverPortEv(
    const QWebSocketServerPrivate *self) {
  return self->serverPort();
}

//  void QWebSocketServerPrivate::setMaxPendingConnections(int
//      numConnections)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate24setMaxPendingConnectionsEi(
    QWebSocketServerPrivate *self,
    int numConnections) {
  self->setMaxPendingConnections(numConnections);
}

//  void QWebSocketServerPrivate::setHandshakeTimeout(int msec)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate19setHandshakeTimeoutEi(
    QWebSocketServerPrivate *self,
    int msec) {
  self->setHandshakeTimeout(msec);
}

//  bool QWebSocketServerPrivate::setSocketDescriptor(qintptr
//      socketDescriptor)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QWebSocketServerPrivate19setSocketDescriptorEx(
    QWebSocketServerPrivate *self,
    qintptr socketDescriptor) {
  return self->setSocketDescriptor(socketDescriptor);
}

//  qintptr QWebSocketServerPrivate::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK23QWebSocketServerPrivate16socketDescriptorEv(
    const QWebSocketServerPrivate *self) {
  return self->socketDescriptor();
}

//  QList<QWebSocketProtocol::Version>
//      QWebSocketServerPrivate::supportedVersions() const
extern "C" Q_DECL_EXPORT
QList<QWebSocketProtocol::Version> *ritual_ZNK23QWebSocketServerPrivate17supportedVersionsEv(
    const QWebSocketServerPrivate *self) {
  return new QList<QWebSocketProtocol::Version>(self->supportedVersions());
}

//  void QWebSocketServerPrivate::setSupportedSubprotocols(const QStringList
//      &protocols)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate24setSupportedSubprotocolsERK5QListI7QStringE(
    QWebSocketServerPrivate *self,
    const QList<QString> *protocols) {
  self->setSupportedSubprotocols(*protocols);
}

//  QStringList QWebSocketServerPrivate::supportedSubprotocols() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK23QWebSocketServerPrivate21supportedSubprotocolsEv(
    const QWebSocketServerPrivate *self) {
  return new QList<QString>(self->supportedSubprotocols());
}

//  QStringList QWebSocketServerPrivate::supportedExtensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK23QWebSocketServerPrivate19supportedExtensionsEv(
    const QWebSocketServerPrivate *self) {
  return new QList<QString>(self->supportedExtensions());
}

//  void QWebSocketServerPrivate::setServerName(const QString &serverName)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate13setServerNameERK7QString(
    QWebSocketServerPrivate *self,
    const QString *serverName) {
  self->setServerName(*serverName);
}

//  QString QWebSocketServerPrivate::serverName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebSocketServerPrivate10serverNameEv(
    const QWebSocketServerPrivate *self) {
  return new QString(self->serverName());
}

//  SslMode QWebSocketServerPrivate::secureMode() const
extern "C" Q_DECL_EXPORT
QWebSocketServerPrivate::SslMode ritual_ZNK23QWebSocketServerPrivate10secureModeEv(
    const QWebSocketServerPrivate *self) {
  return self->secureMode();
}

#if !defined(QT_NO_SSL)
//  void QWebSocketServerPrivate::setSslConfiguration(const QSslConfiguration
//      &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate19setSslConfigurationERK17QSslConfiguration(
    QWebSocketServerPrivate *self,
    const QSslConfiguration *sslConfiguration) {
  self->setSslConfiguration(*sslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  QSslConfiguration QWebSocketServerPrivate::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK23QWebSocketServerPrivate16sslConfigurationEv(
    const QWebSocketServerPrivate *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

//  void QWebSocketServerPrivate::setError(QWebSocketProtocol::CloseCode
//      code, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate8setErrorEN18QWebSocketProtocol9CloseCodeERK7QString(
    QWebSocketServerPrivate *self,
    QWebSocketProtocol::CloseCode code,
    const QString *errorString) {
  self->setError(code, *errorString);
}

//  void QWebSocketServerPrivate::startHandshakeTimeout(QTcpSocket
//      *pTcpSocket) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QWebSocketServerPrivate21startHandshakeTimeoutEP10QTcpSocket(
    const QWebSocketServerPrivate *self,
    QTcpSocket *pTcpSocket) {
  self->startHandshakeTimeout(pTcpSocket);
}

//  void QWebSocketServerPrivate::addPendingConnection(QWebSocket
//      *pWebSocket)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate20addPendingConnectionEP10QWebSocket(
    QWebSocketServerPrivate *self,
    QWebSocket *pWebSocket) {
  self->addPendingConnection(pWebSocket);
}

//  void QWebSocketServerPrivate::setErrorFromSocketError(QAbstractSocket::So
//      cketError error, const QString &errorDescription)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate23setErrorFromSocketErrorEN15QAbstractSocket11SocketErrorERK7QString(
    QWebSocketServerPrivate *self,
    QAbstractSocket::SocketError error,
    const QString *errorDescription) {
  self->setErrorFromSocketError(error, *errorDescription);
}

//  void QWebSocketServerPrivate::onSocketDisconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate20onSocketDisconnectedEv(
    QWebSocketServerPrivate *self) {
  self->onSocketDisconnected();
}

//  void QWebSocketServerPrivate::finishHandshakeTimeout(QTcpSocket
//      *pTcpSocket)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebSocketServerPrivate22finishHandshakeTimeoutEP10QTcpSocket(
    QWebSocketServerPrivate *self,
    QTcpSocket *pTcpSocket) {
  self->finishHandshakeTimeout(pTcpSocket);
}

//  a Python function taken by a CuteQWebSocketServerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocketServerPrivate(
    QWebSocketServerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebSocketServerPrivate *>(self)->take(key, call);
}

//  QWebSocket *QWebSocketServerPrivate::nextPendingConnection()
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_own_ZN23QWebSocketServerPrivate21nextPendingConnectionEv(
    QWebSocketServerPrivate *self) {
  return self->QWebSocketServerPrivate::nextPendingConnection();
}

//  a QList<QWebSocketProtocol::Version> a ritual of QWebSocketServerPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWebSocketServerPrivate__QList_QWebSocketProtocol_Version(
    QList<QWebSocketProtocol::Version> *self) {
  delete self;
}
