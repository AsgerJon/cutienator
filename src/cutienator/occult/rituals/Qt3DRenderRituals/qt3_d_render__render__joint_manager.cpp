//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>

//  void Qt3DRender::Render::JointManager::addDirtyJoint(Qt3DCore::QNodeId
//      jointId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12JointManager13addDirtyJointEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::JointManager *self,
    const Qt3DCore::QNodeId *jointId) {
  self->addDirtyJoint(*jointId);
}

//  void Qt3DRender::Render::JointManager::removeDirtyJoint(Qt3DCore::QNodeId
//      jointId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12JointManager16removeDirtyJointEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::JointManager *self,
    const Qt3DCore::QNodeId *jointId) {
  self->removeDirtyJoint(*jointId);
}

//  QList<HJoint> Qt3DRender::Render::JointManager::dirtyJoints()
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::Render::HJoint> *ritual_ZN10Qt3DRender6Render12JointManager11dirtyJointsEv(
    Qt3DRender::Render::JointManager *self) {
  return new QList<Qt3DRender::Render::HJoint>(self->dirtyJoints());
}

//  a QList<Qt3DRender::Render::HJoint> a ritual of
//      Qt3DRender::Render::JointManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_JointManager__QList_Qt3DRender_Render_HJoint(
    QList<Qt3DRender::Render::HJoint> *self) {
  delete self;
}
