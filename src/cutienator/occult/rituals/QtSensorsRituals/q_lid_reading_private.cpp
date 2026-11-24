//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qlidsensor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qlidsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLidReadingPrivate::QLidReadingPrivate()
extern "C" Q_DECL_EXPORT
QLidReadingPrivate *ritual_ZN18QLidReadingPrivateC1Ev() {
  return new QLidReadingPrivate();
}

//  QLidReadingPrivate::~QLidReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QLidReadingPrivateD1Ev(QLidReadingPrivate *self) {
  delete self;
}
