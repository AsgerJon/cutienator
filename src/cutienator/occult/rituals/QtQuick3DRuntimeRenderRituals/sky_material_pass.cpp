//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Type SkyMaterialPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK15SkyMaterialPass8passTypeEv(
    const SkyMaterialPass *self) {
  return self->passType();
}

//  SkyMaterialPass::~SkyMaterialPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN15SkyMaterialPassD1Ev(SkyMaterialPass *self) {
  delete self;
}
