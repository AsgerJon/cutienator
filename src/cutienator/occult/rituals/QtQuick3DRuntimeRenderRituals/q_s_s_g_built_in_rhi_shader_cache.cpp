//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererimplshaders_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererimplshaders_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/QByteArray>
#include <QtCore/QFlags>

//  QSSGBuiltInRhiShaderCache::QSSGBuiltInRhiShaderCache(QSSGShaderCache
//      &shaderCache)
extern "C" Q_DECL_EXPORT
QSSGBuiltInRhiShaderCache *ritual_ZN25QSSGBuiltInRhiShaderCacheC1ER15QSSGShaderCache(
    QSSGShaderCache *shaderCache) {
  return new QSSGBuiltInRhiShaderCache(*shaderCache);
}

//  void QSSGBuiltInRhiShaderCache::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGBuiltInRhiShaderCache22releaseCachedResourcesEv(
    QSSGBuiltInRhiShaderCache *self) {
  self->releaseCachedResources();
}

//  QSSGRhiShaderPipelinePtr QSSGBuiltInRhiShaderCache::getRhiGridShader(int
//      viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache16getRhiGridShaderEi(
    QSSGBuiltInRhiShaderCache *self,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiGridShader(viewCount));
}

//  QSSGRhiShaderPipelinePtr QSSGBuiltInRhiShaderCache::getRhiSsaoShader(int
//      viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache16getRhiSsaoShaderEi(
    QSSGBuiltInRhiShaderCache *self,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiSsaoShader(viewCount));
}

//  QSSGRhiShaderPipelinePtr QSSGBuiltInRhiShaderCache::getRhiSkyBoxCubeShade
//      r(QSSGRenderLayer::TonemapMode tonemapMode, bool isLinear, int
//      viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache22getRhiSkyBoxCubeShaderEN15QSSGRenderLayer11TonemapModeEbi(
    QSSGBuiltInRhiShaderCache *self,
    QSSGRenderLayer::TonemapMode tonemapMode,
    bool isLinear,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiSkyBoxCubeShader(
          tonemapMode,
          isLinear,
          viewCount));
}

//  QSSGRhiShaderPipelinePtr QSSGBuiltInRhiShaderCache::getRhiSkyBoxShader(QS
//      SGRenderLayer::TonemapMode tonemapMode, bool isRGBE, int viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache18getRhiSkyBoxShaderEN15QSSGRenderLayer11TonemapModeEbi(
    QSSGBuiltInRhiShaderCache *self,
    QSSGRenderLayer::TonemapMode tonemapMode,
    bool isRGBE,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiSkyBoxShader(
          tonemapMode,
          isRGBE,
          viewCount));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiSupersampleResolveShader(int
//      viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache30getRhiSupersampleResolveShaderEi(
    QSSGBuiltInRhiShaderCache *self,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiSupersampleResolveShader(
          viewCount));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiProgressiveAAShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache25getRhiProgressiveAAShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiProgressiveAAShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiMotionVectorShader(bool skin, bool
//      instance, bool morph)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache24getRhiMotionVectorShaderEbbb(
    QSSGBuiltInRhiShaderCache *self,
    bool skin,
    bool instance,
    bool morph) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiMotionVectorShader(
          skin,
          instance,
          morph));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiTemporalAAShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache22getRhiTemporalAAShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiTemporalAAShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiSimpleQuadShader(int viewCount,
//      QSSGRenderLayer::TonemapMode tonemapMode)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache22getRhiSimpleQuadShaderEiN15QSSGRenderLayer11TonemapModeE(
    QSSGBuiltInRhiShaderCache *self,
    int viewCount,
    QSSGRenderLayer::TonemapMode tonemapMode) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiSimpleQuadShader(
          viewCount,
          tonemapMode));
}

