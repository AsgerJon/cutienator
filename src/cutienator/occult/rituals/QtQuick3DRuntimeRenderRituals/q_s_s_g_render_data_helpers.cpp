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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 107, as local:qssgrenderdata.cpp:calcGlobalNodeDataIndexedImpl
template <QSSGRenderDataHelpers::Strategy Strategy>
static bool calcGlobalNodeDataIndexedImpl(QSSGRenderNode *node,
                                          const QSSGRenderNodeVersionType version,
                                          QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms,
                                          QSSGGlobalRenderNodeData::GlobalOpacityStore &globalOpacities)
{
    using DirtyFlag = QSSGRenderNode::DirtyFlag;
    using FlagT = QSSGRenderNode::FlagT;
    constexpr DirtyFlag TransformAndOpacityDirty = DirtyFlag(FlagT(DirtyFlag::TransformDirty) | FlagT(DirtyFlag::OpacityDirty));

    if (Q_UNLIKELY(!node || (node->h.version() != version)))
        return false;

    constexpr bool forcedRebuild = (Strategy == QSSGRenderDataHelpers::Strategy::Initial);
    bool retval = forcedRebuild || node->isDirty(TransformAndOpacityDirty);

    // NOTE 1: Nodes shared across windows will be marked with a stick dirty flag.
    //         Officially this isn't supported, but in practice it can happen so
    //         we try to be nice and try to keep things moving (literally).
    // NOTE 2: We don't change the return value, as that would interfere with the progressive AA.
    const bool alwaysDirty = node->isDirty(DirtyFlag::StickyDirty);

    if (retval || alwaysDirty) {
        const auto idx = node->h.index();

        auto &globalTransform = globalTransforms[idx];
        auto &globalOpacity = globalOpacities[idx];
        globalOpacity = node->localOpacity;
        globalTransform = node->localTransform;

        if (QSSGRenderNode *parent = node->parent) {
            const auto pidx = parent->h.index();
            const auto pOpacity = globalOpacities[pidx];
            globalOpacity *= pOpacity;

            if (parent->type != QSSGRenderGraphObject::Type::Layer) {
                const auto pTransform = globalTransforms[pidx];
                globalTransform = pTransform * node->localTransform;
            }
        }
        // Clear dirty flags (Transform, Opacity, Active, Pickable)
        node->clearDirty(TransformAndOpacityDirty);
    }

    // We always clear dirty in a reasonable manner but if we aren't active
    // there is no reason to tell the universe if we are dirty or not.
    return retval;
}

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 200, as _ZN21QSSGRenderDataHelpers22calcInstanceTransformsEP14QSSGRenderNodetRSt6vectorI10QMatrix4x4SaIS3_EERS2_IN24QSSGGlobalRenderNodeData18InstanceTransformsESaIS8_EE
inline bool QSSGRenderDataHelpers::calcInstanceTransforms(QSSGRenderNode *node,
                                                   const VersionType version,
                                                   QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms,
                                                   QSSGGlobalRenderNodeData::InstanceTransformStore &instanceTransforms)
{
    if (Q_UNLIKELY(!node || (node->h.version() != version)))
        return false;

    constexpr bool retval = true;

    // NOTE: We've already calculated the global states and transforms at this point
    // so if the node isn't active we don't need to do anything.
    // We're also assuming the node list is stored depth first order.
    const auto idx = node->h.index();
    QSSGRenderNode *parent = node->parent;
    if (parent && parent->type != QSSGRenderGraphObject::Type::Layer && node->getLocalState(QSSGRenderNode::LocalState::Active)) {
        const auto pidx = parent->h.index();
        const auto &pGlobalTransform = globalTransforms[pidx];
        QSSGRenderNode *instanceRoot = node->instanceRoot;
        if (instanceRoot == node) {
            instanceTransforms[idx] = { node->localTransform, pGlobalTransform };
        } else if (instanceRoot) {
            auto &[nodeInstanceLocalTransform, nodeInstanceGlobalTransform] = instanceTransforms[idx];
            auto &[instanceRootLocalTransform, instanceRootGlobalTransform] = instanceTransforms[instanceRoot->h.index()];
            nodeInstanceGlobalTransform = instanceRootGlobalTransform;
            //### technically O(n^2) -- we could cache localInstanceTransform if every node in the
            // tree is guaranteed to have the same instance root. That would require an API change.
            nodeInstanceLocalTransform = node->localTransform;
            auto *p = parent;
            while (p) {
                if (p == instanceRoot) {
                    nodeInstanceLocalTransform = instanceRootLocalTransform * nodeInstanceLocalTransform;
                    break;
                }
                nodeInstanceLocalTransform = p->localTransform * nodeInstanceLocalTransform;
                p = p->parent;
            }
        } else {
            // By default, we do magic: translation is applied to the global instance transform,
            // while scale/rotation is local
            QMatrix4x4 globalInstanceTransform = globalTransforms[pidx];
            QMatrix4x4 localInstanceTransform = node->localTransform;
            auto &localInstanceMatrix = *reinterpret_cast<float (*)[4][4]>(localInstanceTransform.data());
            QVector3D localPos{localInstanceMatrix[3][0], localInstanceMatrix[3][1], localInstanceMatrix[3][2]};
            localInstanceMatrix[3][0] = 0;
            localInstanceMatrix[3][1] = 0;
            localInstanceMatrix[3][2] = 0;
            globalInstanceTransform = pGlobalTransform;
            globalInstanceTransform.translate(localPos);
            instanceTransforms[idx] = { localInstanceTransform, globalInstanceTransform };
        }
    } else {
        instanceTransforms[idx] = { node->localTransform, {} };
    }

    return retval;
}

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

