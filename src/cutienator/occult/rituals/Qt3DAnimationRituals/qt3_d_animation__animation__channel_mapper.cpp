//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/channelmapper_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/channelmapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/Qt3DCore>
#include <QtCore/QVector>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/channelmapper_p.h>
#include <Qt3DAnimation/qchannelmapper.h>
#include <Qt3DAnimation/qchannelmapping.h>
#include <Qt3DAnimation/private/qchannelmapper_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <algorithm>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/loadanimationclipjob_p.h>
#include <Qt3DAnimation/private/findrunningclipanimatorsjob_p.h>
#include <Qt3DAnimation/private/evaluateclipanimatorjob_p.h>
#include <Qt3DAnimation/private/buildblendtreesjob_p.h>
#include <Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/buildblendtreesjob_p.h>
#include <Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/vector_helper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapper.cpp, line 33, as _ZN13Qt3DAnimation9Animation13ChannelMapper16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void ChannelMapper::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QChannelMapper *node = qobject_cast<const QChannelMapper *>(frontEnd);
    if (!node)
        return;

    auto ids = Qt3DCore::qIdsForNodes(node->mappings());
    std::sort(std::begin(ids), std::end(ids));
    m_isDirty = firstTime;
    if (m_mappingIds != ids) {
        m_mappingIds = ids;
        setDirty(Handler::ChannelMappingsDirty);
        m_isDirty = true;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    Q_UNUSED(firstTime);

    d_ptr->setEnabled(frontEnd->isEnabled());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 28, as _ZN13Qt3DAnimation9Animation11BackendNode8setDirtyENS0_7Handler9DirtyFlagE
namespace Qt3DAnimation::Animation {
inline void BackendNode::setDirty(Handler::DirtyFlag flag)
{
    Q_ASSERT(m_handler);
    m_handler->setDirty(flag, peerId());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 45, as _ZN13Qt3DAnimation9Animation7Handler8setDirtyENS1_9DirtyFlagEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void Handler::setDirty(DirtyFlag flag, Qt3DCore::QNodeId nodeId)
{
    switch (flag) {
    case AnimationClipDirty: {
        QMutexLocker lock(&m_mutex);
        const auto handle = m_animationClipLoaderManager->lookupHandle(nodeId);
        if (!m_dirtyAnimationClips.contains(handle))
            m_dirtyAnimationClips.push_back(handle);
        break;
    }

    case ChannelMappingsDirty: {
        break;
    }

    case ClipAnimatorDirty: {
        QMutexLocker lock(&m_mutex);
        const auto handle = m_clipAnimatorManager->lookupHandle(nodeId);
        if (!m_dirtyClipAnimators.contains(handle))
            m_dirtyClipAnimators.push_back(handle);
        break;
    }

    case BlendedClipAnimatorDirty: {
        QMutexLocker lock(&m_mutex);
        const HBlendedClipAnimator handle = m_blendedClipAnimatorManager->lookupHandle(nodeId);
        if (!m_dirtyBlendedAnimators.contains(handle))
            m_dirtyBlendedAnimators.push_back(handle);
        break;
    }
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapper.cpp, line 25, as _ZN13Qt3DAnimation9Animation13ChannelMapper7cleanupEv
namespace Qt3DAnimation::Animation {
inline void ChannelMapper::cleanup()
{
    setEnabled(false);
    m_mappingIds.clear();
    m_mappings.clear();
    m_isDirty = true;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/channelmapper.cpp, line 50, as _ZNK13Qt3DAnimation9Animation13ChannelMapper14updateMappingsEv
namespace Qt3DAnimation::Animation {
inline void ChannelMapper::updateMappings() const
{
    m_mappings.clear();
    m_mappings.reserve(m_mappingIds.size());
    const auto mappingManager = m_handler->channelMappingManager();
    for (const auto &mappingId : m_mappingIds) {
        const auto mapping = mappingManager->lookupResource(mappingId);
        Q_ASSERT(mapping);
        m_mappings.push_back(mapping);
    }
    m_isDirty = false;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  void Qt3DAnimation::Animation::ChannelMapper::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ChannelMapper7cleanupEv(
    Qt3DAnimation::Animation::ChannelMapper *self) {
  self->cleanup();
}

//  void Qt3DAnimation::Animation::ChannelMapper::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ChannelMapper16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ChannelMapper *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DAnimation::Animation::ChannelMapper::setMappingIds(const
//      Qt3DCore::QNodeIdVector &mappingIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13ChannelMapper13setMappingIdsERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DAnimation::Animation::ChannelMapper *self,
    const Qt3DCore::QNodeIdVector *mappingIds) {
  self->setMappingIds(*mappingIds);
}

//  Qt3DCore::QNodeIdVector
//      Qt3DAnimation::Animation::ChannelMapper::mappingIds() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdVector *ritual_ZNK13Qt3DAnimation9Animation13ChannelMapper10mappingIdsEv(
    const Qt3DAnimation::Animation::ChannelMapper *self) {
  return new Qt3DCore::QNodeIdVector(self->mappingIds());
}

//  QVector<ChannelMapping *>
//      Qt3DAnimation::Animation::ChannelMapper::mappings() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DAnimation::Animation::ChannelMapping *> *ritual_ZNK13Qt3DAnimation9Animation13ChannelMapper8mappingsEv(
    const Qt3DAnimation::Animation::ChannelMapper *self) {
  return new QVector<Qt3DAnimation::Animation::ChannelMapping *>(
      self->mappings());
}

//  void Qt3DAnimation::Animation::ChannelMapper::updateMappings() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13Qt3DAnimation9Animation13ChannelMapper14updateMappingsEv(
    const Qt3DAnimation::Animation::ChannelMapper *self) {
  self->updateMappings();
}

//  void Qt3DAnimation::Animation::ChannelMapper::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation13ChannelMapper16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::ChannelMapper *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::ChannelMapper::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a Qt3DCore::QNodeIdVector a ritual of
//      Qt3DAnimation::Animation::ChannelMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ChannelMapper__Qt3DCore_QNodeIdVector(
    Qt3DCore::QNodeIdVector *self) {
  delete self;
}

//  a QVector<Qt3DAnimation::Animation::ChannelMapping *> a ritual of
//      Qt3DAnimation::Animation::ChannelMapper gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_ChannelMapper__QVector_Qt3DAnimation_Animation_ChannelMapping(
    QVector<Qt3DAnimation::Animation::ChannelMapping *> *self) {
  delete self;
}
