//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qlevelofdetailswitch_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qlevelofdetailswitch_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QLevelOfDetailSwitchPrivate that Python can take functions over in. Every Qt3DRender::QLevelOfDetailSwitchPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QLevelOfDetailSwitchPrivateCall0)(const void *, int, int *);
typedef void (*CuteQt3DRender_QLevelOfDetailSwitchPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QLevelOfDetailSwitchPrivateCall2)(const void *, int *);
class CuteQt3DRender_QLevelOfDetailSwitchPrivate : public Qt3DRender::QLevelOfDetailSwitchPrivate {
public:
  using Qt3DRender::QLevelOfDetailSwitchPrivate::QLevelOfDetailSwitchPrivate;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender21QLevelOfDetailPrivate15setCurrentIndexEi")) {
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

  //  void Qt3DRender::QLevelOfDetailSwitchPrivate::setCurrentIndex(int
  //      currentIndex)
  void setCurrentIndex(int currentIndex) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QLevelOfDetailSwitchPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailSwitchPrivateCall0>(taken[0]);
      call(this, currentIndex, &handled);
      if (handled) return;
    }
    Qt3DRender::QLevelOfDetailSwitchPrivate::setCurrentIndex(currentIndex);
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QLevelOfDetailSwitchPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailSwitchPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QLevelOfDetailSwitchPrivateCall2 call = reinterpret_cast<CuteQt3DRender_QLevelOfDetailSwitchPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QLevelOfDetailSwitch *Qt3DRender::QLevelOfDetailSwitchPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QLevelOfDetailSwitch *ritual_ZN10Qt3DRender27QLevelOfDetailSwitchPrivate6q_funcEv(
    Qt3DRender::QLevelOfDetailSwitchPrivate *self) {
  return self->q_func();
}

//  const QLevelOfDetailSwitch
//      *Qt3DRender::QLevelOfDetailSwitchPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QLevelOfDetailSwitch *ritual_ZNK10Qt3DRender27QLevelOfDetailSwitchPrivate6q_funcEv(
    const Qt3DRender::QLevelOfDetailSwitchPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QLevelOfDetailSwitchPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QLevelOfDetailSwitchPrivate(
    Qt3DRender::QLevelOfDetailSwitchPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QLevelOfDetailSwitchPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QLevelOfDetailSwitchPrivate::setCurrentIndex(int
//      currentIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender27QLevelOfDetailSwitchPrivate15setCurrentIndexEi(
    Qt3DRender::QLevelOfDetailSwitchPrivate *self,
    int currentIndex) {
  self->Qt3DRender::QLevelOfDetailSwitchPrivate::setCurrentIndex(
      currentIndex);
}
