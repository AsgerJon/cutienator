//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiColorAttachment::QRhiColorAttachment()
extern "C" Q_DECL_EXPORT
QRhiColorAttachment *ritual_ZN19QRhiColorAttachmentC1Ev() {
  return new QRhiColorAttachment();
}

//  QRhiColorAttachment::QRhiColorAttachment(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
QRhiColorAttachment *ritual_ZN19QRhiColorAttachmentC1EP11QRhiTexture(
    QRhiTexture *texture) {
  return new QRhiColorAttachment(texture);
}

//  QRhiColorAttachment::QRhiColorAttachment(QRhiRenderBuffer *renderBuffer)
extern "C" Q_DECL_EXPORT
QRhiColorAttachment *ritual_ZN19QRhiColorAttachmentC1EP16QRhiRenderBuffer(
    QRhiRenderBuffer *renderBuffer) {
  return new QRhiColorAttachment(renderBuffer);
}

//  QRhiTexture *QRhiColorAttachment::texture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QRhiColorAttachment7textureEv(
    const QRhiColorAttachment *self) {
  return self->texture();
}

//  void QRhiColorAttachment::setTexture(QRhiTexture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment10setTextureEP11QRhiTexture(
    QRhiColorAttachment *self,
    QRhiTexture *tex) {
  self->setTexture(tex);
}

//  QRhiRenderBuffer *QRhiColorAttachment::renderBuffer() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK19QRhiColorAttachment12renderBufferEv(
    const QRhiColorAttachment *self) {
  return self->renderBuffer();
}

//  void QRhiColorAttachment::setRenderBuffer(QRhiRenderBuffer *rb)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment15setRenderBufferEP16QRhiRenderBuffer(
    QRhiColorAttachment *self,
    QRhiRenderBuffer *rb) {
  self->setRenderBuffer(rb);
}

//  int QRhiColorAttachment::layer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRhiColorAttachment5layerEv(
    const QRhiColorAttachment *self) {
  return self->layer();
}

//  void QRhiColorAttachment::setLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment8setLayerEi(
    QRhiColorAttachment *self,
    int layer) {
  self->setLayer(layer);
}

//  int QRhiColorAttachment::level() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRhiColorAttachment5levelEv(
    const QRhiColorAttachment *self) {
  return self->level();
}

//  void QRhiColorAttachment::setLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment8setLevelEi(
    QRhiColorAttachment *self,
    int level) {
  self->setLevel(level);
}

//  QRhiTexture *QRhiColorAttachment::resolveTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QRhiColorAttachment14resolveTextureEv(
    const QRhiColorAttachment *self) {
  return self->resolveTexture();
}

//  void QRhiColorAttachment::setResolveTexture(QRhiTexture *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment17setResolveTextureEP11QRhiTexture(
    QRhiColorAttachment *self,
    QRhiTexture *tex) {
  self->setResolveTexture(tex);
}

//  int QRhiColorAttachment::resolveLayer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRhiColorAttachment12resolveLayerEv(
    const QRhiColorAttachment *self) {
  return self->resolveLayer();
}

//  void QRhiColorAttachment::setResolveLayer(int layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment15setResolveLayerEi(
    QRhiColorAttachment *self,
    int layer) {
  self->setResolveLayer(layer);
}

//  int QRhiColorAttachment::resolveLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRhiColorAttachment12resolveLevelEv(
    const QRhiColorAttachment *self) {
  return self->resolveLevel();
}

//  void QRhiColorAttachment::setResolveLevel(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment15setResolveLevelEi(
    QRhiColorAttachment *self,
    int level) {
  self->setResolveLevel(level);
}

//  int QRhiColorAttachment::multiViewCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRhiColorAttachment14multiViewCountEv(
    const QRhiColorAttachment *self) {
  return self->multiViewCount();
}

//  void QRhiColorAttachment::setMultiViewCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachment17setMultiViewCountEi(
    QRhiColorAttachment *self,
    int count) {
  self->setMultiViewCount(count);
}

//  QRhiColorAttachment::~QRhiColorAttachment()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRhiColorAttachmentD1Ev(QRhiColorAttachment *self) {
  delete self;
}
