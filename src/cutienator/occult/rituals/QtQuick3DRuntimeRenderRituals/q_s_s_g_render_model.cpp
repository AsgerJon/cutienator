//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendermodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QSSGRenderModel::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QSSGRenderModel13instanceCountEv(
    const QSSGRenderModel *self) {
  return self->instanceCount();
}

//  bool QSSGRenderModel::instancing() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderModel10instancingEv(const QSSGRenderModel *self) {
  return self->instancing();
}

//  bool QSSGRenderModel::hasLightmap() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderModel11hasLightmapEv(
    const QSSGRenderModel *self) {
  return self->hasLightmap();
}

//  bool QSSGRenderModel::usesBoneTexture() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderModel15usesBoneTextureEv(
    const QSSGRenderModel *self) {
  return self->usesBoneTexture();
}

//  QSSGRenderModel::QSSGRenderModel()
extern "C" Q_DECL_EXPORT
QSSGRenderModel *ritual_ZN15QSSGRenderModelC1Ev() {
  return new QSSGRenderModel();
}
