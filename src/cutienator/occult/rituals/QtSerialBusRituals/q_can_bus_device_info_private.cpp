//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/6.12.0/QtSerialBus/private/qcanbusdeviceinfo_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtSerialBus/QtSerialBus>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSerialBus/6.12.0/QtSerialBus/private/qcanbusdeviceinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QCanBusDeviceInfoPrivate::QCanBusDeviceInfoPrivate()
extern "C" Q_DECL_EXPORT
QCanBusDeviceInfoPrivate *ritual_ZN24QCanBusDeviceInfoPrivateC1Ev() {
  return new QCanBusDeviceInfoPrivate();
}

//  QCanBusDeviceInfoPrivate::~QCanBusDeviceInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QCanBusDeviceInfoPrivateD1Ev(
    QCanBusDeviceInfoPrivate *self) {
  delete self;
}
