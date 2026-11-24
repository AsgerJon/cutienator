//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderlight_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGRenderLight::QSSGRenderLight(Type type)
extern "C" Q_DECL_EXPORT
QSSGRenderLight *ritual_ZN15QSSGRenderLightC1EN21QSSGRenderGraphObject4TypeE(
    QSSGRenderGraphObject::Type type) {
  return new QSSGRenderLight(type);
}

//  bool QSSGRenderLight::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLight9isEnabledEv(const QSSGRenderLight *self) {
  return self->isEnabled();
}

//  bool QSSGRenderLight::isDirty(DirtyFlag dirtyFlag) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QSSGRenderLight7isDirtyENS_9DirtyFlagE(
    const QSSGRenderLight *self,
    QSSGRenderLight::DirtyFlag dirtyFlag) {
  return self->isDirty(dirtyFlag);
}

//  void QSSGRenderLight::markDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLight9markDirtyENS_9DirtyFlagE(
    QSSGRenderLight *self,
    QSSGRenderLight::DirtyFlag dirtyFlag) {
  self->markDirty(dirtyFlag);
}

//  void QSSGRenderLight::clearDirty(DirtyFlag dirtyFlag)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QSSGRenderLight10clearDirtyENS_9DirtyFlagE(
    QSSGRenderLight *self,
    QSSGRenderLight::DirtyFlag dirtyFlag) {
  self->clearDirty(dirtyFlag);
}
