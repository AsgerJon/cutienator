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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderpass.cpp, line 1635, as _ZN17UserExtensionPass13resetForFrameEv
inline void UserExtensionPass::resetForFrame()
{
    for (const auto &p : std::as_const(extensions))
        p->resetForFrame();

    // TODO: We should track if we need to update this list.
    extensions.clear();
}
//  -----------------------------------------------------------------------

//  Type UserExtensionPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK17UserExtensionPass8passTypeEv(
    const UserExtensionPass *self) {
  return self->passType();
}

//  void UserExtensionPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN17UserExtensionPass13resetForFrameEv(UserExtensionPass *self) {
  self->resetForFrame();
}

//  bool UserExtensionPass::hasData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17UserExtensionPass7hasDataEv(const UserExtensionPass *self) {
  return self->hasData();
}

//  UserExtensionPass::~UserExtensionPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN17UserExtensionPassD1Ev(UserExtensionPass *self) {
  delete self;
}
