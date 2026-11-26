//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_dummy_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_dummy_p.h>)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_dummy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothuuid.h>
#include <QtBluetooth/qlowenergyadvertisingparameters.h>
#include <QtBluetooth/qlowenergyadvertisingdata.h>
#include <QtBluetooth/qlowenergyconnectionparameters.h>
#include <QtCore/qbytearray.h>
#include <QtBluetooth/qlowenergyservicedata.h>
#include <QtCore/QSharedPointer>
#include <QtCore/QByteArray>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/private/qlowenergycontrollerbase_p.h>
#include <QtCore/QLoggingCategory>
#include <QtBluetooth/QBluetoothLocalDevice>
#include <QtBluetooth/QLowEnergyCharacteristicData>
#include <QtBluetooth/QLowEnergyDescriptorData>
#include <QtBluetooth/QLowEnergyServiceData>
#include <QtBluetooth/private/qlowenergycontroller_dummy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 27, as _ZN27QLowEnergyControllerPrivateD2Ev
inline QLowEnergyControllerPrivate::~QLowEnergyControllerPrivate()
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 53, as _ZN27QLowEnergyControllerPrivate8setErrorEN20QLowEnergyController5ErrorE
inline void QLowEnergyControllerPrivate::setError(
        QLowEnergyController::Error newError)
{
    Q_Q(QLowEnergyController);
    error = newError;

    switch (newError) {
    case QLowEnergyController::UnknownRemoteDeviceError:
        errorString = QLowEnergyController::tr("Remote device cannot be found");
        break;
    case QLowEnergyController::InvalidBluetoothAdapterError:
        errorString = QLowEnergyController::tr("Cannot find local adapter");
        break;
    case QLowEnergyController::NetworkError:
        errorString = QLowEnergyController::tr("Error occurred during connection I/O");
        break;
    case QLowEnergyController::ConnectionError:
        errorString = QLowEnergyController::tr("Error occurred trying to connect to remote device.");
        break;
    case QLowEnergyController::AdvertisingError:
        errorString = QLowEnergyController::tr("Error occurred trying to start advertising");
        break;
    case QLowEnergyController::RemoteHostClosedError:
        errorString = QLowEnergyController::tr("Remote device closed the connection");
        break;
    case QLowEnergyController::AuthorizationError:
        errorString = QLowEnergyController::tr("Failed to authorize on the remote device");
        break;
    case QLowEnergyController::MissingPermissionsError:
        errorString = QLowEnergyController::tr("Missing permissions error");
        break;
    case QLowEnergyController::RssiReadError:
        errorString = QLowEnergyController::tr("Error reading RSSI value");
        break;
    case QLowEnergyController::NoError:
        return;
    default:
    case QLowEnergyController::UnknownError:
        errorString = QLowEnergyController::tr("Unknown Error");
        break;
    }

    emit q->errorOccurred(newError);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 20, as _ZN33QLowEnergyControllerPrivateCommon4initEv
inline void QLowEnergyControllerPrivateCommon::init()
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 24, as _ZN33QLowEnergyControllerPrivateCommon15connectToDeviceEv
inline void QLowEnergyControllerPrivateCommon::connectToDevice()
{
    // required to pass unit test on default backend
    if (remoteDevice.isNull()) {
        qWarning() << "Invalid/null remote device address";
        setError(QLowEnergyController::UnknownRemoteDeviceError);
        return;
    }

    qWarning() << "QLowEnergyControllerPrivateCommon::connectToDevice(): Not implemented";
    setError(QLowEnergyController::UnknownError);
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 37, as _ZN33QLowEnergyControllerPrivateCommon20disconnectFromDeviceEv
inline void QLowEnergyControllerPrivateCommon::disconnectFromDevice()
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 42, as _ZN33QLowEnergyControllerPrivateCommon16discoverServicesEv
inline void QLowEnergyControllerPrivateCommon::discoverServices()
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 47, as _ZN33QLowEnergyControllerPrivateCommon22discoverServiceDetailsERK14QBluetoothUuidN17QLowEnergyService13DiscoveryModeE
inline void QLowEnergyControllerPrivateCommon::discoverServiceDetails(
        const QBluetoothUuid & /*service*/, QLowEnergyService::DiscoveryMode /*mode*/)
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 83, as _ZN33QLowEnergyControllerPrivateCommon16startAdvertisingERK31QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_
inline void QLowEnergyControllerPrivateCommon::startAdvertising(const QLowEnergyAdvertisingParameters &/* params */,
        const QLowEnergyAdvertisingData &/* advertisingData */,
        const QLowEnergyAdvertisingData &/* scanResponseData */)
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 89, as _ZN33QLowEnergyControllerPrivateCommon15stopAdvertisingEv
inline void QLowEnergyControllerPrivateCommon::stopAdvertising()
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 93, as _ZN33QLowEnergyControllerPrivateCommon23requestConnectionUpdateERK30QLowEnergyConnectionParameters
inline void QLowEnergyControllerPrivateCommon::requestConnectionUpdate(const QLowEnergyConnectionParameters & /* params */)
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 53, as _ZN33QLowEnergyControllerPrivateCommon18readCharacteristicE14QSharedPointerI24QLowEnergyServicePrivateEt
inline void QLowEnergyControllerPrivateCommon::readCharacteristic(const QSharedPointer<QLowEnergyServicePrivate> /*service*/,
                        const QLowEnergyHandle /*charHandle*/)
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 59, as _ZN33QLowEnergyControllerPrivateCommon14readDescriptorE14QSharedPointerI24QLowEnergyServicePrivateEtt
inline void QLowEnergyControllerPrivateCommon::readDescriptor(const QSharedPointer<QLowEnergyServicePrivate> /*service*/,
                    const QLowEnergyHandle /*charHandle*/,
                    const QLowEnergyHandle /*descriptorHandle*/)
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 66, as _ZN33QLowEnergyControllerPrivateCommon19writeCharacteristicE14QSharedPointerI24QLowEnergyServicePrivateEtRK10QByteArrayN17QLowEnergyService9WriteModeE
inline void QLowEnergyControllerPrivateCommon::writeCharacteristic(const QSharedPointer<QLowEnergyServicePrivate> /*service*/,
        const QLowEnergyHandle /*charHandle*/,
        const QByteArray &/*newValue*/,
        QLowEnergyService::WriteMode /*writeMode*/)
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 74, as _ZN33QLowEnergyControllerPrivateCommon15writeDescriptorE14QSharedPointerI24QLowEnergyServicePrivateEttRK10QByteArray
inline void QLowEnergyControllerPrivateCommon::writeDescriptor(
        const QSharedPointer<QLowEnergyServicePrivate> /*service*/,
        const QLowEnergyHandle /*charHandle*/,
        const QLowEnergyHandle /*descriptorHandle*/,
        const QByteArray &/*newValue*/)
{

}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 97, as _ZN33QLowEnergyControllerPrivateCommon25addToGenericAttributeListERK21QLowEnergyServiceDatat
inline void QLowEnergyControllerPrivateCommon::addToGenericAttributeList(const QLowEnergyServiceData &/* service */,
                                                            QLowEnergyHandle /* startHandle */)
{
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_dummy.cpp, line 102, as _ZNK33QLowEnergyControllerPrivateCommon3mtuEv
inline int QLowEnergyControllerPrivateCommon::mtu() const
{
    // not supported
    return -1;
}
//  -----------------------------------------------------------------------

//  void QLowEnergyControllerPrivateCommon::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon4initEv(
    QLowEnergyControllerPrivateCommon *self) {
  self->init();
}

//  void QLowEnergyControllerPrivateCommon::connectToDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon15connectToDeviceEv(
    QLowEnergyControllerPrivateCommon *self) {
  self->connectToDevice();
}

//  void QLowEnergyControllerPrivateCommon::disconnectFromDevice()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon20disconnectFromDeviceEv(
    QLowEnergyControllerPrivateCommon *self) {
  self->disconnectFromDevice();
}

