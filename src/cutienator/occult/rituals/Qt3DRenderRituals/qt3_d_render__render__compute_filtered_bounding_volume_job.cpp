//  Written by dev_tooling.RitualGenerator from the records of Qt3DRender/6.1
//  2.0/Qt3DRender/private/computefilteredboundingvolumejob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/computefilteredboundingvolumejob_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/sphere_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on Qt3DRender::Render::ComputeFilteredBoundingVolumeJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob : Qt3DRender::Render::ComputeFilteredBoundingVolumeJob {
  using Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished;
};

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(Qt3DC
//      ore::QAspectManager *aspectManager, const Qt3DRender::Render::Sphere
//      &sphere)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8finishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DCore::QAspectManager *aspectManager,
    const Qt3DRender::Render::Sphere *sphere) {
  self->finished(aspectManager, *sphere);
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob3runEv(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self) {
  self->Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run();
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(Qt3DC
//      ore::QAspectManager *aspectManager, const Qt3DRender::Render::Sphere
//      &sphere)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8finishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DCore::QAspectManager *aspectManager,
    const Qt3DRender::Render::Sphere *sphere) {
  static_cast<OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob *>(self)->OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob::finished(
      aspectManager,
      *sphere);
}
