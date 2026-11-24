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

//  bool QtMultimediaPrivate::QDmaBufVideoBuffer::isDmaBuf() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QtMultimediaPrivate18QDmaBufVideoBuffer8isDmaBufEv(
    const QtMultimediaPrivate::QDmaBufVideoBuffer *self) {
  return self->isDmaBuf();
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

#endif  // QT_CONFIG(linux_dmabuf)
