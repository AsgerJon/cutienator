//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/materialparametergathererjob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/materialparametergathererjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void Qt3DRender::Render::MaterialParameterGathererJob::setNodeManagers(No
//      deManagers *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob15setNodeManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::MaterialParameterGathererJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setNodeManagers(manager);
}

//  void Qt3DRender::Render::MaterialParameterGathererJob::setTechniqueFilter
//      (TechniqueFilter *techniqueFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob18setTechniqueFilterEPNS0_15TechniqueFilterE(
    Qt3DRender::Render::MaterialParameterGathererJob *self,
    Qt3DRender::Render::TechniqueFilter *techniqueFilter) {
  self->setTechniqueFilter(techniqueFilter);
}

//  void Qt3DRender::Render::MaterialParameterGathererJob::setRenderPassFilte
//      r(RenderPassFilter *renderPassFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob19setRenderPassFilterEPNS0_16RenderPassFilterE(
    Qt3DRender::Render::MaterialParameterGathererJob *self,
    Qt3DRender::Render::RenderPassFilter *renderPassFilter) {
  self->setRenderPassFilter(renderPassFilter);
}

//  TechniqueFilter
//      *Qt3DRender::Render::MaterialParameterGathererJob::techniqueFilter()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::TechniqueFilter *ritual_ZNK10Qt3DRender6Render28MaterialParameterGathererJob15techniqueFilterEv(
    const Qt3DRender::Render::MaterialParameterGathererJob *self) {
  return self->techniqueFilter();
}

//  RenderPassFilter
//      *Qt3DRender::Render::MaterialParameterGathererJob::renderPassFilter()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderPassFilter *ritual_ZNK10Qt3DRender6Render28MaterialParameterGathererJob16renderPassFilterEv(
    const Qt3DRender::Render::MaterialParameterGathererJob *self) {
  return self->renderPassFilter();
}
