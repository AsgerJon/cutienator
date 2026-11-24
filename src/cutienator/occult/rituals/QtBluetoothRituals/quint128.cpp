//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothuuid.h, Qt 6.12.0. Changes made here are lost.
#include <QtBluetooth/qtbluetoothglobal.h>
#if !defined(QT_SUPPORTS_INT128)
#include <QtBluetooth/qbluetoothuuid.h>

//  quint128::~quint128()
extern "C" Q_DECL_EXPORT
void ritual_ZN8quint128D1Ev(quint128 *self) {
  delete self;
}

#endif  // !defined(QT_SUPPORTS_INT128)
