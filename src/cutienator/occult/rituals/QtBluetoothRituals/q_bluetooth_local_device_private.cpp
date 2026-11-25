//  Written by hand on 2026-11-25 from
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothlocaldevice_p.h, Qt
//  6.12.0, as the Qt of Windows installs it. Kept as it is when the
//  generator runs again. Qt builds QtBluetooth for Windows with
//  'QT_WINRT_BLUETOOTH' defined, and its headers declare these classes, and
//  lay out their bases, only under it: it is defined here the same way.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object. Not written: the
//  constructor, 'isValid', 'updateAdapterState', 'tr', the slots and
//  the signal. The Qt of macOS is built with 'QT_OSX_BLUETOOTH', under
//  which this header declares no class.
#include <QtBluetooth/qtbluetoothglobal.h>
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#if defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
#ifndef QT_WINRT_BLUETOOTH
#define QT_WINRT_BLUETOOTH
#endif  // QT_WINRT_BLUETOOTH
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothlocaldevice_p.h>

//  const QMetaObject *QBluetoothLocalDevicePrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QBluetoothLocalDevicePrivate10metaObjectEv(
    const QBluetoothLocalDevicePrivate *self) {
  return self->metaObject();
}

//  QBluetoothLocalDevicePrivate::~QBluetoothLocalDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBluetoothLocalDevicePrivateD1Ev(
    QBluetoothLocalDevicePrivate *self) {
  delete self;
}

#endif  // defined(Q_OS_WIN) && QT_CONFIG(cpp_winrt)
