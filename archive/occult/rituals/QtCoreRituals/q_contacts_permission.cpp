//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpermissions.h>

//  void QContactsPermission::setAccessMode(AccessMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QContactsPermission13setAccessModeENS_10AccessModeE(
    QContactsPermission *self,
    QContactsPermission::AccessMode mode) {
  self->setAccessMode(mode);
}

//  AccessMode QContactsPermission::accessMode() const
extern "C" Q_DECL_EXPORT
QContactsPermission::AccessMode ritual_ZNK19QContactsPermission10accessModeEv(
    const QContactsPermission *self) {
  return self->accessMode();
}

//  QContactsPermission::QContactsPermission()
extern "C" Q_DECL_EXPORT
QContactsPermission *ritual_ZN19QContactsPermissionC1Ev() {
  return new QContactsPermission();
}

//  QContactsPermission::QContactsPermission(const QContactsPermission
//      &other)
extern "C" Q_DECL_EXPORT
QContactsPermission *ritual_ZN19QContactsPermissionC1ERKS_(
    const QContactsPermission *other) {
  return new QContactsPermission(*other);
}

//  QContactsPermission::~QContactsPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QContactsPermissionD1Ev(QContactsPermission *self) {
  delete self;
}
