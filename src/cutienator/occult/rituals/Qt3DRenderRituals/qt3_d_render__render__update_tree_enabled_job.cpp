//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/updatetreeenabledjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/updatetreeenabledjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::UpdateTreeEnabledJob::UpdateTreeEnabledJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UpdateTreeEnabledJob *ritual_ZN10Qt3DRender6Render20UpdateTreeEnabledJobC1Ev() {
  return new Qt3DRender::Render::UpdateTreeEnabledJob();
}

//  void Qt3DRender::Render::UpdateTreeEnabledJob::setRoot(Entity *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20UpdateTreeEnabledJob7setRootEPNS0_6EntityE(
    Qt3DRender::Render::UpdateTreeEnabledJob *self,
    Qt3DRender::Render::Entity *root) {
  self->setRoot(root);
}

//  void Qt3DRender::Render::UpdateTreeEnabledJob::setManagers(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20UpdateTreeEnabledJob11setManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::UpdateTreeEnabledJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManagers(manager);
}

//  void Qt3DRender::Render::UpdateTreeEnabledJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render20UpdateTreeEnabledJob3runEv(
    Qt3DRender::Render::UpdateTreeEnabledJob *self) {
  self->run();
}

//  void Qt3DRender::Render::UpdateTreeEnabledJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render20UpdateTreeEnabledJob3runEv(
    Qt3DRender::Render::UpdateTreeEnabledJob *self) {
  self->Qt3DRender::Render::UpdateTreeEnabledJob::run();
}
