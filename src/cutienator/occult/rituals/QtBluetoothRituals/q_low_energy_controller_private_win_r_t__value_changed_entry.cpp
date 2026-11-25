//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_winrt_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. Qt builds QtBluetooth for Windows with
//  'QT_WINRT_BLUETOOTH' defined, and its headers declare these classes, and
//  lay out their bases, only under it: it is defined here the same way.
//  A 'GattCharacteristic' and a 'winrt::event_token' are passed
//  as addresses. Not written: 'operator='.
//  Edited by hand on 2026-11-25: compiled by C++20, as the next line
//  asks 'Summon': Qt's C++/WinRT headers wait with coroutines, which
//  'clang++' has only from C++20 on.
//  Summon: -std=c++20
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
#ifndef QT_WINRT_BLUETOOTH
#define QT_WINRT_BLUETOOTH
#endif  // QT_WINRT_BLUETOOTH
#include <QtBluetooth/6.12.0/QtBluetooth/private/qlowenergycontroller_winrt_p.h>

//  QLowEnergyControllerPrivateWinRT::ValueChangedEntry::ValueChangedEntry()
extern "C" Q_DECL_EXPORT
QLowEnergyControllerPrivateWinRT::ValueChangedEntry *ritual_ZN32QLowEnergyControllerPrivateWinRT17ValueChangedEntryC1Ev() {
  return new QLowEnergyControllerPrivateWinRT::ValueChangedEntry();
}

//  QLowEnergyControllerPrivateWinRT::ValueChangedEntry::ValueChangedEntry(Ga
//      ttCharacteristic c, winrt::event_token t)
extern "C" Q_DECL_EXPORT
QLowEnergyControllerPrivateWinRT::ValueChangedEntry *ritual_ZN32QLowEnergyControllerPrivateWinRT17ValueChangedEntryC1EN5winrt7Windows7Devices9Bluetooth23GenericAttributeProfile18GattCharacteristicENS1_11event_tokenE(
    const winrt::Windows::Devices::Bluetooth::GenericAttributeProfile::GattCharacteristic *c,
    const winrt::event_token *t) {
  return new QLowEnergyControllerPrivateWinRT::ValueChangedEntry(*c, *t);
}

//  QLowEnergyControllerPrivateWinRT::ValueChangedEntry::ValueChangedEntry(co
//      nst ValueChangedEntry &other)
extern "C" Q_DECL_EXPORT
QLowEnergyControllerPrivateWinRT::ValueChangedEntry *ritual_ZN32QLowEnergyControllerPrivateWinRT17ValueChangedEntryC1ERKS0_(
    const QLowEnergyControllerPrivateWinRT::ValueChangedEntry *other) {
  return new QLowEnergyControllerPrivateWinRT::ValueChangedEntry(*other);
}

//  QLowEnergyControllerPrivateWinRT::ValueChangedEntry::~ValueChangedEntry()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QLowEnergyControllerPrivateWinRT17ValueChangedEntryD1Ev(
    QLowEnergyControllerPrivateWinRT::ValueChangedEntry *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
