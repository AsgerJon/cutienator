//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgfrustum_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <optional>
#include <QtGui/QVector3D>
#include <QtCore/QVarLengthArray>
#include <QtCore/QList>

//  QSSGRendererPrivate::QSSGRendererPrivate()
extern "C" Q_DECL_EXPORT
QSSGRendererPrivate *ritual_ZN19QSSGRendererPrivateC1Ev() {
  return new QSSGRendererPrivate();
}

//  QSSGRhiShaderPipelinePtr
//      QSSGRendererPrivate::generateRhiShaderPipelineImpl(QSSGSubsetRenderab
//      le &renderable, QSSGShaderLibraryManager &shaderLibraryManager,
//      QSSGShaderCache &shaderCache, QSSGProgramGenerator
//      &shaderProgramGenerator, const QSSGShaderDefaultMaterialKeyProperties
//      &shaderKeyProperties, const QSSGShaderFeatures &featureSet, const
//      QSSGUserShaderAugmentation &shaderAugmentation, QByteArray
//      &shaderString)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN19QSSGRendererPrivate29generateRhiShaderPipelineImplER20QSSGSubsetRenderableR24QSSGShaderLibraryManagerR15QSSGShaderCacheR20QSSGProgramGeneratorRK38QSSGShaderDefaultMaterialKeyPropertiesRK18QSSGShaderFeaturesRK26QSSGUserShaderAugmentationR10QByteArray(
    QSSGSubsetRenderable *renderable,
    QSSGShaderLibraryManager *shaderLibraryManager,
    QSSGShaderCache *shaderCache,
    QSSGProgramGenerator *shaderProgramGenerator,
    const QSSGShaderDefaultMaterialKeyProperties *shaderKeyProperties,
    const QSSGShaderFeatures *featureSet,
    const QSSGUserShaderAugmentation *shaderAugmentation,
    QByteArray *shaderString) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGRendererPrivate::generateRhiShaderPipelineImpl(
          *renderable,
          *shaderLibraryManager,
          *shaderCache,
          *shaderProgramGenerator,
          *shaderKeyProperties,
          *featureSet,
          *shaderAugmentation,
          *shaderString));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGRendererPrivate::generateRhiShaderPipeline(QSSGRenderer
//      &renderer, QSSGSubsetRenderable &inRenderable, const
//      QSSGShaderFeatures &inFeatureSet, const QSSGUserShaderAugmentation
//      &shaderAugmentation)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN19QSSGRendererPrivate25generateRhiShaderPipelineER12QSSGRendererR20QSSGSubsetRenderableRK18QSSGShaderFeaturesRK26QSSGUserShaderAugmentation(
    QSSGRenderer *renderer,
    QSSGSubsetRenderable *inRenderable,
    const QSSGShaderFeatures *inFeatureSet,
    const QSSGUserShaderAugmentation *shaderAugmentation) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGRendererPrivate::generateRhiShaderPipeline(
          *renderer,
          *inRenderable,
          *inFeatureSet,
          *shaderAugmentation));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGRendererPrivate::getShaderPipelineForDefaultMaterial(QSSGRenderer
//      &renderer, QSSGSubsetRenderable &inRenderable, const
//      QSSGShaderFeatures &inFeatureSet, const QSSGUserShaderAugmentation
//      &shaderAugmentation)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN19QSSGRendererPrivate35getShaderPipelineForDefaultMaterialER12QSSGRendererR20QSSGSubsetRenderableRK18QSSGShaderFeaturesRK26QSSGUserShaderAugmentation(
    QSSGRenderer *renderer,
    QSSGSubsetRenderable *inRenderable,
    const QSSGShaderFeatures *inFeatureSet,
    const QSSGUserShaderAugmentation *shaderAugmentation) {
  return new QSSGRhiShaderPipelinePtr(
      QSSGRendererPrivate::getShaderPipelineForDefaultMaterial(
          *renderer,
          *inRenderable,
          *inFeatureSet,
          *shaderAugmentation));
}

//  void QSSGRendererPrivate::getLayerHitObjectList(const QSSGRenderLayer
//      &layer, QSSGBufferManager &bufferManager, const QSSGRenderRay &ray,
//      bool inPickEverything, PickResultList &outIntersectionResult)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivate21getLayerHitObjectListERK15QSSGRenderLayerR17QSSGBufferManagerRK13QSSGRenderRaybR15QVarLengthArrayI20QSSGRenderPickResultLx20EE(
    const QSSGRenderLayer *layer,
    QSSGBufferManager *bufferManager,
    const QSSGRenderRay *ray,
    bool inPickEverything,
    QSSGRendererPrivate::PickResultList *outIntersectionResult) {
  QSSGRendererPrivate::getLayerHitObjectList(
      *layer,
      *bufferManager,
      *ray,
      inPickEverything,
      *outIntersectionResult);
}

