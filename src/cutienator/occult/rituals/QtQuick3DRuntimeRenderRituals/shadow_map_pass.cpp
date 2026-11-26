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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 169, as _ZN13ShadowMapPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData
inline void ShadowMapPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData &data)
{
    Q_UNUSED(renderer)
    using namespace RenderHelpers;

    QSSG_ASSERT(!data.renderedCameras.isEmpty(), return);
    camera = data.renderedCameras[0];

    QSSG_ASSERT(shadowPassObjects.isEmpty(), shadowPassObjects.clear());

    data.getShadowCastingObjects(*camera, shadowPassObjects, castingObjectsBox, receivingObjectsBox);

    globalLights = data.globalLights;
    enabled = !shadowPassObjects.isEmpty() || !globalLights.isEmpty();

    if (enabled) {
        shadowMapManager = data.requestShadowMapManager();

        ps = data.getPipelineState();
        ps.flags |= { QSSGRhiGraphicsPipelineState::Flag::DepthTestEnabled, QSSGRhiGraphicsPipelineState::Flag::DepthWriteEnabled };
        // Try reducing self-shadowing and artifacts.
        ps.depthBias = 2;
        ps.slopeScaledDepthBias = 1.5f;

        if (!debugCamera) {
            debugCamera = std::make_unique<QSSGRenderCamera>(QSSGRenderGraphObject::Type::OrthographicCamera);
        }
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 237, as _ZN13ShadowMapPass13resetForFrameEv
inline void ShadowMapPass::resetForFrame()
{
    enabled = false;
    camera = nullptr;
    castingObjectsBox = {};
    receivingObjectsBox = {};
    ps = {};
    shadowPassObjects.clear();
    globalLights.clear();
}
//  -----------------------------------------------------------------------

//  void ShadowMapPass::renderPrep(QSSGRenderer &renderer,
//      QSSGLayerRenderData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN13ShadowMapPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData(
    ShadowMapPass *self,
    QSSGRenderer *renderer,
    QSSGLayerRenderData *data) {
  self->renderPrep(*renderer, *data);
}

//  Type ShadowMapPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK13ShadowMapPass8passTypeEv(
    const ShadowMapPass *self) {
  return self->passType();
}

//  void ShadowMapPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN13ShadowMapPass13resetForFrameEv(ShadowMapPass *self) {
  self->resetForFrame();
}
