//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qtiltsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qtiltsensor.h>

//  bool QTiltFilter::filter(QTiltReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTiltFilter6filterEP12QTiltReading(
    QTiltFilter *self,
    QTiltReading *reading) {
  return self->filter(reading);
}

//  bool QTiltFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTiltFilter6filterEP14QSensorReading(
    QTiltFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QTiltFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN11QTiltFilter6filterEP14QSensorReading(
    QTiltFilter *self,
    QSensorReading *reading) {
  return self->QTiltFilter::filter(reading);
}