//  void QSSGRendererPrivate::intersectRayWithSubsetRenderable(const
//      QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
//      QSSGRenderRay &inRay, const QSSGRenderNode &node, PickResultList
//      &outIntersectionResultList)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivate32intersectRayWithSubsetRenderableERK15QSSGRenderLayerR17QSSGBufferManagerRK13QSSGRenderRayRK14QSSGRenderNodeR15QVarLengthArrayI20QSSGRenderPickResultLx20EE(
    const QSSGRenderLayer *layer,
    QSSGBufferManager *bufferManager,
    const QSSGRenderRay *inRay,
    const QSSGRenderNode *node,
    QSSGRendererPrivate::PickResultList *outIntersectionResultList) {
  QSSGRendererPrivate::intersectRayWithSubsetRenderable(
      *layer,
      *bufferManager,
      *inRay,
      *node,
      *outIntersectionResultList);
}

//  void QSSGRendererPrivate::intersectRayWithItem2D(const QSSGRenderLayer
//      &layer, const QSSGRenderRay &inRay, const QSSGRenderItem2D &item2D,
//      PickResultList &outIntersectionResultList)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivate22intersectRayWithItem2DERK15QSSGRenderLayerRK13QSSGRenderRayRK16QSSGRenderItem2DR15QVarLengthArrayI20QSSGRenderPickResultLx20EE(
    const QSSGRenderLayer *layer,
    const QSSGRenderRay *inRay,
    const QSSGRenderItem2D *item2D,
    QSSGRendererPrivate::PickResultList *outIntersectionResultList) {
  QSSGRendererPrivate::intersectRayWithItem2D(
      *layer,
      *inRay,
      *item2D,
      *outIntersectionResultList);
}

//  std::optional<QSSGRenderPickResult>
//      QSSGRendererPrivate::closestPointOnSubsetRenderable(const
//      QSSGRenderLayer &layer, QSSGBufferManager &bufferManager, const
//      QVector3D &center, float radiusSquared, const QSSGRenderNode &node)
extern "C" Q_DECL_EXPORT
std::optional<QSSGRenderPickResult> *ritual_ZN19QSSGRendererPrivate30closestPointOnSubsetRenderableERK15QSSGRenderLayerR17QSSGBufferManagerRK9QVector3DfRK14QSSGRenderNode(
    const QSSGRenderLayer *layer,
    QSSGBufferManager *bufferManager,
    const QVector3D *center,
    float radiusSquared,
    const QSSGRenderNode *node) {
  return new std::optional<QSSGRenderPickResult>(
      QSSGRendererPrivate::closestPointOnSubsetRenderable(
          *layer,
          *bufferManager,
          *center,
          radiusSquared,
          *node));
}

//  PickResultList QSSGRendererPrivate::syncPickAll(const
//      QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
//      QSSGRenderRay &ray)
extern "C" Q_DECL_EXPORT
QSSGRendererPrivate::PickResultList *ritual_ZN19QSSGRendererPrivate11syncPickAllERK26QSSGRenderContextInterfaceRK15QSSGRenderLayerRK13QSSGRenderRay(
    const QSSGRenderContextInterface *ctx,
    const QSSGRenderLayer *layer,
    const QSSGRenderRay *ray) {
  return new QSSGRendererPrivate::PickResultList(
      QSSGRendererPrivate::syncPickAll(
          *ctx,
          *layer,
          *ray));
}

//  PickResultList QSSGRendererPrivate::syncPick(const
//      QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
//      QSSGRenderRay &ray, QSSGRenderNode *target)
extern "C" Q_DECL_EXPORT
QSSGRendererPrivate::PickResultList *ritual_ZN19QSSGRendererPrivate8syncPickERK26QSSGRenderContextInterfaceRK15QSSGRenderLayerRK13QSSGRenderRayP14QSSGRenderNode(
    const QSSGRenderContextInterface *ctx,
    const QSSGRenderLayer *layer,
    const QSSGRenderRay *ray,
    QSSGRenderNode *target) {
  return new QSSGRendererPrivate::PickResultList(
      QSSGRendererPrivate::syncPick(
          *ctx,
          *layer,
          *ray,
          target));
}

//  PickResultList QSSGRendererPrivate::syncPickSubset(const QSSGRenderLayer
//      &layer, QSSGBufferManager &bufferManager, const QSSGRenderRay &ray,
//      QVarLengthArray<QSSGRenderNode *> subset)
extern "C" Q_DECL_EXPORT
QSSGRendererPrivate::PickResultList *ritual_ZN19QSSGRendererPrivate14syncPickSubsetERK15QSSGRenderLayerR17QSSGBufferManagerRK13QSSGRenderRay15QVarLengthArrayIP14QSSGRenderNodeLx256EE(
    const QSSGRenderLayer *layer,
    QSSGBufferManager *bufferManager,
    const QSSGRenderRay *ray,
    const QVarLengthArray<QSSGRenderNode *> *subset) {
  return new QSSGRendererPrivate::PickResultList(
      QSSGRendererPrivate::syncPickSubset(
          *layer,
          *bufferManager,
          *ray,
          *subset));
}

