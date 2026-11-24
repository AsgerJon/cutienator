//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qcompass_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qcompass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCompassReadingPrivate::QCompassReadingPrivate()
extern "C" Q_DECL_EXPORT
QCompassReadingPrivate *ritual_ZN22QCompassReadingPrivateC1Ev() {
  return new QCompassReadingPrivate();
}

//  QCompassReadingPrivate::~QCompassReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCompassReadingPrivateD1Ev(QCompassReadingPrivate *self) {
  delete self;
}
