//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DPhysi
//  cs/6.12.0/QtQuick3DPhysics/private/qcharactercontroller_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qtquick3dphysicsglobal_p.h>
#include <QtQuick3DPhysics/QtQuick3DPhysics>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qcharactercontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QCharacterController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QCharacterController10metaObjectEv(
    const QCharacterController *self) {
  return self->metaObject();
}

//  QString QCharacterController::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QCharacterController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCharacterController::tr(s, c, n));
}

//  QCharacterController::QCharacterController()
extern "C" Q_DECL_EXPORT
QCharacterController *ritual_ZN20QCharacterControllerC1Ev() {
  return new QCharacterController();
}

//  const QVector3D &QCharacterController::movement() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK20QCharacterController8movementEv(
    const QCharacterController *self) {
  return new QVector3D(self->movement());
}

//  void QCharacterController::setMovement(const QVector3D &newMovement)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCharacterController11setMovementERK9QVector3D(
    QCharacterController *self,
    const QVector3D *newMovement) {
  self->setMovement(*newMovement);
}

//  const QVector3D &QCharacterController::gravity() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK20QCharacterController7gravityEv(
    const QCharacterController *self) {
  return new QVector3D(self->gravity());
}

//  void QCharacterController::setGravity(const QVector3D &newGravity)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCharacterController10setGravityERK9QVector3D(
    QCharacterController *self,
    const QVector3D *newGravity) {
  self->setGravity(*newGravity);
}

//  QVector3D QCharacterController::getDisplacement(float deltaTime)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN20QCharacterController15getDisplacementEf(
    QCharacterController *self,
    float deltaTime) {
  return new QVector3D(self->getDisplacement(deltaTime));
}

//  bool QCharacterController::midAirControl() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCharacterController13midAirControlEv(
    const QCharacterController *self) {
  return self->midAirControl();
}

//  void QCharacterController::setMidAirControl(bool newMidAirControl)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCharacterController16setMidAirControlEb(
    QCharacterController *self,
    bool newMidAirControl) {
  self->setMidAirControl(newMidAirControl);
}

//  void QCharacterController::teleport(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCharacterController8teleportERK9QVector3D(
    QCharacterController *self,
    const QVector3D *position) {
  self->teleport(*position);
}

//  bool QCharacterController::enableShapeHitCallback() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QCharacterController22enableShapeHitCallbackEv(
    const QCharacterController *self) {
  return self->enableShapeHitCallback();
}

//  void QCharacterController::setEnableShapeHitCallback(bool
//      newEnableShapeHitCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QCharacterController25setEnableShapeHitCallbackEb(
    QCharacterController *self,
    bool newEnableShapeHitCallback) {
  self->setEnableShapeHitCallback(newEnableShapeHitCallback);
}
