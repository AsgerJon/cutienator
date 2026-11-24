//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qhumiditysensor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qhumiditysensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QHumidityReadingPrivate::QHumidityReadingPrivate()
extern "C" Q_DECL_EXPORT
QHumidityReadingPrivate *ritual_ZN23QHumidityReadingPrivateC1Ev() {
  return new QHumidityReadingPrivate();
}

//  QHumidityReadingPrivate::~QHumidityReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QHumidityReadingPrivateD1Ev(QHumidityReadingPrivate *self) {
  delete self;
}
