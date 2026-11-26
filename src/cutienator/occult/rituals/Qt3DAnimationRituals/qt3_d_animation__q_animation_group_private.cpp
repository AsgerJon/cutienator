//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationgroup_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#if QT_CONFIG(animation)
#include <QtCore/qanimationgroup.h>
#endif
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationgroup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qanimationgroup.h>
#include "Qt3DAnimation/private/qanimationgroup_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qanimationgroup.cpp, line 67, as _ZN13Qt3DAnimation22QAnimationGroupPrivateC1Ev
namespace Qt3DAnimation {
inline QAnimationGroupPrivate::QAnimationGroupPrivate()
    : QObjectPrivate()
    , m_position(0.0f)
    , m_duration(0.0f)
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationgroup.cpp, line 75, as _ZN13Qt3DAnimation22QAnimationGroupPrivate14updatePositionEf
namespace Qt3DAnimation {
inline void QAnimationGroupPrivate::updatePosition(float position)
{
    m_position = position;
    for (QAbstractAnimation *aa : std::as_const(m_animations))
        aa->setPosition(position);
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QAnimationGroupPrivate::QAnimationGroupPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroupPrivate *ritual_ZN13Qt3DAnimation22QAnimationGroupPrivateC1Ev() {
  return new Qt3DAnimation::QAnimationGroupPrivate();
}

//  void Qt3DAnimation::QAnimationGroupPrivate::updatePosition(float
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation22QAnimationGroupPrivate14updatePositionEf(
    Qt3DAnimation::QAnimationGroupPrivate *self,
    float position) {
  self->updatePosition(position);
}

//  QAnimationGroup *Qt3DAnimation::QAnimationGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroup *ritual_ZN13Qt3DAnimation22QAnimationGroupPrivate6q_funcEv(
    Qt3DAnimation::QAnimationGroupPrivate *self) {
  return self->q_func();
}

//  const QAnimationGroup *Qt3DAnimation::QAnimationGroupPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationGroup *ritual_ZNK13Qt3DAnimation22QAnimationGroupPrivate6q_funcEv(
    const Qt3DAnimation::QAnimationGroupPrivate *self) {
  return self->q_func();
}
