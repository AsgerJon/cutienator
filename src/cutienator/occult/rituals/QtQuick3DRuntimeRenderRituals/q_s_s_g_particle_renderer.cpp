//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticleshaderkeys_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGParticleRenderer::updateUniformsForParticles(const
//      QSSGLayerRenderData &inData, QSSGRhiShaderPipeline &shaderPipeline,
//      QSSGRhiContext *rhiCtx, char *ubufData, QSSGParticlesRenderable
//      &renderable, const QSSGRenderCameraList &cameras)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRenderer26updateUniformsForParticlesERK19QSSGLayerRenderDataR21QSSGRhiShaderPipelineP14QSSGRhiContextPcR23QSSGParticlesRenderableRK15QVarLengthArrayIP16QSSGRenderCameraLx2EE(
    const QSSGLayerRenderData *inData,
    QSSGRhiShaderPipeline *shaderPipeline,
    QSSGRhiContext *rhiCtx,
    char *ubufData,
    QSSGParticlesRenderable *renderable,
    const QSSGRenderCameraList *cameras) {
  QSSGParticleRenderer::updateUniformsForParticles(
      *inData,
      *shaderPipeline,
      rhiCtx,
      ubufData,
      *renderable,
      *cameras);
}

//  void QSSGParticleRenderer::updateUniformsForParticleModel(QSSGRhiShaderPi
//      peline &shaderPipeline, char *ubufData, const QSSGRenderModel *model,
//      quint32 offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRenderer30updateUniformsForParticleModelER21QSSGRhiShaderPipelinePcPK15QSSGRenderModelj(
    QSSGRhiShaderPipeline *shaderPipeline,
    char *ubufData,
    const QSSGRenderModel *model,
    quint32 offset) {
  QSSGParticleRenderer::updateUniformsForParticleModel(
      *shaderPipeline,
      ubufData,
      model,
      offset);
}

//  QSSGRhiShaderPipelinePtr
//      QSSGParticleRenderer::getShaderPipelineParticles(QSSGRenderer
//      &renderer, QSSGParticlesRenderable &inRenderable, const
//      QSSGShaderFeatures &inFeatureSet)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN20QSSGParticleRenderer26getShaderPipelineParticlesER12QSSGRendererR23QSSGParticlesRenderableRK18QSSGShaderFeatures(
    QSSGRenderer *renderer,
    QSSGParticlesRenderable *inRenderable,
    const QSSGShaderFeatures *inFeatureSet) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGParticleRenderer::getShaderPipelineParticles(
          *renderer,
          *inRenderable,
          *inFeatureSet));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGParticleRenderer::generateRhiShaderPipeline(QSSGRenderer
//      &renderer, QSSGParticlesRenderable &inRenderable, const
//      QSSGShaderFeatures &inFeatureSet, QByteArray &shaderString, const
//      QSSGShaderParticleMaterialKeyProperties &shaderKeyProperties)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN20QSSGParticleRenderer25generateRhiShaderPipelineER12QSSGRendererR23QSSGParticlesRenderableRK18QSSGShaderFeaturesR10QByteArrayRK39QSSGShaderParticleMaterialKeyProperties(
    QSSGRenderer *renderer,
    QSSGParticlesRenderable *inRenderable,
    const QSSGShaderFeatures *inFeatureSet,
    QByteArray *shaderString,
    const QSSGShaderParticleMaterialKeyProperties *shaderKeyProperties) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGParticleRenderer::generateRhiShaderPipeline(
          *renderer,
          *inRenderable,
          *inFeatureSet,
          *shaderString,
          *shaderKeyProperties));
}

