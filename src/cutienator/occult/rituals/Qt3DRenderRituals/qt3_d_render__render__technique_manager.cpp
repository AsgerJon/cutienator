//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/techniquemanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/techniquemanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <vector>
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::TechniqueManager::TechniqueManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TechniqueManager *ritual_ZN10Qt3DRender6Render16TechniqueManagerC1Ev() {
  return new Qt3DRender::Render::TechniqueManager();
}

//  void
//      Qt3DRender::Render::TechniqueManager::addDirtyTechnique(Qt3DCore::QNo
//      deId techniqueId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16TechniqueManager17addDirtyTechniqueEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::TechniqueManager *self,
    const Qt3DCore::QNodeId *techniqueId) {
  self->addDirtyTechnique(*techniqueId);
}

//  std::vector<Qt3DCore::QNodeId>
//      Qt3DRender::Render::TechniqueManager::takeDirtyTechniques()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DCore::QNodeId> *ritual_ZN10Qt3DRender6Render16TechniqueManager19takeDirtyTechniquesEv(
    Qt3DRender::Render::TechniqueManager *self) {
  return new std::vector<Qt3DCore::QNodeId>(self->takeDirtyTechniques());
}

//  a std::vector<Qt3DCore::QNodeId> a ritual of
//      Qt3DRender::Render::TechniqueManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_TechniqueManager__std_vector_Qt3DCore_QNodeId(
    std::vector<Qt3DCore::QNodeId> *self) {
  delete self;
}
