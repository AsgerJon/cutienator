//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickgroupgoal_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickgroupgoal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickGroupGoalAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickGroupGoalAffector : QQuickGroupGoalAffector {
  using QQuickGroupGoalAffector::affectParticle;
};

//  const QMetaObject *QQuickGroupGoalAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QQuickGroupGoalAffector10metaObjectEv(
    const QQuickGroupGoalAffector *self) {
  return self->metaObject();
}

//  QString QQuickGroupGoalAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN23QQuickGroupGoalAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickGroupGoalAffector::tr(s, c, n));
}

//  QQuickGroupGoalAffector::QQuickGroupGoalAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickGroupGoalAffector *ritual_ZN23QQuickGroupGoalAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickGroupGoalAffector(parent);
}

//  QString QQuickGroupGoalAffector::goalState() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickGroupGoalAffector9goalStateEv(
    const QQuickGroupGoalAffector *self) {
  return new QString(self->goalState());
}

//  bool QQuickGroupGoalAffector::jump() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickGroupGoalAffector4jumpEv(
    const QQuickGroupGoalAffector *self) {
  return self->jump();
}

//  bool QQuickGroupGoalAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QQuickGroupGoalAffector14affectParticleEP18QQuickParticleDatad(
    QQuickGroupGoalAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickGroupGoalAffector::setGoalState(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGroupGoalAffector12setGoalStateERK7QString(
    QQuickGroupGoalAffector *self,
    const QString *arg) {
  self->setGoalState(*arg);
}

//  void QQuickGroupGoalAffector::setJump(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickGroupGoalAffector7setJumpEb(
    QQuickGroupGoalAffector *self,
    bool arg) {
  self->setJump(arg);
}

//  bool QQuickGroupGoalAffector::affectParticle(QQuickParticleData *d, qreal
//      dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QQuickGroupGoalAffector14affectParticleEP18QQuickParticleDatad(
    QQuickGroupGoalAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickGroupGoalAffector *>(self)->OwnQQuickGroupGoalAffector::affectParticle(
      d,
      dt);
}
