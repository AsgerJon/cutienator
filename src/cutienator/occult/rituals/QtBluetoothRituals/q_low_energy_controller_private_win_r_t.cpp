//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_winrt_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. Qt builds QtBluetooth for Windows with
//  'QT_WINRT_BLUETOOTH' defined, and its headers declare these classes, and
//  lay out their bases, only under it: it is defined here the same way.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object. It is final, so
//  'self' is taken as a QLowEnergyControllerPrivate, and the calls stay
//  virtual. Not written: the constructor, 'tr', the signals, the
//  slots, and 'readCharacteristic', 'readDescriptor',
//  'writeCharacteristic' and 'writeDescriptor', which take a
//  'QSharedPointer'.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
#ifndef QT_WINRT_BLUETOOTH
#define QT_WINRT_BLUETOOTH
#endif  // QT_WINRT_BLUETOOTH
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_winrt_p.h>
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qlowenergyadvertisingdata.h>
#include <QtBluetooth/qlowenergyadvertisingparameters.h>
#include <QtBluetooth/qlowenergyconnectionparameters.h>
#include <QtBluetooth/qlowenergyservice.h>
#include <QtBluetooth/qlowenergyservicedata.h>

//  const QMetaObject *QLowEnergyControllerPrivateWinRT::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK32QLowEnergyControllerPrivateWinRT10metaObjectEv(
    const QLowEnergyControllerPrivate *self) {
  return self->metaObject();
}

//  QLowEnergyControllerPrivateWinRT::~QLowEnergyControllerPrivateWinRT()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRTD1Ev(
    QLowEnergyControllerPrivate *self) {
  delete self;
}

//  void QLowEnergyControllerPrivateWinRT::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT4initEv(
    QLowEnergyControllerPrivate *self) {
  self->init();
}

//  void QLowEnergyControllerPrivateWinRT::connectToDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT15connectToDeviceEv(
    QLowEnergyControllerPrivate *self) {
  self->connectToDevice();
}

//  void QLowEnergyControllerPrivateWinRT::disconnectFromDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT20disconnectFromDeviceEv(
    QLowEnergyControllerPrivate *self) {
  self->disconnectFromDevice();
}

//  void QLowEnergyControllerPrivateWinRT::discoverServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT16discoverServicesEv(
    QLowEnergyControllerPrivate *self) {
  self->discoverServices();
}

//  void QLowEnergyControllerPrivateWinRT::discoverServiceDetails(const
//      QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT22discoverServiceDetailsERK14QBluetoothUuidN17QLowEnergyService13DiscoveryModeE(
    QLowEnergyControllerPrivate *self,
    const QBluetoothUuid *service,
    QLowEnergyService::DiscoveryMode mode) {
  self->discoverServiceDetails(*service, mode);
}

//  void QLowEnergyControllerPrivateWinRT::startAdvertising(const
//      QLowEnergyAdvertisingParameters &params, const
//      QLowEnergyAdvertisingData &advertisingData, const
//      QLowEnergyAdvertisingData &scanResponseData)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT16startAdvertisingERK31QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyAdvertisingParameters *params,
    const QLowEnergyAdvertisingData *advertisingData,
    const QLowEnergyAdvertisingData *scanResponseData) {
  self->startAdvertising(*params, *advertisingData, *scanResponseData);
}

//  void QLowEnergyControllerPrivateWinRT::stopAdvertising()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT15stopAdvertisingEv(
    QLowEnergyControllerPrivate *self) {
  self->stopAdvertising();
}

//  void QLowEnergyControllerPrivateWinRT::requestConnectionUpdate(const
//      QLowEnergyConnectionParameters &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT23requestConnectionUpdateERK30QLowEnergyConnectionParameters(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyConnectionParameters *params) {
  self->requestConnectionUpdate(*params);
}

//  void QLowEnergyControllerPrivateWinRT::addToGenericAttributeList(const
//      QLowEnergyServiceData &service, QLowEnergyHandle startHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT25addToGenericAttributeListERK21QLowEnergyServiceDatat(
    QLowEnergyControllerPrivate *self,
    const QLowEnergyServiceData *service,
    QLowEnergyHandle startHandle) {
  self->addToGenericAttributeList(*service, startHandle);
}

//  int QLowEnergyControllerPrivateWinRT::mtu() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK32QLowEnergyControllerPrivateWinRT3mtuEv(
    const QLowEnergyControllerPrivate *self) {
  return self->mtu();
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
