//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickage_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickAgeAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickAgeAffector : QQuickAgeAffector {
  using QQuickAgeAffector::affectParticle;
};

//  const QMetaObject *QQuickAgeAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickAgeAffector10metaObjectEv(
    const QQuickAgeAffector *self) {
  return self->metaObject();
}

//  QString QQuickAgeAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QQuickAgeAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickAgeAffector::tr(s, c, n));
}

//  QQuickAgeAffector::QQuickAgeAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickAgeAffector *ritual_ZN17QQuickAgeAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickAgeAffector(parent);
}

//  int QQuickAgeAffector::lifeLeft() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickAgeAffector8lifeLeftEv(const QQuickAgeAffector *self) {
  return self->lifeLeft();
}

//  bool QQuickAgeAffector::advancePosition() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickAgeAffector15advancePositionEv(
    const QQuickAgeAffector *self) {
  return self->advancePosition();
}

//  bool QQuickAgeAffector::affectParticle(QQuickParticleData *d, qreal dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickAgeAffector14affectParticleEP18QQuickParticleDatad(
    QQuickAgeAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickAgeAffector::setLifeLeft(int arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAgeAffector11setLifeLeftEi(
    QQuickAgeAffector *self,
    int arg) {
  self->setLifeLeft(arg);
}

//  void QQuickAgeAffector::setAdvancePosition(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickAgeAffector18setAdvancePositionEb(
    QQuickAgeAffector *self,
    bool arg) {
  self->setAdvancePosition(arg);
}

//  bool QQuickAgeAffector::affectParticle(QQuickParticleData *d, qreal dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickAgeAffector14affectParticleEP18QQuickParticleDatad(
    QQuickAgeAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickAgeAffector *>(self)->OwnQQuickAgeAffector::affectParticle(
      d,
      dt);
}
