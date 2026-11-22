//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpermissions.h>

//  QCameraPermission::QCameraPermission()
extern "C" Q_DECL_EXPORT
QCameraPermission *ritual_ZN17QCameraPermissionC1Ev() {
  return new QCameraPermission();
}

//  QCameraPermission::QCameraPermission(const QCameraPermission &other)
extern "C" Q_DECL_EXPORT
QCameraPermission *ritual_ZN17QCameraPermissionC1ERKS_(
    const QCameraPermission *other) {
  return new QCameraPermission(*other);
}

//  QCameraPermission::~QCameraPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCameraPermissionD1Ev(QCameraPermission *self) {
  delete self;
}
