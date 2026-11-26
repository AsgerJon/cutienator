//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationaspect_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationaspect_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/buildblendtreesjob_p.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnodevisitor_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/private/clipblendvalue_p.h>
#include <Qt3DAnimation/private/lerpclipblend_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/private/loadanimationclipjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DAnimation/qanimationcliploader.h>
#include <Qt3DAnimation/private/qanimationcliploader_p.h>
#include <Qt3DAnimation/private/animationclip_p.h>
#include <Qt3DAnimation/private/qabstractanimationclip_p.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
#include <Qt3DAnimation/private/findrunningclipanimatorsjob_p.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/animationutils_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
#include <Qt3DAnimation/private/clipanimator_p.h>
#include <Qt3DAnimation/qclipanimator.h>
#include <Qt3DAnimation/qchannelmapper.h>
#include <Qt3DAnimation/qclock.h>
#include <Qt3DAnimation/private/qclipanimator_p.h>
#include <Qt3DAnimation/private/animationclip_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/animationclip_p.h>
#include <Qt3DAnimation/qanimationclip.h>
#include <Qt3DAnimation/qanimationcliploader.h>
#include <Qt3DAnimation/private/qanimationclip_p.h>
#include <Qt3DAnimation/private/qanimationcliploader_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/gltfimporter_p.h>
#include <Qt3DCore/private/qurlhelper_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qfile.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qurlquery.h>
#include <Qt3DAnimation/private/channelmapper_p.h>
#include <Qt3DAnimation/qchannelmapper.h>
#include <Qt3DAnimation/qchannelmapping.h>
#include <Qt3DAnimation/private/qchannelmapper_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <algorithm>
#include <Qt3DAnimation/private/channelmapping_p.h>
#include <Qt3DAnimation/qchannelmapping.h>
#include <Qt3DAnimation/qskeletonmapping.h>
#include <Qt3DAnimation/qcallbackmapping.h>
#include <Qt3DAnimation/private/qcallbackmapping_p.h>
#include <Qt3DAnimation/private/qchannelmapping_p.h>
#include <Qt3DAnimation/private/qskeletonmapping_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DCore/qabstractskeleton.h>
#include <Qt3DAnimation/private/blendedclipanimator_p.h>
#include <Qt3DAnimation/qblendedclipanimator.h>
#include <Qt3DAnimation/qchannelmapper.h>
#include <Qt3DAnimation/qclock.h>
#include <Qt3DAnimation/qabstractclipblendnode.h>
#include <Qt3DAnimation/private/qblendedclipanimator_p.h>
#include <Qt3DAnimation/private/skeleton_p.h>
#include <Qt3DCore/private/qabstractskeleton_p.h>
#include <Qt3DAnimation/qanimationcliploader.h>
#include <Qt3DAnimation/private/qanimationcliploader_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
#include <Qt3DAnimation/private/qabstractanimationclip_p.h>
#include <Qt3DAnimation/private/clipblendvalue_p.h>
#include <Qt3DAnimation/qclipblendvalue.h>
#include <Qt3DAnimation/private/qclipblendvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/loadanimationclipjob.cpp, line 20, as local:loadanimationclipjob.cpp:LoadAnimationClipJobPrivate
namespace Qt3DAnimation::Animation {
class LoadAnimationClipJobPrivate : public Qt3DCore::QAspectJobPrivate
{
public:
    LoadAnimationClipJobPrivate() { }
    ~LoadAnimationClipJobPrivate() override { }

    void postFrame(Qt3DCore::QAspectManager *manager) override;

