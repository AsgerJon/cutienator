//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/bluez_data_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/bluez_data_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  hci_dev_stats::~hci_dev_stats()
extern "C" Q_DECL_EXPORT
void ritual_ZN13hci_dev_statsD1Ev(hci_dev_stats *self) {
  delete self;
}
