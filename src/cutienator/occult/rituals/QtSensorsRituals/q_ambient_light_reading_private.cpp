//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qambientlightsensor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qambientlightsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QAmbientLightReadingPrivate::QAmbientLightReadingPrivate()
extern "C" Q_DECL_EXPORT
QAmbientLightReadingPrivate *ritual_ZN27QAmbientLightReadingPrivateC1Ev() {
  return new QAmbientLightReadingPrivate();
}

//  QAmbientLightReadingPrivate::~QAmbientLightReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAmbientLightReadingPrivateD1Ev(
    QAmbientLightReadingPrivate *self) {
  delete self;
}
