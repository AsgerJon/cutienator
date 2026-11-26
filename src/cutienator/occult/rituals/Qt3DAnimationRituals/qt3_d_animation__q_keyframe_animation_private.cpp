//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qkeyframeanimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qkeyframeanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qabstractanimation.h>
#include "Qt3DAnimation/private/qabstractanimation_p.h"
#include <Qt3DAnimation/qkeyframeanimation.h>
#include "Qt3DAnimation/private/qkeyframeanimation_p.h"
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from ../qt3d/src/animation/frontend/qkeyframeanimation.cpp, line 125, as _ZN13Qt3DAnimation25QKeyframeAnimationPrivateC1Ev
namespace Qt3DAnimation {
inline QKeyframeAnimationPrivate::QKeyframeAnimationPrivate()
    : QAbstractAnimationPrivate(QAbstractAnimation::KeyframeAnimation)
    , m_target(nullptr)
    , m_minposition(0.0f)
    , m_maxposition(0.0f)
    , m_startMode(QKeyframeAnimation::Constant)
    , m_endMode(QKeyframeAnimation::Constant)
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qkeyframeanimation.cpp, line 200, as _ZN13Qt3DAnimation25QKeyframeAnimationPrivate14calculateFrameEf
namespace Qt3DAnimation {
inline void QKeyframeAnimationPrivate::calculateFrame(float position)
{
    if (m_target && m_framePositions.size() > 0
        && m_keyframes.size() == m_framePositions.size()) {
        if (position < m_minposition) {
            if (m_startMode == QKeyframeAnimation::None) {
                return;
            } else if (m_startMode == QKeyframeAnimation::Constant) {
                m_target->setRotation(m_keyframes.first()->rotation());
                m_target->setScale3D(m_keyframes.first()->scale3D());
                m_target->setTranslation(m_keyframes.first()->translation());
                return;
            } else {
                // must be repeat
                position = std::fmod(-(position - m_minposition), m_maxposition - m_minposition)
                                     + m_minposition;
            }
        } else if (position >= m_maxposition) {
            if (m_endMode == QKeyframeAnimation::None) {
                return;
            } else if (m_endMode == QKeyframeAnimation::Constant) {
                m_target->setRotation(m_keyframes.last()->rotation());
                m_target->setScale3D(m_keyframes.last()->scale3D());
                m_target->setTranslation(m_keyframes.last()->translation());
                return;
            } else {
                // must be repeat
                position = std::fmod(position - m_minposition, m_maxposition - m_minposition)
                                     + m_minposition;
            }
        }
        if (position >= m_minposition && position < m_maxposition) {
            for (int i = 0; i < m_framePositions.size() - 1; i++) {
                if (position >= m_framePositions.at(i)
                    && position < m_framePositions.at(i+1)) {
                    float ip = (position - m_framePositions.at(i))
                                / (m_framePositions.at(i+1) - m_framePositions.at(i));
                    float eIp = m_easing.valueForProgress(ip);
                    float eIip = 1.0f - eIp;

                    Qt3DCore::QTransform *a = m_keyframes.at(i);
                    Qt3DCore::QTransform *b = m_keyframes.at(i+1);

                    QVector3D s = a->scale3D() * eIip + b->scale3D() * eIp;
                    QVector3D t = a->translation() * eIip + b->translation() * eIp;
                    QQuaternion r = QQuaternion::slerp(a->rotation(), b->rotation(), eIp);

                    m_target->setRotation(r);
                    m_target->setScale3D(s);
                    m_target->setTranslation(t);
                    return;
                }
            }
        }
    }
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QKeyframeAnimationPrivate::QKeyframeAnimationPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimationPrivate *ritual_ZN13Qt3DAnimation25QKeyframeAnimationPrivateC1Ev() {
  return new Qt3DAnimation::QKeyframeAnimationPrivate();
}

//  void Qt3DAnimation::QKeyframeAnimationPrivate::calculateFrame(float
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation25QKeyframeAnimationPrivate14calculateFrameEf(
    Qt3DAnimation::QKeyframeAnimationPrivate *self,
    float position) {
  self->calculateFrame(position);
}

//  QKeyframeAnimation *Qt3DAnimation::QKeyframeAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QKeyframeAnimation *ritual_ZN13Qt3DAnimation25QKeyframeAnimationPrivate6q_funcEv(
    Qt3DAnimation::QKeyframeAnimationPrivate *self) {
  return self->q_func();
}

//  const QKeyframeAnimation
//      *Qt3DAnimation::QKeyframeAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QKeyframeAnimation *ritual_ZNK13Qt3DAnimation25QKeyframeAnimationPrivate6q_funcEv(
    const Qt3DAnimation::QKeyframeAnimationPrivate *self) {
  return self->q_func();
}
