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

//  void Qt3DCore::Quick::QQuick3DVector4DValueType::qt_qmlMarker_foreign()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType20qt_qmlMarker_foreignEv(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  self->qt_qmlMarker_foreign();
}

//  void Qt3DCore::Quick::QQuick3DVector4DValueType::qt_qmlMarker_extended()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType21qt_qmlMarker_extendedEv(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  self->qt_qmlMarker_extended();
}

//  QVariant Qt3DCore::Quick::QQuick3DVector4DValueType::create(const
//      QJSValue &params)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType6createERK8QJSValue(
    const QJSValue *params) {
  return new QVariant(
      Qt3DCore::Quick::QQuick3DVector4DValueType::create(
          *params));
}

//  QString Qt3DCore::Quick::QQuick3DVector4DValueType::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType8toStringEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return new QString(self->toString());
}

//  qreal Qt3DCore::Quick::QQuick3DVector4DValueType::x() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType1xEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return self->x();
}

//  qreal Qt3DCore::Quick::QQuick3DVector4DValueType::y() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType1yEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return self->y();
}

//  qreal Qt3DCore::Quick::QQuick3DVector4DValueType::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType1zEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return self->z();
}

//  qreal Qt3DCore::Quick::QQuick3DVector4DValueType::w() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType1wEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return self->w();
}

//  void Qt3DCore::Quick::QQuick3DVector4DValueType::setX(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType4setXEd(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    qreal a0) {
  self->setX(a0);
}

//  void Qt3DCore::Quick::QQuick3DVector4DValueType::setY(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType4setYEd(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    qreal a0) {
  self->setY(a0);
}

//  void Qt3DCore::Quick::QQuick3DVector4DValueType::setZ(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType4setZEd(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    qreal a0) {
  self->setZ(a0);
}

//  void Qt3DCore::Quick::QQuick3DVector4DValueType::setW(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueType4setWEd(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    qreal a0) {
  self->setW(a0);
}

//  qreal Qt3DCore::Quick::QQuick3DVector4DValueType::dotProduct(const
//      QVector4D &vec) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType10dotProductERK9QVector4D(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QVector4D *vec) {
  return self->dotProduct(*vec);
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector4DValueType::times(const
//      QVector4D &vec) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType5timesERK9QVector4D(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QVector4D *vec) {
  return new QVector4D(self->times(*vec));
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector4DValueType::times(const
//      QMatrix4x4 &m) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType5timesERK10QMatrix4x4(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QMatrix4x4 *m) {
  return new QVector4D(self->times(*m));
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector4DValueType::times(qreal scalar)
//      const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType5timesEd(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    qreal scalar) {
  return new QVector4D(self->times(scalar));
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector4DValueType::plus(const
//      QVector4D &vec) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType4plusERK9QVector4D(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QVector4D *vec) {
  return new QVector4D(self->plus(*vec));
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector4DValueType::minus(const
//      QVector4D &vec) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType5minusERK9QVector4D(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QVector4D *vec) {
  return new QVector4D(self->minus(*vec));
}

//  QVector4D Qt3DCore::Quick::QQuick3DVector4DValueType::normalized() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType10normalizedEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return new QVector4D(self->normalized());
}

//  qreal Qt3DCore::Quick::QQuick3DVector4DValueType::length() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType6lengthEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return self->length();
}

//  QVector2D Qt3DCore::Quick::QQuick3DVector4DValueType::toVector2d() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType10toVector2dEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return new QVector2D(self->toVector2d());
}

//  QVector3D Qt3DCore::Quick::QQuick3DVector4DValueType::toVector3d() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType10toVector3dEv(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  return new QVector3D(self->toVector3d());
}

//  bool Qt3DCore::Quick::QQuick3DVector4DValueType::fuzzyEquals(const
//      QVector4D &vec, qreal epsilon) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType11fuzzyEqualsERK9QVector4Dd(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QVector4D *vec,
    qreal epsilon) {
  return self->fuzzyEquals(*vec, epsilon);
}

//  bool Qt3DCore::Quick::QQuick3DVector4DValueType::fuzzyEquals(const
//      QVector4D &vec) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8Qt3DCore5Quick25QQuick3DVector4DValueType11fuzzyEqualsERK9QVector4D(
    const Qt3DCore::Quick::QQuick3DVector4DValueType *self,
    const QVector4D *vec) {
  return self->fuzzyEquals(*vec);
}

//  Qt3DCore::Quick::QQuick3DVector4DValueType::~QQuick3DVector4DValueType()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Qt3DCore5Quick25QQuick3DVector4DValueTypeD1Ev(
    Qt3DCore::Quick::QQuick3DVector4DValueType *self) {
  delete self;
}
