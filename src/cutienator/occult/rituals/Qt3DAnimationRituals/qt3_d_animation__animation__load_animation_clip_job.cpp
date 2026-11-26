//  Written by hand on 2026-11-25 from
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/loadanimationclipjob_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Qt's library offers nothing of this class by name: only its inline
//  functions and its virtual run are called, through the object.
//  Not written: the constructor, addDirtyAnimationClips (takes a QList)
//  and clearDirtyAnimationClips.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/loadanimationclipjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DAnimation::Animation::LoadAnimationClipJob::setHandler(Handler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation20LoadAnimationClipJob10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::LoadAnimationClipJob *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  Handler *Qt3DAnimation::Animation::LoadAnimationClipJob::handler() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Handler *ritual_ZNK13Qt3DAnimation9Animation20LoadAnimationClipJob7handlerEv(
    const Qt3DAnimation::Animation::LoadAnimationClipJob *self) {
  return self->handler();
}

//  void Qt3DAnimation::Animation::LoadAnimationClipJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation20LoadAnimationClipJob3runEv(
    Qt3DAnimation::Animation::LoadAnimationClipJob *self) {
  self->run();
}
