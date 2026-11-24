//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleSystemAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleSystemAnimation : QQuick3DParticleSystemAnimation {
  using QQuick3DParticleSystemAnimation::updateCurrentTime;
  using QQuick3DParticleSystemAnimation::duration;
};

//  const QMetaObject *QQuick3DParticleSystemAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK31QQuick3DParticleSystemAnimation10metaObjectEv(
    const QQuick3DParticleSystemAnimation *self) {
  return self->metaObject();
}

//  void QQuick3DParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuick3DParticleSystemAnimation17updateCurrentTimeEi(
    QQuick3DParticleSystemAnimation *self,
    int t) {
  self->updateCurrentTime(t);
}

//  int QQuick3DParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK31QQuick3DParticleSystemAnimation8durationEv(
    const QQuick3DParticleSystemAnimation *self) {
  return self->duration();
}

//  void QQuick3DParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN31QQuick3DParticleSystemAnimation17updateCurrentTimeEi(
    QQuick3DParticleSystemAnimation *self,
    int t) {
  static_cast<OwnQQuick3DParticleSystemAnimation *>(self)->OwnQQuick3DParticleSystemAnimation::updateCurrentTime(
      t);
}

//  int QQuick3DParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK31QQuick3DParticleSystemAnimation8durationEv(
    const QQuick3DParticleSystemAnimation *self) {
  return static_cast<const OwnQQuick3DParticleSystemAnimation *>(self)->OwnQQuick3DParticleSystemAnimation::duration();
}
