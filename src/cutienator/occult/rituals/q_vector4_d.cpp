//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvectornd.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtGui/qmatrix4x4.h>

//  QVector4D::QVector4D()
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1Ev() {
  return new QVector4D();
}

//  QVector4D::QVector4D(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QVector4D(a0);
}

//  QVector4D::QVector4D(float xpos, float ypos, float zpos, float wpos)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1Effff(
    float xpos,
    float ypos,
    float zpos,
    float wpos) {
  return new QVector4D(xpos, ypos, zpos, wpos);
}

//  QVector4D::QVector4D(QPoint point)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1E6QPoint(const QPoint *point) {
  return new QVector4D(*point);
}

//  QVector4D::QVector4D(QPointF point)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1E7QPointF(const QPointF *point) {
  return new QVector4D(*point);
}

//  QVector4D::QVector4D(QVector2D vector)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1E9QVector2D(const QVector2D *vector) {
  return new QVector4D(*vector);
}

//  QVector4D::QVector4D(QVector2D vector, float zpos, float wpos)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1E9QVector2Dff(
    const QVector2D *vector,
    float zpos,
    float wpos) {
  return new QVector4D(*vector, zpos, wpos);
}

//  QVector4D::QVector4D(QVector3D vector)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1E9QVector3D(const QVector3D *vector) {
  return new QVector4D(*vector);
}

//  QVector4D::QVector4D(QVector3D vector, float wpos)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZN9QVector4DC1E9QVector3Df(
    const QVector3D *vector,
    float wpos) {
  return new QVector4D(*vector, wpos);
}

//  bool QVector4D::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QVector4D6isNullEv(const QVector4D *self) {
  return self->isNull();
}

//  float QVector4D::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4D1xEv(const QVector4D *self) {
  return self->x();
}

//  float QVector4D::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4D1yEv(const QVector4D *self) {
  return self->y();
}

//  float QVector4D::z() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4D1zEv(const QVector4D *self) {
  return self->z();
}

//  float QVector4D::w() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4D1wEv(const QVector4D *self) {
  return self->w();
}

//  void QVector4D::setX(float x)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4D4setXEf(QVector4D *self, float x) {
  self->setX(x);
}

//  void QVector4D::setY(float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4D4setYEf(QVector4D *self, float y) {
  self->setY(y);
}

//  void QVector4D::setZ(float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4D4setZEf(QVector4D *self, float z) {
  self->setZ(z);
}

//  void QVector4D::setW(float w)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4D4setWEf(QVector4D *self, float w) {
  self->setW(w);
}

//  float QVector4D::operator[](int i) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4DixEi(const QVector4D *self, int i) {
  return self->operator[](i);
}

//  float QVector4D::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4D6lengthEv(const QVector4D *self) {
  return self->length();
}

//  float QVector4D::lengthSquared() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QVector4D13lengthSquaredEv(const QVector4D *self) {
  return self->lengthSquared();
}

//  QVector4D QVector4D::normalized() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK9QVector4D10normalizedEv(const QVector4D *self) {
  return new QVector4D(self->normalized());
}

//  void QVector4D::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4D9normalizeEv(QVector4D *self) {
  self->normalize();
}

//  QVector4D &QVector4D::operator+=(QVector4D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DpLES_(QVector4D *self, const QVector4D *vector) {
  self->operator+=(*vector);
}

//  QVector4D &QVector4D::operator-=(QVector4D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DmIES_(QVector4D *self, const QVector4D *vector) {
  self->operator-=(*vector);
}

//  QVector4D &QVector4D::operator*=(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DmLEf(QVector4D *self, float factor) {
  self->operator*=(factor);
}

//  QVector4D &QVector4D::operator*=(QVector4D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DmLES_(QVector4D *self, const QVector4D *vector) {
  self->operator*=(*vector);
}

//  QVector4D &QVector4D::operator/=(float divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DdVEf(QVector4D *self, float divisor) {
  self->operator/=(divisor);
}

