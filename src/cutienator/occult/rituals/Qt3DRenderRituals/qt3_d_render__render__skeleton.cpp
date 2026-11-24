//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/skeleton_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <Qt3DCore/qnodeid.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DRender::Render::Skeleton::setSkeletonManager(SkeletonManager
//      *skeletonManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton18setSkeletonManagerEPNS0_15SkeletonManagerE(
    Qt3DRender::Render::Skeleton *self,
    Qt3DRender::Render::SkeletonManager *skeletonManager) {
  self->setSkeletonManager(skeletonManager);
}

//  SkeletonManager *Qt3DRender::Render::Skeleton::skeletonManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonManager *ritual_ZNK10Qt3DRender6Render8Skeleton15skeletonManagerEv(
    const Qt3DRender::Render::Skeleton *self) {
  return self->skeletonManager();
}

//  void Qt3DRender::Render::Skeleton::setJointManager(JointManager
//      *jointManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton15setJointManagerEPNS0_12JointManagerE(
    Qt3DRender::Render::Skeleton *self,
    Qt3DRender::Render::JointManager *jointManager) {
  self->setJointManager(jointManager);
}

//  JointManager *Qt3DRender::Render::Skeleton::jointManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::JointManager *ritual_ZNK10Qt3DRender6Render8Skeleton12jointManagerEv(
    const Qt3DRender::Render::Skeleton *self) {
  return self->jointManager();
}

//  Qt3DCore::QSkeletonLoader::Status Qt3DRender::Render::Skeleton::status()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QSkeletonLoader::Status ritual_ZNK10Qt3DRender6Render8Skeleton6statusEv(
    const Qt3DRender::Render::Skeleton *self) {
  return self->status();
}

//  QUrl Qt3DRender::Render::Skeleton::source() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10Qt3DRender6Render8Skeleton6sourceEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new QUrl(self->source());
}

//  SkeletonDataType Qt3DRender::Render::Skeleton::dataType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Skeleton::SkeletonDataType ritual_ZNK10Qt3DRender6Render8Skeleton8dataTypeEv(
    const Qt3DRender::Render::Skeleton *self) {
  return self->dataType();
}

//  bool Qt3DRender::Render::Skeleton::createJoints() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render8Skeleton12createJointsEv(
    const Qt3DRender::Render::Skeleton *self) {
  return self->createJoints();
}

//  void Qt3DRender::Render::Skeleton::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton7setNameERK7QString(
    Qt3DRender::Render::Skeleton *self,
    const QString *name) {
  self->setName(*name);
}

//  QString Qt3DRender::Render::Skeleton::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render8Skeleton4nameEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new QString(self->name());
}

//  qsizetype Qt3DRender::Render::Skeleton::jointCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK10Qt3DRender6Render8Skeleton10jointCountEv(
    const Qt3DRender::Render::Skeleton *self) {
  return self->jointCount();
}

//  Qt3DCore::QNodeId Qt3DRender::Render::Skeleton::rootJointId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render8Skeleton11rootJointIdEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new Qt3DCore::QNodeId(self->rootJointId());
}

//  const SkeletonData &Qt3DRender::Render::Skeleton::skeletonData() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonData *ritual_ZNK10Qt3DRender6Render8Skeleton12skeletonDataEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new Qt3DRender::Render::SkeletonData(self->skeletonData());
}

//  SkeletonData Qt3DRender::Render::Skeleton::skeletonData()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SkeletonData *ritual_ZN10Qt3DRender6Render8Skeleton12skeletonDataEv(
    Qt3DRender::Render::Skeleton *self) {
  return new Qt3DRender::Render::SkeletonData(self->skeletonData());
}

//  void Qt3DRender::Render::Skeleton::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render8Skeleton16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Skeleton *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Skeleton::syncFromFrontEnd(frontEnd, firstTime);
}
