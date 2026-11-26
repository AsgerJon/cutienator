//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/handler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/handler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QVector>
#include <vector>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#include <QtCore/qloggingcategory.h>
#include <Qt3DAnimation/private/evaluateclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DAnimation/qclipanimator.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/animationutils_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
#include <Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qskeleton_p.h>
#include <Qt3DAnimation/qblendedclipanimator.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/animationutils_p.h>
#include <Qt3DAnimation/private/clipblendvalue_p.h>
#include <Qt3DAnimation/private/lerpclipblend_p.h>
#include <Qt3DAnimation/private/clipblendnodevisitor_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
#include <Qt3DAnimation/qanimationcliploader.h>
#include <Qt3DAnimation/private/qanimationcliploader_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
#include <Qt3DAnimation/private/qabstractanimationclip_p.h>
#include <Qt3DAnimation/private/abstractevaluateclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qskeleton_p.h>
#include <Qt3DAnimation/qabstractclipanimator.h>
#include <Qt3DAnimation/private/clipblendvalue_p.h>
#include <Qt3DAnimation/qclipblendvalue.h>
#include <Qt3DAnimation/private/qclipblendvalue_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
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

//  from ../qt3d/src/animation/backend/abstractevaluateclipanimatorjob.cpp, line 15, as local:abstractevaluateclipanimatorjob.cpp:AbstractEvaluateClipAnimatorJobPrivate
namespace Qt3DAnimation::Animation {
class AbstractEvaluateClipAnimatorJobPrivate : public Qt3DCore::QAspectJobPrivate
{
public:
    AbstractEvaluateClipAnimatorJobPrivate() { }
    ~AbstractEvaluateClipAnimatorJobPrivate() override { }

    void postFrame(Qt3DCore::QAspectManager *manager) override;

