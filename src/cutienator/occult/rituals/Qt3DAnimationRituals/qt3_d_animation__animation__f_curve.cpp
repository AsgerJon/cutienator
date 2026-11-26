//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 1. Kept as it is when the generator runs again.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/keyframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qjsonobject.h>
#include <Qt3DAnimation/qchannelcomponent.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/functionrangefinder_p.h>
#include <Qt3DAnimation/private/bezierevaluator_p.h>
#include <Qt3DAnimation/private/keyframe_p.h>
#include <QtCore/qglobal.h>
#include <QtCore/qdebug.h>
#include <cmath>
#include <Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/private/bezierevaluator_p.h>
#include <QtCore/qjsonarray.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/QLatin1String>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/bezierevaluator.cpp, line 130, as local:bezierevaluator.cpp:almostZero
namespace Qt3DAnimation::Animation {
inline bool almostZero(float value, float threshold=1e-3f)
{
    // 1e-3 might seem excessively fuzzy, but any smaller value will make the
    // factors a, b, and c large enough to knock out the cubic solver.
    return value > -threshold && value < threshold;
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

//  from ../qt3d/src/animation/backend/bezierevaluator.cpp, line 46, as _ZNK13Qt3DAnimation9Animation15BezierEvaluator12valueForTimeEf
namespace Qt3DAnimation::Animation {
inline float BezierEvaluator::valueForTime(float time) const
{
    const float u = parameterForTime(time);

    // Calculate powers of u and (1-u) that we need
    const float u2 = u * u;
    const float u3 = u2 * u;
    const float mu = 1.0f - u;
    const float mu2 = mu * mu;
    const float mu3 = mu2 * mu;

    // The cubic Bezier control points
    const float p0 = m_keyframe0.value;
    const float p1 = m_keyframe0.rightControlPoint.y();
    const float p2 = m_keyframe1.leftControlPoint.y();
    const float p3 = m_keyframe1.value;

    // Evaluate the cubic Bezier function
    return p0 * mu3 + 3.0f * p1 * mu2 * u + 3.0f * p2 * mu * u2 + p3 * u3;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 81, as _ZNK13Qt3DAnimation9Animation19FunctionRangeFinder4huntEf
namespace Qt3DAnimation::Animation {
inline int FunctionRangeFinder::hunt(float x) const
{
    if (m_x->size() < 2 || m_rangeSize < 2 || m_rangeSize > m_x->size())
        return -1;

    qsizetype jLower = m_previousLowerBound;
    qsizetype jMid;
    qsizetype jUpper;
    if (jLower < 0 || jLower > (m_x->size() - 1)) {
        jLower = 0;
        jUpper = m_x->size() - 1;
    } else {
        qsizetype increment = 1;
        if ((x >= m_x->at(jLower)) == m_ascending) {
            for (;;) {
                jUpper = jLower + increment;
                if (jUpper >= m_x->size() - 1) {
                    jUpper = m_x->size() - 1;
                    break;
                } else if ((x < m_x->at(jUpper)) == m_ascending) {
                    break;
                } else {
                    jLower = jUpper;
                    increment += increment;
                }
            }
        } else {
            jUpper = jLower;
            for (;;) {
                jLower = jLower - increment;
                if (jLower <= 0) {
                    jLower = 0;
                    break;
                } else if ((x >= m_x->at(jLower)) == m_ascending) {
                    break;
                } else {
                    jUpper = jLower;
                    increment += increment;
                }
            }
        }
    }

    while (jUpper - jLower > 1) {
        jMid = (jUpper + jLower) >> 1;
        if ((x >= m_x->at(jMid)) == m_ascending)
            jLower = jMid;
        else
            jUpper = jMid;
    }

    m_correlated = std::abs(jLower - m_previousLowerBound) <= m_correlationThreshold;
    m_previousLowerBound = jLower;

    return qMax(0, qMin(m_x->size() - m_rangeSize, jLower - ((m_rangeSize - 2) >> 1)));
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/functionrangefinder.cpp, line 56, as _ZNK13Qt3DAnimation9Animation19FunctionRangeFinder6locateEf
namespace Qt3DAnimation::Animation {
inline int FunctionRangeFinder::locate(float x) const
{
    if (m_x->size() < 2 || m_rangeSize < 2 || m_rangeSize > m_x->size())
        return -1;

    qsizetype jLower = 0;
    qsizetype jUpper = m_x->size() - 1;
    while (jUpper - jLower > 1) {
        qsizetype jMid = (jUpper + jLower) >> 1;
        if ((x >= m_x->at(jMid)) == m_ascending)
            jLower = jMid;
        else
            jUpper = jMid;
    }

    m_correlated = std::abs(jLower - m_previousLowerBound) <= m_correlationThreshold;
    m_previousLowerBound = jLower;

    return qMax(0, qMin(m_x->size() - m_rangeSize, jLower - ((m_rangeSize - 2) >> 1)));
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/bezierevaluator.cpp, line 100, as _ZNK13Qt3DAnimation9Animation15BezierEvaluator16parameterForTimeEf
namespace Qt3DAnimation::Animation {
inline float BezierEvaluator::parameterForTime(float time) const
{
    Q_ASSERT(time >= m_time0);
    Q_ASSERT(time <= m_time1);

    const float p0 = m_time0;
    const float p1 = m_keyframe0.rightControlPoint.x();
    const float p2 = m_keyframe1.leftControlPoint.x();
    const float p3 = m_time1;

    const float coeffs[4] = {
        p0 - time,                      // d
        3.0f * (p1 - p0),               // c
        3.0f * (p0 - 2.0f * p1 + p2),   // b
        p3 - p0 + 3.0f * (p1 - p2)      // a
    };

    float roots[3];
    const int numberOfRoots = findCubicRoots(coeffs, roots);
    for (int i = 0; i < numberOfRoots; ++i) {
        if (roots[i] >= -0.01f && roots[i] <= 1.01f)
            return qMin(qMax(roots[i], 0.0f), 1.0f);
    }

    qWarning() << "Failed to find root of cubic bezier at time" << time
               << "with coeffs: a =" << coeffs[3] << "b =" << coeffs[2]
               << "c =" << coeffs[1] << "d =" << coeffs[0];
    return 0.0f;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 16, as _ZN13Qt3DAnimation9Animation6FCurveC1Ev
namespace Qt3DAnimation::Animation {
inline FCurve::FCurve()
    : m_rangeFinder(&m_localTimes)
{
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

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 114, as _ZNK13Qt3DAnimation9Animation6FCurve9startTimeEv
namespace Qt3DAnimation::Animation {
inline float FCurve::startTime() const
{
    if (!m_localTimes.isEmpty())
        return m_localTimes.first();
    return 0.0f;
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

//  from ../qt3d/src/animation/backend/fcurve.cpp, line 105, as _ZNK13Qt3DAnimation9Animation6FCurve18lowerKeyframeBoundEf
namespace Qt3DAnimation::Animation {
inline int FCurve::lowerKeyframeBound(float localTime) const
{
    if (localTime < m_localTimes.first())
        return 0;
    if (localTime > m_localTimes.last())
        return 0;
    return m_rangeFinder.findLowerBound(localTime);
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
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::FCurve::FCurve()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::FCurve *ritual_ZN13Qt3DAnimation9Animation6FCurveC1Ev() {
  return new Qt3DAnimation::Animation::FCurve();
}

//  int Qt3DAnimation::Animation::FCurve::keyframeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation6FCurve13keyframeCountEv(
    const Qt3DAnimation::Animation::FCurve *self) {
  return self->keyframeCount();
}

//  void Qt3DAnimation::Animation::FCurve::appendKeyframe(float localTime,
//      const Keyframe &keyframe)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation6FCurve14appendKeyframeEfRKNS0_8KeyframeE(
    Qt3DAnimation::Animation::FCurve *self,
    float localTime,
    const Qt3DAnimation::Animation::Keyframe *keyframe) {
  self->appendKeyframe(localTime, *keyframe);
}

//  void Qt3DAnimation::Animation::FCurve::clearKeyframes()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation6FCurve14clearKeyframesEv(
    Qt3DAnimation::Animation::FCurve *self) {
  self->clearKeyframes();
}

//  const float &Qt3DAnimation::Animation::FCurve::localTime(int index) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation6FCurve9localTimeEi(
    const Qt3DAnimation::Animation::FCurve *self,
    int index) {
  return self->localTime(index);
}

//  const Keyframe &Qt3DAnimation::Animation::FCurve::keyframe(int index)
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Keyframe *ritual_ZNK13Qt3DAnimation9Animation6FCurve8keyframeEi(
    const Qt3DAnimation::Animation::FCurve *self,
    int index) {
  return new Qt3DAnimation::Animation::Keyframe(self->keyframe(index));
}

//  Keyframe &Qt3DAnimation::Animation::FCurve::keyframe(int index)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Keyframe *ritual_ZN13Qt3DAnimation9Animation6FCurve8keyframeEi(
    Qt3DAnimation::Animation::FCurve *self,
    int index) {
  return &(self->keyframe(index));
}

//  float Qt3DAnimation::Animation::FCurve::startTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation6FCurve9startTimeEv(
    const Qt3DAnimation::Animation::FCurve *self) {
  return self->startTime();
}

//  float Qt3DAnimation::Animation::FCurve::endTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation6FCurve7endTimeEv(
    const Qt3DAnimation::Animation::FCurve *self) {
  return self->endTime();
}

//  int Qt3DAnimation::Animation::FCurve::lowerKeyframeBound(float localTime)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation6FCurve18lowerKeyframeBoundEf(
    const Qt3DAnimation::Animation::FCurve *self,
    float localTime) {
  return self->lowerKeyframeBound(localTime);
}

//  void Qt3DAnimation::Animation::FCurve::read(const QJsonObject &json)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation6FCurve4readERK11QJsonObject(
    Qt3DAnimation::Animation::FCurve *self,
    const QJsonObject *json) {
  self->read(*json);
}

//  void Qt3DAnimation::Animation::FCurve::setFromQChannelComponent(const
//      QChannelComponent &qcc)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation6FCurve24setFromQChannelComponentERKNS_17QChannelComponentE(
    Qt3DAnimation::Animation::FCurve *self,
    const Qt3DAnimation::QChannelComponent *qcc) {
  self->setFromQChannelComponent(*qcc);
}

//  Qt3DAnimation::Animation::FCurve::~FCurve()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation6FCurveD1Ev(
    Qt3DAnimation::Animation::FCurve *self) {
  delete self;
}

//  float &Qt3DAnimation::Animation::FCurve::localTime(int index)
extern "C" Q_DECL_EXPORT
float *ritual_ZN13Qt3DAnimation9Animation6FCurve9localTimeEi(
    Qt3DAnimation::Animation::FCurve *self,
    int index) {
  return &(self->localTime(index));
}
