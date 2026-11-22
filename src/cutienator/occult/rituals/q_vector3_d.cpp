//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvectornd.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtGui/qmatrix4x4.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>

//  QVector3D::QVector3D()
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1Ev() {
  return new QVector3D();
}

//  QVector3D::QVector3D(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QVector3D(a0);
}

//  QVector3D::QVector3D(float xpos, float ypos, float zpos)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1Efff(float xpos, float ypos, float zpos) {
  return new QVector3D(xpos, ypos, zpos);
}

//  QVector3D::QVector3D(QPoint point)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1E6QPoint(const QPoint *point) {
  return new QVector3D(*point);
}

//  QVector3D::QVector3D(QPointF point)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1E7QPointF(const QPointF *point) {
  return new QVector3D(*point);
}

//  QVector3D::QVector3D(QVector2D vector)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1E9QVector2D(const QVector2D *vector) {
  return new QVector3D(*vector);
}

//  QVector3D::QVector3D(QVector2D vector, float zpos)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1E9QVector2Df(
    const QVector2D *vector,
    float zpos) {
  return new QVector3D(*vector, zpos);
}

//  QVector3D::QVector3D(QVector4D vector)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3DC1E9QVector4D(const QVector4D *vector) {
  return new QVector3D(*vector);
}

//  bool QVector3D::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QVector3D6isNullEv(const QVector3D *self) {
  return self->isNull();
}

//  float QVector3D::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D1xEv(const QVector3D *self) {
  return self->x();
}

//  float QVector3D::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D1yEv(const QVector3D *self) {
  return self->y();
}

//  float QVector3D::z() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D1zEv(const QVector3D *self) {
  return self->z();
}

//  void QVector3D::setX(float x)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3D4setXEf(QVector3D *self, float x) {
  self->setX(x);
}

//  void QVector3D::setY(float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3D4setYEf(QVector3D *self, float y) {
  self->setY(y);
}

//  void QVector3D::setZ(float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3D4setZEf(QVector3D *self, float z) {
  self->setZ(z);
}

//  float QVector3D::operator[](int i) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3DixEi(const QVector3D *self, int i) {
  return self->operator[](i);
}

//  float QVector3D::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D6lengthEv(const QVector3D *self) {
  return self->length();
}

//  float QVector3D::lengthSquared() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D13lengthSquaredEv(const QVector3D *self) {
  return self->lengthSquared();
}

//  QVector3D QVector3D::normalized() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector3D10normalizedEv(const QVector3D *self) {
  return new QVector3D(self->normalized());
}

//  void QVector3D::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3D9normalizeEv(QVector3D *self) {
  self->normalize();
}

//  QVector3D &QVector3D::operator+=(QVector3D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DpLES_(QVector3D *self, const QVector3D *vector) {
  self->operator+=(*vector);
}

//  QVector3D &QVector3D::operator-=(QVector3D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DmIES_(QVector3D *self, const QVector3D *vector) {
  self->operator-=(*vector);
}

//  QVector3D &QVector3D::operator*=(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DmLEf(QVector3D *self, float factor) {
  self->operator*=(factor);
}

//  QVector3D &QVector3D::operator*=(QVector3D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DmLES_(QVector3D *self, const QVector3D *vector) {
  self->operator*=(*vector);
}

//  QVector3D &QVector3D::operator/=(float divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DdVEf(QVector3D *self, float divisor) {
  self->operator/=(divisor);
}

//  QVector3D &QVector3D::operator/=(QVector3D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DdVES_(QVector3D *self, const QVector3D *vector) {
  self->operator/=(*vector);
}

//  float QVector3D::dotProduct(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
float ritual_ZN9QVector3D10dotProductES_S_(
    const QVector3D *v1,
    const QVector3D *v2) {
  return QVector3D::dotProduct(*v1, *v2);
}

//  QVector3D QVector3D::crossProduct(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3D12crossProductES_S_(
    const QVector3D *v1,
    const QVector3D *v2) {
  return new QVector3D(QVector3D::crossProduct(*v1, *v2));
}

//  QVector3D QVector3D::normal(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3D6normalES_S_(
    const QVector3D *v1,
    const QVector3D *v2) {
  return new QVector3D(QVector3D::normal(*v1, *v2));
}

//  QVector3D QVector3D::normal(QVector3D v1, QVector3D v2, QVector3D v3)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZN9QVector3D6normalES_S_S_(
    const QVector3D *v1,
    const QVector3D *v2,
    const QVector3D *v3) {
  return new QVector3D(QVector3D::normal(*v1, *v2, *v3));
}

