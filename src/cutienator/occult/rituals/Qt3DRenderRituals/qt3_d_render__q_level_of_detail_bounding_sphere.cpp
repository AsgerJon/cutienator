//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qlevelofdetailboundingsphere.h, Qt 6.12.0. Changes made here
//  are lost.
#include <Qt3DRender/qlevelofdetailboundingsphere.h>
#include <QtGui/qvectornd.h>

//  Qt3DRender::QLevelOfDetailBoundingSphere::QLevelOfDetailBoundingSphere(QV
//      ector3D center, float radius)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereC1E9QVector3Df(
    const QVector3D *center,
    float radius) {
  return new Qt3DRender::QLevelOfDetailBoundingSphere(*center, radius);
}

//  Qt3DRender::QLevelOfDetailBoundingSphere::QLevelOfDetailBoundingSphere(co
//      nst QLevelOfDetailBoundingSphere &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereC1ERKS0_(
    const Qt3DRender::QLevelOfDetailBoundingSphere *other) {
  return new Qt3DRender::QLevelOfDetailBoundingSphere(*other);
}

//  Qt3DRender::QLevelOfDetailBoundingSphere::~QLevelOfDetailBoundingSphere()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereD1Ev(
    Qt3DRender::QLevelOfDetailBoundingSphere *self) {
  delete self;
}

//  QLevelOfDetailBoundingSphere
//      &Qt3DRender::QLevelOfDetailBoundingSphere::operator=(const
//      QLevelOfDetailBoundingSphere &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailBoundingSphere *ritual_ZN10Qt3DRender28QLevelOfDetailBoundingSphereaSERKS0_(
    Qt3DRender::QLevelOfDetailBoundingSphere *self,
    const Qt3DRender::QLevelOfDetailBoundingSphere *other) {
  return &(self->operator=(*other));
}

//  QVector3D Qt3DRender::QLevelOfDetailBoundingSphere::center() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphere6centerEv(
    const Qt3DRender::QLevelOfDetailBoundingSphere *self) {
  return new QVector3D(self->center());
}

//  float Qt3DRender::QLevelOfDetailBoundingSphere::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphere6radiusEv(
    const Qt3DRender::QLevelOfDetailBoundingSphere *self) {
  return self->radius();
}

//  bool Qt3DRender::QLevelOfDetailBoundingSphere::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphere7isEmptyEv(
    const Qt3DRender::QLevelOfDetailBoundingSphere *self) {
  return self->isEmpty();
}

//  bool Qt3DRender::QLevelOfDetailBoundingSphere::operator==(const
//      QLevelOfDetailBoundingSphere &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphereeqERKS0_(
    const Qt3DRender::QLevelOfDetailBoundingSphere *self,
    const Qt3DRender::QLevelOfDetailBoundingSphere *other) {
  return self->operator==(*other);
}

//  bool Qt3DRender::QLevelOfDetailBoundingSphere::operator!=(const
//      QLevelOfDetailBoundingSphere &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender28QLevelOfDetailBoundingSphereneERKS0_(
    const Qt3DRender::QLevelOfDetailBoundingSphere *self,
    const Qt3DRender::QLevelOfDetailBoundingSphere *other) {
  return self->operator!=(*other);
}
