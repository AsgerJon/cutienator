//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qsceneloader_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qsceneloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::QSceneLoaderPrivate that Python can take functions over in. Every Qt3DRender::QSceneLoaderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QSceneLoaderPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QSceneLoaderPrivateCall1)(const void *, int *);
class CuteQt3DRender_QSceneLoaderPrivate : public Qt3DRender::QSceneLoaderPrivate {
public:
  using Qt3DRender::QSceneLoaderPrivate::QSceneLoaderPrivate;
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
      CuteQt3DRender_QSceneLoaderPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QSceneLoaderPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QSceneLoaderPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QSceneLoaderPrivate::QSceneLoaderPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneLoaderPrivate *ritual_ZN10Qt3DRender19QSceneLoaderPrivateC1Ev() {
  return new CuteQt3DRender_QSceneLoaderPrivate();
}

//  void Qt3DRender::QSceneLoaderPrivate::setStatus(QSceneLoader::Status
//      status)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QSceneLoaderPrivate9setStatusENS_12QSceneLoader6StatusE(
    Qt3DRender::QSceneLoaderPrivate *self,
    Qt3DRender::QSceneLoader::Status status) {
  self->setStatus(status);
}

//  void Qt3DRender::QSceneLoaderPrivate::setSceneRoot(Qt3DCore::QEntity
//      *root)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QSceneLoaderPrivate12setSceneRootEPN8Qt3DCore7QEntityE(
    Qt3DRender::QSceneLoaderPrivate *self,
    Qt3DCore::QEntity *root) {
  self->setSceneRoot(root);
}

//  QSceneLoader *Qt3DRender::QSceneLoaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSceneLoader *ritual_ZN10Qt3DRender19QSceneLoaderPrivate6q_funcEv(
    Qt3DRender::QSceneLoaderPrivate *self) {
  return self->q_func();
}

//  const QSceneLoader *Qt3DRender::QSceneLoaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QSceneLoader *ritual_ZNK10Qt3DRender19QSceneLoaderPrivate6q_funcEv(
    const Qt3DRender::QSceneLoaderPrivate *self) {
  return self->q_func();
}

//  void Qt3DRender::QSceneLoaderPrivate::populateEntityMap(Qt3DCore::QEntity
//      *parentEntity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QSceneLoaderPrivate17populateEntityMapEPN8Qt3DCore7QEntityE(
    Qt3DRender::QSceneLoaderPrivate *self,
    Qt3DCore::QEntity *parentEntity) {
  self->populateEntityMap(parentEntity);
}

//  a Python function taken by a CuteQt3DRender_QSceneLoaderPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QSceneLoaderPrivate(
    Qt3DRender::QSceneLoaderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QSceneLoaderPrivate *>(self)->take(key, call);
}
