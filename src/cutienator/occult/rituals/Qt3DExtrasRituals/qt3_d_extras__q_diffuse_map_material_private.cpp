//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusemapmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qdiffusemapmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DExtras::QDiffuseMapMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QDiffuseMapMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QDiffuseMapMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QDiffuseMapMaterialPrivate : public Qt3DExtras::QDiffuseMapMaterialPrivate {
public:
  using Qt3DExtras::QDiffuseMapMaterialPrivate::QDiffuseMapMaterialPrivate;
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
      CuteQt3DExtras_QDiffuseMapMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QDiffuseMapMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QDiffuseMapMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QDiffuseMapMaterial *Qt3DExtras::QDiffuseMapMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QDiffuseMapMaterial *ritual_ZN10Qt3DExtras26QDiffuseMapMaterialPrivate6q_funcEv(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self) {
  return self->q_func();
}

//  const QDiffuseMapMaterial
//      *Qt3DExtras::QDiffuseMapMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QDiffuseMapMaterial *ritual_ZNK10Qt3DExtras26QDiffuseMapMaterialPrivate6q_funcEv(
    const Qt3DExtras::QDiffuseMapMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QDiffuseMapMaterialPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QDiffuseMapMaterialPrivate(
    Qt3DExtras::QDiffuseMapMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QDiffuseMapMaterialPrivate *>(self)->take(key, call);
}
