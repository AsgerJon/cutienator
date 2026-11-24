//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickgravity_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickgravity_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickGravityAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGravityAffector : QQuickGravityAffector {
  using QQuickGravityAffector::affectParticle;
};

//  const QMetaObject *QQuickGravityAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QQuickGravityAffector10metaObjectEv(
    const QQuickGravityAffector *self) {
  return self->metaObject();
}

//  QString QQuickGravityAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QQuickGravityAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGravityAffector::tr(s, c, n));
}

//  QQuickGravityAffector::QQuickGravityAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGravityAffector *ritual_ZN21QQuickGravityAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickGravityAffector(parent);
}

//  qreal QQuickGravityAffector::magnitude() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickGravityAffector9magnitudeEv(
    const QQuickGravityAffector *self) {
  return self->magnitude();
}

//  qreal QQuickGravityAffector::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QQuickGravityAffector5angleEv(
    const QQuickGravityAffector *self) {
  return self->angle();
}

//  bool QQuickGravityAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QQuickGravityAffector14affectParticleEP18QQuickParticleDatad(
    QQuickGravityAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickGravityAffector::setMagnitude(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickGravityAffector12setMagnitudeEd(
    QQuickGravityAffector *self,
    qreal arg) {
  self->setMagnitude(arg);
}

//  void QQuickGravityAffector::setAcceleration(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickGravityAffector15setAccelerationEd(
    QQuickGravityAffector *self,
    qreal arg) {
  self->setAcceleration(arg);
}

//  void QQuickGravityAffector::setAngle(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickGravityAffector8setAngleEd(
    QQuickGravityAffector *self,
    qreal arg) {
  self->setAngle(arg);
}

//  bool QQuickGravityAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QQuickGravityAffector14affectParticleEP18QQuickParticleDatad(
    QQuickGravityAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickGravityAffector *>(self)->OwnQQuickGravityAffector::affectParticle(
      d,
      dt);
}
