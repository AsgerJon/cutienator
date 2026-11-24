//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/buildblendtreesjob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/buildblendtreesjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DAnimation::Animation::BuildBlendTreesJob::setHandler(Handler
//      *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation18BuildBlendTreesJob10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::BuildBlendTreesJob *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  Handler *Qt3DAnimation::Animation::BuildBlendTreesJob::handler() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Handler *ritual_ZNK13Qt3DAnimation9Animation18BuildBlendTreesJob7handlerEv(
    const Qt3DAnimation::Animation::BuildBlendTreesJob *self) {
  return self->handler();
}
