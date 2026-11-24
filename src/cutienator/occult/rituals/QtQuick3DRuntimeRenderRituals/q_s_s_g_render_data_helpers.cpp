//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/private/qssgrenderdata_p.h>
#if QT_CONFIG(thread)
#include <QtCore/qthreadpool.h>
#endif
#include <QtCore/qtenvironmentvariables.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <QtQuick/private/qsgrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 156, as _ZN21QSSGRenderDataHelpers21updateGlobalNodeStateEP14QSSGRenderNodet
inline QSSGRenderDataHelpers::GlobalStateResult QSSGRenderDataHelpers::updateGlobalNodeState(QSSGRenderNode *node, const VersionType version)
{
    using LocalState = QSSGRenderNode::LocalState;
    using GlobalState = QSSGRenderNode::GlobalState;
    using DirtyFlag = QSSGRenderNode::DirtyFlag;
    using FlagT = QSSGRenderNode::FlagT;

    constexpr DirtyFlag ClearDirtyMask = DirtyFlag(FlagT(DirtyFlag::ActiveDirty) | FlagT(DirtyFlag::PickableDirty) | FlagT(DirtyFlag::ImportDirty));

    constexpr GlobalStateResult activeChangeFlag[] = { GlobalStateResult::None, GlobalStateResult::ActiveChanged };
    constexpr GlobalStateResult pickableChangeFlag[] = { GlobalStateResult::None, GlobalStateResult::PickableChanged };
    constexpr GlobalStateResult tagChangeFlag[] = { GlobalStateResult::None, GlobalStateResult::TagChanged };

    if (Q_UNLIKELY(!node || (node->h.version() != version)))
        return GlobalStateResult::None;

    const bool activeDirty = node->isDirty(DirtyFlag::ActiveDirty);
    const bool pickableDirty = node->isDirty(DirtyFlag::PickableDirty);
    const bool importedDirty = node->isDirty(DirtyFlag::ImportDirty);
    // There's nothing more to do if the tag is dirty, but we still need to clear the dirty flag.
    const bool tagDirty = node->isDirty(DirtyFlag::TagDirty);
    node->clearDirty(DirtyFlag::TagDirty);

    const bool updateState = activeDirty || pickableDirty || importedDirty;

    if (updateState) {
        const QSSGRenderNode *parent = node->parent;
        const bool hasParent = (parent != nullptr);
        const bool globallyActive = node->getLocalState(LocalState::Active) && (!hasParent || parent->getGlobalState(GlobalState::Active));
        node->flags = globallyActive ? (node->flags | FlagT(GlobalState::Active)) : (node->flags & ~FlagT(GlobalState::Active));
        const bool globallyPickable = node->getLocalState(LocalState::Pickable) || (hasParent && parent->getGlobalState(GlobalState::Pickable));
        node->flags = globallyPickable ? (node->flags | FlagT(GlobalState::Pickable)) : (node->flags & ~FlagT(GlobalState::Pickable));
        const bool globallyImported = node->getLocalState(LocalState::Imported) || (hasParent && parent->getGlobalState(GlobalState::Imported));
        node->flags = globallyImported ? (node->flags | FlagT(GlobalState::Imported)) : (node->flags & ~FlagT(GlobalState::Imported));

        // Clear dirty flags (Active, Pickable, Imported)
        node->clearDirty(ClearDirtyMask);
    }

    return GlobalStateResult(FlagT(activeChangeFlag[activeDirty])
                             | FlagT(pickableChangeFlag[pickableDirty])
                             | FlagT(tagChangeFlag[tagDirty]));
}
//  -----------------------------------------------------------------------

//  GlobalStateResult
//      QSSGRenderDataHelpers::updateGlobalNodeState(QSSGRenderNode *node,
//      const VersionType version)
extern "C" Q_DECL_EXPORT
QSSGRenderDataHelpers::GlobalStateResult ritual_ZN21QSSGRenderDataHelpers21updateGlobalNodeStateEP14QSSGRenderNodet(
    QSSGRenderNode *node,
    QSSGRenderDataHelpers::VersionType version) {
  return QSSGRenderDataHelpers::updateGlobalNodeState(node, version);
}

//  QSSGRenderDataHelpers::~QSSGRenderDataHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderDataHelpersD1Ev(QSSGRenderDataHelpers *self) {
  delete self;
}
