//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/6.12.0/Qt3DInput/private/qaction_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DInput/6.12.0/Qt3DInput/private/qt3dinput_global_p.h>
#include <QtGui/qaction.h>
#include <Qt3DInput/Qt3DInput>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DInput/6.12.0/Qt3DInput/private/qaction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DInput::QActionPrivate that Python can take functions over in. Every Qt3DInput::QActionPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DInput_QActionPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DInput_QActionPrivateCall1)(const void *, int *);
class CuteQt3DInput_QActionPrivate : public Qt3DInput::QActionPrivate {
public:
  using Qt3DInput::QActionPrivate::QActionPrivate;
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
      CuteQt3DInput_QActionPrivateCall0 call = reinterpret_cast<CuteQt3DInput_QActionPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DInput_QActionPrivateCall1 call = reinterpret_cast<CuteQt3DInput_QActionPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DInput::QActionPrivate::QActionPrivate()
extern "C" Q_DECL_EXPORT
Qt3DInput::QActionPrivate *ritual_ZN9Qt3DInput14QActionPrivateC1Ev() {
  return new CuteQt3DInput_QActionPrivate();
}

//  QAction *Qt3DInput::QActionPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DInput::QAction *ritual_ZN9Qt3DInput14QActionPrivate6q_funcEv(
    Qt3DInput::QActionPrivate *self) {
  return self->q_func();
}

//  const QAction *Qt3DInput::QActionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DInput::QAction *ritual_ZNK9Qt3DInput14QActionPrivate6q_funcEv(
    const Qt3DInput::QActionPrivate *self) {
  return self->q_func();
}

//  void Qt3DInput::QActionPrivate::setActive(bool active)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput14QActionPrivate9setActiveEb(
    Qt3DInput::QActionPrivate *self,
    bool active) {
  self->setActive(active);
}

//  a Python function taken by a CuteQt3DInput_QActionPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QActionPrivate(
    Qt3DInput::QActionPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QActionPrivate *>(self)->take(key, call);
}
