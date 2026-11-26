//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractanimation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#if QT_CONFIG(animation)
#include <QtCore/qabstractanimation.h>
#endif
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractanimation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qabstractanimation.h>
#include "Qt3DAnimation/private/qabstractanimation_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qabstractanimation.cpp, line 85, as _ZN13Qt3DAnimation25QAbstractAnimationPrivateC1ENS_18QAbstractAnimation13AnimationTypeE
namespace Qt3DAnimation {
inline QAbstractAnimationPrivate::QAbstractAnimationPrivate(QAbstractAnimation::AnimationType type)
    : QObjectPrivate()
    , m_animationType(type)
    , m_position(0.0f)
    , m_duration(0.0f)
{

}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QAbstractAnimationPrivate::QAbstractAnimationPrivate(QAbst
//      ractAnimation::AnimationType type)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractAnimationPrivate *ritual_ZN13Qt3DAnimation25QAbstractAnimationPrivateC1ENS_18QAbstractAnimation13AnimationTypeE(
    Qt3DAnimation::QAbstractAnimation::AnimationType type) {
  return new Qt3DAnimation::QAbstractAnimationPrivate(type);
}

//  QAbstractAnimation *Qt3DAnimation::QAbstractAnimationPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractAnimation *ritual_ZN13Qt3DAnimation25QAbstractAnimationPrivate6q_funcEv(
    Qt3DAnimation::QAbstractAnimationPrivate *self) {
  return self->q_func();
}

//  const QAbstractAnimation
//      *Qt3DAnimation::QAbstractAnimationPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAbstractAnimation *ritual_ZNK13Qt3DAnimation25QAbstractAnimationPrivate6q_funcEv(
    const Qt3DAnimation::QAbstractAnimationPrivate *self) {
  return self->q_func();
}
