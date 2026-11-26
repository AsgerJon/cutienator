//  Written by dev_tooling.RitualGenerator from the records of Qt3DAnimation/
//  6.12.0/Qt3DAnimation/private/findrunningclipanimatorsjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/findrunningclipanimatorsjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/findrunningclipanimatorsjob_p.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/animationlogging_p.h>
#include <Qt3DAnimation/private/animationutils_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qt3d/src/animation/backend/findrunningclipanimatorsjob.cpp, line 23, as _ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob21setDirtyClipAnimatorsERK5QListIN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEE
namespace Qt3DAnimation::Animation {
inline void FindRunningClipAnimatorsJob::setDirtyClipAnimators(const QVector<HClipAnimator> &clipAnimatorHandles)
{
    m_clipAnimatorHandles = clipAnimatorHandles;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  void
//      Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::setHandler(Han
//      dler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::FindRunningClipAnimatorsJob *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  Handler *Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::handler()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Handler *ritual_ZNK13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob7handlerEv(
    const Qt3DAnimation::Animation::FindRunningClipAnimatorsJob *self) {
  return self->handler();
}

//  void Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::setDirtyClipA
//      nimators(const QVector<HClipAnimator> &animationClipHandles)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob21setDirtyClipAnimatorsERK5QListIN8Qt3DCore7QHandleINS0_12ClipAnimatorEEEE(
    Qt3DAnimation::Animation::FindRunningClipAnimatorsJob *self,
    const QVector<Qt3DAnimation::Animation::HClipAnimator> *animationClipHandles) {
  self->setDirtyClipAnimators(*animationClipHandles);
}

//  void Qt3DAnimation::Animation::FindRunningClipAnimatorsJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation27FindRunningClipAnimatorsJob3runEv(
    Qt3DAnimation::Animation::FindRunningClipAnimatorsJob *self) {
  self->run();
}
