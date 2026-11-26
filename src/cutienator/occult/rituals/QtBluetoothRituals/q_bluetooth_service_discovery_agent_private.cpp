//  Written by dev_tooling.RitualGenerator from the records of QtBluetooth/6.
//  12.0/QtBluetooth/private/qbluetoothservicediscoveryagent_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/qbluetoothservicediscoveryagent.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothservicediscoveryagent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothdeviceinfo.h>
#include <QtBluetooth/qbluetoothserviceinfo.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/qbluetoothhostinfo.h>
#include <QtBluetooth/qbluetoothlocaldevice.h>
#include <QtBluetooth/qbluetoothservicediscoveryagent.h>
#include <QtBluetooth/private/qbluetoothservicediscoveryagent_p.h>
#include <QtBluetooth/qbluetoothdevicediscoveryagent.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qbluetoothservicediscoveryagent.cpp, line 458, as _ZN38QBluetoothServiceDiscoveryAgentPrivate19stopDeviceDiscoveryEv
inline void QBluetoothServiceDiscoveryAgentPrivate::stopDeviceDiscovery()
{
    // disconnect to avoid recursion during stop() - QTBUG-60131
    // we don't care about a potential signals from device discovery agent anymore
    deviceDiscoveryAgent->disconnect();

    deviceDiscoveryAgent->stop();
    delete deviceDiscoveryAgent;
    deviceDiscoveryAgent = nullptr;

    setDiscoveryState(Inactive);

    Q_Q(QBluetoothServiceDiscoveryAgent);
    emit q->canceled();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothservicediscoveryagent.cpp, line 496, as _ZN38QBluetoothServiceDiscoveryAgentPrivate19_q_deviceDiscoveredERK20QBluetoothDeviceInfo
inline void QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscovered(const QBluetoothDeviceInfo &info)
{
    // look for duplicates, and cached entries
    const auto addressEquals = [](const auto &a) {
        return [a](const auto &info) { return info.address() == a; };
    };
    erase_if(discoveredDevices, addressEquals(info.address()));
    discoveredDevices.prepend(info);
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothservicediscoveryagent.cpp, line 506, as _ZN38QBluetoothServiceDiscoveryAgentPrivate23_q_deviceDiscoveryErrorEN30QBluetoothDeviceDiscoveryAgent5ErrorE
inline void QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscoveryError(QBluetoothDeviceDiscoveryAgent::Error newError)
{
    error = static_cast<QBluetoothServiceDiscoveryAgent::Error>(newError);
    errorString = deviceDiscoveryAgent->errorString();

    // disconnect to avoid recursion during stop() - QTBUG-60131
    // we don't care about a potential signals from device discovery agent anymore
    deviceDiscoveryAgent->disconnect();

    deviceDiscoveryAgent->stop();
    delete deviceDiscoveryAgent;
    deviceDiscoveryAgent = nullptr;

    setDiscoveryState(Inactive);
    Q_Q(QBluetoothServiceDiscoveryAgent);
    emit q->errorOccurred(error);
    emit q->finished();
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothservicediscoveryagent.cpp, line 561, as _ZNK38QBluetoothServiceDiscoveryAgentPrivate19isDuplicatedServiceERK21QBluetoothServiceInfo
inline bool QBluetoothServiceDiscoveryAgentPrivate::isDuplicatedService(
        const QBluetoothServiceInfo &serviceInfo) const
{
    //check the service is not already part of our known list
    for (const QBluetoothServiceInfo &info : discoveredServices) {
        if (info.device() == serviceInfo.device()
                && info.serviceClassUuids() == serviceInfo.serviceClassUuids()
                && info.serviceUuid() == serviceInfo.serviceUuid()
                && info.serverChannel() == serviceInfo.serverChannel()) {
            return true;
        }
    }
    return false;
}
//  -----------------------------------------------------------------------

//  QBluetoothServiceDiscoveryAgent
//      *QBluetoothServiceDiscoveryAgentPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgent *ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate6q_funcEv(
    QBluetoothServiceDiscoveryAgentPrivate *self) {
  return self->q_func();
}

//  const QBluetoothServiceDiscoveryAgent
//      *QBluetoothServiceDiscoveryAgentPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothServiceDiscoveryAgent *ritual_ZNK38QBluetoothServiceDiscoveryAgentPrivate6q_funcEv(
    const QBluetoothServiceDiscoveryAgentPrivate *self) {
  return self->q_func();
}

//  void QBluetoothServiceDiscoveryAgentPrivate::stopDeviceDiscovery()
extern "C" Q_DECL_EXPORT
void ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate19stopDeviceDiscoveryEv(
    QBluetoothServiceDiscoveryAgentPrivate *self) {
  self->stopDeviceDiscovery();
}

//  void
//      QBluetoothServiceDiscoveryAgentPrivate::setDiscoveryState(DiscoverySt
//      ate s)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate17setDiscoveryStateENS_14DiscoveryStateE(
    QBluetoothServiceDiscoveryAgentPrivate *self,
    QBluetoothServiceDiscoveryAgentPrivate::DiscoveryState s) {
  self->setDiscoveryState(s);
}

//  DiscoveryState QBluetoothServiceDiscoveryAgentPrivate::discoveryState()
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgentPrivate::DiscoveryState ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate14discoveryStateEv(
    QBluetoothServiceDiscoveryAgentPrivate *self) {
  return self->discoveryState();
}

//  void QBluetoothServiceDiscoveryAgentPrivate::setDiscoveryMode(QBluetoothS
//      erviceDiscoveryAgent::DiscoveryMode m)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate16setDiscoveryModeEN31QBluetoothServiceDiscoveryAgent13DiscoveryModeE(
    QBluetoothServiceDiscoveryAgentPrivate *self,
    QBluetoothServiceDiscoveryAgent::DiscoveryMode m) {
  self->setDiscoveryMode(m);
}

//  QBluetoothServiceDiscoveryAgent::DiscoveryMode
//      QBluetoothServiceDiscoveryAgentPrivate::DiscoveryMode()
extern "C" Q_DECL_EXPORT
QBluetoothServiceDiscoveryAgent::DiscoveryMode ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate13DiscoveryModeEv(
    QBluetoothServiceDiscoveryAgentPrivate *self) {
  return self->DiscoveryMode();
}

//  void QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscovered(const
//      QBluetoothDeviceInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate19_q_deviceDiscoveredERK20QBluetoothDeviceInfo(
    QBluetoothServiceDiscoveryAgentPrivate *self,
    const QBluetoothDeviceInfo *info) {
  self->_q_deviceDiscovered(*info);
}

//  void QBluetoothServiceDiscoveryAgentPrivate::_q_deviceDiscoveryError(QBlu
//      etoothDeviceDiscoveryAgent::Error a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN38QBluetoothServiceDiscoveryAgentPrivate23_q_deviceDiscoveryErrorEN30QBluetoothDeviceDiscoveryAgent5ErrorE(
    QBluetoothServiceDiscoveryAgentPrivate *self,
    QBluetoothDeviceDiscoveryAgent::Error a0) {
  self->_q_deviceDiscoveryError(a0);
}

//  bool QBluetoothServiceDiscoveryAgentPrivate::isDuplicatedService(const
//      QBluetoothServiceInfo &serviceInfo) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK38QBluetoothServiceDiscoveryAgentPrivate19isDuplicatedServiceERK21QBluetoothServiceInfo(
    const QBluetoothServiceDiscoveryAgentPrivate *self,
    const QBluetoothServiceInfo *serviceInfo) {
  return self->isDuplicatedService(*serviceInfo);
}
