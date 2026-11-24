//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlerepeller_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlerepeller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticleRepeller may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticleRepeller : QQuick3DParticleRepeller {
  using QQuick3DParticleRepeller::prepareToAffect;
  using QQuick3DParticleRepeller::affectParticle;
};

//  const QMetaObject *QQuick3DParticleRepeller::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DParticleRepeller10metaObjectEv(
    const QQuick3DParticleRepeller *self) {
  return self->metaObject();
}

//  QString QQuick3DParticleRepeller::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuick3DParticleRepeller2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticleRepeller::tr(s, c, n));
}

//  QQuick3DParticleRepeller::QQuick3DParticleRepeller(QQuick3DNode *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticleRepeller *ritual_ZN24QQuick3DParticleRepellerC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticleRepeller(parent);
}

//  float QQuick3DParticleRepeller::radius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DParticleRepeller6radiusEv(
    const QQuick3DParticleRepeller *self) {
  return self->radius();
}

//  float QQuick3DParticleRepeller::outerRadius() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DParticleRepeller11outerRadiusEv(
    const QQuick3DParticleRepeller *self) {
  return self->outerRadius();
}

//  float QQuick3DParticleRepeller::strength() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK24QQuick3DParticleRepeller8strengthEv(
    const QQuick3DParticleRepeller *self) {
  return self->strength();
}

//  void QQuick3DParticleRepeller::setRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleRepeller9setRadiusEf(
    QQuick3DParticleRepeller *self,
    float radius) {
  self->setRadius(radius);
}

//  void QQuick3DParticleRepeller::setOuterRadius(float radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleRepeller14setOuterRadiusEf(
    QQuick3DParticleRepeller *self,
    float radius) {
  self->setOuterRadius(radius);
}

//  void QQuick3DParticleRepeller::setStrength(float strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleRepeller11setStrengthEf(
    QQuick3DParticleRepeller *self,
    float strength) {
  self->setStrength(strength);
}

//  void QQuick3DParticleRepeller::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleRepeller15prepareToAffectEv(
    QQuick3DParticleRepeller *self) {
  self->prepareToAffect();
}

//  void QQuick3DParticleRepeller::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DParticleRepeller14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleRepeller *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*sd, d, time);
}

//  void QQuick3DParticleRepeller::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DParticleRepeller15prepareToAffectEv(
    QQuick3DParticleRepeller *self) {
  static_cast<OwnQQuick3DParticleRepeller *>(self)->OwnQQuick3DParticleRepeller::prepareToAffect();
}

//  void QQuick3DParticleRepeller::affectParticle(const QQuick3DParticleData
//      &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQuick3DParticleRepeller14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticleRepeller *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  static_cast<OwnQQuick3DParticleRepeller *>(self)->OwnQQuick3DParticleRepeller::affectParticle(
      *sd,
      d,
      time);
}
