//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderitem2d_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershaderkeys_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderparticleshaderkeys_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QSSGLayerRenderData::~QSSGLayerRenderData()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderDataD1Ev(QSSGLayerRenderData *self) {
  delete self;
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

//  const RenderableItem2DEntries
//      &QSSGLayerRenderData::getRenderableItem2Ds()
extern "C" Q_DECL_EXPORT
QList<QSSGRenderItem2D *> *ritual_ZN19QSSGLayerRenderData20getRenderableItem2DsEv(
    QSSGLayerRenderData *self) {
  return new QList<QSSGRenderItem2D *>(self->getRenderableItem2Ds());
}

//  void QSSGLayerRenderData::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData13resetForFrameEv(
    QSSGLayerRenderData *self) {
  self->resetForFrame();
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

//  QSSGRenderCameraData QSSGLayerRenderData::getCameraDataImpl(const
//      QSSGRenderCamera *camera) const
extern "C" Q_DECL_EXPORT
QSSGRenderCameraData *ritual_ZNK19QSSGLayerRenderData17getCameraDataImplEPK16QSSGRenderCamera(
    const QSSGLayerRenderData *self,
    const QSSGRenderCamera *camera) {
  return new QSSGRenderCameraData(self->getCameraDataImpl(camera));
}

//  QSSGLayerRenderData *QSSGLayerRenderData::getCurrent(const QSSGFrameData
//      &data)
extern "C" Q_DECL_EXPORT
QSSGLayerRenderData *ritual_ZN19QSSGLayerRenderData10getCurrentERK13QSSGFrameData(
    const QSSGFrameData *data) {
  return QSSGLayerRenderData::getCurrent(*data);
}

//  void QSSGLayerRenderData::updateFilteredLayerNodes(quint32 layerMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData24updateFilteredLayerNodesEj(
    QSSGLayerRenderData *self,
    quint32 layerMask) {
  self->updateFilteredLayerNodes(layerMask);
}

//  void QSSGLayerRenderData::ensureCachedCameraDatas()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGLayerRenderData23ensureCachedCameraDatasEv(
    QSSGLayerRenderData *self) {
  self->ensureCachedCameraDatas();
}