//  from ../qtquick3d/src/runtimerender/rendererimpl/qssgrenderdata.cpp, line 662, as _ZN21QSSGRenderDataHelpers27updateGlobalNodeDataIndexedEP14QSSGRenderNodetRSt6vectorI10QMatrix4x4SaIS3_EERS2_IfSaIfEE
inline bool QSSGRenderDataHelpers::updateGlobalNodeDataIndexed(QSSGRenderNode *node, const VersionType version, QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms, QSSGGlobalRenderNodeData::GlobalOpacityStore &globalOpacities)
{
    return calcGlobalNodeDataIndexedImpl<Strategy::Update>(node, version, globalTransforms, globalOpacities);
}
//  -----------------------------------------------------------------------

//  bool QSSGRenderDataHelpers::calcInstanceTransforms(QSSGRenderNode *node,
//      const VersionType version,
//      QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms,
//      QSSGGlobalRenderNodeData::InstanceTransformStore &instanceTransforms)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderDataHelpers22calcInstanceTransformsEP14QSSGRenderNodetRSt6vectorI10QMatrix4x4SaIS3_EERS2_IN24QSSGGlobalRenderNodeData18InstanceTransformsESaIS8_EE(
    QSSGRenderNode *node,
    QSSGRenderDataHelpers::VersionType version,
    QSSGGlobalRenderNodeData::GlobalTransformStore *globalTransforms,
    QSSGGlobalRenderNodeData::InstanceTransformStore *instanceTransforms) {
  return QSSGRenderDataHelpers::calcInstanceTransforms(
      node,
      version,
      *globalTransforms,
      *instanceTransforms);
}

//  GlobalStateResult
//      QSSGRenderDataHelpers::updateGlobalNodeState(QSSGRenderNode *node,
//      const VersionType version)
extern "C" Q_DECL_EXPORT
QSSGRenderDataHelpers::GlobalStateResult ritual_ZN21QSSGRenderDataHelpers21updateGlobalNodeStateEP14QSSGRenderNodet(
    QSSGRenderNode *node,
    QSSGRenderDataHelpers::VersionType version) {
  return QSSGRenderDataHelpers::updateGlobalNodeState(node, version);
}

//  bool QSSGRenderDataHelpers::updateGlobalNodeDataIndexed(QSSGRenderNode
//      *node, const VersionType version,
//      QSSGGlobalRenderNodeData::GlobalTransformStore &globalTransforms,
//      QSSGGlobalRenderNodeData::GlobalOpacityStore &globalOpacities)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSSGRenderDataHelpers27updateGlobalNodeDataIndexedEP14QSSGRenderNodetRSt6vectorI10QMatrix4x4SaIS3_EERS2_IfSaIfEE(
    QSSGRenderNode *node,
    QSSGRenderDataHelpers::VersionType version,
    QSSGGlobalRenderNodeData::GlobalTransformStore *globalTransforms,
    QSSGGlobalRenderNodeData::GlobalOpacityStore *globalOpacities) {
  return QSSGRenderDataHelpers::updateGlobalNodeDataIndexed(
      node,
      version,
      *globalTransforms,
      *globalOpacities);
}

//  QSSGRenderDataHelpers::~QSSGRenderDataHelpers()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSSGRenderDataHelpersD1Ev(QSSGRenderDataHelpers *self) {
  delete self;
}
