//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/updateshaderdatatransformjob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/updateshaderdatatransformjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::UpdateShaderDataTransformJob that Python can take functions over in. Every Qt3DRender::Render::UpdateShaderDataTransformJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_UpdateShaderDataTransformJobCall0)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DRender_Render_UpdateShaderDataTransformJobCall1)(const void *, int *);
class CuteQt3DRender_Render_UpdateShaderDataTransformJob : public Qt3DRender::Render::UpdateShaderDataTransformJob {
public:
  using Qt3DRender::Render::UpdateShaderDataTransformJob::UpdateShaderDataTransformJob;
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
      CuteQt3DRender_Render_UpdateShaderDataTransformJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_UpdateShaderDataTransformJobCall0>(taken[0]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_UpdateShaderDataTransformJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_UpdateShaderDataTransformJobCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  Qt3DRender::Render::UpdateShaderDataTransformJob::UpdateShaderDataTransfo
//      rmJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::UpdateShaderDataTransformJob *ritual_ZN10Qt3DRender6Render28UpdateShaderDataTransformJobC1Ev() {
  return new CuteQt3DRender_Render_UpdateShaderDataTransformJob();
}

//  Qt3DRender::Render::UpdateShaderDataTransformJob::~UpdateShaderDataTransf
//      ormJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28UpdateShaderDataTransformJobD1Ev(
    Qt3DRender::Render::UpdateShaderDataTransformJob *self) {
  delete self;
}

//  void Qt3DRender::Render::UpdateShaderDataTransformJob::setManagers(NodeMa
//      nagers *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28UpdateShaderDataTransformJob11setManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::UpdateShaderDataTransformJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManagers(manager);
}

//  NodeManagers
//      *Qt3DRender::Render::UpdateShaderDataTransformJob::managers() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender6Render28UpdateShaderDataTransformJob8managersEv(
    const Qt3DRender::Render::UpdateShaderDataTransformJob *self) {
  return self->managers();
}

//  void Qt3DRender::Render::UpdateShaderDataTransformJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render28UpdateShaderDataTransformJob3runEv(
    Qt3DRender::Render::UpdateShaderDataTransformJob *self) {
  self->run();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_UpdateShaderDataTransformJob, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_UpdateShaderDataTransformJob(
    Qt3DRender::Render::UpdateShaderDataTransformJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_UpdateShaderDataTransformJob *>(self)->take(key, call);
}
