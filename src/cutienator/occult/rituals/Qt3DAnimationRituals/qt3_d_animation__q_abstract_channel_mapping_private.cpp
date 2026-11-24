//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractchannelmapping_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qabstractchannelmapping_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DAnimation::QAbstractChannelMappingPrivate that Python can take functions over in. Every Qt3DAnimation::QAbstractChannelMappingPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_QAbstractChannelMappingPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DAnimation_QAbstractChannelMappingPrivateCall1)(const void *, int *);
class CuteQt3DAnimation_QAbstractChannelMappingPrivate : public Qt3DAnimation::QAbstractChannelMappingPrivate {
public:
  using Qt3DAnimation::QAbstractChannelMappingPrivate::QAbstractChannelMappingPrivate;
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
      CuteQt3DAnimation_QAbstractChannelMappingPrivateCall0 call = reinterpret_cast<CuteQt3DAnimation_QAbstractChannelMappingPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_QAbstractChannelMappingPrivateCall1 call = reinterpret_cast<CuteQt3DAnimation_QAbstractChannelMappingPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QAbstractChannelMapping
//      *Qt3DAnimation::QAbstractChannelMappingPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DAnimation::QAbstractChannelMapping *ritual_ZN13Qt3DAnimation30QAbstractChannelMappingPrivate6q_funcEv(
    Qt3DAnimation::QAbstractChannelMappingPrivate *self) {
  return self->q_func();
}

//  const QAbstractChannelMapping
//      *Qt3DAnimation::QAbstractChannelMappingPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DAnimation::QAbstractChannelMapping *ritual_ZNK13Qt3DAnimation30QAbstractChannelMappingPrivate6q_funcEv(
    const Qt3DAnimation::QAbstractChannelMappingPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DAnimation_QAbstractChannelMappingPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_QAbstractChannelMappingPrivate(
    Qt3DAnimation::QAbstractChannelMappingPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_QAbstractChannelMappingPrivate *>(self)->take(key, call);
}
