//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qcameradevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcameradevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qcameradevice.h>

//  const QCameraDevicePrivate *QCameraDevicePrivate::handle(const
//      QCameraDevice &device)
extern "C" Q_DECL_EXPORT
const QCameraDevicePrivate *ritual_ZN20QCameraDevicePrivate6handleERK13QCameraDevice(
    const QCameraDevice *device) {
  return QCameraDevicePrivate::handle(*device);
}

//  bool QCameraDevicePrivate::operator==(const QCameraDevicePrivate &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCameraDevicePrivateeqERKS_(
    const QCameraDevicePrivate *self,
    const QCameraDevicePrivate *other) {
  return self->operator==(*other);
}

//  QCameraDevice QCameraDevicePrivate::create()
extern "C" Q_DECL_EXPORT
QCameraDevice *ritual_ZN20QCameraDevicePrivate6createEv(
    QCameraDevicePrivate *self) {
  return new QCameraDevice(self->create());
}

//  QCameraDevicePrivate::~QCameraDevicePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCameraDevicePrivateD1Ev(QCameraDevicePrivate *self) {
  delete self;
}
