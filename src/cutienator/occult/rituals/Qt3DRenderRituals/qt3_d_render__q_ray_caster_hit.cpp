//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qraycasterhit.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qraycasterhit.h>
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qstring.h>

//  Qt3DRender::QRayCasterHit::QRayCasterHit()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCasterHit *ritual_ZN10Qt3DRender13QRayCasterHitC1Ev() {
  return new Qt3DRender::QRayCasterHit();
}

//  Qt3DRender::QRayCasterHit::QRayCasterHit(QRayCasterHit::HitType type,
//      Qt3DCore::QNodeId id, float distance, const QVector3D
//      &localIntersect, const QVector3D &worldIntersect, uint
//      primitiveIndex, uint v1, uint v2, uint v3)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCasterHit *ritual_ZN10Qt3DRender13QRayCasterHitC1ENS0_7HitTypeEN8Qt3DCore7QNodeIdEfRK9QVector3DS6_jjjj(
    Qt3DRender::QRayCasterHit::HitType type,
    const Qt3DCore::QNodeId *id,
    float distance,
    const QVector3D *localIntersect,
    const QVector3D *worldIntersect,
    uint primitiveIndex,
    uint v1,
    uint v2,
    uint v3) {
  return new Qt3DRender::QRayCasterHit(
      type,
      *id,
      distance,
      *localIntersect,
      *worldIntersect,
      primitiveIndex,
      v1,
      v2,
      v3);
}

//  Qt3DRender::QRayCasterHit::QRayCasterHit(const QRayCasterHit &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCasterHit *ritual_ZN10Qt3DRender13QRayCasterHitC1ERKS0_(
    const Qt3DRender::QRayCasterHit *other) {
  return new Qt3DRender::QRayCasterHit(*other);
}

//  Qt3DRender::QRayCasterHit::~QRayCasterHit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QRayCasterHitD1Ev(
    Qt3DRender::QRayCasterHit *self) {
  delete self;
}

//  QRayCasterHit &Qt3DRender::QRayCasterHit::operator=(const QRayCasterHit
//      &other)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCasterHit *ritual_ZN10Qt3DRender13QRayCasterHitaSERKS0_(
    Qt3DRender::QRayCasterHit *self,
    const Qt3DRender::QRayCasterHit *other) {
  return &(self->operator=(*other));
}

//  HitType Qt3DRender::QRayCasterHit::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCasterHit::HitType ritual_ZNK10Qt3DRender13QRayCasterHit4typeEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->type();
}

//  Qt3DCore::QNodeId Qt3DRender::QRayCasterHit::entityId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender13QRayCasterHit8entityIdEv(
    const Qt3DRender::QRayCasterHit *self) {
  return new Qt3DCore::QNodeId(self->entityId());
}

//  Qt3DCore::QEntity *Qt3DRender::QRayCasterHit::entity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK10Qt3DRender13QRayCasterHit6entityEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->entity();
}

//  float Qt3DRender::QRayCasterHit::distance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender13QRayCasterHit8distanceEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->distance();
}

//  QVector3D Qt3DRender::QRayCasterHit::localIntersection() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender13QRayCasterHit17localIntersectionEv(
    const Qt3DRender::QRayCasterHit *self) {
  return new QVector3D(self->localIntersection());
}

//  QVector3D Qt3DRender::QRayCasterHit::worldIntersection() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender13QRayCasterHit17worldIntersectionEv(
    const Qt3DRender::QRayCasterHit *self) {
  return new QVector3D(self->worldIntersection());
}

//  uint Qt3DRender::QRayCasterHit::primitiveIndex() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender13QRayCasterHit14primitiveIndexEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->primitiveIndex();
}

//  uint Qt3DRender::QRayCasterHit::vertex1Index() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender13QRayCasterHit12vertex1IndexEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->vertex1Index();
}

//  uint Qt3DRender::QRayCasterHit::vertex2Index() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender13QRayCasterHit12vertex2IndexEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->vertex2Index();
}

//  uint Qt3DRender::QRayCasterHit::vertex3Index() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK10Qt3DRender13QRayCasterHit12vertex3IndexEv(
    const Qt3DRender::QRayCasterHit *self) {
  return self->vertex3Index();
}

//  QString Qt3DRender::QRayCasterHit::toString()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender13QRayCasterHit8toStringEv(
    Qt3DRender::QRayCasterHit *self) {
  return new QString(self->toString());
}

//  void Qt3DRender::QRayCasterHit::setEntity(Qt3DCore::QEntity *entity)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10Qt3DRender13QRayCasterHit9setEntityEPN8Qt3DCore7QEntityE(
    const Qt3DRender::QRayCasterHit *self,
    Qt3DCore::QEntity *entity) {
  self->setEntity(entity);
}
