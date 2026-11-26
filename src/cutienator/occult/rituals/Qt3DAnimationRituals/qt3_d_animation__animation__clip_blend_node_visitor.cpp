//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnodevisitor_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnodevisitor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/private/clipblendnodevisitor_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/managers.cpp, line 31, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipBlendNode *ClipBlendNodeManager::lookupNode(Qt3DCore::QNodeId id) const
{
    return m_nodes.value(id, nullptr);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnodevisitor.cpp, line 20, as _ZN13Qt3DAnimation9Animation20ClipBlendNodeVisitorC1EPNS0_20ClipBlendNodeManagerENS1_14TraversalOrderENS1_10NodeFilterE
namespace Qt3DAnimation::Animation {
inline ClipBlendNodeVisitor::ClipBlendNodeVisitor(ClipBlendNodeManager *manager,
                                           TraversalOrder order,
                                           NodeFilter filter)
    : m_manager(manager)
    , m_order(order)
    , m_filter(filter)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnodevisitor.cpp, line 29, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor8traverseEN8Qt3DCore7QNodeIdERKSt8functionIFvPNS0_13ClipBlendNodeEEE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeVisitor::traverse(Qt3DCore::QNodeId rootId,
                                    const VisitFunction &visitFunction) const
{
    ClipBlendNode *node = m_manager->lookupNode(rootId);
    if (node != nullptr) {
        switch (m_order) {
        case PreOrder: {
            switch (m_filter) {
            case VisitAllNodes:
                visitPreOrderAllNodes(node, visitFunction);
                break;

            case VisitOnlyDependencies:
                visitPreOrderDependencyNodes(node, visitFunction);
                break;
            }

            break;
        }

        case PostOrder: {
            switch (m_filter) {
            case VisitAllNodes:
                visitPostOrderAllNodes(node, visitFunction);
                break;

            case VisitOnlyDependencies:
                visitPostOrderDependencyNodes(node, visitFunction);
                break;
            }

            break;
        }
        }
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnodevisitor.cpp, line 71, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor21visitPreOrderAllNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeVisitor::visitPreOrderAllNodes(ClipBlendNode *node,
                                                 const VisitFunction &visitFunction) const
{
    visitFunction(node);
    const Qt3DCore::QNodeIdVector childIds = node->allDependencyIds();
    for (const Qt3DCore::QNodeId &childId: childIds) {
        ClipBlendNode *childNode = m_manager->lookupNode(childId);
        if (childNode != nullptr)
            visitPreOrderAllNodes(childNode, visitFunction);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnodevisitor.cpp, line 88, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor22visitPostOrderAllNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeVisitor::visitPostOrderAllNodes(ClipBlendNode *node,
                                                  const VisitFunction &visitFunction) const
{
    const Qt3DCore::QNodeIdVector childIds = node->allDependencyIds();
    for (const Qt3DCore::QNodeId &childId: childIds) {
        ClipBlendNode *childNode = m_manager->lookupNode(childId);
        if (childNode != nullptr)
            visitPostOrderAllNodes(childNode, visitFunction);
    }
    visitFunction(node);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnodevisitor.cpp, line 105, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor28visitPreOrderDependencyNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeVisitor::visitPreOrderDependencyNodes(ClipBlendNode *node,
                                                        const VisitFunction &visitFunction) const
{
    visitFunction(node);
    const Qt3DCore::QNodeIdVector childIds = node->currentDependencyIds();
    for (const Qt3DCore::QNodeId &childId: childIds) {
        ClipBlendNode *childNode = m_manager->lookupNode(childId);
        if (childNode != nullptr)
            visitPreOrderDependencyNodes(childNode, visitFunction);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnodevisitor.cpp, line 122, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor29visitPostOrderDependencyNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeVisitor::visitPostOrderDependencyNodes(ClipBlendNode *node,
                                                         const VisitFunction &visitFunction) const
{
    const Qt3DCore::QNodeIdVector childIds = node->currentDependencyIds();
    for (const Qt3DCore::QNodeId &childId: childIds) {
        ClipBlendNode *childNode = m_manager->lookupNode(childId);
        if (childNode != nullptr)
            visitPostOrderDependencyNodes(childNode, visitFunction);
    }
    visitFunction(node);
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::ClipBlendNodeVisitor::ClipBlendNodeVisitor(Clip
//      BlendNodeManager *manager, TraversalOrder order, NodeFilter filter)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendNodeVisitor *ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeVisitorC1EPNS0_20ClipBlendNodeManagerENS1_14TraversalOrderENS1_10NodeFilterE(
    Qt3DAnimation::Animation::ClipBlendNodeManager *manager,
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::TraversalOrder order,
    Qt3DAnimation::Animation::ClipBlendNodeVisitor::NodeFilter filter) {
  return new Qt3DAnimation::Animation::ClipBlendNodeVisitor(
      manager,
      order,
      filter);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeVisitor::traverse(Qt3DCore::Q
//      NodeId rootId, const VisitFunction &visitFunction) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor8traverseEN8Qt3DCore7QNodeIdERKSt8functionIFvPNS0_13ClipBlendNodeEEE(
    const Qt3DAnimation::Animation::ClipBlendNodeVisitor *self,
    const Qt3DCore::QNodeId *rootId,
    const Qt3DAnimation::Animation::VisitFunction *visitFunction) {
  self->traverse(*rootId, *visitFunction);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPreOrderAllNode
//      s(ClipBlendNode *node, const VisitFunction &visitFunction) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor21visitPreOrderAllNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE(
    const Qt3DAnimation::Animation::ClipBlendNodeVisitor *self,
    Qt3DAnimation::Animation::ClipBlendNode *node,
    const Qt3DAnimation::Animation::VisitFunction *visitFunction) {
  self->visitPreOrderAllNodes(node, *visitFunction);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPostOrderAllNod
//      es(ClipBlendNode *node, const VisitFunction &visitFunction) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor22visitPostOrderAllNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE(
    const Qt3DAnimation::Animation::ClipBlendNodeVisitor *self,
    Qt3DAnimation::Animation::ClipBlendNode *node,
    const Qt3DAnimation::Animation::VisitFunction *visitFunction) {
  self->visitPostOrderAllNodes(node, *visitFunction);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPreOrderDepende
//      ncyNodes(ClipBlendNode *node, const VisitFunction &visitFunction)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor28visitPreOrderDependencyNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE(
    const Qt3DAnimation::Animation::ClipBlendNodeVisitor *self,
    Qt3DAnimation::Animation::ClipBlendNode *node,
    const Qt3DAnimation::Animation::VisitFunction *visitFunction) {
  self->visitPreOrderDependencyNodes(node, *visitFunction);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeVisitor::visitPostOrderDepend
//      encyNodes(ClipBlendNode *node, const VisitFunction &visitFunction)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeVisitor29visitPostOrderDependencyNodesEPNS0_13ClipBlendNodeERKSt8functionIFvS3_EE(
    const Qt3DAnimation::Animation::ClipBlendNodeVisitor *self,
    Qt3DAnimation::Animation::ClipBlendNode *node,
    const Qt3DAnimation::Animation::VisitFunction *visitFunction) {
  self->visitPostOrderDependencyNodes(node, *visitFunction);
}

//  Qt3DAnimation::Animation::ClipBlendNodeVisitor::~ClipBlendNodeVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeVisitorD1Ev(
    Qt3DAnimation::Animation::ClipBlendNodeVisitor *self) {
  delete self;
}
