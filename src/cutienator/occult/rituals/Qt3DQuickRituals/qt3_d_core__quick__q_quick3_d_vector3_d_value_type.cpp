//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquick_global_p.h>
#include <Qt3DQuick/Qt3DQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuick/6.12.0/Qt3DQuick/private/qt3dquickvaluetypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qjsvalue.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qmatrix4x4.h>

//  void Qt3DCore::Quick::QQuick3DVector3DValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType20qt_qmlMarker_foreignEv(
    Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void Qt3DCore::Quick::QQuick3DVector3DValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType21qt_qmlMarker_extendedEv(
    Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant Qt3DCore::Quick::QQuick3DVector3DValueType::create(const
//      QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(
      Qt3DCore::Quick::QQuick3DVector3DValueType::create(
          *params));
}

//  QString Qt3DCore::Quick::QQuick3DVector3DValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType8toStringEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return new QString(self->toString());
}

//  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType1xEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return self->x();
}

//  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType1yEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return self->y();
}

//  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType1zEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return self->z();
}

//  void Qt3DCore::Quick::QQuick3DVector3DValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType4setXEd(
    Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void Qt3DCore::Quick::QQuick3DVector3DValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType4setYEd(
    Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  void Qt3DCore::Quick::QQuick3DVector3DValueType::setZ(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueType4setZEd(
    Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    qreal a0) {
  self->setZ(a0);
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::crossProduct(const
//      QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType12crossProductERK9QVector3D(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->crossProduct(*vec));
}

//  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::dotProduct(const
//      QVector3D &vec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10dotProductERK9QVector3D(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec) {
  return self->dotProduct(*vec);
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::times(const
//      QMatrix4x4 &m) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5timesERK10QMatrix4x4(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QMatrix4x4 *m) {
  return new QVector3D(self->times(*m));
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::times(const
//      QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5timesERK9QVector3D(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->times(*vec));
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::times(qreal scalar)
//      const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5timesEd(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    qreal scalar) {
  return new QVector3D(self->times(scalar));
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::plus(const
//      QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType4plusERK9QVector3D(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->plus(*vec));
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::minus(const
//      QVector3D &vec) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType5minusERK9QVector3D(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec) {
  return new QVector3D(self->minus(*vec));
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector3DValueType::normalized() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10normalizedEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return new QVector3D(self->normalized());
}

//  qreal Qt3DCore::Quick::QQuick3DVector3DValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType6lengthEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return self->length();
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector3DValueType::toVector2d() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10toVector2dEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return new QVector2D(self->toVector2d());
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector3DValueType::toVector4d() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType10toVector4dEv(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  return new QVector4D(self->toVector4d());
}

//  bool Qt3DCore::Quick::QQuick3DVector3DValueType::fuzzyEquals(const
//      QVector3D &vec, qreal epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType11fuzzyEqualsERK9QVector3Dd(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec,
    qreal epsilon) {
  return self->fuzzyEquals(*vec, epsilon);
}

//  bool Qt3DCore::Quick::QQuick3DVector3DValueType::fuzzyEquals(const
//      QVector3D &vec) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick25QQuick3DVector3DValueType11fuzzyEqualsERK9QVector3D(
    const Qt3DCore::Quick::QQuick3DVector3DValueType *self,
    const QVector3D *vec) {
  return self->fuzzyEquals(*vec);
}

//  Qt3DCore::Quick::QQuick3DVector3DValueType::~QQuick3DVector3DValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector3DValueTypeD1Ev(
    Qt3DCore::Quick::QQuick3DVector3DValueType *self) {
  delete self;
}
