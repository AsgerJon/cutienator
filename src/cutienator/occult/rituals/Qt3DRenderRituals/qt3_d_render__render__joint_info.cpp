//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::JointInfo::JointInfo()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::JointInfo *ritual_ZN10Qt3DRender6Render9JointInfoC1Ev() {
  return new Qt3DRender::Render::JointInfo();
}

//  Qt3DRender::Render::JointInfo::JointInfo(Joint *joint, int
//      parentJointIndex)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::JointInfo *ritual_ZN10Qt3DRender6Render9JointInfoC1EPNS0_5JointEi(
    Qt3DRender::Render::Joint *joint,
    int parentJointIndex) {
  return new Qt3DRender::Render::JointInfo(joint, parentJointIndex);
}

//  Qt3DRender::Render::JointInfo::~JointInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9JointInfoD1Ev(
    Qt3DRender::Render::JointInfo *self) {
  delete self;
}
