//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/qhttpserver.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/private/qabstracthttpserver_p.h>
#include <QtHttpServer/private/qhttpserverhttp1protocolhandler_p.h>
#include <QtHttpServer/private/qhttpserverrequest_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qtcpserver.h>
#include <QtNetwork/qtcpsocket.h>
#if QT_CONFIG(ssl) && QT_CONFIG(http)
#include <QtNetwork/private/qhttp2connection_p.h>
#endif
#if QT_CONFIG(localserver)
#include <QtNetwork/qlocalserver.h>
#include <QtNetwork/qlocalsocket.h>
#endif
#if QT_CONFIG(ssl)
#include <QtNetwork/qsslserver.h>
#endif
#if QT_CONFIG(http) && QT_CONFIG(ssl)
#include <QtHttpServer/private/qhttpserverhttp2protocolhandler_p.h>
#endif
#include <algorithm>
#include <QtHttpServer/qhttpserver.h>
#include <QtHttpServer/qhttpserverrequest.h>
#include <QtHttpServer/qhttpserverresponder.h>
#include <QtHttpServer/qhttpserverresponse.h>
#include <QtHttpServer/private/qhttpserver_p.h>
#include <QtHttpServer/private/qhttpserverstream_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qtcpsocket.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qabstracthttpserver.cpp, line 65, as _ZN26QAbstractHttpServerPrivateC2Ev
inline QAbstractHttpServerPrivate::QAbstractHttpServerPrivate()
{
    restartHeartbeatTimer();
}

//  from ../qthttpserver/src/httpserver/qabstracthttpserver.cpp, line 220, as _ZN26QAbstractHttpServerPrivate21restartHeartbeatTimerEv
inline void QAbstractHttpServerPrivate::restartHeartbeatTimer()
{
    if (heartbeatTimer.isActive())
        heartbeatTimer.stop();

    const auto timerInterval = qMax(configuration.keepAliveTimeout() / 2,
                                    std::chrono::seconds(5));
    heartbeatTimer.start(timerInterval);
}

//  from ../qthttpserver/src/httpserver/qhttpserver.cpp, line 22, as _ZN18QHttpServerPrivateC1EP11QHttpServer
inline QHttpServerPrivate::QHttpServerPrivate(QHttpServer *p) :
    router(p)
{
}
//  -----------------------------------------------------------------------

//  QHttpServer *QHttpServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHttpServer *ritual_ZN18QHttpServerPrivate6q_funcEv(
    QHttpServerPrivate *self) {
  return self->q_func();
}

//  const QHttpServer *QHttpServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHttpServer *ritual_ZNK18QHttpServerPrivate6q_funcEv(
    const QHttpServerPrivate *self) {
  return self->q_func();
}

//  QHttpServerPrivate::QHttpServerPrivate(QHttpServer *p)
extern "C" Q_DECL_EXPORT
QHttpServerPrivate *ritual_ZN18QHttpServerPrivateC1EP11QHttpServer(
    QHttpServer *p) {
  return new QHttpServerPrivate(p);
}
