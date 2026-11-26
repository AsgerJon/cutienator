//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/dispatchcompute_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/dispatchcompute_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::DispatchCompute that Python can take functions over in. Every Qt3DRender::Render::DispatchCompute
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_DispatchComputeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_DispatchCompute : public Qt3DRender::Render::DispatchCompute {
public:
  using Qt3DRender::Render::DispatchCompute::DispatchCompute;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::DispatchCompute::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_DispatchComputeCall0 call = reinterpret_cast<CuteQt3DRender_Render_DispatchComputeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::DispatchCompute::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::DispatchCompute::DispatchCompute()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::DispatchCompute *ritual_ZN10Qt3DRender6Render15DispatchComputeC1Ev() {
  return new CuteQt3DRender_Render_DispatchCompute();
}

//  Qt3DRender::Render::DispatchCompute::~DispatchCompute()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15DispatchComputeD1Ev(
    Qt3DRender::Render::DispatchCompute *self) {
  delete self;
}

//  void Qt3DRender::Render::DispatchCompute::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15DispatchCompute7cleanupEv(
    Qt3DRender::Render::DispatchCompute *self) {
  self->cleanup();
}

//  int Qt3DRender::Render::DispatchCompute::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render15DispatchCompute1xEv(
    const Qt3DRender::Render::DispatchCompute *self) {
  return self->x();
}

//  int Qt3DRender::Render::DispatchCompute::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render15DispatchCompute1yEv(
    const Qt3DRender::Render::DispatchCompute *self) {
  return self->y();
}

//  int Qt3DRender::Render::DispatchCompute::z() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render15DispatchCompute1zEv(
    const Qt3DRender::Render::DispatchCompute *self) {
  return self->z();
}

//  void Qt3DRender::Render::DispatchCompute::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15DispatchCompute16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::DispatchCompute *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  a Python function taken by a CuteQt3DRender_Render_DispatchCompute, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_DispatchCompute(
    Qt3DRender::Render::DispatchCompute *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_DispatchCompute *>(self)->take(key, call);
}

//  void Qt3DRender::Render::DispatchCompute::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15DispatchCompute16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::DispatchCompute *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::DispatchCompute::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
