//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DParti
//  cles/6.12.0/QtQuick3DParticles/private/qquick3dparticlepointrotator_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qtquick3dparticlesglobal_p.h>
#include <QtQuick3DParticles/QtQuick3DParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticlepointrotator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DParticles/6.12.0/QtQuick3DParticles/private/qquick3dparticledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Only a class built on QQuick3DParticlePointRotator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuick3DParticlePointRotator : QQuick3DParticlePointRotator {
  using QQuick3DParticlePointRotator::prepareToAffect;
  using QQuick3DParticlePointRotator::affectParticle;
};

//  const QMetaObject *QQuick3DParticlePointRotator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QQuick3DParticlePointRotator10metaObjectEv(
    const QQuick3DParticlePointRotator *self) {
  return self->metaObject();
}

//  QString QQuick3DParticlePointRotator::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QQuick3DParticlePointRotator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DParticlePointRotator::tr(s, c, n));
}

//  QQuick3DParticlePointRotator::QQuick3DParticlePointRotator(QQuick3DNode
//      *parent)
extern "C" Q_DECL_EXPORT
QQuick3DParticlePointRotator *ritual_ZN28QQuick3DParticlePointRotatorC1EP12QQuick3DNode(
    QQuick3DNode *parent) {
  return new QQuick3DParticlePointRotator(parent);
}

//  float QQuick3DParticlePointRotator::magnitude() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK28QQuick3DParticlePointRotator9magnitudeEv(
    const QQuick3DParticlePointRotator *self) {
  return self->magnitude();
}

//  QVector3D QQuick3DParticlePointRotator::direction() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK28QQuick3DParticlePointRotator9directionEv(
    const QQuick3DParticlePointRotator *self) {
  return new QVector3D(self->direction());
}

//  QVector3D QQuick3DParticlePointRotator::pivotPoint() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK28QQuick3DParticlePointRotator10pivotPointEv(
    const QQuick3DParticlePointRotator *self) {
  return new QVector3D(self->pivotPoint());
}

//  void QQuick3DParticlePointRotator::setMagnitude(float magnitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticlePointRotator12setMagnitudeEf(
    QQuick3DParticlePointRotator *self,
    float magnitude) {
  self->setMagnitude(magnitude);
}

//  void QQuick3DParticlePointRotator::setDirection(const QVector3D
//      &direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticlePointRotator12setDirectionERK9QVector3D(
    QQuick3DParticlePointRotator *self,
    const QVector3D *direction) {
  self->setDirection(*direction);
}

//  void QQuick3DParticlePointRotator::setPivotPoint(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticlePointRotator13setPivotPointERK9QVector3D(
    QQuick3DParticlePointRotator *self,
    const QVector3D *point) {
  self->setPivotPoint(*point);
}

//  void QQuick3DParticlePointRotator::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticlePointRotator15prepareToAffectEv(
    QQuick3DParticlePointRotator *self) {
  self->prepareToAffect();
}

//  void QQuick3DParticlePointRotator::affectParticle(const
//      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuick3DParticlePointRotator14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticlePointRotator *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  self->affectParticle(*sd, d, time);
}

//  void QQuick3DParticlePointRotator::prepareToAffect()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticlePointRotator15prepareToAffectEv(
    QQuick3DParticlePointRotator *self) {
  static_cast<OwnQQuick3DParticlePointRotator *>(self)->OwnQQuick3DParticlePointRotator::prepareToAffect();
}

//  void QQuick3DParticlePointRotator::affectParticle(const
//      QQuick3DParticleData &sd, QQuick3DParticleDataCurrent *d, float time)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN28QQuick3DParticlePointRotator14affectParticleERK20QQuick3DParticleDataP27QQuick3DParticleDataCurrentf(
    QQuick3DParticlePointRotator *self,
    const QQuick3DParticleData *sd,
    QQuick3DParticleDataCurrent *d,
    float time) {
  static_cast<OwnQQuick3DParticlePointRotator *>(self)->OwnQQuick3DParticlePointRotator::affectParticle(
      *sd,
      d,
      time);
}
