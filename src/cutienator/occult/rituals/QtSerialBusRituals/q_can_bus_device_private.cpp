//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcanbusdevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/qcanbusdevice.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcanbusdevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCanBusDevice *QCanBusDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
QCanBusDevice *ritual_ZN20QCanBusDevicePrivate6q_funcEv(
    QCanBusDevicePrivate *self) {
  return self->q_func();
}

//  const QCanBusDevice *QCanBusDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCanBusDevice *ritual_ZNK20QCanBusDevicePrivate6q_funcEv(
    const QCanBusDevicePrivate *self) {
  return self->q_func();
}

//  QCanBusDevicePrivate::QCanBusDevicePrivate()
extern "C" Q_DECL_EXPORT
QCanBusDevicePrivate *ritual_ZN20QCanBusDevicePrivateC1Ev() {
  return new QCanBusDevicePrivate();
}
