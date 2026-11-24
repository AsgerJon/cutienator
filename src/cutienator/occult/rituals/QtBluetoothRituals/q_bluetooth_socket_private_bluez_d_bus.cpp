//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbluetoothsocketbase_p.h"
#include "qbluetoothsocket.h"
#include "qbluetoothsocket_bluezdbus_p.h"
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qrandom.h>
#include <QtNetwork/qlocalsocket.h>
#include <unistd.h>
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

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 56, as _ZN32QBluetoothSocketPrivateBluezDBus22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline void QBluetoothSocketPrivateBluezDBus::connectToServiceHelper(
        const QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)
{
    // TODO Remove when Bluez4 support dropped
    // Only used by QBluetoothSocketPrivateBluez
    Q_UNUSED(openMode);
    Q_UNUSED(address);
    Q_UNUSED(port);
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 42, as _ZN32QBluetoothSocketPrivateBluezDBus18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE
inline bool QBluetoothSocketPrivateBluezDBus::ensureNativeSocket(QBluetoothServiceInfo::Protocol type)
{
    switch (type) {
    case QBluetoothServiceInfo::UnknownProtocol:
        break;
    case QBluetoothServiceInfo::RfcommProtocol:
    case QBluetoothServiceInfo::L2capProtocol:
        socketType = type;
        return true;
    }

    return false;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 445, as _ZN32QBluetoothSocketPrivateBluezDBus9writeDataEPKcx
inline qint64 QBluetoothSocketPrivateBluezDBus::writeData(const char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);

    Q_Q(QBluetoothSocket);

    if (state != QBluetoothSocket::SocketState::ConnectedState) {
        errorString = QBluetoothSocket::tr("Cannot write while not connected");
        q->setSocketError(QBluetoothSocket::SocketError::OperationError);
        return -1;
    }

    if (localSocket)
        return localSocket->write(data, maxSize);

    return -1;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 488, as _ZN32QBluetoothSocketPrivateBluezDBus19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline bool QBluetoothSocketPrivateBluezDBus::setSocketDescriptor(int socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
                                           QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode openMode)
{
    Q_UNUSED(socketDescriptor);
    Q_UNUSED(socketType);
    Q_UNUSED(socketState);
    Q_UNUSED(openMode);
    return false;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 498, as _ZNK32QBluetoothSocketPrivateBluezDBus14bytesAvailableEv
inline qint64 QBluetoothSocketPrivateBluezDBus::bytesAvailable() const
{
    if (localSocket)
        return localSocket->bytesAvailable();

    return 0;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 506, as _ZNK32QBluetoothSocketPrivateBluezDBus11canReadLineEv
inline bool QBluetoothSocketPrivateBluezDBus::canReadLine() const
{
    if (localSocket)
        return localSocket->canReadLine();

    return false;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 514, as _ZNK32QBluetoothSocketPrivateBluezDBus12bytesToWriteEv
inline qint64 QBluetoothSocketPrivateBluezDBus::bytesToWrite() const
{
    if (localSocket)
        return localSocket->bytesToWrite();

    return 0;
}
//  -----------------------------------------------------------------------

//  void QBluetoothSocketPrivateBluezDBus::connectToServiceHelper(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QBluetoothSocketPrivateBluezDBus22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateBluezDBus *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToServiceHelper(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  bool QBluetoothSocketPrivateBluezDBus::ensureNativeSocket(QBluetoothServi
//      ceInfo::Protocol type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QBluetoothSocketPrivateBluezDBus18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE(
    QBluetoothSocketPrivateBluezDBus *self,
    QBluetoothServiceInfo::Protocol type) {
  return self->ensureNativeSocket(type);
}

//  qint64 QBluetoothSocketPrivateBluezDBus::writeData(const char *data,
//      qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN32QBluetoothSocketPrivateBluezDBus9writeDataEPKcx(
    QBluetoothSocketPrivateBluezDBus *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  bool QBluetoothSocketPrivateBluezDBus::setSocketDescriptor(int
//      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
//      QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN32QBluetoothSocketPrivateBluezDBus19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateBluezDBus *self,
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

//  qint64 QBluetoothSocketPrivateBluezDBus::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK32QBluetoothSocketPrivateBluezDBus14bytesAvailableEv(
    const QBluetoothSocketPrivateBluezDBus *self) {
  return self->bytesAvailable();
}

//  bool QBluetoothSocketPrivateBluezDBus::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK32QBluetoothSocketPrivateBluezDBus11canReadLineEv(
    const QBluetoothSocketPrivateBluezDBus *self) {
  return self->canReadLine();
}

//  qint64 QBluetoothSocketPrivateBluezDBus::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK32QBluetoothSocketPrivateBluezDBus12bytesToWriteEv(
    const QBluetoothSocketPrivateBluezDBus *self) {
  return self->bytesToWrite();
}
