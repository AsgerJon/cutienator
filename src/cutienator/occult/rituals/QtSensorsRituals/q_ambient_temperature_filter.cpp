//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qambienttemperaturesensor.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtSensors/qambienttemperaturesensor.h>

//  bool QAmbientTemperatureFilter::filter(QAmbientTemperatureReading
//      *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAmbientTemperatureFilter6filterEP26QAmbientTemperatureReading(
    QAmbientTemperatureFilter *self,
    QAmbientTemperatureReading *reading) {
  return self->filter(reading);
}

//  bool QAmbientTemperatureFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QAmbientTemperatureFilter6filterEP14QSensorReading(
    QAmbientTemperatureFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QAmbientTemperatureFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QAmbientTemperatureFilter6filterEP14QSensorReading(
    QAmbientTemperatureFilter *self,
    QSensorReading *reading) {
  return self->QAmbientTemperatureFilter::filter(reading);
}
