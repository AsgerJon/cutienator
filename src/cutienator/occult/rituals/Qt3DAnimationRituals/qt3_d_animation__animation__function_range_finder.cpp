//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/functionrangefinder_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/functionrangefinder_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int Qt3DAnimation::Animation::FunctionRangeFinder::rangeSize() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder9rangeSizeEv(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  return self->rangeSize();
}

//  void Qt3DAnimation::Animation::FunctionRangeFinder::setRangeSize(int
//      rangeSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder12setRangeSizeEi(
    Qt3DAnimation::Animation::FunctionRangeFinder *self,
    int rangeSize) {
  self->setRangeSize(rangeSize);
}

//  bool Qt3DAnimation::Animation::FunctionRangeFinder::isAscending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder11isAscendingEv(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  return self->isAscending();
}

//  void Qt3DAnimation::Animation::FunctionRangeFinder::setAscending(bool
//      ascending)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder12setAscendingEb(
    Qt3DAnimation::Animation::FunctionRangeFinder *self,
    bool ascending) {
  self->setAscending(ascending);
}

//  int Qt3DAnimation::Animation::FunctionRangeFinder::correlationThreshold()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation19FunctionRangeFinder20correlationThresholdEv(
    const Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  return self->correlationThreshold();
}

//  void Qt3DAnimation::Animation::FunctionRangeFinder::updateAutomaticCorrel
//      ationThreshold()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinder35updateAutomaticCorrelationThresholdEv(
    Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  self->updateAutomaticCorrelationThreshold();
}

//  Qt3DAnimation::Animation::FunctionRangeFinder::~FunctionRangeFinder()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation19FunctionRangeFinderD1Ev(
    Qt3DAnimation::Animation::FunctionRangeFinder *self) {
  delete self;
}
