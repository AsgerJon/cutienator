//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRhiContext *QSSGRhiContextPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSSGRhiContext *ritual_ZN21QSSGRhiContextPrivate6q_funcEv(
    QSSGRhiContextPrivate *self) {
  return self->q_func();
}

//  const QSSGRhiContext *QSSGRhiContextPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSSGRhiContext *ritual_ZNK21QSSGRhiContextPrivate6q_funcEv(
    const QSSGRhiContextPrivate *self) {
  return self->q_func();
}

//  QSSGRhiContextPrivate::QSSGRhiContextPrivate(QSSGRhiContext &rhiCtx, QRhi
//      *rhi_)
extern "C" Q_DECL_EXPORT
QSSGRhiContextPrivate *ritual_ZN21QSSGRhiContextPrivateC1ER14QSSGRhiContextP4QRhi(
    QSSGRhiContext *rhiCtx,
    QRhi *rhi_) {
  return new QSSGRhiContextPrivate(*rhiCtx, rhi_);
}

//  QSSGRhiContextPrivate *QSSGRhiContextPrivate::get(QSSGRhiContext *q)
extern "C" Q_DECL_EXPORT
QSSGRhiContextPrivate *ritual_ZN21QSSGRhiContextPrivate3getEP14QSSGRhiContext(
    QSSGRhiContext *q) {
  return QSSGRhiContextPrivate::get(q);
}

//  const QSSGRhiContextPrivate *QSSGRhiContextPrivate::get(const
//      QSSGRhiContext *q)
extern "C" Q_DECL_EXPORT
const QSSGRhiContextPrivate *ritual_ZN21QSSGRhiContextPrivate3getEPK14QSSGRhiContext(
    const QSSGRhiContext *q) {
  return QSSGRhiContextPrivate::get(q);
}

//  bool QSSGRhiContextPrivate::shaderDebuggingEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRhiContextPrivate22shaderDebuggingEnabledEv() {
  return QSSGRhiContextPrivate::shaderDebuggingEnabled();
}

//  bool QSSGRhiContextPrivate::editorMode()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRhiContextPrivate10editorModeEv() {
  return QSSGRhiContextPrivate::editorMode();
}

//  void QSSGRhiContextPrivate::setMainRenderPassDescriptor(QRhiRenderPassDes
//      criptor *rpDesc)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate27setMainRenderPassDescriptorEP24QRhiRenderPassDescriptor(
    QSSGRhiContextPrivate *self,
    QRhiRenderPassDescriptor *rpDesc) {
  self->setMainRenderPassDescriptor(rpDesc);
}

//  void QSSGRhiContextPrivate::setCommandBuffer(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate16setCommandBufferEP17QRhiCommandBuffer(
    QSSGRhiContextPrivate *self,
    QRhiCommandBuffer *cb) {
  self->setCommandBuffer(cb);
}

//  void QSSGRhiContextPrivate::setRenderTarget(QRhiRenderTarget *rt)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate15setRenderTargetEP16QRhiRenderTarget(
    QSSGRhiContextPrivate *self,
    QRhiRenderTarget *rt) {
  self->setRenderTarget(rt);
}

//  void QSSGRhiContextPrivate::setMainPassSampleCount(int samples)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate22setMainPassSampleCountEi(
    QSSGRhiContextPrivate *self,
    int samples) {
  self->setMainPassSampleCount(samples);
}

//  void QSSGRhiContextPrivate::setMainPassViewCount(int viewCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate20setMainPassViewCountEi(
    QSSGRhiContextPrivate *self,
    int viewCount) {
  self->setMainPassViewCount(viewCount);
}

//  void QSSGRhiContextPrivate::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate22releaseCachedResourcesEv(
    QSSGRhiContextPrivate *self) {
  self->releaseCachedResources();
}

//  void QSSGRhiContextPrivate::registerTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate15registerTextureEP11QRhiTexture(
    QSSGRhiContextPrivate *self,
    QRhiTexture *texture) {
  self->registerTexture(texture);
}

//  void QSSGRhiContextPrivate::releaseTexture(QRhiTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate14releaseTextureEP11QRhiTexture(
    QSSGRhiContextPrivate *self,
    QRhiTexture *texture) {
  self->releaseTexture(texture);
}

//  void QSSGRhiContextPrivate::registerMesh(QSSGRenderMesh *mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate12registerMeshEP14QSSGRenderMesh(
    QSSGRhiContextPrivate *self,
    QSSGRenderMesh *mesh) {
  self->registerMesh(mesh);
}

//  void QSSGRhiContextPrivate::releaseMesh(QSSGRenderMesh *mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate11releaseMeshEP14QSSGRenderMesh(
    QSSGRhiContextPrivate *self,
    QSSGRenderMesh *mesh) {
  self->releaseMesh(mesh);
}

//  QRhiShaderResourceBindings *QSSGRhiContextPrivate::srb(const
//      QSSGRhiShaderResourceBindingList &bindings)
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZN21QSSGRhiContextPrivate3srbERK32QSSGRhiShaderResourceBindingList(
    QSSGRhiContextPrivate *self,
    const QSSGRhiShaderResourceBindingList *bindings) {
  return self->srb(*bindings);
}

//  void
//      QSSGRhiContextPrivate::releaseCachedSrb(QSSGRhiShaderResourceBindingL
//      ist &bindings)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate16releaseCachedSrbER32QSSGRhiShaderResourceBindingList(
    QSSGRhiContextPrivate *self,
    QSSGRhiShaderResourceBindingList *bindings) {
  self->releaseCachedSrb(*bindings);
}

