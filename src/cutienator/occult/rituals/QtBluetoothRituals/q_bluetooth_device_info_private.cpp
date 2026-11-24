//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothdeviceinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothdeviceinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbluetoothdeviceinfo.h"
#include "qbluetoothdeviceinfo_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qbluetoothdeviceinfo.cpp, line 234, as _ZN27QBluetoothDeviceInfoPrivateC1Ev
inline QBluetoothDeviceInfoPrivate::QBluetoothDeviceInfoPrivate()
{
}
//  -----------------------------------------------------------------------

//  QBluetoothDeviceInfoPrivate::QBluetoothDeviceInfoPrivate()
extern "C" Q_DECL_EXPORT
QBluetoothDeviceInfoPrivate *ritual_ZN27QBluetoothDeviceInfoPrivateC1Ev() {
  return new QBluetoothDeviceInfoPrivate();
}

//  QBluetoothDeviceInfoPrivate::~QBluetoothDeviceInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QBluetoothDeviceInfoPrivateD1Ev(
    QBluetoothDeviceInfoPrivate *self) {
  delete self;
}
