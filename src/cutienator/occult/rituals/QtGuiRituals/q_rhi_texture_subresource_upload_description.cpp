//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>

//  QRhiTextureSubresourceUploadDescription::QRhiTextureSubresourceUploadDesc
//      ription()
extern "C" Q_DECL_EXPORT
QRhiTextureSubresourceUploadDescription *ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1Ev() {
  return new QRhiTextureSubresourceUploadDescription();
}

//  QRhiTextureSubresourceUploadDescription::QRhiTextureSubresourceUploadDesc
//      ription(const QImage &image)
extern "C" Q_DECL_EXPORT
QRhiTextureSubresourceUploadDescription *ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1ERK6QImage(
    const QImage *image) {
  return new QRhiTextureSubresourceUploadDescription(*image);
}

//  QRhiTextureSubresourceUploadDescription::QRhiTextureSubresourceUploadDesc
//      ription(const void *data, quint32 size)
extern "C" Q_DECL_EXPORT
QRhiTextureSubresourceUploadDescription *ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1EPKvj(
    const void *data,
    quint32 size) {
  return new QRhiTextureSubresourceUploadDescription(data, size);
}

//  QRhiTextureSubresourceUploadDescription::QRhiTextureSubresourceUploadDesc
//      ription(const QByteArray &data)
extern "C" Q_DECL_EXPORT
QRhiTextureSubresourceUploadDescription *ritual_ZN39QRhiTextureSubresourceUploadDescriptionC1ERK10QByteArray(
    const QByteArray *data) {
  return new QRhiTextureSubresourceUploadDescription(*data);
}

//  QImage QRhiTextureSubresourceUploadDescription::image() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK39QRhiTextureSubresourceUploadDescription5imageEv(
    const QRhiTextureSubresourceUploadDescription *self) {
  return new QImage(self->image());
}

//  void QRhiTextureSubresourceUploadDescription::setImage(const QImage
//      &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescription8setImageERK6QImage(
    QRhiTextureSubresourceUploadDescription *self,
    const QImage *image) {
  self->setImage(*image);
}

//  QByteArray QRhiTextureSubresourceUploadDescription::data() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK39QRhiTextureSubresourceUploadDescription4dataEv(
    const QRhiTextureSubresourceUploadDescription *self) {
  return new QByteArray(self->data());
}

//  void QRhiTextureSubresourceUploadDescription::setData(const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescription7setDataERK10QByteArray(
    QRhiTextureSubresourceUploadDescription *self,
    const QByteArray *data) {
  self->setData(*data);
}

//  quint32 QRhiTextureSubresourceUploadDescription::dataStride() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK39QRhiTextureSubresourceUploadDescription10dataStrideEv(
    const QRhiTextureSubresourceUploadDescription *self) {
  return self->dataStride();
}

//  void QRhiTextureSubresourceUploadDescription::setDataStride(quint32
//      stride)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescription13setDataStrideEj(
    QRhiTextureSubresourceUploadDescription *self,
    quint32 stride) {
  self->setDataStride(stride);
}

//  QPoint QRhiTextureSubresourceUploadDescription::destinationTopLeft()
//      const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK39QRhiTextureSubresourceUploadDescription18destinationTopLeftEv(
    const QRhiTextureSubresourceUploadDescription *self) {
  return new QPoint(self->destinationTopLeft());
}

//  void QRhiTextureSubresourceUploadDescription::setDestinationTopLeft(const
//      QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescription21setDestinationTopLeftERK6QPoint(
    QRhiTextureSubresourceUploadDescription *self,
    const QPoint *p) {
  self->setDestinationTopLeft(*p);
}

//  QSize QRhiTextureSubresourceUploadDescription::sourceSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK39QRhiTextureSubresourceUploadDescription10sourceSizeEv(
    const QRhiTextureSubresourceUploadDescription *self) {
  return new QSize(self->sourceSize());
}

//  void QRhiTextureSubresourceUploadDescription::setSourceSize(const QSize
//      &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescription13setSourceSizeERK5QSize(
    QRhiTextureSubresourceUploadDescription *self,
    const QSize *size) {
  self->setSourceSize(*size);
}

//  QPoint QRhiTextureSubresourceUploadDescription::sourceTopLeft() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK39QRhiTextureSubresourceUploadDescription13sourceTopLeftEv(
    const QRhiTextureSubresourceUploadDescription *self) {
  return new QPoint(self->sourceTopLeft());
}

//  void QRhiTextureSubresourceUploadDescription::setSourceTopLeft(const
//      QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescription16setSourceTopLeftERK6QPoint(
    QRhiTextureSubresourceUploadDescription *self,
    const QPoint *p) {
  self->setSourceTopLeft(*p);
}

//  QRhiTextureSubresourceUploadDescription::~QRhiTextureSubresourceUploadDes
//      cription()
extern "C" Q_DECL_EXPORT
void ritual_ZN39QRhiTextureSubresourceUploadDescriptionD1Ev(
    QRhiTextureSubresourceUploadDescription *self) {
  delete self;
}
