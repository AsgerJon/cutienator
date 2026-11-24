//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qgyroscope.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qgyroscope.h>

//  bool QGyroscopeFilter::filter(QGyroscopeReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QGyroscopeFilter6filterEP17QGyroscopeReading(
    QGyroscopeFilter *self,
    QGyroscopeReading *reading) {
  return self->filter(reading);
}

//  bool QGyroscopeFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QGyroscopeFilter6filterEP14QSensorReading(
    QGyroscopeFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QGyroscopeFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QGyroscopeFilter6filterEP14QSensorReading(
    QGyroscopeFilter *self,
    QSensorReading *reading) {
  return self->QGyroscopeFilter::filter(reading);
}
