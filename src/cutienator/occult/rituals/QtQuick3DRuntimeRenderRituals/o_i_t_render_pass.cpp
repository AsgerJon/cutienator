//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrendercontextcore.h>
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 2022, as _ZNK13OITRenderPass8passTypeEv
inline QSSGRenderPass::Type OITRenderPass::passType() const
{
    if (method == QSSGRenderLayer::OITMethod::WeightedBlended)
        return Type::Standalone;
    return Type::Main;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 2030, as _ZN13OITRenderPass13resetForFrameEv
inline void OITRenderPass::resetForFrame()
{
    sortedTransparentObjects.clear();
    ps = {};
    shaderFeatures = {};
    rhiAccumTexture = nullptr;
    rhiRevealageTexture = nullptr;
    rhiDepthTexture = nullptr;
    rhiCounterImage = nullptr;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1657, as _ZN13OITRenderPass24linkedListRequiresResizeE5QSize
inline bool OITRenderPass::linkedListRequiresResize(QSize dim)
{
    quint32 reported = reportedNodeCount;
    quint32 current = currentNodeCount;
    quint32 fullCount = dim.width() * dim.height();

    // resize if reported is greater than current or if there are less than 50% of screen size nodes free
    if (reported > current)
        return true;
    quint32 freeCount = current - reported;
    if (freeCount < fullCount / 2)
        return true;
    // resize if we have more than 100% screen size free nodes
    if (freeCount > fullCount)
        return true;
    return false;
}
//  -----------------------------------------------------------------------

//  Type OITRenderPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK13OITRenderPass8passTypeEv(
    const OITRenderPass *self) {
  return self->passType();
}

//  void OITRenderPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN13OITRenderPass13resetForFrameEv(OITRenderPass *self) {
  self->resetForFrame();
}

//  void OITRenderPass::setMethod(QSSGRenderLayer::OITMethod m)
extern "C" Q_DECL_EXPORT
void ritual_ZN13OITRenderPass9setMethodEN15QSSGRenderLayer9OITMethodE(
    OITRenderPass *self,
    QSSGRenderLayer::OITMethod m) {
  self->setMethod(m);
}

//  bool OITRenderPass::linkedListRequiresResize(QSize dim)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13OITRenderPass24linkedListRequiresResizeE5QSize(
    OITRenderPass *self,
    const QSize *dim) {
  return self->linkedListRequiresResize(*dim);
}

//  OITRenderPass::~OITRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN13OITRenderPassD1Ev(OITRenderPass *self) {
  delete self;
}
