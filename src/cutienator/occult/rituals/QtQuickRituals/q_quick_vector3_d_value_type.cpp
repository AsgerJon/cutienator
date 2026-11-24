//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickvaluetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qstring.h>
#include <QtGui/qmatrix4x4.h>

//  void QQuickVector3DValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3DValueType20qt_qmlMarker_foreignEv(
    QQuickVector3DValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickVector3DValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3DValueType21qt_qmlMarker_extendedEv(
    QQuickVector3DValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickVector3DValueType::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23QQuickVector3DValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(QQuickVector3DValueType::create(*params));
}

//  QQuickVector3DValueType::QQuickVector3DValueType()
extern "C" Q_DECL_EXPORT
QQuickVector3DValueType *ritual_ZN23QQuickVector3DValueTypeC1Ev() {
  return new QQuickVector3DValueType();
}

//  QQuickVector3DValueType::QQuickVector3DValueType(const QVector3D
//      &vector3D)
extern "C" Q_DECL_EXPORT
QQuickVector3DValueType *ritual_ZN23QQuickVector3DValueTypeC1ERK9QVector3D(
    const QVector3D *vector3D) {
  return new QQuickVector3DValueType(*vector3D);
}

//  QString QQuickVector3DValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickVector3DValueType8toStringEv(
    const QQuickVector3DValueType *self) {
  return new QString(self->toString());
}

//  qreal QQuickVector3DValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector3DValueType1xEv(
    const QQuickVector3DValueType *self) {
  return self->x();
}

//  qreal QQuickVector3DValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector3DValueType1yEv(
    const QQuickVector3DValueType *self) {
  return self->y();
}

//  qreal QQuickVector3DValueType::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector3DValueType1zEv(
    const QQuickVector3DValueType *self) {
  return self->z();
}

//  void QQuickVector3DValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3DValueType4setXEd(
    QQuickVector3DValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void QQuickVector3DValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3DValueType4setYEd(
    QQuickVector3DValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  void QQuickVector3DValueType::setZ(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3DValueType4setZEd(
    QQuickVector3DValueType *self,
    qreal a0) {
  self->setZ(a0);
}

//  QVector3D QQuickVector3DValueType::crossProduct(const QVector3D &vec)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType12crossProductERK9QVector3D(
    const QQuickVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->crossProduct(*vec));
}

//  qreal QQuickVector3DValueType::dotProduct(const QVector3D &vec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector3DValueType10dotProductERK9QVector3D(
    const QQuickVector3DValueType *self,
    const QVector3D *vec) {
  return self->dotProduct(*vec);
}

//  QVector3D QQuickVector3DValueType::times(const QMatrix4x4 &m) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType5timesERK10QMatrix4x4(
    const QQuickVector3DValueType *self,
    const QMatrix4x4 *m) {
  return new QVector3D(self->times(*m));
}

//  QVector3D QQuickVector3DValueType::times(const QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType5timesERK9QVector3D(
    const QQuickVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->times(*vec));
}

//  QVector3D QQuickVector3DValueType::times(qreal scalar) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType5timesEd(
    const QQuickVector3DValueType *self,
    qreal scalar) {
  return new QVector3D(self->times(scalar));
}

//  QVector3D QQuickVector3DValueType::plus(const QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType4plusERK9QVector3D(
    const QQuickVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->plus(*vec));
}

//  QVector3D QQuickVector3DValueType::minus(const QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType5minusERK9QVector3D(
    const QQuickVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->minus(*vec));
}

//  QVector3D QQuickVector3DValueType::normalized() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector3DValueType10normalizedEv(
    const QQuickVector3DValueType *self) {
  return new QVector3D(self->normalized());
}

//  qreal QQuickVector3DValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector3DValueType6lengthEv(
    const QQuickVector3DValueType *self) {
  return self->length();
}

//  QVector2D QQuickVector3DValueType::toVector2d() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector3DValueType10toVector2dEv(
    const QQuickVector3DValueType *self) {
  return new QVector2D(self->toVector2d());
}

//  QVector4D QQuickVector3DValueType::toVector4d() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector3DValueType10toVector4dEv(
    const QQuickVector3DValueType *self) {
  return new QVector4D(self->toVector4d());
}

//  bool QQuickVector3DValueType::fuzzyEquals(const QVector3D &vec, qreal
//      epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickVector3DValueType11fuzzyEqualsERK9QVector3Dd(
    const QQuickVector3DValueType *self,
    const QVector3D *vec,
    qreal epsilon) {
  return self->fuzzyEquals(*vec, epsilon);
}

//  bool QQuickVector3DValueType::fuzzyEquals(const QVector3D &vec) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickVector3DValueType11fuzzyEqualsERK9QVector3D(
    const QQuickVector3DValueType *self,
    const QVector3D *vec) {
  return self->fuzzyEquals(*vec);
}

//  QQuickVector3DValueType::~QQuickVector3DValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector3DValueTypeD1Ev(QQuickVector3DValueType *self) {
  delete self;
}
