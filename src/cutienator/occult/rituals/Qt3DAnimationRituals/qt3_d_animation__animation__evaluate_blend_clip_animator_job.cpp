//  Written by dev_tooling.RitualGenerator from the records of Qt3DAnimation/
//  6.12.0/Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/evaluateblendclipanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/abstractevaluateclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qskeleton_p.h>
#include <Qt3DAnimation/qabstractclipanimator.h>
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
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/qabstractanimationclip.h>
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

//  from ../qt3d/src/animation/backend/abstractevaluateclipanimatorjob.cpp, line 27, as _ZN13Qt3DAnimation9Animation31AbstractEvaluateClipAnimatorJobC2Ev
namespace Qt3DAnimation::Animation {
inline AbstractEvaluateClipAnimatorJob::AbstractEvaluateClipAnimatorJob()
    : Qt3DCore::QAspectJob(*new AbstractEvaluateClipAnimatorJobPrivate)
{
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

//  from ../qt3d/src/animation/backend/clipblendvalue.cpp, line 61, as _ZN13Qt3DAnimation9Animation14ClipBlendValue10clipFormatEN8Qt3DCore7QNodeIdE
namespace Qt3DAnimation::Animation {
inline ClipFormat &ClipBlendValue::clipFormat(Qt3DCore::QNodeId animatorId)
{
    const int animatorIndex = m_animatorIds.indexOf(animatorId);
    return m_clipFormats[animatorIndex];
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  void Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob::setHandler(H
//      andler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJob10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  Handler
//      *Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob::handler()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Handler *ritual_ZNK13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJob7handlerEv(
    const Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob *self) {
  return self->handler();
}

//  void Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob::setBlendClip
//      Animator(const HBlendedClipAnimator &blendClipAnimatorHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJob20setBlendClipAnimatorERKN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEE(
    Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob *self,
    const Qt3DAnimation::Animation::HBlendedClipAnimator *blendClipAnimatorHandle) {
  self->setBlendClipAnimator(*blendClipAnimatorHandle);
}

//  HBlendedClipAnimator Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJ
//      ob::blendClipAnimator() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::HBlendedClipAnimator *ritual_ZNK13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJob17blendClipAnimatorEv(
    const Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob *self) {
  return new Qt3DAnimation::Animation::HBlendedClipAnimator(
      self->blendClipAnimator());
}

//  void Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation28EvaluateBlendClipAnimatorJob3runEv(
    Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob *self) {
  self->run();
}

//  a Qt3DAnimation::Animation::HBlendedClipAnimator a ritual of
//      Qt3DAnimation::Animation::EvaluateBlendClipAnimatorJob gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_EvaluateBlendClipAnimatorJob__Qt3DAnimation_Animation_HBlendedClipAnimator(
    Qt3DAnimation::Animation::HBlendedClipAnimator *self) {
  delete self;
}
