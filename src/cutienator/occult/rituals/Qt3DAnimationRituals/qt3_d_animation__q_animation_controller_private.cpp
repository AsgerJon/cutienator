//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationcontroller_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qanimationcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/qanimationcontroller.h>
#include <Qt3DAnimation/qanimationgroup.h>
#include <Qt3DAnimation/private/qanimationcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/frontend/qanimationcontroller.cpp, line 124, as _ZN13Qt3DAnimation27QAnimationControllerPrivateC1Ev
namespace Qt3DAnimation {
inline QAnimationControllerPrivate::QAnimationControllerPrivate()
    : QObjectPrivate()
    , m_activeAnimationGroup(0)
    , m_position(0.0f)
    , m_scaledPosition(0.0f)
    , m_positionScale(1.0f)
    , m_positionOffset(0.0f)
    , m_entity(nullptr)
    , m_recursive(true)
{

}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcontroller.cpp, line 137, as _ZN13Qt3DAnimation27QAnimationControllerPrivate14updatePositionEf
namespace Qt3DAnimation {
inline void QAnimationControllerPrivate::updatePosition(float position)
{
    m_position = position;
    m_scaledPosition = scaledPosition(position);
    if (m_activeAnimationGroup >= 0 && m_activeAnimationGroup < m_animationGroups.size())
        m_animationGroups[m_activeAnimationGroup]->setPosition(m_scaledPosition);
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcontroller.cpp, line 159, as _ZN13Qt3DAnimation27QAnimationControllerPrivate17extractAnimationsEv
namespace Qt3DAnimation {
inline void QAnimationControllerPrivate::extractAnimations()
{
    Q_Q(QAnimationController);
    if (!m_entity)
        return;
    QList<Qt3DAnimation::QAbstractAnimation *> animations
            = m_entity->findChildren<Qt3DAnimation::QAbstractAnimation *>(QString(),
                m_recursive ? Qt::FindChildrenRecursively : Qt::FindDirectChildrenOnly);
    if (animations.size() > 0) {
        for (Qt3DAnimation::QAbstractAnimation *a : animations) {
            QAnimationGroup *group = findGroup(a->animationName());
            if (!group) {
                group = new QAnimationGroup(q);
                group->setName(a->animationName());
                m_animationGroups.push_back(group);
            }
            group->addAnimation(a);
        }
    }
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcontroller.cpp, line 179, as _ZN13Qt3DAnimation27QAnimationControllerPrivate15clearAnimationsEv
namespace Qt3DAnimation {
inline void QAnimationControllerPrivate::clearAnimations()
{
    for (Qt3DAnimation::QAnimationGroup *a : std::as_const(m_animationGroups))
        a->deleteLater();
    m_animationGroups.clear();
    m_activeAnimationGroup = 0;
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcontroller.cpp, line 150, as _ZN13Qt3DAnimation27QAnimationControllerPrivate9findGroupERK7QString
namespace Qt3DAnimation {
inline QAnimationGroup *QAnimationControllerPrivate::findGroup(const QString &name)
{
    for (QAnimationGroup *g : std::as_const(m_animationGroups)) {
        if (g->name() == name)
            return g;
    }
    return nullptr;
}
}  // namespace Qt3DAnimation

//  from ../qt3d/src/animation/frontend/qanimationcontroller.cpp, line 145, as _ZNK13Qt3DAnimation27QAnimationControllerPrivate14scaledPositionEf
namespace Qt3DAnimation {
inline float QAnimationControllerPrivate::scaledPosition(float position) const
{
    return m_positionScale * position + m_positionOffset;
}
}  // namespace Qt3DAnimation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::QAnimationControllerPrivate::QAnimationControllerPrivate()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationControllerPrivate *ritual_ZN13Qt3DAnimation27QAnimationControllerPrivateC1Ev() {
  return new Qt3DAnimation::QAnimationControllerPrivate();
}

//  void Qt3DAnimation::QAnimationControllerPrivate::updatePosition(float
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate14updatePositionEf(
    Qt3DAnimation::QAnimationControllerPrivate *self,
    float position) {
  self->updatePosition(position);
}

//  void Qt3DAnimation::QAnimationControllerPrivate::extractAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate17extractAnimationsEv(
    Qt3DAnimation::QAnimationControllerPrivate *self) {
  self->extractAnimations();
}

//  void Qt3DAnimation::QAnimationControllerPrivate::clearAnimations()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate15clearAnimationsEv(
    Qt3DAnimation::QAnimationControllerPrivate *self) {
  self->clearAnimations();
}

//  QAnimationGroup
//      *Qt3DAnimation::QAnimationControllerPrivate::findGroup(const QString
//      &name)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationGroup *ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate9findGroupERK7QString(
    Qt3DAnimation::QAnimationControllerPrivate *self,
    const QString *name) {
  return self->findGroup(*name);
}

//  float Qt3DAnimation::QAnimationControllerPrivate::scaledPosition(float
//      position) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation27QAnimationControllerPrivate14scaledPositionEf(
    const Qt3DAnimation::QAnimationControllerPrivate *self,
    float position) {
  return self->scaledPosition(position);
}

//  QAnimationController
//      *Qt3DAnimation::QAnimationControllerPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAnimationController *ritual_ZN13Qt3DAnimation27QAnimationControllerPrivate6q_funcEv(
    Qt3DAnimation::QAnimationControllerPrivate *self) {
  return self->q_func();
}

//  const QAnimationController
//      *Qt3DAnimation::QAnimationControllerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAnimationController *ritual_ZNK13Qt3DAnimation27QAnimationControllerPrivate6q_funcEv(
    const Qt3DAnimation::QAnimationControllerPrivate *self) {
  return self->q_func();
}
