//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgplane_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qtquick3dutilsglobal_p.h>
#include <QtQuick3DUtils/QtQuick3DUtils>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssgplane_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>

//  QSSGPlane::QSSGPlane()
extern "C" Q_DECL_EXPORT
QSSGPlane *ritual_ZN9QSSGPlaneC1Ev() {
  return new QSSGPlane();
}

//  QSSGPlane::QSSGPlane(float nx, float ny, float nz, float distance)
extern "C" Q_DECL_EXPORT
QSSGPlane *ritual_ZN9QSSGPlaneC1Effff(
    float nx,
    float ny,
    float nz,
    float distance) {
  return new QSSGPlane(nx, ny, nz, distance);
}

//  QSSGPlane::QSSGPlane(const QVector3D &normal, float distance)
extern "C" Q_DECL_EXPORT
QSSGPlane *ritual_ZN9QSSGPlaneC1ERK9QVector3Df(
    const QVector3D *normal,
    float distance) {
  return new QSSGPlane(*normal, distance);
}

//  QSSGPlane::QSSGPlane(const QVector3D &point, const QVector3D &normal)
extern "C" Q_DECL_EXPORT
QSSGPlane *ritual_ZN9QSSGPlaneC1ERK9QVector3DS2_(
    const QVector3D *point,
    const QVector3D *normal) {
  return new QSSGPlane(*point, *normal);
}

//  QSSGPlane::QSSGPlane(const QVector3D &p0, const QVector3D &p1, const
//      QVector3D &p2)
extern "C" Q_DECL_EXPORT
QSSGPlane *ritual_ZN9QSSGPlaneC1ERK9QVector3DS2_S2_(
    const QVector3D *p0,
    const QVector3D *p1,
    const QVector3D *p2) {
  return new QSSGPlane(*p0, *p1, *p2);
}

//  float QSSGPlane::distance(const QVector3D &p) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QSSGPlane8distanceERK9QVector3D(
    const QSSGPlane *self,
    const QVector3D *p) {
  return self->distance(*p);
}

//  bool QSSGPlane::contains(const QVector3D &p) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QSSGPlane8containsERK9QVector3D(
    const QSSGPlane *self,
    const QVector3D *p) {
  return self->contains(*p);
}

//  QVector3D QSSGPlane::project(const QVector3D &p) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QSSGPlane7projectERK9QVector3D(
    const QSSGPlane *self,
    const QVector3D *p) {
  return new QVector3D(self->project(*p));
}

//  QVector3D QSSGPlane::pointInPlane() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QSSGPlane12pointInPlaneEv(const QSSGPlane *self) {
  return new QVector3D(self->pointInPlane());
}

//  void QSSGPlane::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSSGPlane9normalizeEv(QSSGPlane *self) {
  self->normalize();
}

//  QSSGPlane::~QSSGPlane()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QSSGPlaneD1Ev(QSSGPlane *self) {
  delete self;
}
