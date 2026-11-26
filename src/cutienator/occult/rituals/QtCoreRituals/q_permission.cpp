//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(permissions)
#if QT_CONFIG(permissions)
#include <QtCore/qpermissions.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qdebug.h>

//  QPermission::QPermission()
extern "C" Q_DECL_EXPORT
QPermission *ritual_ZN11QPermissionC1Ev() {
  return new QPermission();
}

//  Qt::PermissionStatus QPermission::status() const
extern "C" Q_DECL_EXPORT
Qt::PermissionStatus ritual_ZNK11QPermission6statusEv(
    const QPermission *self) {
  return self->status();
}

//  QMetaType QPermission::type() const
extern "C" Q_DECL_EXPORT
QMetaType *ritual_ZNK11QPermission4typeEv(const QPermission *self) {
  return new QMetaType(self->type());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, const QPermission &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK11QPermission(
    const QDebug *debug,
    const QPermission *a1) {
  return new QDebug(operator<<(*debug, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  const void *QPermission::data(QMetaType id) const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK11QPermission4dataE9QMetaType(
    const QPermission *self,
    const QMetaType *id) {
  return self->data(*id);
}

//  QPermission::~QPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPermissionD1Ev(QPermission *self) {
  delete self;
}

//  QPermission::QPermission<QCameraPermission>(const QCameraPermission &t)
extern "C" Q_DECL_EXPORT
QPermission * ritual_ZN11QPermissionC1I17QCameraPermissionLb1EERKT_(
    const QCameraPermission *t) {
  return new QPermission(*t);
}

//  QPermission::QPermission<QMicrophonePermission>(const
//      QMicrophonePermission &t)
extern "C" Q_DECL_EXPORT
QPermission * ritual_ZN11QPermissionC1I21QMicrophonePermissionLb1EERKT_(
    const QMicrophonePermission *t) {
  return new QPermission(*t);
}

//  QPermission::QPermission<QLocationPermission>(const QLocationPermission
//      &t)
extern "C" Q_DECL_EXPORT
QPermission * ritual_ZN11QPermissionC1I19QLocationPermissionLb1EERKT_(
    const QLocationPermission *t) {
  return new QPermission(*t);
}

//  QPermission::QPermission<QBluetoothPermission>(const QBluetoothPermission
//      &t)
extern "C" Q_DECL_EXPORT
QPermission * ritual_ZN11QPermissionC1I20QBluetoothPermissionLb1EERKT_(
    const QBluetoothPermission *t) {
  return new QPermission(*t);
}

//  QPermission::QPermission<QContactsPermission>(const QContactsPermission
//      &t)
extern "C" Q_DECL_EXPORT
QPermission * ritual_ZN11QPermissionC1I19QContactsPermissionLb1EERKT_(
    const QContactsPermission *t) {
  return new QPermission(*t);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
