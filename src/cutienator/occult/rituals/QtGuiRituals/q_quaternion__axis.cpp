//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qquaternion.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_QUATERNION)
#include <QtGui/qquaternion.h>
#include <QtGui/qvectornd.h>

#if !defined(QT_NO_VECTOR3D)
//  Axis QQuaternion::Axis::fromVector3D(QVector3D v)
extern "C" Q_DECL_EXPORT
QQuaternion::Axis *ritual_ZN11QQuaternion4Axis12fromVector3DE9QVector3D(
    const QVector3D *v) {
  return new QQuaternion::Axis(QQuaternion::Axis::fromVector3D(*v));
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  QVector3D QQuaternion::Axis::toVector3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QQuaternion4Axis10toVector3DEv(
    const QQuaternion::Axis *self) {
  return new QVector3D(self->toVector3D());
}
#endif  // !defined(QT_NO_VECTOR3D)

//  QQuaternion::Axis::~Axis()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion4AxisD1Ev(QQuaternion::Axis *self) {
  delete self;
}

#endif  // !defined(QT_NO_QUATERNION)
