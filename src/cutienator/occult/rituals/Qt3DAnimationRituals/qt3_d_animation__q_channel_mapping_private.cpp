//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qchannelmapping_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qchannelmapping_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DAnimation::QChannelMappingPrivate that Python can take functions over in. Every Qt3DAnimation::QChannelMappingPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QChannelMappingPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DAnimation_QChannelMappingPrivateCall1)(const void *, int *);
class CuteQt3DAnimation_QChannelMappingPrivate : public Qt3DAnimation::QChannelMappingPrivate {
public:
  using Qt3DAnimation::QChannelMappingPrivate::QChannelMappingPrivate;
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
      CuteQt3DAnimation_QChannelMappingPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QChannelMappingPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QChannelMappingPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QChannelMapping *Qt3DAnimation::QChannelMappingPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QChannelMapping *ritual_ZN13Qt3DAnimation22QChannelMappingPrivate6q_funcEv(
    Qt3DAnimation::QChannelMappingPrivate *self) {
  return self->q_func();
}

//  const QChannelMapping *Qt3DAnimation::QChannelMappingPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QChannelMapping *ritual_ZNK13Qt3DAnimation22QChannelMappingPrivate6q_funcEv(
    const Qt3DAnimation::QChannelMappingPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DAnimation_QChannelMappingPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QChannelMappingPrivate(
    Qt3DAnimation::QChannelMappingPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QChannelMappingPrivate *>(self)->take(key, call);
}
