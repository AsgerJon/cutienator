//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/loadgeometryjob_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/loadgeometryjob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on Qt3DRender::Render::LoadGeometryJob may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQt3DRender_Render_LoadGeometryJob : Qt3DRender::Render::LoadGeometryJob {
  using Qt3DRender::Render::LoadGeometryJob::run;
};

//  A Qt3DRender::Render::LoadGeometryJob that Python can take functions over in. Every Qt3DRender::Render::LoadGeometryJob
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_LoadGeometryJobCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_LoadGeometryJobCall1)(const void *, Qt3DCore::QAspectEngine *, int *);
typedef bool (*CuteQt3DRender_Render_LoadGeometryJobCall2)(const void *, int *);
class CuteQt3DRender_Render_LoadGeometryJob : public Qt3DRender::Render::LoadGeometryJob {
public:
  using Qt3DRender::Render::LoadGeometryJob::LoadGeometryJob;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore10QAspectJob3runEv")) {
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

  //  void Qt3DRender::Render::LoadGeometryJob::run()
  void run() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadGeometryJobCall0 call = reinterpret_cast<CuteQt3DRender_Render_LoadGeometryJobCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::LoadGeometryJob::run();
  }

  //  void Qt3DCore::QAspectJob::postFrame(QAspectEngine *aspectEngine)
  void postFrame(Qt3DCore::QAspectEngine *aspectEngine) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadGeometryJobCall1 call = reinterpret_cast<CuteQt3DRender_Render_LoadGeometryJobCall1>(taken[1]);
      call(this, aspectEngine, &handled);
      if (handled) return;
    }
    Qt3DCore::QAspectJob::postFrame(aspectEngine);
  }

  //  bool Qt3DCore::QAspectJob::isRequired()
  bool isRequired() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadGeometryJobCall2 call = reinterpret_cast<CuteQt3DRender_Render_LoadGeometryJobCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJob::isRequired();
  }
};

//  void Qt3DRender::Render::LoadGeometryJob::setNodeManagers(NodeManagers
//      *nodeManagers)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15LoadGeometryJob15setNodeManagersEPNS0_12NodeManagersE(
    Qt3DRender::Render::LoadGeometryJob *self,
    Qt3DRender::Render::NodeManagers *nodeManagers) {
  self->setNodeManagers(nodeManagers);
}

//  a Python function taken by a CuteQt3DRender_Render_LoadGeometryJob, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_LoadGeometryJob(
    Qt3DRender::Render::LoadGeometryJob *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_LoadGeometryJob *>(self)->take(key, call);
}

//  void Qt3DRender::Render::LoadGeometryJob::run()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15LoadGeometryJob3runEv(
    Qt3DRender::Render::LoadGeometryJob *self) {
  static_cast<OwnQt3DRender_Render_LoadGeometryJob *>(self)->OwnQt3DRender_Render_LoadGeometryJob::run();
}
