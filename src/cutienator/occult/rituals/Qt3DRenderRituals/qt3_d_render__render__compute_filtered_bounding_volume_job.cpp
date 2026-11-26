//  Written by hand on 2026-11-25 from
//  Qt3DRender/6.12.0/Qt3DRender/private/computefilteredboundingvolumejob_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Not written: 'd_func' (its private class is not complete in any
//  header Qt installs).
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/computefilteredboundingvolumejob_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/sphere_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on Qt3DRender::Render::ComputeFilteredBoundingVolumeJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob : Qt3DRender::Render::ComputeFilteredBoundingVolumeJob {
  using Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished;
};

//  A Qt3DRender::Render::ComputeFilteredBoundingVolumeJob that Python can take functions over in. Every Qt3DRender::Render::ComputeFilteredBoundingVolumeJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef void (*CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall2)(const void *, int *);
typedef void (*CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall3)(const void *, Qt3DCore::QAspectManager *, const Qt3DRender::Render::Sphere *, int *);
class CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJob : public Qt3DRender::Render::ComputeFilteredBoundingVolumeJob {
public:
  using Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::ComputeFilteredBoundingVolumeJob;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob10isRequiredEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob9postFrameEPNS_13QAspectEngineE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob3runEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8finishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run()
  void run() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall2 call = reinterpret_cast<CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run();
  }

  //  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(Qt3DCore::QAspectManager
  //      *aspectManager, const Qt3DRender::Render::Sphere &sphere)
  void finished(Qt3DCore::QAspectManager *aspectManager, const Qt3DRender::Render::Sphere &sphere) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall3 call = reinterpret_cast<CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJobCall3>(taken[3]);
      call(this, aspectManager, &sphere, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(aspectManager, sphere);
  }
};

//  Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::ComputeFilteredBoundingVolumeJob()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJobC1Ev() {
  return new CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJob();
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::setRoot(Entity *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob7setRootEPNS0_6EntityE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DRender::Render::Entity *root) {
  self->setRoot(root);
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::setManagers(NodeManagers *manager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob11setManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DRender::Render::NodeManagers *manager) {
  self->setManagers(manager);
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::ignoreSubTree(Entity *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob13ignoreSubTreeEPNS0_6EntityE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DRender::Render::Entity *node) {
  self->ignoreSubTree(node);
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob3runEv(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self) {
  self->run();
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(Qt3DCore::QAspectManager
//      *aspectManager, const Qt3DRender::Render::Sphere &sphere)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8finishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DCore::QAspectManager *aspectManager,
    const Qt3DRender::Render::Sphere *sphere) {
  static_cast<OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob *>(self)->finished(aspectManager, *sphere);
}

//  a Python function taken by a
//      CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJob, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_ComputeFilteredBoundingVolumeJob(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_ComputeFilteredBoundingVolumeJob *>(self)->take(key, call);
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob3runEv(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self) {
  self->Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::run();
}

//  void Qt3DRender::Render::ComputeFilteredBoundingVolumeJob::finished(Qt3DCore::QAspectManager
//      *aspectManager, const Qt3DRender::Render::Sphere &sphere)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render32ComputeFilteredBoundingVolumeJob8finishedEPN8Qt3DCore14QAspectManagerERKNS0_6SphereE(
    Qt3DRender::Render::ComputeFilteredBoundingVolumeJob *self,
    Qt3DCore::QAspectManager *aspectManager,
    const Qt3DRender::Render::Sphere *sphere) {
  static_cast<OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob *>(self)->OwnQt3DRender_Render_ComputeFilteredBoundingVolumeJob::finished(
      aspectManager,
      *sphere);
}
