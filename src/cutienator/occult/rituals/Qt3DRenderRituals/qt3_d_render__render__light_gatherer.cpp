//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/lightgatherer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/lightgatherer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DRender::Render::LightGatherer::setManager(EntityManager
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13LightGatherer10setManagerEPNS0_13EntityManagerE(
    Qt3DRender::Render::LightGatherer *self,
    Qt3DRender::Render::EntityManager *manager) {
  self->setManager(manager);
}

//  EnvironmentLight *Qt3DRender::Render::LightGatherer::environmentLight()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::EnvironmentLight *ritual_ZNK10Qt3DRender6Render13LightGatherer16environmentLightEv(
    const Qt3DRender::Render::LightGatherer *self) {
  return self->environmentLight();
}

//  void Qt3DRender::Render::LightGatherer::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render13LightGatherer3runEv(
    Qt3DRender::Render::LightGatherer *self) {
  self->Qt3DRender::Render::LightGatherer::run();
}
