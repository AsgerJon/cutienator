//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
//  Qt 6.12.0. Edited by hand on 2026-11-25: added by hand, rituals for
//  functions the generator leaves out: 1. Kept as it is when the generator
//  runs again.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderclippingfrustum_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderitem2d_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticleshaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <QtGui/QMatrix4x4>
#include <QtGui/QMatrix3x3>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#if QT_CONFIG(thread)
#include <QtCore/qthreadpool.h>
#endif
#include <QtCore/qtenvironmentvariables.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskeleton_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderjoint_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermorphtarget_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h>
#include <QtQuick3DRuntimeRender/private/qssgruntimerenderlogging_p.h>
#include <QtQuick3DRuntimeRender/private/qssglightmapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtCore/qspan.h>
#include <array>
#include <QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 451, as _ZNK19QSSGRenderModelData15getNormalMatrixE23QSSGRenderStorageHandleIL10HandleType1EE14QGenericMatrixILi3ELi3EfE
inline QMatrix3x3 QSSGRenderModelData::getNormalMatrix(QSSGRenderNodeHandle h, QMatrix3x3 defaultValue) const
{
    const bool hasId = h.hasId();
    const bool validVersion = hasId && (h.version() == m_gnd->version());
    const auto index = h.index();
    if (!validVersion || !(m_gnd->normalMatrices.size() > index))
        return defaultValue;

    return m_gnd->normalMatrices[index];
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 462, as _ZNK19QSSGRenderModelData15getNormalMatrixERK15QSSGRenderModel
inline QMatrix3x3 QSSGRenderModelData::getNormalMatrix(const QSSGRenderModel &model) const
{
    return getNormalMatrix(model.h, QMatrix3x3{ Qt::Uninitialized });
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 672, as _ZNK20QSSGRenderItem2DData17getItem2DRendererERK16QSSGRenderItem2D
inline QSSGRenderItem2DData::Item2DRenderer QSSGRenderItem2DData::getItem2DRenderer(const QSSGRenderItem2D &item) const
{
    const auto foundIt = item2DRenderers.find(&item);
    return (foundIt != item2DRenderers.cend()) ? foundIt->second : Item2DRenderer{};
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglayerrenderdata.cpp, line 486, as _ZN19QSSGLayerRenderData17perFrameAllocatorER26QSSGRenderContextInterface
inline const std::unique_ptr<QSSGPerFrameAllocator> &QSSGLayerRenderData::perFrameAllocator(QSSGRenderContextInterface &ctx)
{
    return ctx.perFrameAllocator();
}
//  -----------------------------------------------------------------------

//  QSSGLayerRenderData::QSSGLayerRenderData(QSSGRenderLayer &inLayer,
//      QSSGRenderer &inRenderer)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZN19QSSGLayerRenderDataC1ER15QSSGRenderLayerR12QSSGRenderer(
    QSSGRenderLayer *inLayer,
    QSSGRenderer *inRenderer) {
  return new QSSGLayerRenderData(*inLayer, *inRenderer);
}

//  QSSGLayerRenderData::~QSSGLayerRenderData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderDataD1Ev(QSSGLayerRenderData *self) {
  delete self;
}

//  void QSSGLayerRenderData::setVertexInputPresence(const
//      QSSGRenderableObjectFlags &renderableFlags,
//      QSSGShaderDefaultMaterialKey &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData22setVertexInputPresenceERK25QSSGRenderableObjectFlagsR25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EE(
    QSSGLayerRenderData *self,
    const QSSGRenderableObjectFlags *renderableFlags,
    QSSGShaderDefaultMaterialKey *key) {
  self->setVertexInputPresence(*renderableFlags, *key);
}

//  bool
//      QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterfac
//      e &ctx, const RenderableNodeEntries &renderableModels,
//      QSSGLayerRenderPreparationResultFlags &ioFlags, const
//      QSSGRenderCameraList &allCameras, const QSSGRenderCameraDataList
//      &allCameraData, TModelContextPtrList &modelContexts,
//      QSSGRenderableObjectList &opaqueObjects, QSSGRenderableObjectList
//      &transparentObjects, QSSGRenderableObjectList &screenTextureObjects,
//      float lodThreshold)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSSGLayerRenderData22prepareModelsForRenderER26QSSGRenderContextInterfaceRK5QListI23QSSGRenderableNodeEntryER37QSSGLayerRenderPreparationResultFlagsRK15QVarLengthArrayIP16QSSGRenderCameraLx2EERKS9_I20QSSGRenderCameraDataLx2EERS2_IP16QSSGModelContextERS2_I26QSSGRenderableObjectHandleESP_SP_f(
    QSSGLayerRenderData *self,
    QSSGRenderContextInterface *ctx,
    const QList<QSSGRenderableNodeEntry> *renderableModels,
    QSSGLayerRenderPreparationResultFlags *ioFlags,
    const QSSGRenderCameraList *allCameras,
    const QSSGRenderCameraDataList *allCameraData,
    QSSGLayerRenderData::TModelContextPtrList *modelContexts,
    QSSGRenderableObjectList *opaqueObjects,
    QSSGRenderableObjectList *transparentObjects,
    QSSGRenderableObjectList *screenTextureObjects,
    float lodThreshold) {
  return self->prepareModelsForRender(
      *ctx,
      *renderableModels,
      *ioFlags,
      *allCameras,
      *allCameraData,
      *modelContexts,
      *opaqueObjects,
      *transparentObjects,
      *screenTextureObjects,
      lodThreshold);
}

//  bool QSSGLayerRenderData::prepareParticlesForRender(const
//      RenderableNodeEntries &renderableParticles, const
//      QSSGRenderCameraData &cameraData,
//      QSSGLayerRenderPreparationResultFlags &ioFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSSGLayerRenderData25prepareParticlesForRenderERK5QListI23QSSGRenderableNodeEntryERK20QSSGRenderCameraDataR37QSSGLayerRenderPreparationResultFlags(
    QSSGLayerRenderData *self,
    const QList<QSSGRenderableNodeEntry> *renderableParticles,
    const QSSGRenderCameraData *cameraData,
    QSSGLayerRenderPreparationResultFlags *ioFlags) {
  return self->prepareParticlesForRender(
      *renderableParticles,
      *cameraData,
      *ioFlags);
}