//  QVector3D QVector3D::project(const QMatrix4x4 &modelView, const
//      QMatrix4x4 &projection, const QRect &viewport) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector3D7projectERK10QMatrix4x4S2_RK5QRect(
    const QVector3D *self,
    const QMatrix4x4 *modelView,
    const QMatrix4x4 *projection,
    const QRect *viewport) {
  return new QVector3D(self->project(*modelView, *projection, *viewport));
}

//  QVector3D QVector3D::unproject(const QMatrix4x4 &modelView, const
//      QMatrix4x4 &projection, const QRect &viewport) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector3D9unprojectERK10QMatrix4x4S2_RK5QRect(
    const QVector3D *self,
    const QMatrix4x4 *modelView,
    const QMatrix4x4 *projection,
    const QRect *viewport) {
  return new QVector3D(self->unproject(*modelView, *projection, *viewport));
}

//  bool operator==(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq9QVector3DS_(const QVector3D *v1, const QVector3D *v2) {
  return operator==(*v1, *v2);
}

//  bool operator!=(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
bool ritual_Zne9QVector3DS_(const QVector3D *v1, const QVector3D *v2) {
  return operator!=(*v1, *v2);
}

//  float QVector3D::distanceToPoint(QVector3D point) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D15distanceToPointES_(
    const QVector3D *self,
    const QVector3D *point) {
  return self->distanceToPoint(*point);
}

//  float QVector3D::distanceToPlane(QVector3D plane, QVector3D normal) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D15distanceToPlaneES_S_(
    const QVector3D *self,
    const QVector3D *plane,
    const QVector3D *normal) {
  return self->distanceToPlane(*plane, *normal);
}

//  float QVector3D::distanceToPlane(QVector3D plane1, QVector3D plane2,
//      QVector3D plane3) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D15distanceToPlaneES_S_S_(
    const QVector3D *self,
    const QVector3D *plane1,
    const QVector3D *plane2,
    const QVector3D *plane3) {
  return self->distanceToPlane(*plane1, *plane2, *plane3);
}

//  float QVector3D::distanceToLine(QVector3D point, QVector3D direction)
//      const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector3D14distanceToLineES_S_(
    const QVector3D *self,
    const QVector3D *point,
    const QVector3D *direction) {
  return self->distanceToLine(*point, *direction);
}

//  QVector3D operator+(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zpl9QVector3DS_(const QVector3D *v1, const QVector3D *v2) {
  return new QVector3D(operator+(*v1, *v2));
}

//  QVector3D operator-(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zmi9QVector3DS_(const QVector3D *v1, const QVector3D *v2) {
  return new QVector3D(operator-(*v1, *v2));
}

//  QVector3D operator*(float factor, QVector3D vector)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zmlf9QVector3D(float factor, const QVector3D *vector) {
  return new QVector3D(operator*(factor, *vector));
}

//  QVector3D operator*(QVector3D vector, float factor)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zml9QVector3Df(const QVector3D *vector, float factor) {
  return new QVector3D(operator*(*vector, factor));
}

//  QVector3D operator*(QVector3D v1, QVector3D v2)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zml9QVector3DS_(const QVector3D *v1, const QVector3D *v2) {
  return new QVector3D(operator*(*v1, *v2));
}

//  QVector3D operator-(QVector3D vector)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zng9QVector3D(const QVector3D *vector) {
  return new QVector3D(operator-(*vector));
}

//  QVector3D operator/(QVector3D vector, float divisor)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zdv9QVector3Df(const QVector3D *vector, float divisor) {
  return new QVector3D(operator/(*vector, divisor));
}

//  QVector3D operator/(QVector3D vector, QVector3D divisor)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_Zdv9QVector3DS_(
    const QVector3D *vector,
    const QVector3D *divisor) {
  return new QVector3D(operator/(*vector, *divisor));
}

//  QVector2D QVector3D::toVector2D() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QVector3D10toVector2DEv(const QVector3D *self) {
  return new QVector2D(self->toVector2D());
}

//  QVector4D QVector3D::toVector4D() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK9QVector3D10toVector4DEv(const QVector3D *self) {
  return new QVector4D(self->toVector4D());
}

//  QPoint QVector3D::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK9QVector3D7toPointEv(const QVector3D *self) {
  return new QPoint(self->toPoint());
}

//  QPointF QVector3D::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QVector3D8toPointFEv(const QVector3D *self) {
  return new QPointF(self->toPointF());
}

//  QVariant QVector3D::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QVector3Dcv8QVariantEv(const QVector3D *self) {
  return new QVariant(self->operator QVariant());
}

//  QVector3D operator*(const QVector3D &vector, const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZmlRK9QVector3DRK10QMatrix4x4(
    const QVector3D *vector,
    const QMatrix4x4 *matrix) {
  return new QVector3D(operator*(*vector, *matrix));
}

//  QVector3D::~QVector3D()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector3DD1Ev(QVector3D *self) {
  delete self;
}
