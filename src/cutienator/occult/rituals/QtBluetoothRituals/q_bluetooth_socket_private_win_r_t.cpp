//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_winrt_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. Qt builds QtBluetooth for Windows with
//  'QT_WINRT_BLUETOOTH' defined, and its headers declare these classes, and
//  lay out their bases, only under it: it is defined here the same way.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object. It is final, so
//  'self' is taken as a QBluetoothSocketBasePrivate, and the calls stay
//  virtual. Not written: the constructor, 'addToPendingData', 'tr',
//  the slots, and the 'setSocketDescriptor' that takes a
//  'Microsoft::WRL::ComPtr'.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
#ifndef QT_WINRT_BLUETOOTH
#define QT_WINRT_BLUETOOTH
#endif  // QT_WINRT_BLUETOOTH
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothsocket_winrt_p.h>
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QBluetoothSocketPrivateWinRT::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QBluetoothSocketPrivateWinRT10metaObjectEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->metaObject();
}

//  QBluetoothSocketPrivateWinRT::~QBluetoothSocketPrivateWinRT()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRTD1Ev(
    QBluetoothSocketBasePrivate *self) {
  delete self;
}

//  void QBluetoothSocketPrivateWinRT::connectToServiceHelper(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRT22connectToServiceHelperERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToServiceHelper(*address, port, QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketPrivateWinRT::connectToService(const
//      QBluetoothServiceInfo &service, QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRT16connectToServiceERK21QBluetoothServiceInfo6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothServiceInfo *service,
    int openMode) {
  self->connectToService(*service, QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketPrivateWinRT::connectToService(const
//      QBluetoothAddress &address, const QBluetoothUuid &uuid,
//      QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRT16connectToServiceERK17QBluetoothAddressRK14QBluetoothUuid6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothAddress *address,
    const QBluetoothUuid *uuid,
    int openMode) {
  self->connectToService(*address, *uuid, QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QBluetoothSocketPrivateWinRT::connectToService(const
//      QBluetoothAddress &address, quint16 port, QIODevice::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRT16connectToServiceERK17QBluetoothAddresst6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    const QBluetoothAddress *address,
    quint16 port,
    int openMode) {
  self->connectToService(*address, port, QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  bool QBluetoothSocketPrivateWinRT::ensureNativeSocket(QBluetoothServiceIn
//      fo::Protocol type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QBluetoothSocketPrivateWinRT18ensureNativeSocketEN21QBluetoothServiceInfo8ProtocolE(
    QBluetoothSocketBasePrivate *self,
    QBluetoothServiceInfo::Protocol type) {
  return self->ensureNativeSocket(type);
}

//  QString QBluetoothSocketPrivateWinRT::localName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QBluetoothSocketPrivateWinRT9localNameEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QString(self->localName());
}

//  QBluetoothAddress QBluetoothSocketPrivateWinRT::localAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK28QBluetoothSocketPrivateWinRT12localAddressEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QBluetoothAddress(self->localAddress());
}

//  quint16 QBluetoothSocketPrivateWinRT::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK28QBluetoothSocketPrivateWinRT9localPortEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->localPort();
}

//  QString QBluetoothSocketPrivateWinRT::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QBluetoothSocketPrivateWinRT8peerNameEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QString(self->peerName());
}

//  QBluetoothAddress QBluetoothSocketPrivateWinRT::peerAddress() const
extern "C" Q_DECL_EXPORT
QBluetoothAddress *ritual_ZNK28QBluetoothSocketPrivateWinRT11peerAddressEv(
    const QBluetoothSocketBasePrivate *self) {
  return new QBluetoothAddress(self->peerAddress());
}

//  quint16 QBluetoothSocketPrivateWinRT::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK28QBluetoothSocketPrivateWinRT8peerPortEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->peerPort();
}

//  void QBluetoothSocketPrivateWinRT::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRT5abortEv(
    QBluetoothSocketBasePrivate *self) {
  self->abort();
}

//  void QBluetoothSocketPrivateWinRT::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothSocketPrivateWinRT5closeEv(
    QBluetoothSocketBasePrivate *self) {
  self->close();
}

//  qint64 QBluetoothSocketPrivateWinRT::writeData(const char *data, qint64
//      maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN28QBluetoothSocketPrivateWinRT9writeDataEPKcx(
    QBluetoothSocketBasePrivate *self,
    const char *data,
    qint64 maxSize) {
  return self->writeData(data, maxSize);
}

//  qint64 QBluetoothSocketPrivateWinRT::readData(char *data, qint64 maxSize)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN28QBluetoothSocketPrivateWinRT8readDataEPcx(
    QBluetoothSocketBasePrivate *self,
    char *data,
    qint64 maxSize) {
  return self->readData(data, maxSize);
}

//  bool QBluetoothSocketPrivateWinRT::setSocketDescriptor(int
//      socketDescriptor, QBluetoothServiceInfo::Protocol socketType,
//      QBluetoothSocket::SocketState socketState, QBluetoothSocket::OpenMode
//      openMode)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QBluetoothSocketPrivateWinRT19setSocketDescriptorEiN21QBluetoothServiceInfo8ProtocolEN16QBluetoothSocket11SocketStateE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QBluetoothSocketBasePrivate *self,
    int socketDescriptor,
    QBluetoothServiceInfo::Protocol socketType,
    QBluetoothSocket::SocketState socketState,
    int openMode) {
  return self->setSocketDescriptor(
      socketDescriptor, socketType, socketState,
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  qint64 QBluetoothSocketPrivateWinRT::bytesAvailable() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK28QBluetoothSocketPrivateWinRT14bytesAvailableEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->bytesAvailable();
}

//  bool QBluetoothSocketPrivateWinRT::canReadLine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QBluetoothSocketPrivateWinRT11canReadLineEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->canReadLine();
}

//  qint64 QBluetoothSocketPrivateWinRT::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK28QBluetoothSocketPrivateWinRT12bytesToWriteEv(
    const QBluetoothSocketBasePrivate *self) {
  return self->bytesToWrite();
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