//  void QLowEnergyControllerPrivateCommon::discoverServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon16discoverServicesEv(
    QLowEnergyControllerPrivateCommon *self) {
  self->discoverServices();
}

//  void QLowEnergyControllerPrivateCommon::discoverServiceDetails(const
//      QBluetoothUuid &service, QLowEnergyService::DiscoveryMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon22discoverServiceDetailsERK14QBluetoothUuidN17QLowEnergyService13DiscoveryModeE(
    QLowEnergyControllerPrivateCommon *self,
    const QBluetoothUuid *service,
    QLowEnergyService::DiscoveryMode mode) {
  self->discoverServiceDetails(*service, mode);
}

//  void QLowEnergyControllerPrivateCommon::startAdvertising(const
//      QLowEnergyAdvertisingParameters &params, const
//      QLowEnergyAdvertisingData &advertisingData, const
//      QLowEnergyAdvertisingData &scanResponseData)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon16startAdvertisingERK31QLowEnergyAdvertisingParametersRK25QLowEnergyAdvertisingDataS5_(
    QLowEnergyControllerPrivateCommon *self,
    const QLowEnergyAdvertisingParameters *params,
    const QLowEnergyAdvertisingData *advertisingData,
    const QLowEnergyAdvertisingData *scanResponseData) {
  self->startAdvertising(*params, *advertisingData, *scanResponseData);
}

