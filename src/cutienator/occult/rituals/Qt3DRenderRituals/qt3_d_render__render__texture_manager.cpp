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

//  Qt3DRender::Render::TextureManager::TextureManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TextureManager *ritual_ZN10Qt3DRender6Render14TextureManagerC1Ev() {
  return new Qt3DRender::Render::TextureManager();
}

//  void Qt3DRender::Render::TextureManager::addTextureIdToCleanup(Qt3DCore::
//      QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14TextureManager21addTextureIdToCleanupEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::TextureManager *self,
    const Qt3DCore::QNodeId *id) {
  self->addTextureIdToCleanup(*id);
}

//  void Qt3DRender::Render::TextureManager::removeTextureIdToCleanup(Qt3DCor
//      e::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14TextureManager24removeTextureIdToCleanupEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::TextureManager *self,
    const Qt3DCore::QNodeId *id) {
  self->removeTextureIdToCleanup(*id);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::TextureManager::takeTexturesIdsToCleanup()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render14TextureManager24takeTexturesIdsToCleanupEv(
    Qt3DRender::Render::TextureManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->takeTexturesIdsToCleanup());
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::TextureManager
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_TextureManager__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
