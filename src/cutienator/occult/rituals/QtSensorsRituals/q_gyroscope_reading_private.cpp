//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qgyroscope_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qgyroscope_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QGyroscopeReadingPrivate::QGyroscopeReadingPrivate()
extern "C" Q_DECL_EXPORT
QGyroscopeReadingPrivate *ritual_ZN24QGyroscopeReadingPrivateC1Ev() {
  return new QGyroscopeReadingPrivate();
}

//  QGyroscopeReadingPrivate::~QGyroscopeReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGyroscopeReadingPrivateD1Ev(
    QGyroscopeReadingPrivate *self) {
  delete self;
}
