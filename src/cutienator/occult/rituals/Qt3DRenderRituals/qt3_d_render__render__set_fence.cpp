//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/setfence_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/setfence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::SetFence that Python can take functions over in. Every Qt3DRender::Render::SetFence
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_SetFenceCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_SetFence : public Qt3DRender::Render::SetFence {
public:
  using Qt3DRender::Render::SetFence::SetFence;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_SetFenceCall0 call = reinterpret_cast<CuteQt3DRender_Render_SetFenceCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::SetFence::SetFence()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::SetFence *ritual_ZN10Qt3DRender6Render8SetFenceC1Ev() {
  return new CuteQt3DRender_Render_SetFence();
}

//  Qt3DRender::Render::SetFence::~SetFence()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8SetFenceD1Ev(
    Qt3DRender::Render::SetFence *self) {
  delete self;
}

//  a Python function taken by a CuteQt3DRender_Render_SetFence, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_SetFence(
    Qt3DRender::Render::SetFence *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_SetFence *>(self)->take(key, call);
}
