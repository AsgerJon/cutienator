//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrhicontext.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QSSGGraphicsPipelineStateKey QSSGGraphicsPipelineStateKey::create(const
//      QSSGRhiGraphicsPipelineState &state, const QRhiRenderPassDescriptor
//      *rpDesc, const QRhiShaderResourceBindings *srb)
extern "C" Q_DECL_EXPORT
QSSGGraphicsPipelineStateKey *ritual_ZN28QSSGGraphicsPipelineStateKey6createERK28QSSGRhiGraphicsPipelineStatePK24QRhiRenderPassDescriptorPK26QRhiShaderResourceBindings(
    const QSSGRhiGraphicsPipelineState *state,
    const QRhiRenderPassDescriptor *rpDesc,
    const QRhiShaderResourceBindings *srb) {
  return new QSSGGraphicsPipelineStateKey(
      QSSGGraphicsPipelineStateKey::create(
          *state,
          rpDesc,
          srb));
}

//  QSSGGraphicsPipelineStateKey::~QSSGGraphicsPipelineStateKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QSSGGraphicsPipelineStateKeyD1Ev(
    QSSGGraphicsPipelineStateKey *self) {
  delete self;
}