//  void QLowEnergyControllerPrivateCommon::stopAdvertising()
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon15stopAdvertisingEv(
    QLowEnergyControllerPrivateCommon *self) {
  self->stopAdvertising();
}

//  void QLowEnergyControllerPrivateCommon::requestConnectionUpdate(const
//      QLowEnergyConnectionParameters &params)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon23requestConnectionUpdateERK30QLowEnergyConnectionParameters(
    QLowEnergyControllerPrivateCommon *self,
    const QLowEnergyConnectionParameters *params) {
  self->requestConnectionUpdate(*params);
}

//  void QLowEnergyControllerPrivateCommon::readCharacteristic(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon18readCharacteristicE14QSharedPointerI24QLowEnergyServicePrivateEt(
    QLowEnergyControllerPrivateCommon *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle) {
  self->readCharacteristic(*service, charHandle);
}

//  void QLowEnergyControllerPrivateCommon::readDescriptor(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle, const QLowEnergyHandle descriptorHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon14readDescriptorE14QSharedPointerI24QLowEnergyServicePrivateEtt(
    QLowEnergyControllerPrivateCommon *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle,
    QLowEnergyHandle descriptorHandle) {
  self->readDescriptor(*service, charHandle, descriptorHandle);
}

//  void QLowEnergyControllerPrivateCommon::writeCharacteristic(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle, const QByteArray &newValue,
//      QLowEnergyService::WriteMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon19writeCharacteristicE14QSharedPointerI24QLowEnergyServicePrivateEtRK10QByteArrayN17QLowEnergyService9WriteModeE(
    QLowEnergyControllerPrivateCommon *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle,
    const QByteArray *newValue,
    QLowEnergyService::WriteMode mode) {
  self->writeCharacteristic(*service, charHandle, *newValue, mode);
}

//  void QLowEnergyControllerPrivateCommon::writeDescriptor(const
//      QSharedPointer<QLowEnergyServicePrivate> service, const
//      QLowEnergyHandle charHandle, const QLowEnergyHandle descriptorHandle,
//      const QByteArray &newValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon15writeDescriptorE14QSharedPointerI24QLowEnergyServicePrivateEttRK10QByteArray(
    QLowEnergyControllerPrivateCommon *self,
    const QSharedPointer<QLowEnergyServicePrivate> *service,
    QLowEnergyHandle charHandle,
    QLowEnergyHandle descriptorHandle,
    const QByteArray *newValue) {
  self->writeDescriptor(*service, charHandle, descriptorHandle, *newValue);
}

//  void QLowEnergyControllerPrivateCommon::addToGenericAttributeList(const
//      QLowEnergyServiceData &service, QLowEnergyHandle startHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN33QLowEnergyControllerPrivateCommon25addToGenericAttributeListERK21QLowEnergyServiceDatat(
    QLowEnergyControllerPrivateCommon *self,
    const QLowEnergyServiceData *service,
    QLowEnergyHandle startHandle) {
  self->addToGenericAttributeList(*service, startHandle);
}

//  int QLowEnergyControllerPrivateCommon::mtu() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK33QLowEnergyControllerPrivateCommon3mtuEv(
    const QLowEnergyControllerPrivateCommon *self) {
  return self->mtu();
}

#endif  // __has_include(<QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_dummy_p.h>)