//  void QSSGLayerRenderData::prepareResourceLoaders()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData22prepareResourceLoadersEv(
    QSSGLayerRenderData *self) {
  self->prepareResourceLoaders();
}

//  void QSSGLayerRenderData::prepareForRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData16prepareForRenderEv(
    QSSGLayerRenderData *self) {
  self->prepareForRender();
}

//  void QSSGLayerRenderData::prepareReflectionProbesForRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData32prepareReflectionProbesForRenderEv(
    QSSGLayerRenderData *self) {
  self->prepareReflectionProbesForRender();
}

//  qsizetype QSSGLayerRenderData::frustumCullingInline(const
//      QSSGClippingFrustum &clipFrustum, QSSGRenderableObjectList
//      &renderables)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QSSGLayerRenderData20frustumCullingInlineERK19QSSGClippingFrustumR5QListI26QSSGRenderableObjectHandleE(
    const QSSGClippingFrustum *clipFrustum,
    QSSGRenderableObjectList *renderables) {
  return QSSGLayerRenderData::frustumCullingInline(
      *clipFrustum,
      *renderables);
}

//  qsizetype QSSGLayerRenderData::filterLayerMaskInline(quint32 layerMask,
//      QSSGRenderableObjectList &renderables)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QSSGLayerRenderData21filterLayerMaskInlineEjR5QListI26QSSGRenderableObjectHandleE(
    quint32 layerMask,
    QSSGRenderableObjectList *renderables) {
  return QSSGLayerRenderData::filterLayerMaskInline(layerMask, *renderables);
}

//  const QSSGRenderableObjectList
//      &QSSGLayerRenderData::getSortedOpaqueRenderableObjects(const
//      QSSGRenderCamera &camera, size_t index, quint32 layerMask)
extern "C" Q_DECL_EXPORT
QList<QSSGRenderableObjectHandle> *ritual_ZN19QSSGLayerRenderData32getSortedOpaqueRenderableObjectsERK16QSSGRenderCameramj(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    size_t index,
    quint32 layerMask) {
  return new QList<QSSGRenderableObjectHandle>(
      self->getSortedOpaqueRenderableObjects(
          *camera,
          index,
          layerMask));
}

//  const QSSGRenderableObjectList
//      &QSSGLayerRenderData::getSortedTransparentRenderableObjects(const
//      QSSGRenderCamera &camera, size_t index, quint32 layerMask)
extern "C" Q_DECL_EXPORT
QList<QSSGRenderableObjectHandle> *ritual_ZN19QSSGLayerRenderData37getSortedTransparentRenderableObjectsERK16QSSGRenderCameramj(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    size_t index,
    quint32 layerMask) {
  return new QList<QSSGRenderableObjectHandle>(
      self->getSortedTransparentRenderableObjects(
          *camera,
          index,
          layerMask));
}

//  const QSSGRenderableObjectList
//      &QSSGLayerRenderData::getSortedScreenTextureRenderableObjects(const
//      QSSGRenderCamera &camera, size_t index)
extern "C" Q_DECL_EXPORT
QList<QSSGRenderableObjectHandle> *ritual_ZN19QSSGLayerRenderData39getSortedScreenTextureRenderableObjectsERK16QSSGRenderCameram(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    size_t index) {
  return new QList<QSSGRenderableObjectHandle>(
      self->getSortedScreenTextureRenderableObjects(
          *camera,
          index));
}

//  const QVector<QSSGBakedLightingModel>
//      &QSSGLayerRenderData::getSortedBakedLightingModels()
extern "C" Q_DECL_EXPORT
const QVector<QSSGBakedLightingModel> *ritual_ZN19QSSGLayerRenderData28getSortedBakedLightingModelsEv(
    QSSGLayerRenderData *self) {
  return &(self->getSortedBakedLightingModels());
}

//  const RenderableItem2DEntries
//      &QSSGLayerRenderData::getRenderableItem2Ds()
extern "C" Q_DECL_EXPORT
QList<QSSGRenderItem2D *> *ritual_ZN19QSSGLayerRenderData20getRenderableItem2DsEv(
    QSSGLayerRenderData *self) {
  return new QList<QSSGRenderItem2D *>(self->getRenderableItem2Ds());
}

//  const QSSGRenderableObjectList
//      &QSSGLayerRenderData::getSortedRenderedDepthWriteObjects(const
//      QSSGRenderCamera &camera, size_t index)
extern "C" Q_DECL_EXPORT
QList<QSSGRenderableObjectHandle> *ritual_ZN19QSSGLayerRenderData34getSortedRenderedDepthWriteObjectsERK16QSSGRenderCameram(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    size_t index) {
  return new QList<QSSGRenderableObjectHandle>(
      self->getSortedRenderedDepthWriteObjects(
          *camera,
          index));
}

//  const QSSGRenderableObjectList
//      &QSSGLayerRenderData::getSortedrenderedOpaqueDepthPrepassObjects(cons
//      t QSSGRenderCamera &camera, size_t index)
extern "C" Q_DECL_EXPORT
QList<QSSGRenderableObjectHandle> *ritual_ZN19QSSGLayerRenderData42getSortedrenderedOpaqueDepthPrepassObjectsERK16QSSGRenderCameram(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    size_t index) {
  return new QList<QSSGRenderableObjectHandle>(
      self->getSortedrenderedOpaqueDepthPrepassObjects(
          *camera,
          index));
}

