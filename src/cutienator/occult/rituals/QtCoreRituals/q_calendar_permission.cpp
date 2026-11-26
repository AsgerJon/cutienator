//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(permissions)
#if QT_CONFIG(permissions)
#include <QtCore/qpermissions.h>

//  void QCalendarPermission::setAccessMode(AccessMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCalendarPermission13setAccessModeENS_10AccessModeE(
    QCalendarPermission *self,
    QCalendarPermission::AccessMode mode) {
  self->setAccessMode(mode);
}

//  AccessMode QCalendarPermission::accessMode() const
extern "C" Q_DECL_EXPORT
QCalendarPermission::AccessMode ritual_ZNK19QCalendarPermission10accessModeEv(
    const QCalendarPermission *self) {
  return self->accessMode();
}

//  QCalendarPermission::QCalendarPermission()
extern "C" Q_DECL_EXPORT
QCalendarPermission *ritual_ZN19QCalendarPermissionC1Ev() {
  return new QCalendarPermission();
}

//  QCalendarPermission::QCalendarPermission(const QCalendarPermission
//      &other)
extern "C" Q_DECL_EXPORT
QCalendarPermission *ritual_ZN19QCalendarPermissionC1ERKS_(
    const QCalendarPermission *other) {
  return new QCalendarPermission(*other);
}

//  QCalendarPermission::QCalendarPermission(QCalendarPermission &&other)
extern "C" Q_DECL_EXPORT
QCalendarPermission *ritual_ZN19QCalendarPermissionC1EOS_(
    QCalendarPermission *other) {
  return new QCalendarPermission(std::move(*other));
}

//  QCalendarPermission::~QCalendarPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCalendarPermissionD1Ev(QCalendarPermission *self) {
  delete self;
}

//  QCalendarPermission &QCalendarPermission::operator=(const
//      QCalendarPermission &other)
extern "C" Q_DECL_EXPORT
QCalendarPermission *ritual_ZN19QCalendarPermissionaSERKS_(
    QCalendarPermission *self,
    const QCalendarPermission *other) {
  return &(self->operator=(*other));
}

//  QCalendarPermission &QCalendarPermission::operator=(QCalendarPermission
//      &&other)
extern "C" Q_DECL_EXPORT
QCalendarPermission *ritual_ZN19QCalendarPermissionaSEOS_(
    QCalendarPermission *self,
    QCalendarPermission *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QCalendarPermission::swap(QCalendarPermission &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCalendarPermission4swapERS_(
    QCalendarPermission *self,
    QCalendarPermission *other) {
  self->swap(*other);
}

#endif  // QT_CONFIG(permissions)
#endif  // QT_CONFIG(permissions)
