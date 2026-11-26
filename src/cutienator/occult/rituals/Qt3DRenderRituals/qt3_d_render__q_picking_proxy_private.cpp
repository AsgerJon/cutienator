//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qpickingproxy_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qpickingproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QPickingProxyPrivate that Python can take functions over in. Every Qt3DRender::QPickingProxyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QPickingProxyPrivateCall0)(const void *, Qt3DCore::QGeometryView *, int *);
typedef void (*CuteQt3DRender_QPickingProxyPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QPickingProxyPrivateCall2)(const void *, int *);
class CuteQt3DRender_QPickingProxyPrivate : public Qt3DRender::QPickingProxyPrivate {
public:
  using Qt3DRender::QPickingProxyPrivate::QPickingProxyPrivate;
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
  //      Qt3DRender::QPickingProxyPrivate::setView(Qt3DCore::QGeometryView
  //      *view)
  void setView(Qt3DCore::QGeometryView *view) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QPickingProxyPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QPickingProxyPrivateCall0>(taken[0]);
      call(this, view, &handled);
      if (handled) return;
    }
    Qt3DRender::QPickingProxyPrivate::setView(view);
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QPickingProxyPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QPickingProxyPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QPickingProxyPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QPickingProxyPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QPickingProxyPrivate::QPickingProxyPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickingProxyPrivate *ritual_ZN10Qt3DRender20QPickingProxyPrivateC1Ev() {
  return new CuteQt3DRender_QPickingProxyPrivate();
}

//  Qt3DRender::QPickingProxyPrivate::~QPickingProxyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QPickingProxyPrivateD1Ev(
    Qt3DRender::QPickingProxyPrivate *self) {
  delete self;
}

//  QPickingProxy *Qt3DRender::QPickingProxyPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickingProxy *ritual_ZN10Qt3DRender20QPickingProxyPrivate6q_funcEv(
    Qt3DRender::QPickingProxyPrivate *self) {
  return self->q_func();
}

//  const QPickingProxy *Qt3DRender::QPickingProxyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QPickingProxy *ritual_ZNK10Qt3DRender20QPickingProxyPrivate6q_funcEv(
    const Qt3DRender::QPickingProxyPrivate *self) {
  return self->q_func();
}

//  void Qt3DRender::QPickingProxyPrivate::setView(Qt3DCore::QGeometryView
//      *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender20QPickingProxyPrivate7setViewEPN8Qt3DCore13QGeometryViewE(
    Qt3DRender::QPickingProxyPrivate *self,
    Qt3DCore::QGeometryView *view) {
  self->setView(view);
}

//  a Python function taken by a CuteQt3DRender_QPickingProxyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPickingProxyPrivate(
    Qt3DRender::QPickingProxyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPickingProxyPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QPickingProxyPrivate::setView(Qt3DCore::QGeometryView
//      *view)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender20QPickingProxyPrivate7setViewEPN8Qt3DCore13QGeometryViewE(
    Qt3DRender::QPickingProxyPrivate *self,
    Qt3DCore::QGeometryView *view) {
  self->Qt3DRender::QPickingProxyPrivate::setView(view);
}
