//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qsensor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSensorReadingPrivate::QSensorReadingPrivate()
extern "C" Q_DECL_EXPORT
QSensorReadingPrivate *ritual_ZN21QSensorReadingPrivateC1Ev() {
  return new QSensorReadingPrivate();
}

//  QSensorReadingPrivate::~QSensorReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSensorReadingPrivateD1Ev(QSensorReadingPrivate *self) {
  delete self;
}
