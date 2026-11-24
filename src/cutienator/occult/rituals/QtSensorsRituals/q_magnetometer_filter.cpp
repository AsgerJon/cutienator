//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qmagnetometer.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qmagnetometer.h>

//  bool QMagnetometerFilter::filter(QMagnetometerReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMagnetometerFilter6filterEP20QMagnetometerReading(
    QMagnetometerFilter *self,
    QMagnetometerReading *reading) {
  return self->filter(reading);
}

//  bool QMagnetometerFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QMagnetometerFilter6filterEP14QSensorReading(
    QMagnetometerFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QMagnetometerFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QMagnetometerFilter6filterEP14QSensorReading(
    QMagnetometerFilter *self,
    QSensorReading *reading) {
  return self->QMagnetometerFilter::filter(reading);
}
