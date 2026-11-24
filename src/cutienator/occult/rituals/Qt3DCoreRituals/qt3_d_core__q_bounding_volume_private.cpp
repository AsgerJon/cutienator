//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qboundingvolume_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qboundingvolume_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QBoundingVolumePrivate that Python can take functions over in. Every Qt3DCore::QBoundingVolumePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QBoundingVolumePrivateCall0)(const void *, Qt3DCore::QGeometryView *, int *);
typedef void (*CuteQt3DCore_QBoundingVolumePrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DCore_QBoundingVolumePrivateCall2)(const void *, int *);
class CuteQt3DCore_QBoundingVolumePrivate : public Qt3DCore::QBoundingVolumePrivate {
public:
  using Qt3DCore::QBoundingVolumePrivate::QBoundingVolumePrivate;
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

  //  void Qt3DCore::QBoundingVolumePrivate::setView(QGeometryView *view)
  void setView(Qt3DCore::QGeometryView *view) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QBoundingVolumePrivateCall0 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumePrivateCall0>(taken[0]);
      call(this, view, &handled);
      if (handled) return;
    }
    Qt3DCore::QBoundingVolumePrivate::setView(view);
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QBoundingVolumePrivateCall1 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumePrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DCore_QBoundingVolumePrivateCall2 call = reinterpret_cast<CuteQt3DCore_QBoundingVolumePrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QBoundingVolume *Qt3DCore::QBoundingVolumePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QBoundingVolume *ritual_ZN8Qt3DCore22QBoundingVolumePrivate6q_funcEv(
    Qt3DCore::QBoundingVolumePrivate *self) {
  return self->q_func();
}

//  const QBoundingVolume *Qt3DCore::QBoundingVolumePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QBoundingVolume *ritual_ZNK8Qt3DCore22QBoundingVolumePrivate6q_funcEv(
    const Qt3DCore::QBoundingVolumePrivate *self) {
  return self->q_func();
}

//  void Qt3DCore::QBoundingVolumePrivate::setView(QGeometryView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGeometryViewE(
    Qt3DCore::QBoundingVolumePrivate *self,
    Qt3DCore::QGeometryView *view) {
  self->setView(view);
}

//  a Python function taken by a CuteQt3DCore_QBoundingVolumePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QBoundingVolumePrivate(
    Qt3DCore::QBoundingVolumePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QBoundingVolumePrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QBoundingVolumePrivate::setView(QGeometryView *view)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore22QBoundingVolumePrivate7setViewEPNS_13QGeometryViewE(
    Qt3DCore::QBoundingVolumePrivate *self,
    Qt3DCore::QGeometryView *view) {
  self->Qt3DCore::QBoundingVolumePrivate::setView(view);
}
