//  Written by hand on 2026-11-25 from
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dscreenraycaster_p_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  The header of Quick3DScreenRayCaster is included as well: 'q_func'
//  casts to it, and the private header only declares it.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dscreenraycaster_p.h>
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dscreenraycaster_p_p.h>
#include <cstring>

//  A Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate that Python can take functions over in. Every Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivateCall1)(const void *, int *);
class CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivate : public Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate {
public:
  using Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate::Quick3DScreenRayCasterPrivate;
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
      CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate::Quick3DScreenRayCasterPriva
//      te()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate *ritual_ZN10Qt3DRender6Render5Quick29Quick3DScreenRayCasterPrivateC1Ev() {
  return new CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivate();
}

//  Quick3DScreenRayCaster
//      *Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DScreenRayCaster *ritual_ZN10Qt3DRender6Render5Quick29Quick3DScreenRayCasterPrivate6q_funcEv(
    Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate *self) {
  return self->q_func();
}

//  const Quick3DScreenRayCaster
//      *Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Quick::Quick3DScreenRayCaster *ritual_ZNK10Qt3DRender6Render5Quick29Quick3DScreenRayCasterPrivate6q_funcEv(
    const Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Quick3DScreenRayCasterPrivate(
    Qt3DRender::Render::Quick::Quick3DScreenRayCasterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Quick3DScreenRayCasterPrivate *>(self)->take(key, call);
}
