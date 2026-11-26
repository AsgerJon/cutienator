//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qdmabufvideobuffer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/qtmultimediaglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#if QT_CONFIG(linux_dmabuf)
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qdmabufvideobuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtMultimedia/qabstractvideobuffer.h>
#include <QtCore/QSize>
#include <QtCore/QSpan>
#include <memory>

//  QtMultimediaPrivate::QDmaBufVideoBuffer::QDmaBufVideoBuffer(QVideoFrameFo
//      rmat::PixelFormat format, QSize size, QSpan<const DmaBufPlane>
//      planes, std::shared_ptr<void> keepAlive)
extern "C" Q_DECL_EXPORT
QtMultimediaPrivate::QDmaBufVideoBuffer *ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBufferC1EN17QVideoFrameFormat11PixelFormatE5QSize5QSpanIKNS_11DmaBufPlaneELm18446744073709551615EESt10shared_ptrIvE(
    QVideoFrameFormat::PixelFormat format,
    const QSize *size,
    const QSpan<const QtMultimediaPrivate::DmaBufPlane> *planes,
    const std::shared_ptr<void> *keepAlive) {
  return new QtMultimediaPrivate::QDmaBufVideoBuffer(
      format,
      *size,
      *planes,
      *keepAlive);
}

//  QtMultimediaPrivate::QDmaBufVideoBuffer::~QDmaBufVideoBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBufferD1Ev(
    QtMultimediaPrivate::QDmaBufVideoBuffer *self) {
  delete self;
}

//  bool QtMultimediaPrivate::QDmaBufVideoBuffer::isDmaBuf() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer8isDmaBufEv(
    const QtMultimediaPrivate::QDmaBufVideoBuffer *self) {
  return self->isDmaBuf();
}

//  QVideoFrameTexturesUPtr
//      QtMultimediaPrivate::QDmaBufVideoBuffer::mapTextures(QRhi &rhi,
//      QVideoFrameTexturesUPtr &oldTextures)
extern "C" Q_DECL_EXPORT
QVideoFrameTexturesUPtr *ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBuffer11mapTexturesER4QRhiRSt10unique_ptrI19QVideoFrameTexturesSt14default_deleteIS4_EE(
    QtMultimediaPrivate::QDmaBufVideoBuffer *self,
    QRhi *rhi,
    QVideoFrameTexturesUPtr *oldTextures) {
  return new QVideoFrameTexturesUPtr(self->mapTextures(*rhi, *oldTextures));
}

//  MapData QtMultimediaPrivate::QDmaBufVideoBuffer::map(QVideoFrame::MapMode
//      mode)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer::MapData *ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBuffer3mapEN11QVideoFrame7MapModeE(
    QtMultimediaPrivate::QDmaBufVideoBuffer *self,
    QVideoFrame::MapMode mode) {
  return new QAbstractVideoBuffer::MapData(self->map(mode));
}

//  void QtMultimediaPrivate::QDmaBufVideoBuffer::unmap()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QtMultimediaPrivate18QDmaBufVideoBuffer5unmapEv(
    QtMultimediaPrivate::QDmaBufVideoBuffer *self) {
  self->unmap();
}

//  QVideoFrameFormat::PixelFormat
//      QtMultimediaPrivate::QDmaBufVideoBuffer::pixelFormat() const
extern "C" Q_DECL_EXPORT
QVideoFrameFormat::PixelFormat ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer11pixelFormatEv(
    const QtMultimediaPrivate::QDmaBufVideoBuffer *self) {
  return self->pixelFormat();
}

//  QSize QtMultimediaPrivate::QDmaBufVideoBuffer::size() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer4sizeEv(
    const QtMultimediaPrivate::QDmaBufVideoBuffer *self) {
  return new QSize(self->size());
}

//  a QVideoFrameTexturesUPtr a ritual of
//      QtMultimediaPrivate::QDmaBufVideoBuffer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QtMultimediaPrivate_QDmaBufVideoBuffer__QVideoFrameTexturesUPtr(
    QVideoFrameTexturesUPtr *self) {
  delete self;
}

#endif  // QT_CONFIG(linux_dmabuf)
