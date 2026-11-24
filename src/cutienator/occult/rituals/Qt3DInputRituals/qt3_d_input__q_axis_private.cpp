//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qaxis_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qaxis_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QAxisPrivate that Python can take functions over in. Every Qt3DInput::QAxisPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QAxisPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QAxisPrivateCall1)(const void *, int *);
class CuteQt3DInput_QAxisPrivate : public Qt3DInput::QAxisPrivate {
public:
  using Qt3DInput::QAxisPrivate::QAxisPrivate;
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
      CuteQt3DInput_QAxisPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QAxisPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QAxisPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QAxisPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QAxisPrivate::QAxisPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxisPrivate *ritual_ZN9Qt3DInput12QAxisPrivateC1Ev() {
  return new CuteQt3DInput_QAxisPrivate();
}

//  QAxis *Qt3DInput::QAxisPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAxis *ritual_ZN9Qt3DInput12QAxisPrivate6q_funcEv(
    Qt3DInput::QAxisPrivate *self) {
  return self->q_func();
}

//  const QAxis *Qt3DInput::QAxisPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAxis *ritual_ZNK9Qt3DInput12QAxisPrivate6q_funcEv(
    const Qt3DInput::QAxisPrivate *self) {
  return self->q_func();
}

//  void Qt3DInput::QAxisPrivate::setValue(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput12QAxisPrivate8setValueEf(
    Qt3DInput::QAxisPrivate *self,
    float value) {
  self->setValue(value);
}

//  a Python function taken by a CuteQt3DInput_QAxisPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QAxisPrivate(
    Qt3DInput::QAxisPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QAxisPrivate *>(self)->take(key, call);
}
