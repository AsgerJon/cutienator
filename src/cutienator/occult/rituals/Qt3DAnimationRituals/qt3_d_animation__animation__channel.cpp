//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <Qt3DAnimation/qchannel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/private/bezierevaluator_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/QLatin1String>
#include <Qt3DAnimation/private/functionrangefinder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 192, as _ZN13Qt3DAnimation9Animation16ChannelComponent4readERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline void ChannelComponent::read(const QJsonObject &json)
{
    name = json[QLatin1String("channelComponentName")].toString();
    fcurve.read(json);
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 16, as _ZN13Qt3DAnimation9Animation6FCurveC1Ev
namespace Qt3DAnimation::Animation {
inline FCurve::FCurve()
    : m_rangeFinder(&m_localTimes)
{
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

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 134, as _ZN13Qt3DAnimation9Animation6FCurve4readERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline void FCurve::read(const QJsonObject &json)
{
    clearKeyframes();

    const QJsonArray keyframeArray = json[QLatin1String("keyFrames")].toArray();
    const qsizetype keyframeCount = keyframeArray.size();

    for (int i = 0; i < keyframeCount; ++i) {
        const QJsonObject keyframeData = keyframeArray.at(i).toObject();

        // Extract the keyframe local time and value
        const QJsonArray keyframeCoords = keyframeData[QLatin1String("coords")].toArray();
        float localTime = keyframeCoords.at(0).toDouble();

        Keyframe keyframe;
        keyframe.value = keyframeCoords.at(1).toDouble();

        if (keyframeData.contains(QLatin1String("leftHandle"))) {
            keyframe.interpolation = QKeyFrame::BezierInterpolation;

            const QJsonArray leftHandle = keyframeData[QLatin1String("leftHandle")].toArray();
            keyframe.leftControlPoint[0] = leftHandle.at(0).toDouble();
            keyframe.leftControlPoint[1] = leftHandle.at(1).toDouble();

            const QJsonArray rightHandle = keyframeData[QLatin1String("rightHandle")].toArray();
            keyframe.rightControlPoint[0] = rightHandle.at(0).toDouble();
            keyframe.rightControlPoint[1] = rightHandle.at(1).toDouble();
        } else {
            keyframe.interpolation = QKeyFrame::LinearInterpolation;
        }

        appendKeyframe(localTime, keyframe);
    }

    // TODO: Ensure beziers have no loops or cusps by scaling the control points
    // back so they do not interset.
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

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 204, as _ZN13Qt3DAnimation9Animation7Channel4readERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline void Channel::read(const QJsonObject &json)
{
    name = json[QLatin1String("channelName")].toString();
    const auto jointIndexValue = json[QLatin1String("jointIndex")];
    if (!jointIndexValue.isUndefined())
        jointIndex = jointIndexValue.toInt();
    const QJsonArray channelComponentsArray = json[QLatin1String("channelComponents")].toArray();
    const qsizetype channelCount = channelComponentsArray.size();
    channelComponents.resize(channelCount);

    for (qsizetype i = 0; i < channelCount; ++i) {
        const QJsonObject channel = channelComponentsArray.at(i).toObject();
        channelComponents[i].read(channel);
    }
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
//  -----------------------------------------------------------------------

//  void Qt3DAnimation::Animation::Channel::read(const QJsonObject &json)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Channel4readERK11QJsonObject(
    Qt3DAnimation::Animation::Channel *self,
    const QJsonObject *json) {
  self->read(*json);
}

//  void Qt3DAnimation::Animation::Channel::setFromQChannel(const QChannel
//      &qch)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7Channel15setFromQChannelERKNS_8QChannelE(
    Qt3DAnimation::Animation::Channel *self,
    const Qt3DAnimation::QChannel *qch) {
  self->setFromQChannel(*qch);
}

//  Qt3DAnimation::Animation::Channel::~Channel()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation7ChannelD1Ev(
    Qt3DAnimation::Animation::Channel *self) {
  delete self;
}