    QList<AnimationClip *> m_updatedNodes;
};
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/loadanimationclipjob.cpp, line 69, as local:loadanimationclipjob.cpp:LoadAnimationClipJobPrivate::postFrame
namespace Qt3DAnimation::Animation {
inline void LoadAnimationClipJobPrivate::postFrame(Qt3DCore::QAspectManager *manager)
{
    for (AnimationClip *clip: std::as_const(m_updatedNodes)) {
        QAbstractAnimationClip *node = qobject_cast<QAbstractAnimationClip *>(manager->lookupNode(clip->peerId()));
        if (!node)
            continue;

        QAbstractAnimationClipPrivate *dnode = static_cast<QAbstractAnimationClipPrivate *>(Qt3DCore::QNodePrivate::get(node));
        dnode->setDuration(clip->duration());

        QAnimationClipLoader *loader = qobject_cast<QAnimationClipLoader *>(node);
        if (loader) {
            QAnimationClipLoaderPrivate *dloader = static_cast<QAnimationClipLoaderPrivate *>(dnode);
            dloader->setStatus(clip->status());
        }
    }

    m_updatedNodes.clear();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 22, as _ZN13Qt3DAnimation9Animation7HandlerC1Ev
namespace Qt3DAnimation::Animation {
inline Handler::Handler()
    : m_animationClipLoaderManager(new AnimationClipLoaderManager)
    , m_clockManager(new ClockManager)
    , m_clipAnimatorManager(new ClipAnimatorManager)
    , m_blendedClipAnimatorManager(new BlendedClipAnimatorManager)
    , m_channelMappingManager(new ChannelMappingManager)
    , m_channelMapperManager(new ChannelMapperManager)
    , m_clipBlendNodeManager(new ClipBlendNodeManager)
    , m_skeletonManager(new SkeletonManager)
    , m_loadAnimationClipJob(new LoadAnimationClipJob)
    , m_findRunningClipAnimatorsJob(new FindRunningClipAnimatorsJob)
    , m_buildBlendTreesJob(new BuildBlendTreesJob)
    , m_simulationTime(0)
{
    m_loadAnimationClipJob->setHandler(this);
    m_findRunningClipAnimatorsJob->setHandler(this);
    m_buildBlendTreesJob->setHandler(this);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 41, as _ZN13Qt3DAnimation9Animation7HandlerD1Ev
namespace Qt3DAnimation::Animation {
inline Handler::~Handler()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/buildblendtreesjob.cpp, line 18, as _ZN13Qt3DAnimation9Animation18BuildBlendTreesJobC1Ev
namespace Qt3DAnimation::Animation {
inline BuildBlendTreesJob::BuildBlendTreesJob()
    : Qt3DCore::QAspectJob()
     , m_handler(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::BuildBlendTree, 0)
}
}  // namespace Qt3DAnimation::Animation

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

//  from ../qt3d/src/animation/backend/loadanimationclipjob.cpp, line 31, as _ZN13Qt3DAnimation9Animation20LoadAnimationClipJobC1Ev
namespace Qt3DAnimation::Animation {
inline LoadAnimationClipJob::LoadAnimationClipJob()
    : Qt3DCore::QAspectJob(*new LoadAnimationClipJobPrivate)
    , m_animationClipHandles()
    , m_handler(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::LoadAnimationClip, 0)
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/findrunningclipanimatorsjob.cpp, line 16, as _ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJobC1Ev
namespace Qt3DAnimation::Animation {
inline FindRunningClipAnimatorsJob::FindRunningClipAnimatorsJob()
    : Qt3DCore::QAspectJob()
    , m_handler(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::FindRunningClipAnimator, 0)
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 86, as _ZN13Qt3DAnimation9Animation12ClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QClipAnimator *node = qobject_cast<const QClipAnimator *>(frontEnd);
    if (!node)
        return;

    auto id = Qt3DCore::qIdForNode(node->clip());
    if (m_clipId != id)
        setClipId(id);
    id = Qt3DCore::qIdForNode(node->channelMapper());
    if (m_mapperId != id)
        setMapperId(id);
    id = Qt3DCore::qIdForNode(node->clock());
    if (m_clockId != id)
        setClockId(id);

    if (m_running != node->isRunning())
        setRunning(node->isRunning());
    if (m_loops != node->loopCount())
        m_loops = node->loopCount();
    if (!qFuzzyCompare(m_normalizedLocalTime, node->normalizedTime()))
        setNormalizedLocalTime(node->normalizedTime());

    if (firstTime)
        setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 64, as _ZN13Qt3DAnimation9Animation13AnimationClip16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void AnimationClip::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAbstractAnimationClip *node = qobject_cast<const QAbstractAnimationClip *>(frontEnd);
    if (!node)
        return;

    const QAnimationClip *clipNode = qobject_cast<const QAnimationClip *>(frontEnd);
    if (clipNode) {
        if (firstTime)
            m_dataType = Data;
        Q_ASSERT(m_dataType == Data);
        if (m_clipData != clipNode->clipData()) {
            m_clipData = clipNode->clipData();
            if (m_clipData.isValid())
                setDirty(Handler::AnimationClipDirty);
        }
    }

    const QAnimationClipLoader *loaderNode = qobject_cast<const QAnimationClipLoader *>(frontEnd);
    if (loaderNode) {
        if (firstTime)
            m_dataType = File;
        Q_ASSERT(m_dataType == File);
        if (m_source != loaderNode->source()) {
            m_source = loaderNode->source();
            if (!m_source.isEmpty())
                setDirty(Handler::AnimationClipDirty);
        }
    }
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

//  from ../qt3d/src/animation/backend/channelmapping.cpp, line 46, as _ZN13Qt3DAnimation9Animation14ChannelMapping16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void ChannelMapping::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QAbstractChannelMapping *node = qobject_cast<const QAbstractChannelMapping *>(frontEnd);
    if (!node)
        return;

    const QChannelMapping *channelMapping = qobject_cast<const QChannelMapping *>(frontEnd);
    if (channelMapping) {
        m_mappingType = ChannelMappingType;
        m_channelName = channelMapping->channelName();
        m_targetId = Qt3DCore::qIdForNode(channelMapping->target());

        QChannelMappingPrivate *d = static_cast<QChannelMappingPrivate *>(Qt3DCore::QNodePrivate::get(const_cast<QChannelMapping *>(channelMapping)));
        m_type = d->m_type;
        m_propertyName = d->m_propertyName;
        m_componentCount = d->m_componentCount;
    }

    const QSkeletonMapping *skeletonMapping = qobject_cast<const QSkeletonMapping *>(frontEnd);
    if (skeletonMapping) {
        m_mappingType = SkeletonMappingType;
        m_skeletonId = Qt3DCore::qIdForNode(skeletonMapping->skeleton());
    }

    const QCallbackMapping *callbackMapping = qobject_cast<const QCallbackMapping *>(frontEnd);
    if (callbackMapping) {
        m_mappingType = ChannelMappingType;
        m_channelName = callbackMapping->channelName();

        const QCallbackMappingPrivate *d = static_cast<const QCallbackMappingPrivate *>(Qt3DCore::QNodePrivate::get(callbackMapping));
        m_type = d->m_type;
        m_callback = d->m_callback;
        m_callbackFlags = d->m_callbackFlags;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 104, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);
    const QBlendedClipAnimator *node = qobject_cast<const QBlendedClipAnimator *>(frontEnd);
    if (!node)
        return;

    auto id = Qt3DCore::qIdForNode(node->blendTree());
    if (id != m_blendTreeRootId)
        setBlendTreeRootId(id);
    id = Qt3DCore::qIdForNode(node->channelMapper());
    if (m_mapperId != id)
        setMapperId(id);
    id = Qt3DCore::qIdForNode(node->clock());
    if (m_clockId != id)
        setClockId(id);

    if (m_running != node->isRunning())
        setRunning(node->isRunning());
    if (m_loops != node->loopCount())
        m_loops = node->loopCount();
    if (!qFuzzyCompare(m_normalizedLocalTime, node->normalizedTime()))
        setNormalizedLocalTime(node->normalizedTime());

    if (firstTime)
        setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/skeleton.cpp, line 33, as _ZN13Qt3DAnimation9Animation8Skeleton16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
using namespace Qt3DCore;
inline void Skeleton::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);

    const Qt3DCore::QAbstractSkeleton *node = qobject_cast<const Qt3DCore::QAbstractSkeleton *>(frontEnd);
    if (!node)
        return;

    auto dnode = Qt3DCore::QAbstractSkeletonPrivate::get(node);

    // TODO: Mark joint info as dirty so we can rebuild any indexes used
    // by the animators and channel mappings.
    m_jointNames = dnode->m_jointNames;
    m_jointLocalPoses = dnode->m_localPoses;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/frontend/qanimationcliploader.cpp, line 18, as _ZN13Qt3DAnimation27QAnimationClipLoaderPrivate9setStatusENS_20QAnimationClipLoader6StatusE
namespace Qt3DAnimation {
inline void QAnimationClipLoaderPrivate::setStatus(QAnimationClipLoader::Status status)
{
    Q_Q(QAnimationClipLoader);
    if (status != m_status) {
        m_status = status;
        const bool blocked = q->blockNotifications(true);
        emit q->statusChanged(m_status);
        q->blockNotifications(blocked);
    }
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qabstractanimationclip.cpp, line 17, as _ZN13Qt3DAnimation29QAbstractAnimationClipPrivate11setDurationEf
namespace Qt3DAnimation {
inline void QAbstractAnimationClipPrivate::setDuration(float duration)
{
    if (qFuzzyCompare(duration, m_duration))
        return;

    Q_Q(QAbstractAnimationClip);
    bool wasBlocked = q->blockNotifications(true);
    m_duration = duration;
    emit q->durationChanged(duration);
    q->blockNotifications(wasBlocked);
}
}  // namespace Qt3DAnimation

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

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 51, as _ZN13Qt3DAnimation9Animation12ClipAnimator10setClockIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setClockId(Qt3DCore::QNodeId clockId)
{
    m_clockId = clockId;
    setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 57, as _ZN13Qt3DAnimation9Animation12ClipAnimator10setRunningEb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setRunning(bool running)
{
    m_running = running;
    if (!running)
        m_currentLoop = 0;
    setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 45, as _ZN13Qt3DAnimation9Animation12ClipAnimator11setMapperIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setMapperId(Qt3DCore::QNodeId mapperId)
{
    m_mapperId = mapperId;
    setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 65, as _ZN13Qt3DAnimation9Animation12ClipAnimator22setNormalizedLocalTimeEfb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setNormalizedLocalTime(float normalizedTime, bool allowMarkDirty)
{
    m_normalizedLocalTime = normalizedTime;
    if (isValidNormalizedTime(normalizedTime) && allowMarkDirty)
        setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 34, as _ZN13Qt3DAnimation9Animation12ClipAnimator9setClipIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setClipId(Qt3DCore::QNodeId clipId)
{
    m_clipId = clipId;
    setDirty(Handler::ClipAnimatorDirty);

    // register at the clip to make sure we are marked dirty when the clip finished loading
    AnimationClip *clip = m_handler->animationClipLoaderManager()->lookupResource(clipId);
    if (clip)
        clip->addDependingClipAnimator(peerId());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 79, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setClockIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setClockId(Qt3DCore::QNodeId clockId)
{
    m_clockId = clockId;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 85, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator10setRunningEb
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setRunning(bool running)
{
    m_running = running;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 73, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator11setMapperIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setMapperId(Qt3DCore::QNodeId mapperId)
{
    m_mapperId = mapperId;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 67, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator18setBlendTreeRootIdEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setBlendTreeRootId(Qt3DCore::QNodeId blendTreeId)
{
    m_blendTreeRootId = blendTreeId;
    setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/blendedclipanimator.cpp, line 97, as _ZN13Qt3DAnimation9Animation19BlendedClipAnimator22setNormalizedLocalTimeEfb
namespace Qt3DAnimation::Animation {
inline void BlendedClipAnimator::setNormalizedLocalTime(float normalizedTime, bool allowMarkDirty)
{
    m_normalizedLocalTime = normalizedTime;
    if (isValidNormalizedTime(m_normalizedLocalTime) && allowMarkDirty)
        setDirty(Handler::BlendedClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/buildblendtreesjob.cpp, line 38, as _ZN13Qt3DAnimation9Animation18BuildBlendTreesJob3runEv
namespace Qt3DAnimation::Animation {
inline void BuildBlendTreesJob::run()
{
    for (const HBlendedClipAnimator &blendedClipAnimatorHandle : std::as_const(m_blendedClipAnimatorHandles)) {
        // Retrieve BlendTree node
        BlendedClipAnimator *blendClipAnimator = m_handler->blendedClipAnimatorManager()->data(blendedClipAnimatorHandle);
        Q_ASSERT(blendClipAnimator);


        const bool canRun = blendClipAnimator->canRun();
        const bool running = blendClipAnimator->isRunning();
        const bool seeking = blendClipAnimator->isSeeking();
        m_handler->setBlendedClipAnimatorRunning(blendedClipAnimatorHandle, canRun && (seeking || running));

        if (!canRun && !(seeking || running))
            continue;

        // Build the format for clip results that should be used by nodes in the blend
        // tree when used with this animator
        const ChannelMapper *mapper = m_handler->channelMapperManager()->lookupResource(blendClipAnimator->mapperId());
        if (!mapper)
            continue;
        const QVector<ChannelNameAndType> channelNamesAndTypes
                = buildRequiredChannelsAndTypes(m_handler, mapper);
        const QVector<ComponentIndices> channelComponentIndices
                = assignChannelComponentIndices(channelNamesAndTypes);

        // Find the leaf value nodes of the blend tree and for each of them
        // create a set of format indices that can later be used to map the
        // raw ClipResults resulting from evaluating an animation clip to the
        // layout used by the blend tree for this animator
        QVector<QBitArray> blendTreeChannelMask;
        const QVector<Qt3DCore::QNodeId> valueNodeIds
                = gatherValueNodesToEvaluate(m_handler, blendClipAnimator->blendTreeRootId());

        // Store the clip value nodes to avoid further lookups below.
        // TODO: Refactor this next block into a function in animationutils.cpp that takes
        // a QList<QClipBlendValue*> as input.
        QList<ClipBlendValue *> valueNodes;
        valueNodes.reserve(valueNodeIds.size());
        for (const auto &valueNodeId : valueNodeIds) {
            ClipBlendValue *valueNode
                    = static_cast<ClipBlendValue *>(m_handler->clipBlendNodeManager()->lookupNode(valueNodeId));
            Q_ASSERT(valueNode);
            valueNodes.push_back(valueNode);

            const Qt3DCore::QNodeId clipId = valueNode->clipId();
            AnimationClip *clip = m_handler->animationClipLoaderManager()->lookupResource(clipId);
            Q_ASSERT(clip);

            const ClipFormat format = generateClipFormatIndices(channelNamesAndTypes,
                                                                channelComponentIndices,
                                                                clip);
            valueNode->setClipFormat(blendClipAnimator->peerId(), format);

            // this BlendClipAnimator needs to be notified when the clip has been loaded
            clip->addDependingBlendedClipAnimator(blendClipAnimator->peerId());

            // Combine the masks from each source clip to see which channels should be
            // evaluated and result in a mappingData being created. If any contributing clip
            // supports a channel, that will produce a channel mapping. Clips with those channels
            // missing will use default values when blending:
            //
            //  Default scale = (1, 1, 1)
            //  Default rotation = (1, 0, 0, 0)
            //  Default translation = (0, 0, 0)
            //  Default joint transforms should be taken from the skeleton initial pose
            //
            // Everything else has all components set to 0. If user wants something else, they
            // should provide a clip with a single keyframe at the desired default value.
            if (blendTreeChannelMask.isEmpty()) {
                // Initialize the blend tree mask from the mask of the first clip
                blendTreeChannelMask = format.sourceClipMask;
            } else {
                // We allow through a channel if any source clip in the tree has
                // data for that channel. Clips without data for a channel will
                // have default values substituted when evaluating the blend tree.
                int channelIndex = 0;
                for (const auto &channelMask : std::as_const(format.sourceClipMask))
                    blendTreeChannelMask[channelIndex++] |= channelMask;
            }
        }

        // Now that we know the overall blend tree mask, go back and compare this to
        // the masks from each of the value nodes. If the overall mask requires a
        // channel but the value node does not provide it, we need to store default
        // values to use for that channel so that the blending evaluation works as
        // expected.
        for (const auto valueNode : valueNodes) {
            ClipFormat &f = valueNode->clipFormat(blendClipAnimator->peerId());

            const qsizetype channelCount = blendTreeChannelMask.size();
            for (qsizetype i = 0; i < channelCount; ++i) {
                if (blendTreeChannelMask[i] == f.sourceClipMask[i])
                    continue; // Masks match, nothing to do

                // If we get to here then we need to obtain a default value
                // for this channel and store it for later application to any
                // missing components of this channel.
                const QVector<float> defaultValue = defaultValueForChannel(m_handler,
                                                                           f.namesAndTypes[i]);

                // Find the indices where we later need to inject these default
                // values and store them in the format.
                const ComponentIndices &componentIndices = f.formattedComponentIndices[i];
                Q_ASSERT(componentIndices.size() == defaultValue.size());
                for (qsizetype j = 0; j < defaultValue.size(); ++j)
                    f.defaultComponentValues.push_back({componentIndices[j], defaultValue[j]});
            }
        }

        // Finally, build the mapping data vector for this blended clip animator. This
        // gets used during the final stage of evaluation when sending the property changes
        // out to the targets of the animation. We do the costly work once up front.
        const Qt3DCore::QNodeIdVector channelMappingIds = mapper->mappingIds();
        QVector<ChannelMapping *> channelMappings;
        channelMappings.reserve(channelMappingIds.size());
        for (const auto &mappingId : channelMappingIds) {
            ChannelMapping *mapping = m_handler->channelMappingManager()->lookupResource(mappingId);
            Q_ASSERT(mapping);
            channelMappings.push_back(mapping);
        }

        const QVector<MappingData> mappingDataVec = buildPropertyMappings(channelMappings,
                                                                          channelNamesAndTypes,
                                                                          channelComponentIndices,
                                                                          blendTreeChannelMask);
        blendClipAnimator->setMappingData(mappingDataVec);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/loadanimationclipjob.cpp, line 52, as _ZN13Qt3DAnimation9Animation20LoadAnimationClipJob3runEv
namespace Qt3DAnimation::Animation {
inline void LoadAnimationClipJob::run()
{
    Q_ASSERT(m_handler);
    Q_D(LoadAnimationClipJob);

    d->m_updatedNodes.reserve(m_animationClipHandles.size());
    AnimationClipLoaderManager *animationClipManager = m_handler->animationClipLoaderManager();
    for (const auto &animationClipHandle : std::as_const(m_animationClipHandles)) {
        AnimationClip *animationClip = animationClipManager->data(animationClipHandle);
        Q_ASSERT(animationClip);
        animationClip->loadAnimation();
        d->m_updatedNodes.push_back(animationClip);
    }

    clearDirtyAnimationClips();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/findrunningclipanimatorsjob.cpp, line 28, as _ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob3runEv
namespace Qt3DAnimation::Animation {
inline void FindRunningClipAnimatorsJob::run()
{
    Q_ASSERT(m_handler);

    ClipAnimatorManager *clipAnimatorManager = m_handler->clipAnimatorManager();
    for (const auto &clipAnimatorHandle : std::as_const(m_clipAnimatorHandles)) {
        ClipAnimator *clipAnimator = clipAnimatorManager->data(clipAnimatorHandle);
        Q_ASSERT(clipAnimator);
        if (!clipAnimator->isEnabled())
            continue;

        const bool canRun = clipAnimator->canRun();
        const bool running = clipAnimator->isRunning();
        const bool seeking = clipAnimator->isSeeking();
        m_handler->setClipAnimatorRunning(clipAnimatorHandle, canRun && (seeking || running));

        // TODO: Actually check if this is needed first, currently we re-build this every time
        // canRun (or the normalized time) is true.
        if (!canRun || !(seeking || running))
            continue;

        // The clip animator needs to know how to map fcurve values through to properties on QNodes.
        // Now we know this animator can run, build the mapping table. Even though this could be
        // done a little simpler in the non-blended case, we follow the same code path as the
        // blended clip animator for consistency and ease of maintenance.
        const ChannelMapper *mapper = m_handler->channelMapperManager()->lookupResource(clipAnimator->mapperId());
        Q_ASSERT(mapper);
        const QVector<ChannelMapping *> channelMappings = mapper->mappings();

        const QVector<ChannelNameAndType> channelNamesAndTypes
                = buildRequiredChannelsAndTypes(m_handler, mapper);
        const QVector<ComponentIndices> channelComponentIndices
                = assignChannelComponentIndices(channelNamesAndTypes);

        const AnimationClip *clip = m_handler->animationClipLoaderManager()->lookupResource(clipAnimator->clipId());
        Q_ASSERT(clip);
        const ClipFormat format = generateClipFormatIndices(channelNamesAndTypes,
                                                            channelComponentIndices,
                                                            clip);
        clipAnimator->setClipFormat(format);

        const QVector<MappingData> mappingData = buildPropertyMappings(channelMappings,
                                                                       channelNamesAndTypes,
                                                                       format.formattedComponentIndices,
                                                                       format.sourceClipMask);
        clipAnimator->setMappingData(mappingData);
    }

    qCDebug(Jobs) << "Running clip animators =" << m_handler->runningClipAnimators();

    // Clear the handles to process ready for next frame
    m_clipAnimatorHandles.clear();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 100, as _ZN13Qt3DAnimation9Animation13AnimationClip13loadAnimationEv
namespace Qt3DAnimation::Animation {
inline void AnimationClip::loadAnimation()
{
    qCDebug(Jobs) << Q_FUNC_INFO << m_source;
    clearData();

    // Load the data
    switch (m_dataType) {
    case File:
        loadAnimationFromUrl();
        break;

    case Data:
        loadAnimationFromData();
        break;

    default:
        Q_UNREACHABLE();
    }

    // Update the duration
    const float t = findDuration();
    setDuration(t);

    m_channelComponentCount = findChannelComponentCount();

    // If using a loader inform the frontend of the status change
    if (m_source.isEmpty()) {
        if (qFuzzyIsNull(t) || m_channelComponentCount == 0)
            setStatus(QAnimationClipLoader::Error);
        else
            setStatus(QAnimationClipLoader::Ready);
    }

    // notify all ClipAnimators and BlendedClipAnimators that depend on this clip,
    // that the clip has changed and that they are now dirty
    {
        QMutexLocker lock(&m_mutex);
        for (const Qt3DCore::QNodeId &id : std::as_const(m_dependingAnimators)) {
            ClipAnimator *animator = m_handler->clipAnimatorManager()->lookupResource(id);
            if (animator)
                animator->animationClipMarkedDirty();
        }
        for (const Qt3DCore::QNodeId &id : std::as_const(m_dependingBlendedAnimators)) {
            BlendedClipAnimator *animator = m_handler->blendedClipAnimatorManager()->lookupResource(id);
            if (animator)
                animator->animationClipMarkedDirty();
        }
        m_dependingAnimators.clear();
        m_dependingBlendedAnimators.clear();
    }

    qCDebug(Jobs) << "Loaded animation data:" << *this;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 265, as _ZN13Qt3DAnimation9Animation13AnimationClip24addDependingClipAnimatorERKN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void AnimationClip::addDependingClipAnimator(const Qt3DCore::QNodeId &id)
{
    QMutexLocker lock(&m_mutex);
    m_dependingAnimators.push_back(id);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 271, as _ZN13Qt3DAnimation9Animation13AnimationClip31addDependingBlendedClipAnimatorERKN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline void AnimationClip::addDependingBlendedClipAnimator(const Qt3DCore::QNodeId &id)
{
    QMutexLocker lock(&m_mutex);
    m_dependingBlendedAnimators.push_back(id);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 61, as _ZN13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipFormat &ClipBlendValue::clipFormat(Qt3DCore::QNodeId animatorId)
{
    const int animatorIndex = m_animatorIds.indexOf(animatorId);
    return m_clipFormats[animatorIndex];
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 48, as _ZN13Qt3DAnimation9Animation14ClipBlendValue13setClipFormatEN8Qt3DCore7QNodeIdERKNS0_10ClipFormatE
namespace Qt3DAnimation::Animation {
inline void ClipBlendValue::setClipFormat(Qt3DCore::QNodeId animatorId, const ClipFormat &formatIndices)
{
    // Do we already have an entry for this animator?
    const int animatorIndex = m_animatorIds.indexOf(animatorId);
    if (animatorIndex == -1) {
        // Nope, add it
        m_animatorIds.push_back(animatorId);
        m_clipFormats.push_back(formatIndices);
    } else {
        m_clipFormats[animatorIndex] = formatIndices;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/loadanimationclipjob.cpp, line 47, as _ZN13Qt3DAnimation9Animation20LoadAnimationClipJob24clearDirtyAnimationClipsEv
namespace Qt3DAnimation::Animation {
inline void LoadAnimationClipJob::clearDirtyAnimationClips()
{
    m_animationClipHandles.clear();
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  A Qt3DAnimation::QAnimationAspectPrivate that Python can take functions over in. Every Qt3DAnimation::QAnimationAspectPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall1)(const void *, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall2)(const void *, Qt3DCore::QNode *, Qt3DCore::QBackendNode *, bool, int *);
typedef void (*CuteQt3DAnimation_QAnimationAspectPrivateCall3)(const void *, int *);
class CuteQt3DAnimation_QAnimationAspectPrivate : public Qt3DAnimation::QAnimationAspectPrivate {
public:
  using Qt3DAnimation::QAnimationAspectPrivate::QAnimationAspectPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface8jobsDoneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore27QAspectJobProviderInterface9frameDoneEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore22QAbstractAspectPrivate21syncDirtyFrontEndNodeEPNS_5QNodeEPNS_12QBackendNodeEb")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore22QAbstractAspectPrivate23onEngineAboutToShutdownEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAbstractAspectPrivate::jobsDone()
  void jobsDone() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::jobsDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::frameDone()
  void frameDone() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::frameDone();
  }

  //  void Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(QNode
  //      *node, QBackendNode *backend, bool firstTime) const
  void syncDirtyFrontEndNode(
      Qt3DCore::QNode *node,
      Qt3DCore::QBackendNode *backend,
      bool firstTime) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall2 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall2>(taken[2]);
      call(this, node, backend, firstTime, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::syncDirtyFrontEndNode(node, backend, firstTime);
  }

  //  void Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown()
  void onEngineAboutToShutdown() override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DAnimation_QAnimationAspectPrivateCall3 call = reinterpret_cast<CuteQt3DAnimation_QAnimationAspectPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAbstractAspectPrivate::onEngineAboutToShutdown();
  }
};

//  QAnimationAspect *Qt3DAnimation::QAnimationAspectPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationAspect *ritual_ZN13Qt3DAnimation23QAnimationAspectPrivate6q_funcEv(
    Qt3DAnimation::QAnimationAspectPrivate *self) {
  return self->q_func();
}

//  const QAnimationAspect *Qt3DAnimation::QAnimationAspectPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationAspect *ritual_ZNK13Qt3DAnimation23QAnimationAspectPrivate6q_funcEv(
    const Qt3DAnimation::QAnimationAspectPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DAnimation_QAnimationAspectPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAnimationAspectPrivate(
    Qt3DAnimation::QAnimationAspectPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAnimationAspectPrivate *>(self)->take(key, call);
}
