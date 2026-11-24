//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qaccelerometer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qaccelerometer.h>

//  bool QAccelerometerFilter::filter(QAccelerometerReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAccelerometerFilter6filterEP21QAccelerometerReading(
    QAccelerometerFilter *self,
    QAccelerometerReading *reading) {
  return self->filter(reading);
}

//  bool QAccelerometerFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QAccelerometerFilter6filterEP14QSensorReading(
    QAccelerometerFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QAccelerometerFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QAccelerometerFilter6filterEP14QSensorReading(
    QAccelerometerFilter *self,
    QSensorReading *reading) {
  return self->QAccelerometerFilter::filter(reading);
}
