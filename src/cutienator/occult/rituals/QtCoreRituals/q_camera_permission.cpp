//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(permissions)
#if QT_CONFIG(permissions)
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

//  QCameraPermission::QCameraPermission(QCameraPermission &&other)
extern "C" Q_DECL_EXPORT
QCameraPermission *ritual_ZN17QCameraPermissionC1EOS_(
    QCameraPermission *other) {
  return new QCameraPermission(std::move(*other));
}

//  QCameraPermission::~QCameraPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCameraPermissionD1Ev(QCameraPermission *self) {
  delete self;
}

//  QCameraPermission &QCameraPermission::operator=(const QCameraPermission
//      &other)
extern "C" Q_DECL_EXPORT
QCameraPermission *ritual_ZN17QCameraPermissionaSERKS_(
    QCameraPermission *self,
    const QCameraPermission *other) {
  return &(self->operator=(*other));
}

//  QCameraPermission &QCameraPermission::operator=(QCameraPermission
//      &&other)
extern "C" Q_DECL_EXPORT
QCameraPermission *ritual_ZN17QCameraPermissionaSEOS_(
    QCameraPermission *self,
    QCameraPermission *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCameraPermission::swap(QCameraPermission &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCameraPermission4swapERS_(
    QCameraPermission *self,
    QCameraPermission *other) {
  self->swap(*other);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
