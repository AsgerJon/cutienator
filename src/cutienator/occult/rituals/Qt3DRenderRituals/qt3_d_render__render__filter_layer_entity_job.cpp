//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/filterlayerentityjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/filterlayerentityjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/Qt3DCore>

//  Qt3DRender::Render::FilterLayerEntityJob::FilterLayerEntityJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FilterLayerEntityJob *ritual_ZN10Qt3DRender6Render20FilterLayerEntityJobC1Ev() {
  return new Qt3DRender::Render::FilterLayerEntityJob();
}

//  void Qt3DRender::Render::FilterLayerEntityJob::setManager(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob10setManagerEPNS0_12NodeManagersE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManager(manager);
}

//  void Qt3DRender::Render::FilterLayerEntityJob::setLayerFilters(const
//      Qt3DCore::QNodeIdVector &layerIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob15setLayerFiltersERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    const Qt3DCore::QNodeIdVector *layerIds) {
  self->setLayerFilters(*layerIds);
}

//  std::vector<Entity *>
//      &Qt3DRender::Render::FilterLayerEntityJob::filteredEntities()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::Entity *> *ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob16filteredEntitiesEv(
    Qt3DRender::Render::FilterLayerEntityJob *self) {
  return &(self->filteredEntities());
}

//  bool Qt3DRender::Render::FilterLayerEntityJob::hasLayerFilter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render20FilterLayerEntityJob14hasLayerFilterEv(
    const Qt3DRender::Render::FilterLayerEntityJob *self) {
  return self->hasLayerFilter();
}

//  Qt3DCore::QNodeIdVector
//      Qt3DRender::Render::FilterLayerEntityJob::layerFilters() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeIdVector *ritual_ZNK10Qt3DRender6Render20FilterLayerEntityJob12layerFiltersEv(
    const Qt3DRender::Render::FilterLayerEntityJob *self) {
  return new Qt3DCore::QNodeIdVector(self->layerFilters());
}

//  void Qt3DRender::Render::FilterLayerEntityJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob3runEv(
    Qt3DRender::Render::FilterLayerEntityJob *self) {
  self->run();
}

//  void Qt3DRender::Render::FilterLayerEntityJob::filterEntityAgainstLayers(
//      Entity *entity, const Qt3DCore::QNodeIdVector &layerIds, const
//      QLayerFilter::FilterMode filterMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob25filterEntityAgainstLayersEPNS0_6EntityERK5QListIN8Qt3DCore7QNodeIdEENS_12QLayerFilter10FilterModeE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    Qt3DRender::Render::Entity *entity,
    const Qt3DCore::QNodeIdVector *layerIds,
    const Qt3DRender::QLayerFilter::FilterMode *filterMode) {
  self->filterEntityAgainstLayers(entity, *layerIds, *filterMode);
}

//  void Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAnyMatchingLay
//      ers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob29filterAcceptAnyMatchingLayersEPNS0_6EntityERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    Qt3DRender::Render::Entity *entity,
    const Qt3DCore::QNodeIdVector *layerIds) {
  self->filterAcceptAnyMatchingLayers(entity, *layerIds);
}

//  void Qt3DRender::Render::FilterLayerEntityJob::filterAcceptAllMatchingLay
//      ers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob29filterAcceptAllMatchingLayersEPNS0_6EntityERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    Qt3DRender::Render::Entity *entity,
    const Qt3DCore::QNodeIdVector *layerIds) {
  self->filterAcceptAllMatchingLayers(entity, *layerIds);
}

//  void Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAnyMatchingLa
//      yers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob30filterDiscardAnyMatchingLayersEPNS0_6EntityERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    Qt3DRender::Render::Entity *entity,
    const Qt3DCore::QNodeIdVector *layerIds) {
  self->filterDiscardAnyMatchingLayers(entity, *layerIds);
}

//  void Qt3DRender::Render::FilterLayerEntityJob::filterDiscardAllMatchingLa
//      yers(Entity *entity, const Qt3DCore::QNodeIdVector &layerIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob30filterDiscardAllMatchingLayersEPNS0_6EntityERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::FilterLayerEntityJob *self,
    Qt3DRender::Render::Entity *entity,
    const Qt3DCore::QNodeIdVector *layerIds) {
  self->filterDiscardAllMatchingLayers(entity, *layerIds);
}

//  void Qt3DRender::Render::FilterLayerEntityJob::filterLayerAndEntity()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob20filterLayerAndEntityEv(
    Qt3DRender::Render::FilterLayerEntityJob *self) {
  self->filterLayerAndEntity();
}

//  void Qt3DRender::Render::FilterLayerEntityJob::selectAllEntities()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20FilterLayerEntityJob17selectAllEntitiesEv(
    Qt3DRender::Render::FilterLayerEntityJob *self) {
  self->selectAllEntities();
}

//  a Qt3DCore::QNodeIdVector a ritual of
//      Qt3DRender::Render::FilterLayerEntityJob gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_FilterLayerEntityJob__Qt3DCore_QNodeIdVector(
    Qt3DCore::QNodeIdVector *self) {
  delete self;
}
