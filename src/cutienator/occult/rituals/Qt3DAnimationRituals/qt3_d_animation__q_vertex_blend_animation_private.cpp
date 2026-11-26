//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qvertexblendanimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qvertexblendanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qabstractanimation.h>
#include "Qt3DAnimation/private/qabstractanimation_p.h"
#include <Qt3DAnimation/qvertexblendanimation.h>
#include <Qt3DAnimation/private/qvertexblendanimation_p.h>
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

//  from ../qt3d/src/animation/frontend/qvertexblendanimation.cpp, line 110, as _ZN13Qt3DAnimation28QVertexBlendAnimationPrivateC1Ev
namespace Qt3DAnimation {
inline QVertexBlendAnimationPrivate::QVertexBlendAnimationPrivate()
    : QAbstractAnimationPrivate(QAbstractAnimation::VertexBlendAnimation)
    , m_interpolator(0.0f)
    , m_target(nullptr)
    , m_currentBase(nullptr)
    , m_currentTarget(nullptr)
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qvertexblendanimation.cpp, line 120, as _ZN13Qt3DAnimation28QVertexBlendAnimationPrivate23getAttributesInPositionEfPiS1_Pf
namespace Qt3DAnimation {
inline void QVertexBlendAnimationPrivate::getAttributesInPosition(float position, int *target0,
                                                           int *target1, float *interpolator)
{
    if (position < m_targetPositions.first()) {
        *target0 = 0;
        *target1 = qMin(1, m_targetPositions.size());
        *interpolator = 0.0f;
    } else if (position > m_targetPositions.last()) {
        *target0 = qMax(m_targetPositions.size() - 2, 0);
        *target1 = qMax(m_targetPositions.size() - 1, 0);
        *interpolator = 1.0f;
    } else {
        for (int i = 0; i < m_targetPositions.size() - 1; i++) {
            if (position >= m_targetPositions[i] && position < m_targetPositions[i + 1]) {
                *target0 = i;
                *target1 = i + 1;
                float a = (position - m_targetPositions[i])
                            / (m_targetPositions[i + 1] - m_targetPositions[i]);
                *interpolator = a;
            }
        }
    }
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qvertexblendanimation.cpp, line 144, as _ZN13Qt3DAnimation28QVertexBlendAnimationPrivate15updateAnimationEf
namespace Qt3DAnimation {
inline void QVertexBlendAnimationPrivate::updateAnimation(float position)
{
    Q_Q(QVertexBlendAnimation);
    if (!m_target || !m_target->geometry())
        return;

    Qt3DAnimation::QMorphTarget *base;
    Qt3DAnimation::QMorphTarget *target;
    int target0, target1;
    float interpolator;
    getAttributesInPosition(position, &target0, &target1, &interpolator);

    base = m_morphTargets.at(target0);
    target = m_morphTargets.at(target1);

    Qt3DCore::QGeometry *geometry = m_target->geometry();

    // remove attributes from previous frame
    if (m_currentBase && m_currentTarget &&
        (base != m_currentBase || target != m_currentTarget)) {
        const QList<Qt3DCore::QAttribute *> baseAttributes = m_currentBase->attributeList();
        const QList<Qt3DCore::QAttribute *> targetAttributes = m_currentTarget->attributeList();
        for (int i = 0; i < baseAttributes.size(); ++i) {
            geometry->removeAttribute(baseAttributes.at(i));
            geometry->removeAttribute(targetAttributes.at(i));
        }
    }

    const QList<Qt3DCore::QAttribute *> baseAttributes = base->attributeList();
    const QList<Qt3DCore::QAttribute *> targetAttributes = target->attributeList();
    const QStringList attributeNames = base->attributeNames();

    // add attributes from current frame to the geometry
    if (base != m_currentBase || target != m_currentTarget) {
        for (int i = 0; i < baseAttributes.size(); ++i) {
            const QString baseName = attributeNames.at(i);
            QString targetName = baseName;
            targetName.append(QLatin1String("Target"));

            baseAttributes[i]->setName(baseName);
            geometry->addAttribute(baseAttributes.at(i));
            targetAttributes[i]->setName(targetName);
            geometry->addAttribute(targetAttributes.at(i));
        }
    }
    m_currentBase = base;
    m_currentTarget = target;

    if (!qFuzzyCompare(interpolator, m_interpolator)) {
        m_interpolator = interpolator;
        emit q->interpolatorChanged(interpolator);
    }
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QVertexBlendAnimationPrivate::QVertexBlendAnimationPrivate
//      ()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QVertexBlendAnimationPrivate *ritual_ZN13Qt3DAnimation28QVertexBlendAnimationPrivateC1Ev() {
  return new Qt3DAnimation::QVertexBlendAnimationPrivate();
}

//  void Qt3DAnimation::QVertexBlendAnimationPrivate::getAttributesInPosition
//      (float position, int *target0, int *target1, float *interpolator)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation28QVertexBlendAnimationPrivate23getAttributesInPositionEfPiS1_Pf(
    Qt3DAnimation::QVertexBlendAnimationPrivate *self,
    float position,
    int *target0,
    int *target1,
    float *interpolator) {
  self->getAttributesInPosition(position, target0, target1, interpolator);
}

//  void Qt3DAnimation::QVertexBlendAnimationPrivate::updateAnimation(float
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation28QVertexBlendAnimationPrivate15updateAnimationEf(
    Qt3DAnimation::QVertexBlendAnimationPrivate *self,
    float position) {
  self->updateAnimation(position);
}

//  QVertexBlendAnimation
//      *Qt3DAnimation::QVertexBlendAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QVertexBlendAnimation *ritual_ZN13Qt3DAnimation28QVertexBlendAnimationPrivate6q_funcEv(
    Qt3DAnimation::QVertexBlendAnimationPrivate *self) {
  return self->q_func();
}

//  const QVertexBlendAnimation
//      *Qt3DAnimation::QVertexBlendAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QVertexBlendAnimation *ritual_ZNK13Qt3DAnimation28QVertexBlendAnimationPrivate6q_funcEv(
    const Qt3DAnimation::QVertexBlendAnimationPrivate *self) {
  return self->q_func();
}