//  void QSSGLayerRenderData::getShadowCastingObjects(const QSSGRenderCamera
//      &camera, QSSGRenderableObjectList &outObjects, QSSGBounds3
//      &outBoundsCasting, QSSGBounds3 &outBoundsReceiving)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData23getShadowCastingObjectsERK16QSSGRenderCameraR5QListI26QSSGRenderableObjectHandleER11QSSGBounds3S8_(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    QSSGRenderableObjectList *outObjects,
    QSSGBounds3 *outBoundsCasting,
    QSSGBounds3 *outBoundsReceiving) {
  self->getShadowCastingObjects(
      *camera,
      *outObjects,
      *outBoundsCasting,
      *outBoundsReceiving);
}

//  void QSSGLayerRenderData::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData13resetForFrameEv(
    QSSGLayerRenderData *self) {
  self->resetForFrame();
}

//  QSSGFrameData &QSSGLayerRenderData::getFrameData()
extern "C" Q_DECL_EXPORT
QSSGFrameData *ritual_ZN19QSSGLayerRenderData12getFrameDataEv(
    QSSGLayerRenderData *self) {
  return &(self->getFrameData());
}

//  QSSGShaderFeatures QSSGLayerRenderData::getShaderFeatures() const
extern "C" Q_DECL_EXPORT
QSSGShaderFeatures *ritual_ZNK19QSSGLayerRenderData17getShaderFeaturesEv(
    const QSSGLayerRenderData *self) {
  return new QSSGShaderFeatures(self->getShaderFeatures());
}

//  QSSGRhiGraphicsPipelineState QSSGLayerRenderData::getPipelineState()
//      const
extern "C" Q_DECL_EXPORT
QSSGRhiGraphicsPipelineState *ritual_ZNK19QSSGLayerRenderData16getPipelineStateEv(
    const QSSGLayerRenderData *self) {
  return new QSSGRhiGraphicsPipelineState(self->getPipelineState());
}

//  void
//      QSSGLayerRenderData::initializeLightmapBaking(QSSGLightmapBaker::Cont
//      ext &ctx)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData24initializeLightmapBakingERN17QSSGLightmapBaker7ContextE(
    QSSGLayerRenderData *self,
    QSSGLightmapBaker::Context *ctx) {
  self->initializeLightmapBaking(*ctx);
}

//  void QSSGLayerRenderData::maybeProcessLightmapBaking()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData26maybeProcessLightmapBakingEv(
    QSSGLayerRenderData *self) {
  self->maybeProcessLightmapBaking();
}

//  QSSGRenderGraphObject *QSSGLayerRenderData::getCamera(QSSGCameraId id)
//      const
extern "C" Q_DECL_EXPORT
QSSGRenderGraphObject *ritual_ZNK19QSSGLayerRenderData9getCameraE12QSSGCameraId(
    const QSSGLayerRenderData *self,
    QSSGCameraId id) {
  return self->getCamera(id);
}

//  QSSGRenderCamera *QSSGLayerRenderData::activeCamera() const
extern "C" Q_DECL_EXPORT
QSSGRenderCamera *ritual_ZNK19QSSGLayerRenderData12activeCameraEv(
    const QSSGLayerRenderData *self) {
  return self->activeCamera();
}

//  QSSGRenderCameraData QSSGLayerRenderData::getCameraRenderData(const
//      QSSGRenderCamera *camera)
extern "C" Q_DECL_EXPORT
QSSGRenderCameraData *ritual_ZN19QSSGLayerRenderData19getCameraRenderDataEPK16QSSGRenderCamera(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera) {
  return new QSSGRenderCameraData(self->getCameraRenderData(camera));
}

//  QSSGRenderCameraData QSSGLayerRenderData::getCameraRenderData(const
//      QSSGRenderCamera *camera) const
extern "C" Q_DECL_EXPORT
QSSGRenderCameraData *ritual_ZNK19QSSGLayerRenderData19getCameraRenderDataEPK16QSSGRenderCamera(
    const QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera) {
  return new QSSGRenderCameraData(self->getCameraRenderData(camera));
}

//  void QSSGLayerRenderData::setLightmapTexture(const QSSGModelContext
//      &modelContext, QRhiTexture *lightmapTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData18setLightmapTextureERK16QSSGModelContextP11QRhiTexture(
    QSSGLayerRenderData *self,
    const QSSGModelContext *modelContext,
    QRhiTexture *lightmapTexture) {
  self->setLightmapTexture(*modelContext, lightmapTexture);
}

//  QRhiTexture *QSSGLayerRenderData::getLightmapTexture(const
//      QSSGModelContext &modelContext) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QSSGLayerRenderData18getLightmapTextureERK16QSSGModelContext(
    const QSSGLayerRenderData *self,
    const QSSGModelContext *modelContext) {
  return self->getLightmapTexture(*modelContext);
}

//  void QSSGLayerRenderData::setBonemapTexture(const QSSGModelContext
//      &modelContext, QRhiTexture *bonemapTexture)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData17setBonemapTextureERK16QSSGModelContextP11QRhiTexture(
    QSSGLayerRenderData *self,
    const QSSGModelContext *modelContext,
    QRhiTexture *bonemapTexture) {
  self->setBonemapTexture(*modelContext, bonemapTexture);
}

//  QRhiTexture *QSSGLayerRenderData::getBonemapTexture(const
//      QSSGModelContext &modelContext) const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QSSGLayerRenderData17getBonemapTextureERK16QSSGModelContext(
    const QSSGLayerRenderData *self,
    const QSSGModelContext *modelContext) {
  return self->getBonemapTexture(*modelContext);
}

//  QSSGRenderContextInterface *QSSGLayerRenderData::contextInterface() const
extern "C" Q_DECL_EXPORT
QSSGRenderContextInterface *ritual_ZNK19QSSGLayerRenderData16contextInterfaceEv(
    const QSSGLayerRenderData *self) {
  return self->contextInterface();
}

//  bool QSSGLayerRenderData::isZPrePassActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QSSGLayerRenderData16isZPrePassActiveEv(
    const QSSGLayerRenderData *self) {
  return self->isZPrePassActive();
}

