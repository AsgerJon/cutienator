//  Written by hand on 2026-11-25 from
//  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterialmanager_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  The private functions that take the private FrameState are written
//  with its full name, QSSGRenderSkyMaterialManager::FrameState, handed
//  as an address.
//  The class is exported, has no virtual function and no Q_OBJECT, so it
//  has no Cute class.
//  Not written: renderEnvironmentCube (takes a std::shared_ptr).
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterialmanager_p.h>

//  QSSGRenderSkyMaterialManager::QSSGRenderSkyMaterialManager(const QSSGRenderContextInterface &inContext)
extern "C" Q_DECL_EXPORT
QSSGRenderSkyMaterialManager *ritual_ZN28QSSGRenderSkyMaterialManagerC1ERK26QSSGRenderContextInterface(
    const QSSGRenderContextInterface *inContext) {
  return new QSSGRenderSkyMaterialManager(*inContext);
}

//  QSSGRenderSkyMaterialManager::~QSSGRenderSkyMaterialManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManagerD1Ev(
    QSSGRenderSkyMaterialManager *self) {
  delete self;
}

//  void QSSGRenderSkyMaterialManager::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager22releaseCachedResourcesEv(
    QSSGRenderSkyMaterialManager *self) {
  self->releaseCachedResources();
}

//  QSSGRenderImageTexture QSSGRenderSkyMaterialManager::resolve(QSSGRenderSkyMaterial *settings)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN28QSSGRenderSkyMaterialManager7resolveEP21QSSGRenderSkyMaterial(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *settings) {
  return new QSSGRenderImageTexture(self->resolve(settings));
}

//  bool QSSGRenderSkyMaterialManager::ensureEnvironmentMap(QSSGRenderSkyMaterial *settings)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSSGRenderSkyMaterialManager20ensureEnvironmentMapEP21QSSGRenderSkyMaterial(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *settings) {
  return self->ensureEnvironmentMap(settings);
}

//  bool QSSGRenderSkyMaterialManager::computeFrameState(QSSGRenderSkyMaterial *inSky, FrameState &fs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSSGRenderSkyMaterialManager17computeFrameStateEP21QSSGRenderSkyMaterialRNS_10FrameStateE(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *inSky,
    QSSGRenderSkyMaterialManager::FrameState *fs) {
  return self->computeFrameState(inSky, *fs);
}

//  bool QSSGRenderSkyMaterialManager::ensureTextures(FrameState &fs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSSGRenderSkyMaterialManager14ensureTexturesERNS_10FrameStateE(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterialManager::FrameState *fs) {
  return self->ensureTextures(*fs);
}

//  void QSSGRenderSkyMaterialManager::deriveCycleState(QSSGRenderSkyMaterial *inSky, FrameState &fs)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager16deriveCycleStateEP21QSSGRenderSkyMaterialRNS_10FrameStateE(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *inSky,
    QSSGRenderSkyMaterialManager::FrameState *fs) {
  self->deriveCycleState(inSky, *fs);
}

//  void QSSGRenderSkyMaterialManager::validateAndUpdateCacheKey(const FrameState &fs,
//      QSSGRhiShaderPipeline *envShaderPipelineKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager25validateAndUpdateCacheKeyERKNS_10FrameStateEP21QSSGRhiShaderPipeline(
    QSSGRenderSkyMaterialManager *self,
    const QSSGRenderSkyMaterialManager::FrameState *fs,
    QSSGRhiShaderPipeline *envShaderPipelineKey) {
  self->validateAndUpdateCacheKey(*fs, envShaderPipelineKey);
}

//  bool QSSGRenderSkyMaterialManager::ensureSharedResources(FrameState &fs, QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSSGRenderSkyMaterialManager21ensureSharedResourcesERNS_10FrameStateEP17QRhiCommandBuffer(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterialManager::FrameState *fs,
    QRhiCommandBuffer *cb) {
  return self->ensureSharedResources(*fs, cb);
}

//  void QSSGRenderSkyMaterialManager::runEnvironmentMipChain(const FrameState &fs,
//      QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager22runEnvironmentMipChainERKNS_10FrameStateEP17QRhiCommandBuffer(
    QSSGRenderSkyMaterialManager *self,
    const QSSGRenderSkyMaterialManager::FrameState *fs,
    QRhiCommandBuffer *cb) {
  self->runEnvironmentMipChain(*fs, cb);
}

//  bool QSSGRenderSkyMaterialManager::runPrefilterCycle(QSSGRenderSkyMaterial *inSky,
//      const FrameState &fs, QRhiCommandBuffer *cb, QRhiResourceUpdateBatch
//      *&rub)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSSGRenderSkyMaterialManager17runPrefilterCycleEP21QSSGRenderSkyMaterialRKNS_10FrameStateEP17QRhiCommandBufferRP23QRhiResourceUpdateBatch(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *inSky,
    const QSSGRenderSkyMaterialManager::FrameState *fs,
    QRhiCommandBuffer *cb,
    QRhiResourceUpdateBatch **rub) {
  return self->runPrefilterCycle(inSky, *fs, cb, *rub);
}

//  void QSSGRenderSkyMaterialManager::initializeTailMips(const FrameState &fs, QRhiCommandBuffer
//      *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager18initializeTailMipsERKNS_10FrameStateEP17QRhiCommandBuffer(
    QSSGRenderSkyMaterialManager *self,
    const QSSGRenderSkyMaterialManager::FrameState *fs,
    QRhiCommandBuffer *cb) {
  self->initializeTailMips(*fs, cb);
}

//  void QSSGRenderSkyMaterialManager::clearPrefilterCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager19clearPrefilterCacheEv(
    QSSGRenderSkyMaterialManager *self) {
  self->clearPrefilterCache();
}
