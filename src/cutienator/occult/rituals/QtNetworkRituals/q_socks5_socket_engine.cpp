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
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkinterface.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkdatagram_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
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

//  from src/network/socket/qsocks5socketengine.cpp, line 42, as local:qsocks5socketengine.cpp:Q_INIT_CHECK
#define Q_INIT_CHECK(returnValue) do { \

//  from src/network/socket/qsocks5socketengine.cpp, line 71, as local:qsocks5socketengine.cpp:QSOCKS5_Q_DEBUG
#if defined(QSOCKS5SOCKETLAYER_DEBUG)
#  define QSOCKS5_Q_DEBUG qDebug() << this
#endif  // defined(QSOCKS5SOCKETLAYER_DEBUG)

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

//  from src/network/socket/qsocks5socketengine.cpp, line 272, as local:qsocks5socketengine.cpp:QSocks5BindData
struct QSocks5BindData : public QSocks5Data
{
    QHostAddress localAddress;
    quint16 localPort = 0;
    QHostAddress peerAddress;
    quint16 peerPort = 0;
    QElapsedTimer timeStamp;
};

//  from src/network/socket/qsocks5socketengine.cpp, line 281, as local:qsocks5socketengine.cpp:QSocks5RevivedDatagram
struct QSocks5RevivedDatagram
{
    QByteArray data;
    QHostAddress address;
    quint16 port = 0;
};

//  from src/network/socket/qsocks5socketengine.cpp, line 289, as local:qsocks5socketengine.cpp:QSocks5UdpAssociateData
#if !defined(QT_NO_UDPSOCKET)
struct QSocks5UdpAssociateData : public QSocks5Data
{
    QUdpSocket *udpSocket = nullptr;
    QHostAddress associateAddress;
    quint16 associatePort = 0;
    QQueue<QSocks5RevivedDatagram> pendingDatagrams;
};
#endif  // !defined(QT_NO_UDPSOCKET)

