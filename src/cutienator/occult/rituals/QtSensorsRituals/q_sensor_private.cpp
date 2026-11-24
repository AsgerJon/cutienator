//  Written by dev_tooling.RitualGenerator from the records of
//  QtSensors/6.12.0/QtSensors/private/qsensor_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSensors/qsensor.h>
#include <QtSensors/QtSensors>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/6.12.0/QtSensors/private/qsensor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSensors/qsensor.h>
#include <QtSensors/private/qsensor_p.h>
#include <QtSensors/qsensorbackend.h>
#include <QtSensors/qsensormanager.h>
#include <QtCore/QDebug>
#include <QtCore/QMetaProperty>
#include <QtCore/QTimer>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtsensors/src/sensors/qsensor.cpp, line 122, as _ZN14QSensorPrivate4initERK10QByteArray
inline void QSensorPrivate::init(const QByteArray &sensorType)
{
    Q_Q(QSensor);
    type = sensorType;
    q->registerInstance(); // so the availableSensorsChanged() signal works
}
//  -----------------------------------------------------------------------

//  QSensor *QSensorPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSensor *ritual_ZN14QSensorPrivate6q_funcEv(QSensorPrivate *self) {
  return self->q_func();
}

//  const QSensor *QSensorPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSensor *ritual_ZNK14QSensorPrivate6q_funcEv(
    const QSensorPrivate *self) {
  return self->q_func();
}

//  QSensorPrivate::QSensorPrivate()
extern "C" Q_DECL_EXPORT
QSensorPrivate *ritual_ZN14QSensorPrivateC1Ev() {
  return new QSensorPrivate();
}

//  void QSensorPrivate::init(const QByteArray &sensorType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSensorPrivate4initERK10QByteArray(
    QSensorPrivate *self,
    const QByteArray *sensorType) {
  self->init(*sensorType);
}
