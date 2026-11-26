//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/filtercompatibletechniquejob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/filtercompatibletechniquejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::FilterCompatibleTechniqueJob::FilterCompatibleTechniq
//      ueJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FilterCompatibleTechniqueJob *ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJobC1Ev() {
  return new Qt3DRender::Render::FilterCompatibleTechniqueJob();
}

//  void Qt3DRender::Render::FilterCompatibleTechniqueJob::setManager(Techniq
//      ueManager *managers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob10setManagerEPNS0_16TechniqueManagerE(
    Qt3DRender::Render::FilterCompatibleTechniqueJob *self,
    Qt3DRender::Render::TechniqueManager *managers) {
  self->setManager(managers);
}

//  TechniqueManager
//      *Qt3DRender::Render::FilterCompatibleTechniqueJob::manager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TechniqueManager *ritual_ZNK10Qt3DRender6Render28FilterCompatibleTechniqueJob7managerEv(
    const Qt3DRender::Render::FilterCompatibleTechniqueJob *self) {
  return self->manager();
}

//  void Qt3DRender::Render::FilterCompatibleTechniqueJob::setRenderer(Abstra
//      ctRenderer *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob11setRendererEPNS0_16AbstractRendererE(
    Qt3DRender::Render::FilterCompatibleTechniqueJob *self,
    Qt3DRender::Render::AbstractRenderer *renderer) {
  self->setRenderer(renderer);
}

//  AbstractRenderer
//      *Qt3DRender::Render::FilterCompatibleTechniqueJob::renderer() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AbstractRenderer *ritual_ZNK10Qt3DRender6Render28FilterCompatibleTechniqueJob8rendererEv(
    const Qt3DRender::Render::FilterCompatibleTechniqueJob *self) {
  return self->renderer();
}

//  void Qt3DRender::Render::FilterCompatibleTechniqueJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob3runEv(
    Qt3DRender::Render::FilterCompatibleTechniqueJob *self) {
  self->run();
}

//  void Qt3DRender::Render::FilterCompatibleTechniqueJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render28FilterCompatibleTechniqueJob3runEv(
    Qt3DRender::Render::FilterCompatibleTechniqueJob *self) {
  self->Qt3DRender::Render::FilterCompatibleTechniqueJob::run();
}
