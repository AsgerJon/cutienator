//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSSGRhiQuadRenderer::prepareQuad(QSSGRhiContext *rhiCtx,
//      QRhiResourceUpdateBatch *maybeRub)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiQuadRenderer11prepareQuadEP14QSSGRhiContextP23QRhiResourceUpdateBatch(
    QSSGRhiQuadRenderer *self,
    QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *maybeRub) {
  self->prepareQuad(rhiCtx, maybeRub);
}

//  void QSSGRhiQuadRenderer::recordRenderQuad(QSSGRhiContext *rhiCtx,
//      QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
//      QRhiRenderPassDescriptor *rpDesc, Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiQuadRenderer16recordRenderQuadEP14QSSGRhiContextP28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP24QRhiRenderPassDescriptor6QFlagsINS_4FlagEE(
    QSSGRhiQuadRenderer *self,
    QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps,
    QRhiShaderResourceBindings *srb,
    QRhiRenderPassDescriptor *rpDesc,
    int flags) {
  self->recordRenderQuad(
      rhiCtx,
      ps,
      srb,
      rpDesc,
      QFlags<QSSGRhiQuadRenderer::Flag>::fromInt(flags));
}

//  void QSSGRhiQuadRenderer::recordRenderQuadPass(QSSGRhiContext *rhiCtx,
//      QSSGRhiGraphicsPipelineState *ps, QRhiShaderResourceBindings *srb,
//      QRhiTextureRenderTarget *rt, Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiQuadRenderer20recordRenderQuadPassEP14QSSGRhiContextP28QSSGRhiGraphicsPipelineStateP26QRhiShaderResourceBindingsP23QRhiTextureRenderTarget6QFlagsINS_4FlagEE(
    QSSGRhiQuadRenderer *self,
    QSSGRhiContext *rhiCtx,
    QSSGRhiGraphicsPipelineState *ps,
    QRhiShaderResourceBindings *srb,
    QRhiTextureRenderTarget *rt,
    int flags) {
  self->recordRenderQuadPass(
      rhiCtx,
      ps,
      srb,
      rt,
      QFlags<QSSGRhiQuadRenderer::Flag>::fromInt(flags));
}

//  void QSSGRhiQuadRenderer::ensureBuffers(QSSGRhiContext *rhiCtx,
//      QRhiResourceUpdateBatch *rub)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiQuadRenderer13ensureBuffersEP14QSSGRhiContextP23QRhiResourceUpdateBatch(
    QSSGRhiQuadRenderer *self,
    QSSGRhiContext *rhiCtx,
    QRhiResourceUpdateBatch *rub) {
  self->ensureBuffers(rhiCtx, rub);
}

//  QSSGRhiQuadRenderer::~QSSGRhiQuadRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRhiQuadRendererD1Ev(QSSGRhiQuadRenderer *self) {
  delete self;
}
