//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnativesocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractsocketengine_p.h"
#include "qnativesocketengine_p.h"
#include "qmutex.h"
#include "qnetworkproxy.h"
#include "qnativesocketengine_p_p.h"
#include <qabstracteventdispatcher.h>
#include <qsocketnotifier.h>
#include <qnetworkinterface.h>
#include <private/qthread_p.h>
#include <private/qobject_p.h>
#if !defined(QT_NO_NETWORKPROXY)
# include "qnetworkproxy.h"
# include "qabstractsocket.h"
# include "qtcpserver.h"
#endif
#if !defined(QT_NO_SCTP)
# include "qsctpserver.h"
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qabstractsocketengine.cpp, line 144, as _ZN21QAbstractSocketEngine22connectionNotificationEv
inline void QAbstractSocketEngine::connectionNotification()
{
    if (QAbstractSocketEngineReceiver *receiver = d_func()->receiver)
        receiver->connectionNotification();
}

//  from src/network/socket/qnativesocketengine.cpp, line 188, as _ZNK26QNativeSocketEnginePrivate8setErrorEN15QAbstractSocket11SocketErrorENS_11ErrorStringE
inline void QNativeSocketEnginePrivate::setError(QAbstractSocket::SocketError error, ErrorString errorString) const
{
    if (hasSetSocketError) {
        // Only set socket errors once for one engine; expect the
        // socket to recreate its engine after an error. Note: There's
        // one exception: SocketError(11) bypasses this as it's purely
        // a temporary internal error condition.
        // Another exception is the way the waitFor*() functions set
        // an error when a timeout occurs. After the call to setError()
        // they reset the hasSetSocketError to false
        return;
    }
    if (error != QAbstractSocket::SocketError(11))
        hasSetSocketError = true;

    socketError = error;

    switch (errorString) {
    case NonBlockingInitFailedErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unable to initialize non-blocking socket");
        break;
    case BroadcastingInitFailedErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unable to initialize broadcast socket");
        break;
    // should not happen anymore
    case NoIpV6ErrorString:
        socketErrorString = QNativeSocketEngine::tr("Attempt to use IPv6 socket on a platform with no IPv6 support");
        break;
    case RemoteHostClosedErrorString:
        socketErrorString = QNativeSocketEngine::tr("The remote host closed the connection");
        break;
    case TimeOutErrorString:
        socketErrorString = QNativeSocketEngine::tr("Network operation timed out");
        break;
    case ResourceErrorString:
        socketErrorString = QNativeSocketEngine::tr("Out of resources");
        break;
    case OperationUnsupportedErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unsupported socket operation");
        break;
    case ProtocolUnsupportedErrorString:
        socketErrorString = QNativeSocketEngine::tr("Protocol type not supported");
        break;
    case InvalidSocketErrorString:
        socketErrorString = QNativeSocketEngine::tr("Invalid socket descriptor");
        break;
    case HostUnreachableErrorString:
        socketErrorString = QNativeSocketEngine::tr("Host unreachable");
        break;
    case NetworkUnreachableErrorString:
        socketErrorString = QNativeSocketEngine::tr("Network unreachable");
        break;
    case AccessErrorString:
        socketErrorString = QNativeSocketEngine::tr("Permission denied");
        break;
    case ConnectionTimeOutErrorString:
        socketErrorString = QNativeSocketEngine::tr("Connection timed out");
        break;
    case ConnectionRefusedErrorString:
        socketErrorString = QNativeSocketEngine::tr("Connection refused");
        break;
    case AddressInuseErrorString:
        socketErrorString = QNativeSocketEngine::tr("The bound address is already in use");
        break;
    case AddressNotAvailableErrorString:
        socketErrorString = QNativeSocketEngine::tr("The address is not available");
        break;
    case AddressProtectedErrorString:
        socketErrorString = QNativeSocketEngine::tr("The address is protected");
        break;
    case DatagramTooLargeErrorString:
        socketErrorString = QNativeSocketEngine::tr("Datagram was too large to send");
        break;
    case SendDatagramErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unable to send a message");
        break;
    case ReceiveDatagramErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unable to receive a message");
        break;
    case WriteErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unable to write");
        break;
    case ReadErrorString:
        socketErrorString = QNativeSocketEngine::tr("Network error");
        break;
    case PortInuseErrorString:
        socketErrorString = QNativeSocketEngine::tr("Another socket is already listening on the same port");
        break;
    case NotSocketErrorString:
        socketErrorString = QNativeSocketEngine::tr("Operation on non-socket");
        break;
    case InvalidProxyTypeString:
        socketErrorString = QNativeSocketEngine::tr("The proxy type is invalid for this operation");
        break;
    case TemporaryErrorString:
        socketErrorString = QNativeSocketEngine::tr("Temporary error");
        break;
    case NetworkDroppedConnectionErrorString:
        socketErrorString = QNativeSocketEngine::tr("Network dropped connection on reset");
        break;
    case ConnectionResetErrorString:
        socketErrorString = QNativeSocketEngine::tr("Connection reset by peer");
        break;
    case UnknownSocketErrorString:
        socketErrorString = QNativeSocketEngine::tr("Unknown error");
        break;
    }
}

