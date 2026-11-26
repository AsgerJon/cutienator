//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvectornd.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, rituals for functions the generator leaves out: 1. Kept as it is
//  when the generator runs again.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_VECTOR2D)
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

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

#if !defined(QT_NO_VECTOR3D)
//  QVector2D::QVector2D(QVector3D vector)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1E9QVector3D(const QVector3D *vector) {
  return new QVector2D(*vector);
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR4D)
//  QVector2D::QVector2D(QVector4D vector)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_ZN9QVector2DC1E9QVector4D(const QVector4D *vector) {
  return new QVector2D(*vector);
}
#endif  // !defined(QT_NO_VECTOR4D)

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

//  QVector2D &QVector2D::operator+=(QVector2D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DpLES_(QVector2D *self, const QVector2D *vector) {
  self->operator+=(*vector);
}

//  QVector2D &QVector2D::operator-=(QVector2D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DmIES_(QVector2D *self, const QVector2D *vector) {
  self->operator-=(*vector);
}

//  QVector2D &QVector2D::operator*=(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DmLEf(QVector2D *self, float factor) {
  self->operator*=(factor);
}

//  QVector2D &QVector2D::operator*=(QVector2D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DmLES_(QVector2D *self, const QVector2D *vector) {
  self->operator*=(*vector);
}

//  QVector2D &QVector2D::operator/=(float divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DdVEf(QVector2D *self, float divisor) {
  self->operator/=(divisor);
}

//  QVector2D &QVector2D::operator/=(QVector2D vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QVector2DdVES_(QVector2D *self, const QVector2D *vector) {
  self->operator/=(*vector);
}

//  float QVector2D::dotProduct(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
float ritual_ZN9QVector2D10dotProductES_S_(
    const QVector2D *v1,
    const QVector2D *v2) {
  return QVector2D::dotProduct(*v1, *v2);
}

//  bool operator==(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq9QVector2DS_(const QVector2D *v1, const QVector2D *v2) {
  return operator==(*v1, *v2);
}

//  bool operator!=(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
bool ritual_Zne9QVector2DS_(const QVector2D *v1, const QVector2D *v2) {
  return operator!=(*v1, *v2);
}

//  QVector2D operator+(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zpl9QVector2DS_(const QVector2D *v1, const QVector2D *v2) {
  return new QVector2D(operator+(*v1, *v2));
}

//  QVector2D operator-(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zmi9QVector2DS_(const QVector2D *v1, const QVector2D *v2) {
  return new QVector2D(operator-(*v1, *v2));
}

//  QVector2D operator*(float factor, QVector2D vector)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zmlf9QVector2D(float factor, const QVector2D *vector) {
  return new QVector2D(operator*(factor, *vector));
}

//  QVector2D operator*(QVector2D vector, float factor)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zml9QVector2Df(const QVector2D *vector, float factor) {
  return new QVector2D(operator*(*vector, factor));
}

//  QVector2D operator*(QVector2D v1, QVector2D v2)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zml9QVector2DS_(const QVector2D *v1, const QVector2D *v2) {
  return new QVector2D(operator*(*v1, *v2));
}

//  QVector2D operator-(QVector2D vector)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zng9QVector2D(const QVector2D *vector) {
  return new QVector2D(operator-(*vector));
}

//  QVector2D operator/(QVector2D vector, float divisor)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zdv9QVector2Df(const QVector2D *vector, float divisor) {
  return new QVector2D(operator/(*vector, divisor));
}

//  QVector2D operator/(QVector2D vector, QVector2D divisor)
extern "C" Q_DECL_EXPORT
QVector2D *ritual_Zdv9QVector2DS_(
    const QVector2D *vector,
    const QVector2D *divisor) {
  return new QVector2D(operator/(*vector, *divisor));
}

#if !defined(QT_NO_VECTOR3D)
//  QVector3D QVector2D::toVector3D() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9QVector2D10toVector3DEv(const QVector2D *self) {
  return new QVector3D(self->toVector3D());
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR4D)
//  QVector4D QVector2D::toVector4D() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK9QVector2D10toVector4DEv(const QVector2D *self) {
  return new QVector4D(self->toVector4D());
}
#endif  // !defined(QT_NO_VECTOR4D)

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

//  QList<QVector2D>::QList()
extern "C" Q_DECL_EXPORT
QList<QVector2D> *ritual_list_make_QVector2D() {
  return new QList<QVector2D>();
}

//  void QList<QVector2D>::append(const QVector2D &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QVector2D(
    QList<QVector2D> *self,
    const QVector2D *element) {
  self->append(*element);
}

//  qsizetype QList<QVector2D>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QVector2D(const QList<QVector2D> *self) {
  return self->size();
}

//  const QVector2D &QList<QVector2D>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QVector2D *ritual_list_at_QVector2D(
    const QList<QVector2D> *self,
    long long index) {
  return new QVector2D(self->at(index));
}

//  QList<QVector2D>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QVector2D(QList<QVector2D> *self) {
  delete self;
}

//  float &QVector2D::operator[](int i)
extern "C" Q_DECL_EXPORT
float *ritual_ZN9QVector2DixEi(
    QVector2D *self,
    int i) {
  return &((*self)[i]);
}

#endif  // !defined(QT_NO_VECTOR2D)
