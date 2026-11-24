//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QSSGRenderRay::HitResult::intersects() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QSSGRenderRay9HitResult10intersectsEv(
    const QSSGRenderRay::HitResult *self) {
  return self->intersects();
}

//  QSSGRenderRay::HitResult::~HitResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSSGRenderRay9HitResultD1Ev(QSSGRenderRay::HitResult *self) {
  delete self;
}
