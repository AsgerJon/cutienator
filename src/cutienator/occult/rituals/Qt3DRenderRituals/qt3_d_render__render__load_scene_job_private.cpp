//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::LoadSceneJobPrivate that Python can take functions over in. Every Qt3DRender::Render::LoadSceneJobPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_LoadSceneJobPrivateCall0)(const void *, Qt3DCore::QAspectManager *, int *);
typedef bool (*CuteQt3DRender_Render_LoadSceneJobPrivateCall1)(const void *, int *);
class CuteQt3DRender_Render_LoadSceneJobPrivate : public Qt3DRender::Render::LoadSceneJobPrivate {
public:
  using Qt3DRender::Render::LoadSceneJobPrivate::LoadSceneJobPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore17QAspectJobPrivate9postFrameEPNS_14QAspectManagerE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Qt3DCore17QAspectJobPrivate10isRequiredEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::LoadSceneJobPrivate::postFrame(Qt3DCore::QAs
  //      pectManager *manager)
  void postFrame(Qt3DCore::QAspectManager *manager) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadSceneJobPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Render_LoadSceneJobPrivateCall0>(taken[0]);
      call(this, manager, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::LoadSceneJobPrivate::postFrame(manager);
  }

  //  bool Qt3DCore::QAspectJobPrivate::isRequired() const
  bool isRequired() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_LoadSceneJobPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Render_LoadSceneJobPrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DCore::QAspectJobPrivate::isRequired();
  }
};

//  Qt3DRender::Render::LoadSceneJobPrivate::~LoadSceneJobPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivateD1Ev(
    Qt3DRender::Render::LoadSceneJobPrivate *self) {
  delete self;
}

//  LoadSceneJob *Qt3DRender::Render::LoadSceneJobPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::LoadSceneJob *ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivate6q_funcEv(
    Qt3DRender::Render::LoadSceneJobPrivate *self) {
  return self->q_func();
}

//  const LoadSceneJob *Qt3DRender::Render::LoadSceneJobPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::LoadSceneJob *ritual_ZNK10Qt3DRender6Render19LoadSceneJobPrivate6q_funcEv(
    const Qt3DRender::Render::LoadSceneJobPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_Render_LoadSceneJobPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_LoadSceneJobPrivate(
    Qt3DRender::Render::LoadSceneJobPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_LoadSceneJobPrivate *>(self)->take(key, call);
}
