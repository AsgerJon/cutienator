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
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderhelpers_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qbitarray.h>
#include <cmath>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlight_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicustommaterialsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderlayer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercamera_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskeleton_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderjoint_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendermorphtarget_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderparticles_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderbuffermanager_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/private/qssgperframeallocator_p.h>
#include <QtQuick3DRuntimeRender/private/qssgruntimerenderlogging_p.h>
#include <QtQuick3DRuntimeRender/private/qssglightmapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgdebugdrawsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssgshadermaterialadapter_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtCore/qspan.h>
#include <array>
#include <QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1126, as _ZN10SkyboxPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData
inline void SkyboxPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData &data)
{
    if (!skipPrep) {
        const auto &rhiCtx = renderer.contextInterface()->rhiContext();
        QSSG_ASSERT(rhiCtx->rhi()->isRecordingFrame(), return);
        QSSG_ASSERT(!data.renderedCameras.isEmpty(), return);
        QSSG_ASSERT(data.renderedCameras.count() == data.layer.viewCount, return);
        layer = &data.layer;
        QSSG_ASSERT(layer, return);

        rpDesc = rhiCtx->mainRenderPassDescriptor();
        ps = data.getPipelineState();
        ps.samples = rhiCtx->mainPassSampleCount();
        ps.viewCount = data.layer.viewCount;
        ps.polygonMode = QRhiGraphicsPipeline::Fill;

        // When there are effects, then it is up to the last pass of the
        // last effect to perform tonemapping, neither the skybox nor the
        // main render pass should alter the colors then.
        skipTonemapping = layer->firstEffect != nullptr;

        RenderHelpers::rhiPrepareSkyBox(*renderer.contextInterface(), this, *layer, data.renderedCameras, renderer);
        skipPrep = true;
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 2107, as _ZN13RenderHelpers23rhiPrepareScreenTextureEP14QSSGRhiContextRK5QSizebP24QSSGRhiRenderableTextureh
inline bool RenderHelpers::rhiPrepareScreenTexture(QSSGRhiContext *rhiCtx,
                                            const QSize &size,
                                            bool wantsMips,
                                            QSSGRhiRenderableTexture *renderableTex,
                                            quint8 viewCount)
{
    QRhi *rhi = rhiCtx->rhi();
    bool needsBuild = false;
    QRhiTexture::Flags flags = QRhiTexture::RenderTarget;
    if (wantsMips)
        flags |= QRhiTexture::MipMapped | QRhiTexture::UsedWithGenerateMips;

    if (!renderableTex->texture) {
        // always non-msaa, even if multisampling is used in the main pass
        if (viewCount <= 1)
            renderableTex->texture = rhi->newTexture(QRhiTexture::RGBA8, size, 1, flags);
        else
            renderableTex->texture = rhi->newTextureArray(QRhiTexture::RGBA8, viewCount, size, 1, flags);
        needsBuild = true;
    } else if (renderableTex->texture->pixelSize() != size) {
        renderableTex->texture->setPixelSize(size);
        needsBuild = true;
    }

    if (!renderableTex->depthStencil && !renderableTex->depthTexture) {
        if (viewCount <= 1)
            renderableTex->depthStencil = rhi->newRenderBuffer(QRhiRenderBuffer::DepthStencil, size);
        else
            renderableTex->depthTexture = rhi->newTextureArray(QRhiTexture::D24S8, viewCount, size, 1, QRhiTexture::RenderTarget);
        needsBuild = true;
    } else {
        if (renderableTex->depthStencil && renderableTex->depthStencil->pixelSize() != size) {
            renderableTex->depthStencil->setPixelSize(size);
            needsBuild = true;
        } else if (renderableTex->depthTexture && renderableTex->depthTexture->pixelSize() != size) {
            renderableTex->depthTexture->setPixelSize(size);
            needsBuild = true;
        }
    }

    if (needsBuild) {
        if (!renderableTex->texture->create()) {
            qWarning("Failed to build screen texture (size %dx%d)", size.width(), size.height());
            renderableTex->reset();
            return false;
        }
        if (renderableTex->depthStencil && !renderableTex->depthStencil->create()) {
            qWarning("Failed to build depth-stencil buffer for screen texture (size %dx%d)",
                     size.width(), size.height());
            renderableTex->reset();
            return false;
        } else if (renderableTex->depthTexture && !renderableTex->depthTexture->create()) {
            qWarning("Failed to build depth-stencil texture array (multiview) for screen texture (size %dx%d)",
                     size.width(), size.height());
            renderableTex->reset();
            return false;
        }
        renderableTex->resetRenderTarget();
        QRhiTextureRenderTargetDescription desc;
        QRhiColorAttachment colorAttachment(renderableTex->texture);
        colorAttachment.setMultiViewCount(viewCount);
        desc.setColorAttachments({ colorAttachment });
        if (renderableTex->depthStencil)
            desc.setDepthStencilBuffer(renderableTex->depthStencil);
        else if (renderableTex->depthTexture)
            desc.setDepthTexture(renderableTex->depthTexture);
        renderableTex->rt = rhi->newTextureRenderTarget(desc);
        renderableTex->rt->setName(QByteArrayLiteral("Screen texture"));
        renderableTex->rpDesc = renderableTex->rt->newCompatibleRenderPassDescriptor();
        renderableTex->rt->setRenderPassDescriptor(renderableTex->rpDesc);
        if (!renderableTex->rt->create()) {
            qWarning("Failed to build render target for screen texture");
            renderableTex->reset();
            return false;
        }
    }

    return true;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 52, as _ZN14QSSGRenderPassD2Ev
inline QSSGRenderPass::~QSSGRenderPass()
{

}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1363, as _ZN17SkyboxCubeMapPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData
inline void SkyboxCubeMapPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData &data)
{
    const auto &rhiCtx = renderer.contextInterface()->rhiContext();
    QSSG_ASSERT(rhiCtx->rhi()->isRecordingFrame(), return);
    QSSG_ASSERT(!data.renderedCameras.isEmpty(), return);
    QSSG_ASSERT(data.renderedCameras.count() == data.layer.viewCount, return);
    layer = &data.layer;
    QSSG_ASSERT(layer, return);

    rpDesc = rhiCtx->mainRenderPassDescriptor();
    ps = data.getPipelineState();
    ps.samples = rhiCtx->mainPassSampleCount();
    ps.viewCount = data.layer.viewCount;
    ps.polygonMode = QRhiGraphicsPipeline::Fill;

    QSSGRenderLayer::TonemapMode tonemapMode = skipTonemapping && (layer->tonemapMode != QSSGRenderLayer::TonemapMode::Custom) ?  QSSGRenderLayer::TonemapMode::None : layer->tonemapMode;

    const auto &shaderCache = renderer.contextInterface()->shaderCache();
    skyBoxCubeShader = shaderCache->getBuiltInRhiShaders().getRhiSkyBoxCubeShader(tonemapMode, !data.layer.skyBoxIsSrgb, data.layer.viewCount);

    RenderHelpers::rhiPrepareSkyBox(*renderer.contextInterface(), this, *layer, data.renderedCameras, renderer, uint(tonemapMode));
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssglayerrenderdata.cpp, line 3133, as _ZNK32QSSGLayerRenderPreparationResult17textureDimensionsEv
inline QSize QSSGLayerRenderPreparationResult::textureDimensions() const
{
    const auto size = viewport.size().toSize();
    return QSize(QSSGRendererUtil::nextMultipleOf4(size.width()), QSSGRendererUtil::nextMultipleOf4(size.height()));
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1177, as _ZN10SkyboxPass13resetForFrameEv
inline void SkyboxPass::resetForFrame()
{
    ps = {};
    layer = nullptr;
    skipPrep = false;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1403, as _ZN17SkyboxCubeMapPass13resetForFrameEv
inline void SkyboxCubeMapPass::resetForFrame()
{
    ps = {};
    layer = nullptr;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 849, as _ZN13ScreenMapPass13resetForFrameEv
inline void ScreenMapPass::resetForFrame()
{
    rhiScreenTexture = nullptr;
    if (skyboxPass)
        skyboxPass->resetForFrame();
    if (skyboxCubeMapPass)
        skyboxCubeMapPass->resetForFrame();
    ps = {};
    wantsMips = false;
    clearColor = Qt::transparent;
    shaderFeatures = {};
    sortedOpaqueObjects.clear();
}
//  -----------------------------------------------------------------------

//  Type ScreenMapPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK13ScreenMapPass8passTypeEv(
    const ScreenMapPass *self) {
  return self->passType();
}

//  void ScreenMapPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN13ScreenMapPass13resetForFrameEv(ScreenMapPass *self) {
  self->resetForFrame();
}

//  ScreenMapPass::~ScreenMapPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN13ScreenMapPassD1Ev(ScreenMapPass *self) {
  delete self;
}
