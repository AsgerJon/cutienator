//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clock_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clock_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DAnimation::Animation::Clock::setPlaybackRate(double
//      playbackRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation5Clock15setPlaybackRateEd(
    Qt3DAnimation::Animation::Clock *self,
    double playbackRate) {
  self->setPlaybackRate(playbackRate);
}

//  double Qt3DAnimation::Animation::Clock::playbackRate() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation5Clock12playbackRateEv(
    const Qt3DAnimation::Animation::Clock *self) {
  return self->playbackRate();
}
