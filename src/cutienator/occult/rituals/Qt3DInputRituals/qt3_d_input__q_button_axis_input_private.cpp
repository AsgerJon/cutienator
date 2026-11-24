//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qbuttonaxisinput_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qbuttonaxisinput_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QButtonAxisInputPrivate that Python can take functions over in. Every Qt3DInput::QButtonAxisInputPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QButtonAxisInputPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QButtonAxisInputPrivateCall1)(const void *, int *);
class CuteQt3DInput_QButtonAxisInputPrivate : public Qt3DInput::QButtonAxisInputPrivate {
public:
  using Qt3DInput::QButtonAxisInputPrivate::QButtonAxisInputPrivate;
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
      CuteQt3DInput_QButtonAxisInputPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QButtonAxisInputPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QButtonAxisInputPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QButtonAxisInputPrivate::QButtonAxisInputPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QButtonAxisInputPrivate *ritual_ZN9Qt3DInput23QButtonAxisInputPrivateC1Ev() {
  return new CuteQt3DInput_QButtonAxisInputPrivate();
}

//  a Python function taken by a CuteQt3DInput_QButtonAxisInputPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QButtonAxisInputPrivate(
    Qt3DInput::QButtonAxisInputPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QButtonAxisInputPrivate *>(self)->take(key, call);
}
