//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/bluez_data_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if QT_CONFIG(bluez)
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/bluez_data_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bt_security::~bt_security()
extern "C" Q_DECL_EXPORT
void ritual_ZN11bt_securityD1Ev(bt_security *self) {
  delete self;
}

#endif  // QT_CONFIG(bluez)
