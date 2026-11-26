//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendershadercache_p.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderableobjects_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 928, as _ZN10OpaquePass4prepERK26QSSGRenderContextInterfaceR19QSSGLayerRenderDataPvR28QSSGRhiGraphicsPipelineState18QSSGShaderFeaturesP24QRhiRenderPassDescriptorRK5QListI26QSSGRenderableObjectHandleE
inline void OpaquePass::prep(const QSSGRenderContextInterface &ctx,
                      QSSGLayerRenderData &data,
                      QSSGPassKey passKey,
                      QSSGRhiGraphicsPipelineState &ps,
                      QSSGShaderFeatures shaderFeatures,
                      QRhiRenderPassDescriptor *rpDesc,
                      const QSSGRenderableObjectList &sortedOpaqueObjects)
{
    const auto &rhiCtx = ctx.rhiContext();
    QSSG_ASSERT(rpDesc && rhiCtx->rhi()->isRecordingFrame(), return);

    const auto &layer = data.layer;
    const bool layerEnableDepthTest = layer.layerFlags.testFlag(QSSGRenderLayer::LayerFlag::EnableDepthTest);

    for (const auto &handle : std::as_const(sortedOpaqueObjects)) {
        QSSGRenderableObject *theObject = handle.obj;
        const auto depthWriteMode = theObject->depthWriteMode;
        const bool curDepthWriteEnabled = !(depthWriteMode == QSSGDepthDrawMode::Never ||
                                            depthWriteMode == QSSGDepthDrawMode::OpaquePrePass ||
                                            data.isZPrePassActive() || !layerEnableDepthTest);
        ps.flags.setFlag(QSSGRhiGraphicsPipelineState::Flag::DepthWriteEnabled, curDepthWriteEnabled);
        RenderHelpers::rhiPrepareRenderable(rhiCtx.get(), passKey, data, *theObject, rpDesc, &ps, shaderFeatures, ps.samples, ps.viewCount);
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1004, as _ZN10OpaquePass13resetForFrameEv
inline void OpaquePass::resetForFrame()
{
    sortedOpaqueObjects.clear();
    ps = {};
    shaderFeatures = {};
}
//  -----------------------------------------------------------------------

//  void OpaquePass::prep(const QSSGRenderContextInterface &ctx,
//      QSSGLayerRenderData &data, QSSGPassKey passKey,
//      QSSGRhiGraphicsPipelineState &ps, QSSGShaderFeatures shaderFeatures,
//      QRhiRenderPassDescriptor *rpDesc, const QSSGRenderableObjectList
//      &sortedOpaqueObjects)
extern "C" Q_DECL_EXPORT
void ritual_ZN10OpaquePass4prepERK26QSSGRenderContextInterfaceR19QSSGLayerRenderDataPvR28QSSGRhiGraphicsPipelineState18QSSGShaderFeaturesP24QRhiRenderPassDescriptorRK5QListI26QSSGRenderableObjectHandleE(
    const QSSGRenderContextInterface *ctx,
    QSSGLayerRenderData *data,
    QSSGPassKey passKey,
    QSSGRhiGraphicsPipelineState *ps,
    const QSSGShaderFeatures *shaderFeatures,
    QRhiRenderPassDescriptor *rpDesc,
    const QList<QSSGRenderableObjectHandle> *sortedOpaqueObjects) {
  OpaquePass::prep(
      *ctx,
      *data,
      passKey,
      *ps,
      *shaderFeatures,
      rpDesc,
      *sortedOpaqueObjects);
}

//  Type OpaquePass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK10OpaquePass8passTypeEv(
    const OpaquePass *self) {
  return self->passType();
}

//  void OpaquePass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10OpaquePass13resetForFrameEv(OpaquePass *self) {
  self->resetForFrame();
}

//  OpaquePass::~OpaquePass()
extern "C" Q_DECL_EXPORT
void ritual_ZN10OpaquePassD1Ev(OpaquePass *self) {
  delete self;
}
