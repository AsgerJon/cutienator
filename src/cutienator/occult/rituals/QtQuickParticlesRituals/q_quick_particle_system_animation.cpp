//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuickParticleSystemAnimation may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickParticleSystemAnimation : QQuickParticleSystemAnimation {
  using QQuickParticleSystemAnimation::updateCurrentTime;
  using QQuickParticleSystemAnimation::duration;
};

//  const QMetaObject *QQuickParticleSystemAnimation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QQuickParticleSystemAnimation10metaObjectEv(
    const QQuickParticleSystemAnimation *self) {
  return self->metaObject();
}

//  void *QQuickParticleSystemAnimation::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN29QQuickParticleSystemAnimation11qt_metacastEPKc(
    QQuickParticleSystemAnimation *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickParticleSystemAnimation::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN29QQuickParticleSystemAnimation11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickParticleSystemAnimation *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  void QQuickParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQuickParticleSystemAnimation17updateCurrentTimeEi(
    QQuickParticleSystemAnimation *self,
    int t) {
  self->updateCurrentTime(t);
}

//  int QQuickParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QQuickParticleSystemAnimation8durationEv(
    const QQuickParticleSystemAnimation *self) {
  return self->duration();
}

//  void QQuickParticleSystemAnimation::updateCurrentTime(int t)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QQuickParticleSystemAnimation17updateCurrentTimeEi(
    QQuickParticleSystemAnimation *self,
    int t) {
  static_cast<OwnQQuickParticleSystemAnimation *>(self)->OwnQQuickParticleSystemAnimation::updateCurrentTime(
      t);
}

//  int QQuickParticleSystemAnimation::duration() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK29QQuickParticleSystemAnimation8durationEv(
    const QQuickParticleSystemAnimation *self) {
  return static_cast<const OwnQQuickParticleSystemAnimation *>(self)->OwnQQuickParticleSystemAnimation::duration();
}