//  from src/network/socket/qnativesocketengine.cpp, line 398, as _ZN19QNativeSocketEngineD1Ev
inline QNativeSocketEngine::~QNativeSocketEngine()
{
    close();
}

//  from src/network/socket/qnativesocketengine.cpp, line 414, as _ZN19QNativeSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE
inline bool QNativeSocketEngine::initialize(QAbstractSocket::SocketType socketType, QAbstractSocket::NetworkLayerProtocol protocol)
{
    Q_D(QNativeSocketEngine);
    if (isValid())
        close();

    // Create the socket
    if (!d->createNewSocket(socketType, protocol)) {
#if defined (QNATIVESOCKETENGINE_DEBUG)
        QString typeStr = "UnknownSocketType"_L1;
        if (socketType == QAbstractSocket::TcpSocket) typeStr = "TcpSocket"_L1;
        else if (socketType == QAbstractSocket::UdpSocket) typeStr = "UdpSocket"_L1;
        else if (socketType == QAbstractSocket::SctpSocket) typeStr = "SctpSocket"_L1;
        QString protocolStr = "UnknownProtocol"_L1;
        if (protocol == QAbstractSocket::IPv4Protocol) protocolStr = "IPv4Protocol"_L1;
        else if (protocol == QAbstractSocket::IPv6Protocol) protocolStr = "IPv6Protocol"_L1;
        qDebug("QNativeSocketEngine::initialize(type == %s, protocol == %s) failed: %s",
               typeStr.toLatin1().constData(), protocolStr.toLatin1().constData(), d->socketErrorString.toLatin1().constData());
#endif
        return false;
    }

    if (socketType == QAbstractSocket::UdpSocket) {
        // Set the broadcasting flag if it's a UDP socket.
        // IPv6 does not support broadcast — only set option for IPv4
        if (protocol != QAbstractSocket::IPv6Protocol) {
            if (!setOption(BroadcastSocketOption, 1)) {
                d->setError(QAbstractSocket::UnsupportedSocketOperationError,
                            QNativeSocketEnginePrivate::BroadcastingInitFailedErrorString);
                close();
                return false;
            }
        }

        // Set some extra flags that are interesting to us, but accept failure
        setOption(ReceivePacketInformation, 1);
        setOption(ReceiveHopLimit, 1);
    }


#ifndef Q_OS_WASM
    // Make sure we receive out-of-band data
    if (socketType == QAbstractSocket::TcpSocket
        && !setOption(ReceiveOutOfBandData, 1)) {
        qWarning("QNativeSocketEngine::initialize unable to inline out-of-band data");
    }
#endif

    // Before Qt 4.6, we always set the send and receive buffer size to 49152 as
    // this was found to be an optimal value. However, modern OS
    // all have some kind of auto tuning for this and we therefore don't set
    // this explicitly anymore.
    // If it introduces any performance regressions for Qt 4.6.x (x > 0) then
    // it will be put back in.
    //
    // You can use tests/manual/qhttpnetworkconnection to test HTTP download speed
    // with this.
    //
    // pre-4.6:
    // setReceiveBufferSize(49152);
    // setSendBufferSize(49152);

    return true;
}

