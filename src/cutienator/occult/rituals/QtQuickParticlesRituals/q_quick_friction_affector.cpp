//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickfriction_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickfriction_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickFrictionAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickFrictionAffector : QQuickFrictionAffector {
  using QQuickFrictionAffector::affectParticle;
};

//  const QMetaObject *QQuickFrictionAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QQuickFrictionAffector10metaObjectEv(
    const QQuickFrictionAffector *self) {
  return self->metaObject();
}

//  void *QQuickFrictionAffector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QQuickFrictionAffector11qt_metacastEPKc(
    QQuickFrictionAffector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickFrictionAffector::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN22QQuickFrictionAffector11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickFrictionAffector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickFrictionAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QQuickFrictionAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickFrictionAffector::tr(s, c, n));
}

//  QQuickFrictionAffector::QQuickFrictionAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickFrictionAffector *ritual_ZN22QQuickFrictionAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickFrictionAffector(parent);
}

//  qreal QQuickFrictionAffector::factor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickFrictionAffector6factorEv(
    const QQuickFrictionAffector *self) {
  return self->factor();
}

//  qreal QQuickFrictionAffector::threshold() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QQuickFrictionAffector9thresholdEv(
    const QQuickFrictionAffector *self) {
  return self->threshold();
}

//  bool QQuickFrictionAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickFrictionAffector14affectParticleEP18QQuickParticleDatad(
    QQuickFrictionAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickFrictionAffector::factorChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFrictionAffector13factorChangedEd(
    QQuickFrictionAffector *self,
    qreal arg) {
  self->factorChanged(arg);
}

//  void QQuickFrictionAffector::thresholdChanged(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFrictionAffector16thresholdChangedEd(
    QQuickFrictionAffector *self,
    qreal arg) {
  self->thresholdChanged(arg);
}

//  void QQuickFrictionAffector::setFactor(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFrictionAffector9setFactorEd(
    QQuickFrictionAffector *self,
    qreal arg) {
  self->setFactor(arg);
}

//  void QQuickFrictionAffector::setThreshold(qreal arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickFrictionAffector12setThresholdEd(
    QQuickFrictionAffector *self,
    qreal arg) {
  self->setThreshold(arg);
}

//  bool QQuickFrictionAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickFrictionAffector14affectParticleEP18QQuickParticleDatad(
    QQuickFrictionAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickFrictionAffector *>(self)->OwnQQuickFrictionAffector::affectParticle(
      d,
      dt);
}
