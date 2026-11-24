//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluez_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluez_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbluetoothsocketbase_p.h"
#include "qbluetoothsocket.h"
#include "qbluetoothsocket_bluez_p.h"
#include "qbluetoothdeviceinfo.h"
#include <QtBluetooth/QBluetoothLocalDevice>
#include <qplatformdefs.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/QLoggingCategory>
#include <errno.h>
#include <unistd.h>
#include <string.h>
#include <QtCore/QSocketNotifier>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocketbase.cpp, line 8, as _ZN27QBluetoothSocketBasePrivateC2EP7QObject
inline QBluetoothSocketBasePrivate::QBluetoothSocketBasePrivate(QObject *parent) : QObject(parent)
{

}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocketbase.cpp, line 13, as _ZN27QBluetoothSocketBasePrivateD2Ev
inline QBluetoothSocketBasePrivate::~QBluetoothSocketBasePrivate()
{

}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 367, as _ZN28QBluetoothSocketPrivateBluez5abortEv
inline void QBluetoothSocketPrivateBluez::abort()
{
    delete readNotifier;
    readNotifier = nullptr;
    delete connectWriteNotifier;
    connectWriteNotifier = nullptr;

    // We don't transition through Closing for abort, so
    // we don't call disconnectFromService or
    // QBluetoothSocket::close
    QT_CLOSE(socket);
    socket = -1;

    Q_Q(QBluetoothSocket);

    q->setOpenMode(QIODevice::NotOpen);
    q->setSocketState(QBluetoothSocket::SocketState::UnconnectedState);
    emit q->readChannelFinished();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 588, as _ZN28QBluetoothSocketPrivateBluez5closeEv
inline void QBluetoothSocketPrivateBluez::close()
{
    // If we have pending data on the write buffer, wait until it has been written,
    // after which this close() will be called again
    if (txBuffer.size() > 0)
        connectWriteNotifier->setEnabled(true);
    else
        abort();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 527, as _ZN28QBluetoothSocketPrivateBluez9writeDataEPKcx
inline qint64 QBluetoothSocketPrivateBluez::writeData(const char *data, qint64 maxSize)
{
    Q_Q(QBluetoothSocket);

    if (state != QBluetoothSocket::SocketState::ConnectedState) {
        errorString = QBluetoothSocket::tr("Cannot write while not connected");
        q->setSocketError(QBluetoothSocket::SocketError::OperationError);
        return -1;
    }

    if (q->openMode() & QIODevice::Unbuffered) {
        auto sz = ::qt_safe_write(socket, data, maxSize);
        if (sz < 0) {
            switch (errno) {
            case EAGAIN:
                sz = 0;
                break;
            default:
                errorString = QBluetoothSocket::tr("Network Error: %1").arg(qt_error_string(errno));
                q->setSocketError(QBluetoothSocket::SocketError::NetworkError);
            }
        }

        if (sz > 0)
            emit q->bytesWritten(sz);

        return sz;
    }
    else {

        if(!connectWriteNotifier)
            return -1;

        if(txBuffer.size() == 0) {
            connectWriteNotifier->setEnabled(true);
            QMetaObject::invokeMethod(this, "_q_writeNotify", Qt::QueuedConnection);
        }

        char *txbuf = txBuffer.reserve(maxSize);
        memcpy(txbuf, data, maxSize);

        return maxSize;
    }
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 598, as _ZN28QBluetoothSocketPrivateBluez19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline bool QBluetoothSocketPrivateBluez::setSocketDescriptor(int socketDescriptor, QBluetoothServiceInfo::Protocol socketType_,
                                           QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode openMode)
{
    Q_Q(QBluetoothSocket);
    delete readNotifier;
    readNotifier = nullptr;
    delete connectWriteNotifier;
    connectWriteNotifier = nullptr;

    socketType = socketType_;
    if (socket != -1)
        QT_CLOSE(socket);

    socket = socketDescriptor;

    // ensure that O_NONBLOCK is set on new connections.
    int flags = fcntl(socket, F_GETFL, 0);
    if (!(flags & O_NONBLOCK))
        fcntl(socket, F_SETFL, flags | O_NONBLOCK);

    readNotifier = new QSocketNotifier(socket, QSocketNotifier::Read);
    QObject::connect(readNotifier, SIGNAL(activated(QSocketDescriptor)), this, SLOT(_q_readNotify()));
    connectWriteNotifier = new QSocketNotifier(socket, QSocketNotifier::Write, q);
    QObject::connect(connectWriteNotifier, SIGNAL(activated(QSocketDescriptor)), this, SLOT(_q_writeNotify()));

    q->setOpenMode(openMode);
    q->setSocketState(socketState);

    return true;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 629, as _ZNK28QBluetoothSocketPrivateBluez14bytesAvailableEv
inline qint64 QBluetoothSocketPrivateBluez::bytesAvailable() const
{
    return rxBuffer.size();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 639, as _ZNK28QBluetoothSocketPrivateBluez11canReadLineEv
inline bool QBluetoothSocketPrivateBluez::canReadLine() const
{
    return rxBuffer.canReadLine();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 634, as _ZNK28QBluetoothSocketPrivateBluez12bytesToWriteEv
inline qint64 QBluetoothSocketPrivateBluez::bytesToWrite() const
{
    return txBuffer.size();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 281, as _ZN28QBluetoothSocketPrivateBluez14_q_writeNotifyEv
inline void QBluetoothSocketPrivateBluez::_q_writeNotify()
{
    Q_Q(QBluetoothSocket);
    if (connecting && state == QBluetoothSocket::SocketState::ConnectingState){
        int errorno, len;
        len = sizeof(errorno);
        ::getsockopt(socket, SOL_SOCKET, SO_ERROR, &errorno, (socklen_t*)&len);
        if(errorno) {
            errorString = qt_error_string(errorno);
            q->setSocketError(QBluetoothSocket::SocketError::UnknownSocketError);
            return;
        }

        q->setSocketState(QBluetoothSocket::SocketState::ConnectedState);

        connectWriteNotifier->setEnabled(false);
        connecting = false;
    }
    else {
        if (txBuffer.size() == 0) {
            connectWriteNotifier->setEnabled(false);
            return;
        }

        char buf[1024];

        const auto size = txBuffer.read(buf, 1024);
        const auto writtenBytes = qt_safe_write(socket, buf, size);
        if (writtenBytes < 0) {
            switch (errno) {
            case EAGAIN:
                txBuffer.ungetBlock(buf, size);
                break;
            default:
                // every other case returns error
                errorString = QBluetoothSocket::tr("Network Error: %1").arg(qt_error_string(errno)) ;
                q->setSocketError(QBluetoothSocket::SocketError::NetworkError);
                break;
            }
        } else {
            if (writtenBytes < size) {
                // add remainder back to buffer
                char* remainder = buf + writtenBytes;
                txBuffer.ungetBlock(remainder, size - writtenBytes);
            }
            if (writtenBytes > 0)
                emit q->bytesWritten(writtenBytes);
        }

        if (txBuffer.size()) {
            connectWriteNotifier->setEnabled(true);
        }
        else if (state == QBluetoothSocket::SocketState::ClosingState) {
            connectWriteNotifier->setEnabled(false);
            this->close();
        }
    }
}
//  -----------------------------------------------------------------------

//  void QBluetoothSocketPrivateBluez::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateBluez5abortEv(
    QBluetoothSocketPrivateBluez *self) {
  self->abort();
}

//  void QBluetoothSocketPrivateBluez::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateBluez5closeEv(
    QBluetoothSocketPrivateBluez *self) {
  self->close();
}

//  qint64 QBluetoothSocketPrivateBluez::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN28QBluetoothSocketPrivateBluez9writeDataEPKcx(
    QBluetoothSocketPrivateBluez *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  bool QBluetoothSocketPrivateBluez::setSocketDescriptor(int
//      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
//      QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QBluetoothSocketPrivateBluez19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateBluez *self,
    int socketDescriptor,
    QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState,
    int openMode) {
  return self->setSocketDescriptor(
      socketDescriptor,
      socketType,
      socketState,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  qint64 QBluetoothSocketPrivateBluez::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK28QBluetoothSocketPrivateBluez14bytesAvailableEv(
    const QBluetoothSocketPrivateBluez *self) {
  return self->bytesAvailable();
}

//  bool QBluetoothSocketPrivateBluez::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QBluetoothSocketPrivateBluez11canReadLineEv(
    const QBluetoothSocketPrivateBluez *self) {
  return self->canReadLine();
}

//  qint64 QBluetoothSocketPrivateBluez::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK28QBluetoothSocketPrivateBluez12bytesToWriteEv(
    const QBluetoothSocketPrivateBluez *self) {
  return self->bytesToWrite();
}

//  void QBluetoothSocketPrivateBluez::_q_writeNotify()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateBluez14_q_writeNotifyEv(
    QBluetoothSocketPrivateBluez *self) {
  self->_q_writeNotify();
}
