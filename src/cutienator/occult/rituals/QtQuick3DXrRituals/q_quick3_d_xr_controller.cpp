//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcontroller_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qtquick3dxrglobal_p.h>
#include <QtQuick3DXr/QtQuick3DXr>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrcontroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QQuick3DXrController::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QQuick3DXrController10metaObjectEv(
    const QQuick3DXrController *self) {
  return self->metaObject();
}

//  void *QQuick3DXrController::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN20QQuick3DXrController11qt_metacastEPKc(
    QQuick3DXrController *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DXrController::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN20QQuick3DXrController11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DXrController *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QQuick3DXrController::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QQuick3DXrController2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuick3DXrController::tr(s, c, n));
}

//  QQuick3DXrController::QQuick3DXrController()
extern "C" Q_DECL_EXPORT
QQuick3DXrController *ritual_ZN20QQuick3DXrControllerC1Ev() {
  return new QQuick3DXrController();
}

//  Controller QQuick3DXrController::controller() const
extern "C" Q_DECL_EXPORT
QQuick3DXrController::Controller ritual_ZNK20QQuick3DXrController10controllerEv(
    const QQuick3DXrController *self) {
  return self->controller();
}

//  void QQuick3DXrController::setController(Controller newController)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController13setControllerENS_10ControllerE(
    QQuick3DXrController *self,
    QQuick3DXrController::Controller newController) {
  self->setController(newController);
}

//  QQuick3DXrHandInput *QQuick3DXrController::handInput() const
extern "C" Q_DECL_EXPORT
QQuick3DXrHandInput *ritual_ZNK20QQuick3DXrController9handInputEv(
    const QQuick3DXrController *self) {
  return self->handInput();
}

//  HandPoseSpace QQuick3DXrController::poseSpace() const
extern "C" Q_DECL_EXPORT
QQuick3DXrController::HandPoseSpace ritual_ZNK20QQuick3DXrController9poseSpaceEv(
    const QQuick3DXrController *self) {
  return self->poseSpace();
}

//  void QQuick3DXrController::setPoseSpace(HandPoseSpace newPoseSpace)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController12setPoseSpaceENS_13HandPoseSpaceE(
    QQuick3DXrController *self,
    QQuick3DXrController::HandPoseSpace newPoseSpace) {
  self->setPoseSpace(newPoseSpace);
}

//  QVector3D QQuick3DXrController::pokePosition() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK20QQuick3DXrController12pokePositionEv(
    const QQuick3DXrController *self) {
  return new QVector3D(self->pokePosition());
}

//  QList<QVector3D> QQuick3DXrController::jointPositions() const
extern "C" Q_DECL_EXPORT
QList<QVector3D> *ritual_ZNK20QQuick3DXrController14jointPositionsEv(
    const QQuick3DXrController *self) {
  return new QList<QVector3D>(self->jointPositions());
}

//  QList<QQuaternion> QQuick3DXrController::jointRotations() const
extern "C" Q_DECL_EXPORT
QList<QQuaternion> *ritual_ZNK20QQuick3DXrController14jointRotationsEv(
    const QQuick3DXrController *self) {
  return new QList<QQuaternion>(self->jointRotations());
}

//  bool QQuick3DXrController::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuick3DXrController8isActiveEv(
    const QQuick3DXrController *self) {
  return self->isActive();
}

//  void QQuick3DXrController::controllerChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController17controllerChangedEv(
    QQuick3DXrController *self) {
  self->controllerChanged();
}

//  void QQuick3DXrController::actionMapperChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController19actionMapperChangedEv(
    QQuick3DXrController *self) {
  self->actionMapperChanged();
}

//  void QQuick3DXrController::poseSpaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController16poseSpaceChangedEv(
    QQuick3DXrController *self) {
  self->poseSpaceChanged();
}

//  void QQuick3DXrController::pokePositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController19pokePositionChangedEv(
    QQuick3DXrController *self) {
  self->pokePositionChanged();
}

//  void QQuick3DXrController::jointPositionsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController21jointPositionsChangedEv(
    QQuick3DXrController *self) {
  self->jointPositionsChanged();
}

//  void QQuick3DXrController::jointRotationsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController21jointRotationsChangedEv(
    QQuick3DXrController *self) {
  self->jointRotationsChanged();
}

//  void QQuick3DXrController::jointDataUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController16jointDataUpdatedEv(
    QQuick3DXrController *self) {
  self->jointDataUpdated();
}

//  void QQuick3DXrController::isActiveChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuick3DXrController15isActiveChangedEv(
    QQuick3DXrController *self) {
  self->isActiveChanged();
}
