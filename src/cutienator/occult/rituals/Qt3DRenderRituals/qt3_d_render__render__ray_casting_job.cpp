//  Written by hand on 2026-11-25 from
//  Qt3DRender/6.12.0/Qt3DRender/private/raycastingjob_p.h, Qt 6.12.0,
//  from Qt's source. Kept as it is when the generator runs again. Left
//  out: d_func() (the private class is only declared where the header is
//  read, so it cannot be named). Left out: both pick
//  (QAbstractRayCaster::Hits, QList) and dispatchHits (std::vector) are
//  not written.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/raycastingjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::RayCastingJob that Python can take functions over
//      in. Every Qt3DRender::Render::RayCastingJob Python makes is one. Each
//      function below asks the Python function handed over for it, and runs
//      Qt's own without one.
typedef bool (*CuteQt3DRender_Render_RayCastingJobCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_RayCastingJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DRender_Render_RayCastingJobCall2)(const void *, int *);
class CuteQt3DRender_Render_RayCastingJob : public Qt3DRender::Render::RayCastingJob {
public:
  using Qt3DRender::Render::RayCastingJob::RayCastingJob;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render18AbstractPickingJob9runHelperEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DRender::Render::RayCastingJob::runHelper()
  bool runHelper() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_RayCastingJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_RayCastingJobCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DRender::Render::RayCastingJob::runHelper();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_RayCastingJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_RayCastingJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_RayCastingJobCall2 call = reinterpret_cast<CuteQt3DRender_Render_RayCastingJobCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  Qt3DRender::Render::RayCastingJob::RayCastingJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RayCastingJob *ritual_ZN10Qt3DRender6Render13RayCastingJobC1Ev() {
  return new CuteQt3DRender_Render_RayCastingJob();
}

//  Qt3DRender::Render::RayCastingJob::~RayCastingJob()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13RayCastingJobD1Ev(
    Qt3DRender::Render::RayCastingJob *self) {
  delete self;
}

//  void Qt3DRender::Render::RayCastingJob::markCastersDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13RayCastingJob16markCastersDirtyEv(
    Qt3DRender::Render::RayCastingJob *self) {
  self->markCastersDirty();
}

//  bool Qt3DRender::Render::RayCastingJob::runHelper()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render13RayCastingJob9runHelperEv(
    Qt3DRender::Render::RayCastingJob *self) {
  return self->runHelper();
}

//  a Python function taken by a CuteQt3DRender_Render_RayCastingJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_RayCastingJob(
    Qt3DRender::Render::RayCastingJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_RayCastingJob *>(self)->take(key, call);
}

//  bool Qt3DRender::Render::RayCastingJob::runHelper()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender6Render13RayCastingJob9runHelperEv(
    Qt3DRender::Render::RayCastingJob *self) {
  return self->Qt3DRender::Render::RayCastingJob::runHelper();
}
