//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qproximitysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qproximitysensor.h>

//  bool QProximityFilter::filter(QProximityReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProximityFilter6filterEP17QProximityReading(
    QProximityFilter *self,
    QProximityReading *reading) {
  return self->filter(reading);
}

//  bool QProximityFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QProximityFilter6filterEP14QSensorReading(
    QProximityFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QProximityFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QProximityFilter6filterEP14QSensorReading(
    QProximityFilter *self,
    QSensorReading *reading) {
  return self->QProximityFilter::filter(reading);
}
