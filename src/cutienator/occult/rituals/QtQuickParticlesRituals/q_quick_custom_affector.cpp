//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickcustomaffector_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickcustomaffector_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickparticlesystem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  Only a class built on QQuickCustomAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickCustomAffector : QQuickCustomAffector {
  using QQuickCustomAffector::affectParticle;
};

//  const QMetaObject *QQuickCustomAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuickCustomAffector10metaObjectEv(
    const QQuickCustomAffector *self) {
  return self->metaObject();
}

//  QString QQuickCustomAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuickCustomAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickCustomAffector::tr(s, c, n));
}

//  QQuickCustomAffector::QQuickCustomAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickCustomAffector *ritual_ZN20QQuickCustomAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickCustomAffector(parent);
}

//  void QQuickCustomAffector::affectSystem(qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector12affectSystemEd(
    QQuickCustomAffector *self,
    qreal dt) {
  self->affectSystem(dt);
}

//  QQuickDirection *QQuickCustomAffector::position() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK20QQuickCustomAffector8positionEv(
    const QQuickCustomAffector *self) {
  return self->position();
}

//  QQuickDirection *QQuickCustomAffector::velocity() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK20QQuickCustomAffector8velocityEv(
    const QQuickCustomAffector *self) {
  return self->velocity();
}

//  QQuickDirection *QQuickCustomAffector::acceleration() const
extern "C" Q_DECL_EXPORT
QQuickDirection *ritual_ZNK20QQuickCustomAffector12accelerationEv(
    const QQuickCustomAffector *self) {
  return self->acceleration();
}

//  void QQuickCustomAffector::positionReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector13positionResetEv(
    QQuickCustomAffector *self) {
  self->positionReset();
}

//  void QQuickCustomAffector::velocityReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector13velocityResetEv(
    QQuickCustomAffector *self) {
  self->velocityReset();
}

//  void QQuickCustomAffector::accelerationReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector17accelerationResetEv(
    QQuickCustomAffector *self) {
  self->accelerationReset();
}

//  bool QQuickCustomAffector::relative() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickCustomAffector8relativeEv(
    const QQuickCustomAffector *self) {
  return self->relative();
}

//  void QQuickCustomAffector::setPosition(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector11setPositionEP15QQuickDirection(
    QQuickCustomAffector *self,
    QQuickDirection *arg) {
  self->setPosition(arg);
}

//  void QQuickCustomAffector::setVelocity(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector11setVelocityEP15QQuickDirection(
    QQuickCustomAffector *self,
    QQuickDirection *arg) {
  self->setVelocity(arg);
}

//  void QQuickCustomAffector::setAcceleration(QQuickDirection *arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector15setAccelerationEP15QQuickDirection(
    QQuickCustomAffector *self,
    QQuickDirection *arg) {
  self->setAcceleration(arg);
}

//  void QQuickCustomAffector::setRelative(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector11setRelativeEb(
    QQuickCustomAffector *self,
    bool arg) {
  self->setRelative(arg);
}

//  bool QQuickCustomAffector::isAffectConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickCustomAffector17isAffectConnectedEv(
    QQuickCustomAffector *self) {
  return self->isAffectConnected();
}

//  bool QQuickCustomAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickCustomAffector14affectParticleEP18QQuickParticleDatad(
    QQuickCustomAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickCustomAffector::affectProperties(const
//      QList<QQuickParticleData *> &particles, qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickCustomAffector16affectPropertiesERK5QListIP18QQuickParticleDataEd(
    QQuickCustomAffector *self,
    const QList<QQuickParticleData *> *particles,
    qreal dt) {
  self->affectProperties(*particles, dt);
}

//  void QQuickCustomAffector::affectSystem(qreal dt)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickCustomAffector12affectSystemEd(
    QQuickCustomAffector *self,
    qreal dt) {
  self->QQuickCustomAffector::affectSystem(dt);
}

//  bool QQuickCustomAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQuickCustomAffector14affectParticleEP18QQuickParticleDatad(
    QQuickCustomAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickCustomAffector *>(self)->OwnQQuickCustomAffector::affectParticle(
      d,
      dt);
}
