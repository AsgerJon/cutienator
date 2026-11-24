//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qrotationsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qrotationsensor.h>

//  bool QRotationFilter::filter(QRotationReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QRotationFilter6filterEP16QRotationReading(
    QRotationFilter *self,
    QRotationReading *reading) {
  return self->filter(reading);
}

//  bool QRotationFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QRotationFilter6filterEP14QSensorReading(
    QRotationFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QRotationFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QRotationFilter6filterEP14QSensorReading(
    QRotationFilter *self,
    QSensorReading *reading) {
  return self->QRotationFilter::filter(reading);
}
