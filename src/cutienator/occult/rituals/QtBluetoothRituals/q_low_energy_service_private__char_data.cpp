//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergyserviceprivate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLowEnergyServicePrivate::CharData::~CharData()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QLowEnergyServicePrivate8CharDataD1Ev(
    QLowEnergyServicePrivate::CharData *self) {
  delete self;
}
