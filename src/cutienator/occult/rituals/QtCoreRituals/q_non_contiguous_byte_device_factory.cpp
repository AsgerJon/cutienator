//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qnoncontiguousbytedevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <memory>
#include <QtCore/QByteArray>

//  QNonContiguousByteDevice
//      *QNonContiguousByteDeviceFactory::create(QIODevice *device)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZN31QNonContiguousByteDeviceFactory6createEP9QIODevice(
    QIODevice *device) {
  return QNonContiguousByteDeviceFactory::create(device);
}

//  std::shared_ptr<QNonContiguousByteDevice>
//      QNonContiguousByteDeviceFactory::createShared(QIODevice *device)
extern "C" Q_DECL_EXPORT
std::shared_ptr<QNonContiguousByteDevice> *ritual_ZN31QNonContiguousByteDeviceFactory12createSharedEP9QIODevice(
    QIODevice *device) {
  return new std::shared_ptr<QNonContiguousByteDevice>(
      QNonContiguousByteDeviceFactory::createShared(
          device));
}

//  QNonContiguousByteDevice *QNonContiguousByteDeviceFactory::create(const
//      QByteArray &byteArray)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZN31QNonContiguousByteDeviceFactory6createERK10QByteArray(
    const QByteArray *byteArray) {
  return QNonContiguousByteDeviceFactory::create(*byteArray);
}

//  std::shared_ptr<QNonContiguousByteDevice>
//      QNonContiguousByteDeviceFactory::createShared(const QByteArray
//      &byteArray)
extern "C" Q_DECL_EXPORT
std::shared_ptr<QNonContiguousByteDevice> *ritual_ZN31QNonContiguousByteDeviceFactory12createSharedERK10QByteArray(
    const QByteArray *byteArray) {
  return new std::shared_ptr<QNonContiguousByteDevice>(
      QNonContiguousByteDeviceFactory::createShared(
          *byteArray));
}

//  QNonContiguousByteDevice
//      *QNonContiguousByteDeviceFactory::create(std::shared_ptr<QRingBuffer>
//      ringBuffer)
extern "C" Q_DECL_EXPORT
QNonContiguousByteDevice *ritual_ZN31QNonContiguousByteDeviceFactory6createESt10shared_ptrI11QRingBufferE(
    const std::shared_ptr<QRingBuffer> *ringBuffer) {
  return QNonContiguousByteDeviceFactory::create(*ringBuffer);
}

//  std::shared_ptr<QNonContiguousByteDevice> QNonContiguousByteDeviceFactory
//      ::createShared(std::shared_ptr<QRingBuffer> ringBuffer)
extern "C" Q_DECL_EXPORT
std::shared_ptr<QNonContiguousByteDevice> *ritual_ZN31QNonContiguousByteDeviceFactory12createSharedESt10shared_ptrI11QRingBufferE(
    const std::shared_ptr<QRingBuffer> *ringBuffer) {
  return new std::shared_ptr<QNonContiguousByteDevice>(
      QNonContiguousByteDeviceFactory::createShared(
          *ringBuffer));
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

//  a std::shared_ptr<QNonContiguousByteDevice> a ritual of
//      QNonContiguousByteDeviceFactory gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNonContiguousByteDeviceFactory__std_shared_ptr_QNonContiguousByteDevice(
    std::shared_ptr<QNonContiguousByteDevice> *self) {
  delete self;
}
