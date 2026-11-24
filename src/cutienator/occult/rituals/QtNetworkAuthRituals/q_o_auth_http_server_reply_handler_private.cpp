//  Written by dev_tooling.RitualGenerator from the records of QtNetworkAuth/
//  6.12.0/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtNetworkAuth/qoauthhttpserverreplyhandler.h>
#include <QtNetworkAuth/QtNetworkAuth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauthhttpserverreplyhandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qabstractoauth.h>
#include <qoauthhttpserverreplyhandler.h>
#include "qabstractoauthreplyhandler_p.h"
#include <private/qoauthhttpserverreplyhandler_p.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  bool QOAuthHttpServerReplyHandlerPrivate::listen(const QHostAddress
//      &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN35QOAuthHttpServerReplyHandlerPrivate6listenERK12QHostAddresst(
    QOAuthHttpServerReplyHandlerPrivate *self,
    const QHostAddress *address,
    quint16 port) {
  return self->listen(*address, port);
}
