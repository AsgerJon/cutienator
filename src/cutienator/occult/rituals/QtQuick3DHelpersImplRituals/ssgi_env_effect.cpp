//  Written by hand on 2026-11-25 from
//  QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/
//  sceneeffects_p.h, Qt 6.12.0, from Qt's source. Kept as it is when
//  the generator runs again.
//  SsgiEnvEffect is not exported by Qt (no Q_..._EXPORT on its class
//  line), so only its virtual functions are called, through the
//  object: metaObject(), the implicit destructor (virtual through
//  QObject) and the two private overrides registerWithEnv and
//  unregisterWithEnv.
//  Not written: the constructor; enabled and setEnabled (not
//  virtual, defined outside the header); the enabledChanged signal.
#include <QtQuick3D/qtquick3dglobal.h>
#include <QtQuick3DHelpersImpl/6.12.0/QtQuick3DHelpersImpl/private/sceneeffects_p.h>

//  const QMetaObject *SsgiEnvEffect::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13SsgiEnvEffect10metaObjectEv(
    const SsgiEnvEffect *self) {
  return self->metaObject();
}

//  SsgiEnvEffect::~SsgiEnvEffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN13SsgiEnvEffectD1Ev(SsgiEnvEffect *self) {
  delete self;
}

//  void SsgiEnvEffect::registerWithEnv(SceneEffectEnvironment
//      *newEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SsgiEnvEffect15registerWithEnvEP22SceneEffectEnvironment(
    SsgiEnvEffect *self,
    SceneEffectEnvironment *newEnvironment) {
  self->registerWithEnv(newEnvironment);
}

//  void SsgiEnvEffect::unregisterWithEnv(SceneEffectEnvironment
//      *oldEnvironment)
extern "C" Q_DECL_EXPORT
void ritual_ZN13SsgiEnvEffect17unregisterWithEnvEP22SceneEffectEnvironment(
    SsgiEnvEffect *self,
    SceneEffectEnvironment *oldEnvironment) {
  self->unregisterWithEnv(oldEnvironment);
}
