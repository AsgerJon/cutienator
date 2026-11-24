//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qssgrenderpass_p.h"
#include "qssgrhiquadrenderer_p.h"
#include "qssglayerrenderdata_p.h"
#include "qssgdebugdrawsystem_p.h"
#include "qssgrenderhelpers_p.h"
#include "qssgrendercommands_p.h"
#include <QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 2169, as _ZN16OITCompositePass13resetForFrameEv
inline void OITCompositePass::resetForFrame()
{
    ps = {};
    shaderFeatures = {};
    rhiAccumTexture = nullptr;
    rhiRevealageTexture = nullptr;
}
//  -----------------------------------------------------------------------

//  Type OITCompositePass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK16OITCompositePass8passTypeEv(
    const OITCompositePass *self) {
  return self->passType();
}

//  void OITCompositePass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN16OITCompositePass13resetForFrameEv(OITCompositePass *self) {
  self->resetForFrame();
}

//  void OITCompositePass::setMethod(QSSGRenderLayer::OITMethod m)
extern "C" Q_DECL_EXPORT
void ritual_ZN16OITCompositePass9setMethodEN15QSSGRenderLayer9OITMethodE(
    OITCompositePass *self,
    QSSGRenderLayer::OITMethod m) {
  self->setMethod(m);
}

//  OITCompositePass::~OITCompositePass()
extern "C" Q_DECL_EXPORT
void ritual_ZN16OITCompositePassD1Ev(OITCompositePass *self) {
  delete self;
}
