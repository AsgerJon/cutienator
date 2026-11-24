//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qpressuresensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qpressuresensor.h>

//  bool QPressureFilter::filter(QPressureReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPressureFilter6filterEP16QPressureReading(
    QPressureFilter *self,
    QPressureReading *reading) {
  return self->filter(reading);
}

//  bool QPressureFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QPressureFilter6filterEP14QSensorReading(
    QPressureFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QPressureFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN15QPressureFilter6filterEP14QSensorReading(
    QPressureFilter *self,
    QSensorReading *reading) {
  return self->QPressureFilter::filter(reading);
}
