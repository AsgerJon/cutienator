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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 863, as _ZN20ScreenReflectionPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData
inline void ScreenReflectionPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData &data)
{
    QSSG_ASSERT(!data.renderedCameras.isEmpty(), return);
    QSSGRenderCamera *camera = data.renderedCameras[0];

    const auto &rhiCtx = renderer.contextInterface()->rhiContext();
    QSSG_ASSERT(rhiCtx->rhi()->isRecordingFrame(), return);
    rhiScreenTexture = data.getRenderResult(QSSGRenderResult::Key::ScreenTexture);
    QSSG_ASSERT_X(rhiScreenTexture && rhiScreenTexture->isValid(), "Invalid screen texture!", return);

    const auto &layer = data.layer;
    const auto shaderFeatures = data.getShaderFeatures();
    const bool layerEnableDepthTest = layer.layerFlags.testFlag(QSSGRenderLayer::LayerFlag::EnableDepthTest);

    QRhiRenderPassDescriptor *mainRpDesc = rhiCtx->mainRenderPassDescriptor();
    const int samples = rhiCtx->mainPassSampleCount();
    const int viewCount = data.layer.viewCount;

    // NOTE: We're piggybacking on the screen map pass for now, but we could do better.
    ps = data.getPipelineState();
    const bool depthTestEnabled = (data.screenMapPass.ps.flags.testFlag(QSSGRhiGraphicsPipelineState::Flag::DepthTestEnabled));
    ps.flags.setFlag(QSSGRhiGraphicsPipelineState::Flag::DepthTestEnabled, depthTestEnabled);
    const bool depthWriteEnabled = (data.screenMapPass.ps.flags.testFlag(QSSGRhiGraphicsPipelineState::Flag::DepthWriteEnabled));
    ps.flags.setFlag(QSSGRhiGraphicsPipelineState::Flag::DepthWriteEnabled, depthWriteEnabled);
    sortedScreenTextureObjects = data.getSortedScreenTextureRenderableObjects(*camera);
    for (const auto &handle : std::as_const(sortedScreenTextureObjects)) {
        QSSGRenderableObject *theObject = handle.obj;
        const auto depthWriteMode = theObject->depthWriteMode;
        ps.flags.setFlag(QSSGRhiGraphicsPipelineState::Flag::BlendEnabled, theObject->renderableFlags.hasTransparency());
        const bool curDepthWriteEnabled = !(depthWriteMode == QSSGDepthDrawMode::Never || depthWriteMode == QSSGDepthDrawMode::OpaquePrePass
                                     || data.isZPrePassActive() || !layerEnableDepthTest);
        ps.flags.setFlag(QSSGRhiGraphicsPipelineState::Flag::DepthWriteEnabled, curDepthWriteEnabled);
        RenderHelpers::rhiPrepareRenderable(rhiCtx.get(), this, data, *theObject, mainRpDesc, &ps, shaderFeatures, samples, viewCount);
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 921, as _ZN20ScreenReflectionPass13resetForFrameEv
inline void ScreenReflectionPass::resetForFrame()
{
    sortedScreenTextureObjects.clear();
    rhiScreenTexture = nullptr;
    ps = {};
}
//  -----------------------------------------------------------------------

//  void ScreenReflectionPass::renderPrep(QSSGRenderer &renderer,
//      QSSGLayerRenderData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN20ScreenReflectionPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData(
    ScreenReflectionPass *self,
    QSSGRenderer *renderer,
    QSSGLayerRenderData *data) {
  self->renderPrep(*renderer, *data);
}

//  Type ScreenReflectionPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK20ScreenReflectionPass8passTypeEv(
    const ScreenReflectionPass *self) {
  return self->passType();
}

//  void ScreenReflectionPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN20ScreenReflectionPass13resetForFrameEv(
    ScreenReflectionPass *self) {
  self->resetForFrame();
}

//  ScreenReflectionPass::~ScreenReflectionPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN20ScreenReflectionPassD1Ev(ScreenReflectionPass *self) {
  delete self;
}
