//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/bluez_data_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/bluez_data_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  hci_dev_req::~hci_dev_req()
extern "C" Q_DECL_EXPORT
void ritual_ZN11hci_dev_reqD1Ev(hci_dev_req *self) {
  delete self;
}
