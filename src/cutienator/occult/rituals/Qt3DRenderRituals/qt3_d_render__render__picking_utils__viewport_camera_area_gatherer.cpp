//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickboundingvolumeutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::ViewportCam
//      eraAreaGatherer(const Qt3DCore::QNodeId &nodeId)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGathererC1ERKN8Qt3DCore7QNodeIdE(
    const Qt3DCore::QNodeId *nodeId) {
  return new Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer(
      *nodeId);
}

//  Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer::~ViewportCa
//      meraAreaGatherer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12PickingUtils26ViewportCameraAreaGathererD1Ev(
    Qt3DRender::Render::PickingUtils::ViewportCameraAreaGatherer *self) {
  delete self;
}
