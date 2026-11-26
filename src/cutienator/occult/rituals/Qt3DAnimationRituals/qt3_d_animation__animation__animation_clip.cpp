//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationclip_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationclip_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
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
#include <QtCore/qloggingcategory.h>
#include <Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/private/bezierevaluator_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/QLatin1String>
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
#include <Qt3DAnimation/private/functionrangefinder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 23, as local:animationclip.cpp:ANIMATION_INDEX_KEY
#define ANIMATION_INDEX_KEY     QLatin1String("animationIndex")

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 24, as local:animationclip.cpp:ANIMATION_NAME_KEY
#define ANIMATION_NAME_KEY      QLatin1String("animationName")

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
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

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 28, as _ZN13Qt3DAnimation9Animation11BackendNode8setDirtyENS0_7Handler9DirtyFlagE
namespace Qt3DAnimation::Animation {
inline void BackendNode::setDirty(Handler::DirtyFlag flag)
{
    Q_ASSERT(m_handler);
    m_handler->setDirty(flag, peerId());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/animationlogging.cpp, line 13, as _ZN13Qt3DAnimation9Animation4JobsEv
namespace Qt3DAnimation::Animation {
inline const QLoggingCategory &Jobs()
{
    static const QLoggingCategory category("Qt3D.Animation.Jobs", QtWarningMsg);
    return category;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 220, as _ZN13Qt3DAnimation9Animation7Channel15setFromQChannelERKNS_8QChannelE
namespace Qt3DAnimation::Animation {
inline void Channel::setFromQChannel(const QChannel &qch)
{
    name = qch.name();
    jointIndex = qch.jointIndex();
    channelComponents.resize(qch.channelComponentCount());
    qsizetype i = 0;
    for (const auto &frontendChannelComponent : qch)
        channelComponents[i++].setFromQChannelComponent(frontendChannelComponent);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 121, as _ZNK13Qt3DAnimation9Animation6FCurve7endTimeEv
namespace Qt3DAnimation::Animation {
inline float FCurve::endTime() const
{
    if (!m_localTimes.isEmpty())
        return m_localTimes.last();
    return 0.0f;
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

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 198, as _ZN13Qt3DAnimation9Animation16ChannelComponent24setFromQChannelComponentERKNS_17QChannelComponentE
namespace Qt3DAnimation::Animation {
inline void ChannelComponent::setFromQChannelComponent(const QChannelComponent &qcc)
{
    name = qcc.name();
    fcurve.setFromQChannelComponent(qcc);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 16, as _ZN13Qt3DAnimation9Animation6FCurveC1Ev
namespace Qt3DAnimation::Animation {
inline FCurve::FCurve()
    : m_rangeFinder(&m_localTimes)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 39, as _ZN13Qt3DAnimation9Animation19FunctionRangeFinderC1EP5QListIfE
namespace Qt3DAnimation::Animation {
inline FunctionRangeFinder::FunctionRangeFinder(QList<float> *x)
    : m_x(x)
    , m_previousLowerBound(0)
    , m_correlated(0)
    , m_rangeSize(2)
    , m_correlationThreshold(1)
    , m_ascending(true)
{
    updateAutomaticCorrelationThreshold();
    if (!m_x->isEmpty())
        m_ascending = (m_x->last() >= m_x->first());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 172, as _ZN13Qt3DAnimation9Animation6FCurve24setFromQChannelComponentERKNS_17QChannelComponentE
namespace Qt3DAnimation::Animation {
inline void FCurve::setFromQChannelComponent(const QChannelComponent &qcc)
{
    clearKeyframes();

    for (const auto &frontendKeyFrame : qcc) {
        // Extract the keyframe local time and value
        const float localTime = frontendKeyFrame.coordinates()[0];

        Keyframe keyFrame;
        keyFrame.interpolation = frontendKeyFrame.interpolationType();
        keyFrame.value = frontendKeyFrame.coordinates()[1];
        keyFrame.leftControlPoint = frontendKeyFrame.leftControlPoint();
        keyFrame.rightControlPoint = frontendKeyFrame.rightControlPoint();
        appendKeyframe(localTime, keyFrame);
    }

    // TODO: Ensure beziers have no loops or cusps by scaling the control points
    // back so they do not interset.
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 128, as _ZN13Qt3DAnimation9Animation6FCurve14appendKeyframeEfRKNS0_8KeyframeE
namespace Qt3DAnimation::Animation {
inline void FCurve::appendKeyframe(float localTime, const Keyframe &keyframe)
{
    m_localTimes.append(localTime);
    m_keyframes.append(keyframe);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 29, as _ZN13Qt3DAnimation9Animation13AnimationClipC1Ev
namespace Qt3DAnimation::Animation {
inline AnimationClip::AnimationClip()
    : BackendNode(ReadWrite)
    , m_source()
    , m_status(QAnimationClipLoader::NotReady)
    , m_clipData()
    , m_dataType(Unknown)
    , m_name()
    , m_channels()
    , m_duration(0.0f)
    , m_channelComponentCount(0)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 42, as _ZN13Qt3DAnimation9Animation13AnimationClip7cleanupEv
namespace Qt3DAnimation::Animation {
inline void AnimationClip::cleanup()
{
    setEnabled(false);
    m_handler = nullptr;
    m_source.clear();
    m_clipData.clearChannels();
    m_status = QAnimationClipLoader::NotReady;
    m_dataType = Unknown;
    m_channels.clear();
    m_duration = 0.0f;
    m_channelComponentCount = 0;

    clearData();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 57, as _ZN13Qt3DAnimation9Animation13AnimationClip9setStatusENS_20QAnimationClipLoader6StatusE
namespace Qt3DAnimation::Animation {
inline void AnimationClip::setStatus(QAnimationClipLoader::Status status)
{
    if (status != m_status) {
        m_status = status;
    }
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

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 277, as _ZN13Qt3DAnimation9Animation13AnimationClip11setDurationEf
namespace Qt3DAnimation::Animation {
inline void AnimationClip::setDuration(float duration)
{
    if (qFuzzyCompare(duration, m_duration))
        return;

    m_duration = duration;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 285, as _ZNK13Qt3DAnimation9Animation13AnimationClip12channelIndexERK7QStringx
namespace Qt3DAnimation::Animation {
inline qsizetype AnimationClip::channelIndex(const QString &channelName, qsizetype jointIndex) const
{
    const qsizetype channelCount = m_channels.size();
    for (qsizetype i = 0; i < channelCount; ++i) {
        if (m_channels[i].name == channelName
            && (jointIndex == -1 || m_channels[i].jointIndex == jointIndex)) {
            return i;
        }
    }
    return -1;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 307, as _ZNK13Qt3DAnimation9Animation13AnimationClip25channelComponentBaseIndexEx
namespace Qt3DAnimation::Animation {
inline qsizetype AnimationClip::channelComponentBaseIndex(qsizetype channelIndex) const
{
    qsizetype index = 0;
    for (qsizetype i = 0; i < channelIndex; ++i)
        index += m_channels[i].channelComponents.size();
    return index;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 256, as _ZN13Qt3DAnimation9Animation13AnimationClip21loadAnimationFromDataEv
namespace Qt3DAnimation::Animation {
inline void AnimationClip::loadAnimationFromData()
{
    // Reformat data from QAnimationClipData to backend format
    m_channels.resize(m_clipData.channelCount());
    qsizetype i = 0;
    for (const auto &frontendChannel : std::as_const(m_clipData))
        m_channels[i++].setFromQChannel(frontendChannel);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 315, as _ZN13Qt3DAnimation9Animation13AnimationClip9clearDataEv
namespace Qt3DAnimation::Animation {
inline void AnimationClip::clearData()
{
    m_name.clear();
    m_channels.clear();
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 321, as _ZN13Qt3DAnimation9Animation13AnimationClip12findDurationEv
namespace Qt3DAnimation::Animation {
inline float AnimationClip::findDuration()
{
    // Iterate over the contained fcurves and find the longest one
    float tMax = 0.f;
    for (const Channel &channel : std::as_const(m_channels)) {
        for (const ChannelComponent &channelComponent : std::as_const(channel.channelComponents)) {
            const float t = channelComponent.fcurve.endTime();
            if (t > tMax)
                tMax = t;
        }
    }
    return tMax;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/animationclip.cpp, line 335, as _ZN13Qt3DAnimation9Animation13AnimationClip25findChannelComponentCountEv
namespace Qt3DAnimation::Animation {
inline qsizetype AnimationClip::findChannelComponentCount()
{
    qsizetype channelCount = 0;
    for (const Channel &channel : std::as_const(m_channels))
        channelCount += channel.channelComponents.size();
    return channelCount;
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::AnimationClip::AnimationClip()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::AnimationClip *ritual_ZN13Qt3DAnimation9Animation13AnimationClipC1Ev() {
  return new Qt3DAnimation::Animation::AnimationClip();
}

//  void Qt3DAnimation::Animation::AnimationClip::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip7cleanupEv(
    Qt3DAnimation::Animation::AnimationClip *self) {
  self->cleanup();
}

//  void Qt3DAnimation::Animation::AnimationClip::setSource(const QUrl
//      &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip9setSourceERK4QUrl(
    Qt3DAnimation::Animation::AnimationClip *self,
    const QUrl *source) {
  self->setSource(*source);
}

//  QUrl Qt3DAnimation::Animation::AnimationClip::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK13Qt3DAnimation9Animation13AnimationClip6sourceEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return new QUrl(self->source());
}

//  void Qt3DAnimation::Animation::AnimationClip::setStatus(QAnimationClipLoa
//      der::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip9setStatusENS_20QAnimationClipLoader6StatusE(
    Qt3DAnimation::Animation::AnimationClip *self,
    Qt3DAnimation::QAnimationClipLoader::Status status) {
  self->setStatus(status);
}

//  QAnimationClipLoader::Status
//      Qt3DAnimation::Animation::AnimationClip::status() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationClipLoader::Status ritual_ZNK13Qt3DAnimation9Animation13AnimationClip6statusEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return self->status();
}

//  void Qt3DAnimation::Animation::AnimationClip::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::AnimationClip *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void
//      Qt3DAnimation::Animation::AnimationClip::addDependingClipAnimator(con
//      st Qt3DCore::QNodeId &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip24addDependingClipAnimatorERKN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::AnimationClip *self,
    const Qt3DCore::QNodeId *id) {
  self->addDependingClipAnimator(*id);
}

//  void Qt3DAnimation::Animation::AnimationClip::addDependingBlendedClipAnim
//      ator(const Qt3DCore::QNodeId &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip31addDependingBlendedClipAnimatorERKN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::AnimationClip *self,
    const Qt3DCore::QNodeId *id) {
  self->addDependingBlendedClipAnimator(*id);
}

//  QString Qt3DAnimation::Animation::AnimationClip::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation9Animation13AnimationClip4nameEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return new QString(self->name());
}

//  const QVector<Channel>
//      &Qt3DAnimation::Animation::AnimationClip::channels() const
extern "C" Q_DECL_EXPORT
const QVector<Qt3DAnimation::Animation::Channel> *ritual_ZNK13Qt3DAnimation9Animation13AnimationClip8channelsEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return &(self->channels());
}

//  void Qt3DAnimation::Animation::AnimationClip::setDuration(float duration)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip11setDurationEf(
    Qt3DAnimation::Animation::AnimationClip *self,
    float duration) {
  self->setDuration(duration);
}

//  float Qt3DAnimation::Animation::AnimationClip::duration() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation13AnimationClip8durationEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return self->duration();
}

//  qsizetype Qt3DAnimation::Animation::AnimationClip::channelIndex(const
//      QString &channelName, qsizetype jointIndex) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13Qt3DAnimation9Animation13AnimationClip12channelIndexERK7QStringx(
    const Qt3DAnimation::Animation::AnimationClip *self,
    const QString *channelName,
    qsizetype jointIndex) {
  return self->channelIndex(*channelName, jointIndex);
}

//  qsizetype Qt3DAnimation::Animation::AnimationClip::channelCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13Qt3DAnimation9Animation13AnimationClip12channelCountEv(
    const Qt3DAnimation::Animation::AnimationClip *self) {
  return self->channelCount();
}

//  qsizetype Qt3DAnimation::Animation::AnimationClip::channelComponentBaseIn
//      dex(qsizetype channelGroupIndex) const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13Qt3DAnimation9Animation13AnimationClip25channelComponentBaseIndexEx(
    const Qt3DAnimation::Animation::AnimationClip *self,
    qsizetype channelGroupIndex) {
  return self->channelComponentBaseIndex(channelGroupIndex);
}

//  void Qt3DAnimation::Animation::AnimationClip::loadAnimationFromData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip21loadAnimationFromDataEv(
    Qt3DAnimation::Animation::AnimationClip *self) {
  self->loadAnimationFromData();
}

//  void Qt3DAnimation::Animation::AnimationClip::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13AnimationClip9clearDataEv(
    Qt3DAnimation::Animation::AnimationClip *self) {
  self->clearData();
}

//  float Qt3DAnimation::Animation::AnimationClip::findDuration()
extern "C" Q_DECL_EXPORT
float ritual_ZN13Qt3DAnimation9Animation13AnimationClip12findDurationEv(
    Qt3DAnimation::Animation::AnimationClip *self) {
  return self->findDuration();
}

//  qsizetype
//      Qt3DAnimation::Animation::AnimationClip::findChannelComponentCount()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN13Qt3DAnimation9Animation13AnimationClip25findChannelComponentCountEv(
    Qt3DAnimation::Animation::AnimationClip *self) {
  return self->findChannelComponentCount();
}

//  void Qt3DAnimation::Animation::AnimationClip::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation13AnimationClip16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::AnimationClip *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::AnimationClip::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
