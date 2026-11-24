//  Written by dev_tooling.RitualGenerator from the records of Qt3DExtras/6.1
//  2.0/Qt3DExtras/private/qnormaldiffusespecularmapmaterial_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qnormaldiffusespecularmapmaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate : public Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate {
public:
  using Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::QNormalDiffuseSpecularMapMaterialPrivate;
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
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QNormalDiffuseSpecularMapMaterial
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QNormalDiffuseSpecularMapMaterial *ritual_ZN10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate6q_funcEv(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self) {
  return self->q_func();
}

//  const QNormalDiffuseSpecularMapMaterial
//      *Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QNormalDiffuseSpecularMapMaterial *ritual_ZNK10Qt3DExtras40QNormalDiffuseSpecularMapMaterialPrivate6q_funcEv(
    const Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate(
    Qt3DExtras::QNormalDiffuseSpecularMapMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QNormalDiffuseSpecularMapMaterialPrivate *>(self)->take(key, call);
}
