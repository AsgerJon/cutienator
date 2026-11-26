//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframe_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 4. Kept as it is when the generator runs again.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideoframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qvideoframe.h>
#include <memory>

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

//  QVideoFramePrivate *QVideoFramePrivate::handle(QVideoFrame &frame)
extern "C" Q_DECL_EXPORT
QVideoFramePrivate *ritual_ZN18QVideoFramePrivate6handleER11QVideoFrame(
    QVideoFrame *frame) {
  return QVideoFramePrivate::handle(*frame);
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

//  template <typename Buffer = QAbstractVideoBuffer>
//  QVideoFramePrivate::QVideoFramePrivate<QAbstractVideoBuffer>(
//      QVideoFrameFormat format,
//      std::unique_ptr<QAbstractVideoBuffer> buffer)
extern "C" Q_DECL_EXPORT
QVideoFramePrivate * ritual_ZN18QVideoFramePrivateC2I20QAbstractVideoBufferEE17QVideoFrameFormatSt10unique_ptrIT_St14default_deleteIS4_EE(const QVideoFrameFormat *format,
    QAbstractVideoBuffer *buffer) {
  return new QVideoFramePrivate(
      *format, std::unique_ptr<QAbstractVideoBuffer>(buffer));
}

//  template <typename Buffer = QAbstractVideoBuffer>
//  QVideoFramePrivate::QVideoFramePrivate<QHwVideoBuffer>(
//      QVideoFrameFormat format,
//      std::unique_ptr<QHwVideoBuffer> buffer)
extern "C" Q_DECL_EXPORT
QVideoFramePrivate * ritual_ZN18QVideoFramePrivateC2I14QHwVideoBufferEE17QVideoFrameFormatSt10unique_ptrIT_St14default_deleteIS4_EE(const QVideoFrameFormat *format,
    QHwVideoBuffer *buffer) {
  return new QVideoFramePrivate(
      *format, std::unique_ptr<QHwVideoBuffer>(buffer));
}

//  template <typename Buffer>
//  static QVideoFrame QVideoFramePrivate::createFrame<QAbstractVideoBuffer>(
//      std::unique_ptr<QAbstractVideoBuffer> buffer,
//      QVideoFrameFormat format)
extern "C" Q_DECL_EXPORT
QVideoFrame * ritual_ZN18QVideoFramePrivate11createFrameI20QAbstractVideoBufferEE11QVideoFrameSt10unique_ptrIT_St14default_deleteIS4_EE17QVideoFrameFormat(QAbstractVideoBuffer *buffer,
    const QVideoFrameFormat *format) {
  return new QVideoFrame(
      QVideoFramePrivate::createFrame<QAbstractVideoBuffer>(
      std::unique_ptr<QAbstractVideoBuffer>(buffer), *format));
}

//  template <typename Buffer>
//  static QVideoFrame QVideoFramePrivate::createFrame<QHwVideoBuffer>(
//      std::unique_ptr<QHwVideoBuffer> buffer, QVideoFrameFormat format)
extern "C" Q_DECL_EXPORT
QVideoFrame * ritual_ZN18QVideoFramePrivate11createFrameI14QHwVideoBufferEE11QVideoFrameSt10unique_ptrIT_St14default_deleteIS4_EE17QVideoFrameFormat(QHwVideoBuffer *buffer,
    const QVideoFrameFormat *format) {
  return new QVideoFrame(QVideoFramePrivate::createFrame<QHwVideoBuffer>(
      std::unique_ptr<QHwVideoBuffer>(buffer), *format));
}
