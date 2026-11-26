//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qgeometryrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qgeometryrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QGeometryRendererPrivate that Python can take functions over in. Every Qt3DRender::QGeometryRendererPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QGeometryRendererPrivateCall0)(const void *, Qt3DCore::QGeometryView *, int *);
typedef void (*CuteQt3DRender_QGeometryRendererPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QGeometryRendererPrivateCall2)(const void *, int *);
class CuteQt3DRender_QGeometryRendererPrivate : public Qt3DRender::QGeometryRendererPrivate {
public:
  using Qt3DRender::QGeometryRendererPrivate::QGeometryRendererPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGeometryViewE")) {
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
  //      Qt3DRender::QGeometryRendererPrivate::setView(Qt3DCore::QGeometry
  //      View *view)
  void setView(Qt3DCore::QGeometryView *view) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QGeometryRendererPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererPrivateCall0>(taken[0]);
      call(this, view, &handled);
      if (handled) return;
    }
    Qt3DRender::QGeometryRendererPrivate::setView(view);
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QGeometryRendererPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QGeometryRendererPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QGeometryRendererPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QGeometryRendererPrivate::QGeometryRendererPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRendererPrivate *ritual_ZN10Qt3DRender24QGeometryRendererPrivateC1Ev() {
  return new CuteQt3DRender_QGeometryRendererPrivate();
}

//  Qt3DRender::QGeometryRendererPrivate::~QGeometryRendererPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender24QGeometryRendererPrivateD1Ev(
    Qt3DRender::QGeometryRendererPrivate *self) {
  delete self;
}

//  QGeometryRenderer *Qt3DRender::QGeometryRendererPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer *ritual_ZN10Qt3DRender24QGeometryRendererPrivate6q_funcEv(
    Qt3DRender::QGeometryRendererPrivate *self) {
  return self->q_func();
}

//  const QGeometryRenderer *Qt3DRender::QGeometryRendererPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QGeometryRenderer *ritual_ZNK10Qt3DRender24QGeometryRendererPrivate6q_funcEv(
    const Qt3DRender::QGeometryRendererPrivate *self) {
  return self->q_func();
}

//  void
//      Qt3DRender::QGeometryRendererPrivate::setView(Qt3DCore::QGeometryView
//      *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender24QGeometryRendererPrivate7setViewEPN8Qt3DCore13QGeometryViewE(
    Qt3DRender::QGeometryRendererPrivate *self,
    Qt3DCore::QGeometryView *view) {
  self->setView(view);
}

//  a Python function taken by a CuteQt3DRender_QGeometryRendererPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QGeometryRendererPrivate(
    Qt3DRender::QGeometryRendererPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QGeometryRendererPrivate *>(self)->take(key, call);
}

//  void
//      Qt3DRender::QGeometryRendererPrivate::setView(Qt3DCore::QGeometryView
//      *view)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender24QGeometryRendererPrivate7setViewEPN8Qt3DCore13QGeometryViewE(
    Qt3DRender::QGeometryRendererPrivate *self,
    Qt3DCore::QGeometryView *view) {
  self->Qt3DRender::QGeometryRendererPrivate::setView(view);
}
