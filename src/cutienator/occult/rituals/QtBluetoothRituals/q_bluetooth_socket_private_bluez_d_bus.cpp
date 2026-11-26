//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothaddress.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/qbluetoothsocketbase_p.h>
#include <QtBluetooth/qbluetoothsocket.h>
#include <QtBluetooth/private/qbluetoothsocket_bluezdbus_p.h>
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qrandom.h>
#include <QtNetwork/qlocalsocket.h>
#include <unistd.h>
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

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocketbase.cpp, line 8, as _ZN27QBluetoothSocketBasePrivateC2EP7QObject
inline QBluetoothSocketBasePrivate::QBluetoothSocketBasePrivate(QObject *parent) : QObject(parent)
{

}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocketbase.cpp, line 13, as _ZN27QBluetoothSocketBasePrivateD2Ev
inline QBluetoothSocketBasePrivate::~QBluetoothSocketBasePrivate()
{

}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 38, as _ZN32QBluetoothSocketPrivateBluezDBusD1Ev
inline QBluetoothSocketPrivateBluezDBus::~QBluetoothSocketPrivateBluezDBus()
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

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluezdbus.cpp, line 464, as _ZN32QBluetoothSocketPrivateBluezDBus8readDataEPcx
inline qint64 QBluetoothSocketPrivateBluezDBus::readData(char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);

    Q_Q(QBluetoothSocket);

    if (state != QBluetoothSocket::SocketState::ConnectedState) {
        errorString = QBluetoothSocket::tr("Cannot read while not connected");
        q->setSocketError(QBluetoothSocket::SocketError::OperationError);
        return -1;
    }

    if (localSocket)
        return localSocket->read(data, maxSize);

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

//  QBluetoothSocketPrivateBluezDBus::~QBluetoothSocketPrivateBluezDBus()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QBluetoothSocketPrivateBluezDBusD1Ev(
    QBluetoothSocketPrivateBluezDBus *self) {
  delete self;
}

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

//  qint64 QBluetoothSocketPrivateBluezDBus::readData(char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN32QBluetoothSocketPrivateBluezDBus8readDataEPcx(
    QBluetoothSocketPrivateBluezDBus *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
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

#endif  // QT_CONFIG(bluez)
