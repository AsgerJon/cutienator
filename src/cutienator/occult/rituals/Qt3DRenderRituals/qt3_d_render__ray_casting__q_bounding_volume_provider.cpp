//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qboundingvolumeprovider_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qboundingvolumeprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>

//  Qt3DRender::RayCasting::QBoundingVolumeProvider::~QBoundingVolumeProvider
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10RayCasting23QBoundingVolumeProviderD1Ev(
    Qt3DRender::RayCasting::QBoundingVolumeProvider *self) {
  delete self;
}

//  QList<QBoundingVolume *>
//      Qt3DRender::RayCasting::QBoundingVolumeProvider::boundingVolumes()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DRender::RayCasting::QBoundingVolume *> *ritual_ZNK10Qt3DRender10RayCasting23QBoundingVolumeProvider15boundingVolumesEv(
    const Qt3DRender::RayCasting::QBoundingVolumeProvider *self) {
  return new QList<Qt3DRender::RayCasting::QBoundingVolume *>(
      self->boundingVolumes());
}

//  a QList<Qt3DRender::RayCasting::QBoundingVolume *> a ritual of
//      Qt3DRender::RayCasting::QBoundingVolumeProvider gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_RayCasting_QBoundingVolumeProvider__QList_Qt3DRender_RayCasting_QBoundingVolume(
    QList<Qt3DRender::RayCasting::QBoundingVolume *> *self) {
  delete self;
}
