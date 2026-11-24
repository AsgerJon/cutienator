//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterialmanag
//  er_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderskymaterialmanager_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderimagetexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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

//  QSSGRenderImageTexture
//      QSSGRenderSkyMaterialManager::resolve(QSSGRenderSkyMaterial
//      *settings)
extern "C" Q_DECL_EXPORT
QSSGRenderImageTexture *ritual_ZN28QSSGRenderSkyMaterialManager7resolveEP21QSSGRenderSkyMaterial(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *settings) {
  return new QSSGRenderImageTexture(self->resolve(settings));
}

//  bool
//      QSSGRenderSkyMaterialManager::ensureEnvironmentMap(QSSGRenderSkyMater
//      ial *settings)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QSSGRenderSkyMaterialManager20ensureEnvironmentMapEP21QSSGRenderSkyMaterial(
    QSSGRenderSkyMaterialManager *self,
    QSSGRenderSkyMaterial *settings) {
  return self->ensureEnvironmentMap(settings);
}

//  void QSSGRenderSkyMaterialManager::clearPrefilterCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGRenderSkyMaterialManager19clearPrefilterCacheEv(
    QSSGRenderSkyMaterialManager *self) {
  self->clearPrefilterCache();
}