//  void QSSGLayerRenderData::setZPrePassPrepResult(bool res)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData21setZPrePassPrepResultEb(
    QSSGLayerRenderData *self,
    bool res) {
  self->setZPrePassPrepResult(res);
}

//  const QSSGShaderDefaultMaterialKeyProperties
//      &QSSGLayerRenderData::getDefaultMaterialPropertyTable() const
extern "C" Q_DECL_EXPORT
QSSGShaderDefaultMaterialKeyProperties *ritual_ZNK19QSSGLayerRenderData31getDefaultMaterialPropertyTableEv(
    const QSSGLayerRenderData *self) {
  return new QSSGShaderDefaultMaterialKeyProperties(
      self->getDefaultMaterialPropertyTable());
}

//  const QSSGShaderParticleMaterialKeyProperties
//      &QSSGLayerRenderData::getParticleMaterialPropertyTable() const
extern "C" Q_DECL_EXPORT
QSSGShaderParticleMaterialKeyProperties *ritual_ZNK19QSSGLayerRenderData32getParticleMaterialPropertyTableEv(
    const QSSGLayerRenderData *self) {
  return new QSSGShaderParticleMaterialKeyProperties(
      self->getParticleMaterialPropertyTable());
}

//  GlobalRenderProperties QSSGLayerRenderData::globalRenderProperties(const
//      QSSGRenderContextInterface &ctx)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData::GlobalRenderProperties *ritual_ZN19QSSGLayerRenderData22globalRenderPropertiesERK26QSSGRenderContextInterface(
    const QSSGRenderContextInterface *ctx) {
  return new QSSGLayerRenderData::GlobalRenderProperties(
      QSSGLayerRenderData::globalRenderProperties(
          *ctx));
}

//  const QSSGRenderShadowMapPtr
//      &QSSGLayerRenderData::requestShadowMapManager()
extern "C" Q_DECL_EXPORT
const QSSGRenderShadowMapPtr *ritual_ZN19QSSGLayerRenderData23requestShadowMapManagerEv(
    QSSGLayerRenderData *self) {
  return &(self->requestShadowMapManager());
}

//  const QSSGRenderReflectionMapPtr
//      &QSSGLayerRenderData::requestReflectionMapManager()
extern "C" Q_DECL_EXPORT
const QSSGRenderReflectionMapPtr *ritual_ZN19QSSGLayerRenderData27requestReflectionMapManagerEv(
    QSSGLayerRenderData *self) {
  return &(self->requestReflectionMapManager());
}

//  const QSSGRenderSkyMaterialManagerPtr
//      &QSSGLayerRenderData::requestSkyMaterialManager()
extern "C" Q_DECL_EXPORT
const QSSGRenderSkyMaterialManagerPtr *ritual_ZN19QSSGLayerRenderData25requestSkyMaterialManagerEv(
    QSSGLayerRenderData *self) {
  return &(self->requestSkyMaterialManager());
}

//  const QSSGUserRenderPassManagerPtr
//      &QSSGLayerRenderData::requestUserRenderPassManager()
extern "C" Q_DECL_EXPORT
const QSSGUserRenderPassManagerPtr *ritual_ZN19QSSGLayerRenderData28requestUserRenderPassManagerEv(
    QSSGLayerRenderData *self) {
  return &(self->requestUserRenderPassManager());
}

//  const QSSGRenderMotionVectorMapPtr
//      &QSSGLayerRenderData::requestMotionVectorMapManager()
extern "C" Q_DECL_EXPORT
const QSSGRenderMotionVectorMapPtr *ritual_ZN19QSSGLayerRenderData29requestMotionVectorMapManagerEv(
    QSSGLayerRenderData *self) {
  return &(self->requestMotionVectorMapManager());
}

//  const QSSGRenderShadowMapPtr &QSSGLayerRenderData::getShadowMapManager()
//      const
extern "C" Q_DECL_EXPORT
const QSSGRenderShadowMapPtr *ritual_ZNK19QSSGLayerRenderData19getShadowMapManagerEv(
    const QSSGLayerRenderData *self) {
  return &(self->getShadowMapManager());
}

//  const QSSGRenderReflectionMapPtr
//      &QSSGLayerRenderData::getReflectionMapManager() const
extern "C" Q_DECL_EXPORT
const QSSGRenderReflectionMapPtr *ritual_ZNK19QSSGLayerRenderData23getReflectionMapManagerEv(
    const QSSGLayerRenderData *self) {
  return &(self->getReflectionMapManager());
}

//  const QSSGRenderSkyMaterialManagerPtr
//      &QSSGLayerRenderData::getSkyMaterialManager() const
extern "C" Q_DECL_EXPORT
const QSSGRenderSkyMaterialManagerPtr *ritual_ZNK19QSSGLayerRenderData21getSkyMaterialManagerEv(
    const QSSGLayerRenderData *self) {
  return &(self->getSkyMaterialManager());
}

//  const QSSGUserRenderPassManagerPtr
//      &QSSGLayerRenderData::getUserRenderPassManager() const
extern "C" Q_DECL_EXPORT
const QSSGUserRenderPassManagerPtr *ritual_ZNK19QSSGLayerRenderData24getUserRenderPassManagerEv(
    const QSSGLayerRenderData *self) {
  return &(self->getUserRenderPassManager());
}

//  const QSSGRenderMotionVectorMapPtr
//      &QSSGLayerRenderData::getMotionvectorMapManager() const
extern "C" Q_DECL_EXPORT
const QSSGRenderMotionVectorMapPtr *ritual_ZNK19QSSGLayerRenderData25getMotionvectorMapManagerEv(
    const QSSGLayerRenderData *self) {
  return &(self->getMotionvectorMapManager());
}

//  QSSGOITRenderContext &QSSGLayerRenderData::getOitRenderContext()
extern "C" Q_DECL_EXPORT
QSSGOITRenderContext *ritual_ZN19QSSGLayerRenderData19getOitRenderContextEv(
    QSSGLayerRenderData *self) {
  return &(self->getOitRenderContext());
}

