//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  sceneeffects_p.h, Qt 6.12.0, from Qt's source. Kept as it is when
//  the generator runs again.
//  MainSceneEffect is not exported by Qt (no Q_..._EXPORT on its class
//  line), so only its virtual functions are called, through the
//  object: metaObject(), the implicit destructor (virtual through
//  QObject) and the two private overrides registerWithEnv and
//  unregisterWithEnv.
//  Not written: the constructor.
#include <QtQuick3D/qtquick3dglobal.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/sceneeffects_p.h>

//  const QMetaObject *MainSceneEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15MainSceneEffect10metaObjectEv(
    const MainSceneEffect *self) {
  return self->metaObject();
}

//  MainSceneEffect::~MainSceneEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN15MainSceneEffectD1Ev(MainSceneEffect *self) {
  delete self;
}

//  void MainSceneEffect::registerWithEnv(SceneEffectEnvironment
//      *newEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15MainSceneEffect15registerWithEnvEP22SceneEffectEnvironment(
    MainSceneEffect *self,
    SceneEffectEnvironment *newEnvironment) {
  self->registerWithEnv(newEnvironment);
}

//  void MainSceneEffect::unregisterWithEnv(SceneEffectEnvironment
//      *oldEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15MainSceneEffect17unregisterWithEnvEP22SceneEffectEnvironment(
    MainSceneEffect *self,
    SceneEffectEnvironment *oldEnvironment) {
  self->unregisterWithEnv(oldEnvironment);
}
