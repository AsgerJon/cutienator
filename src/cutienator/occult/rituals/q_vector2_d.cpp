//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvectornd.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>

//  QVector2D::QVector2D()
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1Ev() {
  return new QVector2D();
}

//  QVector2D::QVector2D(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QVector2D(a0);
}

//  QVector2D::QVector2D(float xpos, float ypos)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1Eff(float xpos, float ypos) {
  return new QVector2D(xpos, ypos);
}

//  QVector2D::QVector2D(QPoint point)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1E6QPoint(const QPoint *point) {
  return new QVector2D(*point);
}

//  QVector2D::QVector2D(QPointF point)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1E7QPointF(const QPointF *point) {
  return new QVector2D(*point);
}

//  QVector2D::QVector2D(QVector3D vector)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1E9QVector3D(const QVector3D *vector) {
  return new QVector2D(*vector);
}

//  QVector2D::QVector2D(QVector4D vector)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1E9QVector4D(const QVector4D *vector) {
  return new QVector2D(*vector);
}

//  bool QVector2D::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QVector2D6isNullEv(const QVector2D *self) {
  return self->isNull();
}

//  float QVector2D::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2D1xEv(const QVector2D *self) {
  return self->x();
}

//  float QVector2D::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2D1yEv(const QVector2D *self) {
  return self->y();
}

//  void QVector2D::setX(float x)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2D4setXEf(QVector2D *self, float x) {
  self->setX(x);
}

//  void QVector2D::setY(float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2D4setYEf(QVector2D *self, float y) {
  self->setY(y);
}

//  float QVector2D::operator[](int i) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2DixEi(const QVector2D *self, int i) {
  return self->operator[](i);
}

//  float QVector2D::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2D6lengthEv(const QVector2D *self) {
  return self->length();
}

//  float QVector2D::lengthSquared() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2D13lengthSquaredEv(const QVector2D *self) {
  return self->lengthSquared();
}

//  QVector2D QVector2D::normalized() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QVector2D10normalizedEv(const QVector2D *self) {
  return new QVector2D(self->normalized());
}

//  void QVector2D::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2D9normalizeEv(QVector2D *self) {
  self->normalize();
}

//  float QVector2D::distanceToPoint(QVector2D point) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2D15distanceToPointES_(
    const QVector2D *self,
    const QVector2D *point) {
  return self->distanceToPoint(*point);
}

//  float QVector2D::distanceToLine(QVector2D point, QVector2D direction)
//      const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector2D14distanceToLineES_S_(
    const QVector2D *self,
    const QVector2D *point,
    const QVector2D *direction) {
  return self->distanceToLine(*point, *direction);
}

//  float QVector2D::dotProduct(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
float ritual_ZN9QVector2D10dotProductES_S_(
    const QVector2D *v1,
    const QVector2D *v2) {
  return QVector2D::dotProduct(*v1, *v2);
}

//  QVector3D QVector2D::toVector3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector2D10toVector3DEv(const QVector2D *self) {
  return new QVector3D(self->toVector3D());
}

//  QVector4D QVector2D::toVector4D() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK9QVector2D10toVector4DEv(const QVector2D *self) {
  return new QVector4D(self->toVector4D());
}

//  QPoint QVector2D::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK9QVector2D7toPointEv(const QVector2D *self) {
  return new QPoint(self->toPoint());
}

//  QPointF QVector2D::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QVector2D8toPointFEv(const QVector2D *self) {
  return new QPointF(self->toPointF());
}

//  QVariant QVector2D::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QVector2Dcv8QVariantEv(const QVector2D *self) {
  return new QVariant(self->operator QVariant());
}

//  QVector2D::~QVector2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DD1Ev(QVector2D *self) {
  delete self;
}