//  std::optional<QSSGRenderPickResult>
//      QSSGRendererPrivate::syncPickClosestPoint(const
//      QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
//      QVector3D &center, const float radiusSquared, QSSGRenderNode *target)
extern "C" Q_DECL_EXPORT
std::optional<QSSGRenderPickResult> *ritual_ZN19QSSGRendererPrivate20syncPickClosestPointERK26QSSGRenderContextInterfaceRK15QSSGRenderLayerRK9QVector3DfP14QSSGRenderNode(
    const QSSGRenderContextInterface *ctx,
    const QSSGRenderLayer *layer,
    const QVector3D *center,
    float radiusSquared,
    QSSGRenderNode *target) {
  return new std::optional<QSSGRenderPickResult>(
      QSSGRendererPrivate::syncPickClosestPoint(
          *ctx,
          *layer,
          *center,
          radiusSquared,
          target));
}

//  QList<const QSSGRenderNode *>
//      QSSGRendererPrivate::syncPickInFrustum(const
//      QSSGRenderContextInterface &ctx, const QSSGRenderLayer &layer, const
//      QSSGFrustum &frustum)
extern "C" Q_DECL_EXPORT
QList<const QSSGRenderNode *> *ritual_ZN19QSSGRendererPrivate17syncPickInFrustumERK26QSSGRenderContextInterfaceRK15QSSGRenderLayerRK11QSSGFrustum(
    const QSSGRenderContextInterface *ctx,
    const QSSGRenderLayer *layer,
    const QSSGFrustum *frustum) {
  return new QList<const QSSGRenderNode *>(
      QSSGRendererPrivate::syncPickInFrustum(
          *ctx,
          *layer,
          *frustum));
}

//  bool QSSGRendererPrivate::isGlobalPickingEnabled(const QSSGRenderer
//      &renderer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSSGRendererPrivate22isGlobalPickingEnabledERK12QSSGRenderer(
    const QSSGRenderer *renderer) {
  return QSSGRendererPrivate::isGlobalPickingEnabled(*renderer);
}

//  void QSSGRendererPrivate::setGlobalPickingEnabled(QSSGRenderer &renderer,
//      bool isEnabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivate23setGlobalPickingEnabledER12QSSGRendererb(
    QSSGRenderer *renderer,
    bool isEnabled) {
  QSSGRendererPrivate::setGlobalPickingEnabled(*renderer, isEnabled);
}

//  void QSSGRendererPrivate::setRenderContextInterface(QSSGRenderer
//      &renderer, QSSGRenderContextInterface *ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivate25setRenderContextInterfaceER12QSSGRendererP26QSSGRenderContextInterface(
    QSSGRenderer *renderer,
    QSSGRenderContextInterface *ctx) {
  QSSGRendererPrivate::setRenderContextInterface(*renderer, ctx);
}

//  void QSSGRendererPrivate::setSgRenderContext(QSSGRenderer &renderer,
//      QSGRenderContext *sgRenderCtx)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivate18setSgRenderContextER12QSSGRendererP16QSGRenderContext(
    QSSGRenderer *renderer,
    QSGRenderContext *sgRenderCtx) {
  QSSGRendererPrivate::setSgRenderContext(*renderer, sgRenderCtx);
}

//  QSSGLayerRenderData *QSSGRendererPrivate::getCurrentRenderData(const
//      QSSGRenderer &renderer)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZN19QSSGRendererPrivate20getCurrentRenderDataERK12QSSGRenderer(
    const QSSGRenderer *renderer) {
  return QSSGRendererPrivate::getCurrentRenderData(*renderer);
}

//  QSGRenderContext *QSSGRendererPrivate::getSgRenderContext(const
//      QSSGRenderer &renderer)
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZN19QSSGRendererPrivate18getSgRenderContextERK12QSSGRenderer(
    const QSSGRenderer *renderer) {
  return QSSGRendererPrivate::getSgRenderContext(*renderer);
}

//  QSSGRendererPrivate::~QSSGRendererPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRendererPrivateD1Ev(QSSGRendererPrivate *self) {
  delete self;
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGRendererPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRendererPrivate__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}

//  a std::optional<QSSGRenderPickResult> a ritual of QSSGRendererPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRendererPrivate__std_optional_QSSGRenderPickResult(
    std::optional<QSSGRenderPickResult> *self) {
  delete self;
}

//  a QSSGRendererPrivate::PickResultList a ritual of QSSGRendererPrivate
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRendererPrivate__QSSGRendererPrivate_PickResultList(
    QSSGRendererPrivate::PickResultList *self) {
  delete self;
}

//  a QList<const QSSGRenderNode *> a ritual of QSSGRendererPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGRendererPrivate__QList_const_QSSGRenderNode(
    QList<const QSSGRenderNode *> *self) {
  delete self;
}