//  const QSSGOITRenderContext
//      &QSSGLayerRenderData::getOitRenderContextConst() const
extern "C" Q_DECL_EXPORT
QSSGOITRenderContext *ritual_ZNK19QSSGLayerRenderData24getOitRenderContextConstEv(
    const QSSGLayerRenderData *self) {
  return new QSSGOITRenderContext(self->getOitRenderContextConst());
}

//  bool QSSGLayerRenderData::prepareInstancing(QSSGRhiContext *rhiCtx,
//      QSSGSubsetRenderable *renderable, const QVector3D &cameraDirection,
//      const QVector3D &cameraPosition, float minThreshold, float
//      maxThreshold)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QSSGLayerRenderData17prepareInstancingEP14QSSGRhiContextP20QSSGSubsetRenderableRK9QVector3DS6_ff(
    QSSGRhiContext *rhiCtx,
    QSSGSubsetRenderable *renderable,
    const QVector3D *cameraDirection,
    const QVector3D *cameraPosition,
    float minThreshold,
    float maxThreshold) {
  return QSSGLayerRenderData::prepareInstancing(
      rhiCtx,
      renderable,
      *cameraDirection,
      *cameraPosition,
      minThreshold,
      maxThreshold);
}

//  QSSGRhiRenderableTexture
//      *QSSGLayerRenderData::getRenderResult(QSSGRenderResult::Key id)
extern "C" Q_DECL_EXPORT
QSSGRhiRenderableTexture *ritual_ZN19QSSGLayerRenderData15getRenderResultEN16QSSGRenderResult3KeyE(
    QSSGLayerRenderData *self,
    QSSGRenderResult::Key id) {
  return self->getRenderResult(id);
}

//  const QSSGRhiRenderableTexture
//      *QSSGLayerRenderData::getRenderResult(QSSGRenderResult::Key id) const
extern "C" Q_DECL_EXPORT
const QSSGRhiRenderableTexture *ritual_ZNK19QSSGLayerRenderData15getRenderResultEN16QSSGRenderResult3KeyE(
    const QSSGLayerRenderData *self,
    QSSGRenderResult::Key id) {
  return self->getRenderResult(id);
}

//  void QSSGLayerRenderData::resolveLayerIblTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData22resolveLayerIblTextureEv(
    QSSGLayerRenderData *self) {
  self->resolveLayerIblTexture();
}

//  const std::unique_ptr<QSSGPerFrameAllocator>
//      &QSSGLayerRenderData::perFrameAllocator(QSSGRenderContextInterface
//      &ctx)
extern "C" Q_DECL_EXPORT
const std::unique_ptr<QSSGPerFrameAllocator> *ritual_ZN19QSSGLayerRenderData17perFrameAllocatorER26QSSGRenderContextInterface(
    QSSGRenderContextInterface *ctx) {
  return &(QSSGLayerRenderData::perFrameAllocator(*ctx));
}

//  QSSGLayerRenderData *QSSGLayerRenderData::getCurrent(const QSSGRenderer
//      &renderer)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZN19QSSGLayerRenderData10getCurrentERK12QSSGRenderer(
    const QSSGRenderer *renderer) {
  return QSSGLayerRenderData::getCurrent(*renderer);
}

//  void QSSGLayerRenderData::saveRenderState(const QSSGRenderer &renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData15saveRenderStateERK12QSSGRenderer(
    QSSGLayerRenderData *self,
    const QSSGRenderer *renderer) {
  self->saveRenderState(*renderer);
}

//  void QSSGLayerRenderData::restoreRenderState(QSSGRenderer &renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData18restoreRenderStateER12QSSGRenderer(
    QSSGLayerRenderData *self,
    QSSGRenderer *renderer) {
  self->restoreRenderState(*renderer);
}

//  void QSSGLayerRenderData::setTonemapFeatures(QSSGShaderFeatures
//      &features, QSSGRenderLayer::TonemapMode tonemapMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData18setTonemapFeaturesER18QSSGShaderFeaturesN15QSSGRenderLayer11TonemapModeE(
    QSSGShaderFeatures *features,
    QSSGRenderLayer::TonemapMode tonemapMode) {
  QSSGLayerRenderData::setTonemapFeatures(*features, tonemapMode);
}

//  QSSGPrepContextId QSSGLayerRenderData::getOrCreateExtensionContext(const
//      QSSGRenderExtension &ext, QSSGRenderCamera *camera, quint32 slot)
extern "C" Q_DECL_EXPORT
QSSGPrepContextId ritual_ZN19QSSGLayerRenderData27getOrCreateExtensionContextERK19QSSGRenderExtensionP16QSSGRenderCameraj(
    QSSGLayerRenderData *self,
    const QSSGRenderExtension *ext,
    QSSGRenderCamera *camera,
    quint32 slot) {
  return self->getOrCreateExtensionContext(*ext, camera, slot);
}

//  QSSGRenderablesId
//      QSSGLayerRenderData::createRenderables(QSSGPrepContextId prepId,
//      const QSSGNodeIdList &nodes, QSSGRenderHelpers::CreateFlags
//      createFlags)
extern "C" Q_DECL_EXPORT
QSSGRenderablesId ritual_ZN19QSSGLayerRenderData17createRenderablesE17QSSGPrepContextIdRK5QListI10QSSGNodeIdE6QFlagsIN17QSSGRenderHelpers10CreateFlagEE(
    QSSGLayerRenderData *self,
    QSSGPrepContextId prepId,
    const QSSGNodeIdList *nodes,
    int createFlags) {
  return self->createRenderables(
      prepId,
      *nodes,
      QFlags<QSSGRenderHelpers::CreateFlag>::fromInt(createFlags));
}

