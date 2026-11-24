//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(socks5)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsocks5socketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qdeadlinetimer.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qabstractsocketengine_p.h"
#include "qnativesocketengine_p.h"
#include "qmutex.h"
#include "qnetworkproxy.h"
#include "qsocks5socketengine_p.h"
#include "qtcpsocket.h"
#include "qudpsocket.h"
#include "qtcpserver.h"
#include "qdebug.h"
#include "qhash.h"
#include "qqueue.h"
#include "qdeadlinetimer.h"
#include "qelapsedtimer.h"
#include "qmutex.h"
#include "qthread.h"
#include "qcoreapplication.h"
#include "qurl.h"
#include "qauthenticator.h"
#include "private/qiodevice_p.h"
#include "private/qringbuffer_p.h"
#include <qendian.h>
#include <qnetworkinterface.h>
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

//  from src/network/socket/qsocks5socketengine.cpp, line 1056, as _ZN19QSocks5SocketEngine8setProxyERK13QNetworkProxy
inline void QSocks5SocketEngine::setProxy(const QNetworkProxy &networkProxy)
{
    Q_D(QSocks5SocketEngine);
    d->proxyInfo = networkProxy;
}

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

//  from src/network/socket/qsocks5socketengine.cpp, line 1552, as _ZNK19QSocks5SocketEngine18multicastInterfaceEv
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
inline QNetworkInterface QSocks5SocketEngine::multicastInterface() const
{
    return QNetworkInterface();
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

//  from src/network/socket/qsocks5socketengine.cpp, line 1800, as _ZN19QSocks5SocketEngine18waitForReadOrWriteEPbS0_bb14QDeadlineTimerS0_
inline bool QSocks5SocketEngine::waitForReadOrWrite(bool *readyToRead, bool *readyToWrite,
                                            bool checkRead, bool checkWrite,
                                            QDeadlineTimer deadline, bool *timedOut)
{
    Q_UNUSED(checkRead);
    if (!checkWrite) {
        bool canRead = waitForRead(deadline, timedOut);
        if (readyToRead)
            *readyToRead = canRead;
        return canRead;
    }

    bool canWrite = waitForWrite(deadline, timedOut);
    if (readyToWrite)
        *readyToWrite = canWrite;
    return canWrite;
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
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall11)(const void *, const QHostAddress *, const QNetworkInterface *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
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
typedef const QNetworkInterface * (*CuteQSocks5SocketEngineCall13)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall14)(const void *, const QNetworkInterface *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall15)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall16)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
typedef qint64 (*CuteQSocks5SocketEngineCall17)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef int (*CuteQSocks5SocketEngineCall18)(const void *, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall19)(const void *, int, int, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef bool (*CuteQSocks5SocketEngineCall20)(const void *, int *);
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
typedef void (*CuteQSocks5SocketEngineCall21)(const void *, bool, int *);
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
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSocks5SocketEngineCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSocks5SocketEngineCall27)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall28)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall29)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall30)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSocks5SocketEngineCall32)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSocks5SocketEngine : public QSocks5SocketEngine {
public:
  using QSocks5SocketEngine::QSocks5SocketEngine;
  void *taken[33] = {};

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
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine18joinMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine19leaveMulticastGroupERK12QHostAddressRK17QNetworkInterface")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine18multicastInterfaceEv")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine21setMulticastInterfaceERK17QNetworkInterface")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19hasPendingDatagramsEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine19pendingDatagramSizeEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine12bytesToWriteEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine6optionENS_12SocketOptionE")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine9setOptionENS_12SocketOptionEi")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine25isReadNotificationEnabledEv")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine26setReadNotificationEnabledEb")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine26isWriteNotificationEnabledEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine27setWriteNotificationEnabledEb")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZNK21QAbstractSocketEngine30isExceptionNotificationEnabledEv")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
#if QT_CONFIG(socks5)
    if (!std::strcmp(key, "_ZN21QAbstractSocketEngine31setExceptionNotificationEnabledEb")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(socks5)
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

#if !defined(QT_NO_UDPSOCKET)
#if !defined(QT_NO_NETWORKINTERFACE)
#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::joinMulticastGroup(const QHostAddress
  //      &groupAddress, const QNetworkInterface &iface)
  bool joinMulticastGroup(
      const QHostAddress &groupAddress,
      const QNetworkInterface &iface) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall11 call = reinterpret_cast<CuteQSocks5SocketEngineCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall12 call = reinterpret_cast<CuteQSocks5SocketEngineCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall13 call = reinterpret_cast<CuteQSocks5SocketEngineCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall14 call = reinterpret_cast<CuteQSocks5SocketEngineCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall15 call = reinterpret_cast<CuteQSocks5SocketEngineCall15>(taken[15]);
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
    if (taken[16]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall16 call = reinterpret_cast<CuteQSocks5SocketEngineCall16>(taken[16]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::pendingDatagramSize();
  }
#endif  // QT_CONFIG(socks5)
#endif  // !defined(QT_NO_UDPSOCKET)

#if QT_CONFIG(socks5)
  //  qint64 QSocks5SocketEngine::bytesToWrite() const
  qint64 bytesToWrite() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall17 call = reinterpret_cast<CuteQSocks5SocketEngineCall17>(taken[17]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::bytesToWrite();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  int QSocks5SocketEngine::option(SocketOption option) const
  int option(QAbstractSocketEngine::SocketOption option) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall18 call = reinterpret_cast<CuteQSocks5SocketEngineCall18>(taken[18]);
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
    if (taken[19]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall19 call = reinterpret_cast<CuteQSocks5SocketEngineCall19>(taken[19]);
      bool given = call(this, static_cast<int>(option), value, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::setOption(option, value);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isReadNotificationEnabled() const
  bool isReadNotificationEnabled() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall20 call = reinterpret_cast<CuteQSocks5SocketEngineCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::isReadNotificationEnabled();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  void QSocks5SocketEngine::setReadNotificationEnabled(bool enable)
  void setReadNotificationEnabled(bool enable) override {
    if (taken[21]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall21 call = reinterpret_cast<CuteQSocks5SocketEngineCall21>(taken[21]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::setReadNotificationEnabled(enable);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isWriteNotificationEnabled() const
  bool isWriteNotificationEnabled() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall22 call = reinterpret_cast<CuteQSocks5SocketEngineCall22>(taken[22]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSocks5SocketEngine::isWriteNotificationEnabled();
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  void QSocks5SocketEngine::setWriteNotificationEnabled(bool enable)
  void setWriteNotificationEnabled(bool enable) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall23 call = reinterpret_cast<CuteQSocks5SocketEngineCall23>(taken[23]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::setWriteNotificationEnabled(enable);
  }
#endif  // QT_CONFIG(socks5)

#if QT_CONFIG(socks5)
  //  bool QSocks5SocketEngine::isExceptionNotificationEnabled() const
  bool isExceptionNotificationEnabled() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall24 call = reinterpret_cast<CuteQSocks5SocketEngineCall24>(taken[24]);
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
    if (taken[25]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall25 call = reinterpret_cast<CuteQSocks5SocketEngineCall25>(taken[25]);
      call(this, enable, &handled);
      if (handled) return;
    }
    QSocks5SocketEngine::setExceptionNotificationEnabled(enable);
  }
#endif  // QT_CONFIG(socks5)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQSocks5SocketEngineCall26 call = reinterpret_cast<CuteQSocks5SocketEngineCall26>(taken[26]);
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
      CuteQSocks5SocketEngineCall27 call = reinterpret_cast<CuteQSocks5SocketEngineCall27>(taken[27]);
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
      CuteQSocks5SocketEngineCall28 call = reinterpret_cast<CuteQSocks5SocketEngineCall28>(taken[28]);
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
      CuteQSocks5SocketEngineCall29 call = reinterpret_cast<CuteQSocks5SocketEngineCall29>(taken[29]);
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
      CuteQSocks5SocketEngineCall30 call = reinterpret_cast<CuteQSocks5SocketEngineCall30>(taken[30]);
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
      CuteQSocks5SocketEngineCall31 call = reinterpret_cast<CuteQSocks5SocketEngineCall31>(taken[31]);
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
      CuteQSocks5SocketEngineCall32 call = reinterpret_cast<CuteQSocks5SocketEngineCall32>(taken[32]);
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

//  bool QSocks5SocketEngine::connectToHostByName(const QString &name,
//      quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSocks5SocketEngine19connectToHostByNameERK7QStringt(
    QSocks5SocketEngine *self,
    const QString *name,
    quint16 port) {
  return self->connectToHostByName(*name, port);
}

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

//  bool QSocks5SocketEngine::isWriteNotificationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSocks5SocketEngine26isWriteNotificationEnabledEv(
    const QSocks5SocketEngine *self) {
  return self->isWriteNotificationEnabled();
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
//  QNetworkInterface QSocks5SocketEngine::multicastInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_own_ZNK19QSocks5SocketEngine18multicastInterfaceEv(
    const QSocks5SocketEngine *self) {
  return new QNetworkInterface(
      self->QSocks5SocketEngine::multicastInterface());
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
#endif  // !defined(QT_NO_UDPSOCKET)

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
