//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercustommaterial_p
//  .h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendercustommaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderCustomMaterial::QSSGRenderCustomMaterial()
extern "C" Q_DECL_EXPORT
QSSGRenderCustomMaterial *ritual_ZN24QSSGRenderCustomMaterialC1Ev() {
  return new QSSGRenderCustomMaterial();
}

//  QSSGRenderCustomMaterial::~QSSGRenderCustomMaterial()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderCustomMaterialD1Ev(
    QSSGRenderCustomMaterial *self) {
  delete self;
}

//  void QSSGRenderCustomMaterial::markDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderCustomMaterial9markDirtyEv(
    QSSGRenderCustomMaterial *self) {
  self->markDirty();
}

//  void QSSGRenderCustomMaterial::clearDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderCustomMaterial10clearDirtyEv(
    QSSGRenderCustomMaterial *self) {
  self->clearDirty();
}

//  void QSSGRenderCustomMaterial::setAlwaysDirty(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSSGRenderCustomMaterial14setAlwaysDirtyEb(
    QSSGRenderCustomMaterial *self,
    bool v) {
  self->setAlwaysDirty(v);
}

//  bool QSSGRenderCustomMaterial::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QSSGRenderCustomMaterial7isDirtyEv(
    const QSSGRenderCustomMaterial *self) {
  return self->isDirty();
}