//  QRhiGraphicsPipeline *QSSGRhiContextPrivate::pipeline(const
//      QSSGRhiGraphicsPipelineState &ps, QRhiRenderPassDescriptor *rpDesc,
//      QRhiShaderResourceBindings *srb)
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN21QSSGRhiContextPrivate8pipelineERK28QSSGRhiGraphicsPipelineStateP24QRhiRenderPassDescriptorP26QRhiShaderResourceBindings(
    QSSGRhiContextPrivate *self,
    const QSSGRhiGraphicsPipelineState *ps,
    QRhiRenderPassDescriptor *rpDesc,
    QRhiShaderResourceBindings *srb) {
  return self->pipeline(*ps, rpDesc, srb);
}

//  QRhiGraphicsPipeline *QSSGRhiContextPrivate::pipeline(const
//      QSSGGraphicsPipelineStateKey &key, QRhiRenderPassDescriptor *rpDesc,
//      QRhiShaderResourceBindings *srb)
extern "C" Q_DECL_EXPORT
QRhiGraphicsPipeline *ritual_ZN21QSSGRhiContextPrivate8pipelineERK28QSSGGraphicsPipelineStateKeyP24QRhiRenderPassDescriptorP26QRhiShaderResourceBindings(
    QSSGRhiContextPrivate *self,
    const QSSGGraphicsPipelineStateKey *key,
    QRhiRenderPassDescriptor *rpDesc,
    QRhiShaderResourceBindings *srb) {
  return self->pipeline(*key, rpDesc, srb);
}

//  QRhiComputePipeline *QSSGRhiContextPrivate::computePipeline(const QShader
//      &shader, QRhiShaderResourceBindings *srb)
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN21QSSGRhiContextPrivate15computePipelineERK7QShaderP26QRhiShaderResourceBindings(
    QSSGRhiContextPrivate *self,
    const QShader *shader,
    QRhiShaderResourceBindings *srb) {
  return self->computePipeline(*shader, srb);
}

//  QRhiComputePipeline *QSSGRhiContextPrivate::computePipeline(const
//      QSSGComputePipelineStateKey &key, QRhiShaderResourceBindings *srb)
extern "C" Q_DECL_EXPORT
QRhiComputePipeline *ritual_ZN21QSSGRhiContextPrivate15computePipelineERK27QSSGComputePipelineStateKeyP26QRhiShaderResourceBindings(
    QSSGRhiContextPrivate *self,
    const QSSGComputePipelineStateKey *key,
    QRhiShaderResourceBindings *srb) {
  return self->computePipeline(*key, srb);
}

//  QSSGRhiDrawCallData &QSSGRhiContextPrivate::drawCallData(const
//      QSSGRhiDrawCallDataKey &key)
extern "C" Q_DECL_EXPORT
QSSGRhiDrawCallData *ritual_ZN21QSSGRhiContextPrivate12drawCallDataERK22QSSGRhiDrawCallDataKey(
    QSSGRhiContextPrivate *self,
    const QSSGRhiDrawCallDataKey *key) {
  return &(self->drawCallData(*key));
}

//  void QSSGRhiContextPrivate::releaseDrawCallData(QSSGRhiDrawCallData &dcd)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate19releaseDrawCallDataER19QSSGRhiDrawCallData(
    QSSGRhiContextPrivate *self,
    QSSGRhiDrawCallData *dcd) {
  self->releaseDrawCallData(*dcd);
}

//  void QSSGRhiContextPrivate::cleanupDrawCallData(const QSSGRenderModel
//      *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate19cleanupDrawCallDataEPK15QSSGRenderModel(
    QSSGRhiContextPrivate *self,
    const QSSGRenderModel *model) {
  self->cleanupDrawCallData(model);
}

//  QSSGRhiInstanceBufferData
//      &QSSGRhiContextPrivate::instanceBufferData(QSSGRenderInstanceTable
//      *instanceTable)
extern "C" Q_DECL_EXPORT
QSSGRhiInstanceBufferData *ritual_ZN21QSSGRhiContextPrivate18instanceBufferDataEP23QSSGRenderInstanceTable(
    QSSGRhiContextPrivate *self,
    QSSGRenderInstanceTable *instanceTable) {
  return &(self->instanceBufferData(instanceTable));
}

//  void QSSGRhiContextPrivate::releaseInstanceBuffer(QSSGRenderInstanceTable
//      *instanceTable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivate21releaseInstanceBufferEP23QSSGRenderInstanceTable(
    QSSGRhiContextPrivate *self,
    QSSGRenderInstanceTable *instanceTable) {
  self->releaseInstanceBuffer(instanceTable);
}

//  QSSGRhiInstanceBufferData
//      &QSSGRhiContextPrivate::instanceBufferData(const QSSGRenderModel
//      *model)
extern "C" Q_DECL_EXPORT
QSSGRhiInstanceBufferData *ritual_ZN21QSSGRhiContextPrivate18instanceBufferDataEPK15QSSGRenderModel(
    QSSGRhiContextPrivate *self,
    const QSSGRenderModel *model) {
  return &(self->instanceBufferData(model));
}

//  QSSGRhiParticleData &QSSGRhiContextPrivate::particleData(const
//      QSSGRenderGraphObject *particlesOrModel)
extern "C" Q_DECL_EXPORT
QSSGRhiParticleData *ritual_ZN21QSSGRhiContextPrivate12particleDataEPK21QSSGRenderGraphObject(
    QSSGRhiContextPrivate *self,
    const QSSGRenderGraphObject *particlesOrModel) {
  return &(self->particleData(particlesOrModel));
}

//  QSSGRhiContextPrivate::~QSSGRhiContextPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRhiContextPrivateD1Ev(QSSGRhiContextPrivate *self) {
  delete self;
}
