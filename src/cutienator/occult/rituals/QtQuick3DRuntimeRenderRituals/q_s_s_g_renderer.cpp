//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>

//  QSSGRenderer::QSSGRenderer()
extern "C" Q_DECL_EXPORT
QSSGRenderer *ritual_ZN12QSSGRendererC1Ev() {
  return new QSSGRenderer();
}

//  QSSGRenderer::~QSSGRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRendererD1Ev(QSSGRenderer *self) {
  delete self;
}

//  quint32 QSSGRenderer::frameCount() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QSSGRenderer10frameCountEv(const QSSGRenderer *self) {
  return self->frameCount();
}

//  void QSSGRenderer::setViewport(QRect inViewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer11setViewportE5QRect(
    QSSGRenderer *self,
    const QRect *inViewport) {
  self->setViewport(*inViewport);
}

//  QRect QSSGRenderer::viewport() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QSSGRenderer8viewportEv(const QSSGRenderer *self) {
  return new QRect(self->viewport());
}

//  void QSSGRenderer::setDpr(float dpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer6setDprEf(QSSGRenderer *self, float dpr) {
  self->setDpr(dpr);
}

//  float QSSGRenderer::dpr() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK12QSSGRenderer3dprEv(const QSSGRenderer *self) {
  return self->dpr();
}

//  void QSSGRenderer::setScissorRect(QRect inScissorRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer14setScissorRectE5QRect(
    QSSGRenderer *self,
    const QRect *inScissorRect) {
  self->setScissorRect(*inScissorRect);
}

//  QRect QSSGRenderer::scissorRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QSSGRenderer11scissorRectEv(const QSSGRenderer *self) {
  return new QRect(self->scissorRect());
}

//  quint32 QSSGRenderer::frameDepth() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK12QSSGRenderer10frameDepthEv(const QSSGRenderer *self) {
  return self->frameDepth();
}

//  QSSGRenderContextInterface *QSSGRenderer::contextInterface() const
extern "C" Q_DECL_EXPORT
QSSGRenderContextInterface *ritual_ZNK12QSSGRenderer16contextInterfaceEv(
    const QSSGRenderer *self) {
  return self->contextInterface();
}

//  void QSSGRenderer::endLayerRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer14endLayerRenderEv(QSSGRenderer *self) {
  self->endLayerRender();
}

//  void QSSGRenderer::addMaterialDirtyClear(QSSGRenderGraphObject *material)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer21addMaterialDirtyClearEP21QSSGRenderGraphObject(
    QSSGRenderer *self,
    QSSGRenderGraphObject *material) {
  self->addMaterialDirtyClear(material);
}

//  void QSSGRenderer::cleanupUnreferencedBuffers(QSSGRenderLayer *inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer26cleanupUnreferencedBuffersEP15QSSGRenderLayer(
    QSSGRenderer *self,
    QSSGRenderLayer *inLayer) {
  self->cleanupUnreferencedBuffers(inLayer);
}

//  void QSSGRenderer::resetResourceCounters(QSSGRenderLayer *inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer21resetResourceCountersEP15QSSGRenderLayer(
    QSSGRenderer *self,
    QSSGRenderLayer *inLayer) {
  self->resetResourceCounters(inLayer);
}

//  void QSSGRenderer::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer22releaseCachedResourcesEv(QSSGRenderer *self) {
  self->releaseCachedResources();
}
