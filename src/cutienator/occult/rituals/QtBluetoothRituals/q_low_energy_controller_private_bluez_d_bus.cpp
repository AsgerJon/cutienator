//  Written by dev_tooling.RitualGenerator from the records of QtBluetooth/6.
//  12.0/QtBluetooth/private/qlowenergycontroller_bluezdbus_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_bluezdbus_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothaddress.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qlowenergycontrollerbase_p.h"
#include <QtCore/QLoggingCategory>
#include <QtBluetooth/QBluetoothLocalDevice>
#include <QtBluetooth/QLowEnergyCharacteristicData>
#include <QtBluetooth/QLowEnergyDescriptorData>
#include <QtBluetooth/QLowEnergyServiceData>
#include "qlowenergycontroller_bluezdbus_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qlowenergycontrollerbase.cpp, line 22, as _ZN27QLowEnergyControllerPrivateC2Ev
inline QLowEnergyControllerPrivate::QLowEnergyControllerPrivate()
    : QObject()
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

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_bluezdbus.cpp, line 1511, as _ZNK36QLowEnergyControllerPrivateBluezDBus3mtuEv
inline int QLowEnergyControllerPrivateBluezDBus::mtu() const
{
    // currently only supported on peripheral role
    return remoteMtu;
}

//  from ../qtconnectivity/src/bluetooth/qlowenergycontroller_bluezdbus.cpp, line 1454, as _ZN36QLowEnergyControllerPrivateBluezDBus35handlePeripheralRemoteDeviceChangedERK17QBluetoothAddressRK7QStringt
inline void QLowEnergyControllerPrivateBluezDBus::handlePeripheralRemoteDeviceChanged(
        const QBluetoothAddress& address,
        const QString& name,
        quint16 mtu)
{
    remoteDevice = address;
    remoteName = name;
    remoteMtu = mtu;
}
//  -----------------------------------------------------------------------

//  int QLowEnergyControllerPrivateBluezDBus::mtu() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK36QLowEnergyControllerPrivateBluezDBus3mtuEv(
    const QLowEnergyControllerPrivateBluezDBus *self) {
  return self->mtu();
}

//  void QLowEnergyControllerPrivateBluezDBus::handlePeripheralRemoteDeviceCh
//      anged(const QBluetoothAddress &address, const QString &name, quint16
//      mtu)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QLowEnergyControllerPrivateBluezDBus35handlePeripheralRemoteDeviceChangedERK17QBluetoothAddressRK7QStringt(
    QLowEnergyControllerPrivateBluezDBus *self,
    const QBluetoothAddress *address,
    const QString *name,
    quint16 mtu) {
  self->handlePeripheralRemoteDeviceChanged(*address, *name, mtu);
}
