//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qhumiditysensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qhumiditysensor.h>

//  bool QHumidityFilter::filter(QHumidityReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHumidityFilter6filterEP16QHumidityReading(
    QHumidityFilter *self,
    QHumidityReading *reading) {
  return self->filter(reading);
}

//  bool QHumidityFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHumidityFilter6filterEP14QSensorReading(
    QHumidityFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QHumidityFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QHumidityFilter6filterEP14QSensorReading(
    QHumidityFilter *self,
    QSensorReading *reading) {
  return self->QHumidityFilter::filter(reading);
}
