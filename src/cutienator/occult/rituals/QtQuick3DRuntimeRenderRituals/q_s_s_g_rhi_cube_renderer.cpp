//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGRhiCubeRenderer::prepareCube(QSSGRhiContext *rhiCtx,
//      QRhiResourceUpdateBatch *maybeRub)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiCubeRenderer11prepareCubeEP14QSSGRhiContextP23QRhiResourceUpdateBatch(
    QSSGRhiCubeRenderer *self,
    QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *maybeRub) {
  self->prepareCube(rhiCtx, maybeRub);
}

//  void QSSGRhiCubeRenderer::recordRenderCube(QSSGRhiContext *rhiCtx,
//      QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
//      QRhiRenderPassDescriptor *rpDesc, QSSGRhiQuadRenderer::Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiCubeRenderer16recordRenderCubeEP14QSSGRhiContextP28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP24QRhiRenderPassDescriptor6QFlagsIN19QSSGRhiQuadRenderer4FlagEE(
    QSSGRhiCubeRenderer *self,
    QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps,
    QRhiShaderResourceBindings *srb,
    QRhiRenderPassDescriptor *rpDesc,
    int flags) {
  self->recordRenderCube(
      rhiCtx,
      ps,
      srb,
      rpDesc,
      QFlags<QSSGRhiQuadRenderer::Flag>::fromInt(flags));
}

//  void QSSGRhiCubeRenderer::ensureBuffers(QSSGRhiContext *rhiCtx,
//      QRhiResourceUpdateBatch *rub)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiCubeRenderer13ensureBuffersEP14QSSGRhiContextP23QRhiResourceUpdateBatch(
    QSSGRhiCubeRenderer *self,
    QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *rub) {
  self->ensureBuffers(rhiCtx, rub);
}

//  QSSGRhiCubeRenderer::~QSSGRhiCubeRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiCubeRendererD1Ev(QSSGRhiCubeRenderer *self) {
  delete self;
}
