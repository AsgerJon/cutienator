//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qabstractcollisionqueryservice_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qabstractcollisionqueryservice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QMetaObject
//      *Qt3DRender::RayCasting::QAbstractCollisionQueryService::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10RayCasting30QAbstractCollisionQueryService10metaObjectEv(
    const Qt3DRender::RayCasting::QAbstractCollisionQueryService *self) {
  return self->metaObject();
}

//  void *Qt3DRender::RayCasting::QAbstractCollisionQueryService::qt_metacast
//      (const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService11qt_metacastEPKc(
    Qt3DRender::RayCasting::QAbstractCollisionQueryService *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString Qt3DRender::RayCasting::QAbstractCollisionQueryService::tr(const
//      char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(
      Qt3DRender::RayCasting::QAbstractCollisionQueryService::tr(
          s,
          c,
          n));
}

//  QQueryHandle
//      Qt3DRender::RayCasting::QAbstractCollisionQueryService::query(const
//      QRay3D &ray, QueryMode mode, QBoundingVolumeProvider *provider)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QQueryHandle ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService5queryERKNS0_6QRay3DENS1_9QueryModeEPNS0_23QBoundingVolumeProviderE(
    Qt3DRender::RayCasting::QAbstractCollisionQueryService *self,
    const Qt3DRender::RayCasting::QRay3D *ray,
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::QueryMode mode,
    Qt3DRender::RayCasting::QBoundingVolumeProvider *provider) {
  return self->query(*ray, mode, provider);
}

//  QCollisionQueryResult::Hit
//      Qt3DRender::RayCasting::QAbstractCollisionQueryService::query(const
//      QRay3D &ray, const QBoundingVolume *volume)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult::Hit *ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService5queryERKNS0_6QRay3DEPKNS0_15QBoundingVolumeE(
    Qt3DRender::RayCasting::QAbstractCollisionQueryService *self,
    const Qt3DRender::RayCasting::QRay3D *ray,
    const Qt3DRender::RayCasting::QBoundingVolume *volume) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult::Hit(
      self->query(
          *ray,
          volume));
}

//  QCollisionQueryResult
//      Qt3DRender::RayCasting::QAbstractCollisionQueryService::fetchResult(c
//      onst QQueryHandle &handle)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService11fetchResultERKi(
    Qt3DRender::RayCasting::QAbstractCollisionQueryService *self,
    Qt3DRender::RayCasting::QQueryHandle handle) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult(
      self->fetchResult(
          handle));
}

//  QAbstractCollisionQueryServicePrivate
//      *Qt3DRender::RayCasting::QAbstractCollisionQueryService::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QAbstractCollisionQueryServicePrivate *ritual_ZN10Qt3DRender10RayCasting30QAbstractCollisionQueryService6d_funcEv(
    Qt3DRender::RayCasting::QAbstractCollisionQueryService *self) {
  return self->d_func();
}

//  const QAbstractCollisionQueryServicePrivate
//      *Qt3DRender::RayCasting::QAbstractCollisionQueryService::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::RayCasting::QAbstractCollisionQueryServicePrivate *ritual_ZNK10Qt3DRender10RayCasting30QAbstractCollisionQueryService6d_funcEv(
    const Qt3DRender::RayCasting::QAbstractCollisionQueryService *self) {
  return self->d_func();
}
