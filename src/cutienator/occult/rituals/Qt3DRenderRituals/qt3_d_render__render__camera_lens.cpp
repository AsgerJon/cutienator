//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/cameralens_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: Qt's 'Matrix4x4' is the SSE class
//  Qt3DCore::Matrix4x4_SSE where __SSE2__ is defined and QMatrix4x4
//  elsewhere (the compiler refused a QMatrix4x4 made from the SSE
//  class); the ritual hands the alias 'Matrix4x4', as Qt writes it, so
//  that it is right for both. Kept as it is when the generator runs
//  again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/cameralens_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qmatrix4x4.h>
#include <cstring>

//  A Qt3DRender::Render::CameraLens that Python can take functions over in. Every Qt3DRender::Render::CameraLens
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_CameraLensCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_CameraLens : public Qt3DRender::Render::CameraLens {
public:
  using Qt3DRender::Render::CameraLens::CameraLens;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::CameraLens::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_CameraLensCall0 call = reinterpret_cast<CuteQt3DRender_Render_CameraLensCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::CameraLens::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Matrix4x4 Qt3DRender::Render::CameraLens::projection() const
extern "C" Q_DECL_EXPORT
Matrix4x4 *ritual_ZNK10Qt3DRender6Render10CameraLens10projectionEv(
    const Qt3DRender::Render::CameraLens *self) {
  return new Matrix4x4(self->projection());
}

//  float Qt3DRender::Render::CameraLens::exposure() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render10CameraLens8exposureEv(
    const Qt3DRender::Render::CameraLens *self) {
  return self->exposure();
}

//  a Python function taken by a CuteQt3DRender_Render_CameraLens, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_CameraLens(
    Qt3DRender::Render::CameraLens *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_CameraLens *>(self)->take(key, call);
}

//  void Qt3DRender::Render::CameraLens::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render10CameraLens16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::CameraLens *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::CameraLens::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