//  void QSSGParticleRenderer::rhiPrepareRenderable(QSSGRhiShaderPipeline
//      &shaderPipeline, QSSGPassKey passKey, QSSGRhiContext *rhiCtx,
//      QSSGRhiGraphicsPipelineState *ps, QSSGParticlesRenderable
//      &renderable, const QSSGLayerRenderData &inData,
//      QRhiRenderPassDescriptor *renderPassDescriptor, int samples, int
//      viewCount, QSSGRenderCamera *alteredCamera, QSSGRenderTextureCubeFace
//      cubeFace, QSSGReflectionMapEntry *entry, bool oit)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRenderer20rhiPrepareRenderableER21QSSGRhiShaderPipelinePvP14QSSGRhiContextP28QSSGRhiGraphicsPipelineStateR23QSSGParticlesRenderableRK19QSSGLayerRenderDataP24QRhiRenderPassDescriptoriiP16QSSGRenderCamera25QSSGRenderTextureCubeFaceP22QSSGReflectionMapEntryb(
    QSSGRhiShaderPipeline *shaderPipeline,
    QSSGPassKey passKey,
    QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps,
    QSSGParticlesRenderable *renderable,
    const QSSGLayerRenderData *inData,
    QRhiRenderPassDescriptor *renderPassDescriptor,
    int samples,
    int viewCount,
    QSSGRenderCamera *alteredCamera,
    QSSGRenderTextureCubeFace cubeFace,
    QSSGReflectionMapEntry *entry,
    bool oit) {
  QSSGParticleRenderer::rhiPrepareRenderable(
      *shaderPipeline,
      passKey,
      rhiCtx,
      ps,
      *renderable,
      *inData,
      renderPassDescriptor,
      samples,
      viewCount,
      alteredCamera,
      cubeFace,
      entry,
      oit);
}

//  void QSSGParticleRenderer::rhiRenderRenderable(QSSGRhiContext *rhiCtx,
//      QSSGParticlesRenderable &renderable, bool *needsSetViewport,
//      QSSGRenderTextureCubeFace cubeFace, const
//      QSSGRhiGraphicsPipelineState &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRenderer19rhiRenderRenderableEP14QSSGRhiContextR23QSSGParticlesRenderablePb25QSSGRenderTextureCubeFaceRK28QSSGRhiGraphicsPipelineState(
    QSSGRhiContext *rhiCtx,
    QSSGParticlesRenderable *renderable,
    bool *needsSetViewport,
    QSSGRenderTextureCubeFace cubeFace,
    const QSSGRhiGraphicsPipelineState *state) {
  QSSGParticleRenderer::rhiRenderRenderable(
      rhiCtx,
      *renderable,
      needsSetViewport,
      cubeFace,
      *state);
}

//  void QSSGParticleRenderer::prepareParticlesForModel(QSSGRhiShaderPipeline
//      &shaderPipeline, QSSGRhiContext *rhiCtx,
//      QSSGRhiShaderResourceBindingList &bindings, const QSSGRenderModel
//      *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRenderer24prepareParticlesForModelER21QSSGRhiShaderPipelineP14QSSGRhiContextR32QSSGRhiShaderResourceBindingListPK15QSSGRenderModel(
    QSSGRhiShaderPipeline *shaderPipeline,
    QSSGRhiContext *rhiCtx,
    QSSGRhiShaderResourceBindingList *bindings,
    const QSSGRenderModel *model) {
  QSSGParticleRenderer::prepareParticlesForModel(
      *shaderPipeline,
      rhiCtx,
      *bindings,
      model);
}

//  QSSGShaderFeatures QSSGParticleRenderer::particleShaderFeatures(const
//      QSSGShaderFeatures &features)
extern "C" Q_DECL_EXPORT
QSSGShaderFeatures *ritual_ZN20QSSGParticleRenderer22particleShaderFeaturesERK18QSSGShaderFeatures(
    const QSSGShaderFeatures *features) {
  return new QSSGShaderFeatures(
      QSSGParticleRenderer::particleShaderFeatures(
          *features));
}

//  void QSSGParticleRenderer::setShaderCacheEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRenderer21setShaderCacheEnabledEb(bool enabled) {
  QSSGParticleRenderer::setShaderCacheEnabled(enabled);
}

//  QSSGParticleRenderer::~QSSGParticleRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSSGParticleRendererD1Ev(QSSGParticleRenderer *self) {
  delete self;
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGParticleRenderer gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGParticleRenderer__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
