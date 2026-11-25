//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothdevicewatcher_winrt_p.h,
//  Qt 6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. Qt builds QtBluetooth for Windows with
//  'QT_WINRT_BLUETOOTH' defined, and its headers declare these classes, and
//  lay out their bases, only under it: it is defined here the same way.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object. Not written: the
//  constructors, 'init', 'start', 'stop', 'tr' and the signals.
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
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothdevicewatcher_winrt_p.h>

//  const QMetaObject *QBluetoothDeviceWatcherWinRT::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QBluetoothDeviceWatcherWinRT10metaObjectEv(
    const QBluetoothDeviceWatcherWinRT *self) {
  return self->metaObject();
}

//  QBluetoothDeviceWatcherWinRT::~QBluetoothDeviceWatcherWinRT()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothDeviceWatcherWinRTD1Ev(
    QBluetoothDeviceWatcherWinRT *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
