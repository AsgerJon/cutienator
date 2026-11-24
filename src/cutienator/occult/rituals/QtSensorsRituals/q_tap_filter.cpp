//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qtapsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qtapsensor.h>

//  bool QTapFilter::filter(QTapReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTapFilter6filterEP11QTapReading(
    QTapFilter *self,
    QTapReading *reading) {
  return self->filter(reading);
}

//  bool QTapFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QTapFilter6filterEP14QSensorReading(
    QTapFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QTapFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10QTapFilter6filterEP14QSensorReading(
    QTapFilter *self,
    QSensorReading *reading) {
  return self->QTapFilter::filter(reading);
}
