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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 52, as _ZN14QSSGRenderPassD2Ev
inline QSSGRenderPass::~QSSGRenderPass()
{

}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 258, as _ZN17ReflectionMapPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData
inline void ReflectionMapPass::renderPrep(QSSGRenderer &renderer, QSSGLayerRenderData &data)
{
    Q_UNUSED(renderer);
    Q_UNUSED(data);

    QSSG_ASSERT(!data.renderedCameras.isEmpty(), return);
    QSSGRenderCamera *camera = data.renderedCameras[0];

    ps = data.getPipelineState();
    ps.flags |= { QSSGRhiGraphicsPipelineState::Flag::DepthTestEnabled,
                  QSSGRhiGraphicsPipelineState::Flag::DepthWriteEnabled,
                  QSSGRhiGraphicsPipelineState::Flag::BlendEnabled };

    QSSG_ASSERT(data.reflectionProbesView.size() != 0, return);

    reflectionProbes = { data.reflectionProbesView.begin(), data.reflectionProbesView.end() };
    reflectionMapManager = data.requestReflectionMapManager();

    const auto &sortedOpaqueObjects = data.getSortedOpaqueRenderableObjects(*camera);
    const auto &sortedTransparentObjects = data.getSortedTransparentRenderableObjects(*camera);
    QSSGRenderableObjectList emptyList{};
    const auto &sortedScreenTextureObjects = m_includeSTO ? data.getSortedScreenTextureRenderableObjects(*camera) : emptyList;

    QSSG_ASSERT(reflectionPassObjects.isEmpty(), reflectionPassObjects.clear());

    // NOTE: We should consider keeping track of the reflection casting objects to avoid
    // filtering this list on each prep.
    for (const auto &handles : { &sortedOpaqueObjects, &sortedTransparentObjects, &sortedScreenTextureObjects }) {
        for (const auto &handle : *handles) {
            if (handle.obj->renderableFlags.testFlag(QSSGRenderableObjectFlag::CastsReflections))
                reflectionPassObjects.push_back(handle);
        }
    }
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 326, as _ZN17ReflectionMapPass13resetForFrameEv
inline void ReflectionMapPass::resetForFrame()
{
    ps = {};
    reflectionProbes.clear();
    reflectionPassObjects.clear();
}
//  -----------------------------------------------------------------------

//  void ReflectionMapPass::renderPrep(QSSGRenderer &renderer,
//      QSSGLayerRenderData &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17ReflectionMapPass10renderPrepER12QSSGRendererR19QSSGLayerRenderData(
    ReflectionMapPass *self,
    QSSGRenderer *renderer,
    QSSGLayerRenderData *data) {
  self->renderPrep(*renderer, *data);
}

//  Type ReflectionMapPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK17ReflectionMapPass8passTypeEv(
    const ReflectionMapPass *self) {
  return self->passType();
}

//  void ReflectionMapPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ReflectionMapPass13resetForFrameEv(ReflectionMapPass *self) {
  self->resetForFrame();
}

//  ReflectionMapPass::~ReflectionMapPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN17ReflectionMapPassD1Ev(ReflectionMapPass *self) {
  delete self;
}
