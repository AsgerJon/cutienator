//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/skeleton_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/skeleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/QVector>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/private/backendnode_p.h>
#include <Qt3DCore/qnode.h>
#include <Qt3DCore/private/qbackendnode_p.h>
#include <Qt3DAnimation/private/skeleton_p.h>
#include <Qt3DCore/private/qabstractskeleton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 13, as _ZN13Qt3DAnimation9Animation11BackendNodeC2EN8Qt3DCore12QBackendNode4ModeE
namespace Qt3DAnimation::Animation {
inline BackendNode::BackendNode(Mode mode)
    : Qt3DCore::QBackendNode(mode)
    , m_handler(nullptr)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/skeleton.cpp, line 33, as _ZN13Qt3DAnimation9Animation8Skeleton16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
using namespace Qt3DCore;
inline void Skeleton::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    BackendNode::syncFromFrontEnd(frontEnd, firstTime);

    const Qt3DCore::QAbstractSkeleton *node = qobject_cast<const Qt3DCore::QAbstractSkeleton *>(frontEnd);
    if (!node)
        return;

    auto dnode = Qt3DCore::QAbstractSkeletonPrivate::get(node);

    // TODO: Mark joint info as dirty so we can rebuild any indexes used
    // by the animators and channel mappings.
    m_jointNames = dnode->m_jointNames;
    m_jointLocalPoses = dnode->m_localPoses;
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 34, as _ZN13Qt3DAnimation9Animation11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb
namespace Qt3DAnimation::Animation {
inline void BackendNode::syncFromFrontEnd(const Qt3DCore::QNode *frontEnd, bool firstTime)
{
    Q_UNUSED(firstTime);

    d_ptr->setEnabled(frontEnd->isEnabled());
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/backendnode.cpp, line 19, as _ZN13Qt3DAnimation9Animation11BackendNodeD2Ev
namespace Qt3DAnimation::Animation {
inline BackendNode::~BackendNode()
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/skeleton.cpp, line 22, as _ZN13Qt3DAnimation9Animation8SkeletonC1Ev
namespace Qt3DAnimation::Animation {
using namespace Qt3DCore;
inline Skeleton::Skeleton()
    : BackendNode(Qt3DCore::QBackendNode::ReadWrite)
{
}
}  // namespace Qt3DAnimation::Animation

//  from ../qt3d/src/animation/backend/skeleton.cpp, line 27, as _ZN13Qt3DAnimation9Animation8Skeleton7cleanupEv
namespace Qt3DAnimation::Animation {
using namespace Qt3DCore;
inline void Skeleton::cleanup()
{
    m_jointNames.clear();
    m_jointLocalPoses.clear();
}
}  // namespace Qt3DAnimation::Animation
//  -----------------------------------------------------------------------

//  Qt3DAnimation::Animation::Skeleton::Skeleton()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::Skeleton *ritual_ZN13Qt3DAnimation9Animation8SkeletonC1Ev() {
  return new Qt3DAnimation::Animation::Skeleton();
}

//  void Qt3DAnimation::Animation::Skeleton::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation8Skeleton7cleanupEv(
    Qt3DAnimation::Animation::Skeleton *self) {
  self->cleanup();
}

//  void Qt3DAnimation::Animation::Skeleton::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation8Skeleton16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::Skeleton *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QVector<Qt3DCore::Sqt> Qt3DAnimation::Animation::Skeleton::joints() const
extern "C" Q_DECL_EXPORT
QVector<Qt3DCore::Sqt> *ritual_ZNK13Qt3DAnimation9Animation8Skeleton6jointsEv(
    const Qt3DAnimation::Animation::Skeleton *self) {
  return new QVector<Qt3DCore::Sqt>(self->joints());
}

//  int Qt3DAnimation::Animation::Skeleton::jointCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13Qt3DAnimation9Animation8Skeleton10jointCountEv(
    const Qt3DAnimation::Animation::Skeleton *self) {
  return self->jointCount();
}

//  QString Qt3DAnimation::Animation::Skeleton::jointName(int jointIndex)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13Qt3DAnimation9Animation8Skeleton9jointNameEi(
    const Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex) {
  return new QString(self->jointName(jointIndex));
}

//  void Qt3DAnimation::Animation::Skeleton::setJointScale(int jointIndex,
//      const QVector3D &scale)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation8Skeleton13setJointScaleEiRK9QVector3D(
    Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex,
    const QVector3D *scale) {
  self->setJointScale(jointIndex, *scale);
}

//  QVector3D Qt3DAnimation::Animation::Skeleton::jointScale(int jointIndex)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13Qt3DAnimation9Animation8Skeleton10jointScaleEi(
    const Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex) {
  return new QVector3D(self->jointScale(jointIndex));
}

//  void Qt3DAnimation::Animation::Skeleton::setJointRotation(int jointIndex,
//      const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation8Skeleton16setJointRotationEiRK11QQuaternion(
    Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex,
    const QQuaternion *rotation) {
  self->setJointRotation(jointIndex, *rotation);
}

//  QQuaternion Qt3DAnimation::Animation::Skeleton::jointRotation(int
//      jointIndex) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK13Qt3DAnimation9Animation8Skeleton13jointRotationEi(
    const Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex) {
  return new QQuaternion(self->jointRotation(jointIndex));
}

//  void Qt3DAnimation::Animation::Skeleton::setJointTranslation(int
//      jointIndex, const QVector3D &translation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation8Skeleton19setJointTranslationEiRK9QVector3D(
    Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex,
    const QVector3D *translation) {
  self->setJointTranslation(jointIndex, *translation);
}

//  QVector3D Qt3DAnimation::Animation::Skeleton::jointTranslation(int
//      jointIndex) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK13Qt3DAnimation9Animation8Skeleton16jointTranslationEi(
    const Qt3DAnimation::Animation::Skeleton *self,
    int jointIndex) {
  return new QVector3D(self->jointTranslation(jointIndex));
}

//  void Qt3DAnimation::Animation::Skeleton::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13Qt3DAnimation9Animation8Skeleton16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DAnimation::Animation::Skeleton *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DAnimation::Animation::Skeleton::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QVector<Qt3DCore::Sqt> a ritual of Qt3DAnimation::Animation::Skeleton
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DAnimation_Animation_Skeleton__QVector_Qt3DCore_Sqt(
    QVector<Qt3DCore::Sqt> *self) {
  delete self;
}
