//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(permissions)
#include <QtCore/qpermissions.h>

//  void QBluetoothPermission::setCommunicationModes(CommunicationModes
//      modes)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothPermission21setCommunicationModesE6QFlagsINS_17CommunicationModeEE(
    QBluetoothPermission *self,
    int modes) {
  self->setCommunicationModes(
      QFlags<QBluetoothPermission::CommunicationMode>::fromInt(modes));
}

//  CommunicationModes QBluetoothPermission::communicationModes() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QBluetoothPermission18communicationModesEv(
    const QBluetoothPermission *self) {
  return static_cast<int>(self->communicationModes().toInt());
}

//  QBluetoothPermission::QBluetoothPermission()
extern "C" Q_DECL_EXPORT
QBluetoothPermission *ritual_ZN20QBluetoothPermissionC1Ev() {
  return new QBluetoothPermission();
}

//  QBluetoothPermission::QBluetoothPermission(const QBluetoothPermission
//      &other)
extern "C" Q_DECL_EXPORT
QBluetoothPermission *ritual_ZN20QBluetoothPermissionC1ERKS_(
    const QBluetoothPermission *other) {
  return new QBluetoothPermission(*other);
}

//  QBluetoothPermission::~QBluetoothPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QBluetoothPermissionD1Ev(QBluetoothPermission *self) {
  delete self;
}

#endif  // QT_CONFIG(permissions)
