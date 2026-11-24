//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgbatchrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  GraphicsPipelineStateKey
//      QSGBatchRenderer::GraphicsPipelineStateKey::create(const
//      GraphicsState &state, const ShaderManagerShader *sms, const
//      QRhiRenderPassDescriptor *rpDesc, const QRhiShaderResourceBindings
//      *srb)
extern "C" Q_DECL_EXPORT
QSGBatchRenderer::GraphicsPipelineStateKey *ritual_ZN16QSGBatchRenderer24GraphicsPipelineStateKey6createERKNS_13GraphicsStateEPKNS_19ShaderManagerShaderEPK24QRhiRenderPassDescriptorPK26QRhiShaderResourceBindings(
    const QSGBatchRenderer::GraphicsState *state,
    const QSGBatchRenderer::ShaderManagerShader *sms,
    const QRhiRenderPassDescriptor *rpDesc,
    const QRhiShaderResourceBindings *srb) {
  return new QSGBatchRenderer::GraphicsPipelineStateKey(
      QSGBatchRenderer::GraphicsPipelineStateKey::create(
          *state,
          sms,
          rpDesc,
          srb));
}

//  QSGBatchRenderer::GraphicsPipelineStateKey::~GraphicsPipelineStateKey()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGBatchRenderer24GraphicsPipelineStateKeyD1Ev(
    QSGBatchRenderer::GraphicsPipelineStateKey *self) {
  delete self;
}
