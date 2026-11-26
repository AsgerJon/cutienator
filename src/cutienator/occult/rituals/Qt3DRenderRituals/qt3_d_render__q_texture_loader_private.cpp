//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qtexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QTextureLoaderPrivate that Python can take functions over in. Every Qt3DRender::QTextureLoaderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QTextureLoaderPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QTextureLoaderPrivateCall1)(const void *, int *);
class CuteQt3DRender_QTextureLoaderPrivate : public Qt3DRender::QTextureLoaderPrivate {
public:
  using Qt3DRender::QTextureLoaderPrivate::QTextureLoaderPrivate;
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

  //  void Qt3DRender::QTextureLoaderPrivate::setScene(Qt3DCore::QScene
  //      *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QTextureLoaderPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QTextureLoaderPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DRender::QTextureLoaderPrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QTextureLoaderPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QTextureLoaderPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QTextureLoaderPrivate::QTextureLoaderPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureLoaderPrivate *ritual_ZN10Qt3DRender21QTextureLoaderPrivateC1Ev() {
  return new CuteQt3DRender_QTextureLoaderPrivate();
}

//  QTextureLoader *Qt3DRender::QTextureLoaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QTextureLoader *ritual_ZN10Qt3DRender21QTextureLoaderPrivate6q_funcEv(
    Qt3DRender::QTextureLoaderPrivate *self) {
  return self->q_func();
}

//  const QTextureLoader *Qt3DRender::QTextureLoaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QTextureLoader *ritual_ZNK10Qt3DRender21QTextureLoaderPrivate6q_funcEv(
    const Qt3DRender::QTextureLoaderPrivate *self) {
  return self->q_func();
}

//  void Qt3DRender::QTextureLoaderPrivate::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QTextureLoaderPrivate8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DRender::QTextureLoaderPrivate *self,
    Qt3DCore::QScene *scene) {
  self->setScene(scene);
}

//  void Qt3DRender::QTextureLoaderPrivate::updateGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender21QTextureLoaderPrivate15updateGeneratorEv(
    Qt3DRender::QTextureLoaderPrivate *self) {
  self->updateGenerator();
}

//  a Python function taken by a CuteQt3DRender_QTextureLoaderPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QTextureLoaderPrivate(
    Qt3DRender::QTextureLoaderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QTextureLoaderPrivate *>(self)->take(key, call);
}

//  void Qt3DRender::QTextureLoaderPrivate::setScene(Qt3DCore::QScene *scene)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender21QTextureLoaderPrivate8setSceneEPN8Qt3DCore6QSceneE(
    Qt3DRender::QTextureLoaderPrivate *self,
    Qt3DCore::QScene *scene) {
  self->Qt3DRender::QTextureLoaderPrivate::setScene(scene);
}