    AnimationRecord m_record;
    QVector<AnimationCallbackAndValue> m_callbacks;
};
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/abstractevaluateclipanimatorjob.cpp, line 50, as local:abstractevaluateclipanimatorjob.cpp:AbstractEvaluateClipAnimatorJobPrivate::postFrame
namespace Qt3DAnimation::Animation {
inline void AbstractEvaluateClipAnimatorJobPrivate::postFrame(Qt3DCore::QAspectManager *manager)
{
    if (m_record.animatorId.isNull())
        return;

    for (auto targetData : std::as_const(m_record.targetChanges)) {
        Qt3DCore::QNode *node = manager->lookupNode(targetData.targetId);
        if (node)
            node->setProperty(targetData.propertyName, targetData.value);
    }

    for (auto skeletonData : std::as_const(m_record.skeletonChanges)) {
        Qt3DCore::QAbstractSkeleton *node = qobject_cast<Qt3DCore::QAbstractSkeleton *>(manager->lookupNode(skeletonData.first));
        if (node) {
            auto d = Qt3DCore::QAbstractSkeletonPrivate::get(node);
            d->m_localPoses = skeletonData.second;
            d->update();
        }
    }

    QAbstractClipAnimator *animator = qobject_cast<QAbstractClipAnimator *>(manager->lookupNode(m_record.animatorId));
    if (animator) {
        if (isValidNormalizedTime(m_record.normalizedTime))
            animator->setNormalizedTime(m_record.normalizedTime);
        if (m_record.finalFrame)
            animator->setRunning(false);
    }

    for (const AnimationCallbackAndValue &callback: std::as_const(m_callbacks)) {
        if (callback.callback)
            callback.callback->valueChanged(callback.value);
    }

    m_record = {};
}
}  // namespace Qt3DAnimation::Animation

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

//  from ../qt3d/src/animation/animationlogging.cpp, line 14, as _ZN13Qt3DAnimation9Animation12HandlerLogicEv
namespace Qt3DAnimation::Animation {
inline const QLoggingCategory &HandlerLogic()
{
    static const QLoggingCategory category("Qt3D.Animation.Handler", QtWarningMsg);
    return category;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/buildblendtreesjob.cpp, line 25, as _ZN13Qt3DAnimation9Animation18BuildBlendTreesJob23setBlendedClipAnimatorsERK5QListIN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEEE
namespace Qt3DAnimation::Animation {
inline void BuildBlendTreesJob::setBlendedClipAnimators(const QVector<HBlendedClipAnimator> &blendedClipAnimatorHandles)
{
    m_blendedClipAnimatorHandles = blendedClipAnimatorHandles;
    BlendedClipAnimatorManager *blendedClipAnimatorManager = m_handler->blendedClipAnimatorManager();
    BlendedClipAnimator *blendedClipAnimator = nullptr;
    for (const auto &blendedClipAnimatorHandle : std::as_const(m_blendedClipAnimatorHandles)) {
        blendedClipAnimator = blendedClipAnimatorManager->data(blendedClipAnimatorHandle);
        Q_ASSERT(blendedClipAnimator);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/loadanimationclipjob.cpp, line 39, as _ZN13Qt3DAnimation9Animation20LoadAnimationClipJob22addDirtyAnimationClipsERK5QListIN8Qt3DCore7QHandleINS0_13AnimationClipEEEE
namespace Qt3DAnimation::Animation {
inline void LoadAnimationClipJob::addDirtyAnimationClips(const QVector<HAnimationClip> &animationClipHandles)
{
    for (const auto &handle : animationClipHandles) {
        if (!m_animationClipHandles.contains(handle))
            m_animationClipHandles.push_back(handle);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/evaluateclipanimatorjob.cpp, line 20, as _ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJobC1Ev
namespace Qt3DAnimation::Animation {
inline EvaluateClipAnimatorJob::EvaluateClipAnimatorJob()
    : AbstractEvaluateClipAnimatorJob()
    , m_handler(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::EvaluateClipAnimator, 0)
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/findrunningclipanimatorsjob.cpp, line 23, as _ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob21setDirtyClipAnimatorsERK5QListIN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEE
namespace Qt3DAnimation::Animation {
inline void FindRunningClipAnimatorsJob::setDirtyClipAnimators(const QVector<HClipAnimator> &clipAnimatorHandles)
{
    m_clipAnimatorHandles = clipAnimatorHandles;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/evaluateblendclipanimatorjob.cpp, line 22, as _ZN13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJobC1Ev
namespace Qt3DAnimation::Animation {
inline EvaluateBlendClipAnimatorJob::EvaluateBlendClipAnimatorJob()
    : AbstractEvaluateClipAnimatorJob()
    , m_handler(nullptr)
{
    SET_JOB_RUN_STAT_TYPE(this, JobTypes::EvaluateBlendClipAnimator, 0)
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

//  from ../qt3d/src/animation/backend/abstractevaluateclipanimatorjob.cpp, line 27, as _ZN13Qt3DAnimation9Animation31AbstractEvaluateClipAnimatorJobC2Ev
namespace Qt3DAnimation::Animation {
inline AbstractEvaluateClipAnimatorJob::AbstractEvaluateClipAnimatorJob()
    : Qt3DCore::QAspectJob(*new AbstractEvaluateClipAnimatorJobPrivate)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/evaluateclipanimatorjob.cpp, line 27, as _ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob3runEv
namespace Qt3DAnimation::Animation {
inline void EvaluateClipAnimatorJob::run()
{
    Q_ASSERT(m_handler);

    ClipAnimator *clipAnimator = m_handler->clipAnimatorManager()->data(m_clipAnimatorHandle);
    Q_ASSERT(clipAnimator);
    const bool running = clipAnimator->isRunning();
    const bool seeking = clipAnimator->isSeeking();
    if (!running && !seeking) {
        m_handler->setClipAnimatorRunning(m_clipAnimatorHandle, false);
        return;
    }

    const qint64 globalTimeNS = m_handler->simulationTime();

    Clock *clock = m_handler->clockManager()->lookupResource(clipAnimator->clockId());

    // Evaluate the fcurves
    AnimationClip *clip = m_handler->animationClipLoaderManager()->lookupResource(clipAnimator->clipId());
    Q_ASSERT(clip);

    const qint64 nsSincePreviousFrame = seeking ? toNsecs(clip->duration() * clipAnimator->normalizedLocalTime())
                                                : clipAnimator->nsSincePreviousFrame(globalTimeNS);

    // Prepare for evaluation (convert global time to local time ....)
    const AnimatorEvaluationData animatorEvaluationData = evaluationDataForAnimator(clipAnimator,
                                                                                    clock,
                                                                                    nsSincePreviousFrame);

    const ClipEvaluationData preEvaluationDataForClip = evaluationDataForClip(clip, animatorEvaluationData);
    const ClipResults rawClipResults = evaluateClipAtPhase(clip, preEvaluationDataForClip.normalizedLocalTime);

    // Reformat the clip results into the layout used by this animator/blend tree
    const ClipFormat clipFormat = clipAnimator->clipFormat();
    ClipResults formattedClipResults = formatClipResults(rawClipResults, clipFormat.sourceClipIndices);

    if (preEvaluationDataForClip.isFinalFrame)
        clipAnimator->setRunning(false);

    clipAnimator->setCurrentLoop(preEvaluationDataForClip.currentLoop);
    clipAnimator->setLastGlobalTimeNS(globalTimeNS);
    clipAnimator->setLastLocalTime(preEvaluationDataForClip.localTime);
    clipAnimator->setLastNormalizedLocalTime(preEvaluationDataForClip.normalizedLocalTime);

    // Prepare property changes (if finalFrame it also prepares the change for the running property for the frontend)
    auto record = prepareAnimationRecord(clipAnimator->peerId(),
                                         clipAnimator->mappingData(),
                                         formattedClipResults,
                                         preEvaluationDataForClip.isFinalFrame,
                                         preEvaluationDataForClip.normalizedLocalTime);

    // Trigger callbacks either on this thread or by notifying the gui thread.
    auto callbacks = prepareCallbacks(clipAnimator->mappingData(), formattedClipResults);

    // Update the normalized time on the backend node so that
    // frontend <-> backend sync will not mark things dirty
    // unless the frontend normalized time really is different
    clipAnimator->setNormalizedLocalTime(record.normalizedTime, false);

    setPostFrameData(record, callbacks);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/evaluateblendclipanimatorjob.cpp, line 29, as _ZN13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJob3runEv
namespace Qt3DAnimation::Animation {
inline void EvaluateBlendClipAnimatorJob::run()
{
    // Find the set of clips that need to be evaluated by querying each node
    // in the blend tree.
    // TODO: We should be able to cache this for each blend animator and only
    // update when a node indicates its dependencies have changed as a result
    // of blend factors changing

    BlendedClipAnimator *blendedClipAnimator = m_handler->blendedClipAnimatorManager()->data(m_blendClipAnimatorHandle);
    Q_ASSERT(blendedClipAnimator);
    const bool running = blendedClipAnimator->isRunning();
    const bool seeking = blendedClipAnimator->isSeeking();
    if (!running && !seeking) {
        m_handler->setBlendedClipAnimatorRunning(m_blendClipAnimatorHandle, false);
        return;
    }

    Qt3DCore::QNodeId blendTreeRootId = blendedClipAnimator->blendTreeRootId();
    const QVector<Qt3DCore::QNodeId> valueNodeIdsToEvaluate = gatherValueNodesToEvaluate(m_handler, blendTreeRootId);

    // Calculate the resulting duration of the blend tree based upon its current state
    ClipBlendNodeManager *blendNodeManager = m_handler->clipBlendNodeManager();
    ClipBlendNode *blendTreeRootNode = blendNodeManager->lookupNode(blendTreeRootId);
    Q_ASSERT(blendTreeRootNode);
    const double duration = blendTreeRootNode->duration();

    Clock *clock = m_handler->clockManager()->lookupResource(blendedClipAnimator->clockId());

    qint64 globalTimeNS = m_handler->simulationTime();
    qint64 nsSincePreviousFrame = seeking ? toNsecs(duration * blendedClipAnimator->normalizedLocalTime())
                                          : blendedClipAnimator->nsSincePreviousFrame(globalTimeNS);

    // Calculate the phase given the blend tree duration and global time
    AnimatorEvaluationData animatorData = evaluationDataForAnimator(blendedClipAnimator, clock, nsSincePreviousFrame);
    const double phase = phaseFromElapsedTime(animatorData.currentTime, animatorData.elapsedTime,
                                              animatorData.playbackRate,
                                              duration,
                                              animatorData.loopCount,
                                              animatorData.currentLoop);

    // Iterate over the value nodes of the blend tree, evaluate the
    // contained animation clips at the current phase and store the results
    // in the animator indexed by node.
    AnimationClipLoaderManager *clipLoaderManager = m_handler->animationClipLoaderManager();
    for (const auto &valueNodeId : valueNodeIdsToEvaluate) {
        ClipBlendValue *valueNode = static_cast<ClipBlendValue *>(blendNodeManager->lookupNode(valueNodeId));
        Q_ASSERT(valueNode);
        AnimationClip *clip = clipLoaderManager->lookupResource(valueNode->clipId());
        Q_ASSERT(clip);

        ClipResults rawClipResults = evaluateClipAtPhase(clip, float(phase));

        // Reformat the clip results into the layout used by this animator/blend tree
        const ClipFormat format = valueNode->clipFormat(blendedClipAnimator->peerId());
        ClipResults formattedClipResults = formatClipResults(rawClipResults, format.sourceClipIndices);
        applyComponentDefaultValues(format.defaultComponentValues, formattedClipResults);
        valueNode->setClipResults(blendedClipAnimator->peerId(), formattedClipResults);
    }

    // Evaluate the blend tree
    ClipResults blendedResults = evaluateBlendTree(m_handler, blendedClipAnimator, blendTreeRootId);

    const double localTime = phase * duration;
    blendedClipAnimator->setLastGlobalTimeNS(globalTimeNS);
    blendedClipAnimator->setLastLocalTime(localTime);
    blendedClipAnimator->setLastNormalizedLocalTime(float(phase));
    blendedClipAnimator->setCurrentLoop(animatorData.currentLoop);

    // Prepare the change record
    const bool finalFrame = isFinalFrame(localTime, duration, animatorData.currentLoop, animatorData.loopCount, animatorData.playbackRate);
    const QVector<MappingData> mappingData = blendedClipAnimator->mappingData();
    auto record = prepareAnimationRecord(blendedClipAnimator->peerId(),
                                         mappingData,
                                         blendedResults,
                                         finalFrame,
                                         float(phase));

    // Trigger callbacks either on this thread or by notifying the gui thread.
    auto callbacks = prepareCallbacks(mappingData, blendedResults);

    // Update the normalized time on the backend node so that
    // frontend <-> backend sync will not mark things dirty
    // unless the frontend normalized time really is different
    blendedClipAnimator->setNormalizedLocalTime(record.normalizedTime, false);

    setPostFrameData(record, callbacks);
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

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 129, as _ZN13Qt3DAnimation9Animation12ClipAnimator16setLastLocalTimeEd
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastLocalTime(double lastLocalTime)
{
    m_lastLocalTime = lastLocalTime;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 119, as _ZN13Qt3DAnimation9Animation12ClipAnimator19setLastGlobalTimeNSEx
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastGlobalTimeNS(qint64 lastGlobalTimeNS)
{
    m_lastGlobalTimeNS = lastGlobalTimeNS;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 114, as _ZN13Qt3DAnimation9Animation12ClipAnimator20nsSincePreviousFrameEx
namespace Qt3DAnimation::Animation {
inline qint64 ClipAnimator::nsSincePreviousFrame(qint64 currentGlobalTimeNS)
{
    return currentGlobalTimeNS - m_lastGlobalTimeNS;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 134, as _ZN13Qt3DAnimation9Animation12ClipAnimator26setLastNormalizedLocalTimeEf
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastNormalizedLocalTime(float normalizedTime)
{
    m_lastNormalizedLocalTime = normalizedTime;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipblendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation13ClipBlendNode14setClipResultsEN8Qt3DCore7QNodeIdERK5QListIfE
namespace Qt3DAnimation::Animation {
inline void ClipBlendNode::setClipResults(Qt3DCore::QNodeId animatorId, const ClipResults &clipResults)
{
    // Do we already have an entry for this animator?
    const qsizetype animatorIndex = m_animatorIds.indexOf(animatorId);
    if (animatorIndex == -1) {
        // Nope, add it
        m_animatorIds.push_back(animatorId);
        m_clipResults.push_back(clipResults);
    } else {
        m_clipResults[animatorIndex] = clipResults;
    }
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

//  from ../qt3d/src/animation/backend/handler.cpp, line 79, as _ZN13Qt3DAnimation9Animation7Handler22setClipAnimatorRunningERKN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEb
namespace Qt3DAnimation::Animation {
inline void Handler::setClipAnimatorRunning(const HClipAnimator &handle, bool running)
{
    QMutexLocker lock(&m_mutex);

    // Add clip to running set if not already present
    if (running && !m_runningClipAnimators.contains(handle)) {
        m_runningClipAnimators.push_back(handle);
        ClipAnimator *clipAnimator = m_clipAnimatorManager->data(handle);
        if (clipAnimator)
            clipAnimator->setStartTime(m_simulationTime);
    }

    // If being marked as not running, remove from set of running clips
    if (!running) {
        m_runningClipAnimators.removeAll(handle);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 98, as _ZN13Qt3DAnimation9Animation7Handler29setBlendedClipAnimatorRunningERKN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEEb
namespace Qt3DAnimation::Animation {
inline void Handler::setBlendedClipAnimatorRunning(const HBlendedClipAnimator &handle, bool running)
{
    QMutexLocker lock(&m_mutex);

    // Add clip to running set if not already present
    if (running && !m_runningBlendedClipAnimators.contains(handle)) {
        m_runningBlendedClipAnimators.push_back(handle);
        BlendedClipAnimator *blendedClipAnimator = m_blendedClipAnimatorManager->data(handle);
        if (blendedClipAnimator)
            blendedClipAnimator->setStartTime(m_simulationTime);
    }

    // If being marked as not running, remove from set of running clips
    if (!running) {
        const auto it = std::find_if(m_runningBlendedClipAnimators.begin(),
                                     m_runningBlendedClipAnimators.end(),
                                     [handle](const HBlendedClipAnimator &h) { return h == handle; });
        if (it != m_runningBlendedClipAnimators.end())
            m_runningBlendedClipAnimators.erase(it);
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 123, as _ZN13Qt3DAnimation9Animation7Handler17cleanupHandleListEP5QListIN8Qt3DCore7QHandleINS0_13AnimationClipEEEE
namespace Qt3DAnimation::Animation {
inline void Handler::cleanupHandleList(QVector<HAnimationClip> *clips)
{
    for (auto it = clips->begin(); it != clips->end(); ) {
        if (!m_animationClipLoaderManager->data(*it))
            it = clips->erase(it);
        else
            ++it;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 133, as _ZN13Qt3DAnimation9Animation7Handler17cleanupHandleListEP5QListIN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEE
namespace Qt3DAnimation::Animation {
inline void Handler::cleanupHandleList(QVector<HClipAnimator> *animators)
{
    for (auto it = animators->begin(); it != animators->end(); ) {
        if (!m_clipAnimatorManager->data(*it))
            it = animators->erase(it);
        else
            ++it;
    }
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/handler.cpp, line 143, as _ZN13Qt3DAnimation9Animation7Handler17cleanupHandleListEP5QListIN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEEE
namespace Qt3DAnimation::Animation {
inline void Handler::cleanupHandleList(QVector<HBlendedClipAnimator> *animators)
{
    for (auto it = animators->begin(); it != animators->end(); ) {
        if (!m_blendedClipAnimatorManager->data(*it))
            it = animators->erase(it);
        else
            ++it;
    }
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  qint64 Qt3DAnimation::Animation::Handler::simulationTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13Qt3DAnimation9Animation7Handler14simulationTimeEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->simulationTime();
}

//  void Qt3DAnimation::Animation::Handler::setDirty(DirtyFlag flag,
//      Qt3DCore::QNodeId nodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Handler8setDirtyENS1_9DirtyFlagEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::Handler *self,
    Qt3DAnimation::Animation::Handler::DirtyFlag flag,
    const Qt3DCore::QNodeId *nodeId) {
  self->setDirty(flag, *nodeId);
}

//  void Qt3DAnimation::Animation::Handler::setClipAnimatorRunning(const
//      HClipAnimator &handle, bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Handler22setClipAnimatorRunningERKN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEb(
    Qt3DAnimation::Animation::Handler *self,
    const Qt3DAnimation::Animation::HClipAnimator *handle,
    bool running) {
  self->setClipAnimatorRunning(*handle, running);
}

//  QVector<HClipAnimator>
//      Qt3DAnimation::Animation::Handler::runningClipAnimators() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DAnimation::Animation::HClipAnimator> *ritual_ZNK13Qt3DAnimation9Animation7Handler20runningClipAnimatorsEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return new QVector<Qt3DAnimation::Animation::HClipAnimator>(
      self->runningClipAnimators());
}

//  void
//      Qt3DAnimation::Animation::Handler::setBlendedClipAnimatorRunning(cons
//      t HBlendedClipAnimator &handle, bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Handler29setBlendedClipAnimatorRunningERKN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEEb(
    Qt3DAnimation::Animation::Handler *self,
    const Qt3DAnimation::Animation::HBlendedClipAnimator *handle,
    bool running) {
  self->setBlendedClipAnimatorRunning(*handle, running);
}

//  QVector<HBlendedClipAnimator>
//      Qt3DAnimation::Animation::Handler::runningBlenndedClipAnimators()
//      const
extern "C" Q_DECL_EXPORT
QVector<Qt3DAnimation::Animation::HBlendedClipAnimator> *ritual_ZNK13Qt3DAnimation9Animation7Handler28runningBlenndedClipAnimatorsEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return new QVector<Qt3DAnimation::Animation::HBlendedClipAnimator>(
      self->runningBlenndedClipAnimators());
}

//  AnimationClipLoaderManager
//      *Qt3DAnimation::Animation::Handler::animationClipLoaderManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::AnimationClipLoaderManager *ritual_ZNK13Qt3DAnimation9Animation7Handler26animationClipLoaderManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->animationClipLoaderManager();
}

//  ClockManager *Qt3DAnimation::Animation::Handler::clockManager() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClockManager *ritual_ZNK13Qt3DAnimation9Animation7Handler12clockManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->clockManager();
}

//  ClipAnimatorManager
//      *Qt3DAnimation::Animation::Handler::clipAnimatorManager() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipAnimatorManager *ritual_ZNK13Qt3DAnimation9Animation7Handler19clipAnimatorManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->clipAnimatorManager();
}

//  BlendedClipAnimatorManager
//      *Qt3DAnimation::Animation::Handler::blendedClipAnimatorManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::BlendedClipAnimatorManager *ritual_ZNK13Qt3DAnimation9Animation7Handler26blendedClipAnimatorManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->blendedClipAnimatorManager();
}

//  ChannelMappingManager
//      *Qt3DAnimation::Animation::Handler::channelMappingManager() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelMappingManager *ritual_ZNK13Qt3DAnimation9Animation7Handler21channelMappingManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->channelMappingManager();
}

//  ChannelMapperManager
//      *Qt3DAnimation::Animation::Handler::channelMapperManager() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ChannelMapperManager *ritual_ZNK13Qt3DAnimation9Animation7Handler20channelMapperManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->channelMapperManager();
}

//  ClipBlendNodeManager
//      *Qt3DAnimation::Animation::Handler::clipBlendNodeManager() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendNodeManager *ritual_ZNK13Qt3DAnimation9Animation7Handler20clipBlendNodeManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->clipBlendNodeManager();
}

//  SkeletonManager *Qt3DAnimation::Animation::Handler::skeletonManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::SkeletonManager *ritual_ZNK13Qt3DAnimation9Animation7Handler15skeletonManagerEv(
    const Qt3DAnimation::Animation::Handler *self) {
  return self->skeletonManager();
}

//  void Qt3DAnimation::Animation::Handler::cleanupHandleList(QVector<HAnimat
//      ionClip> *clips)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Handler17cleanupHandleListEP5QListIN8Qt3DCore7QHandleINS0_13AnimationClipEEEE(
    Qt3DAnimation::Animation::Handler *self,
    QVector<Qt3DAnimation::Animation::HAnimationClip> *clips) {
  self->cleanupHandleList(clips);
}

//  void Qt3DAnimation::Animation::Handler::cleanupHandleList(QVector<HClipAn
//      imator> *animators)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Handler17cleanupHandleListEP5QListIN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEE(
    Qt3DAnimation::Animation::Handler *self,
    QVector<Qt3DAnimation::Animation::HClipAnimator> *animators) {
  self->cleanupHandleList(animators);
}

//  void Qt3DAnimation::Animation::Handler::cleanupHandleList(QVector<HBlende
//      dClipAnimator> *animators)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Handler17cleanupHandleListEP5QListIN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEEE(
    Qt3DAnimation::Animation::Handler *self,
    QVector<Qt3DAnimation::Animation::HBlendedClipAnimator> *animators) {
  self->cleanupHandleList(animators);
}

//  a QVector<Qt3DAnimation::Animation::HClipAnimator> a ritual of
//      Qt3DAnimation::Animation::Handler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_Handler__QVector_Qt3DAnimation_Animation_HClipAnimator(
    QVector<Qt3DAnimation::Animation::HClipAnimator> *self) {
  delete self;
}

//  a QVector<Qt3DAnimation::Animation::HBlendedClipAnimator> a ritual of
//      Qt3DAnimation::Animation::Handler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_Handler__QVector_Qt3DAnimation_Animation_HBlendedClipAnimator(
    QVector<Qt3DAnimation::Animation::HBlendedClipAnimator> *self) {
  delete self;
}

//  a std::vector<Qt3DCore::QAspectJobPtr> a ritual of
//      Qt3DAnimation::Animation::Handler gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_Handler__std_vector_Qt3DCore_QAspectJobPtr(
    std::vector<Qt3DCore::QAspectJobPtr> *self) {
  delete self;
}
