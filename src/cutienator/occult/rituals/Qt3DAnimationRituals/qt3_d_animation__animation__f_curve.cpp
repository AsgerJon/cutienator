//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/fcurve_p.h>
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/keyframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int Qt3DAnimation::Animation::FCurve::keyframeCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation6FCurve13keyframeCountEv(
    const Qt3DAnimation::Animation::FCurve *self) {
  return self->keyframeCount();
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

//  Qt3DAnimation::Animation::FCurve::~FCurve()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation6FCurveD1Ev(
    Qt3DAnimation::Animation::FCurve *self) {
  delete self;
}
