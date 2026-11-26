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

//  bool QSSGRenderer::prepareLayerForRender(QSSGRenderLayer &inLayer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSSGRenderer21prepareLayerForRenderER15QSSGRenderLayer(
    QSSGRenderer *self,
    QSSGRenderLayer *inLayer) {
  return self->prepareLayerForRender(*inLayer);
}

//  void QSSGRenderer::rhiPrepare(QSSGRenderLayer &inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer10rhiPrepareER15QSSGRenderLayer(
    QSSGRenderer *self,
    QSSGRenderLayer *inLayer) {
  self->rhiPrepare(*inLayer);
}

//  void QSSGRenderer::rhiRender(QSSGRenderLayer &inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer9rhiRenderER15QSSGRenderLayer(
    QSSGRenderer *self,
    QSSGRenderLayer *inLayer) {
  self->rhiRender(*inLayer);
}

//  void QSSGRenderer::beginFrame(QSSGRenderLayer &layer, bool
//      allowRecursion)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer10beginFrameER15QSSGRenderLayerb(
    QSSGRenderer *self,
    QSSGRenderLayer *layer,
    bool allowRecursion) {
  self->beginFrame(*layer, allowRecursion);
}

//  bool QSSGRenderer::endFrame(QSSGRenderLayer &layer, bool allowRecursion)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QSSGRenderer8endFrameER15QSSGRenderLayerb(
    QSSGRenderer *self,
    QSSGRenderLayer *layer,
    bool allowRecursion) {
  return self->endFrame(*layer, allowRecursion);
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

//  const std::unique_ptr<QSSGRhiQuadRenderer>
//      &QSSGRenderer::rhiQuadRenderer() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGRhiQuadRenderer> *ritual_ZNK12QSSGRenderer15rhiQuadRendererEv(
    const QSSGRenderer *self) {
  return &(self->rhiQuadRenderer());
}

//  const std::unique_ptr<QSSGRhiCubeRenderer>
//      &QSSGRenderer::rhiCubeRenderer() const
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGRhiCubeRenderer> *ritual_ZNK12QSSGRenderer15rhiCubeRendererEv(
    const QSSGRenderer *self) {
  return &(self->rhiCubeRenderer());
}

//  QSSGRenderContextInterface *QSSGRenderer::contextInterface() const
extern "C" Q_DECL_EXPORT
QSSGRenderContextInterface *ritual_ZNK12QSSGRenderer16contextInterfaceEv(
    const QSSGRenderer *self) {
  return self->contextInterface();
}

//  void QSSGRenderer::beginSubLayerRender(QSSGLayerRenderData &inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer19beginSubLayerRenderER19QSSGLayerRenderData(
    QSSGRenderer *self,
    QSSGLayerRenderData *inLayer) {
  self->beginSubLayerRender(*inLayer);
}

//  void QSSGRenderer::endSubLayerRender(QSSGLayerRenderData &inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer17endSubLayerRenderER19QSSGLayerRenderData(
    QSSGRenderer *self,
    QSSGLayerRenderData *inLayer) {
  self->endSubLayerRender(*inLayer);
}

//  void QSSGRenderer::releaseItem2DData(const QSSGRenderItem2D &item2D)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer17releaseItem2DDataERK16QSSGRenderItem2D(
    QSSGRenderer *self,
    const QSSGRenderItem2D *item2D) {
  self->releaseItem2DData(*item2D);
}

//  void QSSGRenderer::cleanupResources(QList<QSSGRenderGraphObject *>
//      &resources)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer16cleanupResourcesER5QListIP21QSSGRenderGraphObjectE(
    QSSGRenderer *self,
    QList<QSSGRenderGraphObject *> *resources) {
  self->cleanupResources(*resources);
}

//  void QSSGRenderer::cleanupResources(QSet<QSSGRenderGraphObject *>
//      &resources)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer16cleanupResourcesER4QSetIP21QSSGRenderGraphObjectE(
    QSSGRenderer *self,
    QSet<QSSGRenderGraphObject *> *resources) {
  self->cleanupResources(*resources);
}

//  QSSGLayerRenderData
//      *QSSGRenderer::getOrCreateLayerRenderData(QSSGRenderLayer &layer)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZN12QSSGRenderer26getOrCreateLayerRenderDataER15QSSGRenderLayer(
    QSSGRenderer *self,
    QSSGRenderLayer *layer) {
  return self->getOrCreateLayerRenderData(*layer);
}

//  void QSSGRenderer::beginLayerRender(QSSGLayerRenderData &inLayer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer16beginLayerRenderER19QSSGLayerRenderData(
    QSSGRenderer *self,
    QSSGLayerRenderData *inLayer) {
  self->beginLayerRender(*inLayer);
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

//  void QSSGRenderer::registerItem2DData(QSSGRenderItem2DData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer18registerItem2DDataER20QSSGRenderItem2DData(
    QSSGRenderer *self,
    QSSGRenderItem2DData *data) {
  self->registerItem2DData(*data);
}

//  void QSSGRenderer::unregisterItem2DData(QSSGRenderItem2DData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSSGRenderer20unregisterItem2DDataER20QSSGRenderItem2DData(
    QSSGRenderer *self,
    QSSGRenderItem2DData *data) {
  self->unregisterItem2DData(*data);
}
