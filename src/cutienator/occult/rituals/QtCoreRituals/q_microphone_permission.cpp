//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
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

//  QMicrophonePermission::~QMicrophonePermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QMicrophonePermissionD1Ev(QMicrophonePermission *self) {
  delete self;
}

#endif  // QT_CONFIG(permissions)
