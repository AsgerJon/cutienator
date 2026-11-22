//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicstransform.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicstransform.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  const QMetaObject *QGraphicsRotation::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGraphicsRotation10metaObjectEv(
    const QGraphicsRotation *self) {
  return self->metaObject();
}

//  QString QGraphicsRotation::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGraphicsRotation2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsRotation::tr(s, c, n));
}

//  QGraphicsRotation::QGraphicsRotation(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsRotation *ritual_ZN17QGraphicsRotationC1EP7QObject(
    QObject *parent) {
  return new QGraphicsRotation(parent);
}

//  QGraphicsRotation::~QGraphicsRotation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotationD1Ev(QGraphicsRotation *self) {
  delete self;
}

//  QVector3D QGraphicsRotation::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QGraphicsRotation6originEv(
    const QGraphicsRotation *self) {
  return new QVector3D(self->origin());
}

//  void QGraphicsRotation::setOrigin(const QVector3D &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation9setOriginERK9QVector3D(
    QGraphicsRotation *self,
    const QVector3D *point) {
  self->setOrigin(*point);
}

//  qreal QGraphicsRotation::angle() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QGraphicsRotation5angleEv(const QGraphicsRotation *self) {
  return self->angle();
}

//  void QGraphicsRotation::setAngle(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation8setAngleEd(
    QGraphicsRotation *self,
    qreal a0) {
  self->setAngle(a0);
}

//  QVector3D QGraphicsRotation::axis() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK17QGraphicsRotation4axisEv(
    const QGraphicsRotation *self) {
  return new QVector3D(self->axis());
}

//  void QGraphicsRotation::setAxis(const QVector3D &axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation7setAxisERK9QVector3D(
    QGraphicsRotation *self,
    const QVector3D *axis) {
  self->setAxis(*axis);
}

//  void QGraphicsRotation::setAxis(Qt::Axis axis)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGraphicsRotation7setAxisEN2Qt4AxisE(
    QGraphicsRotation *self,
    Qt::Axis axis) {
  self->setAxis(axis);
}

//  void QGraphicsRotation::applyTo(QMatrix4x4 *matrix) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QGraphicsRotation7applyToEP10QMatrix4x4(
    const QGraphicsRotation *self,
    QMatrix4x4 *matrix) {
  self->applyTo(matrix);
}
