//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qattribute_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qattribute_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QAttributePrivate that Python can take functions over in. Every Qt3DCore::QAttributePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QAttributePrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QAttributePrivateCall1)(const void *, Qt3DCore::QScene *, int *);
class CuteQt3DCore_QAttributePrivate : public Qt3DCore::QAttributePrivate {
public:
  using Qt3DCore::QAttributePrivate::QAttributePrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QAttributePrivate::update()
  void update() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QAttributePrivateCall0 call = reinterpret_cast<CuteQt3DCore_QAttributePrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QAttributePrivate::update();
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QAttributePrivateCall1 call = reinterpret_cast<CuteQt3DCore_QAttributePrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }
};

//  QAttribute *Qt3DCore::QAttributePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttribute *ritual_ZN8Qt3DCore17QAttributePrivate6q_funcEv(
    Qt3DCore::QAttributePrivate *self) {
  return self->q_func();
}

//  const QAttribute *Qt3DCore::QAttributePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QAttribute *ritual_ZNK8Qt3DCore17QAttributePrivate6q_funcEv(
    const Qt3DCore::QAttributePrivate *self) {
  return self->q_func();
}

//  Qt3DCore::QAttributePrivate::QAttributePrivate()
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttributePrivate *ritual_ZN8Qt3DCore17QAttributePrivateC1Ev() {
  return new CuteQt3DCore_QAttributePrivate();
}

//  void Qt3DCore::QAttributePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore17QAttributePrivate6updateEv(
    Qt3DCore::QAttributePrivate *self) {
  self->update();
}

//  QAttributePrivate *Qt3DCore::QAttributePrivate::get(QAttribute *q)
extern "C" Q_DECL_EXPORT
Qt3DCore::QAttributePrivate *ritual_ZN8Qt3DCore17QAttributePrivate3getEPNS_10QAttributeE(
    Qt3DCore::QAttribute *q) {
  return Qt3DCore::QAttributePrivate::get(q);
}

//  a Python function taken by a CuteQt3DCore_QAttributePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QAttributePrivate(
    Qt3DCore::QAttributePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QAttributePrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QAttributePrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore17QAttributePrivate6updateEv(
    Qt3DCore::QAttributePrivate *self) {
  self->Qt3DCore::QAttributePrivate::update();
}