//  from src/network/socket/qsocks5socketengine.cpp, line 1062, as _ZNK19QSocks5SocketEngine16socketDescriptorEv
inline qintptr QSocks5SocketEngine::socketDescriptor() const
{
    Q_D(const QSocks5SocketEngine);
    return d->socketDescriptor;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1068, as _ZNK19QSocks5SocketEngine7isValidEv
inline bool QSocks5SocketEngine::isValid() const
{
    Q_D(const QSocks5SocketEngine);
    return d->socketType != QAbstractSocket::UnknownSocketType
           && d->socks5State != QSocks5SocketEnginePrivate::SocksError
           && (d->socketError == QAbstractSocket::UnknownSocketError
               || d->socketError == QAbstractSocket::SocketTimeoutError
               || d->socketError == QAbstractSocket::UnfinishedSocketOperationError);
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1128, as _ZN19QSocks5SocketEngine19connectToHostByNameERK7QStringt
inline bool QSocks5SocketEngine::connectToHostByName(const QString &hostname, quint16 port)
{
    Q_D(QSocks5SocketEngine);

    setPeerAddress(QHostAddress());
    setPeerPort(port);
    d->peerName = hostname;

    return connectInternal();
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1535, as _ZN19QSocks5SocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
inline bool QSocks5SocketEngine::joinMulticastGroup(const QHostAddress &,
                                             const QNetworkInterface &)
{
    setError(QAbstractSocket::UnsupportedSocketOperationError,
             "Operation on socket is not supported"_L1);
    return false;
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

//  from src/network/socket/qsocks5socketengine.cpp, line 1543, as _ZN19QSocks5SocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
inline bool QSocks5SocketEngine::leaveMulticastGroup(const QHostAddress &,
                                              const QNetworkInterface &)
{
    setError(QAbstractSocket::UnsupportedSocketOperationError,
             "Operation on socket is not supported"_L1);
    return false;
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

//  from src/network/socket/qsocks5socketengine.cpp, line 1552, as _ZNK19QSocks5SocketEngine18multicastInterfaceEv
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
inline QNetworkInterface QSocks5SocketEngine::multicastInterface() const
{
    return QNetworkInterface();
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

//  from src/network/socket/qsocks5socketengine.cpp, line 1557, as _ZN19QSocks5SocketEngine21setMulticastInterfaceERK17QNetworkInterface
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
inline bool QSocks5SocketEngine::setMulticastInterface(const QNetworkInterface &)
{
    setError(QAbstractSocket::UnsupportedSocketOperationError,
             "Operation on socket is not supported"_L1);
    return false;
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

//  from src/network/socket/qsocks5socketengine.cpp, line 1656, as _ZNK19QSocks5SocketEngine12bytesToWriteEv
inline qint64 QSocks5SocketEngine::bytesToWrite() const
{
    Q_D(const QSocks5SocketEngine);
    if (d->data && d->data->controlSocket) {
        return d->data->controlSocket->bytesToWrite();
    } else {
        return 0;
    }
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1666, as _ZNK19QSocks5SocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE
inline int QSocks5SocketEngine::option(SocketOption option) const
{
    Q_D(const QSocks5SocketEngine);
    if (d->data && d->data->controlSocket) {
        // convert the enum and call the real socket
        if (option == QAbstractSocketEngine::LowDelayOption)
            return d->data->controlSocket->socketOption(QAbstractSocket::LowDelayOption).toInt();
        if (option == QAbstractSocketEngine::KeepAliveOption)
            return d->data->controlSocket->socketOption(QAbstractSocket::KeepAliveOption).toInt();
    }
    return -1;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1679, as _ZN19QSocks5SocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi
inline bool QSocks5SocketEngine::setOption(SocketOption option, int value)
{
    Q_D(QSocks5SocketEngine);
    if (d->data && d->data->controlSocket) {
        // convert the enum and call the real socket
        if (option == QAbstractSocketEngine::LowDelayOption)
            d->data->controlSocket->setSocketOption(QAbstractSocket::LowDelayOption, value);
        if (option == QAbstractSocketEngine::KeepAliveOption)
            d->data->controlSocket->setSocketOption(QAbstractSocket::KeepAliveOption, value);
        return true;
    }
    return false;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1818, as _ZNK19QSocks5SocketEngine25isReadNotificationEnabledEv
inline bool QSocks5SocketEngine::isReadNotificationEnabled() const
{
    Q_D(const QSocks5SocketEngine);
    return d->readNotificationEnabled;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1851, as _ZNK19QSocks5SocketEngine26isWriteNotificationEnabledEv
inline bool QSocks5SocketEngine::isWriteNotificationEnabled() const
{
    Q_D(const QSocks5SocketEngine);
    return d->writeNotificationEnabled;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1857, as _ZN19QSocks5SocketEngine27setWriteNotificationEnabledEb
inline void QSocks5SocketEngine::setWriteNotificationEnabled(bool enable)
{
    Q_D(QSocks5SocketEngine);
    d->writeNotificationEnabled = enable;
    if (enable && d->socketState == QAbstractSocket::ConnectedState) {
        if (d->mode == QSocks5SocketEnginePrivate::ConnectMode && d->data->controlSocket->bytesToWrite())
            return; // will be emitted as a result of bytes written
       d->emitWriteNotification();
       d->writeNotificationActivated = false;
    }
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1869, as _ZNK19QSocks5SocketEngine30isExceptionNotificationEnabledEv
inline bool QSocks5SocketEngine::isExceptionNotificationEnabled() const
{
    Q_D(const QSocks5SocketEngine);
    return d->exceptNotificationEnabled;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1875, as _ZN19QSocks5SocketEngine31setExceptionNotificationEnabledEb
inline void QSocks5SocketEngine::setExceptionNotificationEnabled(bool enable)
{
    Q_D(QSocks5SocketEngine);
    d->exceptNotificationEnabled = enable;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1078, as _ZN19QSocks5SocketEngine15connectInternalEv
inline bool QSocks5SocketEngine::connectInternal()
{
    Q_D(QSocks5SocketEngine);

    if (!d->data) {
        if (socketType() == QAbstractSocket::TcpSocket) {
            d->initialize(QSocks5SocketEnginePrivate::ConnectMode);
#ifndef QT_NO_UDPSOCKET
        } else if (socketType() == QAbstractSocket::UdpSocket) {
            d->initialize(QSocks5SocketEnginePrivate::UdpAssociateMode);
            // all udp needs to be bound
            if (!bind(QHostAddress("0.0.0.0"_L1), 0))
                return false;

            setState(QAbstractSocket::ConnectedState);
            return true;
#endif
        } else {
            qFatal("QSocks5SocketEngine::connectToHost: in QTcpServer mode");
            return false;
        }
    }

    if (d->socketState != QAbstractSocket::ConnectingState) {
        if (d->socks5State == QSocks5SocketEnginePrivate::Uninitialized
            // We may have new auth credentials since an earlier failure:
         || d->socks5State == QSocks5SocketEnginePrivate::AuthenticatingError) {
            setState(QAbstractSocket::ConnectingState);
            //limit buffer in internal socket, data is buffered in the external socket under application control
            d->data->controlSocket->setReadBufferSize(65536);
        }

        d->data->controlSocket->connectToHost(d->proxyInfo.hostName(), d->proxyInfo.port());
    }

    return false;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 224, as _ZN21QAbstractSocketEngine11setPeerPortEt
inline void QAbstractSocketEngine::setPeerPort(quint16 port)
{
    d_func()->peerPort = port;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 214, as _ZN21QAbstractSocketEngine14setPeerAddressERK12QHostAddress
inline void QAbstractSocketEngine::setPeerAddress(const QHostAddress &address)
{
   d_func()->peerAddress = address;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 108, as _ZNK21QAbstractSocketEngine8setErrorEN15QAbstractSocket11SocketErrorERK7QString
inline void QAbstractSocketEngine::setError(QAbstractSocket::SocketError error, const QString &errorString) const
{
    Q_D(const QAbstractSocketEngine);
    d->socketError = error;
    d->socketErrorString = errorString;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 164, as _ZN21QAbstractSocketEngine8setStateEN15QAbstractSocket11SocketStateE
inline void QAbstractSocketEngine::setState(QAbstractSocket::SocketState state)
{
    d_func()->socketState = state;
}

//  from src/network/socket/qabstractsocketengine.cpp, line 169, as _ZNK21QAbstractSocketEngine10socketTypeEv
inline QAbstractSocket::SocketType QAbstractSocketEngine::socketType() const
{
    return d_func()->socketType;
}

//  from src/network/socket/qsocks5socketengine.cpp, line 1056, as _ZN19QSocks5SocketEngine8setProxyERK13QNetworkProxy
inline void QSocks5SocketEngine::setProxy(const QNetworkProxy &networkProxy)
{
    Q_D(QSocks5SocketEngine);
    d->proxyInfo = networkProxy;
}
//  -----------------------------------------------------------------------

//  A QSocks5SocketEngine that Python can take functions over in. Every QSocks5SocketEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall1)(const void *, qintptr, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef qintptr (*CuteQSocks5SocketEngineCall2)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall3)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall4)(const void *, const QHostAddress *, quint16, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall5)(const void *, const QString *, quint16, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall6)(const void *, const QHostAddress *, quint16, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall7)(const void *, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef qintptr (*CuteQSocks5SocketEngineCall8)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef void (*CuteQSocks5SocketEngineCall9)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall10)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall11)(const void *, char *, qint64, int *);
#endif  // QT_CONFIG(socks5)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall12)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall13)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
typedef const QNetworkInterface * (*CuteQSocks5SocketEngineCall14)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall15)(const void *, const QNetworkInterface *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall16)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall17)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall18)(const void *, char *, qint64, QIpPacketHeader *, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall19)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef int (*CuteQSocks5SocketEngineCall20)(const void *, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall21)(const void *, int, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall22)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef void (*CuteQSocks5SocketEngineCall23)(const void *, bool, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall24)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef void (*CuteQSocks5SocketEngineCall25)(const void *, bool, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall26)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef void (*CuteQSocks5SocketEngineCall27)(const void *, bool, int *);
#endif  // QT_CONFIG(socks5)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSocks5SocketEngineCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSocks5SocketEngineCall29)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall30)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall31)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall32)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall33)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall34)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSocks5SocketEngine : public QSocks5SocketEngine {
public:
  using QSocks5SocketEngine::QSocks5SocketEngine;
  void *taken[35] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine10initializeExN15QAbstractSocket11SocketStateE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine16socketDescriptorEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine7isValidEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine13connectToHostERK12QHostAddresst")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19connectToHostByNameERK7QStringt")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine4bindERK12QHostAddresst")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6listenEi")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine6acceptEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine5closeEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine14bytesAvailableEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine4readEPcx")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine18multicastInterfaceEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkInterface")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine12readDatagramEPcxP15QIpPacketHeader6QFlagsINS_18PacketHeaderOptionEE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine12bytesToWriteEv")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[32] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[33] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[34] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::initialize(QAbstractSocket::SocketType
  //      type, QAbstractSocket::NetworkLayerProtocol protocol)
  bool initialize(
      QAbstractSocket::SocketType type,
      QAbstractSocket::NetworkLayerProtocol protocol) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall0 call = reinterpret_cast<CuteQSocks5SocketEngineCall0>(taken[0]);
      bool given = call(this, static_cast<int>(type), static_cast<int>(protocol), &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::initialize(type, protocol);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::initialize(qintptr socketDescriptor,
  //      QAbstractSocket::SocketState socketState)
  bool initialize(
      qintptr socketDescriptor,
      QAbstractSocket::SocketState socketState) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall1 call = reinterpret_cast<CuteQSocks5SocketEngineCall1>(taken[1]);
      bool given = call(this, socketDescriptor, static_cast<int>(socketState), &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::initialize(socketDescriptor, socketState);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  qintptr QSocks5SocketEngine::socketDescriptor() const
  qintptr socketDescriptor() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall2 call = reinterpret_cast<CuteQSocks5SocketEngineCall2>(taken[2]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::socketDescriptor();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isValid() const
  bool isValid() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall3 call = reinterpret_cast<CuteQSocks5SocketEngineCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::isValid();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::connectToHost(const QHostAddress &address,
  //      quint16 port)
  bool connectToHost(const QHostAddress &address, quint16 port) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall4 call = reinterpret_cast<CuteQSocks5SocketEngineCall4>(taken[4]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::connectToHost(address, port);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::connectToHostByName(const QString &name,
  //      quint16 port)
  bool connectToHostByName(const QString &name, quint16 port) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall5 call = reinterpret_cast<CuteQSocks5SocketEngineCall5>(taken[5]);
      bool given = call(this, &name, port, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::connectToHostByName(name, port);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::bind(const QHostAddress &address, quint16
  //      port)
  bool bind(const QHostAddress &address, quint16 port) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall6 call = reinterpret_cast<CuteQSocks5SocketEngineCall6>(taken[6]);
      bool given = call(this, &address, port, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::bind(address, port);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::listen(int backlog)
  bool listen(int backlog) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall7 call = reinterpret_cast<CuteQSocks5SocketEngineCall7>(taken[7]);
      bool given = call(this, backlog, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::listen(backlog);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  qintptr QSocks5SocketEngine::accept()
  qintptr accept() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall8 call = reinterpret_cast<CuteQSocks5SocketEngineCall8>(taken[8]);
      qintptr given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::accept();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  void QSocks5SocketEngine::close()
  void close() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall9 call = reinterpret_cast<CuteQSocks5SocketEngineCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::close();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  qint64 QSocks5SocketEngine::bytesAvailable() const
  qint64 bytesAvailable() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall10 call = reinterpret_cast<CuteQSocks5SocketEngineCall10>(taken[10]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::bytesAvailable();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  qint64 QSocks5SocketEngine::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall11 call = reinterpret_cast<CuteQSocks5SocketEngineCall11>(taken[11]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::read(data, maxlen);
  }
#endif  // QT_CONFIG(socks5)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::joinMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool joinMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall12 call = reinterpret_cast<CuteQSocks5SocketEngineCall12>(taken[12]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::joinMulticastGroup(groupAddress, iface);
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::leaveMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool leaveMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall13 call = reinterpret_cast<CuteQSocks5SocketEngineCall13>(taken[13]);
      bool given = call(this, &groupAddress, &iface, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::leaveMulticastGroup(groupAddress, iface);
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
  //  QNetworkInterface QSocks5SocketEngine::multicastInterface() const
  QNetworkInterface multicastInterface() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall14 call = reinterpret_cast<CuteQSocks5SocketEngineCall14>(taken[14]);
      const QNetworkInterface * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSocks5SocketEngine::multicastInterface();
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::setMulticastInterface(const
  //      QNetworkInterface &iface)
  bool setMulticastInterface(const QNetworkInterface &iface) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall15 call = reinterpret_cast<CuteQSocks5SocketEngineCall15>(taken[15]);
      bool given = call(this, &iface, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::setMulticastInterface(iface);
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::hasPendingDatagrams() const
  bool hasPendingDatagrams() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall16 call = reinterpret_cast<CuteQSocks5SocketEngineCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::hasPendingDatagrams();
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
  //  qint64 QSocks5SocketEngine::pendingDatagramSize() const
  qint64 pendingDatagramSize() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall17 call = reinterpret_cast<CuteQSocks5SocketEngineCall17>(taken[17]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::pendingDatagramSize();
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)

#if QT_CONFIG(socks5)
  //  qint64 QSocks5SocketEngine::readDatagram(char *data, qint64 maxlen,
  //      QIpPacketHeader *a2, PacketHeaderOptions a3)
  qint64 readDatagram(
      char *data,
      qint64 maxlen,
      QIpPacketHeader *a2,
      QAbstractSocketEngine::PacketHeaderOptions a3) override {
    if (taken[18]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall18 call = reinterpret_cast<CuteQSocks5SocketEngineCall18>(taken[18]);
      qint64 given = call(this, data, maxlen, a2, static_cast<int>(a3.toInt()), &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::readDatagram(data, maxlen, a2, a3);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  qint64 QSocks5SocketEngine::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall19 call = reinterpret_cast<CuteQSocks5SocketEngineCall19>(taken[19]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::bytesToWrite();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  int QSocks5SocketEngine::option(SocketOption option) const
  int option(QAbstractSocketEngine::SocketOption option) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall20 call = reinterpret_cast<CuteQSocks5SocketEngineCall20>(taken[20]);
      int given = call(this, static_cast<int>(option), &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::option(option);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::setOption(SocketOption option, int value)
  bool setOption(
      QAbstractSocketEngine::SocketOption option,
      int value) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall21 call = reinterpret_cast<CuteQSocks5SocketEngineCall21>(taken[21]);
      bool given = call(this, static_cast<int>(option), value, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::setOption(option, value);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isReadNotificationEnabled() const
  bool isReadNotificationEnabled() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall22 call = reinterpret_cast<CuteQSocks5SocketEngineCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::isReadNotificationEnabled();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  void QSocks5SocketEngine::setReadNotificationEnabled(bool enable)
  void setReadNotificationEnabled(bool enable) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall23 call = reinterpret_cast<CuteQSocks5SocketEngineCall23>(taken[23]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::setReadNotificationEnabled(enable);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isWriteNotificationEnabled() const
  bool isWriteNotificationEnabled() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall24 call = reinterpret_cast<CuteQSocks5SocketEngineCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::isWriteNotificationEnabled();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  void QSocks5SocketEngine::setWriteNotificationEnabled(bool enable)
  void setWriteNotificationEnabled(bool enable) override {
    if (taken[25]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall25 call = reinterpret_cast<CuteQSocks5SocketEngineCall25>(taken[25]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::setWriteNotificationEnabled(enable);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isExceptionNotificationEnabled() const
  bool isExceptionNotificationEnabled() const override {
    if (taken[26]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall26 call = reinterpret_cast<CuteQSocks5SocketEngineCall26>(taken[26]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::isExceptionNotificationEnabled();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  void QSocks5SocketEngine::setExceptionNotificationEnabled(bool
  //      enable)
  void setExceptionNotificationEnabled(bool enable) override {
    if (taken[27]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall27 call = reinterpret_cast<CuteQSocks5SocketEngineCall27>(taken[27]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::setExceptionNotificationEnabled(enable);
  }
#endif  // QT_CONFIG(socks5)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall28 call = reinterpret_cast<CuteQSocks5SocketEngineCall28>(taken[28]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall29 call = reinterpret_cast<CuteQSocks5SocketEngineCall29>(taken[29]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[30]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall30 call = reinterpret_cast<CuteQSocks5SocketEngineCall30>(taken[30]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[31]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall31 call = reinterpret_cast<CuteQSocks5SocketEngineCall31>(taken[31]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[32]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall32 call = reinterpret_cast<CuteQSocks5SocketEngineCall32>(taken[32]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[33]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall33 call = reinterpret_cast<CuteQSocks5SocketEngineCall33>(taken[33]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[34]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall34 call = reinterpret_cast<CuteQSocks5SocketEngineCall34>(taken[34]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QSocks5SocketEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QSocks5SocketEngine10metaObjectEv(
    const QSocks5SocketEngine *self) {
  return self->metaObject();
}

//  void *QSocks5SocketEngine::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QSocks5SocketEngine11qt_metacastEPKc(
    QSocks5SocketEngine *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QSocks5SocketEngine::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QSocks5SocketEngine11qt_metacallEN11QMetaObject4CallEiPPv(
    QSocks5SocketEngine *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  bool QSocks5SocketEngine::initialize(QAbstractSocket::SocketType type,
//      QAbstractSocket::NetworkLayerProtocol protocol)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine10initializeEN15QAbstractSocket10SocketTypeENS0_20NetworkLayerProtocolE(
    QSocks5SocketEngine *self,
    QAbstractSocket::SocketType type,
    QAbstractSocket::NetworkLayerProtocol protocol) {
  return self->initialize(type, protocol);
}

//  bool QSocks5SocketEngine::initialize(qintptr socketDescriptor,
//      QAbstractSocket::SocketState socketState)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine10initializeExN15QAbstractSocket11SocketStateE(
    QSocks5SocketEngine *self,
    qintptr socketDescriptor,
    QAbstractSocket::SocketState socketState) {
  return self->initialize(socketDescriptor, socketState);
}

//  void QSocks5SocketEngine::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSocks5SocketEngine8setProxyERK13QNetworkProxy(
    QSocks5SocketEngine *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}

//  qintptr QSocks5SocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_ZNK19QSocks5SocketEngine16socketDescriptorEv(
    const QSocks5SocketEngine *self) {
  return self->socketDescriptor();
}

//  bool QSocks5SocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSocks5SocketEngine7isValidEv(
    const QSocks5SocketEngine *self) {
  return self->isValid();
}

//  bool QSocks5SocketEngine::connectToHost(const QHostAddress &address,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine13connectToHostERK12QHostAddresst(
    QSocks5SocketEngine *self,
    const QHostAddress *address,
    quint16 port) {
  return self->connectToHost(*address, port);
}

//  bool QSocks5SocketEngine::connectToHostByName(const QString &name,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine19connectToHostByNameERK7QStringt(
    QSocks5SocketEngine *self,
    const QString *name,
    quint16 port) {
  return self->connectToHostByName(*name, port);
}

//  bool QSocks5SocketEngine::bind(const QHostAddress &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine4bindERK12QHostAddresst(
    QSocks5SocketEngine *self,
    const QHostAddress *address,
    quint16 port) {
  return self->bind(*address, port);
}

//  bool QSocks5SocketEngine::listen(int backlog)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine6listenEi(
    QSocks5SocketEngine *self,
    int backlog) {
  return self->listen(backlog);
}

//  qintptr QSocks5SocketEngine::accept()
extern "C" Q_DECL_EXPORT
qintptr ritual_ZN19QSocks5SocketEngine6acceptEv(QSocks5SocketEngine *self) {
  return self->accept();
}

//  void QSocks5SocketEngine::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSocks5SocketEngine5closeEv(QSocks5SocketEngine *self) {
  self->close();
}

//  qint64 QSocks5SocketEngine::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QSocks5SocketEngine14bytesAvailableEv(
    const QSocks5SocketEngine *self) {
  return self->bytesAvailable();
}

//  qint64 QSocks5SocketEngine::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN19QSocks5SocketEngine4readEPcx(
    QSocks5SocketEngine *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  qint64 QSocks5SocketEngine::write(const char *data, qint64 len)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN19QSocks5SocketEngine5writeEPKcx(
    QSocks5SocketEngine *self,
    const char *data,
    qint64 len) {
  return self->write(data, len);
}

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QSocks5SocketEngine::joinMulticastGroup(const QHostAddress
//      &groupAddress, const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface(
    QSocks5SocketEngine *self,
    const QHostAddress *groupAddress,
    const QNetworkInterface *iface) {
  return self->joinMulticastGroup(*groupAddress, *iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QSocks5SocketEngine::leaveMulticastGroup(const QHostAddress
//      &groupAddress, const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface(
    QSocks5SocketEngine *self,
    const QHostAddress *groupAddress,
    const QNetworkInterface *iface) {
  return self->leaveMulticastGroup(*groupAddress, *iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  QNetworkInterface QSocks5SocketEngine::multicastInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZNK19QSocks5SocketEngine18multicastInterfaceEv(
    const QSocks5SocketEngine *self) {
  return new QNetworkInterface(self->multicastInterface());
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QSocks5SocketEngine::setMulticastInterface(const QNetworkInterface
//      &iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine21setMulticastInterfaceERK17QNetworkInterface(
    QSocks5SocketEngine *self,
    const QNetworkInterface *iface) {
  return self->setMulticastInterface(*iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
//  bool QSocks5SocketEngine::hasPendingDatagrams() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSocks5SocketEngine19hasPendingDatagramsEv(
    const QSocks5SocketEngine *self) {
  return self->hasPendingDatagrams();
}
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
//  qint64 QSocks5SocketEngine::pendingDatagramSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QSocks5SocketEngine19pendingDatagramSizeEv(
    const QSocks5SocketEngine *self) {
  return self->pendingDatagramSize();
}
#endif  // !defined(QT_NO_UDPSOCKET)

//  qint64 QSocks5SocketEngine::readDatagram(char *data, qint64 maxlen,
//      QIpPacketHeader *a2, PacketHeaderOptions a3)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN19QSocks5SocketEngine12readDatagramEPcxP15QIpPacketHeader6QFlagsIN21QAbstractSocketEngine18PacketHeaderOptionEE(
    QSocks5SocketEngine *self,
    char *data,
    qint64 maxlen,
    QIpPacketHeader *a2,
    int a3) {
  return self->readDatagram(
      data,
      maxlen,
      a2,
      QFlags<QAbstractSocketEngine::PacketHeaderOption>::fromInt(a3));
}

//  qint64 QSocks5SocketEngine::writeDatagram(const char *data, qint64 len,
//      const QIpPacketHeader &a2)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN19QSocks5SocketEngine13writeDatagramEPKcxRK15QIpPacketHeader(
    QSocks5SocketEngine *self,
    const char *data,
    qint64 len,
    const QIpPacketHeader *a2) {
  return self->writeDatagram(data, len, *a2);
}

//  qint64 QSocks5SocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QSocks5SocketEngine12bytesToWriteEv(
    const QSocks5SocketEngine *self) {
  return self->bytesToWrite();
}

//  int QSocks5SocketEngine::option(SocketOption option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QSocks5SocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE(
    const QSocks5SocketEngine *self,
    QAbstractSocketEngine::SocketOption option) {
  return self->option(option);
}

//  bool QSocks5SocketEngine::setOption(SocketOption option, int value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi(
    QSocks5SocketEngine *self,
    QAbstractSocketEngine::SocketOption option,
    int value) {
  return self->setOption(option, value);
}

//  bool QSocks5SocketEngine::waitForRead(QDeadlineTimer deadline, bool
//      *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine11waitForReadE14QDeadlineTimerPb(
    QSocks5SocketEngine *self,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForRead(*deadline, timedOut);
}

//  bool QSocks5SocketEngine::waitForWrite(QDeadlineTimer deadline, bool
//      *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine12waitForWriteE14QDeadlineTimerPb(
    QSocks5SocketEngine *self,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForWrite(*deadline, timedOut);
}

//  bool QSocks5SocketEngine::waitForReadOrWrite(bool *readyToRead, bool
//      *readyToWrite, bool checkRead, bool checkWrite, QDeadlineTimer
//      deadline, bool *timedOut)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine18waitForReadOrWriteEPbS0_bb14QDeadlineTimerS0_(
    QSocks5SocketEngine *self,
    bool *readyToRead,
    bool *readyToWrite,
    bool checkRead,
    bool checkWrite,
    const QDeadlineTimer *deadline,
    bool *timedOut) {
  return self->waitForReadOrWrite(
      readyToRead,
      readyToWrite,
      checkRead,
      checkWrite,
      *deadline,
      timedOut);
}

//  bool QSocks5SocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSocks5SocketEngine25isReadNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->isReadNotificationEnabled();
}

//  void QSocks5SocketEngine::setReadNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSocks5SocketEngine26setReadNotificationEnabledEb(
    QSocks5SocketEngine *self,
    bool enable) {
  self->setReadNotificationEnabled(enable);
}

//  bool QSocks5SocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSocks5SocketEngine26isWriteNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->isWriteNotificationEnabled();
}

//  void QSocks5SocketEngine::setWriteNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSocks5SocketEngine27setWriteNotificationEnabledEb(
    QSocks5SocketEngine *self,
    bool enable) {
  self->setWriteNotificationEnabled(enable);
}

//  bool QSocks5SocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSocks5SocketEngine30isExceptionNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->isExceptionNotificationEnabled();
}

//  void QSocks5SocketEngine::setExceptionNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSocks5SocketEngine31setExceptionNotificationEnabledEb(
    QSocks5SocketEngine *self,
    bool enable) {
  self->setExceptionNotificationEnabled(enable);
}

//  QSocks5SocketEnginePrivate *QSocks5SocketEngine::d_func()
extern "C" Q_DECL_EXPORT
QSocks5SocketEnginePrivate *ritual_ZN19QSocks5SocketEngine6d_funcEv(
    QSocks5SocketEngine *self) {
  return self->d_func();
}

//  const QSocks5SocketEnginePrivate *QSocks5SocketEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QSocks5SocketEnginePrivate *ritual_ZNK19QSocks5SocketEngine6d_funcEv(
    const QSocks5SocketEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQSocks5SocketEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSocks5SocketEngine(
    QSocks5SocketEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSocks5SocketEngine *>(self)->take(key, call);
}

//  qintptr QSocks5SocketEngine::socketDescriptor() const
extern "C" Q_DECL_EXPORT
qintptr ritual_own_ZNK19QSocks5SocketEngine16socketDescriptorEv(
    const QSocks5SocketEngine *self) {
  return self->QSocks5SocketEngine::socketDescriptor();
}

//  bool QSocks5SocketEngine::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QSocks5SocketEngine7isValidEv(
    const QSocks5SocketEngine *self) {
  return self->QSocks5SocketEngine::isValid();
}

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QSocks5SocketEngine::joinMulticastGroup(const QHostAddress
//      &groupAddress, const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QSocks5SocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface(
    QSocks5SocketEngine *self,
    const QHostAddress *groupAddress,
    const QNetworkInterface *iface) {
  return self->QSocks5SocketEngine::joinMulticastGroup(
      *groupAddress,
      *iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QSocks5SocketEngine::leaveMulticastGroup(const QHostAddress
//      &groupAddress, const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QSocks5SocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface(
    QSocks5SocketEngine *self,
    const QHostAddress *groupAddress,
    const QNetworkInterface *iface) {
  return self->QSocks5SocketEngine::leaveMulticastGroup(
      *groupAddress,
      *iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  QNetworkInterface QSocks5SocketEngine::multicastInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_own_ZNK19QSocks5SocketEngine18multicastInterfaceEv(
    const QSocks5SocketEngine *self) {
  return new QNetworkInterface(
      self->QSocks5SocketEngine::multicastInterface());
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
//  bool QSocks5SocketEngine::setMulticastInterface(const QNetworkInterface
//      &iface)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QSocks5SocketEngine21setMulticastInterfaceERK17QNetworkInterface(
    QSocks5SocketEngine *self,
    const QNetworkInterface *iface) {
  return self->QSocks5SocketEngine::setMulticastInterface(*iface);
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

//  qint64 QSocks5SocketEngine::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QSocks5SocketEngine12bytesToWriteEv(
    const QSocks5SocketEngine *self) {
  return self->QSocks5SocketEngine::bytesToWrite();
}

//  int QSocks5SocketEngine::option(SocketOption option) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QSocks5SocketEngine6optionEN21QAbstractSocketEngine12SocketOptionE(
    const QSocks5SocketEngine *self,
    QAbstractSocketEngine::SocketOption option) {
  return self->QSocks5SocketEngine::option(option);
}

//  bool QSocks5SocketEngine::setOption(SocketOption option, int value)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QSocks5SocketEngine9setOptionEN21QAbstractSocketEngine12SocketOptionEi(
    QSocks5SocketEngine *self,
    QAbstractSocketEngine::SocketOption option,
    int value) {
  return self->QSocks5SocketEngine::setOption(option, value);
}

//  bool QSocks5SocketEngine::isReadNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QSocks5SocketEngine25isReadNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->QSocks5SocketEngine::isReadNotificationEnabled();
}

//  bool QSocks5SocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QSocks5SocketEngine26isWriteNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->QSocks5SocketEngine::isWriteNotificationEnabled();
}

//  bool QSocks5SocketEngine::isExceptionNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QSocks5SocketEngine30isExceptionNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->QSocks5SocketEngine::isExceptionNotificationEnabled();
}

//  void QSocks5SocketEngine::setExceptionNotificationEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QSocks5SocketEngine31setExceptionNotificationEnabledEb(
    QSocks5SocketEngine *self,
    bool enable) {
  self->QSocks5SocketEngine::setExceptionNotificationEnabled(enable);
}

#endif  // QT_CONFIG(socks5)
#endif  // QT_CONFIG(socks5)
