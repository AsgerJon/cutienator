//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/buildblendtreesjob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/buildblendtreesjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/buildblendtreesjob_p.h>
#include <Qt3DAnimation/private/handler_p.h>
#include <Qt3DAnimation/private/managers_p.h>
#include <Qt3DAnimation/private/clipblendnodevisitor_p.h>
#include <Qt3DAnimation/private/clipblendnode_p.h>
#include <Qt3DAnimation/private/clipblendvalue_p.h>
#include <Qt3DAnimation/private/lerpclipblend_p.h>
#include <Qt3DAnimation/private/job_common_p.h>
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
//  -----------------------------------------------------------------------

//  void Qt3DAnimation::Animation::BuildBlendTreesJob::setHandler(Handler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation18BuildBlendTreesJob10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::BuildBlendTreesJob *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  Handler *Qt3DAnimation::Animation::BuildBlendTreesJob::handler() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Handler *ritual_ZNK13Qt3DAnimation9Animation18BuildBlendTreesJob7handlerEv(
    const Qt3DAnimation::Animation::BuildBlendTreesJob *self) {
  return self->handler();
}

//  void Qt3DAnimation::Animation::BuildBlendTreesJob::setBlendedClipAnimator
//      s(const QVector<HBlendedClipAnimator> &blendedClipAnimatorHandles)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation18BuildBlendTreesJob23setBlendedClipAnimatorsERK5QListIN8Qt3DCore7QHandleINS0_19BlendedClipAnimatorEEEE(
    Qt3DAnimation::Animation::BuildBlendTreesJob *self,
    const QVector<Qt3DAnimation::Animation::HBlendedClipAnimator> *blendedClipAnimatorHandles) {
  self->setBlendedClipAnimators(*blendedClipAnimatorHandles);
}

//  void Qt3DAnimation::Animation::BuildBlendTreesJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation18BuildBlendTreesJob3runEv(
    Qt3DAnimation::Animation::BuildBlendTreesJob *self) {
  self->run();
}
