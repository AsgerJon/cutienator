//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qtapsensor_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qtapsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QTapReadingPrivate::QTapReadingPrivate()
extern "C" Q_DECL_EXPORT
QTapReadingPrivate *ritual_ZN18QTapReadingPrivateC1Ev() {
  return new QTapReadingPrivate();
}

//  QTapReadingPrivate::~QTapReadingPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTapReadingPrivateD1Ev(QTapReadingPrivate *self) {
  delete self;
}
