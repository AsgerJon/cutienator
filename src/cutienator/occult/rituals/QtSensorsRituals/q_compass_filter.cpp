//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qcompass.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qcompass.h>

//  bool QCompassFilter::filter(QCompassReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QCompassFilter6filterEP15QCompassReading(
    QCompassFilter *self,
    QCompassReading *reading) {
  return self->filter(reading);
}

//  bool QCompassFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QCompassFilter6filterEP14QSensorReading(
    QCompassFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QCompassFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QCompassFilter6filterEP14QSensorReading(
    QCompassFilter *self,
    QSensorReading *reading) {
  return self->QCompassFilter::filter(reading);
}
