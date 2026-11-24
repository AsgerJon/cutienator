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

//  void QQuickVector4DValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueType20qt_qmlMarker_foreignEv(
    QQuickVector4DValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickVector4DValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueType21qt_qmlMarker_extendedEv(
    QQuickVector4DValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickVector4DValueType::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23QQuickVector4DValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(QQuickVector4DValueType::create(*params));
}

//  QQuickVector4DValueType::QQuickVector4DValueType()
extern "C" Q_DECL_EXPORT
QQuickVector4DValueType *ritual_ZN23QQuickVector4DValueTypeC1Ev() {
  return new QQuickVector4DValueType();
}

//  QQuickVector4DValueType::QQuickVector4DValueType(const QVector4D
//      &vector4d)
extern "C" Q_DECL_EXPORT
QQuickVector4DValueType *ritual_ZN23QQuickVector4DValueTypeC1ERK9QVector4D(
    const QVector4D *vector4d) {
  return new QQuickVector4DValueType(*vector4d);
}

//  QString QQuickVector4DValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickVector4DValueType8toStringEv(
    const QQuickVector4DValueType *self) {
  return new QString(self->toString());
}

//  qreal QQuickVector4DValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector4DValueType1xEv(
    const QQuickVector4DValueType *self) {
  return self->x();
}

//  qreal QQuickVector4DValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector4DValueType1yEv(
    const QQuickVector4DValueType *self) {
  return self->y();
}

//  qreal QQuickVector4DValueType::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector4DValueType1zEv(
    const QQuickVector4DValueType *self) {
  return self->z();
}

//  qreal QQuickVector4DValueType::w() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector4DValueType1wEv(
    const QQuickVector4DValueType *self) {
  return self->w();
}

//  void QQuickVector4DValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueType4setXEd(
    QQuickVector4DValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void QQuickVector4DValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueType4setYEd(
    QQuickVector4DValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  void QQuickVector4DValueType::setZ(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueType4setZEd(
    QQuickVector4DValueType *self,
    qreal a0) {
  self->setZ(a0);
}

//  void QQuickVector4DValueType::setW(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueType4setWEd(
    QQuickVector4DValueType *self,
    qreal a0) {
  self->setW(a0);
}

//  qreal QQuickVector4DValueType::dotProduct(const QVector4D &vec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector4DValueType10dotProductERK9QVector4D(
    const QQuickVector4DValueType *self,
    const QVector4D *vec) {
  return self->dotProduct(*vec);
}

//  QVector4D QQuickVector4DValueType::times(const QVector4D &vec) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector4DValueType5timesERK9QVector4D(
    const QQuickVector4DValueType *self,
    const QVector4D *vec) {
  return new QVector4D(self->times(*vec));
}

//  QVector4D QQuickVector4DValueType::times(const QMatrix4x4 &m) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector4DValueType5timesERK10QMatrix4x4(
    const QQuickVector4DValueType *self,
    const QMatrix4x4 *m) {
  return new QVector4D(self->times(*m));
}

//  QVector4D QQuickVector4DValueType::times(qreal scalar) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector4DValueType5timesEd(
    const QQuickVector4DValueType *self,
    qreal scalar) {
  return new QVector4D(self->times(scalar));
}

//  QVector4D QQuickVector4DValueType::plus(const QVector4D &vec) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector4DValueType4plusERK9QVector4D(
    const QQuickVector4DValueType *self,
    const QVector4D *vec) {
  return new QVector4D(self->plus(*vec));
}

//  QVector4D QQuickVector4DValueType::minus(const QVector4D &vec) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector4DValueType5minusERK9QVector4D(
    const QQuickVector4DValueType *self,
    const QVector4D *vec) {
  return new QVector4D(self->minus(*vec));
}

//  QVector4D QQuickVector4DValueType::normalized() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector4DValueType10normalizedEv(
    const QQuickVector4DValueType *self) {
  return new QVector4D(self->normalized());
}

//  qreal QQuickVector4DValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector4DValueType6lengthEv(
    const QQuickVector4DValueType *self) {
  return self->length();
}

//  QVector2D QQuickVector4DValueType::toVector2d() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector4DValueType10toVector2dEv(
    const QQuickVector4DValueType *self) {
  return new QVector2D(self->toVector2d());
}

//  QVector3D QQuickVector4DValueType::toVector3d() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector4DValueType10toVector3dEv(
    const QQuickVector4DValueType *self) {
  return new QVector3D(self->toVector3d());
}

//  bool QQuickVector4DValueType::fuzzyEquals(const QVector4D &vec, qreal
//      epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickVector4DValueType11fuzzyEqualsERK9QVector4Dd(
    const QQuickVector4DValueType *self,
    const QVector4D *vec,
    qreal epsilon) {
  return self->fuzzyEquals(*vec, epsilon);
}

//  bool QQuickVector4DValueType::fuzzyEquals(const QVector4D &vec) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickVector4DValueType11fuzzyEqualsERK9QVector4D(
    const QQuickVector4DValueType *self,
    const QVector4D *vec) {
  return self->fuzzyEquals(*vec);
}

//  QQuickVector4DValueType::~QQuickVector4DValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector4DValueTypeD1Ev(QQuickVector4DValueType *self) {
  delete self;
}
