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

//  void Qt3DCore::Quick::QQuick3DVector2DValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector2DValueType20qt_qmlMarker_foreignEv(
    Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void Qt3DCore::Quick::QQuick3DVector2DValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector2DValueType21qt_qmlMarker_extendedEv(
    Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant Qt3DCore::Quick::QQuick3DVector2DValueType::create(const
//      QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore5Quick25QQuick3DVector2DValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(
      Qt3DCore::Quick::QQuick3DVector2DValueType::create(
          *params));
}

//  QString Qt3DCore::Quick::QQuick3DVector2DValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType8toStringEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return new QString(self->toString());
}

//  qreal Qt3DCore::Quick::QQuick3DVector2DValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType1xEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return self->x();
}

//  qreal Qt3DCore::Quick::QQuick3DVector2DValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType1yEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return self->y();
}

//  void Qt3DCore::Quick::QQuick3DVector2DValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector2DValueType4setXEd(
    Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void Qt3DCore::Quick::QQuick3DVector2DValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector2DValueType4setYEd(
    Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  qreal Qt3DCore::Quick::QQuick3DVector2DValueType::dotProduct(const
//      QVector2D &vec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType10dotProductERK9QVector2D(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    const QVector2D *vec) {
  return self->dotProduct(*vec);
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector2DValueType::times(const
//      QVector2D &vec) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType5timesERK9QVector2D(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    const QVector2D *vec) {
  return new QVector2D(self->times(*vec));
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector2DValueType::times(qreal scalar)
//      const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType5timesEd(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    qreal scalar) {
  return new QVector2D(self->times(scalar));
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector2DValueType::plus(const
//      QVector2D &vec) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType4plusERK9QVector2D(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    const QVector2D *vec) {
  return new QVector2D(self->plus(*vec));
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector2DValueType::minus(const
//      QVector2D &vec) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType5minusERK9QVector2D(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    const QVector2D *vec) {
  return new QVector2D(self->minus(*vec));
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector2DValueType::normalized() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType10normalizedEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return new QVector2D(self->normalized());
}

//  qreal Qt3DCore::Quick::QQuick3DVector2DValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType6lengthEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return self->length();
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector2DValueType::toVector3d() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType10toVector3dEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return new QVector3D(self->toVector3d());
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector2DValueType::toVector4d() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType10toVector4dEv(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  return new QVector4D(self->toVector4d());
}

//  bool Qt3DCore::Quick::QQuick3DVector2DValueType::fuzzyEquals(const
//      QVector2D &vec, qreal epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType11fuzzyEqualsERK9QVector2Dd(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    const QVector2D *vec,
    qreal epsilon) {
  return self->fuzzyEquals(*vec, epsilon);
}

//  bool Qt3DCore::Quick::QQuick3DVector2DValueType::fuzzyEquals(const
//      QVector2D &vec) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick25QQuick3DVector2DValueType11fuzzyEqualsERK9QVector2D(
    const Qt3DCore::Quick::QQuick3DVector2DValueType *self,
    const QVector2D *vec) {
  return self->fuzzyEquals(*vec);
}

//  Qt3DCore::Quick::QQuick3DVector2DValueType::~QQuick3DVector2DValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector2DValueTypeD1Ev(
    Qt3DCore::Quick::QQuick3DVector2DValueType *self) {
  delete self;
}
