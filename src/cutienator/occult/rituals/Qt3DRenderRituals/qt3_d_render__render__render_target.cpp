//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/rendertarget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/rendertarget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::RenderTarget::RenderTarget()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderTarget *ritual_ZN10Qt3DRender6Render12RenderTargetC1Ev() {
  return new Qt3DRender::Render::RenderTarget();
}

//  void Qt3DRender::Render::RenderTarget::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12RenderTarget7cleanupEv(
    Qt3DRender::Render::RenderTarget *self) {
  self->cleanup();
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::RenderTarget::renderOutputs() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render12RenderTarget13renderOutputsEv(
    const Qt3DRender::Render::RenderTarget *self) {
  return new QList<Qt3DCore::QNodeId>(self->renderOutputs());
}

//  bool Qt3DRender::Render::RenderTarget::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12RenderTarget7isDirtyEv(
    const Qt3DRender::Render::RenderTarget *self) {
  return self->isDirty();
}

//  void Qt3DRender::Render::RenderTarget::unsetDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12RenderTarget10unsetDirtyEv(
    Qt3DRender::Render::RenderTarget *self) {
  self->unsetDirty();
}

//  void Qt3DRender::Render::RenderTarget::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12RenderTarget16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderTarget *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::RenderTarget::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12RenderTarget16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderTarget *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderTarget::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::RenderTarget
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_RenderTarget__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
