//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  sceneeffects_p.h, Qt 6.12.0. Kept as it is when the generator
//  runs again.
//  DepthOfFieldEffect is not exported by Qt (no Q_..._EXPORT on its
//  class line), so only its virtual functions are called, through
//  the object: metaObject(), the destructor and the two private
//  overrides registerWithEnv and unregisterWithEnv.
//  Not written: the constructor, the enabled and setEnabled functions
//  (not virtual, defined outside the header) and the enabledChanged
//  signal.
#include <QtQuick3D/qtquick3dglobal.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/sceneeffects_p.h>

//  const QMetaObject *DepthOfFieldEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18DepthOfFieldEffect10metaObjectEv(
    const DepthOfFieldEffect *self) {
  return self->metaObject();
}

//  DepthOfFieldEffect::~DepthOfFieldEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN18DepthOfFieldEffectD1Ev(
    DepthOfFieldEffect *self) {
  delete self;
}

//  void DepthOfFieldEffect::registerWithEnv(
//      SceneEffectEnvironment *newEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DepthOfFieldEffect15registerWithEnvEP22SceneEffectEnvironment(
    DepthOfFieldEffect *self,
    SceneEffectEnvironment *newEnvironment) {
  self->registerWithEnv(newEnvironment);
}

//  void DepthOfFieldEffect::unregisterWithEnv(
//      SceneEffectEnvironment *oldEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN18DepthOfFieldEffect17unregisterWithEnvEP22SceneEffectEnvironment(
    DepthOfFieldEffect *self,
    SceneEffectEnvironment *oldEnvironment) {
  self->unregisterWithEnv(oldEnvironment);
}
