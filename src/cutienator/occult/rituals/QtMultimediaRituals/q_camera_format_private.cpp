//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qcameradevice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qcameradevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qcameradevice.h>

//  QVideoFrameFormat::ColorRange QCameraFormatPrivate::getColorRange(const
//      QCameraFormat &format)
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::ColorRange ritual_ZN20QCameraFormatPrivate13getColorRangeERK13QCameraFormat(
    const QCameraFormat *format) {
  return QCameraFormatPrivate::getColorRange(*format);
}

//  QVideoFrameFormat::ColorSpace QCameraFormatPrivate::getColorSpace(const
//      QCameraFormat &format)
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::ColorSpace ritual_ZN20QCameraFormatPrivate13getColorSpaceERK13QCameraFormat(
    const QCameraFormat *format) {
  return QCameraFormatPrivate::getColorSpace(*format);
}

//  const QCameraFormatPrivate *QCameraFormatPrivate::handle(const
//      QCameraFormat &format)
extern "C" Q_DECL_EXPORT
const QCameraFormatPrivate *ritual_ZN20QCameraFormatPrivate6handleERK13QCameraFormat(
    const QCameraFormat *format) {
  return QCameraFormatPrivate::handle(*format);
}

//  QCameraFormat QCameraFormatPrivate::create()
extern "C" Q_DECL_EXPORT
QCameraFormat *ritual_ZN20QCameraFormatPrivate6createEv(
    QCameraFormatPrivate *self) {
  return new QCameraFormat(self->create());
}

//  QCameraFormatPrivate::~QCameraFormatPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCameraFormatPrivateD1Ev(QCameraFormatPrivate *self) {
  delete self;
}
