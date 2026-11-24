//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Type UserRenderPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK14UserRenderPass8passTypeEv(
    const UserRenderPass *self) {
  return self->passType();
}

//  bool UserRenderPass::hasData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14UserRenderPass7hasDataEv(const UserRenderPass *self) {
  return self->hasData();
}

//  UserRenderPass::~UserRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN14UserRenderPassD1Ev(UserRenderPass *self) {
  delete self;
}
