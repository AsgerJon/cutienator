//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qorientationsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qorientationsensor.h>

//  bool QOrientationFilter::filter(QOrientationReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QOrientationFilter6filterEP19QOrientationReading(
    QOrientationFilter *self,
    QOrientationReading *reading) {
  return self->filter(reading);
}

//  bool QOrientationFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QOrientationFilter6filterEP14QSensorReading(
    QOrientationFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QOrientationFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QOrientationFilter6filterEP14QSensorReading(
    QOrientationFilter *self,
    QSensorReading *reading) {
  return self->QOrientationFilter::filter(reading);
}
