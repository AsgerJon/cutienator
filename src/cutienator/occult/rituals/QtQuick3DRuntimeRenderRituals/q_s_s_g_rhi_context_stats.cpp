//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRhiContextStats &QSSGRhiContextStats::get(QSSGRhiContext &rhiCtx)
extern "C" Q_DECL_EXPORT
QSSGRhiContextStats *ritual_ZN19QSSGRhiContextStats3getER14QSSGRhiContext(
    QSSGRhiContext *rhiCtx) {
  return &(QSSGRhiContextStats::get(*rhiCtx));
}

//  const QSSGRhiContextStats &QSSGRhiContextStats::get(const QSSGRhiContext
//      &rhiCtx)
extern "C" Q_DECL_EXPORT
QSSGRhiContextStats *ritual_ZN19QSSGRhiContextStats3getERK14QSSGRhiContext(
    const QSSGRhiContext *rhiCtx) {
  return new QSSGRhiContextStats(QSSGRhiContextStats::get(*rhiCtx));
}

//  QSSGRhiContextStats::QSSGRhiContextStats(QSSGRhiContext &context)
extern "C" Q_DECL_EXPORT
QSSGRhiContextStats *ritual_ZN19QSSGRhiContextStatsC1ER14QSSGRhiContext(
    QSSGRhiContext *context) {
  return new QSSGRhiContextStats(*context);
}

//  bool QSSGRhiContextStats::profilingEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSSGRhiContextStats16profilingEnabledEv() {
  return QSSGRhiContextStats::profilingEnabled();
}

//  bool QSSGRhiContextStats::rendererDebugEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSSGRhiContextStats20rendererDebugEnabledEv() {
  return QSSGRhiContextStats::rendererDebugEnabled();
}

//  bool QSSGRhiContextStats::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGRhiContextStats9isEnabledEv(
    const QSSGRhiContextStats *self) {
  return self->isEnabled();
}

//  void QSSGRhiContextStats::drawIndexed(quint32 indexCount, quint32
//      instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats11drawIndexedEjj(
    QSSGRhiContextStats *self,
    quint32 indexCount,
    quint32 instanceCount) {
  self->drawIndexed(indexCount, instanceCount);
}

//  void QSSGRhiContextStats::draw(quint32 vertexCount, quint32
//      instanceCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats4drawEjj(
    QSSGRhiContextStats *self,
    quint32 vertexCount,
    quint32 instanceCount) {
  self->draw(vertexCount, instanceCount);
}

//  void QSSGRhiContextStats::meshDataSizeChanges(quint64 newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats19meshDataSizeChangesEy(
    QSSGRhiContextStats *self,
    quint64 newSize) {
  self->meshDataSizeChanges(newSize);
}

//  void QSSGRhiContextStats::imageDataSizeChanges(quint64 newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats20imageDataSizeChangesEy(
    QSSGRhiContextStats *self,
    quint64 newSize) {
  self->imageDataSizeChanges(newSize);
}

//  void QSSGRhiContextStats::registerMaterialShaderGenerationTime(qint64 ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats36registerMaterialShaderGenerationTimeEx(
    QSSGRhiContextStats *self,
    qint64 ms) {
  self->registerMaterialShaderGenerationTime(ms);
}

//  void QSSGRhiContextStats::registerEffectShaderGenerationTime(qint64 ms)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats34registerEffectShaderGenerationTimeEx(
    QSSGRhiContextStats *self,
    qint64 ms) {
  self->registerEffectShaderGenerationTime(ms);
}

//  quint64 QSSGRhiContextStats::totalDrawCallCountForPass(const
//      QSSGRhiContextStats::RenderPassInfo &pass)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN19QSSGRhiContextStats25totalDrawCallCountForPassERKNS_14RenderPassInfoE(
    const QSSGRhiContextStats::RenderPassInfo *pass) {
  return QSSGRhiContextStats::totalDrawCallCountForPass(*pass);
}

//  quint64 QSSGRhiContextStats::totalVertexCountForPass(const
//      QSSGRhiContextStats::RenderPassInfo &pass)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN19QSSGRhiContextStats23totalVertexCountForPassERKNS_14RenderPassInfoE(
    const QSSGRhiContextStats::RenderPassInfo *pass) {
  return QSSGRhiContextStats::totalVertexCountForPass(*pass);
}

//  void QSSGRhiContextStats::start(QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats5startEP15QSSGRenderLayer(
    QSSGRhiContextStats *self,
    QSSGRenderLayer *layer) {
  self->start(layer);
}

//  void QSSGRhiContextStats::stop(QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats4stopEP15QSSGRenderLayer(
    QSSGRhiContextStats *self,
    QSSGRenderLayer *layer) {
  self->stop(layer);
}

//  void QSSGRhiContextStats::beginRenderPass(QRhiTextureRenderTarget *rt)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats15beginRenderPassEP23QRhiTextureRenderTarget(
    QSSGRhiContextStats *self,
    QRhiTextureRenderTarget *rt) {
  self->beginRenderPass(rt);
}

//  void QSSGRhiContextStats::endRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats13endRenderPassEv(
    QSSGRhiContextStats *self) {
  self->endRenderPass();
}

//  void QSSGRhiContextStats::printRenderPass(const RenderPassInfo &rp)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats15printRenderPassERKNS_14RenderPassInfoE(
    QSSGRhiContextStats *self,
    const QSSGRhiContextStats::RenderPassInfo *rp) {
  self->printRenderPass(*rp);
}

//  void QSSGRhiContextStats::cleanupLayerInfo(QSSGRenderLayer *layer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStats16cleanupLayerInfoEP15QSSGRenderLayer(
    QSSGRhiContextStats *self,
    QSSGRenderLayer *layer) {
  self->cleanupLayerInfo(layer);
}

//  QSSGRhiContextStats::~QSSGRhiContextStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiContextStatsD1Ev(QSSGRhiContextStats *self) {
  delete self;
}