//  from src/network/socket/qnativesocketengine.cpp, line 489, as _ZN19QNativeSocketEngine10initializeExN15QAbstractSocket11SocketStateE
inline bool QNativeSocketEngine::initialize(qintptr socketDescriptor, QAbstractSocket::SocketState socketState)
{
    Q_D(QNativeSocketEngine);

    if (isValid())
        close();

    d->socketDescriptor = socketDescriptor;

    // determine socket type and protocol
    if (!d->fetchConnectionParameters()) {
#if defined (QNATIVESOCKETENGINE_DEBUG)
        qDebug() << "QNativeSocketEngine::initialize(socketDescriptor) failed:"
                 << socketDescriptor << d->socketErrorString;
#endif
        d->socketDescriptor = -1;
        return false;
    }

    if (d->socketType != QAbstractSocket::UnknownSocketType) {
        // Make the socket nonblocking.
        if (!setOption(NonBlockingSocketOption, 1)) {
            d->setError(QAbstractSocket::UnsupportedSocketOperationError,
                QNativeSocketEnginePrivate::NonBlockingInitFailedErrorString);
            close();
            return false;
        }

        // Set the broadcasting flag if it's a UDP socket.
        if (d->socketType == QAbstractSocket::UdpSocket
            && d->socketProtocol != QAbstractSocket::IPv6Protocol
            && !setOption(BroadcastSocketOption, 1)) {
            d->setError(QAbstractSocket::UnsupportedSocketOperationError,
                QNativeSocketEnginePrivate::BroadcastingInitFailedErrorString);
            close();
            return false;
        }
    }

    d->socketState = socketState;
    return true;
}

//  from src/network/socket/qnativesocketengine.cpp, line 547, as _ZNK19QNativeSocketEngine16socketDescriptorEv
inline qintptr QNativeSocketEngine::socketDescriptor() const
{
    Q_D(const QNativeSocketEngine);
    return d->socketDescriptor;
}

//  from src/network/socket/qnativesocketengine.cpp, line 537, as _ZNK19QNativeSocketEngine7isValidEv
inline bool QNativeSocketEngine::isValid() const
{
    Q_D(const QNativeSocketEngine);
    return d->socketDescriptor != -1;
}

//  from src/network/socket/qnativesocketengine.cpp, line 621, as _ZN19QNativeSocketEngine19connectToHostByNameERK7QStringt
inline bool QNativeSocketEngine::connectToHostByName(const QString &name, quint16 port)
{
    Q_UNUSED(name);
    Q_UNUSED(port);
    Q_D(QNativeSocketEngine);
    d->setError(QAbstractSocket::UnsupportedSocketOperationError,
                QNativeSocketEnginePrivate::OperationUnsupportedErrorString);
    return false;
}

//  from src/network/socket/qnativesocketengine.cpp, line 940, as _ZN19QNativeSocketEngine5closeEv
inline void QNativeSocketEngine::close()
{
    Q_D(QNativeSocketEngine);
    if (d->readNotifier)
        d->readNotifier->setEnabled(false);
    if (d->writeNotifier)
        d->writeNotifier->setEnabled(false);
    if (d->exceptNotifier)
        d->exceptNotifier->setEnabled(false);

    if (d->socketDescriptor != -1) {
        d->nativeClose();
        d->socketDescriptor = -1;
    }
    d->socketState = QAbstractSocket::UnconnectedState;
    d->hasSetSocketError = false;
    d->localPort = 0;
    d->localAddress.clear();
    d->peerPort = 0;
    d->peerAddress.clear();
    d->inboundStreamCount = d->outboundStreamCount = 0;
    if (d->readNotifier) {
        delete d->readNotifier;
        d->readNotifier = nullptr;
    }
    if (d->writeNotifier) {
        delete d->writeNotifier;
        d->writeNotifier = nullptr;
    }
    if (d->exceptNotifier) {
        delete d->exceptNotifier;
        d->exceptNotifier = nullptr;
    }
}

//  from src/network/socket/qnativesocketengine.cpp, line 898, as _ZNK19QNativeSocketEngine12bytesToWriteEv
inline qint64 QNativeSocketEngine::bytesToWrite() const
{
    return 0;
}

//  from src/network/socket/qnativesocketengine.cpp, line 1213, as _ZNK19QNativeSocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE
inline int QNativeSocketEngine::option(SocketOption socketOption) const
{
    Q_D(const QNativeSocketEngine);
    return d->option(socketOption);
}

//  from src/network/socket/qnativesocketengine.cpp, line 1204, as _ZN19QNativeSocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi
inline bool QNativeSocketEngine::setOption(SocketOption option, int value)
{
    Q_D(QNativeSocketEngine);
    return d->setOption(option, value);
}

