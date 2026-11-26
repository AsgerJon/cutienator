//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/cameraselectornode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/cameraselectornode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DRender::Render::CameraSelector::CameraSelector()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::CameraSelector *ritual_ZN10Qt3DRender6Render14CameraSelectorC1Ev() {
  return new Qt3DRender::Render::CameraSelector();
}

//  Qt3DCore::QNodeId Qt3DRender::Render::CameraSelector::cameraUuid() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render14CameraSelector10cameraUuidEv(
    const Qt3DRender::Render::CameraSelector *self) {
  return new Qt3DCore::QNodeId(self->cameraUuid());
}

//  void Qt3DRender::Render::CameraSelector::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14CameraSelector16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::CameraSelector *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::CameraSelector::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render14CameraSelector16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::CameraSelector *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::CameraSelector::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
