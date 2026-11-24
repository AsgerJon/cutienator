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
#include <QtGui/qquaternion.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>

//  void QQuickQuaternionValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueType20qt_qmlMarker_foreignEv(
    QQuickQuaternionValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickQuaternionValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueType21qt_qmlMarker_extendedEv(
    QQuickQuaternionValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickQuaternionValueType::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN25QQuickQuaternionValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(QQuickQuaternionValueType::create(*params));
}

//  QQuickQuaternionValueType::QQuickQuaternionValueType()
extern "C" Q_DECL_EXPORT
QQuickQuaternionValueType *ritual_ZN25QQuickQuaternionValueTypeC1Ev() {
  return new QQuickQuaternionValueType();
}

//  QQuickQuaternionValueType::QQuickQuaternionValueType(const QQuaternion
//      &quat)
extern "C" Q_DECL_EXPORT
QQuickQuaternionValueType *ritual_ZN25QQuickQuaternionValueTypeC1ERK11QQuaternion(
    const QQuaternion *quat) {
  return new QQuickQuaternionValueType(*quat);
}

//  QString QQuickQuaternionValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QQuickQuaternionValueType8toStringEv(
    const QQuickQuaternionValueType *self) {
  return new QString(self->toString());
}

//  qreal QQuickQuaternionValueType::scalar() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickQuaternionValueType6scalarEv(
    const QQuickQuaternionValueType *self) {
  return self->scalar();
}

//  qreal QQuickQuaternionValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickQuaternionValueType1xEv(
    const QQuickQuaternionValueType *self) {
  return self->x();
}

//  qreal QQuickQuaternionValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickQuaternionValueType1yEv(
    const QQuickQuaternionValueType *self) {
  return self->y();
}

//  qreal QQuickQuaternionValueType::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickQuaternionValueType1zEv(
    const QQuickQuaternionValueType *self) {
  return self->z();
}

//  void QQuickQuaternionValueType::setScalar(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueType9setScalarEd(
    QQuickQuaternionValueType *self,
    qreal a0) {
  self->setScalar(a0);
}

//  void QQuickQuaternionValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueType4setXEd(
    QQuickQuaternionValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void QQuickQuaternionValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueType4setYEd(
    QQuickQuaternionValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  void QQuickQuaternionValueType::setZ(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueType4setZEd(
    QQuickQuaternionValueType *self,
    qreal a0) {
  self->setZ(a0);
}

//  qreal QQuickQuaternionValueType::dotProduct(const QQuaternion &q) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickQuaternionValueType10dotProductERK11QQuaternion(
    const QQuickQuaternionValueType *self,
    const QQuaternion *q) {
  return self->dotProduct(*q);
}

//  QQuaternion QQuickQuaternionValueType::times(const QQuaternion &q) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType5timesERK11QQuaternion(
    const QQuickQuaternionValueType *self,
    const QQuaternion *q) {
  return new QQuaternion(self->times(*q));
}

//  QVector3D QQuickQuaternionValueType::times(const QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK25QQuickQuaternionValueType5timesERK9QVector3D(
    const QQuickQuaternionValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->times(*vec));
}

//  QQuaternion QQuickQuaternionValueType::times(qreal factor) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType5timesEd(
    const QQuickQuaternionValueType *self,
    qreal factor) {
  return new QQuaternion(self->times(factor));
}

//  QQuaternion QQuickQuaternionValueType::plus(const QQuaternion &q) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType4plusERK11QQuaternion(
    const QQuickQuaternionValueType *self,
    const QQuaternion *q) {
  return new QQuaternion(self->plus(*q));
}

//  QQuaternion QQuickQuaternionValueType::minus(const QQuaternion &q) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType5minusERK11QQuaternion(
    const QQuickQuaternionValueType *self,
    const QQuaternion *q) {
  return new QQuaternion(self->minus(*q));
}

//  QQuaternion QQuickQuaternionValueType::normalized() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType10normalizedEv(
    const QQuickQuaternionValueType *self) {
  return new QQuaternion(self->normalized());
}

//  QQuaternion QQuickQuaternionValueType::inverted() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType8invertedEv(
    const QQuickQuaternionValueType *self) {
  return new QQuaternion(self->inverted());
}

//  QQuaternion QQuickQuaternionValueType::conjugated() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK25QQuickQuaternionValueType10conjugatedEv(
    const QQuickQuaternionValueType *self) {
  return new QQuaternion(self->conjugated());
}

//  qreal QQuickQuaternionValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickQuaternionValueType6lengthEv(
    const QQuickQuaternionValueType *self) {
  return self->length();
}

//  QVector3D QQuickQuaternionValueType::toEulerAngles() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK25QQuickQuaternionValueType13toEulerAnglesEv(
    const QQuickQuaternionValueType *self) {
  return new QVector3D(self->toEulerAngles());
}

//  QVector4D QQuickQuaternionValueType::toVector4d() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK25QQuickQuaternionValueType10toVector4dEv(
    const QQuickQuaternionValueType *self) {
  return new QVector4D(self->toVector4d());
}

//  bool QQuickQuaternionValueType::fuzzyEquals(const QQuaternion &q, qreal
//      epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickQuaternionValueType11fuzzyEqualsERK11QQuaterniond(
    const QQuickQuaternionValueType *self,
    const QQuaternion *q,
    qreal epsilon) {
  return self->fuzzyEquals(*q, epsilon);
}

//  bool QQuickQuaternionValueType::fuzzyEquals(const QQuaternion &q) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQuickQuaternionValueType11fuzzyEqualsERK11QQuaternion(
    const QQuickQuaternionValueType *self,
    const QQuaternion *q) {
  return self->fuzzyEquals(*q);
}

//  QQuickQuaternionValueType::~QQuickQuaternionValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickQuaternionValueTypeD1Ev(
    QQuickQuaternionValueType *self) {
  delete self;
}
