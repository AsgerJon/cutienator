//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothserviceinfo.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QBluetoothServiceInfo::Alternative::Alternative()
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Alternative *ritual_ZN21QBluetoothServiceInfo11AlternativeC1Ev() {
  return new QBluetoothServiceInfo::Alternative();
}

//  QBluetoothServiceInfo::Alternative::Alternative(const QList<QVariant>
//      &list)
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Alternative *ritual_ZN21QBluetoothServiceInfo11AlternativeC1ERK5QListI8QVariantE(
    const QList<QVariant> *list) {
  return new QBluetoothServiceInfo::Alternative(*list);
}

//  QBluetoothServiceInfo::Alternative::~Alternative()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo11AlternativeD1Ev(
    QBluetoothServiceInfo::Alternative *self) {
  delete self;
}
