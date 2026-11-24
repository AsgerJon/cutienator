//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevice_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qabstractphysicaldevice_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QAbstractPhysicalDevicePrivate that Python can take functions over in. Every Qt3DInput::QAbstractPhysicalDevicePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAbstractPhysicalDevicePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QAbstractPhysicalDevicePrivateCall1)(const void *, int *);
class CuteQt3DInput_QAbstractPhysicalDevicePrivate : public Qt3DInput::QAbstractPhysicalDevicePrivate {
public:
  using Qt3DInput::QAbstractPhysicalDevicePrivate::QAbstractPhysicalDevicePrivate;
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
      CuteQt3DInput_QAbstractPhysicalDevicePrivateCall0 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDevicePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAbstractPhysicalDevicePrivateCall1 call = reinterpret_cast<CuteQt3DInput_QAbstractPhysicalDevicePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QAbstractPhysicalDevice
//      *Qt3DInput::QAbstractPhysicalDevicePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAbstractPhysicalDevice *ritual_ZN9Qt3DInput30QAbstractPhysicalDevicePrivate6q_funcEv(
    Qt3DInput::QAbstractPhysicalDevicePrivate *self) {
  return self->q_func();
}

//  const QAbstractPhysicalDevice
//      *Qt3DInput::QAbstractPhysicalDevicePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAbstractPhysicalDevice *ritual_ZNK9Qt3DInput30QAbstractPhysicalDevicePrivate6q_funcEv(
    const Qt3DInput::QAbstractPhysicalDevicePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DInput_QAbstractPhysicalDevicePrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAbstractPhysicalDevicePrivate(
    Qt3DInput::QAbstractPhysicalDevicePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAbstractPhysicalDevicePrivate *>(self)->take(key, call);
}
