//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/private/qnativesocketengine_p_p.h>
#include <QtCore/qabstracteventdispatcher.h>
#include <QtCore/qsocketnotifier.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/private/qthread_p.h>
#include <QtCore/private/qobject_p.h>
#if !defined(QT_NO_NETWORKPROXY)
# include <QtNetwork/qnetworkproxy.h>
# include <QtNetwork/qabstractsocket.h>
# include <QtNetwork/qtcpserver.h>
#endif
#if !defined(QT_NO_SCTP)
# include <QtNetwork/qsctpserver.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  from src/network/socket/qnativesocketengine.cpp, line 164, as _ZN26QNativeSocketEnginePrivateC1Ev
#if defined(Q_OS_LINUX)
inline QNativeSocketEnginePrivate::QNativeSocketEnginePrivate() :
    socketDescriptor(-1),
    readNotifier(nullptr),
    writeNotifier(nullptr),
    exceptNotifier(nullptr)
{
#if defined(Q_OS_WIN)
    QSysInfo::machineHostName();        // this initializes ws2_32.dll
#endif
}
#endif  // defined(Q_OS_LINUX)

//  from src/network/socket/qnativesocketengine.cpp, line 178, as _ZN26QNativeSocketEnginePrivateD1Ev
inline QNativeSocketEnginePrivate::~QNativeSocketEnginePrivate()
{
}

//  from src/network/socket/qnativesocketengine.cpp, line 304, as _ZNK26QNativeSocketEnginePrivate21adjustAddressProtocolERK12QHostAddress
inline QHostAddress QNativeSocketEnginePrivate::adjustAddressProtocol(const QHostAddress &address) const
{
    QAbstractSocket::NetworkLayerProtocol targetProtocol = socketProtocol;
    if (Q_LIKELY(targetProtocol == QAbstractSocket::UnknownNetworkLayerProtocol))
        return address;

    QAbstractSocket::NetworkLayerProtocol sourceProtocol = address.protocol();

    if (targetProtocol == QAbstractSocket::AnyIPProtocol)
        targetProtocol = QAbstractSocket::IPv6Protocol;
    if (targetProtocol == QAbstractSocket::IPv6Protocol && sourceProtocol == QAbstractSocket::IPv4Protocol) {
        // convert to IPv6 v4-mapped address. This always works
        return QHostAddress(address.toIPv6Address());
    }

    if (targetProtocol == QAbstractSocket::IPv4Protocol && sourceProtocol == QAbstractSocket::IPv6Protocol) {
        // convert to IPv4 if the source is a v4-mapped address
        quint32 ip4 = address.toIPv4Address();
        if (ip4)
            return QHostAddress(ip4);
    }

    return address;
}
//  -----------------------------------------------------------------------

//  QNativeSocketEngine *QNativeSocketEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QNativeSocketEngine *ritual_ZN26QNativeSocketEnginePrivate6q_funcEv(
    QNativeSocketEnginePrivate *self) {
  return self->q_func();
}

//  const QNativeSocketEngine *QNativeSocketEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QNativeSocketEngine *ritual_ZNK26QNativeSocketEnginePrivate6q_funcEv(
    const QNativeSocketEnginePrivate *self) {
  return self->q_func();
}

//  QNativeSocketEnginePrivate::QNativeSocketEnginePrivate()
extern "C" Q_DECL_EXPORT
QNativeSocketEnginePrivate *ritual_ZN26QNativeSocketEnginePrivateC1Ev() {
  return new QNativeSocketEnginePrivate();
}

//  QNativeSocketEnginePrivate::~QNativeSocketEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNativeSocketEnginePrivateD1Ev(
    QNativeSocketEnginePrivate *self) {
  delete self;
}

//  QHostAddress QNativeSocketEnginePrivate::adjustAddressProtocol(const
//      QHostAddress &address) const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK26QNativeSocketEnginePrivate21adjustAddressProtocolERK12QHostAddress(
    const QNativeSocketEnginePrivate *self,
    const QHostAddress *address) {
  return new QHostAddress(self->adjustAddressProtocol(*address));
}

//  void QNativeSocketEnginePrivate::setPortAndAddress(quint16 port, const
//      QHostAddress &address, qt_sockaddr *aa, socklen_t *sockAddrSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QNativeSocketEnginePrivate17setPortAndAddressEtRK12QHostAddressP11qt_sockaddrPj(
    QNativeSocketEnginePrivate *self,
    quint16 port,
    const QHostAddress *address,
    qt_sockaddr *aa,
    socklen_t *sockAddrSize) {
  self->setPortAndAddress(port, *address, aa, sockAddrSize);
}
