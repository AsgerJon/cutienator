//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/renderstates_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/renderstates_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::ScissorTest that Python can take functions over in. Every Qt3DRender::Render::ScissorTest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_ScissorTestCall0)(const void *, const Qt3DRender::QRenderState *, int *);
class CuteQt3DRender_Render_ScissorTest : public Qt3DRender::Render::ScissorTest {
public:
  using Qt3DRender::Render::ScissorTest::ScissorTest;
  CuteQt3DRender_Render_ScissorTest(const Qt3DRender::Render::ScissorTest & other) : Qt3DRender::Render::ScissorTest(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render11ScissorTest16updatePropertiesEPKNS_12QRenderStateE")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::ScissorTest::updateProperties(const
  //      QRenderState *node)
  void updateProperties(const Qt3DRender::QRenderState *node) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_ScissorTestCall0 call = reinterpret_cast<CuteQt3DRender_Render_ScissorTestCall0>(taken[0]);
      call(this, node, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::ScissorTest::updateProperties(node);
  }
};

//  void Qt3DRender::Render::ScissorTest::updateProperties(const QRenderState
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11ScissorTest16updatePropertiesEPKNS_12QRenderStateE(
    Qt3DRender::Render::ScissorTest *self,
    const Qt3DRender::QRenderState *node) {
  self->updateProperties(node);
}

//  Qt3DRender::Render::ScissorTest::~ScissorTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11ScissorTestD1Ev(
    Qt3DRender::Render::ScissorTest *self) {
  delete self;
}

//  a Python function taken by a CuteQt3DRender_Render_ScissorTest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_ScissorTest(
    Qt3DRender::Render::ScissorTest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_ScissorTest *>(self)->take(key, call);
}

//  void Qt3DRender::Render::ScissorTest::updateProperties(const QRenderState
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render11ScissorTest16updatePropertiesEPKNS_12QRenderStateE(
    Qt3DRender::Render::ScissorTest *self,
    const Qt3DRender::QRenderState *node) {
  self->Qt3DRender::Render::ScissorTest::updateProperties(node);
}
