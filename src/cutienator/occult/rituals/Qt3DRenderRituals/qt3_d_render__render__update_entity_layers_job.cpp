//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/updateentitylayersjob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/updateentitylayersjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::UpdateEntityLayersJob::UpdateEntityLayersJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UpdateEntityLayersJob *ritual_ZN10Qt3DRender6Render21UpdateEntityLayersJobC1Ev() {
  return new Qt3DRender::Render::UpdateEntityLayersJob();
}

//  void Qt3DRender::Render::UpdateEntityLayersJob::setManager(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21UpdateEntityLayersJob10setManagerEPNS0_12NodeManagersE(
    Qt3DRender::Render::UpdateEntityLayersJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManager(manager);
}

//  NodeManagers *Qt3DRender::Render::UpdateEntityLayersJob::manager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender6Render21UpdateEntityLayersJob7managerEv(
    const Qt3DRender::Render::UpdateEntityLayersJob *self) {
  return self->manager();
}

//  void Qt3DRender::Render::UpdateEntityLayersJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render21UpdateEntityLayersJob3runEv(
    Qt3DRender::Render::UpdateEntityLayersJob *self) {
  self->run();
}
