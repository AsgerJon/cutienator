//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/private/qsocks5socketengine_p.h>
#include <QtNetwork/qtcpsocket.h>
#include <QtNetwork/qudpsocket.h>
#include <QtNetwork/qtcpserver.h>
#include <QtCore/qdebug.h>
#include <QtCore/qhash.h>
#include <QtCore/qqueue.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qelapsedtimer.h>
#include <QtCore/qmutex.h>
#include <QtCore/qthread.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qauthenticator.h>
#include <QtCore/private/qiodevice_p.h>
#include <QtCore/private/qringbuffer_p.h>
#include <QtCore/qendian.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qbasictimer.h>
#include <QtCore/qpointer.h>
#include <memory>
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

//  from src/network/socket/qsocks5socketengine.cpp, line 486, as _ZN26QSocks5SocketEnginePrivateC1Ev
inline QSocks5SocketEnginePrivate::QSocks5SocketEnginePrivate()
    : socks5State(Uninitialized)
    , readNotificationEnabled(false)
    , writeNotificationEnabled(false)
    , exceptNotificationEnabled(false)
    , socketDescriptor(-1)
    , data(nullptr)
    , connectData(nullptr)
#ifndef QT_NO_UDPSOCKET
    , udpData(nullptr)
#endif
    , bindData(nullptr)
    , readNotificationActivated(false)
    , writeNotificationActivated(false)
    , readNotificationPending(false)
    , writeNotificationPending(false)
    , connectionNotificationPending(false)
{
    mode = NoMode;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 507, as _ZN26QSocks5SocketEnginePrivateD1Ev
inline QSocks5SocketEnginePrivate::~QSocks5SocketEnginePrivate()
{
}
//  -----------------------------------------------------------------------

//  QSocks5SocketEngine *QSocks5SocketEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QSocks5SocketEngine *ritual_ZN26QSocks5SocketEnginePrivate6q_funcEv(
    QSocks5SocketEnginePrivate *self) {
  return self->q_func();
}

//  const QSocks5SocketEngine *QSocks5SocketEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSocks5SocketEngine *ritual_ZNK26QSocks5SocketEnginePrivate6q_funcEv(
    const QSocks5SocketEnginePrivate *self) {
  return self->q_func();
}

//  QSocks5SocketEnginePrivate::QSocks5SocketEnginePrivate()
extern "C" Q_DECL_EXPORT
QSocks5SocketEnginePrivate *ritual_ZN26QSocks5SocketEnginePrivateC1Ev() {
  return new QSocks5SocketEnginePrivate();
}

//  QSocks5SocketEnginePrivate::~QSocks5SocketEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QSocks5SocketEnginePrivateD1Ev(
    QSocks5SocketEnginePrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(socks5)
#endif  // QT_CONFIG(socks5)
