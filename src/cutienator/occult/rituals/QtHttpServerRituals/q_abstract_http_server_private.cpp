//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qabstracthttpserver_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/qabstracthttpserver.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qabstracthttpserver_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qabstracthttpserver.cpp, line 65, as _ZN26QAbstractHttpServerPrivateC1Ev
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
//  -----------------------------------------------------------------------

//  QAbstractHttpServer *QAbstractHttpServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractHttpServer *ritual_ZN26QAbstractHttpServerPrivate6q_funcEv(
    QAbstractHttpServerPrivate *self) {
  return self->q_func();
}

//  const QAbstractHttpServer *QAbstractHttpServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractHttpServer *ritual_ZNK26QAbstractHttpServerPrivate6q_funcEv(
    const QAbstractHttpServerPrivate *self) {
  return self->q_func();
}

//  QAbstractHttpServerPrivate::QAbstractHttpServerPrivate()
extern "C" Q_DECL_EXPORT
QAbstractHttpServerPrivate *ritual_ZN26QAbstractHttpServerPrivateC1Ev() {
  return new QAbstractHttpServerPrivate();
}

//  void QAbstractHttpServerPrivate::restartHeartbeatTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QAbstractHttpServerPrivate21restartHeartbeatTimerEv(
    QAbstractHttpServerPrivate *self) {
  self->restartHeartbeatTimer();
}
