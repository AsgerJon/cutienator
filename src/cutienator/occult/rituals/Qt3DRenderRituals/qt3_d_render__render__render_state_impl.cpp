//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/genericstate_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/genericstate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::RenderStateImpl that Python can take functions over in. Every Qt3DRender::Render::RenderStateImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQt3DRender_Render_RenderStateImplCall0)(const void *, int *);
typedef void (*CuteQt3DRender_Render_RenderStateImplCall1)(const void *, const Qt3DRender::QRenderState *, int *);
class CuteQt3DRender_Render_RenderStateImpl : public Qt3DRender::Render::RenderStateImpl {
public:
  using Qt3DRender::Render::RenderStateImpl::RenderStateImpl;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK10Qt3DRender6Render15RenderStateImpl4maskEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render15RenderStateImpl16updatePropertiesEPKNS_12QRenderStateE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  StateMask Qt3DRender::Render::RenderStateImpl::mask() const
  Qt3DRender::Render::StateMask mask() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_RenderStateImplCall0 call = reinterpret_cast<CuteQt3DRender_Render_RenderStateImplCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<Qt3DRender::Render::StateMask>(given);
    }
    return {};
  }

  //  void Qt3DRender::Render::RenderStateImpl::updateProperties(const
  //      QRenderState *a0)
  void updateProperties(const Qt3DRender::QRenderState *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_RenderStateImplCall1 call = reinterpret_cast<CuteQt3DRender_Render_RenderStateImplCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::RenderStateImpl::updateProperties(a0);
  }
};

//  Qt3DRender::Render::RenderStateImpl::~RenderStateImpl()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15RenderStateImplD1Ev(
    Qt3DRender::Render::RenderStateImpl *self) {
  delete self;
}

//  StateMask Qt3DRender::Render::RenderStateImpl::mask() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateMask ritual_ZNK10Qt3DRender6Render15RenderStateImpl4maskEv(
    const Qt3DRender::Render::RenderStateImpl *self) {
  return self->mask();
}

//  bool Qt3DRender::Render::RenderStateImpl::equalTo(const RenderStateImpl
//      &renderState) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render15RenderStateImpl7equalToERKS1_(
    const Qt3DRender::Render::RenderStateImpl *self,
    const Qt3DRender::Render::RenderStateImpl *renderState) {
  return self->equalTo(*renderState);
}

//  void Qt3DRender::Render::RenderStateImpl::updateProperties(const
//      QRenderState *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15RenderStateImpl16updatePropertiesEPKNS_12QRenderStateE(
    Qt3DRender::Render::RenderStateImpl *self,
    const Qt3DRender::QRenderState *a0) {
  self->updateProperties(a0);
}

//  a Python function taken by a CuteQt3DRender_Render_RenderStateImpl, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_RenderStateImpl(
    Qt3DRender::Render::RenderStateImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_RenderStateImpl *>(self)->take(key, call);
}

//  void Qt3DRender::Render::RenderStateImpl::updateProperties(const
//      QRenderState *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15RenderStateImpl16updatePropertiesEPKNS_12QRenderStateE(
    Qt3DRender::Render::RenderStateImpl *self,
    const Qt3DRender::QRenderState *a0) {
  self->Qt3DRender::Render::RenderStateImpl::updateProperties(a0);
}
