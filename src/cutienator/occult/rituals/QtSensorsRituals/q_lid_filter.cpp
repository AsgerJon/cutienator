//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qlidsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qlidsensor.h>

//  bool QLidFilter::filter(QLidReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QLidFilter6filterEP11QLidReading(
    QLidFilter *self,
    QLidReading *reading) {
  return self->filter(reading);
}

//  bool QLidFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QLidFilter6filterEP14QSensorReading(
    QLidFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QLidFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QLidFilter6filterEP14QSensorReading(
    QLidFilter *self,
    QSensorReading *reading) {
  return self->QLidFilter::filter(reading);
}
