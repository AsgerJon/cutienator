//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/managers_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/managers.cpp, line 12, as _ZN13Qt3DAnimation9Animation20ClipBlendNodeManagerC1Ev
namespace Qt3DAnimation::Animation {
inline ClipBlendNodeManager::ClipBlendNodeManager()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/managers.cpp, line 16, as _ZN13Qt3DAnimation9Animation20ClipBlendNodeManagerD1Ev
namespace Qt3DAnimation::Animation {
inline ClipBlendNodeManager::~ClipBlendNodeManager()
{
    qDeleteAll(m_nodes);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/managers.cpp, line 21, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager12containsNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline bool ClipBlendNodeManager::containsNode(Qt3DCore::QNodeId id) const
{
    return m_nodes.contains(id);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/managers.cpp, line 26, as _ZN13Qt3DAnimation9Animation20ClipBlendNodeManager10appendNodeEN8Qt3DCore7QNodeIdEPNS0_13ClipBlendNodeE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeManager::appendNode(Qt3DCore::QNodeId id, ClipBlendNode *node)
{
    m_nodes.insert(id, node);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/managers.cpp, line 31, as _ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipBlendNode *ClipBlendNodeManager::lookupNode(Qt3DCore::QNodeId id) const
{
    return m_nodes.value(id, nullptr);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/managers.cpp, line 36, as _ZN13Qt3DAnimation9Animation20ClipBlendNodeManager11releaseNodeEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNodeManager::releaseNode(Qt3DCore::QNodeId id)
{
    delete m_nodes.take(id);
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::ClipBlendNodeManager::ClipBlendNodeManager()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendNodeManager *ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManagerC1Ev() {
  return new Qt3DAnimation::Animation::ClipBlendNodeManager();
}

//  Qt3DAnimation::Animation::ClipBlendNodeManager::~ClipBlendNodeManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManagerD1Ev(
    Qt3DAnimation::Animation::ClipBlendNodeManager *self) {
  delete self;
}

//  bool Qt3DAnimation::Animation::ClipBlendNodeManager::containsNode(Qt3DCor
//      e::QNodeId id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager12containsNodeEN8Qt3DCore7QNodeIdE(
    const Qt3DAnimation::Animation::ClipBlendNodeManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->containsNode(*id);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeManager::appendNode(Qt3DCore:
//      :QNodeId id, ClipBlendNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManager10appendNodeEN8Qt3DCore7QNodeIdEPNS0_13ClipBlendNodeE(
    Qt3DAnimation::Animation::ClipBlendNodeManager *self,
    const Qt3DCore::QNodeId *id,
    Qt3DAnimation::Animation::ClipBlendNode *node) {
  self->appendNode(*id, node);
}

//  ClipBlendNode *Qt3DAnimation::Animation::ClipBlendNodeManager::lookupNode
//      (Qt3DCore::QNodeId id) const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendNode *ritual_ZNK13Qt3DAnimation9Animation20ClipBlendNodeManager10lookupNodeEN8Qt3DCore7QNodeIdE(
    const Qt3DAnimation::Animation::ClipBlendNodeManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupNode(*id);
}

//  void Qt3DAnimation::Animation::ClipBlendNodeManager::releaseNode(Qt3DCore
//      ::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation20ClipBlendNodeManager11releaseNodeEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipBlendNodeManager *self,
    const Qt3DCore::QNodeId *id) {
  self->releaseNode(*id);
}
