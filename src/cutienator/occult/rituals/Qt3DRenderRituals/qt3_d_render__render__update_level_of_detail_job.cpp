//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/updatelevelofdetailjob_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/updatelevelofdetailjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::UpdateLevelOfDetailJob that Python can take functions over in. Every Qt3DRender::Render::UpdateLevelOfDetailJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_UpdateLevelOfDetailJobCall0)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DRender_Render_UpdateLevelOfDetailJobCall1)(const void *, int *);
class CuteQt3DRender_Render_UpdateLevelOfDetailJob : public Qt3DRender::Render::UpdateLevelOfDetailJob {
public:
  using Qt3DRender::Render::UpdateLevelOfDetailJob::UpdateLevelOfDetailJob;
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
      CuteQt3DRender_Render_UpdateLevelOfDetailJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_UpdateLevelOfDetailJobCall0>(taken[0]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_UpdateLevelOfDetailJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_UpdateLevelOfDetailJobCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  NodeManagers *Qt3DRender::Render::UpdateLevelOfDetailJob::managers()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender6Render22UpdateLevelOfDetailJob8managersEv(
    const Qt3DRender::Render::UpdateLevelOfDetailJob *self) {
  return self->managers();
}

//  Entity *Qt3DRender::Render::UpdateLevelOfDetailJob::root() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Entity *ritual_ZNK10Qt3DRender6Render22UpdateLevelOfDetailJob4rootEv(
    const Qt3DRender::Render::UpdateLevelOfDetailJob *self) {
  return self->root();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_UpdateLevelOfDetailJob, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_UpdateLevelOfDetailJob(
    Qt3DRender::Render::UpdateLevelOfDetailJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_UpdateLevelOfDetailJob *>(self)->take(key, call);
}
