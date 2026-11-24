//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/qchannel.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/qchannel.h>

//  bool operator==(const QChannel &a0, const QChannel &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationeqERKNS_8QChannelES2_(
    const Qt3DAnimation::QChannel *a0,
    const Qt3DAnimation::QChannel *a1) {
  return operator==(*a0, *a1);
}

//  bool operator!=(const QChannel &a0, const QChannel &a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13Qt3DAnimationneERKNS_8QChannelES2_(
    const Qt3DAnimation::QChannel *a0,
    const Qt3DAnimation::QChannel *a1) {
  return operator!=(*a0, *a1);
}
