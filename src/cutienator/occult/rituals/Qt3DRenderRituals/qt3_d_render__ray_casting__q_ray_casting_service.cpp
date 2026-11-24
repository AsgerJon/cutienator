//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qraycastingservice_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qraycastingservice_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qray3d_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/qcollisionqueryresult_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRayCastingServicePrivate
//      *Qt3DRender::RayCasting::QRayCastingService::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QRayCastingServicePrivate *ritual_ZN10Qt3DRender10RayCasting18QRayCastingService6d_funcEv(
    Qt3DRender::RayCasting::QRayCastingService *self) {
  return self->d_func();
}

//  const QRayCastingServicePrivate
//      *Qt3DRender::RayCasting::QRayCastingService::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::RayCasting::QRayCastingServicePrivate *ritual_ZNK10Qt3DRender10RayCasting18QRayCastingService6d_funcEv(
    const Qt3DRender::RayCasting::QRayCastingService *self) {
  return self->d_func();
}

//  QQueryHandle Qt3DRender::RayCasting::QRayCastingService::query(const
//      QRay3D &ray, QueryMode mode, QBoundingVolumeProvider *provider)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QQueryHandle ritual_own_ZN10Qt3DRender10RayCasting18QRayCastingService5queryERKNS0_6QRay3DENS0_30QAbstractCollisionQueryService9QueryModeEPNS0_23QBoundingVolumeProviderE(
    Qt3DRender::RayCasting::QRayCastingService *self,
    const Qt3DRender::RayCasting::QRay3D *ray,
    Qt3DRender::RayCasting::QAbstractCollisionQueryService::QueryMode mode,
    Qt3DRender::RayCasting::QBoundingVolumeProvider *provider) {
  return self->Qt3DRender::RayCasting::QRayCastingService::query(
      *ray,
      mode,
      provider);
}

//  QCollisionQueryResult::Hit
//      Qt3DRender::RayCasting::QRayCastingService::query(const QRay3D &ray,
//      const QBoundingVolume *volume)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult::Hit *ritual_own_ZN10Qt3DRender10RayCasting18QRayCastingService5queryERKNS0_6QRay3DEPKNS0_15QBoundingVolumeE(
    Qt3DRender::RayCasting::QRayCastingService *self,
    const Qt3DRender::RayCasting::QRay3D *ray,
    const Qt3DRender::RayCasting::QBoundingVolume *volume) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult::Hit(
      self->Qt3DRender::RayCasting::QRayCastingService::query(
          *ray,
          volume));
}

//  QCollisionQueryResult
//      Qt3DRender::RayCasting::QRayCastingService::fetchResult(const
//      QQueryHandle &handle)
extern "C" Q_DECL_EXPORT
Qt3DRender::RayCasting::QCollisionQueryResult *ritual_own_ZN10Qt3DRender10RayCasting18QRayCastingService11fetchResultERKi(
    Qt3DRender::RayCasting::QRayCastingService *self,
    Qt3DRender::RayCasting::QQueryHandle handle) {
  return new Qt3DRender::RayCasting::QCollisionQueryResult(
      self->Qt3DRender::RayCasting::QRayCastingService::fetchResult(
          handle));
}
