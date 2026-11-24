//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothhostinfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothhostinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QBluetoothHostInfoPrivate::QBluetoothHostInfoPrivate()
extern "C" Q_DECL_EXPORT
QBluetoothHostInfoPrivate *ritual_ZN25QBluetoothHostInfoPrivateC1Ev() {
  return new QBluetoothHostInfoPrivate();
}

//  QBluetoothHostInfoPrivate::~QBluetoothHostInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QBluetoothHostInfoPrivateD1Ev(
    QBluetoothHostInfoPrivate *self) {
  delete self;
}
