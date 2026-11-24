//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipanimator_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/animationutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::clipId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator6clipIdEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->clipId());
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::mapperId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator8mapperIdEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->mapperId());
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipAnimator::clockId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator7clockIdEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->clockId());
}

//  bool Qt3DAnimation::Animation::ClipAnimator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator9isRunningEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->isRunning();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator8setLoopsEi(
    Qt3DAnimation::Animation::ClipAnimator *self,
    int loops) {
  self->setLoops(loops);
}

//  int Qt3DAnimation::Animation::ClipAnimator::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator5loopsEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->loops();
}

//  float Qt3DAnimation::Animation::ClipAnimator::normalizedLocalTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator19normalizedLocalTimeEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->normalizedLocalTime();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setHandler(Handler *handler)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator10setHandlerEPNS0_7HandlerE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    Qt3DAnimation::Animation::Handler *handler) {
  self->setHandler(handler);
}

//  bool Qt3DAnimation::Animation::ClipAnimator::canRun() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator6canRunEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->canRun();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setStartTime(qint64
//      globalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator12setStartTimeEx(
    Qt3DAnimation::Animation::ClipAnimator *self,
    qint64 globalTime) {
  self->setStartTime(globalTime);
}

//  int Qt3DAnimation::Animation::ClipAnimator::currentLoop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator11currentLoopEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->currentLoop();
}

//  void Qt3DAnimation::Animation::ClipAnimator::setCurrentLoop(int
//      currentLoop)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator14setCurrentLoopEi(
    Qt3DAnimation::Animation::ClipAnimator *self,
    int currentLoop) {
  self->setCurrentLoop(currentLoop);
}

//  void Qt3DAnimation::Animation::ClipAnimator::setClipFormat(const
//      ClipFormat &clipFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation12ClipAnimator13setClipFormatERKNS0_10ClipFormatE(
    Qt3DAnimation::Animation::ClipAnimator *self,
    const Qt3DAnimation::Animation::ClipFormat *clipFormat) {
  self->setClipFormat(*clipFormat);
}

//  ClipFormat Qt3DAnimation::Animation::ClipAnimator::clipFormat() const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipFormat *ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator10clipFormatEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return new Qt3DAnimation::Animation::ClipFormat(self->clipFormat());
}

//  float Qt3DAnimation::Animation::ClipAnimator::lastNormalizedLocalTime()
extern "C" Q_DECL_EXPORT
float ritual_ZN13Qt3DAnimation9Animation12ClipAnimator23lastNormalizedLocalTimeEv(
    Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->lastNormalizedLocalTime();
}

//  bool Qt3DAnimation::Animation::ClipAnimator::isSeeking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation12ClipAnimator9isSeekingEv(
    const Qt3DAnimation::Animation::ClipAnimator *self) {
  return self->isSeeking();
}