//  void QSSGLayerRenderData::setGlobalTransform(QSSGRenderablesId
//      renderablesId, const QSSGRenderModel &model, const QMatrix4x4 &mvp)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData18setGlobalTransformE17QSSGRenderablesIdRK15QSSGRenderModelRK10QMatrix4x4(
    QSSGLayerRenderData *self,
    QSSGRenderablesId renderablesId,
    const QSSGRenderModel *model,
    const QMatrix4x4 *mvp) {
  self->setGlobalTransform(renderablesId, *model, *mvp);
}

//  QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(QSSGPrepContextId
//      prepId, const QSSGRenderModel &model)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN19QSSGLayerRenderData18getGlobalTransformE17QSSGPrepContextIdRK15QSSGRenderModel(
    QSSGLayerRenderData *self,
    QSSGPrepContextId prepId,
    const QSSGRenderModel *model) {
  return new QMatrix4x4(self->getGlobalTransform(prepId, *model));
}

//  void QSSGLayerRenderData::setGlobalOpacity(QSSGRenderablesId
//      renderablesId, const QSSGRenderModel &model, float opacity)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData16setGlobalOpacityE17QSSGRenderablesIdRK15QSSGRenderModelf(
    QSSGLayerRenderData *self,
    QSSGRenderablesId renderablesId,
    const QSSGRenderModel *model,
    float opacity) {
  self->setGlobalOpacity(renderablesId, *model, opacity);
}

//  float QSSGLayerRenderData::getGlobalOpacity(QSSGPrepContextId prepId,
//      const QSSGRenderModel &model)
extern "C" Q_DECL_EXPORT
float ritual_ZN19QSSGLayerRenderData16getGlobalOpacityE17QSSGPrepContextIdRK15QSSGRenderModel(
    QSSGLayerRenderData *self,
    QSSGPrepContextId prepId,
    const QSSGRenderModel *model) {
  return self->getGlobalOpacity(prepId, *model);
}

//  void QSSGLayerRenderData::setModelMaterials(QSSGRenderablesId
//      renderablesId, const QSSGRenderModel &model, const
//      QList<QSSGResourceId> &materials)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData17setModelMaterialsE17QSSGRenderablesIdRK15QSSGRenderModelRK5QListI14QSSGResourceIdE(
    QSSGLayerRenderData *self,
    QSSGRenderablesId renderablesId,
    const QSSGRenderModel *model,
    const QList<QSSGResourceId> *materials) {
  self->setModelMaterials(renderablesId, *model, *materials);
}

//  void QSSGLayerRenderData::setModelMaterials(const QSSGRenderablesId
//      renderablesId, const QList<QSSGResourceId> &materials)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData17setModelMaterialsE17QSSGRenderablesIdRK5QListI14QSSGResourceIdE(
    QSSGLayerRenderData *self,
    const QSSGRenderablesId *renderablesId,
    const QList<QSSGResourceId> *materials) {
  self->setModelMaterials(*renderablesId, *materials);
}

//  QSSGPrepResultId
//      QSSGLayerRenderData::prepareModelsForRender(QSSGRenderContextInterfac
//      e &contextInterface, QSSGPrepContextId prepId, QSSGRenderablesId
//      renderablesId, float lodThreshold)
extern "C" Q_DECL_EXPORT
QSSGPrepResultId ritual_ZN19QSSGLayerRenderData22prepareModelsForRenderER26QSSGRenderContextInterface17QSSGPrepContextId17QSSGRenderablesIdf(
    QSSGLayerRenderData *self,
    QSSGRenderContextInterface *contextInterface,
    QSSGPrepContextId prepId,
    QSSGRenderablesId renderablesId,
    float lodThreshold) {
  return self->prepareModelsForRender(
      *contextInterface,
      prepId,
      renderablesId,
      lodThreshold);
}

//  QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle
//      h, const QMatrix4x4 &defaultValue) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QSSGLayerRenderData18getGlobalTransformE23QSSGRenderStorageHandleIL10HandleType1EERK10QMatrix4x4(
    const QSSGLayerRenderData *self,
    const QSSGRenderNodeHandle *h,
    const QMatrix4x4 *defaultValue) {
  return new QMatrix4x4(self->getGlobalTransform(*h, *defaultValue));
}

//  QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(QSSGRenderNodeHandle
//      h) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QSSGLayerRenderData18getGlobalTransformE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGLayerRenderData *self,
    const QSSGRenderNodeHandle *h) {
  return new QMatrix4x4(self->getGlobalTransform(*h));
}

//  QMatrix4x4 QSSGLayerRenderData::getGlobalTransform(const QSSGRenderNode
//      &node) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK19QSSGLayerRenderData18getGlobalTransformERK14QSSGRenderNode(
    const QSSGLayerRenderData *self,
    const QSSGRenderNode *node) {
  return new QMatrix4x4(self->getGlobalTransform(*node));
}

//  QMatrix3x3 QSSGLayerRenderData::getNormalMatrix(QSSGRenderNodeHandle h)
//      const
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZNK19QSSGLayerRenderData15getNormalMatrixE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGLayerRenderData *self,
    const QSSGRenderNodeHandle *h) {
  return new QMatrix3x3(self->getNormalMatrix(*h));
}

//  QMatrix3x3 QSSGLayerRenderData::getNormalMatrix(const QSSGRenderModel
//      &model) const
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZNK19QSSGLayerRenderData15getNormalMatrixERK15QSSGRenderModel(
    const QSSGLayerRenderData *self,
    const QSSGRenderModel *model) {
  return new QMatrix3x3(self->getNormalMatrix(*model));
}

//  InstanceTransforms
//      QSSGLayerRenderData::getInstanceTransforms(QSSGRenderNodeHandle h)
//      const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::InstanceTransforms *ritual_ZNK19QSSGLayerRenderData21getInstanceTransformsE23QSSGRenderStorageHandleIL10HandleType1EE(
    const QSSGLayerRenderData *self,
    const QSSGRenderNodeHandle *h) {
  return new QSSGGlobalRenderNodeData::InstanceTransforms(
      self->getInstanceTransforms(
          *h));
}

