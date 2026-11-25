//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  sceneeffects_p.h, Qt 6.12.0, from Qt's source. Kept as it is when
//  the generator runs again.
//  SceneEffectBase is not exported by Qt (no Q_..._EXPORT on its class
//  line), so only its virtual functions are called, through the
//  object: metaObject(), the implicit destructor (virtual through
//  QObject) and the two private pure virtual functions
//  registerWithEnv and unregisterWithEnv. The class is abstract.
//  Not written: the constructor; environment, setEnvironment and the
//  protected scheduleEnvUpdate (not virtual, defined outside the
//  header); the environmentChanged signal.
#include <QtQuick3D/qtquick3dglobal.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/sceneeffects_p.h>

//  const QMetaObject *SceneEffectBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15SceneEffectBase10metaObjectEv(
    const SceneEffectBase *self) {
  return self->metaObject();
}

//  SceneEffectBase::~SceneEffectBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN15SceneEffectBaseD1Ev(SceneEffectBase *self) {
  delete self;
}

//  void SceneEffectBase::registerWithEnv(SceneEffectEnvironment
//      *newEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SceneEffectBase15registerWithEnvEP22SceneEffectEnvironment(
    SceneEffectBase *self,
    SceneEffectEnvironment *newEnvironment) {
  self->registerWithEnv(newEnvironment);
}

//  void SceneEffectBase::unregisterWithEnv(SceneEffectEnvironment
//      *oldEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN15SceneEffectBase17unregisterWithEnvEP22SceneEffectEnvironment(
    SceneEffectBase *self,
    SceneEffectEnvironment *oldEnvironment) {
  self->unregisterWithEnv(oldEnvironment);
}
