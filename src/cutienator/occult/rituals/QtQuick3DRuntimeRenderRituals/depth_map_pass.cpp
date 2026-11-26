//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void DepthMapPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DepthMapPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData(
    DepthMapPass *self,
    QSSGRenderer *renderer,
    QSSGLayerRenderData *data) {
  self->renderPrep(*renderer, *data);
}

//  void DepthMapPass::renderPass(QSSGRenderer &renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DepthMapPass10renderPassER12QSSGRenderer(
    DepthMapPass *self,
    QSSGRenderer *renderer) {
  self->renderPass(*renderer);
}

//  Type DepthMapPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK12DepthMapPass8passTypeEv(
    const DepthMapPass *self) {
  return self->passType();
}

//  void DepthMapPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DepthMapPass13resetForFrameEv(DepthMapPass *self) {
  self->resetForFrame();
}

//  void DepthMapPass::setMultisamplingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN12DepthMapPass23setMultisamplingEnabledEb(
    DepthMapPass *self,
    bool enabled) {
  self->setMultisamplingEnabled(enabled);
}

//  bool DepthMapPass::isMultisamplingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12DepthMapPass22isMultisamplingEnabledEv(
    const DepthMapPass *self) {
  return self->isMultisamplingEnabled();
}

//  DepthMapPass::~DepthMapPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN12DepthMapPassD1Ev(DepthMapPass *self) {
  delete self;
}
