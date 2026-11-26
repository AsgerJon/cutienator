//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::RenderTargetManager::RenderTargetManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderTargetManager *ritual_ZN10Qt3DRender6Render19RenderTargetManagerC1Ev() {
  return new Qt3DRender::Render::RenderTargetManager();
}

//  void Qt3DRender::Render::RenderTargetManager::addRenderTargetIdToCleanup(
//      Qt3DCore::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19RenderTargetManager26addRenderTargetIdToCleanupEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderTargetManager *self,
    const Qt3DCore::QNodeId *id) {
  self->addRenderTargetIdToCleanup(*id);
}

//  void Qt3DRender::Render::RenderTargetManager::removeRenderTargetToCleanup
//      (Qt3DCore::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19RenderTargetManager27removeRenderTargetToCleanupEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderTargetManager *self,
    const Qt3DCore::QNodeId *id) {
  self->removeRenderTargetToCleanup(*id);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::RenderTargetManager::takeRenderTargetIdsToCleanup
//      ()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render19RenderTargetManager28takeRenderTargetIdsToCleanupEv(
    Qt3DRender::Render::RenderTargetManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->takeRenderTargetIdsToCleanup());
}

//  a QList<Qt3DCore::QNodeId> a ritual of
//      Qt3DRender::Render::RenderTargetManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_RenderTargetManager__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