//  QSSGRhiShaderPipelinePtr QSSGBuiltInRhiShaderCache::getRhiLightmapUVRaste
//      rizationShader(LightmapUVRasterizationShaderMode mode)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache35getRhiLightmapUVRasterizationShaderENS_33LightmapUVRasterizationShaderModeE(
    QSSGBuiltInRhiShaderCache *self,
    QSSGBuiltInRhiShaderCache::LightmapUVRasterizationShaderMode mode) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiLightmapUVRasterizationShader(
          mode));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiLightmapDilateShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache26getRhiLightmapDilateShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiLightmapDilateShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiDebugObjectShader(int viewCount)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache23getRhiDebugObjectShaderEi(
    QSSGBuiltInRhiShaderCache *self,
    int viewCount) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiDebugObjectShader(
          viewCount));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiReflectionprobePreFilterShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache36getRhiReflectionprobePreFilterShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiReflectionprobePreFilterShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache27getRhiSkyIblPreFilterShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiSkyIblPreFilterShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiSkyIblPreFilterNormalizeShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache36getRhiSkyIblPreFilterNormalizeShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiSkyIblPreFilterNormalizeShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhienvironmentmapPreFilterShader(bool
//      isRGBE)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache35getRhienvironmentmapPreFilterShaderEb(
    QSSGBuiltInRhiShaderCache *self,
    bool isRGBE) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhienvironmentmapPreFilterShader(
          isRGBE));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiEnvironmentmapShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache26getRhiEnvironmentmapShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiEnvironmentmapShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiClearMRTShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache20getRhiClearMRTShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiClearMRTShader());
}

//  QSSGRhiShaderPipelinePtr QSSGBuiltInRhiShaderCache::getRhiOitCompositeSha
//      der(QSSGRenderLayer::OITMethod method, bool multisample, bool
//      use_buffers)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache24getRhiOitCompositeShaderEN15QSSGRenderLayer9OITMethodEbb(
    QSSGBuiltInRhiShaderCache *self,
    QSSGRenderLayer::OITMethod method,
    bool multisample,
    bool use_buffers) {
  return new QSSGRhiShaderPipelinePtr(
      self->getRhiOitCompositeShader(
          method,
          multisample,
          use_buffers));
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiCubeMapToAtlasShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache26getRhiCubeMapToAtlasShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiCubeMapToAtlasShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiClearShadowMapShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache26getRhiClearShadowMapShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiClearShadowMapShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiClearImageShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache22getRhiClearImageShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiClearImageShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getRhiClearBufferShader()
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache23getRhiClearBufferShaderEv(
    QSSGBuiltInRhiShaderCache *self) {
  return new QSSGRhiShaderPipelinePtr(self->getRhiClearBufferShader());
}

//  QSSGRhiShaderPipelinePtr
//      QSSGBuiltInRhiShaderCache::getBuiltinRhiShader(const QByteArray
//      &name, BuiltinShader &storage, int viewCount,
//      QSSGRhiShaderPipeline::StageFlags vertexStageFlags)
extern "C" Q_DECL_EXPORT
QSSGRhiShaderPipelinePtr *ritual_ZN25QSSGBuiltInRhiShaderCache19getBuiltinRhiShaderERK10QByteArrayRNS_13BuiltinShaderEi6QFlagsIN21QSSGRhiShaderPipeline9StageFlagEE(
    QSSGBuiltInRhiShaderCache *self,
    const QByteArray *name,
    QSSGBuiltInRhiShaderCache::BuiltinShader *storage,
    int viewCount,
    int vertexStageFlags) {
  return new QSSGRhiShaderPipelinePtr(
      self->getBuiltinRhiShader(
          *name,
          *storage,
          viewCount,
          QFlags<QSSGRhiShaderPipeline::StageFlag>::fromInt(vertexStageFlags)));
}

//  QSSGBuiltInRhiShaderCache::~QSSGBuiltInRhiShaderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGBuiltInRhiShaderCacheD1Ev(
    QSSGBuiltInRhiShaderCache *self) {
  delete self;
}

//  a QSSGRhiShaderPipelinePtr a ritual of QSSGBuiltInRhiShaderCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSSGBuiltInRhiShaderCache__QSSGRhiShaderPipelinePtr(
    QSSGRhiShaderPipelinePtr *self) {
  delete self;
}
