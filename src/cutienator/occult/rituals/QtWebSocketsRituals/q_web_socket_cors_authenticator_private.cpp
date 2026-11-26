//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketcorsauthenticator_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtWebSockets/QtWebSockets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/6.12.0/QtWebSockets/private/qwebsocketcorsauthenticator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWebSockets/qwebsocketcorsauthenticator.h>
#include <QtWebSockets/private/qwebsocketcorsauthenticator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwebsockets/src/websockets/qwebsocketcorsauthenticator.cpp, line 46, as _ZN34QWebSocketCorsAuthenticatorPrivateC1ERK7QStringb
inline QWebSocketCorsAuthenticatorPrivate::QWebSocketCorsAuthenticatorPrivate(const QString &origin,
                                                                       bool allowed) :
    m_origin(origin),
    m_isAllowed(allowed)
{}

//  from ../qtwebsockets/src/websockets/qwebsocketcorsauthenticator.cpp, line 55, as _ZN34QWebSocketCorsAuthenticatorPrivateD1Ev
inline QWebSocketCorsAuthenticatorPrivate::~QWebSocketCorsAuthenticatorPrivate()
{}
//  -----------------------------------------------------------------------

//  QWebSocketCorsAuthenticatorPrivate::QWebSocketCorsAuthenticatorPrivate(co
//      nst QString &origin, bool allowed)
extern "C" Q_DECL_EXPORT
QWebSocketCorsAuthenticatorPrivate *ritual_ZN34QWebSocketCorsAuthenticatorPrivateC1ERK7QStringb(
    const QString *origin,
    bool allowed) {
  return new QWebSocketCorsAuthenticatorPrivate(*origin, allowed);
}

//  QWebSocketCorsAuthenticatorPrivate::~QWebSocketCorsAuthenticatorPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QWebSocketCorsAuthenticatorPrivateD1Ev(
    QWebSocketCorsAuthenticatorPrivate *self) {
  delete self;
}
