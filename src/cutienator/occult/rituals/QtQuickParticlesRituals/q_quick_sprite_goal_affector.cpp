//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickParticles/6.12.0/QtQuickParticles/private/qquickspritegoal_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qtquickparticlesglobal_p.h>
#include <QtQuickParticles/QtQuickParticles>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickParticles/6.12.0/QtQuickParticles/private/qquickspritegoal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  Only a class built on QQuickSpriteGoalAffector may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickSpriteGoalAffector : QQuickSpriteGoalAffector {
  using QQuickSpriteGoalAffector::affectParticle;
};

//  const QMetaObject *QQuickSpriteGoalAffector::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuickSpriteGoalAffector10metaObjectEv(
    const QQuickSpriteGoalAffector *self) {
  return self->metaObject();
}

//  void *QQuickSpriteGoalAffector::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuickSpriteGoalAffector11qt_metacastEPKc(
    QQuickSpriteGoalAffector *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickSpriteGoalAffector::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuickSpriteGoalAffector11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickSpriteGoalAffector *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuickSpriteGoalAffector::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QQuickSpriteGoalAffector2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickSpriteGoalAffector::tr(s, c, n));
}

//  QQuickSpriteGoalAffector::QQuickSpriteGoalAffector(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
QQuickSpriteGoalAffector *ritual_ZN24QQuickSpriteGoalAffectorC1EP10QQuickItem(
    QQuickItem *parent) {
  return new QQuickSpriteGoalAffector(parent);
}

//  QString QQuickSpriteGoalAffector::goalState() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QQuickSpriteGoalAffector9goalStateEv(
    const QQuickSpriteGoalAffector *self) {
  return new QString(self->goalState());
}

//  bool QQuickSpriteGoalAffector::jump() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickSpriteGoalAffector4jumpEv(
    const QQuickSpriteGoalAffector *self) {
  return self->jump();
}

//  bool QQuickSpriteGoalAffector::systemStates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QQuickSpriteGoalAffector12systemStatesEv(
    const QQuickSpriteGoalAffector *self) {
  return self->systemStates();
}

//  bool QQuickSpriteGoalAffector::affectParticle(QQuickParticleData *d,
//      qreal dt)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QQuickSpriteGoalAffector14affectParticleEP18QQuickParticleDatad(
    QQuickSpriteGoalAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return self->affectParticle(d, dt);
}

//  void QQuickSpriteGoalAffector::goalStateChanged(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector16goalStateChangedERK7QString(
    QQuickSpriteGoalAffector *self,
    const QString *arg) {
  self->goalStateChanged(*arg);
}

//  void QQuickSpriteGoalAffector::jumpChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector11jumpChangedEb(
    QQuickSpriteGoalAffector *self,
    bool arg) {
  self->jumpChanged(arg);
}

//  void QQuickSpriteGoalAffector::systemStatesChanged(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector19systemStatesChangedEb(
    QQuickSpriteGoalAffector *self,
    bool arg) {
  self->systemStatesChanged(arg);
}

//  void QQuickSpriteGoalAffector::setGoalState(const QString &arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector12setGoalStateERK7QString(
    QQuickSpriteGoalAffector *self,
    const QString *arg) {
  self->setGoalState(*arg);
}

//  void QQuickSpriteGoalAffector::setJump(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector7setJumpEb(
    QQuickSpriteGoalAffector *self,
    bool arg) {
  self->setJump(arg);
}

//  void QQuickSpriteGoalAffector::setSystemStates(bool arg)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector15setSystemStatesEb(
    QQuickSpriteGoalAffector *self,
    bool arg) {
  self->setSystemStates(arg);
}

//  void QQuickSpriteGoalAffector::updateStateIndex(QQuickStochasticEngine
//      *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuickSpriteGoalAffector16updateStateIndexEP22QQuickStochasticEngine(
    QQuickSpriteGoalAffector *self,
    QQuickStochasticEngine *e) {
  self->updateStateIndex(e);
}

//  bool QQuickSpriteGoalAffector::affectParticle(QQuickParticleData *d,
//      qreal dt)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN24QQuickSpriteGoalAffector14affectParticleEP18QQuickParticleDatad(
    QQuickSpriteGoalAffector *self,
    QQuickParticleData *d,
    qreal dt) {
  return static_cast<OwnQQuickSpriteGoalAffector *>(self)->OwnQQuickSpriteGoalAffector::affectParticle(
      d,
      dt);
}
