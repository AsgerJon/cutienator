//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpermissions.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(permissions)
#include <QtCore/qpermissions.h>

//  void QLocationPermission::setAccuracy(Accuracy accuracy)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLocationPermission11setAccuracyENS_8AccuracyE(
    QLocationPermission *self,
    QLocationPermission::Accuracy accuracy) {
  self->setAccuracy(accuracy);
}

//  Accuracy QLocationPermission::accuracy() const
extern "C" Q_DECL_EXPORT
QLocationPermission::Accuracy ritual_ZNK19QLocationPermission8accuracyEv(
    const QLocationPermission *self) {
  return self->accuracy();
}

//  void QLocationPermission::setAvailability(Availability availability)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLocationPermission15setAvailabilityENS_12AvailabilityE(
    QLocationPermission *self,
    QLocationPermission::Availability availability) {
  self->setAvailability(availability);
}

//  Availability QLocationPermission::availability() const
extern "C" Q_DECL_EXPORT
QLocationPermission::Availability ritual_ZNK19QLocationPermission12availabilityEv(
    const QLocationPermission *self) {
  return self->availability();
}

//  QLocationPermission::QLocationPermission()
extern "C" Q_DECL_EXPORT
QLocationPermission *ritual_ZN19QLocationPermissionC1Ev() {
  return new QLocationPermission();
}

//  QLocationPermission::QLocationPermission(const QLocationPermission
//      &other)
extern "C" Q_DECL_EXPORT
QLocationPermission *ritual_ZN19QLocationPermissionC1ERKS_(
    const QLocationPermission *other) {
  return new QLocationPermission(*other);
}

//  QLocationPermission::~QLocationPermission()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QLocationPermissionD1Ev(QLocationPermission *self) {
  delete self;
}

#endif  // QT_CONFIG(permissions)
