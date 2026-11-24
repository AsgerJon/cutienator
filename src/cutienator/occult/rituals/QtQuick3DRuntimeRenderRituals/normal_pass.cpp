//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Type NormalPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK10NormalPass8passTypeEv(
    const NormalPass *self) {
  return self->passType();
}

//  void NormalPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10NormalPass13resetForFrameEv(NormalPass *self) {
  self->resetForFrame();
}

//  NormalPass::~NormalPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN10NormalPassD1Ev(NormalPass *self) {
  delete self;
}
