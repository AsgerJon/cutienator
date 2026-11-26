//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/evaluateclipanimatorjob_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/evaluateclipanimatorjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/abstractevaluateclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qskeleton_p.h>
#include <Qt3DAnimation/qabstractclipanimator.h>
#include <Qt3DAnimation/private/evaluateclipanimatorjob_p.h>
#include <Qt3DCore/private/qaspectjob_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DAnimation/qclipanimator.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 65, as _ZN13Qt3DAnimation9Animation12ClipAnimator22setNormalizedLocalTimeEfb
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setNormalizedLocalTime(float normalizedTime, bool allowMarkDirty)
{
    m_normalizedLocalTime = normalizedTime;
    if (isValidNormalizedTime(normalizedTime) && allowMarkDirty)
        setDirty(Handler::ClipAnimatorDirty);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/clipanimator.cpp, line 134, as _ZN13Qt3DAnimation9Animation12ClipAnimator26setLastNormalizedLocalTimeEf
namespace Qt3DAnimation::Animation {
inline void ClipAnimator::setLastNormalizedLocalTime(float normalizedTime)
{
    m_lastNormalizedLocalTime = normalizedTime;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  void
//      Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setHandler(Handler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  Handler *Qt3DAnimation::Animation::EvaluateClipAnimatorJob::handler()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Handler *ritual_ZNK13Qt3DAnimation9Animation23EvaluateClipAnimatorJob7handlerEv(
    const Qt3DAnimation::Animation::EvaluateClipAnimatorJob *self) {
  return self->handler();
}

//  void
//      Qt3DAnimation::Animation::EvaluateClipAnimatorJob::setClipAnimator(co
//      nst HClipAnimator &clipAnimatorHandle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob15setClipAnimatorERKN8Qt3DCore7QHandleINS0_12ClipAnimatorEEE(
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob *self,
    const Qt3DAnimation::Animation::HClipAnimator *clipAnimatorHandle) {
  self->setClipAnimator(*clipAnimatorHandle);
}

//  void
//      Qt3DAnimation::Animation::EvaluateClipAnimatorJob::clearClipAnimator(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob17clearClipAnimatorEv(
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob *self) {
  self->clearClipAnimator();
}

//  void Qt3DAnimation::Animation::EvaluateClipAnimatorJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation23EvaluateClipAnimatorJob3runEv(
    Qt3DAnimation::Animation::EvaluateClipAnimatorJob *self) {
  self->run();
}