//  from src/network/socket/qnativesocketengine.cpp, line 1219, as _ZNK19QNativeSocketEngine25isReadNotificationEnabledEv
inline bool QNativeSocketEngine::isReadNotificationEnabled() const
{
    Q_D(const QNativeSocketEngine);
    return d->readNotifier && d->readNotifier->isEnabled();
}

//  from src/network/socket/qnativesocketengine.cpp, line 1325, as _ZNK19QNativeSocketEngine26isWriteNotificationEnabledEv
inline bool QNativeSocketEngine::isWriteNotificationEnabled() const
{
    Q_D(const QNativeSocketEngine);
    return d->writeNotifier && d->writeNotifier->isEnabled();
}

//  from src/network/socket/qnativesocketengine.cpp, line 1342, as _ZNK19QNativeSocketEngine30isExceptionNotificationEnabledEv
inline bool QNativeSocketEngine::isExceptionNotificationEnabled() const
{
    Q_D(const QNativeSocketEngine);
    return d->exceptNotifier && d->exceptNotifier->isEnabled();
}
//  -----------------------------------------------------------------------

//  A QNativeSocketEngine that Python can take functions over in. Every QNativeSocketEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQNativeSocketEngineCall0)(const void *, int, int, int *);
typedef bool (*CuteQNativeSocketEngineCall1)(const void *, qintptr, int, int *);
typedef qintptr (*CuteQNativeSocketEngineCall2)(const void *, int *);
typedef bool (*CuteQNativeSocketEngineCall3)(const void *, int *);
typedef bool (*CuteQNativeSocketEngineCall4)(const void *, const QHostAddress *, quint16, int *);
typedef bool (*CuteQNativeSocketEngineCall5)(const void *, const QString *, quint16, int *);
typedef bool (*CuteQNativeSocketEngineCall6)(const void *, const QHostAddress *, quint16, int *);
typedef bool (*CuteQNativeSocketEngineCall7)(const void *, int, int *);
typedef qintptr (*CuteQNativeSocketEngineCall8)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall9)(const void *, int *);
typedef qint64 (*CuteQNativeSocketEngineCall10)(const void *, int *);
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef bool (*CuteQNativeSocketEngineCall11)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef bool (*CuteQNativeSocketEngineCall12)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef const QNetworkInterface * (*CuteQNativeSocketEngineCall13)(const void *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
typedef bool (*CuteQNativeSocketEngineCall14)(const void *, const QNetworkInterface *, int *);
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
typedef bool (*CuteQNativeSocketEngineCall15)(const void *, int *);
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
typedef qint64 (*CuteQNativeSocketEngineCall16)(const void *, int *);
#endif  // !defined(QT_NO_UDPSOCKET)
typedef qint64 (*CuteQNativeSocketEngineCall17)(const void *, int *);
typedef int (*CuteQNativeSocketEngineCall18)(const void *, int, int *);
typedef bool (*CuteQNativeSocketEngineCall19)(const void *, int, int, int *);
typedef bool (*CuteQNativeSocketEngineCall20)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall21)(const void *, bool, int *);
typedef bool (*CuteQNativeSocketEngineCall22)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall23)(const void *, bool, int *);
typedef bool (*CuteQNativeSocketEngineCall24)(const void *, int *);
typedef void (*CuteQNativeSocketEngineCall25)(const void *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNativeSocketEngineCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNativeSocketEngineCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNativeSocketEngineCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNativeSocketEngine : public QNativeSocketEngine {
public:
  using QNativeSocketEngine::QNativeSocketEngine;
  void *taken[33] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11SocketStateE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine16socketDescriptorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine7isValidEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine4bindERK12QHostAddresst")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6listenEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6acceptEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine5closeEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine14bytesAvailableEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine18multicastInterfaceEv")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkInterface")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_UDPSOCKET)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine12bytesToWriteEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb")) {
      taken[25] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QNativeSocketEngine::initialize(QAbstractSocket::SocketType
  //      type, QAbstractSocket::NetworkLayerProtocol protocol)
  bool initialize(
      QAbstractSocket::SocketType type,
      QAbstractSocket::NetworkLayerProtocol protocol) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNativeSocketEngineCall0 call = reinterpret_cast<CuteQNativeSocketEngineCall0>(taken[0]);
      bool given = call(this, static_cast<int>(type), static_cast<int>(protocol), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::initialize(type, protocol);
  }

  //  bool QNativeSocketEngine::initialize(qintptr socketDescriptor,
  //      QAbstractSocket::SocketState socketState)
  bool initialize(
      qintptr socketDescriptor,
      QAbstractSocket::SocketState socketState) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNativeSocketEngineCall1 call = reinterpret_cast<CuteQNativeSocketEngineCall1>(taken[1]);
      bool given = call(this, socketDescriptor, static_cast<int>(socketState), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::initialize(socketDescriptor, socketState);
  }

  //  qintptr QNativeSocketEngine::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNativeSocketEngineCall2 call = reinterpret_cast<CuteQNativeSocketEngineCall2>(taken[2]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::socketDescriptor();
  }

  //  bool QNativeSocketEngine::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQNativeSocketEngineCall3 call = reinterpret_cast<CuteQNativeSocketEngineCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isValid();
  }

  //  bool QNativeSocketEngine::connectToHost(const QHostAddress &address,
  //      quint16 port)
  bool connectToHost(const QHostAddress &address, quint16 port) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNativeSocketEngineCall4 call = reinterpret_cast<CuteQNativeSocketEngineCall4>(taken[4]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::connectToHost(address, port);
  }

  //  bool QNativeSocketEngine::connectToHostByName(const QString &name,
  //      quint16 port)
  bool connectToHostByName(const QString &name, quint16 port) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNativeSocketEngineCall5 call = reinterpret_cast<CuteQNativeSocketEngineCall5>(taken[5]);
      bool given = call(this, &name, port, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::connectToHostByName(name, port);
  }

  //  bool QNativeSocketEngine::bind(const QHostAddress &address, quint16
  //      port)
  bool bind(const QHostAddress &address, quint16 port) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNativeSocketEngineCall6 call = reinterpret_cast<CuteQNativeSocketEngineCall6>(taken[6]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::bind(address, port);
  }

  //  bool QNativeSocketEngine::listen(int backlog)
  bool listen(int backlog) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNativeSocketEngineCall7 call = reinterpret_cast<CuteQNativeSocketEngineCall7>(taken[7]);
      bool given = call(this, backlog, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::listen(backlog);
  }

  //  qintptr QNativeSocketEngine::accept()
  qintptr accept() override {
    if (taken[8]) {
      int handled = 0;
      CuteQNativeSocketEngineCall8 call = reinterpret_cast<CuteQNativeSocketEngineCall8>(taken[8]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::accept();
  }

  //  void QNativeSocketEngine::close()
  void close() override {
    if (taken[9]) {
      int handled = 0;
      CuteQNativeSocketEngineCall9 call = reinterpret_cast<CuteQNativeSocketEngineCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::close();
  }

  //  qint64 QNativeSocketEngine::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQNativeSocketEngineCall10 call = reinterpret_cast<CuteQNativeSocketEngineCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::bytesAvailable();
  }

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  bool QNativeSocketEngine::joinMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool joinMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNativeSocketEngineCall11 call = reinterpret_cast<CuteQNativeSocketEngineCall11>(taken[11]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::joinMulticastGroup(groupAddress, iface);
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  bool QNativeSocketEngine::leaveMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool leaveMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNativeSocketEngineCall12 call = reinterpret_cast<CuteQNativeSocketEngineCall12>(taken[12]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::leaveMulticastGroup(groupAddress, iface);
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  QNetworkInterface QNativeSocketEngine::multicastInterface() const
  QNetworkInterface multicastInterface() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQNativeSocketEngineCall13 call = reinterpret_cast<CuteQNativeSocketEngineCall13>(taken[13]);
      const QNetworkInterface * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNativeSocketEngine::multicastInterface();
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
  //  bool QNativeSocketEngine::setMulticastInterface(const
  //      QNetworkInterface &iface)
  bool setMulticastInterface(const QNetworkInterface &iface) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNativeSocketEngineCall14 call = reinterpret_cast<CuteQNativeSocketEngineCall14>(taken[14]);
      bool given = call(this, &iface, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::setMulticastInterface(iface);
  }
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
  //  bool QNativeSocketEngine::hasPendingDatagrams() const
  bool hasPendingDatagrams() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQNativeSocketEngineCall15 call = reinterpret_cast<CuteQNativeSocketEngineCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::hasPendingDatagrams();
  }
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
  //  qint64 QNativeSocketEngine::pendingDatagramSize() const
  qint64 pendingDatagramSize() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQNativeSocketEngineCall16 call = reinterpret_cast<CuteQNativeSocketEngineCall16>(taken[16]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::pendingDatagramSize();
  }
#endif  // !defined(QT_NO_UDPSOCKET)

  //  qint64 QNativeSocketEngine::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQNativeSocketEngineCall17 call = reinterpret_cast<CuteQNativeSocketEngineCall17>(taken[17]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::bytesToWrite();
  }

  //  int QNativeSocketEngine::option(SocketOption option) const
  int option(QAbstractSocketEngine::SocketOption option) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQNativeSocketEngineCall18 call = reinterpret_cast<CuteQNativeSocketEngineCall18>(taken[18]);
      int given = call(this, static_cast<int>(option), &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::option(option);
  }

  //  bool QNativeSocketEngine::setOption(SocketOption option, int value)
  bool setOption(
      QAbstractSocketEngine::SocketOption option,
      int value) override {
    if (taken[19]) {
      int handled = 0;
      CuteQNativeSocketEngineCall19 call = reinterpret_cast<CuteQNativeSocketEngineCall19>(taken[19]);
      bool given = call(this, static_cast<int>(option), value, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::setOption(option, value);
  }

  //  bool QNativeSocketEngine::isReadNotificationEnabled() const
  bool isReadNotificationEnabled() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQNativeSocketEngineCall20 call = reinterpret_cast<CuteQNativeSocketEngineCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isReadNotificationEnabled();
  }

  //  void QNativeSocketEngine::setReadNotificationEnabled(bool enable)
  void setReadNotificationEnabled(bool enable) override {
    if (taken[21]) {
      int handled = 0;
      CuteQNativeSocketEngineCall21 call = reinterpret_cast<CuteQNativeSocketEngineCall21>(taken[21]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::setReadNotificationEnabled(enable);
  }

  //  bool QNativeSocketEngine::isWriteNotificationEnabled() const
  bool isWriteNotificationEnabled() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQNativeSocketEngineCall22 call = reinterpret_cast<CuteQNativeSocketEngineCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isWriteNotificationEnabled();
  }

  //  void QNativeSocketEngine::setWriteNotificationEnabled(bool enable)
  void setWriteNotificationEnabled(bool enable) override {
    if (taken[23]) {
      int handled = 0;
      CuteQNativeSocketEngineCall23 call = reinterpret_cast<CuteQNativeSocketEngineCall23>(taken[23]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::setWriteNotificationEnabled(enable);
  }

  //  bool QNativeSocketEngine::isExceptionNotificationEnabled() const
  bool isExceptionNotificationEnabled() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQNativeSocketEngineCall24 call = reinterpret_cast<CuteQNativeSocketEngineCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNativeSocketEngine::isExceptionNotificationEnabled();
  }

  //  void QNativeSocketEngine::setExceptionNotificationEnabled(bool
  //      enable)
  void setExceptionNotificationEnabled(bool enable) override {
    if (taken[25]) {
      int handled = 0;
      CuteQNativeSocketEngineCall25 call = reinterpret_cast<CuteQNativeSocketEngineCall25>(taken[25]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QNativeSocketEngine::setExceptionNotificationEnabled(enable);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQNativeSocketEngineCall26 call = reinterpret_cast<CuteQNativeSocketEngineCall26>(taken[26]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQNativeSocketEngineCall27 call = reinterpret_cast<CuteQNativeSocketEngineCall27>(taken[27]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQNativeSocketEngineCall28 call = reinterpret_cast<CuteQNativeSocketEngineCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQNativeSocketEngineCall29 call = reinterpret_cast<CuteQNativeSocketEngineCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQNativeSocketEngineCall30 call = reinterpret_cast<CuteQNativeSocketEngineCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQNativeSocketEngineCall31 call = reinterpret_cast<CuteQNativeSocketEngineCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[32]) {
      int handled = 0;
      CuteQNativeSocketEngineCall32 call = reinterpret_cast<CuteQNativeSocketEngineCall32>(taken[32]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNativeSocketEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QNativeSocketEngine10metaObjectEv(
    const QNativeSocketEngine *self) {
  return self->metaObject();
}

//  QNativeSocketEngine::~QNativeSocketEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNativeSocketEngineD1Ev(QNativeSocketEngine *self) {
  delete self;
}

//  bool QNativeSocketEngine::initialize(QAbstractSocket::SocketType type,
//      QAbstractSocket::NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNativeSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE(
    QNativeSocketEngine *self,
    QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  return self->initialize(type, protocol);
}

//  bool QNativeSocketEngine::initialize(qintptr socketDescriptor,
//      QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNativeSocketEngine10initializeExN15QAbstractSocket11SocketStateE(
    QNativeSocketEngine *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState socketState) {
  return self->initialize(socketDescriptor, socketState);
}

//  qintptr QNativeSocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK19QNativeSocketEngine16socketDescriptorEv(
    const QNativeSocketEngine *self) {
  return self->socketDescriptor();
}

//  bool QNativeSocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNativeSocketEngine7isValidEv(
    const QNativeSocketEngine *self) {
  return self->isValid();
}

//  bool QNativeSocketEngine::connectToHostByName(const QString &name,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNativeSocketEngine19connectToHostByNameERK7QStringt(
    QNativeSocketEngine *self,
    const QString *name,
    quint16 port) {
  return self->connectToHostByName(*name, port);
}

//  void QNativeSocketEngine::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QNativeSocketEngine5closeEv(QNativeSocketEngine *self) {
  self->close();
}

//  qint64 QNativeSocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QNativeSocketEngine12bytesToWriteEv(
    const QNativeSocketEngine *self) {
  return self->bytesToWrite();
}

//  int QNativeSocketEngine::option(SocketOption option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QNativeSocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE(
    const QNativeSocketEngine *self,
    QAbstractSocketEngine::SocketOption option) {
  return self->option(option);
}

//  bool QNativeSocketEngine::setOption(SocketOption option, int value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QNativeSocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi(
    QNativeSocketEngine *self,
    QAbstractSocketEngine::SocketOption option,
    int value) {
  return self->setOption(option, value);
}

//  bool QNativeSocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNativeSocketEngine25isReadNotificationEnabledEv(
    const QNativeSocketEngine *self) {
  return self->isReadNotificationEnabled();
}

