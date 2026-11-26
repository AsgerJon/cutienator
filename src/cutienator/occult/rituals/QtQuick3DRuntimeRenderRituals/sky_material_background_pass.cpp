//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderhelpers_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1100, as local:qssgrenderpass.cpp:skyMaterialTonemapFeatures
static void skyMaterialTonemapFeatures(QSSGRenderLayer::TonemapMode mode, QSSGShaderFeatures &features, quint32 &key)
{
    switch (mode) {
    case QSSGRenderLayer::TonemapMode::Linear:
        features.set(QSSGShaderFeatures::Feature::LinearTonemapping, true);
        key = 1;
        break;
    case QSSGRenderLayer::TonemapMode::Aces:
        features.set(QSSGShaderFeatures::Feature::AcesTonemapping, true);
        key = 2;
        break;
    case QSSGRenderLayer::TonemapMode::HejlDawson:
        features.set(QSSGShaderFeatures::Feature::HejlDawsonTonemapping, true);
        key = 3;
        break;
    case QSSGRenderLayer::TonemapMode::Filmic:
        features.set(QSSGShaderFeatures::Feature::FilmicTonemapping, true);
        key = 4;
        break;
    case QSSGRenderLayer::TonemapMode::None:
    case QSSGRenderLayer::TonemapMode::Custom:
        key = 0; // passthrough (Custom tonemapping in the sky is not yet supported)
        break;
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1186, as _ZN25SkyMaterialBackgroundPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData
inline void SkyMaterialBackgroundPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData &data)
{
    const auto &ctx = *renderer.contextInterface();
    const auto &rhiCtx = ctx.rhiContext();
    QSSG_ASSERT(rhiCtx->rhi()->isRecordingFrame(), return);
    QSSG_ASSERT(!data.renderedCameras.isEmpty(), return);
    QSSG_ASSERT(data.renderedCameras.count() == data.layer.viewCount, return);
    layer = &data.layer;
    QSSG_ASSERT(layer && layer->skyMaterial, return);

    ready = false;

    rpDesc = rhiCtx->mainRenderPassDescriptor();
    ps = data.getPipelineState();
    ps.samples = rhiCtx->mainPassSampleCount();
    ps.viewCount = data.layer.viewCount;
    ps.polygonMode = QRhiGraphicsPipeline::Fill;
    // When there are effects, the last effect pass performs tonemapping, so the sky must
    // output linear here (TonemapMode::None below).
    skipTonemapping = layer->firstEffect != nullptr;

    QRhi *rhi = rhiCtx->rhi();
    QSSGRenderSkyMaterial &skyMaterial = *layer->skyMaterial;
    const int viewCount = data.layer.viewCount;

    const QSSGRenderLayer::TonemapMode tonemapMode =
            skipTonemapping && (layer->tonemapMode != QSSGRenderLayer::TonemapMode::Custom)
            ? QSSGRenderLayer::TonemapMode::None
            : layer->tonemapMode;
    QSSGShaderFeatures tonemapFeatures;
    quint32 tonemapKey = 0;
    skyMaterialTonemapFeatures(tonemapMode, tonemapFeatures, tonemapKey);

    pipeline = skyMaterial.ensureBackgroundPipeline(ctx, tonemapFeatures, tonemapKey, viewCount);
    if (!pipeline) // shader/textures not ready yet — skip this frame (clear color shows)
        return;

    // Reconstruct the view direction inputs exactly like skybox.vert, per view:
    //   eye = orientation * (cameraRotation * (inverseProjection * ndcPos))
    // viewRotation folds orientation * cameraRotation into one translation-free matrix.
    // orientation (the probe orientation) is shared across views.
    const QMatrix3x3 o = layer->lightProbeSettings.probeOrientation;
    const QMatrix4x4 orientation(o(0, 0), o(0, 1), o(0, 2), 0.0f,
                                 o(1, 0), o(1, 1), o(1, 2), 0.0f,
                                 o(2, 0), o(2, 1), o(2, 2), 0.0f,
                                 0.0f,    0.0f,    0.0f,    1.0f);
    QVarLengthArray<QMatrix4x4, 2> inverseProjections;
    QVarLengthArray<QMatrix4x4, 2> viewRotations;
    for (int v = 0; v < viewCount; ++v) {
        const QSSGRenderCamera &camera = *data.renderedCameras[v];
        inverseProjections.append(camera.projection.inverted());
        QMatrix4x4 cameraRotation = data.getGlobalTransform(camera);
        cameraRotation.setColumn(3, QVector4D(0.0f, 0.0f, 0.0f, 1.0f)); // drop translation
        viewRotations.append(orientation * cameraRotation);
    }
    const float adjustY = rhi->isYUpInNDC() ? 1.0f : -1.0f;
    const float exposure = layer->lightProbeSettings.probeExposure;

    skyMaterial.updateBackgroundUniforms(ctx, inverseProjections, viewRotations, adjustY, exposure);

    QSSGRhiContextPrivate *rhiCtxD = QSSGRhiContextPrivate::get(rhiCtx.get());
    backgroundSrb = rhiCtxD->srb(skyMaterial.backgroundBindings);

    switch (skyMaterial.skyboxMode) {
    case QSSGRenderSkyMaterial::SkyboxMode::ScreenSpaceHalf:
        scaleDivisor = 2;
        break;
    case QSSGRenderSkyMaterial::SkyboxMode::ScreenSpaceQuarter:
        scaleDivisor = 4;
        break;
    case QSSGRenderSkyMaterial::SkyboxMode::ScreenSpaceFull:
    case QSSGRenderSkyMaterial::SkyboxMode::Cubemap:
        scaleDivisor = 1;
        break;
    }

    renderer.rhiQuadRenderer()->prepareQuad(rhiCtx.get(), nullptr);

    // Reduced-scale: render the (tonemapped) sky into a smaller offscreen target now, in
    // the prepare phase, so renderPass only has to upscale-blit it into the main pass.
    if (scaleDivisor > 1) {
        const std::array<float, 4> vp = ps.viewport.viewport();
        const QSize fullSize(int(vp.at(2)), int(vp.at(3)));
        const QSize targetSize = (fullSize / qreal(scaleDivisor)).expandedTo(QSize(1, 1));
        const bool multiView = viewCount >= 2;
        const int wantArraySize = multiView ? viewCount : 0;

        offscreenTexture = data.getRenderResult(QSSGRenderResult::Key::SkyMaterialBackgroundTexture);
        QSSGRhiRenderableTexture *tex = offscreenTexture;
        if (!tex->texture || tex->texture->pixelSize() != targetSize || tex->texture->arraySize() != wantArraySize) {
            tex->reset();
            tex->texture = multiView ? rhi->newTextureArray(QRhiTexture::RGBA16F, viewCount, targetSize, 1, QRhiTexture::RenderTarget)
                                     : rhi->newTexture(QRhiTexture::RGBA16F, targetSize, 1, QRhiTexture::RenderTarget);
            if (!tex->texture->create()) {
                qWarning("Failed to build SkyMaterial screen-space background texture");
                tex->reset();
                offscreenTexture = nullptr;
                return;
            }
            QRhiColorAttachment att(tex->texture);
            att.setMultiViewCount(viewCount);
            QRhiTextureRenderTargetDescription desc;
            desc.setColorAttachments({ att });
            tex->rt = rhi->newTextureRenderTarget(desc);
            tex->rt->setName(QByteArrayLiteral("SkyMaterial screen-space background"));
            tex->rpDesc = tex->rt->newCompatibleRenderPassDescriptor();
            tex->rt->setRenderPassDescriptor(tex->rpDesc);
            if (!tex->rt->create()) {
                qWarning("Failed to build SkyMaterial screen-space background render target");
                tex->reset();
                offscreenTexture = nullptr;
                return;
            }
        }

        QSSGRhiGraphicsPipelineState offscreenPs;
        offscreenPs.viewport = QRhiViewport(0, 0, float(targetSize.width()), float(targetSize.height()));
        offscreenPs.samples = 1;
        offscreenPs.viewCount = viewCount;
        offscreenPs.polygonMode = QRhiGraphicsPipeline::Fill;
        QSSGRhiGraphicsPipelineStatePrivate::setShaderPipeline(offscreenPs, pipeline.get());
        renderer.rhiQuadRenderer()->recordRenderQuadPass(rhiCtx.get(), &offscreenPs, backgroundSrb,
                                                         offscreenTexture->rt, QSSGRhiQuadRenderer::RenderBehind);
    }

    ready = true;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1352, as _ZN25SkyMaterialBackgroundPass13resetForFrameEv
inline void SkyMaterialBackgroundPass::resetForFrame()
{
    ps = {};
    layer = nullptr;
    ready = false;
    scaleDivisor = 1;
    pipeline = nullptr;
    backgroundSrb = nullptr;
    offscreenTexture = nullptr;
}
//  -----------------------------------------------------------------------

//  void SkyMaterialBackgroundPass::renderPrep(QSSGRenderer &renderer,
//      QSSGLayerRenderData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN25SkyMaterialBackgroundPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData(
    SkyMaterialBackgroundPass *self,
    QSSGRenderer *renderer,
    QSSGLayerRenderData *data) {
  self->renderPrep(*renderer, *data);
}

//  Type SkyMaterialBackgroundPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK25SkyMaterialBackgroundPass8passTypeEv(
    const SkyMaterialBackgroundPass *self) {
  return self->passType();
}

//  void SkyMaterialBackgroundPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN25SkyMaterialBackgroundPass13resetForFrameEv(
    SkyMaterialBackgroundPass *self) {
  self->resetForFrame();
}

//  SkyMaterialBackgroundPass::~SkyMaterialBackgroundPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN25SkyMaterialBackgroundPassD1Ev(
    SkyMaterialBackgroundPass *self) {
  delete self;
}
