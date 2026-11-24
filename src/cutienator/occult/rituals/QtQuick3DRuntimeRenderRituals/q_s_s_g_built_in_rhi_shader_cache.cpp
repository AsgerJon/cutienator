//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererimplshaders_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendererimplshaders_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGBuiltInRhiShaderCache::releaseCachedResources()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGBuiltInRhiShaderCache22releaseCachedResourcesEv(
    QSSGBuiltInRhiShaderCache *self) {
  self->releaseCachedResources();
}

//  QSSGBuiltInRhiShaderCache::~QSSGBuiltInRhiShaderCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QSSGBuiltInRhiShaderCacheD1Ev(
    QSSGBuiltInRhiShaderCache *self) {
  delete self;
}
