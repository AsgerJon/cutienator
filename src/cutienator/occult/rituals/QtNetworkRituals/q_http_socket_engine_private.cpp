//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(http)
#if !defined(QT_NO_NETWORKPROXY)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qhttpsocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractsocketengine_p.h"
#include "qnativesocketengine_p.h"
#include "qmutex.h"
#include "qnetworkproxy.h"
#include "qhttpsocketengine_p.h"
#include "qtcpsocket.h"
#include "qhostaddress.h"
#include "qurl.h"
#include "private/qhttpnetworkreply_p.h"
#include "private/qiodevice_p.h"
#include "qdeadlinetimer.h"
#include "qnetworkinterface.h"
#if !defined(QT_NO_NETWORKPROXY)
#include <qdebug.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qabstractsocketengine.cpp, line 40, as _ZN28QAbstractSocketEnginePrivateC2Ev
inline QAbstractSocketEnginePrivate::QAbstractSocketEnginePrivate()
    : socketError(QAbstractSocket::UnknownSocketError)
    , hasSetSocketError(false)
    , socketErrorString(QLatin1StringView(QT_TRANSLATE_NOOP(QSocketLayer, "Unknown error")))
    , socketState(QAbstractSocket::UnconnectedState)
    , socketType(QAbstractSocket::UnknownSocketType)
    , socketProtocol(QAbstractSocket::UnknownNetworkLayerProtocol)
    , localPort(0)
    , peerPort(0)
    , inboundStreamCount(0)
    , outboundStreamCount(0)
    , receiver(nullptr)
{
}

//  from src/network/socket/qhttpsocketengine.cpp, line 798, as _ZN24QHttpSocketEnginePrivateC1Ev
#if !defined(QT_NO_NETWORKPROXY)
inline QHttpSocketEnginePrivate::QHttpSocketEnginePrivate()
    : readNotificationEnabled(false)
    , writeNotificationEnabled(false)
    , exceptNotificationEnabled(false)
    , readNotificationPending(false)
    , writeNotificationPending(false)
    , connectionNotificationPending(false)
    , credentialsSent(false)
    , pendingResponseData(0)
{
    socket = nullptr;
    reply = nullptr;
    state = QHttpSocketEngine::None;
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  from src/network/socket/qhttpsocketengine.cpp, line 813, as _ZN24QHttpSocketEnginePrivateD1Ev
#if !defined(QT_NO_NETWORKPROXY)
inline QHttpSocketEnginePrivate::~QHttpSocketEnginePrivate()
{
}
#endif  // !defined(QT_NO_NETWORKPROXY)
//  -----------------------------------------------------------------------

//  QHttpSocketEngine *QHttpSocketEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QHttpSocketEngine *ritual_ZN24QHttpSocketEnginePrivate6q_funcEv(
    QHttpSocketEnginePrivate *self) {
  return self->q_func();
}

//  const QHttpSocketEngine *QHttpSocketEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHttpSocketEngine *ritual_ZNK24QHttpSocketEnginePrivate6q_funcEv(
    const QHttpSocketEnginePrivate *self) {
  return self->q_func();
}

//  QHttpSocketEnginePrivate::QHttpSocketEnginePrivate()
extern "C" Q_DECL_EXPORT
QHttpSocketEnginePrivate *ritual_ZN24QHttpSocketEnginePrivateC1Ev() {
  return new QHttpSocketEnginePrivate();
}

//  QHttpSocketEnginePrivate::~QHttpSocketEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QHttpSocketEnginePrivateD1Ev(
    QHttpSocketEnginePrivate *self) {
  delete self;
}

#endif  // !defined(QT_NO_NETWORKPROXY)
#endif  // QT_CONFIG(http)
