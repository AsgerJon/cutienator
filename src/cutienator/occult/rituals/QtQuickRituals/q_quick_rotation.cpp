//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktranslate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QQuickRotation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QQuickRotation10metaObjectEv(
    const QQuickRotation *self) {
  return self->metaObject();
}

//  QString QQuickRotation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QQuickRotation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQuickRotation::tr(s, c, n));
}

//  QQuickRotation::QQuickRotation(QObject *parent)
extern "C" Q_DECL_EXPORT
QQuickRotation *ritual_ZN14QQuickRotationC1EP7QObject(QObject *parent) {
  return new QQuickRotation(parent);
}

//  QVector3D QQuickRotation::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QQuickRotation6originEv(const QQuickRotation *self) {
  return new QVector3D(self->origin());
}

//  void QQuickRotation::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRotation9setOriginERK9QVector3D(
    QQuickRotation *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QQuickRotation::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickRotation5angleEv(const QQuickRotation *self) {
  return self->angle();
}

//  void QQuickRotation::setAngle(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRotation8setAngleEd(QQuickRotation *self, qreal a0) {
  self->setAngle(a0);
}

//  QVector3D QQuickRotation::axis() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK14QQuickRotation4axisEv(const QQuickRotation *self) {
  return new QVector3D(self->axis());
}

//  void QQuickRotation::setAxis(const QVector3D &axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRotation7setAxisERK9QVector3D(
    QQuickRotation *self,
    const QVector3D *axis) {
  self->setAxis(*axis);
}

//  void QQuickRotation::setAxis(Qt::Axis axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRotation7setAxisEN2Qt4AxisE(
    QQuickRotation *self,
    Qt::Axis axis) {
  self->setAxis(axis);
}

//  qreal QQuickRotation::distanceToPlane() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QQuickRotation15distanceToPlaneEv(
    const QQuickRotation *self) {
  return self->distanceToPlane();
}

//  void QQuickRotation::setDistanceToPlane(qreal newDistanceToPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQuickRotation18setDistanceToPlaneEd(
    QQuickRotation *self,
    qreal newDistanceToPlane) {
  self->setDistanceToPlane(newDistanceToPlane);
}

//  void QQuickRotation::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK14QQuickRotation7applyToEP10QMatrix4x4(
    const QQuickRotation *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}

//  void QQuickRotation::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK14QQuickRotation7applyToEP10QMatrix4x4(
    const QQuickRotation *self,
    QMatrix4x4 *matrix) {
  self->QQuickRotation::applyTo(matrix);
}
