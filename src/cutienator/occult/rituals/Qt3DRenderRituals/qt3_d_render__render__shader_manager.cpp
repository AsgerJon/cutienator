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

//  Qt3DRender::Render::ShaderManager::ShaderManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ShaderManager *ritual_ZN10Qt3DRender6Render13ShaderManagerC1Ev() {
  return new Qt3DRender::Render::ShaderManager();
}

//  void
//      Qt3DRender::Render::ShaderManager::addShaderIdToCleanup(Qt3DCore::QNo
//      deId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderManager20addShaderIdToCleanupEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::ShaderManager *self,
    const Qt3DCore::QNodeId *id) {
  self->addShaderIdToCleanup(*id);
}

//  void Qt3DRender::Render::ShaderManager::removeShaderIdFromIdsToCleanup(Qt
//      3DCore::QNodeId id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13ShaderManager30removeShaderIdFromIdsToCleanupEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::ShaderManager *self,
    const Qt3DCore::QNodeId *id) {
  self->removeShaderIdFromIdsToCleanup(*id);
}

//  bool
//      Qt3DRender::Render::ShaderManager::hasShaderIdToCleanup(Qt3DCore::QNo
//      deId id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render13ShaderManager20hasShaderIdToCleanupEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::ShaderManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->hasShaderIdToCleanup(*id);
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::ShaderManager::shaderIdsToCleanup() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render13ShaderManager18shaderIdsToCleanupEv(
    const Qt3DRender::Render::ShaderManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->shaderIdsToCleanup());
}

//  QList<Qt3DCore::QNodeId>
//      Qt3DRender::Render::ShaderManager::takeShaderIdsToCleanup()
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render13ShaderManager22takeShaderIdsToCleanupEv(
    Qt3DRender::Render::ShaderManager *self) {
  return new QList<Qt3DCore::QNodeId>(self->takeShaderIdsToCleanup());
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::ShaderManager
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_ShaderManager__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
