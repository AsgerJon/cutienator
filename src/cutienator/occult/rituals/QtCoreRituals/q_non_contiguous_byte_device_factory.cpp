//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  QNonContiguousByteDevice
//      *QNonContiguousByteDeviceFactory::create(QIODevice *device)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZN31QNonContiguousByteDeviceFactory6createEP9QIODevice(
    QIODevice *device) {
  return QNonContiguousByteDeviceFactory::create(device);
}

//  QNonContiguousByteDevice *QNonContiguousByteDeviceFactory::create(const
//      QByteArray &byteArray)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZN31QNonContiguousByteDeviceFactory6createERK10QByteArray(
    const QByteArray *byteArray) {
  return QNonContiguousByteDeviceFactory::create(*byteArray);
}

//  QIODevice *QNonContiguousByteDeviceFactory::wrap(QNonContiguousByteDevice
//      *byteDevice)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN31QNonContiguousByteDeviceFactory4wrapEP24QNonContiguousByteDevice(
    QNonContiguousByteDevice *byteDevice) {
  return QNonContiguousByteDeviceFactory::wrap(byteDevice);
}

//  QNonContiguousByteDeviceFactory::~QNonContiguousByteDeviceFactory()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QNonContiguousByteDeviceFactoryD1Ev(
    QNonContiguousByteDeviceFactory *self) {
  delete self;
}
