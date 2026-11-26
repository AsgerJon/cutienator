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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/network/socket/qsocks5socketengine.cpp, line 47, as local:qsocks5socketengine.cpp:S5_VERSION_5
#define S5_VERSION_5 0x05

//  from src/network/socket/qsocks5socketengine.cpp, line 48, as local:qsocks5socketengine.cpp:S5_CONNECT
#define S5_CONNECT 0x01

//  from src/network/socket/qsocks5socketengine.cpp, line 49, as local:qsocks5socketengine.cpp:S5_BIND
#define S5_BIND 0x02

//  from src/network/socket/qsocks5socketengine.cpp, line 50, as local:qsocks5socketengine.cpp:S5_UDP_ASSOCIATE
#define S5_UDP_ASSOCIATE 0x03

//  from src/network/socket/qsocks5socketengine.cpp, line 72, as local:qsocks5socketengine.cpp:QSOCKS5_D_DEBUG
#if defined(QSOCKS5SOCKETLAYER_DEBUG)
#  define QSOCKS5_D_DEBUG qDebug() << q_ptr
#endif  // defined(QSOCKS5SOCKETLAYER_DEBUG)

//  from src/network/socket/qsocks5socketengine.cpp, line 73, as local:qsocks5socketengine.cpp:QSOCKS5_DEBUG
#if defined(QSOCKS5SOCKETLAYER_DEBUG)
#  define QSOCKS5_DEBUG qDebug() << "[QSocks5]"
#endif  // defined(QSOCKS5SOCKETLAYER_DEBUG)

//  from src/network/socket/qsocks5socketengine.cpp, line 261, as local:qsocks5socketengine.cpp:QSocks5Data
struct QSocks5Data
{
    QTcpSocket *controlSocket;
    QSocks5Authenticator *authenticator;
};

//  from src/network/socket/qsocks5socketengine.cpp, line 267, as local:qsocks5socketengine.cpp:QSocks5ConnectData
struct QSocks5ConnectData : public QSocks5Data
{
    QRingBuffer readBuffer;
};

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
