//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrequest_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverrequest_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qsslconfiguration.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtHttpServer/private/qhttpserverparser_p.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtNetwork/qhttpheaders.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qtcpsocket.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslsocket.h>
#endif
#if QT_CONFIG(http)
#include <QtNetwork/private/qhttp2connection_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qthttpserver/src/httpserver/qhttpserverrequest.cpp, line 53, as _ZN25QHttpServerRequestPrivateC1ERK12QHostAddresstS2_t
inline QHttpServerRequestPrivate::QHttpServerRequestPrivate(const QHostAddress &remoteAddress,
                                                     quint16 remotePort,
                                                     const QHostAddress &localAddress,
                                                     quint16 localPort)
    : remoteAddress(remoteAddress),
      remotePort(remotePort),
      localAddress(localAddress),
      localPort(localPort)
{
}

//  from ../qthttpserver/src/httpserver/qhttpserverrequest.cpp, line 68, as _ZN25QHttpServerRequestPrivateC1ERK12QHostAddresstS2_tRK17QSslConfiguration
#if QT_CONFIG(ssl)
inline QHttpServerRequestPrivate::QHttpServerRequestPrivate(const QHostAddress &remoteAddress,
                                                     quint16 remotePort,
                                                     const QHostAddress &localAddress,
                                                     quint16 localPort,
                                                     const QSslConfiguration &sslConfiguration)
    : remoteAddress(remoteAddress),
      remotePort(remotePort),
      localAddress(localAddress),
      localPort(localPort),
      sslConfiguration(sslConfiguration)
{
}
#endif  // QT_CONFIG(ssl)
//  -----------------------------------------------------------------------

//  QHttpServerRequestPrivate::QHttpServerRequestPrivate(const QHostAddress
//      &remoteAddress, quint16 remotePort, const QHostAddress &localAddress,
//      quint16 localPort)
extern "C" Q_DECL_EXPORT
QHttpServerRequestPrivate *ritual_ZN25QHttpServerRequestPrivateC1ERK12QHostAddresstS2_t(
    const QHostAddress *remoteAddress,
    quint16 remotePort,
    const QHostAddress *localAddress,
    quint16 localPort) {
  return new QHttpServerRequestPrivate(
      *remoteAddress,
      remotePort,
      *localAddress,
      localPort);
}

#if QT_CONFIG(ssl)
//  QHttpServerRequestPrivate::QHttpServerRequestPrivate(const QHostAddress
//      &remoteAddress, quint16 remotePort, const QHostAddress &localAddress,
//      quint16 localPort, const QSslConfiguration &sslConfiguration)
extern "C" Q_DECL_EXPORT
QHttpServerRequestPrivate *ritual_ZN25QHttpServerRequestPrivateC1ERK12QHostAddresstS2_tRK17QSslConfiguration(
    const QHostAddress *remoteAddress,
    quint16 remotePort,
    const QHostAddress *localAddress,
    quint16 localPort,
    const QSslConfiguration *sslConfiguration) {
  return new QHttpServerRequestPrivate(
      *remoteAddress,
      remotePort,
      *localAddress,
      localPort,
      *sslConfiguration);
}
#endif  // QT_CONFIG(ssl)

//  QHttpServerRequestPrivate::QHttpServerRequestPrivate()
extern "C" Q_DECL_EXPORT
QHttpServerRequestPrivate *ritual_ZN25QHttpServerRequestPrivateC1Ev() {
  return new QHttpServerRequestPrivate();
}

//  QHttpServerRequestPrivate::QHttpServerRequestPrivate(const
//      QHttpServerRequestPrivate &other)
extern "C" Q_DECL_EXPORT
QHttpServerRequestPrivate *ritual_ZN25QHttpServerRequestPrivateC1ERKS_(
    const QHttpServerRequestPrivate *other) {
  return new QHttpServerRequestPrivate(*other);
}

//  QHttpServerRequestPrivate::~QHttpServerRequestPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QHttpServerRequestPrivateD1Ev(
    QHttpServerRequestPrivate *self) {
  delete self;
}