//  bool QNativeSocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNativeSocketEngine26isWriteNotificationEnabledEv(
    const QNativeSocketEngine *self) {
  return self->isWriteNotificationEnabled();
}

//  bool QNativeSocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QNativeSocketEngine30isExceptionNotificationEnabledEv(
    const QNativeSocketEngine *self) {
  return self->isExceptionNotificationEnabled();
}

//  QNativeSocketEnginePrivate *QNativeSocketEngine::d_func()
extern "C" Q_DECL_EXPORT
QNativeSocketEnginePrivate *ritual_ZN19QNativeSocketEngine6d_funcEv(
    QNativeSocketEngine *self) {
  return self->d_func();
}

//  const QNativeSocketEnginePrivate *QNativeSocketEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QNativeSocketEnginePrivate *ritual_ZNK19QNativeSocketEngine6d_funcEv(
    const QNativeSocketEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNativeSocketEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNativeSocketEngine(
    QNativeSocketEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNativeSocketEngine *>(self)->take(key, call);
}

//  qintptr QNativeSocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK19QNativeSocketEngine16socketDescriptorEv(
    const QNativeSocketEngine *self) {
  return self->QNativeSocketEngine::socketDescriptor();
}

//  bool QNativeSocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QNativeSocketEngine7isValidEv(
    const QNativeSocketEngine *self) {
  return self->QNativeSocketEngine::isValid();
}

//  qint64 QNativeSocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QNativeSocketEngine12bytesToWriteEv(
    const QNativeSocketEngine *self) {
  return self->QNativeSocketEngine::bytesToWrite();
}

//  bool QNativeSocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QNativeSocketEngine25isReadNotificationEnabledEv(
    const QNativeSocketEngine *self) {
  return self->QNativeSocketEngine::isReadNotificationEnabled();
}

//  bool QNativeSocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QNativeSocketEngine26isWriteNotificationEnabledEv(
    const QNativeSocketEngine *self) {
  return self->QNativeSocketEngine::isWriteNotificationEnabled();
}

//  bool QNativeSocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QNativeSocketEngine30isExceptionNotificationEnabledEv(
    const QNativeSocketEngine *self) {
  return self->QNativeSocketEngine::isExceptionNotificationEnabled();
}
