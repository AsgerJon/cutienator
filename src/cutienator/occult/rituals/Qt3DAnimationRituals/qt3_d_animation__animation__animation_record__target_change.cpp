//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qvariant.h>

//  Qt3DAnimation::Animation::AnimationRecord::TargetChange::TargetChange(Qt3
//      DCore::QNodeId id, const char *name, QVariant v)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::AnimationRecord::TargetChange *ritual_ZN13Qt3DAnimation9Animation15AnimationRecord12TargetChangeC1EN8Qt3DCore7QNodeIdEPKc8QVariant(
    const Qt3DCore::QNodeId *id,
    const char *name,
    const QVariant *v) {
  return new Qt3DAnimation::Animation::AnimationRecord::TargetChange(
      *id,
      name,
      *v);
}

//  Qt3DAnimation::Animation::AnimationRecord::TargetChange::~TargetChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation15AnimationRecord12TargetChangeD1Ev(
    Qt3DAnimation::Animation::AnimationRecord::TargetChange *self) {
  delete self;
}
