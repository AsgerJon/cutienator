//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendersettings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendersettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/qstring.h>

//  Qt3DRender::Render::RenderSettings::RenderSettings()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderSettings *ritual_ZN10Qt3DRender6Render14RenderSettingsC1Ev() {
  return new Qt3DRender::Render::RenderSettings();
}

//  void Qt3DRender::Render::RenderSettings::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderSettings16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderSettings *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId
//      Qt3DRender::Render::RenderSettings::activeFrameGraphID() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render14RenderSettings18activeFrameGraphIDEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return new Qt3DCore::QNodeId(self->activeFrameGraphID());
}

//  QRenderSettings::RenderPolicy
//      Qt3DRender::Render::RenderSettings::renderPolicy() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderSettings::RenderPolicy ritual_ZNK10Qt3DRender6Render14RenderSettings12renderPolicyEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return self->renderPolicy();
}

//  QPickingSettings::PickMethod
//      Qt3DRender::Render::RenderSettings::pickMethod() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickingSettings::PickMethod ritual_ZNK10Qt3DRender6Render14RenderSettings10pickMethodEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return self->pickMethod();
}

//  QPickingSettings::PickResultMode
//      Qt3DRender::Render::RenderSettings::pickResultMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickingSettings::PickResultMode ritual_ZNK10Qt3DRender6Render14RenderSettings14pickResultModeEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return self->pickResultMode();
}

//  QPickingSettings::FaceOrientationPickingMode
//      Qt3DRender::Render::RenderSettings::faceOrientationPickingMode()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickingSettings::FaceOrientationPickingMode ritual_ZNK10Qt3DRender6Render14RenderSettings26faceOrientationPickingModeEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return self->faceOrientationPickingMode();
}

//  float Qt3DRender::Render::RenderSettings::pickWorldSpaceTolerance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render14RenderSettings23pickWorldSpaceToleranceEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return self->pickWorldSpaceTolerance();
}

//  QString Qt3DRender::Render::RenderSettings::capabilities() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender6Render14RenderSettings12capabilitiesEv(
    const Qt3DRender::Render::RenderSettings *self) {
  return new QString(self->capabilities());
}

//  void Qt3DRender::Render::RenderSettings::setActiveFrameGraphId(Qt3DCore::
//      QNodeId frameGraphNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14RenderSettings21setActiveFrameGraphIdEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderSettings *self,
    const Qt3DCore::QNodeId *frameGraphNodeId) {
  self->setActiveFrameGraphId(*frameGraphNodeId);
}

//  void Qt3DRender::Render::RenderSettings::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render14RenderSettings16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderSettings *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderSettings::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
