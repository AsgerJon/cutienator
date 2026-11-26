//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(permissions)
#if QT_CONFIG(permissions)
#include <QtCore/qpermissions.h>

//  QMicrophonePermission::QMicrophonePermission()
extern "C" Q_DECL_EXPORT
QMicrophonePermission *ritual_ZN21QMicrophonePermissionC1Ev() {
  return new QMicrophonePermission();
}

//  QMicrophonePermission::QMicrophonePermission(const QMicrophonePermission
//      &other)
extern "C" Q_DECL_EXPORT
QMicrophonePermission *ritual_ZN21QMicrophonePermissionC1ERKS_(
    const QMicrophonePermission *other) {
  return new QMicrophonePermission(*other);
}

//  QMicrophonePermission::QMicrophonePermission(QMicrophonePermission
//      &&other)
extern "C" Q_DECL_EXPORT
QMicrophonePermission *ritual_ZN21QMicrophonePermissionC1EOS_(
    QMicrophonePermission *other) {
  return new QMicrophonePermission(std::move(*other));
}

//  QMicrophonePermission::~QMicrophonePermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMicrophonePermissionD1Ev(QMicrophonePermission *self) {
  delete self;
}

//  QMicrophonePermission &QMicrophonePermission::operator=(const
//      QMicrophonePermission &other)
extern "C" Q_DECL_EXPORT
QMicrophonePermission *ritual_ZN21QMicrophonePermissionaSERKS_(
    QMicrophonePermission *self,
    const QMicrophonePermission *other) {
  return &(self->operator=(*other));
}

//  QMicrophonePermission
//      &QMicrophonePermission::operator=(QMicrophonePermission &&other)
extern "C" Q_DECL_EXPORT
QMicrophonePermission *ritual_ZN21QMicrophonePermissionaSEOS_(
    QMicrophonePermission *self,
    QMicrophonePermission *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QMicrophonePermission::swap(QMicrophonePermission &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMicrophonePermission4swapERS_(
    QMicrophonePermission *self,
    QMicrophonePermission *other) {
  self->swap(*other);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
