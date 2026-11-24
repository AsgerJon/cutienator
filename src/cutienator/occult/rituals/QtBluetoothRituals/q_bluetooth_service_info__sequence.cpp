//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/qbluetoothserviceinfo.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtBluetooth/qbluetoothserviceinfo.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

//  QBluetoothServiceInfo::Sequence::Sequence()
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Sequence *ritual_ZN21QBluetoothServiceInfo8SequenceC1Ev() {
  return new QBluetoothServiceInfo::Sequence();
}

//  QBluetoothServiceInfo::Sequence::Sequence(const QList<QVariant> &list)
extern "C" Q_DECL_EXPORT
QBluetoothServiceInfo::Sequence *ritual_ZN21QBluetoothServiceInfo8SequenceC1ERK5QListI8QVariantE(
    const QList<QVariant> *list) {
  return new QBluetoothServiceInfo::Sequence(*list);
}

//  QBluetoothServiceInfo::Sequence::~Sequence()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QBluetoothServiceInfo8SequenceD1Ev(
    QBluetoothServiceInfo::Sequence *self) {
  delete self;
}
