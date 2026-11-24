//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DCore/6.12.0/Qt3DCore/private/qtransform_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <Qt3DCore/6.12.0/Qt3DCore/private/qt3dcore_global_p.h>
#include <QtGui/qtransform.h>
#include <Qt3DCore/Qt3DCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/6.12.0/Qt3DCore/private/qtransform_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DCore::QTransformPrivate that Python can take functions over in. Every Qt3DCore::QTransformPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DCore_QTransformPrivateCall0)(const void *, int *);
typedef void (*CuteQt3DCore_QTransformPrivateCall1)(const void *, Qt3DCore::QScene *, int *);
class CuteQt3DCore_QTransformPrivate : public Qt3DCore::QTransformPrivate {
public:
  using Qt3DCore::QTransformPrivate::QTransformPrivate;
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

  //  void Qt3DCore::QTransformPrivate::update()
  void update() override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DCore_QTransformPrivateCall0 call = reinterpret_cast<CuteQt3DCore_QTransformPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QTransformPrivate::update();
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DCore_QTransformPrivateCall1 call = reinterpret_cast<CuteQt3DCore_QTransformPrivateCall1>(taken[1]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }
};

//  QTransform *Qt3DCore::QTransformPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DCore::QTransform *ritual_ZN8Qt3DCore17QTransformPrivate6q_funcEv(
    Qt3DCore::QTransformPrivate *self) {
  return self->q_func();
}

//  const QTransform *Qt3DCore::QTransformPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DCore::QTransform *ritual_ZNK8Qt3DCore17QTransformPrivate6q_funcEv(
    const Qt3DCore::QTransformPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DCore_QTransformPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DCore_QTransformPrivate(
    Qt3DCore::QTransformPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DCore_QTransformPrivate *>(self)->take(key, call);
}

//  void Qt3DCore::QTransformPrivate::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN8Qt3DCore17QTransformPrivate6updateEv(
    Qt3DCore::QTransformPrivate *self) {
  self->Qt3DCore::QTransformPrivate::update();
}
