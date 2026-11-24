//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/joint_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/joint_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/sqt_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>

//  Qt3DCore::Sqt Qt3DRender::Render::Joint::localPose() const
extern "C" Q_DECL_EXPORT
Qt3DCore::Sqt *ritual_ZNK10Qt3DRender6Render5Joint9localPoseEv(
    const Qt3DRender::Render::Joint *self) {
  return new Qt3DCore::Sqt(self->localPose());
}

//  QMatrix4x4 Qt3DRender::Render::Joint::inverseBindMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10Qt3DRender6Render5Joint17inverseBindMatrixEv(
    const Qt3DRender::Render::Joint *self) {
  return new QMatrix4x4(self->inverseBindMatrix());
}

//  QString Qt3DRender::Render::Joint::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render5Joint4nameEv(
    const Qt3DRender::Render::Joint *self) {
  return new QString(self->name());
}

//  QVector3D Qt3DRender::Render::Joint::translation() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render5Joint11translationEv(
    const Qt3DRender::Render::Joint *self) {
  return new QVector3D(self->translation());
}

//  QQuaternion Qt3DRender::Render::Joint::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK10Qt3DRender6Render5Joint8rotationEv(
    const Qt3DRender::Render::Joint *self) {
  return new QQuaternion(self->rotation());
}

//  QVector3D Qt3DRender::Render::Joint::scale() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render5Joint5scaleEv(
    const Qt3DRender::Render::Joint *self) {
  return new QVector3D(self->scale());
}

//  void Qt3DRender::Render::Joint::setJointManager(JointManager
//      *jointManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Joint15setJointManagerEPNS0_12JointManagerE(
    Qt3DRender::Render::Joint *self,
    Qt3DRender::Render::JointManager *jointManager) {
  self->setJointManager(jointManager);
}

//  JointManager *Qt3DRender::Render::Joint::jointManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::JointManager *ritual_ZNK10Qt3DRender6Render5Joint12jointManagerEv(
    const Qt3DRender::Render::Joint *self) {
  return self->jointManager();
}

//  void Qt3DRender::Render::Joint::setSkeletonManager(SkeletonManager
//      *skeletonManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Joint18setSkeletonManagerEPNS0_15SkeletonManagerE(
    Qt3DRender::Render::Joint *self,
    Qt3DRender::Render::SkeletonManager *skeletonManager) {
  self->setSkeletonManager(skeletonManager);
}

//  SkeletonManager *Qt3DRender::Render::Joint::skeletonManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonManager *ritual_ZNK10Qt3DRender6Render5Joint15skeletonManagerEv(
    const Qt3DRender::Render::Joint *self) {
  return self->skeletonManager();
}

//  void Qt3DRender::Render::Joint::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render5Joint16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Joint *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Joint::syncFromFrontEnd(frontEnd, firstTime);
}
