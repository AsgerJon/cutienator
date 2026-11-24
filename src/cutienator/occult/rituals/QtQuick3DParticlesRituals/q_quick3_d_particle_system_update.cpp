//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleSystemUpdate may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleSystemUpdate : QQuick3DParticleSystemUpdate {
  using QQuick3DParticleSystemUpdate::updateCurrentTime;
  using QQuick3DParticleSystemUpdate::duration;
};

//  const QMetaObject *QQuick3DParticleSystemUpdate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DParticleSystemUpdate10metaObjectEv(
    const QQuick3DParticleSystemUpdate *self) {
  return self->metaObject();
}

//  void QQuick3DParticleSystemUpdate::setDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleSystemUpdate8setDirtyEb(
    QQuick3DParticleSystemUpdate *self,
    bool dirty) {
  self->setDirty(dirty);
}

//  void QQuick3DParticleSystemUpdate::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticleSystemUpdate17updateCurrentTimeEi(
    QQuick3DParticleSystemUpdate *self,
    int t) {
  self->updateCurrentTime(t);
}

//  int QQuick3DParticleSystemUpdate::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QQuick3DParticleSystemUpdate8durationEv(
    const QQuick3DParticleSystemUpdate *self) {
  return self->duration();
}

//  void QQuick3DParticleSystemUpdate::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticleSystemUpdate17updateCurrentTimeEi(
    QQuick3DParticleSystemUpdate *self,
    int t) {
  static_cast<OwnQQuick3DParticleSystemUpdate *>(self)->OwnQQuick3DParticleSystemUpdate::updateCurrentTime(
      t);
}

//  int QQuick3DParticleSystemUpdate::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK28QQuick3DParticleSystemUpdate8durationEv(
    const QQuick3DParticleSystemUpdate *self) {
  return static_cast<const OwnQQuick3DParticleSystemUpdate *>(self)->OwnQQuick3DParticleSystemUpdate::duration();
}
