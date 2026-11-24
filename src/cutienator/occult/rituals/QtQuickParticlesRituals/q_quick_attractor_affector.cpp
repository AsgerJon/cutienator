//  Written by dev_tooling.RitualGenerator from the records of QtQuickParticl
//  es/6.12.0/QtQuickParticles/private/qquickpointattractor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickpointattractor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickAttractorAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAttractorAffector : QQuickAttractorAffector {
  using QQuickAttractorAffector::affectParticle;
};

//  const QMetaObject *QQuickAttractorAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickAttractorAffector10metaObjectEv(
    const QQuickAttractorAffector *self) {
  return self->metaObject();
}

//  QString QQuickAttractorAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickAttractorAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAttractorAffector::tr(s, c, n));
}

//  QQuickAttractorAffector::QQuickAttractorAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickAttractorAffector *ritual_ZN23QQuickAttractorAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickAttractorAffector(parent);
}

//  qreal QQuickAttractorAffector::strength() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickAttractorAffector8strengthEv(
    const QQuickAttractorAffector *self) {
  return self->strength();
}

//  qreal QQuickAttractorAffector::pointX() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickAttractorAffector6pointXEv(
    const QQuickAttractorAffector *self) {
  return self->pointX();
}

//  qreal QQuickAttractorAffector::pointY() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickAttractorAffector6pointYEv(
    const QQuickAttractorAffector *self) {
  return self->pointY();
}

//  AffectableParameters QQuickAttractorAffector::affectedParameter() const
extern "C" Q_DECL_EXPORT
QQuickAttractorAffector::AffectableParameters ritual_ZNK23QQuickAttractorAffector17affectedParameterEv(
    const QQuickAttractorAffector *self) {
  return self->affectedParameter();
}

//  Proportion QQuickAttractorAffector::proportionalToDistance() const
extern "C" Q_DECL_EXPORT
QQuickAttractorAffector::Proportion ritual_ZNK23QQuickAttractorAffector22proportionalToDistanceEv(
    const QQuickAttractorAffector *self) {
  return self->proportionalToDistance();
}

//  void QQuickAttractorAffector::setStrength(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAttractorAffector11setStrengthEd(
    QQuickAttractorAffector *self,
    qreal arg) {
  self->setStrength(arg);
}

//  void QQuickAttractorAffector::setPointX(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAttractorAffector9setPointXEd(
    QQuickAttractorAffector *self,
    qreal arg) {
  self->setPointX(arg);
}

//  void QQuickAttractorAffector::setPointY(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAttractorAffector9setPointYEd(
    QQuickAttractorAffector *self,
    qreal arg) {
  self->setPointY(arg);
}

//  void QQuickAttractorAffector::setAffectedParameter(AffectableParameters
//      arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAttractorAffector20setAffectedParameterENS_20AffectableParametersE(
    QQuickAttractorAffector *self,
    QQuickAttractorAffector::AffectableParameters arg) {
  self->setAffectedParameter(arg);
}

//  void QQuickAttractorAffector::setProportionalToDistance(Proportion arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickAttractorAffector25setProportionalToDistanceENS_10ProportionE(
    QQuickAttractorAffector *self,
    QQuickAttractorAffector::Proportion arg) {
  self->setProportionalToDistance(arg);
}

//  bool QQuickAttractorAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickAttractorAffector14affectParticleEP18QQuickParticleDatad(
    QQuickAttractorAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  bool QQuickAttractorAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickAttractorAffector14affectParticleEP18QQuickParticleDatad(
    QQuickAttractorAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickAttractorAffector *>(self)->OwnQQuickAttractorAffector::affectParticle(
      d,
      dt);
}
