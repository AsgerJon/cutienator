//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3draycaster_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3draycaster_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::Quick::Quick3DRayCasterPrivate that Python can take functions over in. Every Qt3DRender::Render::Quick::Quick3DRayCasterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivateCall1)(const void *, int *);
class CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivate : public Qt3DRender::Render::Quick::Quick3DRayCasterPrivate {
public:
  using Qt3DRender::Render::Quick::Quick3DRayCasterPrivate::Quick3DRayCasterPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::Render::Quick::Quick3DRayCasterPrivate::Quick3DRayCasterPriva
//      te()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *ritual_ZN10Qt3DRender6Render5Quick23Quick3DRayCasterPrivateC1Ev() {
  return new CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivate();
}

//  Quick3DRayCaster
//      *Qt3DRender::Render::Quick::Quick3DRayCasterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DRayCaster *ritual_ZN10Qt3DRender6Render5Quick23Quick3DRayCasterPrivate6q_funcEv(
    Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *self) {
  return self->q_func();
}

//  const Quick3DRayCaster
//      *Qt3DRender::Render::Quick::Quick3DRayCasterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Quick::Quick3DRayCaster *ritual_ZNK10Qt3DRender6Render5Quick23Quick3DRayCasterPrivate6q_funcEv(
    const Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Quick3DRayCasterPrivate(
    Qt3DRender::Render::Quick::Quick3DRayCasterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Quick3DRayCasterPrivate *>(self)->take(key, call);
}
