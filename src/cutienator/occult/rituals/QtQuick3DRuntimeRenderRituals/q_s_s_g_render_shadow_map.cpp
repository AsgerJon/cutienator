//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadowmap_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderShadowMap::~QSSGRenderShadowMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderShadowMapD1Ev(QSSGRenderShadowMap *self) {
  delete self;
}

//  void QSSGRenderShadowMap::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderShadowMap22releaseCachedResourcesEv(
    QSSGRenderShadowMap *self) {
  self->releaseCachedResources();
}

//  QSSGShadowMapEntry *QSSGRenderShadowMap::shadowMapEntry(int lightIdx)
extern "C" Q_DECL_EXPORT
QSSGShadowMapEntry *ritual_ZN19QSSGRenderShadowMap14shadowMapEntryEi(
    QSSGRenderShadowMap *self,
    int lightIdx) {
  return self->shadowMapEntry(lightIdx);
}

//  QRhiTextureRenderTarget *QSSGRenderShadowMap::layerRenderTarget(int
//      layerIndex)
extern "C" Q_DECL_EXPORT
QRhiTextureRenderTarget *ritual_ZN19QSSGRenderShadowMap17layerRenderTargetEi(
    QSSGRenderShadowMap *self,
    int layerIndex) {
  return self->layerRenderTarget(layerIndex);
}

//  QRhiRenderPassDescriptor
//      *QSSGRenderShadowMap::layerRenderPassDescriptor(int layerIndex)
extern "C" Q_DECL_EXPORT
QRhiRenderPassDescriptor *ritual_ZN19QSSGRenderShadowMap25layerRenderPassDescriptorEi(
    QSSGRenderShadowMap *self,
    int layerIndex) {
  return self->layerRenderPassDescriptor(layerIndex);
}

//  QRhiTexture *QSSGRenderShadowMap::shadowMapAtlasTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QSSGRenderShadowMap21shadowMapAtlasTextureEv(
    const QSSGRenderShadowMap *self) {
  return self->shadowMapAtlasTexture();
}

//  QRhiTexture *QSSGRenderShadowMap::shadowMapBlueNoiseTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK19QSSGRenderShadowMap25shadowMapBlueNoiseTextureEv(
    const QSSGRenderShadowMap *self) {
  return self->shadowMapBlueNoiseTexture();
}

//  qsizetype QSSGRenderShadowMap::shadowMapEntryCount()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QSSGRenderShadowMap19shadowMapEntryCountEv(
    QSSGRenderShadowMap *self) {
  return self->shadowMapEntryCount();
}

//  QRhiShaderResourceBindings *QSSGRenderShadowMap::shadowClearSrb() const
extern "C" Q_DECL_EXPORT
QRhiShaderResourceBindings *ritual_ZNK19QSSGRenderShadowMap14shadowClearSrbEv(
    const QSSGRenderShadowMap *self) {
  return self->shadowClearSrb();
}
