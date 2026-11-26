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
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/sqt_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/skeletondata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QVector>
#include <QtCore/QString>
#include <QtGui/QMatrix4x4>

//  Qt3DRender::Render::Skeleton::Skeleton()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Skeleton *ritual_ZN10Qt3DRender6Render8SkeletonC1Ev() {
  return new Qt3DRender::Render::Skeleton();
}

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

//  void Qt3DRender::Render::Skeleton::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton7cleanupEv(
    Qt3DRender::Render::Skeleton *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Skeleton::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Skeleton *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void
//      Qt3DRender::Render::Skeleton::setStatus(Qt3DCore::QSkeletonLoader::St
//      atus status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton9setStatusEN8Qt3DCore15QSkeletonLoader6StatusE(
    Qt3DRender::Render::Skeleton *self,
    Qt3DCore::QSkeletonLoader::Status status) {
  self->setStatus(status);
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

//  QVector<JointInfo> Qt3DRender::Render::Skeleton::joints() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DRender::Render::JointInfo> *ritual_ZNK10Qt3DRender6Render8Skeleton6jointsEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new QVector<Qt3DRender::Render::JointInfo>(self->joints());
}

//  QVector<QString> Qt3DRender::Render::Skeleton::jointNames() const
extern "C" Q_DECL_EXPORT
QVector<QString> *ritual_ZNK10Qt3DRender6Render8Skeleton10jointNamesEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new QVector<QString>(self->jointNames());
}

//  QVector<Qt3DCore::Sqt> Qt3DRender::Render::Skeleton::localPoses() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DCore::Sqt> *ritual_ZNK10Qt3DRender6Render8Skeleton10localPosesEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new QVector<Qt3DCore::Sqt>(self->localPoses());
}

//  Qt3DCore::QNodeId Qt3DRender::Render::Skeleton::rootJointId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render8Skeleton11rootJointIdEv(
    const Qt3DRender::Render::Skeleton *self) {
  return new Qt3DCore::QNodeId(self->rootJointId());
}

//  void Qt3DRender::Render::Skeleton::setLocalPose(HJoint jointHandle, const
//      Qt3DCore::Sqt &localPose)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton12setLocalPoseEN8Qt3DCore7QHandleINS0_5JointEEERKNS2_3SqtE(
    Qt3DRender::Render::Skeleton *self,
    const Qt3DRender::Render::HJoint *jointHandle,
    const Qt3DCore::Sqt *localPose) {
  self->setLocalPose(*jointHandle, *localPose);
}

//  QVector<QMatrix4x4>
//      Qt3DRender::Render::Skeleton::calculateSkinningMatrixPalette()
extern "C" Q_DECL_EXPORT
QVector<QMatrix4x4> *ritual_ZN10Qt3DRender6Render8Skeleton30calculateSkinningMatrixPaletteEv(
    Qt3DRender::Render::Skeleton *self) {
  return new QVector<QMatrix4x4>(self->calculateSkinningMatrixPalette());
}

//  void Qt3DRender::Render::Skeleton::clearData()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton9clearDataEv(
    Qt3DRender::Render::Skeleton *self) {
  self->clearData();
}

//  void Qt3DRender::Render::Skeleton::setSkeletonData(const SkeletonData
//      &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Skeleton15setSkeletonDataERKNS0_12SkeletonDataE(
    Qt3DRender::Render::Skeleton *self,
    const Qt3DRender::Render::SkeletonData *data) {
  self->setSkeletonData(*data);
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

//  a QVector<Qt3DRender::Render::JointInfo> a ritual of
//      Qt3DRender::Render::Skeleton gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Skeleton__QVector_Qt3DRender_Render_JointInfo(
    QVector<Qt3DRender::Render::JointInfo> *self) {
  delete self;
}

//  a QVector<QString> a ritual of Qt3DRender::Render::Skeleton gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Skeleton__QVector_QString(
    QVector<QString> *self) {
  delete self;
}

//  a QVector<Qt3DCore::Sqt> a ritual of Qt3DRender::Render::Skeleton gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Skeleton__QVector_Qt3DCore_Sqt(
    QVector<Qt3DCore::Sqt> *self) {
  delete self;
}

//  a QVector<QMatrix4x4> a ritual of Qt3DRender::Render::Skeleton gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Skeleton__QVector_QMatrix4x4(
    QVector<QMatrix4x4> *self) {
  delete self;
}
