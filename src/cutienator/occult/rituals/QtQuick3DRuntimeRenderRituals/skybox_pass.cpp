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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 32, as local:qssgrenderhelpers.cpp:RENDERER_VISIBILITY_ALL
static const QRhiShaderResourceBinding::StageFlags RENDERER_VISIBILITY_ALL =
        QRhiShaderResourceBinding::VertexStage | QRhiShaderResourceBinding::FragmentStage;

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 2251, as local:qssgrenderhelpers.cpp:rhiPrepareSkyBox_helper
static void rhiPrepareSkyBox_helper(const QSSGRenderContextInterface &context,
                                    QSSGPassKey passKey,
                                    QSSGRenderLayer &layer,
                                    QSSGRenderCameraList &cameras,
                                    QSSGRenderer &renderer,
                                    QSSGReflectionMapEntry *entry = nullptr,
                                    QSSGRenderTextureCubeFace cubeFace = QSSGRenderTextureCubeFaceNone,
                                    uint tonemapMode = 0)
{
    QSSG_ASSERT(layer.renderData, return);

    const auto *renderData = layer.renderData;

    auto rhiCtx = context.rhiContext().get();

    QSSGRhiContextPrivate *rhiCtxD = QSSGRhiContextPrivate::get(rhiCtx);

    QSSGRenderImageTexture lightProbeTexture;
    switch (layer.background) {
    case QSSGRenderLayer::Background::SkyBox:
        lightProbeTexture = renderer.contextInterface()->bufferManager()->loadRenderImage(layer.lightProbe,
                                                                                          QSSGBufferManager::MipModeBsdf);
        break;
    case QSSGRenderLayer::Background::SkyBoxCubeMap:
        lightProbeTexture = renderer.contextInterface()->bufferManager()->loadRenderImage(layer.skyBoxCubeMap,
                                                                                          QSSGBufferManager::MipModeDisable);
        break;
    case QSSGRenderLayer::Background::SkyMaterial:
        lightProbeTexture = renderData->skyMaterialTexture;
        break;
    default:
        Q_UNREACHABLE_RETURN();
    }

    if (lightProbeTexture.m_texture == nullptr) {
        // No valid texture this frame; drop any previously built SRB rather than
        // reuse one that may reference a texture ensureTextures() has since deleted.
        if (cubeFace != QSSGRenderTextureCubeFaceNone) {
            // All 6 face SRBs bind the same light probe texture, so all of them (not
            // just the face passed in this call) are equally stale.
            for (QRhiShaderResourceBindings *&srb : entry->m_skyBoxSrbs)
                srb = nullptr;
        } else {
            layer.skyBoxSrb = nullptr;
        }
        return;
    }

    const bool cubeMapMode = layer.background == QSSGRenderLayer::Background::SkyBoxCubeMap;

    if (cubeFace == QSSGRenderTextureCubeFaceNone)
        layer.skyBoxIsRgbe8 = lightProbeTexture.m_flags.isRgbe8();
    if (cubeMapMode)
        layer.skyBoxIsSrgb = !lightProbeTexture.m_flags.isLinear();

    QSSGRhiShaderResourceBindingList bindings;

    QRhiSampler *sampler = rhiCtx->sampler({ QRhiSampler::Linear,
                                             QRhiSampler::Linear,
                                             cubeMapMode ? QRhiSampler::None : QRhiSampler::Linear, // cube map doesn't have mipmaps
                                             QRhiSampler::Repeat,
                                             QRhiSampler::ClampToEdge,
                                             QRhiSampler::Repeat });
    int samplerBinding = 1; // the shader code is hand-written, so we don't need to look that up
    bindings.addTexture(samplerBinding, QRhiShaderResourceBinding::FragmentStage, lightProbeTexture.m_texture, sampler);

    const auto cubeFaceIdx = QSSGBaseTypeHelpers::indexOfCubeFace(cubeFace);
    const quintptr entryIdx = quintptr(cubeFace != QSSGRenderTextureCubeFaceNone) * cubeFaceIdx;
    QSSGRhiDrawCallData &dcd = rhiCtxD->drawCallData({ passKey, nullptr, entry, entryIdx });

    QRhi *rhi = rhiCtx->rhi();
    const quint32 ubufSize = cameras.count() >= 2 ? 416 : 240; // same ubuf layout for both skybox and skyboxcube
    if (!dcd.ubuf || dcd.ubuf->size() != ubufSize) {
        delete dcd.ubuf;
        dcd.ubuf = rhi->newBuffer(QRhiBuffer::Dynamic, QRhiBuffer::UniformBuffer, int(ubufSize));
        dcd.ubuf->create();
    }

    float adjustY = rhi->isYUpInNDC() ? 1.0f : -1.0f;
    const float exposure = layer.lightProbeSettings.probeExposure;
    // orientation
    const QMatrix3x3 &rotationMatrix(layer.lightProbeSettings.probeOrientation);

    // The cubemap shader doesn't use blur or mipmapping, so it uses those for tonemapping and texture color space
    const float blurAmountOrSrgb = cubeMapMode ? layer.skyBoxIsSrgb : layer.skyboxBlurAmount;
    const float maxMipLevelOrTonemapMode = cubeMapMode ? float(tonemapMode) : float(lightProbeTexture.m_mipmapCount - 2);

    const QVector4D skyboxProperties = {
        adjustY,
        exposure,
        blurAmountOrSrgb,
        maxMipLevelOrTonemapMode
    };

    char *ubufData = dcd.ubuf->beginFullDynamicBufferUpdateForCurrentFrame();
    quint32 ubufOffset = 0;
    // skyboxProperties
    memcpy(ubufData + ubufOffset, &skyboxProperties, 16);
    ubufOffset += 16;
    // orientation
    memcpy(ubufData + ubufOffset, rotationMatrix.constData(), 12);
    ubufOffset += 16;
    memcpy(ubufData + ubufOffset, (char *)rotationMatrix.constData() + 12, 12);
    ubufOffset += 16;
    memcpy(ubufData + ubufOffset, (char *)rotationMatrix.constData() + 24, 12);
    ubufOffset += 16;

    for (qsizetype viewIdx = 0; viewIdx < cameras.count(); ++viewIdx) {
        const QMatrix4x4 &inverseProjection = cameras[viewIdx]->projection.inverted();
        const QMatrix4x4 &viewMatrix = renderData->getGlobalTransform(*cameras[viewIdx]);
        QMatrix4x4 viewProjection(Qt::Uninitialized); // For cube mode
        cameras[viewIdx]->calculateViewProjectionWithoutTranslation(viewMatrix, 0.1f, 5.0f, viewProjection);

        quint32 viewDataOffset = ubufOffset;
        memcpy(ubufData + viewDataOffset + viewIdx * 64, viewProjection.constData(), 64);
        viewDataOffset += cameras.count() * 64;
        memcpy(ubufData + viewDataOffset + viewIdx * 64, inverseProjection.constData(), 64);
        viewDataOffset += cameras.count() * 64;
        memcpy(ubufData + viewDataOffset + viewIdx * 48, viewMatrix.constData(), 48);
    }
    dcd.ubuf->endFullDynamicBufferUpdateForCurrentFrame();

    bindings.addUniformBuffer(0, RENDERER_VISIBILITY_ALL, dcd.ubuf);

    if (cubeFace != QSSGRenderTextureCubeFaceNone) {
        const auto cubeFaceIdx = QSSGBaseTypeHelpers::indexOfCubeFace(cubeFace);
        entry->m_skyBoxSrbs[cubeFaceIdx] = rhiCtxD->srb(bindings);
    } else {
        layer.skyBoxSrb = rhiCtxD->srb(bindings);
    }

    if (cubeMapMode)
        renderer.rhiCubeRenderer()->prepareCube(rhiCtx, nullptr);
    else
        renderer.rhiQuadRenderer()->prepareQuad(rhiCtx, nullptr);
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderhelpers.cpp, line 2388, as _ZN13RenderHelpers16rhiPrepareSkyBoxERK26QSSGRenderContextInterfacePvR15QSSGRenderLayerR15QVarLengthArrayIP16QSSGRenderCameraLx2EER12QSSGRendererj
inline void RenderHelpers::rhiPrepareSkyBox(const QSSGRenderContextInterface &context,
                                     QSSGPassKey passKey,
                                     QSSGRenderLayer &layer,
                                     QSSGRenderCameraList &cameras,
                                     QSSGRenderer &renderer,
                                     uint tonemapMode)
{
    auto rhiCtx = context.rhiContext().get();
    QRhiCommandBuffer *cb = rhiCtx->commandBuffer();
    cb->debugMarkBegin(QByteArrayLiteral("Quick3D prepare skybox"));

    rhiPrepareSkyBox_helper(context, passKey, layer, cameras, renderer, nullptr, QSSGRenderTextureCubeFaceNone, tonemapMode);

    cb->debugMarkEnd();
}

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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1177, as _ZN10SkyboxPass13resetForFrameEv
inline void SkyboxPass::resetForFrame()
{
    ps = {};
    layer = nullptr;
    skipPrep = false;
}
//  -----------------------------------------------------------------------

//  void SkyboxPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10SkyboxPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData(
    SkyboxPass *self,
    QSSGRenderer *renderer,
    QSSGLayerRenderData *data) {
  self->renderPrep(*renderer, *data);
}

//  Type SkyboxPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK10SkyboxPass8passTypeEv(
    const SkyboxPass *self) {
  return self->passType();
}

//  void SkyboxPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10SkyboxPass13resetForFrameEv(SkyboxPass *self) {
  self->resetForFrame();
}

//  SkyboxPass::~SkyboxPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN10SkyboxPassD1Ev(SkyboxPass *self) {
  delete self;
}
