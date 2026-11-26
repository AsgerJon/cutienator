//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h, Qt 6.12.0. Edited by
//  hand on 2026-11-25: Vector3D is QVector3D or an SSE class by system, and
//  Matrix4x4 the same, so each value taken is made as Vector3D(*x) or
//  Matrix4x4(*x), and each value given is built from its coordinates. Kept
//  as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>

//  Qt3DRender::RayCasting::QRay3D::QRay3D()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRay3D *ritual_ZN10Qt3DRender10RayCasting6QRay3DC1Ev() {
  return new Qt3DRender::RayCasting::QRay3D();
}

//  Qt3DRender::RayCasting::QRay3D::QRay3D(const Vector3D &origin, const
//      Vector3D &direction, float distance)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRay3D *ritual_ZN10Qt3DRender10RayCasting6QRay3DC1ERK9QVector3DS4_f(
    const QVector3D *origin,
    const QVector3D *direction,
    float distance) {
  return new Qt3DRender::RayCasting::QRay3D(Vector3D(*origin), Vector3D(*direction), distance);
}

//  Vector3D Qt3DRender::RayCasting::QRay3D::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10RayCasting6QRay3D6originEv(
    const Qt3DRender::RayCasting::QRay3D *self) {
  Vector3D v = self->origin();
  return new QVector3D(v.x(), v.y(), v.z());
}

//  void Qt3DRender::RayCasting::QRay3D::setOrigin(const Vector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting6QRay3D9setOriginERK9QVector3D(
    Qt3DRender::RayCasting::QRay3D *self,
    const QVector3D *value) {
  self->setOrigin(Vector3D(*value));
}

//  Vector3D Qt3DRender::RayCasting::QRay3D::direction() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10RayCasting6QRay3D9directionEv(
    const Qt3DRender::RayCasting::QRay3D *self) {
  Vector3D v = self->direction();
  return new QVector3D(v.x(), v.y(), v.z());
}

//  void Qt3DRender::RayCasting::QRay3D::setDirection(const Vector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting6QRay3D12setDirectionERK9QVector3D(
    Qt3DRender::RayCasting::QRay3D *self,
    const QVector3D *value) {
  self->setDirection(Vector3D(*value));
}

//  Vector3D Qt3DRender::RayCasting::QRay3D::point(float t) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10RayCasting6QRay3D5pointEf(
    const Qt3DRender::RayCasting::QRay3D *self,
    float t) {
  Vector3D v = self->point(t);
  return new QVector3D(v.x(), v.y(), v.z());
}

//  QRay3D &Qt3DRender::RayCasting::QRay3D::transform(const Matrix4x4
//      &matrix)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRay3D *ritual_ZN10Qt3DRender10RayCasting6QRay3D9transformERK10QMatrix4x4(
    Qt3DRender::RayCasting::QRay3D *self,
    const QMatrix4x4 *matrix) {
  return &(self->transform(Matrix4x4(*matrix)));
}

//  QRay3D Qt3DRender::RayCasting::QRay3D::transformed(const Matrix4x4
//      &matrix) const
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRay3D *ritual_ZNK10Qt3DRender10RayCasting6QRay3D11transformedERK10QMatrix4x4(
    const Qt3DRender::RayCasting::QRay3D *self,
    const QMatrix4x4 *matrix) {
  return new Qt3DRender::RayCasting::QRay3D(self->transformed(Matrix4x4(*matrix)));
}

//  bool Qt3DRender::RayCasting::QRay3D::operator==(const QRay3D &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10RayCasting6QRay3DeqERKS1_(
    const Qt3DRender::RayCasting::QRay3D *self,
    const Qt3DRender::RayCasting::QRay3D *other) {
  return self->operator==(*other);
}

//  bool Qt3DRender::RayCasting::QRay3D::operator!=(const QRay3D &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10RayCasting6QRay3DneERKS1_(
    const Qt3DRender::RayCasting::QRay3D *self,
    const Qt3DRender::RayCasting::QRay3D *other) {
  return self->operator!=(*other);
}

//  bool Qt3DRender::RayCasting::QRay3D::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10RayCasting6QRay3D7isValidEv(
    const Qt3DRender::RayCasting::QRay3D *self) {
  return self->isValid();
}
