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

//  void QQuickVector2DValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector2DValueType20qt_qmlMarker_foreignEv(
    QQuickVector2DValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void QQuickVector2DValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector2DValueType21qt_qmlMarker_extendedEv(
    QQuickVector2DValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant QQuickVector2DValueType::create(const QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN23QQuickVector2DValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(QQuickVector2DValueType::create(*params));
}

//  QQuickVector2DValueType::QQuickVector2DValueType()
extern "C" Q_DECL_EXPORT
QQuickVector2DValueType *ritual_ZN23QQuickVector2DValueTypeC1Ev() {
  return new QQuickVector2DValueType();
}

//  QQuickVector2DValueType::QQuickVector2DValueType(const QVector2D
//      &vector2D)
extern "C" Q_DECL_EXPORT
QQuickVector2DValueType *ritual_ZN23QQuickVector2DValueTypeC1ERK9QVector2D(
    const QVector2D *vector2D) {
  return new QQuickVector2DValueType(*vector2D);
}

//  QString QQuickVector2DValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QQuickVector2DValueType8toStringEv(
    const QQuickVector2DValueType *self) {
  return new QString(self->toString());
}

//  qreal QQuickVector2DValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector2DValueType1xEv(
    const QQuickVector2DValueType *self) {
  return self->x();
}

//  qreal QQuickVector2DValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector2DValueType1yEv(
    const QQuickVector2DValueType *self) {
  return self->y();
}

//  void QQuickVector2DValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector2DValueType4setXEd(
    QQuickVector2DValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void QQuickVector2DValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector2DValueType4setYEd(
    QQuickVector2DValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  qreal QQuickVector2DValueType::dotProduct(const QVector2D &vec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector2DValueType10dotProductERK9QVector2D(
    const QQuickVector2DValueType *self,
    const QVector2D *vec) {
  return self->dotProduct(*vec);
}

//  QVector2D QQuickVector2DValueType::times(const QVector2D &vec) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector2DValueType5timesERK9QVector2D(
    const QQuickVector2DValueType *self,
    const QVector2D *vec) {
  return new QVector2D(self->times(*vec));
}

//  QVector2D QQuickVector2DValueType::times(qreal scalar) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector2DValueType5timesEd(
    const QQuickVector2DValueType *self,
    qreal scalar) {
  return new QVector2D(self->times(scalar));
}

//  QVector2D QQuickVector2DValueType::plus(const QVector2D &vec) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector2DValueType4plusERK9QVector2D(
    const QQuickVector2DValueType *self,
    const QVector2D *vec) {
  return new QVector2D(self->plus(*vec));
}

//  QVector2D QQuickVector2DValueType::minus(const QVector2D &vec) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector2DValueType5minusERK9QVector2D(
    const QQuickVector2DValueType *self,
    const QVector2D *vec) {
  return new QVector2D(self->minus(*vec));
}

//  QVector2D QQuickVector2DValueType::normalized() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK23QQuickVector2DValueType10normalizedEv(
    const QQuickVector2DValueType *self) {
  return new QVector2D(self->normalized());
}

//  qreal QQuickVector2DValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK23QQuickVector2DValueType6lengthEv(
    const QQuickVector2DValueType *self) {
  return self->length();
}

//  QVector3D QQuickVector2DValueType::toVector3d() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK23QQuickVector2DValueType10toVector3dEv(
    const QQuickVector2DValueType *self) {
  return new QVector3D(self->toVector3d());
}

//  QVector4D QQuickVector2DValueType::toVector4d() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK23QQuickVector2DValueType10toVector4dEv(
    const QQuickVector2DValueType *self) {
  return new QVector4D(self->toVector4d());
}

//  bool QQuickVector2DValueType::fuzzyEquals(const QVector2D &vec, qreal
//      epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickVector2DValueType11fuzzyEqualsERK9QVector2Dd(
    const QQuickVector2DValueType *self,
    const QVector2D *vec,
    qreal epsilon) {
  return self->fuzzyEquals(*vec, epsilon);
}

//  bool QQuickVector2DValueType::fuzzyEquals(const QVector2D &vec) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QQuickVector2DValueType11fuzzyEqualsERK9QVector2D(
    const QQuickVector2DValueType *self,
    const QVector2D *vec) {
  return self->fuzzyEquals(*vec);
}

//  QQuickVector2DValueType::~QQuickVector2DValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QQuickVector2DValueTypeD1Ev(QQuickVector2DValueType *self) {
  delete self;
}
