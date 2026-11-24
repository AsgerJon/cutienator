//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription()
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTargetDescription *ritual_ZN34QRhiTextureRenderTargetDescriptionC1Ev() {
  return new QRhiTextureRenderTargetDescription();
}

//  QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(co
//      nst QRhiColorAttachment &colorAttachment)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTargetDescription *ritual_ZN34QRhiTextureRenderTargetDescriptionC1ERK19QRhiColorAttachment(
    const QRhiColorAttachment *colorAttachment) {
  return new QRhiTextureRenderTargetDescription(*colorAttachment);
}

//  QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(co
//      nst QRhiColorAttachment &colorAttachment, QRhiRenderBuffer
//      *depthStencilBuffer)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTargetDescription *ritual_ZN34QRhiTextureRenderTargetDescriptionC1ERK19QRhiColorAttachmentP16QRhiRenderBuffer(
    const QRhiColorAttachment *colorAttachment,
    QRhiRenderBuffer *depthStencilBuffer) {
  return new QRhiTextureRenderTargetDescription(
      *colorAttachment,
      depthStencilBuffer);
}

//  QRhiTextureRenderTargetDescription::QRhiTextureRenderTargetDescription(co
//      nst QRhiColorAttachment &colorAttachment, QRhiTexture *depthTexture)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTargetDescription *ritual_ZN34QRhiTextureRenderTargetDescriptionC1ERK19QRhiColorAttachmentP11QRhiTexture(
    const QRhiColorAttachment *colorAttachment,
    QRhiTexture *depthTexture) {
  return new QRhiTextureRenderTargetDescription(
      *colorAttachment,
      depthTexture);
}

//  const QRhiColorAttachment
//      *QRhiTextureRenderTargetDescription::cbeginColorAttachments() const
extern "C" Q_DECL_EXPORT
const QRhiColorAttachment *ritual_ZNK34QRhiTextureRenderTargetDescription22cbeginColorAttachmentsEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->cbeginColorAttachments();
}

//  const QRhiColorAttachment
//      *QRhiTextureRenderTargetDescription::cendColorAttachments() const
extern "C" Q_DECL_EXPORT
const QRhiColorAttachment *ritual_ZNK34QRhiTextureRenderTargetDescription20cendColorAttachmentsEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->cendColorAttachments();
}

//  const QRhiColorAttachment
//      *QRhiTextureRenderTargetDescription::colorAttachmentAt(qsizetype
//      index) const
extern "C" Q_DECL_EXPORT
const QRhiColorAttachment *ritual_ZNK34QRhiTextureRenderTargetDescription17colorAttachmentAtEx(
    const QRhiTextureRenderTargetDescription *self,
    qsizetype index) {
  return self->colorAttachmentAt(index);
}

//  qsizetype QRhiTextureRenderTargetDescription::colorAttachmentCount()
//      const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK34QRhiTextureRenderTargetDescription20colorAttachmentCountEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->colorAttachmentCount();
}

//  QRhiRenderBuffer
//      *QRhiTextureRenderTargetDescription::depthStencilBuffer() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK34QRhiTextureRenderTargetDescription18depthStencilBufferEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->depthStencilBuffer();
}

//  void QRhiTextureRenderTargetDescription::setDepthStencilBuffer(QRhiRender
//      Buffer *renderBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRhiTextureRenderTargetDescription21setDepthStencilBufferEP16QRhiRenderBuffer(
    QRhiTextureRenderTargetDescription *self,
    QRhiRenderBuffer *renderBuffer) {
  self->setDepthStencilBuffer(renderBuffer);
}

//  QRhiTexture *QRhiTextureRenderTargetDescription::depthTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK34QRhiTextureRenderTargetDescription12depthTextureEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->depthTexture();
}

//  void QRhiTextureRenderTargetDescription::setDepthTexture(QRhiTexture
//      *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRhiTextureRenderTargetDescription15setDepthTextureEP11QRhiTexture(
    QRhiTextureRenderTargetDescription *self,
    QRhiTexture *texture) {
  self->setDepthTexture(texture);
}

//  int QRhiTextureRenderTargetDescription::depthLayer() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK34QRhiTextureRenderTargetDescription10depthLayerEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->depthLayer();
}

//  void QRhiTextureRenderTargetDescription::setDepthLayer(int depthLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRhiTextureRenderTargetDescription13setDepthLayerEi(
    QRhiTextureRenderTargetDescription *self,
    int depthLayer) {
  self->setDepthLayer(depthLayer);
}

//  QRhiTexture *QRhiTextureRenderTargetDescription::depthResolveTexture()
//      const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK34QRhiTextureRenderTargetDescription19depthResolveTextureEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->depthResolveTexture();
}

//  void
//      QRhiTextureRenderTargetDescription::setDepthResolveTexture(QRhiTextur
//      e *tex)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRhiTextureRenderTargetDescription22setDepthResolveTextureEP11QRhiTexture(
    QRhiTextureRenderTargetDescription *self,
    QRhiTexture *tex) {
  self->setDepthResolveTexture(tex);
}

//  QRhiShadingRateMap *QRhiTextureRenderTargetDescription::shadingRateMap()
//      const
extern "C" Q_DECL_EXPORT
QRhiShadingRateMap *ritual_ZNK34QRhiTextureRenderTargetDescription14shadingRateMapEv(
    const QRhiTextureRenderTargetDescription *self) {
  return self->shadingRateMap();
}

//  void
//      QRhiTextureRenderTargetDescription::setShadingRateMap(QRhiShadingRate
//      Map *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRhiTextureRenderTargetDescription17setShadingRateMapEP18QRhiShadingRateMap(
    QRhiTextureRenderTargetDescription *self,
    QRhiShadingRateMap *map) {
  self->setShadingRateMap(map);
}

//  QRhiTextureRenderTargetDescription::~QRhiTextureRenderTargetDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QRhiTextureRenderTargetDescriptionD1Ev(
    QRhiTextureRenderTargetDescription *self) {
  delete self;
}
