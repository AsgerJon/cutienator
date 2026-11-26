//  Written by hand on 2026-11-25 from
//  Qt3DRender/6.12.0/Qt3DRender/private/materialparametergathererjob_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again. Left out: d_func() (the private class is only declared where
//  the header is read, so it cannot be named). Left out:
//  materialToPassAndParameter and both setHandles (std:: types) are not
//  written.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/materialparametergathererjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::MaterialParameterGathererJob that Python can take
//      functions over in. Every
//      Qt3DRender::Render::MaterialParameterGathererJob Python makes is one.
//      Each function below asks the Python function handed over for it, and
//      runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_MaterialParameterGathererJobCall0)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DRender_Render_MaterialParameterGathererJobCall1)(const void *, int *);
class CuteQt3DRender_Render_MaterialParameterGathererJob : public Qt3DRender::Render::MaterialParameterGathererJob {
public:
  using Qt3DRender::Render::MaterialParameterGathererJob::MaterialParameterGathererJob;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_MaterialParameterGathererJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_MaterialParameterGathererJobCall0>(taken[0]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_MaterialParameterGathererJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_MaterialParameterGathererJobCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  Qt3DRender::Render::MaterialParameterGathererJob::MaterialParameterGathererJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::MaterialParameterGathererJob *ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJobC1Ev() {
  return new CuteQt3DRender_Render_MaterialParameterGathererJob();
}

//  Qt3DRender::Render::MaterialParameterGathererJob::~MaterialParameterGathererJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJobD1Ev(
    Qt3DRender::Render::MaterialParameterGathererJob *self) {
  delete self;
}

//  void
//      Qt3DRender::Render::MaterialParameterGathererJob::setNodeManagers(NodeManagers
//      *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob15setNodeManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::MaterialParameterGathererJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setNodeManagers(manager);
}

//  void
//      Qt3DRender::Render::MaterialParameterGathererJob::setTechniqueFilter(TechniqueFilter
//      *techniqueFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob18setTechniqueFilterEPNS0_15TechniqueFilterE(
    Qt3DRender::Render::MaterialParameterGathererJob *self,
    Qt3DRender::Render::TechniqueFilter *techniqueFilter) {
  self->setTechniqueFilter(techniqueFilter);
}

//  void
//      Qt3DRender::Render::MaterialParameterGathererJob::setRenderPassFilter(RenderPassFilter
//      *renderPassFilter)
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
Qt3DRender::Render::TechniqueFilter * ritual_ZNK10Qt3DRender6Render28MaterialParameterGathererJob15techniqueFilterEv(
    const Qt3DRender::Render::MaterialParameterGathererJob *self) {
  return self->techniqueFilter();
}

//  RenderPassFilter
//      *Qt3DRender::Render::MaterialParameterGathererJob::renderPassFilter()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderPassFilter * ritual_ZNK10Qt3DRender6Render28MaterialParameterGathererJob16renderPassFilterEv(
    const Qt3DRender::Render::MaterialParameterGathererJob *self) {
  return self->renderPassFilter();
}

//  void Qt3DRender::Render::MaterialParameterGathererJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28MaterialParameterGathererJob3runEv(
    Qt3DRender::Render::MaterialParameterGathererJob *self) {
  self->run();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_MaterialParameterGathererJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_MaterialParameterGathererJob(
    Qt3DRender::Render::MaterialParameterGathererJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_MaterialParameterGathererJob *>(self)->take(key, call);
}
