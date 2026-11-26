//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_dummy_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_dummy_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_dummy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/qbluetoothsocketbase_p.h>
#include <QtBluetooth/qbluetoothsocket.h>
#include <QtBluetooth/private/qbluetoothsocket_dummy_p.h>
#ifndef QT_IOS_BLUETOOTH
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocketbase.cpp, line 13, as _ZN27QBluetoothSocketBasePrivateD2Ev
inline QBluetoothSocketBasePrivate::~QBluetoothSocketBasePrivate()
{

}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 20, as _ZN28QBluetoothSocketPrivateDummyD1Ev
inline QBluetoothSocketPrivateDummy::~QBluetoothSocketPrivateDummy()
{
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 30, as _ZN28QBluetoothSocketPrivateDummy22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline void QBluetoothSocketPrivateDummy::connectToServiceHelper(const QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)
{
    Q_UNUSED(openMode);
    Q_UNUSED(address);
    Q_UNUSED(port);
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 37, as _ZN28QBluetoothSocketPrivateDummy16connectToServiceERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline void QBluetoothSocketPrivateDummy::connectToService(
        const QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
{
    Q_UNUSED(service);
    Q_UNUSED(openMode);

    Q_Q(QBluetoothSocket);

    qWarning() << "Using non-functional QBluetoothSocketPrivateDummy";
    errorString = QBluetoothSocket::tr("Socket type not supported");
    q->setSocketError(QBluetoothSocket::SocketError::UnsupportedProtocolError);
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 50, as _ZN28QBluetoothSocketPrivateDummy16connectToServiceERK17QBluetoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline void QBluetoothSocketPrivateDummy::connectToService(
        const QBluetoothAddress &address, const QBluetoothUuid &uuid, QIODevice::OpenMode openMode)
{
    Q_UNUSED(address);
    Q_UNUSED(uuid);
    Q_UNUSED(openMode);

    Q_Q(QBluetoothSocket);

    qWarning() << "Using non-functional QBluetoothSocketPrivateDummy";
    errorString = QBluetoothSocket::tr("Socket type not supported");
    q->setSocketError(QBluetoothSocket::SocketError::UnsupportedProtocolError);
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 64, as _ZN28QBluetoothSocketPrivateDummy16connectToServiceERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline void QBluetoothSocketPrivateDummy::connectToService(
        const QBluetoothAddress &address, quint16 port, QIODevice::OpenMode openMode)
{
    Q_UNUSED(address);
    Q_UNUSED(port);
    Q_UNUSED(openMode);

    Q_Q(QBluetoothSocket);

    qWarning() << "Using non-functional QBluetoothSocketPrivateDummy";
    errorString = QBluetoothSocket::tr("Socket type not supported");
    q->setSocketError(QBluetoothSocket::SocketError::UnsupportedProtocolError);
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 24, as _ZN28QBluetoothSocketPrivateDummy18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE
inline bool QBluetoothSocketPrivateDummy::ensureNativeSocket(QBluetoothServiceInfo::Protocol type)
{
    socketType = type;
    return false;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 82, as _ZNK28QBluetoothSocketPrivateDummy9localNameEv
inline QString QBluetoothSocketPrivateDummy::localName() const
{
    return QString();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 87, as _ZNK28QBluetoothSocketPrivateDummy12localAddressEv
inline QBluetoothAddress QBluetoothSocketPrivateDummy::localAddress() const
{
    return QBluetoothAddress();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 92, as _ZNK28QBluetoothSocketPrivateDummy9localPortEv
inline quint16 QBluetoothSocketPrivateDummy::localPort() const
{
    return 0;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 97, as _ZNK28QBluetoothSocketPrivateDummy8peerNameEv
inline QString QBluetoothSocketPrivateDummy::peerName() const
{
    return QString();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 102, as _ZNK28QBluetoothSocketPrivateDummy11peerAddressEv
inline QBluetoothAddress QBluetoothSocketPrivateDummy::peerAddress() const
{
    return QBluetoothAddress();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 107, as _ZNK28QBluetoothSocketPrivateDummy8peerPortEv
inline quint16 QBluetoothSocketPrivateDummy::peerPort() const
{
    return 0;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 78, as _ZN28QBluetoothSocketPrivateDummy5abortEv
inline void QBluetoothSocketPrivateDummy::abort()
{
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 143, as _ZN28QBluetoothSocketPrivateDummy5closeEv
inline void QBluetoothSocketPrivateDummy::close()
{
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 112, as _ZN28QBluetoothSocketPrivateDummy9writeDataEPKcx
inline qint64 QBluetoothSocketPrivateDummy::writeData(const char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);

    Q_Q(QBluetoothSocket);

    if (state != QBluetoothSocket::SocketState::ConnectedState) {
        errorString = QBluetoothSocket::tr("Cannot write while not connected");
        q->setSocketError(QBluetoothSocket::SocketError::OperationError);
        return -1;
    }
    return -1;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 127, as _ZN28QBluetoothSocketPrivateDummy8readDataEPcx
inline qint64 QBluetoothSocketPrivateDummy::readData(char *data, qint64 maxSize)
{
    Q_UNUSED(data);
    Q_UNUSED(maxSize);

    Q_Q(QBluetoothSocket);

    if (state != QBluetoothSocket::SocketState::ConnectedState) {
        errorString = QBluetoothSocket::tr("Cannot read while not connected");
        q->setSocketError(QBluetoothSocket::SocketError::OperationError);
        return -1;
    }

    return -1;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 147, as _ZN28QBluetoothSocketPrivateDummy19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE
inline bool QBluetoothSocketPrivateDummy::setSocketDescriptor(int socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
                                           QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode openMode)
{
    Q_UNUSED(socketDescriptor);
    Q_UNUSED(socketType);
    Q_UNUSED(socketState);
    Q_UNUSED(openMode);
    return false;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 157, as _ZNK28QBluetoothSocketPrivateDummy14bytesAvailableEv
inline qint64 QBluetoothSocketPrivateDummy::bytesAvailable() const
{
    return 0;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 162, as _ZNK28QBluetoothSocketPrivateDummy11canReadLineEv
inline bool QBluetoothSocketPrivateDummy::canReadLine() const
{
    return false;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_dummy.cpp, line 167, as _ZNK28QBluetoothSocketPrivateDummy12bytesToWriteEv
inline qint64 QBluetoothSocketPrivateDummy::bytesToWrite() const
{
    return 0;
}
//  -----------------------------------------------------------------------

//  QBluetoothSocketPrivateDummy::~QBluetoothSocketPrivateDummy()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummyD1Ev(
    QBluetoothSocketPrivateDummy *self) {
  delete self;
}

//  void QBluetoothSocketPrivateDummy::connectToServiceHelper(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummy22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateDummy *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToServiceHelper(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketPrivateDummy::connectToService(const
//      QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummy16connectToServiceERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateDummy *self,
    const QBluetoothServiceInfo *service,
    int openMode) {
  self->connectToService(
      *service,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketPrivateDummy::connectToService(const
//      QBluetoothAddress &address, const QBluetoothUuid &uuid,
//      QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummy16connectToServiceERK17QBluetoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateDummy *self,
    const QBluetoothAddress *address,
    const QBluetoothUuid *uuid,
    int openMode) {
  self->connectToService(
      *address,
      *uuid,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketPrivateDummy::connectToService(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummy16connectToServiceERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateDummy *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToService(
      *address,
      port,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  bool QBluetoothSocketPrivateDummy::ensureNativeSocket(QBluetoothServiceIn
//      fo::Protocol type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QBluetoothSocketPrivateDummy18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE(
    QBluetoothSocketPrivateDummy *self,
    QBluetoothServiceInfo::Protocol type) {
  return self->ensureNativeSocket(type);
}

//  QString QBluetoothSocketPrivateDummy::localName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QBluetoothSocketPrivateDummy9localNameEv(
    const QBluetoothSocketPrivateDummy *self) {
  return new QString(self->localName());
}

//  QBluetoothAddress QBluetoothSocketPrivateDummy::localAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK28QBluetoothSocketPrivateDummy12localAddressEv(
    const QBluetoothSocketPrivateDummy *self) {
  return new QBluetoothAddress(self->localAddress());
}

//  quint16 QBluetoothSocketPrivateDummy::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK28QBluetoothSocketPrivateDummy9localPortEv(
    const QBluetoothSocketPrivateDummy *self) {
  return self->localPort();
}

//  QString QBluetoothSocketPrivateDummy::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QBluetoothSocketPrivateDummy8peerNameEv(
    const QBluetoothSocketPrivateDummy *self) {
  return new QString(self->peerName());
}

//  QBluetoothAddress QBluetoothSocketPrivateDummy::peerAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK28QBluetoothSocketPrivateDummy11peerAddressEv(
    const QBluetoothSocketPrivateDummy *self) {
  return new QBluetoothAddress(self->peerAddress());
}

//  quint16 QBluetoothSocketPrivateDummy::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK28QBluetoothSocketPrivateDummy8peerPortEv(
    const QBluetoothSocketPrivateDummy *self) {
  return self->peerPort();
}

//  void QBluetoothSocketPrivateDummy::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummy5abortEv(
    QBluetoothSocketPrivateDummy *self) {
  self->abort();
}

//  void QBluetoothSocketPrivateDummy::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateDummy5closeEv(
    QBluetoothSocketPrivateDummy *self) {
  self->close();
}

//  qint64 QBluetoothSocketPrivateDummy::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN28QBluetoothSocketPrivateDummy9writeDataEPKcx(
    QBluetoothSocketPrivateDummy *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  qint64 QBluetoothSocketPrivateDummy::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN28QBluetoothSocketPrivateDummy8readDataEPcx(
    QBluetoothSocketPrivateDummy *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
}

//  bool QBluetoothSocketPrivateDummy::setSocketDescriptor(int
//      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
//      QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QBluetoothSocketPrivateDummy19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketPrivateDummy *self,
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

//  qint64 QBluetoothSocketPrivateDummy::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK28QBluetoothSocketPrivateDummy14bytesAvailableEv(
    const QBluetoothSocketPrivateDummy *self) {
  return self->bytesAvailable();
}

//  bool QBluetoothSocketPrivateDummy::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QBluetoothSocketPrivateDummy11canReadLineEv(
    const QBluetoothSocketPrivateDummy *self) {
  return self->canReadLine();
}

//  qint64 QBluetoothSocketPrivateDummy::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK28QBluetoothSocketPrivateDummy12bytesToWriteEv(
    const QBluetoothSocketPrivateDummy *self) {
  return self->bytesToWrite();
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_dummy_p.h>)
