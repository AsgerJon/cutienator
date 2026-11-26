//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: Vector3D is QVector3D or an SSE
//  class by system, and Matrix4x4 the same, so each value taken is made as
//  Vector3D(*x) or Matrix4x4(*x), and each value given is built from its
//  coordinates. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtGui/qvectornd.h>

//  Qt3DRender::RayCasting::QCollisionQueryResult::Hit::Hit()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult::Hit *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult3HitC1Ev() {
  return new Qt3DRender::RayCasting::QCollisionQueryResult::Hit();
}

//  Qt3DRender::RayCasting::QCollisionQueryResult::Hit::Hit(Qt3DCore::QNodeId
//      entity, const Vector3D &intersection, float distance, const Vector3D
//      &uvw)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult::Hit *ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult3HitC1EN8Qt3DCore7QNodeIdERK9QVector3DfS7_(
    const Qt3DCore::QNodeId *entity,
    const QVector3D *intersection,
    float distance,
    const QVector3D *uvw) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult::Hit(
      *entity,
      Vector3D(*intersection),
      distance,
      Vector3D(*uvw));
}

//  Qt3DRender::RayCasting::QCollisionQueryResult::Hit::~Hit()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting21QCollisionQueryResult3HitD1Ev(
    Qt3DRender::RayCasting::QCollisionQueryResult::Hit *self) {
  delete self;
}
