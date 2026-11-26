//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtriggerbody_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtriggerbody_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QMetaObject *QTriggerBody::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QTriggerBody10metaObjectEv(
    const QTriggerBody *self) {
  return self->metaObject();
}

//  void *QTriggerBody::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QTriggerBody11qt_metacastEPKc(
    QTriggerBody *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QTriggerBody::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QTriggerBody11qt_metacallEN11QMetaObject4CallEiPPv(
    QTriggerBody *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QTriggerBody::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTriggerBody2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTriggerBody::tr(s, c, n));
}

//  QTriggerBody::QTriggerBody()
extern "C" Q_DECL_EXPORT
QTriggerBody *ritual_ZN12QTriggerBodyC1Ev() {
  return new QTriggerBody();
}

//  void QTriggerBody::registerCollision(QAbstractPhysicsNode *collision)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTriggerBody17registerCollisionEP20QAbstractPhysicsNode(
    QTriggerBody *self,
    QAbstractPhysicsNode *collision) {
  self->registerCollision(collision);
}

//  void QTriggerBody::deregisterCollision(QAbstractPhysicsNode *collision)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTriggerBody19deregisterCollisionEP20QAbstractPhysicsNode(
    QTriggerBody *self,
    QAbstractPhysicsNode *collision) {
  self->deregisterCollision(collision);
}

//  int QTriggerBody::collisionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTriggerBody14collisionCountEv(const QTriggerBody *self) {
  return self->collisionCount();
}

//  QAbstractPhysXNode *QTriggerBody::createPhysXBackend()
extern "C" Q_DECL_EXPORT
QAbstractPhysXNode *ritual_ZN12QTriggerBody18createPhysXBackendEv(
    QTriggerBody *self) {
  return self->createPhysXBackend();
}

//  void QTriggerBody::bodyEntered(QAbstractPhysicsNode *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTriggerBody11bodyEnteredEP20QAbstractPhysicsNode(
    QTriggerBody *self,
    QAbstractPhysicsNode *body) {
  self->bodyEntered(body);
}

//  void QTriggerBody::bodyExited(QAbstractPhysicsNode *body)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTriggerBody10bodyExitedEP20QAbstractPhysicsNode(
    QTriggerBody *self,
    QAbstractPhysicsNode *body) {
  self->bodyExited(body);
}

//  void QTriggerBody::collisionCountChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTriggerBody21collisionCountChangedEv(QTriggerBody *self) {
  self->collisionCountChanged();
}
