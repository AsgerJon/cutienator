//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dparameter_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/qt3dquickrender_global_p.h>
#include <Qt3DQuickRender/Qt3DQuickRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickRender/6.12.0/Qt3DQuickRender/private/quick3dparameter_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <cstring>

//  A Qt3DRender::Render::Quick::Quick3DParameterPrivate that Python can take functions over in. Every Qt3DRender::Render::Quick::Quick3DParameterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall0)(const void *, const QVariant *, int *);
typedef void (*CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall2)(const void *, int *);
class CuteQt3DRender_Render_Quick_Quick3DParameterPrivate : public Qt3DRender::Render::Quick::Quick3DParameterPrivate {
public:
  using Qt3DRender::Render::Quick::Quick3DParameterPrivate::Quick3DParameterPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender17QParameterPrivate8setValueERK8QVariant")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void
  //      Qt3DRender::Render::Quick::Quick3DParameterPrivate::setValue(cons
  //      t QVariant &value)
  void setValue(const QVariant &value) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall0>(taken[0]);
      call(this, &value, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Quick::Quick3DParameterPrivate::setValue(value);
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall2 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Quick3DParameterPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Quick3DParameter
//      *Qt3DRender::Render::Quick::Quick3DParameterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Quick3DParameter *ritual_ZN10Qt3DRender6Render5Quick23Quick3DParameterPrivate6q_funcEv(
    Qt3DRender::Render::Quick::Quick3DParameterPrivate *self) {
  return self->q_func();
}

//  const Quick3DParameter
//      *Qt3DRender::Render::Quick::Quick3DParameterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Render::Quick::Quick3DParameter *ritual_ZNK10Qt3DRender6Render5Quick23Quick3DParameterPrivate6q_funcEv(
    const Qt3DRender::Render::Quick::Quick3DParameterPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DRender_Render_Quick_Quick3DParameterPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Quick3DParameterPrivate(
    Qt3DRender::Render::Quick::Quick3DParameterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Quick3DParameterPrivate *>(self)->take(key, call);
}
