//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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
