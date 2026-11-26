//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtwebsockets/src/websockets/qwebsocket_p.cpp, line 85, as _ZN23QWebSocketConfigurationC1Ev
inline QWebSocketConfiguration::QWebSocketConfiguration() :
#ifndef QT_NO_SSL
    m_sslConfiguration(QSslConfiguration::defaultConfiguration()),
    m_ignoredSslErrors(),
    m_ignoreSslErrors(false),
#endif
#ifndef QT_NO_NETWORKPROXY
    m_proxy(QNetworkProxy::DefaultProxy),
#endif
    m_pSocket(nullptr)
{
}
//  -----------------------------------------------------------------------

//  QWebSocketConfiguration::QWebSocketConfiguration()
extern "C" Q_DECL_EXPORT
QWebSocketConfiguration *ritual_ZN23QWebSocketConfigurationC1Ev() {
  return new QWebSocketConfiguration();
}
