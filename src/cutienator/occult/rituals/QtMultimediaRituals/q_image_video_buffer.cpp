//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qimagevideobuffer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qimagevideobuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtMultimedia/qabstractvideobuffer.h>
#include <QtMultimedia/qvideoframeformat.h>

//  QImageVideoBuffer::QImageVideoBuffer(QImage image)
extern "C" Q_DECL_EXPORT
QImageVideoBuffer *ritual_ZN17QImageVideoBufferC1E6QImage(
    const QImage *image) {
  return new QImageVideoBuffer(*image);
}

//  MapData QImageVideoBuffer::map(QVideoFrame::MapMode mode)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer::MapData *ritual_ZN17QImageVideoBuffer3mapEN11QVideoFrame7MapModeE(
    QImageVideoBuffer *self,
    QVideoFrame::MapMode mode) {
  return new QAbstractVideoBuffer::MapData(self->map(mode));
}

//  QVideoFrameFormat QImageVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_ZNK17QImageVideoBuffer6formatEv(
    const QImageVideoBuffer *self) {
  return new QVideoFrameFormat(self->format());
}

//  QImage QImageVideoBuffer::underlyingImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK17QImageVideoBuffer15underlyingImageEv(
    const QImageVideoBuffer *self) {
  return new QImage(self->underlyingImage());
}

//  QImageVideoBuffer::~QImageVideoBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QImageVideoBufferD1Ev(QImageVideoBuffer *self) {
  delete self;
}

//  MapData QImageVideoBuffer::map(QVideoFrame::MapMode mode)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer::MapData *ritual_own_ZN17QImageVideoBuffer3mapEN11QVideoFrame7MapModeE(
    QImageVideoBuffer *self,
    QVideoFrame::MapMode mode) {
  return new QAbstractVideoBuffer::MapData(
      self->QImageVideoBuffer::map(
          mode));
}

//  QVideoFrameFormat QImageVideoBuffer::format() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat *ritual_own_ZNK17QImageVideoBuffer6formatEv(
    const QImageVideoBuffer *self) {
  return new QVideoFrameFormat(self->QImageVideoBuffer::format());
}
