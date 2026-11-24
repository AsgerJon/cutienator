//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qlightsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qlightsensor.h>

//  bool QLightFilter::filter(QLightReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLightFilter6filterEP13QLightReading(
    QLightFilter *self,
    QLightReading *reading) {
  return self->filter(reading);
}

//  bool QLightFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QLightFilter6filterEP14QSensorReading(
    QLightFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QLightFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QLightFilter6filterEP14QSensorReading(
    QLightFilter *self,
    QSensorReading *reading) {
  return self->QLightFilter::filter(reading);
}