//  InstanceTransforms QSSGLayerRenderData::getInstanceTransforms(const
//      QSSGRenderNode &node) const
extern "C" Q_DECL_EXPORT
QSSGGlobalRenderNodeData::InstanceTransforms *ritual_ZNK19QSSGLayerRenderData21getInstanceTransformsERK14QSSGRenderNode(
    const QSSGLayerRenderData *self,
    const QSSGRenderNode *node) {
  return new QSSGGlobalRenderNodeData::InstanceTransforms(
      self->getInstanceTransforms(
          *node));
}

//  float QSSGLayerRenderData::getGlobalOpacity(QSSGRenderNodeHandle h, float
//      defaultValue) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QSSGLayerRenderData16getGlobalOpacityE23QSSGRenderStorageHandleIL10HandleType1EEf(
    const QSSGLayerRenderData *self,
    const QSSGRenderNodeHandle *h,
    float defaultValue) {
  return self->getGlobalOpacity(*h, defaultValue);
}

//  float QSSGLayerRenderData::getGlobalOpacity(const QSSGRenderNode &node)
//      const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QSSGLayerRenderData16getGlobalOpacityERK14QSSGRenderNode(
    const QSSGLayerRenderData *self,
    const QSSGRenderNode *node) {
  return self->getGlobalOpacity(*node);
}

//  QSSGRenderItem2DData::Item2DRenderer
//      QSSGLayerRenderData::getItem2DRenderer(const QSSGRenderItem2D &item)
//      const
extern "C" Q_DECL_EXPORT
QSSGRenderItem2DData::Item2DRenderer *ritual_ZNK19QSSGLayerRenderData17getItem2DRendererERK16QSSGRenderItem2D(
    const QSSGLayerRenderData *self,
    const QSSGRenderItem2D *item) {
  return new QSSGRenderItem2DData::Item2DRenderer(
      self->getItem2DRenderer(
          *item));
}

//  void QSSGLayerRenderData::prepareRenderables(QSSGRenderContextInterface
//      &ctx, QSSGPrepResultId prepId, QRhiRenderPassDescriptor
//      *renderPassDescriptor, const QSSGRhiGraphicsPipelineState &ps,
//      QSSGRenderablesFilters filter)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData18prepareRenderablesER26QSSGRenderContextInterface16QSSGPrepResultIdP24QRhiRenderPassDescriptorRK28QSSGRhiGraphicsPipelineState6QFlagsI21QSSGRenderablesFilterE(
    QSSGLayerRenderData *self,
    QSSGRenderContextInterface *ctx,
    QSSGPrepResultId prepId,
    QRhiRenderPassDescriptor *renderPassDescriptor,
    const QSSGRhiGraphicsPipelineState *ps,
    int filter) {
  self->prepareRenderables(
      *ctx,
      prepId,
      renderPassDescriptor,
      *ps,
      QFlags<QSSGRenderablesFilter>::fromInt(filter));
}

//  void QSSGLayerRenderData::renderRenderables(QSSGRenderContextInterface
//      &ctx, QSSGPrepResultId prepId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData17renderRenderablesER26QSSGRenderContextInterface16QSSGPrepResultId(
    QSSGLayerRenderData *self,
    QSSGRenderContextInterface *ctx,
    QSSGPrepResultId prepId) {
  self->renderRenderables(*ctx, prepId);
}

//  QSSGRenderCameraData QSSGLayerRenderData::getCameraDataImpl(const
//      QSSGRenderCamera *camera) const
extern "C" Q_DECL_EXPORT
QSSGRenderCameraData *ritual_ZNK19QSSGLayerRenderData17getCameraDataImplEPK16QSSGRenderCamera(
    const QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera) {
  return new QSSGRenderCameraData(self->getCameraDataImpl(camera));
}

//  QSSGNodeIdList QSSGLayerRenderData::filter(const
//      QSSGGlobalRenderNodeData::LayerNodeView &layerNodes, quint32
//      layerMask, quint32 typeMask)
extern "C" Q_DECL_EXPORT
QSSGNodeIdList *ritual_ZN19QSSGLayerRenderData6filterERK12QSSGDataViewIP14QSSGRenderNodeEjj(
    const QSSGGlobalRenderNodeData::LayerNodeView *layerNodes,
    quint32 layerMask,
    quint32 typeMask) {
  return new QSSGNodeIdList(
      QSSGLayerRenderData::filter(
          *layerNodes,
          layerMask,
          typeMask));
}

//  QSSGLayerRenderData *QSSGLayerRenderData::getCurrent(const QSSGFrameData
//      &data)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZN19QSSGLayerRenderData10getCurrentERK13QSSGFrameData(
    const QSSGFrameData *data) {
  return QSSGLayerRenderData::getCurrent(*data);
}

//  QSSGDefaultMaterialPreparationResult QSSGLayerRenderData::prepareDefaultM
//      aterialForRender(QSSGRenderDefaultMaterial &inMaterial,
//      QSSGRenderableObjectFlags &inExistingFlags, float inOpacity, bool
//      hasAnyLights, bool anyLightHasShadows,
//      QSSGLayerRenderPreparationResultFlags &ioFlags)
extern "C" Q_DECL_EXPORT
QSSGDefaultMaterialPreparationResult *ritual_ZN19QSSGLayerRenderData31prepareDefaultMaterialForRenderER25QSSGRenderDefaultMaterialR25QSSGRenderableObjectFlagsfbbR37QSSGLayerRenderPreparationResultFlags(
    QSSGLayerRenderData *self,
    QSSGRenderDefaultMaterial *inMaterial,
    QSSGRenderableObjectFlags *inExistingFlags,
    float inOpacity,
    bool hasAnyLights,
    bool anyLightHasShadows,
    QSSGLayerRenderPreparationResultFlags *ioFlags) {
  return new QSSGDefaultMaterialPreparationResult(
      self->prepareDefaultMaterialForRender(
          *inMaterial,
          *inExistingFlags,
          inOpacity,
          hasAnyLights,
          anyLightHasShadows,
          *ioFlags));
}

