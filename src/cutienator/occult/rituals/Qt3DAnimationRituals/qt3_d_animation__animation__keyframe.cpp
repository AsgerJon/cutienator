//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/keyframe_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/keyframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool Qt3DAnimation::Animation::Keyframe::operator==(const Keyframe &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation8KeyframeeqERKS1_(
    const Qt3DAnimation::Animation::Keyframe *self,
    const Qt3DAnimation::Animation::Keyframe *rhs) {
  return self->operator==(*rhs);
}

//  Qt3DAnimation::Animation::Keyframe::~Keyframe()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation8KeyframeD1Ev(
    Qt3DAnimation::Animation::Keyframe *self) {
  delete self;
}
