//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/sphere_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: Vector3D is QVector3D or an SSE class by system, and
//  Matrix4x4 the same, so each value taken is made as Vector3D(*x) or
//  Matrix4x4(*x), and each value given is built from its coordinates.
//  Removed expandToContain, which takes a QList. Kept as it is when the
//  generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/sphere_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>

//  Qt3DRender::Render::Sphere::Sphere(Qt3DCore::QNodeId i)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Sphere *ritual_ZN10Qt3DRender6Render6SphereC1EN8Qt3DCore7QNodeIdE(
    const Qt3DCore::QNodeId *i) {
  return new Qt3DRender::Render::Sphere(*i);
}

//  Qt3DRender::Render::Sphere::Sphere(const Vector3D &c, float r,
//      Qt3DCore::QNodeId i)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Sphere *ritual_ZN10Qt3DRender6Render6SphereC1ERK9QVector3DfN8Qt3DCore7QNodeIdE(
    const QVector3D *c,
    float r,
    const Qt3DCore::QNodeId *i) {
  return new Qt3DRender::Render::Sphere(Vector3D(*c), r, *i);
}

//  void Qt3DRender::Render::Sphere::setCenter(const Vector3D &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Sphere9setCenterERK9QVector3D(
    Qt3DRender::Render::Sphere *self,
    const QVector3D *c) {
  self->setCenter(Vector3D(*c));
}

//  Vector3D Qt3DRender::Render::Sphere::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender6Render6Sphere6centerEv(
    const Qt3DRender::Render::Sphere *self) {
  Vector3D v = self->center();
  return new QVector3D(v.x(), v.y(), v.z());
}

//  bool Qt3DRender::Render::Sphere::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render6Sphere6isNullEv(
    const Qt3DRender::Render::Sphere *self) {
  return self->isNull();
}

//  void Qt3DRender::Render::Sphere::setRadius(float r)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Sphere9setRadiusEf(
    Qt3DRender::Render::Sphere *self,
    float r) {
  self->setRadius(r);
}

//  float Qt3DRender::Render::Sphere::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render6Sphere6radiusEv(
    const Qt3DRender::Render::Sphere *self) {
  return self->radius();
}

//  void Qt3DRender::Render::Sphere::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6Sphere5clearEv(
    Qt3DRender::Render::Sphere *self) {
  self->clear();
}

//  Sphere &Qt3DRender::Render::Sphere::transform(const Matrix4x4 &mat)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Sphere *ritual_ZN10Qt3DRender6Render6Sphere9transformERK10QMatrix4x4(
    Qt3DRender::Render::Sphere *self,
    const QMatrix4x4 *mat) {
  return &(self->transform(Matrix4x4(*mat)));
}

//  Qt3DRender::Render::Sphere::~Sphere()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render6SphereD1Ev(
    Qt3DRender::Render::Sphere *self) {
  delete self;
}

//  Vector3D Qt3DRender::Render::Sphere::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_own_ZNK10Qt3DRender6Render6Sphere6centerEv(
    const Qt3DRender::Render::Sphere *self) {
  Vector3D v = self->Qt3DRender::Render::Sphere::center();
  return new QVector3D(v.x(), v.y(), v.z());
}

//  float Qt3DRender::Render::Sphere::radius() const
extern "C" Q_DECL_EXPORT
float ritual_own_ZNK10Qt3DRender6Render6Sphere6radiusEv(
    const Qt3DRender::Render::Sphere *self) {
  return self->Qt3DRender::Render::Sphere::radius();
}
