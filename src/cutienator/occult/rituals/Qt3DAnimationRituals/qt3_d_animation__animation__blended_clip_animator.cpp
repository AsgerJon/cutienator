//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/blendedclipanimator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/blendedclipanimator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::BlendedClipAnimator::mapperId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator8mapperIdEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->mapperId());
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::BlendedClipAnimator::clockId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator7clockIdEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return new Qt3DCore::QNodeId(self->clockId());
}

//  bool Qt3DAnimation::Animation::BlendedClipAnimator::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator9isRunningEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->isRunning();
}

//  float
//      Qt3DAnimation::Animation::BlendedClipAnimator::normalizedLocalTime()
//      const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator19normalizedLocalTimeEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->normalizedLocalTime();
}

//  bool Qt3DAnimation::Animation::BlendedClipAnimator::canRun() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator6canRunEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->canRun();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setStartTime(qint64
//      globalTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator12setStartTimeEx(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    qint64 globalTime) {
  self->setStartTime(globalTime);
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setLoops(int loops)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator8setLoopsEi(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    int loops) {
  self->setLoops(loops);
}

//  int Qt3DAnimation::Animation::BlendedClipAnimator::loops() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator5loopsEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->loops();
}

//  int Qt3DAnimation::Animation::BlendedClipAnimator::currentLoop() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator11currentLoopEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->currentLoop();
}

//  void Qt3DAnimation::Animation::BlendedClipAnimator::setCurrentLoop(int
//      currentLoop)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator14setCurrentLoopEi(
    Qt3DAnimation::Animation::BlendedClipAnimator *self,
    int currentLoop) {
  self->setCurrentLoop(currentLoop);
}

//  float
//      Qt3DAnimation::Animation::BlendedClipAnimator::lastNormalizedLocalTim
//      e()
extern "C" Q_DECL_EXPORT
float ritual_ZN13Qt3DAnimation9Animation19BlendedClipAnimator23lastNormalizedLocalTimeEv(
    Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->lastNormalizedLocalTime();
}

//  bool Qt3DAnimation::Animation::BlendedClipAnimator::isSeeking() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19BlendedClipAnimator9isSeekingEv(
    const Qt3DAnimation::Animation::BlendedClipAnimator *self) {
  return self->isSeeking();
}