//  QVector4D &QVector4D::operator/=(QVector4D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DdVES_(QVector4D *self, const QVector4D *vector) {
  self->operator/=(*vector);
}

//  float QVector4D::dotProduct(QVector4D v1, QVector4D v2)
extern "C" Q_DECL_EXPORT
float ritual_ZN9QVector4D10dotProductES_S_(
    const QVector4D *v1,
    const QVector4D *v2) {
  return QVector4D::dotProduct(*v1, *v2);
}

//  bool operator==(QVector4D v1, QVector4D v2)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq9QVector4DS_(const QVector4D *v1, const QVector4D *v2) {
  return operator==(*v1, *v2);
}

//  bool operator!=(QVector4D v1, QVector4D v2)
extern "C" Q_DECL_EXPORT
bool ritual_Zne9QVector4DS_(const QVector4D *v1, const QVector4D *v2) {
  return operator!=(*v1, *v2);
}

//  QVector4D operator+(QVector4D v1, QVector4D v2)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zpl9QVector4DS_(const QVector4D *v1, const QVector4D *v2) {
  return new QVector4D(operator+(*v1, *v2));
}

//  QVector4D operator-(QVector4D v1, QVector4D v2)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zmi9QVector4DS_(const QVector4D *v1, const QVector4D *v2) {
  return new QVector4D(operator-(*v1, *v2));
}

//  QVector4D operator*(float factor, QVector4D vector)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zmlf9QVector4D(float factor, const QVector4D *vector) {
  return new QVector4D(operator*(factor, *vector));
}

//  QVector4D operator*(QVector4D vector, float factor)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zml9QVector4Df(const QVector4D *vector, float factor) {
  return new QVector4D(operator*(*vector, factor));
}

//  QVector4D operator*(QVector4D v1, QVector4D v2)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zml9QVector4DS_(const QVector4D *v1, const QVector4D *v2) {
  return new QVector4D(operator*(*v1, *v2));
}

//  QVector4D operator-(QVector4D vector)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zng9QVector4D(const QVector4D *vector) {
  return new QVector4D(operator-(*vector));
}

//  QVector4D operator/(QVector4D vector, float divisor)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zdv9QVector4Df(const QVector4D *vector, float divisor) {
  return new QVector4D(operator/(*vector, divisor));
}

//  QVector4D operator/(QVector4D vector, QVector4D divisor)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_Zdv9QVector4DS_(
    const QVector4D *vector,
    const QVector4D *divisor) {
  return new QVector4D(operator/(*vector, *divisor));
}

//  QVector2D QVector4D::toVector2D() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QVector4D10toVector2DEv(const QVector4D *self) {
  return new QVector2D(self->toVector2D());
}

//  QVector2D QVector4D::toVector2DAffine() const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZNK9QVector4D16toVector2DAffineEv(const QVector4D *self) {
  return new QVector2D(self->toVector2DAffine());
}

//  QVector3D QVector4D::toVector3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector4D10toVector3DEv(const QVector4D *self) {
  return new QVector3D(self->toVector3D());
}

//  QVector3D QVector4D::toVector3DAffine() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector4D16toVector3DAffineEv(const QVector4D *self) {
  return new QVector3D(self->toVector3DAffine());
}

//  QPoint QVector4D::toPoint() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK9QVector4D7toPointEv(const QVector4D *self) {
  return new QPoint(self->toPoint());
}

//  QPointF QVector4D::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK9QVector4D8toPointFEv(const QVector4D *self) {
  return new QPointF(self->toPointF());
}

//  QVariant QVector4D::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QVector4Dcv8QVariantEv(const QVector4D *self) {
  return new QVariant(self->operator QVariant());
}

//  QVector4D operator*(const QVector4D &vector, const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZmlRK9QVector4DRK10QMatrix4x4(
    const QVector4D *vector,
    const QMatrix4x4 *matrix) {
  return new QVector4D(operator*(*vector, *matrix));
}

//  QVector4D::~QVector4D()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector4DD1Ev(QVector4D *self) {
  delete self;
}
