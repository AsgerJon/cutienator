//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/bezierevaluator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/bezierevaluator_p.h>
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/keyframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DAnimation::Animation::BezierEvaluator::BezierEvaluator(float time0,
//      const Keyframe &keyframe0, float time1, const Keyframe &keyframe1)
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::BezierEvaluator *ritual_ZN13Qt3DAnimation9Animation15BezierEvaluatorC1EfRKNS0_8KeyframeEfS4_(
    float time0,
    const Qt3DAnimation::Animation::Keyframe *keyframe0,
    float time1,
    const Qt3DAnimation::Animation::Keyframe *keyframe1) {
  return new Qt3DAnimation::Animation::BezierEvaluator(
      time0,
      *keyframe0,
      time1,
      *keyframe1);
}

//  Qt3DAnimation::Animation::BezierEvaluator::~BezierEvaluator()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation15BezierEvaluatorD1Ev(
    Qt3DAnimation::Animation::BezierEvaluator *self) {
  delete self;
}
