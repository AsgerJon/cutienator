//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

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
