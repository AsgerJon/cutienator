//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
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

//  QDebug operator<<(QDebug debug, const QPermission &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK11QPermission(
    const QDebug *debug,
    const QPermission *a1) {
  return new QDebug(operator<<(*debug, *a1));
}

//  QPermission::~QPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPermissionD1Ev(QPermission *self) {
  delete self;
}
