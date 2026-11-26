//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicustommaterialsyste
//  m_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermesh_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGCustomMaterialSystem::setShaderResources(char *ubufData, const
//      QSSGRenderCustomMaterial &inMaterial, const QByteArray
//      &inPropertyName, const QVariant &propertyValue,
//      QSSGRenderShaderValue::Type inPropertyType, QSSGRhiShaderPipeline
//      &shaderPipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem18setShaderResourcesEPcRK24QSSGRenderCustomMaterialRK10QByteArrayRK8QVariantN21QSSGRenderShaderValue4TypeER21QSSGRhiShaderPipeline(
    QSSGCustomMaterialSystem *self,
    char *ubufData,
    const QSSGRenderCustomMaterial *inMaterial,
    const QByteArray *inPropertyName,
    const QVariant *propertyValue,
    QSSGRenderShaderValue::Type inPropertyType,
    QSSGRhiShaderPipeline *shaderPipeline) {
  self->setShaderResources(
      ubufData,
      *inMaterial,
      *inPropertyName,
      *propertyValue,
      inPropertyType,
      *shaderPipeline);
}

//  QSSGCustomMaterialSystem::QSSGCustomMaterialSystem()
extern "C" Q_DECL_EXPORT
QSSGCustomMaterialSystem *ritual_ZN24QSSGCustomMaterialSystemC1Ev() {
  return new QSSGCustomMaterialSystem();
}

//  QSSGCustomMaterialSystem::~QSSGCustomMaterialSystem()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystemD1Ev(
    QSSGCustomMaterialSystem *self) {
  delete self;
}

//  void QSSGCustomMaterialSystem::setRenderContextInterface(QSSGRenderContex
//      tInterface *inContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem25setRenderContextInterfaceEP26QSSGRenderContextInterface(
    QSSGCustomMaterialSystem *self,
    QSSGRenderContextInterface *inContext) {
  self->setRenderContextInterface(inContext);
}

//  void QSSGCustomMaterialSystem::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem22releaseCachedResourcesEv(
    QSSGCustomMaterialSystem *self) {
  self->releaseCachedResources();
}

//  bool QSSGCustomMaterialSystem::prepareForRender(const QSSGRenderModel
//      &inModel, const QSSGRenderSubset &inSubset, QSSGRenderCustomMaterial
//      &inMaterial)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSSGCustomMaterialSystem16prepareForRenderERK15QSSGRenderModelRK16QSSGRenderSubsetR24QSSGRenderCustomMaterial(
    QSSGCustomMaterialSystem *self,
    const QSSGRenderModel *inModel,
    const QSSGRenderSubset *inSubset,
    QSSGRenderCustomMaterial *inMaterial) {
  return self->prepareForRender(*inModel, *inSubset, *inMaterial);
}

//  QSSGRhiShaderPipelinePtr QSSGCustomMaterialSystem::shadersForCustomMateri
//      al(QSSGRhiGraphicsPipelineState *ps, const QSSGRenderCustomMaterial
//      &material, QSSGSubsetRenderable &renderable, const
//      QSSGShaderDefaultMaterialKeyProperties
//      &defaultMaterialShaderKeyProperties, const QSSGShaderFeatures
//      &featureSet, const QSSGUserShaderAugmentation &shaderAugmentation)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN24QSSGCustomMaterialSystem24shadersForCustomMaterialEP28QSSGRhiGraphicsPipelineStateRK24QSSGRenderCustomMaterialR20QSSGSubsetRenderableRK38QSSGShaderDefaultMaterialKeyPropertiesRK18QSSGShaderFeaturesRK26QSSGUserShaderAugmentation(
    QSSGCustomMaterialSystem *self,
    QSSGRhiGraphicsPipelineState *ps,
    const QSSGRenderCustomMaterial *material,
    QSSGSubsetRenderable *renderable,
    const QSSGShaderDefaultMaterialKeyProperties *defaultMaterialShaderKeyProperties,
    const QSSGShaderFeatures *featureSet,
    const QSSGUserShaderAugmentation *shaderAugmentation) {
  return new QSSGRhiShaderPipelinePtr(
      self->shadersForCustomMaterial(
          ps,
          *material,
          *renderable,
          *defaultMaterialShaderKeyProperties,
          *featureSet,
          *shaderAugmentation));
}

