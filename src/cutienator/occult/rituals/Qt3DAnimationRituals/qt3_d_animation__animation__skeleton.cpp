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
