//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturepool_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qvideoframetexturepool_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/qvideoframe.h>

//  bool QVideoFrameTexturePool::texturesDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QVideoFrameTexturePool13texturesDirtyEv(
    const QVideoFrameTexturePool *self) {
  return self->texturesDirty();
}

//  const QVideoFrame &QVideoFrameTexturePool::currentFrame() const
extern "C" Q_DECL_EXPORT
QVideoFrame *ritual_ZNK22QVideoFrameTexturePool12currentFrameEv(
    const QVideoFrameTexturePool *self) {
  return new QVideoFrame(self->currentFrame());
}

//  void QVideoFrameTexturePool::setCurrentFrame(QVideoFrame frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVideoFrameTexturePool15setCurrentFrameE11QVideoFrame(
    QVideoFrameTexturePool *self,
    const QVideoFrame *frame) {
  self->setCurrentFrame(*frame);
}

//  void QVideoFrameTexturePool::onFrameEndInvoked()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVideoFrameTexturePool17onFrameEndInvokedEv(
    QVideoFrameTexturePool *self) {
  self->onFrameEndInvoked();
}

//  void QVideoFrameTexturePool::clearTextures()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QVideoFrameTexturePool13clearTexturesEv(
    QVideoFrameTexturePool *self) {
  self->clearTextures();
}
