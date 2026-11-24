//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/proximityfilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/proximityfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  float Qt3DRender::Render::ProximityFilter::distanceThreshold() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render15ProximityFilter17distanceThresholdEv(
    const Qt3DRender::Render::ProximityFilter *self) {
  return self->distanceThreshold();
}

//  Qt3DCore::QNodeId Qt3DRender::Render::ProximityFilter::entityId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render15ProximityFilter8entityIdEv(
    const Qt3DRender::Render::ProximityFilter *self) {
  return new Qt3DCore::QNodeId(self->entityId());
}

//  void Qt3DRender::Render::ProximityFilter::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15ProximityFilter16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::ProximityFilter *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::ProximityFilter::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
