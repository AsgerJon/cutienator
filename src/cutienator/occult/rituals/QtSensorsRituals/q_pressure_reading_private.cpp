//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qpressuresensor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qpressuresensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QPressureReadingPrivate::QPressureReadingPrivate()
extern "C" Q_DECL_EXPORT
QPressureReadingPrivate *ritual_ZN23QPressureReadingPrivateC1Ev() {
  return new QPressureReadingPrivate();
}

//  QPressureReadingPrivate::~QPressureReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPressureReadingPrivateD1Ev(QPressureReadingPrivate *self) {
  delete self;
}
