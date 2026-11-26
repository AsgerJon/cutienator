//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qmorphinganimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qmorphinganimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qabstractanimation.h>
#include "Qt3DAnimation/private/qabstractanimation_p.h"
#include <Qt3DAnimation/qmorphinganimation.h>
#include <Qt3DAnimation/private/qmorphinganimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qabstractanimation.cpp, line 85, as _ZN13Qt3DAnimation25QAbstractAnimationPrivateC2ENS_18QAbstractAnimation13AnimationTypeE
namespace Qt3DAnimation {
inline QAbstractAnimationPrivate::QAbstractAnimationPrivate(QAbstractAnimation::AnimationType type)
    : QObjectPrivate()
    , m_animationType(type)
    , m_position(0.0f)
    , m_duration(0.0f)
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qmorphinganimation.cpp, line 134, as _ZN13Qt3DAnimation25QMorphingAnimationPrivateC1Ev
namespace Qt3DAnimation {
inline QMorphingAnimationPrivate::QMorphingAnimationPrivate()
    : QAbstractAnimationPrivate(QAbstractAnimation::MorphingAnimation)
    , m_minposition(0.0f)
    , m_maxposition(0.0f)
    , m_flattened(nullptr)
    , m_method(QMorphingAnimation::Relative)
    , m_interpolator(0.0f)
    , m_target(nullptr)
    , m_currentTarget(nullptr)
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qmorphinganimation.cpp, line 147, as _ZN13Qt3DAnimation25QMorphingAnimationPrivateD1Ev
namespace Qt3DAnimation {
inline QMorphingAnimationPrivate::~QMorphingAnimationPrivate()
{
    for (QVector<float> *weights : std::as_const(m_weights))
        delete weights;
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qmorphinganimation.cpp, line 153, as _ZN13Qt3DAnimation25QMorphingAnimationPrivate15updateAnimationEf
namespace Qt3DAnimation {
inline void QMorphingAnimationPrivate::updateAnimation(float position)
{
    Q_Q(QMorphingAnimation);
    if (!m_target || !m_target->geometry())
        return;

    QVector<int> relevantValues;
    float sum = 0.0f;
    float interpolator = 0.0f;
    m_morphKey.resize(m_morphTargets.size());

    // calculate morph key
    if (position < m_minposition) {
        m_morphKey = *m_weights.first();
    } else if (position >= m_maxposition) {
        m_morphKey = *m_weights.last();
    } else {
        for (int i = 0; i < m_targetPositions.size() - 1; ++i) {
            if (position >= m_targetPositions.at(i) && position < m_targetPositions.at(i + 1)) {
                interpolator = (position - m_targetPositions.at(i))
                        / (m_targetPositions.at(i + 1) - m_targetPositions.at(i));
                interpolator = m_easing.valueForProgress(interpolator);
                float iip = 1.0f - interpolator;

                for (int j = 0; j < m_morphTargets.size(); ++j) {
                    m_morphKey[j] = interpolator * m_weights.at(i + 1)->at(j)
                                        + iip * m_weights.at(i)->at(j);
                }
            }
        }
    }

    // check relevant values
    for (int j = 0; j < m_morphKey.size(); ++j) {
        sum += m_morphKey[j];
        if (!qFuzzyIsNull(m_morphKey[j]))
            relevantValues.push_back(j);
    }

    if (relevantValues.size() == 0 || qFuzzyIsNull(sum)) {
        // only base is used
        interpolator = 0.0f;
    } else if (relevantValues.size() == 1) {
        // one morph target has non-zero weight
        setTargetInterpolated(relevantValues[0]);
        interpolator = sum;
    } else {
        // more than one morph target has non-zero weight
        // flatten morph targets to one
        qWarning() << Q_FUNC_INFO << "Flattening required";
    }

    // Relative method uses negative interpolator, normalized uses positive
    if (m_method == QMorphingAnimation::Relative)
        interpolator = -interpolator;

    if (!qFuzzyCompare(interpolator, m_interpolator)) {
        m_interpolator = interpolator;
        emit q->interpolatorChanged(m_interpolator);
    }
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qmorphinganimation.cpp, line 215, as _ZN13Qt3DAnimation25QMorphingAnimationPrivate21setTargetInterpolatedEi
namespace Qt3DAnimation {
inline void QMorphingAnimationPrivate::setTargetInterpolated(int morphTarget)
{
    QMorphTarget *target = m_morphTargets[morphTarget];
    Qt3DCore::QGeometry *geometry = m_target->geometry();

    // remove attributes from previous frame
    if (m_currentTarget && (target != m_currentTarget)) {
        const QList<Qt3DCore::QAttribute *> targetAttributes = m_currentTarget->attributeList();
        for (int i = 0; i < targetAttributes.size(); ++i)
            geometry->removeAttribute(targetAttributes.at(i));
    }

    const QList<Qt3DCore::QAttribute *> targetAttributes = target->attributeList();

    // add attributes from current frame to the geometry
    if (target != m_currentTarget) {
        for (int i = 0; i < m_attributeNames.size(); ++i) {
            QString targetName = m_attributeNames.at(i);
            targetName.append(QLatin1String("Target"));
            targetAttributes[i]->setName(targetName);
            geometry->addAttribute(targetAttributes.at(i));
        }
    }
    m_currentTarget = target;
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QMorphingAnimationPrivate::QMorphingAnimationPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphingAnimationPrivate *ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivateC1Ev() {
  return new Qt3DAnimation::QMorphingAnimationPrivate();
}

//  Qt3DAnimation::QMorphingAnimationPrivate::~QMorphingAnimationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivateD1Ev(
    Qt3DAnimation::QMorphingAnimationPrivate *self) {
  delete self;
}

//  void Qt3DAnimation::QMorphingAnimationPrivate::updateAnimation(float
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivate15updateAnimationEf(
    Qt3DAnimation::QMorphingAnimationPrivate *self,
    float position) {
  self->updateAnimation(position);
}

//  void Qt3DAnimation::QMorphingAnimationPrivate::setTargetInterpolated(int
//      morphTarget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivate21setTargetInterpolatedEi(
    Qt3DAnimation::QMorphingAnimationPrivate *self,
    int morphTarget) {
  self->setTargetInterpolated(morphTarget);
}

//  QMorphingAnimation *Qt3DAnimation::QMorphingAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QMorphingAnimation *ritual_ZN13Qt3DAnimation25QMorphingAnimationPrivate6q_funcEv(
    Qt3DAnimation::QMorphingAnimationPrivate *self) {
  return self->q_func();
}

//  const QMorphingAnimation
//      *Qt3DAnimation::QMorphingAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QMorphingAnimation *ritual_ZNK13Qt3DAnimation25QMorphingAnimationPrivate6q_funcEv(
    const Qt3DAnimation::QMorphingAnimationPrivate *self) {
  return self->q_func();
}
