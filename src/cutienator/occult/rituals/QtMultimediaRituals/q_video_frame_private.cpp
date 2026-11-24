//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframe_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideoframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qvideoframe.h>

//  QVideoFramePrivate::QVideoFramePrivate()
extern "C" Q_DECL_EXPORT
QVideoFramePrivate *ritual_ZN18QVideoFramePrivateC1Ev() {
  return new QVideoFramePrivate();
}

//  QVideoFramePrivate::~QVideoFramePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QVideoFramePrivateD1Ev(QVideoFramePrivate *self) {
  delete self;
}

//  QHwVideoBuffer *QVideoFramePrivate::hwBuffer(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
QHwVideoBuffer *ritual_ZN18QVideoFramePrivate8hwBufferERK11QVideoFrame(
    const QVideoFrame *frame) {
  return QVideoFramePrivate::hwBuffer(*frame);
}

//  bool QVideoFramePrivate::hasDmaBuf(const QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QVideoFramePrivate9hasDmaBufERK11QVideoFrame(
    const QVideoFrame *frame) {
  return QVideoFramePrivate::hasDmaBuf(*frame);
}

//  QAbstractVideoBuffer *QVideoFramePrivate::buffer(const QVideoFrame
//      &frame)
extern "C" Q_DECL_EXPORT
QAbstractVideoBuffer *ritual_ZN18QVideoFramePrivate6bufferERK11QVideoFrame(
    const QVideoFrame *frame) {
  return QVideoFramePrivate::buffer(*frame);
}

//  QVideoFrame QVideoFramePrivate::adoptThisByVideoFrame()
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZN18QVideoFramePrivate21adoptThisByVideoFrameEv(
    QVideoFramePrivate *self) {
  return new QVideoFrame(self->adoptThisByVideoFrame());
}
