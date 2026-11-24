//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qpervertexcolormaterial_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qpervertexcolormaterial_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DExtras::QPerVertexColorMaterialPrivate that Python can take functions over in. Every Qt3DExtras::QPerVertexColorMaterialPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QPerVertexColorMaterialPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QPerVertexColorMaterialPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QPerVertexColorMaterialPrivate : public Qt3DExtras::QPerVertexColorMaterialPrivate {
public:
  using Qt3DExtras::QPerVertexColorMaterialPrivate::QPerVertexColorMaterialPrivate;
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
      CuteQt3DExtras_QPerVertexColorMaterialPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QPerVertexColorMaterialPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QPerVertexColorMaterialPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QPerVertexColorMaterialPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QPerVertexColorMaterial
//      *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QPerVertexColorMaterial *ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivate6q_funcEv(
    Qt3DExtras::QPerVertexColorMaterialPrivate *self) {
  return self->q_func();
}

//  const QPerVertexColorMaterial
//      *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QPerVertexColorMaterial *ritual_ZNK10Qt3DExtras30QPerVertexColorMaterialPrivate6q_funcEv(
    const Qt3DExtras::QPerVertexColorMaterialPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_QPerVertexColorMaterialPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QPerVertexColorMaterialPrivate(
    Qt3DExtras::QPerVertexColorMaterialPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QPerVertexColorMaterialPrivate *>(self)->take(key, call);
}