//  void QSSGCustomMaterialSystem::updateUniformsForCustomMaterial(QSSGRhiSha
//      derPipeline &shaderPipeline, QSSGRhiContext *rhiCtx, const
//      QSSGLayerRenderData &inData, char *ubufData,
//      QSSGRhiGraphicsPipelineState *ps, const QSSGRenderCustomMaterial
//      &material, QSSGSubsetRenderable &renderable, const
//      QSSGRenderCameraList &cameras, const QVector2D *depthAdjust, const
//      QMatrix4x4 *alteredModelViewProjection)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem31updateUniformsForCustomMaterialER21QSSGRhiShaderPipelineP14QSSGRhiContextRK19QSSGLayerRenderDataPcP28QSSGRhiGraphicsPipelineStateRK24QSSGRenderCustomMaterialR20QSSGSubsetRenderableRK15QVarLengthArrayIP16QSSGRenderCameraLx2EEPK9QVector2DPK10QMatrix4x4(
    QSSGCustomMaterialSystem *self,
    QSSGRhiShaderPipeline *shaderPipeline,
    QSSGRhiContext *rhiCtx,
    const QSSGLayerRenderData *inData,
    char *ubufData,
    QSSGRhiGraphicsPipelineState *ps,
    const QSSGRenderCustomMaterial *material,
    QSSGSubsetRenderable *renderable,
    const QSSGRenderCameraList *cameras,
    const QVector2D *depthAdjust,
    const QMatrix4x4 *alteredModelViewProjection) {
  self->updateUniformsForCustomMaterial(
      *shaderPipeline,
      rhiCtx,
      *inData,
      ubufData,
      ps,
      *material,
      *renderable,
      *cameras,
      depthAdjust,
      alteredModelViewProjection);
}

//  void QSSGCustomMaterialSystem::rhiPrepareRenderable(QSSGRhiGraphicsPipeli
//      neState *ps, QSSGPassKey passKey, QSSGSubsetRenderable &renderable,
//      const QSSGShaderFeatures &featureSet, const QSSGRenderCustomMaterial
//      &material, const QSSGLayerRenderData &layerData,
//      QRhiRenderPassDescriptor *renderPassDescriptor, int samples, int
//      viewCount, bool screenMapPass, QSSGRenderCamera *camera,
//      QSSGRenderTextureCubeFace cubeFace, QMatrix4x4 *modelViewProjection,
//      QSSGReflectionMapEntry *entry, bool oit)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem20rhiPrepareRenderableEP28QSSGRhiGraphicsPipelineStatePvR20QSSGSubsetRenderableRK18QSSGShaderFeaturesRK24QSSGRenderCustomMaterialRK19QSSGLayerRenderDataP24QRhiRenderPassDescriptoriibP16QSSGRenderCamera25QSSGRenderTextureCubeFaceP10QMatrix4x4P22QSSGReflectionMapEntryb(
    QSSGCustomMaterialSystem *self,
    QSSGRhiGraphicsPipelineState *ps,
    QSSGPassKey passKey,
    QSSGSubsetRenderable *renderable,
    const QSSGShaderFeatures *featureSet,
    const QSSGRenderCustomMaterial *material,
    const QSSGLayerRenderData *layerData,
    QRhiRenderPassDescriptor *renderPassDescriptor,
    int samples,
    int viewCount,
    bool screenMapPass,
    QSSGRenderCamera *camera,
    QSSGRenderTextureCubeFace cubeFace,
    QMatrix4x4 *modelViewProjection,
    QSSGReflectionMapEntry *entry,
    bool oit) {
  self->rhiPrepareRenderable(
      ps,
      passKey,
      *renderable,
      *featureSet,
      *material,
      *layerData,
      renderPassDescriptor,
      samples,
      viewCount,
      screenMapPass,
      camera,
      cubeFace,
      modelViewProjection,
      entry,
      oit);
}

//  void QSSGCustomMaterialSystem::applyRhiShaderPropertyValues(char
//      *ubufData, const QSSGRenderCustomMaterial &inMaterial,
//      QSSGRhiShaderPipeline &shaderPipeline)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem28applyRhiShaderPropertyValuesEPcRK24QSSGRenderCustomMaterialR21QSSGRhiShaderPipeline(
    QSSGCustomMaterialSystem *self,
    char *ubufData,
    const QSSGRenderCustomMaterial *inMaterial,
    QSSGRhiShaderPipeline *shaderPipeline) {
  self->applyRhiShaderPropertyValues(ubufData, *inMaterial, *shaderPipeline);
}

//  void QSSGCustomMaterialSystem::rhiRenderRenderable(QSSGRhiContext
//      *rhiCtx, QSSGSubsetRenderable &renderable, bool *needsSetViewport,
//      QSSGRenderTextureCubeFace cubeFace, const
//      QSSGRhiGraphicsPipelineState &state, qsizetype userPassIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGCustomMaterialSystem19rhiRenderRenderableEP14QSSGRhiContextR20QSSGSubsetRenderablePb25QSSGRenderTextureCubeFaceRK28QSSGRhiGraphicsPipelineStatex(
    QSSGCustomMaterialSystem *self,
    QSSGRhiContext *rhiCtx,
    QSSGSubsetRenderable *renderable,
    bool *needsSetViewport,
    QSSGRenderTextureCubeFace cubeFace,
    const QSSGRhiGraphicsPipelineState *state,
    qsizetype userPassIndex) {
  self->rhiRenderRenderable(
      rhiCtx,
      *renderable,
      needsSetViewport,
      cubeFace,
      *state,
      userPassIndex);
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGCustomMaterialSystem gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGCustomMaterialSystem__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
