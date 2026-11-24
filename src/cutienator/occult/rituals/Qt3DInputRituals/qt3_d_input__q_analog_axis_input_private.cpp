//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qanalogaxisinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qanalogaxisinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QAnalogAxisInputPrivate that Python can take functions over in. Every Qt3DInput::QAnalogAxisInputPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAnalogAxisInputPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QAnalogAxisInputPrivateCall1)(const void *, int *);
class CuteQt3DInput_QAnalogAxisInputPrivate : public Qt3DInput::QAnalogAxisInputPrivate {
public:
  using Qt3DInput::QAnalogAxisInputPrivate::QAnalogAxisInputPrivate;
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
      CuteQt3DInput_QAnalogAxisInputPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QAnalogAxisInputPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAnalogAxisInputPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QAnalogAxisInputPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QAnalogAxisInputPrivate::QAnalogAxisInputPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAnalogAxisInputPrivate *ritual_ZN9Qt3DInput23QAnalogAxisInputPrivateC1Ev() {
  return new CuteQt3DInput_QAnalogAxisInputPrivate();
}

//  a Python function taken by a CuteQt3DInput_QAnalogAxisInputPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAnalogAxisInputPrivate(
    Qt3DInput::QAnalogAxisInputPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAnalogAxisInputPrivate *>(self)->take(key, call);
}
