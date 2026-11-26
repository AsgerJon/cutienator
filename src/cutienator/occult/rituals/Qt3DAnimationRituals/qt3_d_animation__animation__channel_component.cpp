//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <Qt3DAnimation/qchannelcomponent.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/private/bezierevaluator_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/QLatin1String>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 192, as _ZN13Qt3DAnimation9Animation16ChannelComponent4readERK11QJsonObject
namespace Qt3DAnimation::Animation {
inline void ChannelComponent::read(const QJsonObject &json)
{
    name = json[QLatin1String("channelComponentName")].toString();
    fcurve.read(json);
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
//  -----------------------------------------------------------------------

//  void Qt3DAnimation::Animation::ChannelComponent::read(const QJsonObject
//      &json)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation16ChannelComponent4readERK11QJsonObject(
    Qt3DAnimation::Animation::ChannelComponent *self,
    const QJsonObject *json) {
  self->read(*json);
}

//  void Qt3DAnimation::Animation::ChannelComponent::setFromQChannelComponent
//      (const QChannelComponent &qcc)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation16ChannelComponent24setFromQChannelComponentERKNS_17QChannelComponentE(
    Qt3DAnimation::Animation::ChannelComponent *self,
    const Qt3DAnimation::QChannelComponent *qcc) {
  self->setFromQChannelComponent(*qcc);
}

//  Qt3DAnimation::Animation::ChannelComponent::~ChannelComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation16ChannelComponentD1Ev(
    Qt3DAnimation::Animation::ChannelComponent *self) {
  delete self;
}
