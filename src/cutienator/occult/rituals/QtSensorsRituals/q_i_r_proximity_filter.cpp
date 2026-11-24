//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qirproximitysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qirproximitysensor.h>

//  bool QIRProximityFilter::filter(QIRProximityReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QIRProximityFilter6filterEP19QIRProximityReading(
    QIRProximityFilter *self,
    QIRProximityReading *reading) {
  return self->filter(reading);
}

//  bool QIRProximityFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QIRProximityFilter6filterEP14QSensorReading(
    QIRProximityFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QIRProximityFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN18QIRProximityFilter6filterEP14QSensorReading(
    QIRProximityFilter *self,
    QSensorReading *reading) {
  return self->QIRProximityFilter::filter(reading);
}
