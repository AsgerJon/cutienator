//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/qambientlightsensor.h, Qt 6.12.0. Changes made here are lost.
#include <QtSensors/qambientlightsensor.h>

//  bool QAmbientLightFilter::filter(QAmbientLightReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAmbientLightFilter6filterEP20QAmbientLightReading(
    QAmbientLightFilter *self,
    QAmbientLightReading *reading) {
  return self->filter(reading);
}

//  bool QAmbientLightFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAmbientLightFilter6filterEP14QSensorReading(
    QAmbientLightFilter *self,
    QSensorReading *reading) {
  return self->filter(reading);
}

//  bool QAmbientLightFilter::filter(QSensorReading *reading)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QAmbientLightFilter6filterEP14QSensorReading(
    QAmbientLightFilter *self,
    QSensorReading *reading) {
  return self->QAmbientLightFilter::filter(reading);
}