//  QSSGDefaultMaterialPreparationResult QSSGLayerRenderData::prepareCustomMa
//      terialForRender(QSSGRenderCustomMaterial &inMaterial,
//      QSSGRenderableObjectFlags &inExistingFlags, float inOpacity, bool
//      alreadyDirty, bool hasAnyLights, bool anyLightHasShadows,
//      QSSGLayerRenderPreparationResultFlags &ioFlags)
extern "C" Q_DECL_EXPORT
QSSGDefaultMaterialPreparationResult *ritual_ZN19QSSGLayerRenderData30prepareCustomMaterialForRenderER24QSSGRenderCustomMaterialR25QSSGRenderableObjectFlagsfbbbR37QSSGLayerRenderPreparationResultFlags(
    QSSGLayerRenderData *self,
    QSSGRenderCustomMaterial *inMaterial,
    QSSGRenderableObjectFlags *inExistingFlags,
    float inOpacity,
    bool alreadyDirty,
    bool hasAnyLights,
    bool anyLightHasShadows,
    QSSGLayerRenderPreparationResultFlags *ioFlags) {
  return new QSSGDefaultMaterialPreparationResult(
      self->prepareCustomMaterialForRender(
          *inMaterial,
          *inExistingFlags,
          inOpacity,
          alreadyDirty,
          hasAnyLights,
          anyLightHasShadows,
          *ioFlags));
}

//  void QSSGLayerRenderData::categorizeAndFilterNodes(const
//      QSSGGlobalRenderNodeData::LayerNodeView &layerNodes,
//      QSSGLayerRenderData::NodeCollection &nodeCollection, quint32
//      layerMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData24categorizeAndFilterNodesERK12QSSGDataViewIP14QSSGRenderNodeERNS_14NodeCollectionEj(
    const QSSGGlobalRenderNodeData::LayerNodeView *layerNodes,
    QSSGLayerRenderData::NodeCollection *nodeCollection,
    quint32 layerMask) {
  QSSGLayerRenderData::categorizeAndFilterNodes(
      *layerNodes,
      *nodeCollection,
      layerMask);
}

//  void QSSGLayerRenderData::updateFilteredLayerNodes(quint32 layerMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData24updateFilteredLayerNodesEj(
    QSSGLayerRenderData *self,
    quint32 layerMask) {
  self->updateFilteredLayerNodes(layerMask);
}

//  const QSSGRenderCameraDataList
//      &QSSGLayerRenderData::getCachedCameraDatas()
extern "C" Q_DECL_EXPORT
const QSSGRenderCameraDataList *ritual_ZN19QSSGLayerRenderData20getCachedCameraDatasEv(
    QSSGLayerRenderData *self) {
  return &(self->getCachedCameraDatas());
}

//  void QSSGLayerRenderData::ensureCachedCameraDatas()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData23ensureCachedCameraDatasEv(
    QSSGLayerRenderData *self) {
  self->ensureCachedCameraDatas();
}

//  void QSSGLayerRenderData::updateSortedDepthObjectsListImp(const
//      QSSGRenderCamera &camera, size_t index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData31updateSortedDepthObjectsListImpERK16QSSGRenderCameram(
    QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera,
    size_t index) {
  self->updateSortedDepthObjectsListImp(*camera, index);
}

//  a QMatrix3x3 a ritual of QSSGLayerRenderData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGLayerRenderData__QMatrix3x3(QMatrix3x3 *self) {
  delete self;
}

//  a QSSGLayerRenderData::ModelViewProjections a ritual of
//      QSSGLayerRenderData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGLayerRenderData__QSSGLayerRenderData_ModelViewProjections(
    QSSGLayerRenderData::ModelViewProjections *self) {
  delete self;
}

//  a QSSGRenderItem2DData::Item2DRenderer a ritual of QSSGLayerRenderData
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGLayerRenderData__QSSGRenderItem2DData_Item2DRenderer(
    QSSGRenderItem2DData::Item2DRenderer *self) {
  delete self;
}

//  a QSSGNodeIdList a ritual of QSSGLayerRenderData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGLayerRenderData__QSSGNodeIdList(QSSGNodeIdList *self) {
  delete self;
}

//  void QSSGLayerRenderData::prepareImageForRender(QSSGRenderImage &inImage,
//      QSSGRenderableImage::Type inMapType, QSSGRenderableImage
//      *&ioFirstImage, QSSGRenderableImage *&ioNextImage,
//      QSSGRenderableObjectFlags &ioFlags, QSSGShaderDefaultMaterialKey
//      &ioGeneratedShaderKey, quint32 inImageIndex,
//      QSSGRenderDefaultMaterial *inMaterial)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData21prepareImageForRenderER15QSSGRenderImageN19QSSGRenderableImage4TypeERPS2_S5_R25QSSGRenderableObjectFlagsR25QSSGShaderBaseMaterialKeyI38QSSGShaderDefaultMaterialKeyPropertiesLm25EEjP25QSSGRenderDefaultMaterial(
    QSSGLayerRenderData *self,
    QSSGRenderImage *inImage,
    int inMapType,
    QSSGRenderableImage **ioFirstImage,
    QSSGRenderableImage **ioNextImage,
    QSSGRenderableObjectFlags *ioFlags,
    QSSGShaderDefaultMaterialKey *ioGeneratedShaderKey,
    quint32 inImageIndex,
    QSSGRenderDefaultMaterial *inMaterial) {
  self->prepareImageForRender(
      *inImage, static_cast<QSSGRenderableImage::Type>(inMapType),
      *ioFirstImage, *ioNextImage, *ioFlags, *ioGeneratedShaderKey,
      inImageIndex, inMaterial);
}
