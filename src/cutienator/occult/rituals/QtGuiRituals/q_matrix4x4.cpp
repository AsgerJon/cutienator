//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qmatrix4x4.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_MATRIX4X4)
#include <QtGui/qmatrix4x4.h>
#include <QtGui/qtransform.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qpoint.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qrect.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QMatrix4x4::QMatrix4x4()
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN10QMatrix4x4C1Ev() {
  return new QMatrix4x4();
}

//  QMatrix4x4::QMatrix4x4(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN10QMatrix4x4C1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QMatrix4x4(a0);
}

//  QMatrix4x4::QMatrix4x4(float m11, float m12, float m13, float m14, float
//      m21, float m22, float m23, float m24, float m31, float m32, float
//      m33, float m34, float m41, float m42, float m43, float m44)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN10QMatrix4x4C1Effffffffffffffff(
    float m11,
    float m12,
    float m13,
    float m14,
    float m21,
    float m22,
    float m23,
    float m24,
    float m31,
    float m32,
    float m33,
    float m34,
    float m41,
    float m42,
    float m43,
    float m44) {
  return new QMatrix4x4(
      m11,
      m12,
      m13,
      m14,
      m21,
      m22,
      m23,
      m24,
      m31,
      m32,
      m33,
      m34,
      m41,
      m42,
      m43,
      m44);
}

//  QMatrix4x4::QMatrix4x4(const QTransform &transform)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZN10QMatrix4x4C1ERK10QTransform(
    const QTransform *transform) {
  return new QMatrix4x4(*transform);
}

//  const float &QMatrix4x4::operator()(int row, int column) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QMatrix4x4clEii(
    const QMatrix4x4 *self,
    int row,
    int column) {
  return self->operator()(row, column);
}

#if !defined(QT_NO_VECTOR4D)
//  QVector4D QMatrix4x4::column(int index) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK10QMatrix4x46columnEi(
    const QMatrix4x4 *self,
    int index) {
  return new QVector4D(self->column(index));
}
#endif  // !defined(QT_NO_VECTOR4D)

#if !defined(QT_NO_VECTOR4D)
//  void QMatrix4x4::setColumn(int index, const QVector4D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x49setColumnEiRK9QVector4D(
    QMatrix4x4 *self,
    int index,
    const QVector4D *value) {
  self->setColumn(index, *value);
}
#endif  // !defined(QT_NO_VECTOR4D)

#if !defined(QT_NO_VECTOR4D)
//  QVector4D QMatrix4x4::row(int index) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK10QMatrix4x43rowEi(const QMatrix4x4 *self, int index) {
  return new QVector4D(self->row(index));
}
#endif  // !defined(QT_NO_VECTOR4D)

#if !defined(QT_NO_VECTOR4D)
//  void QMatrix4x4::setRow(int index, const QVector4D &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x46setRowEiRK9QVector4D(
    QMatrix4x4 *self,
    int index,
    const QVector4D *value) {
  self->setRow(index, *value);
}
#endif  // !defined(QT_NO_VECTOR4D)

//  bool QMatrix4x4::isAffine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QMatrix4x48isAffineEv(const QMatrix4x4 *self) {
  return self->isAffine();
}

//  bool QMatrix4x4::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QMatrix4x410isIdentityEv(const QMatrix4x4 *self) {
  return self->isIdentity();
}

//  void QMatrix4x4::setToIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x413setToIdentityEv(QMatrix4x4 *self) {
  self->setToIdentity();
}

//  void QMatrix4x4::fill(float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x44fillEf(QMatrix4x4 *self, float value) {
  self->fill(value);
}

//  double QMatrix4x4::determinant() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK10QMatrix4x411determinantEv(const QMatrix4x4 *self) {
  return self->determinant();
}

//  QMatrix4x4 QMatrix4x4::inverted(bool *invertible) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10QMatrix4x48invertedEPb(
    const QMatrix4x4 *self,
    bool *invertible) {
  return new QMatrix4x4(self->inverted(invertible));
}

//  QMatrix4x4 QMatrix4x4::transposed() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10QMatrix4x410transposedEv(const QMatrix4x4 *self) {
  return new QMatrix4x4(self->transposed());
}

//  QMatrix4x4 &QMatrix4x4::operator+=(const QMatrix4x4 &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x4pLERKS_(
    QMatrix4x4 *self,
    const QMatrix4x4 *other) {
  self->operator+=(*other);
}

//  QMatrix4x4 &QMatrix4x4::operator-=(const QMatrix4x4 &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x4mIERKS_(
    QMatrix4x4 *self,
    const QMatrix4x4 *other) {
  self->operator-=(*other);
}

//  QMatrix4x4 &QMatrix4x4::operator*=(const QMatrix4x4 &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x4mLERKS_(
    QMatrix4x4 *self,
    const QMatrix4x4 *other) {
  self->operator*=(*other);
}

//  QMatrix4x4 &QMatrix4x4::operator*=(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x4mLEf(QMatrix4x4 *self, float factor) {
  self->operator*=(factor);
}

//  QMatrix4x4 &QMatrix4x4::operator/=(float divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x4dVEf(QMatrix4x4 *self, float divisor) {
  self->operator/=(divisor);
}

//  bool QMatrix4x4::operator==(const QMatrix4x4 &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QMatrix4x4eqERKS_(
    const QMatrix4x4 *self,
    const QMatrix4x4 *other) {
  return self->operator==(*other);
}

//  bool QMatrix4x4::operator!=(const QMatrix4x4 &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QMatrix4x4neERKS_(
    const QMatrix4x4 *self,
    const QMatrix4x4 *other) {
  return self->operator!=(*other);
}

//  QMatrix4x4 operator+(const QMatrix4x4 &m1, const QMatrix4x4 &m2)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZplRK10QMatrix4x4S1_(
    const QMatrix4x4 *m1,
    const QMatrix4x4 *m2) {
  return new QMatrix4x4(operator+(*m1, *m2));
}

//  QMatrix4x4 operator-(const QMatrix4x4 &m1, const QMatrix4x4 &m2)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZmiRK10QMatrix4x4S1_(
    const QMatrix4x4 *m1,
    const QMatrix4x4 *m2) {
  return new QMatrix4x4(operator-(*m1, *m2));
}

//  QMatrix4x4 operator*(const QMatrix4x4 &m1, const QMatrix4x4 &m2)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZmlRK10QMatrix4x4S1_(
    const QMatrix4x4 *m1,
    const QMatrix4x4 *m2) {
  return new QMatrix4x4(operator*(*m1, *m2));
}

#if !defined(QT_NO_VECTOR3D)
#if QT_DEPRECATED_SINCE(6, 1)
//  QVector3D operator*(const QMatrix4x4 &matrix, const QVector3D &vector)
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZmlRK10QMatrix4x4RK9QVector3D(
    const QMatrix4x4 *matrix,
    const QVector3D *vector) {
  return new QVector3D(operator*(*matrix, *vector));
}
#endif  // QT_DEPRECATED_SINCE(6, 1)
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR4D)
//  QVector4D operator*(const QMatrix4x4 &matrix, const QVector4D &vector)
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZmlRK10QMatrix4x4RK9QVector4D(
    const QMatrix4x4 *matrix,
    const QVector4D *vector) {
  return new QVector4D(operator*(*matrix, *vector));
}
#endif  // !defined(QT_NO_VECTOR4D)

//  QPoint operator*(const QPoint &point, const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK6QPointRK10QMatrix4x4(
    const QPoint *point,
    const QMatrix4x4 *matrix) {
  return new QPoint(operator*(*point, *matrix));
}

//  QPointF operator*(const QPointF &point, const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmlRK7QPointFRK10QMatrix4x4(
    const QPointF *point,
    const QMatrix4x4 *matrix) {
  return new QPointF(operator*(*point, *matrix));
}

//  QMatrix4x4 operator-(const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZngRK10QMatrix4x4(const QMatrix4x4 *matrix) {
  return new QMatrix4x4(operator-(*matrix));
}

#if QT_DEPRECATED_SINCE(6, 1)
//  QPoint operator*(const QMatrix4x4 &matrix, const QPoint &point)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK10QMatrix4x4RK6QPoint(
    const QMatrix4x4 *matrix,
    const QPoint *point) {
  return new QPoint(operator*(*matrix, *point));
}
#endif  // QT_DEPRECATED_SINCE(6, 1)

#if QT_DEPRECATED_SINCE(6, 1)
//  QPointF operator*(const QMatrix4x4 &matrix, const QPointF &point)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmlRK10QMatrix4x4RK7QPointF(
    const QMatrix4x4 *matrix,
    const QPointF *point) {
  return new QPointF(operator*(*matrix, *point));
}
#endif  // QT_DEPRECATED_SINCE(6, 1)

//  QMatrix4x4 operator*(float factor, const QMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZmlfRK10QMatrix4x4(
    float factor,
    const QMatrix4x4 *matrix) {
  return new QMatrix4x4(operator*(factor, *matrix));
}

//  QMatrix4x4 operator*(const QMatrix4x4 &matrix, float factor)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZmlRK10QMatrix4x4f(
    const QMatrix4x4 *matrix,
    float factor) {
  return new QMatrix4x4(operator*(*matrix, factor));
}

//  QMatrix4x4 operator/(const QMatrix4x4 &matrix, float divisor)
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZdvRK10QMatrix4x4f(
    const QMatrix4x4 *matrix,
    float divisor) {
  return new QMatrix4x4(operator/(*matrix, divisor));
}

#if !defined(QT_NO_VECTOR3D)
//  void QMatrix4x4::scale(const QVector3D &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45scaleERK9QVector3D(
    QMatrix4x4 *self,
    const QVector3D *vector) {
  self->scale(*vector);
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  void QMatrix4x4::translate(const QVector3D &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x49translateERK9QVector3D(
    QMatrix4x4 *self,
    const QVector3D *vector) {
  self->translate(*vector);
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  void QMatrix4x4::rotate(float angle, const QVector3D &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x46rotateEfRK9QVector3D(
    QMatrix4x4 *self,
    float angle,
    const QVector3D *vector) {
  self->rotate(angle, *vector);
}
#endif  // !defined(QT_NO_VECTOR3D)

//  void QMatrix4x4::scale(float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45scaleEff(QMatrix4x4 *self, float x, float y) {
  self->scale(x, y);
}

//  void QMatrix4x4::scale(float x, float y, float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45scaleEfff(
    QMatrix4x4 *self,
    float x,
    float y,
    float z) {
  self->scale(x, y, z);
}

//  void QMatrix4x4::scale(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45scaleEf(QMatrix4x4 *self, float factor) {
  self->scale(factor);
}

//  void QMatrix4x4::translate(float x, float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x49translateEff(QMatrix4x4 *self, float x, float y) {
  self->translate(x, y);
}

//  void QMatrix4x4::translate(float x, float y, float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x49translateEfff(
    QMatrix4x4 *self,
    float x,
    float y,
    float z) {
  self->translate(x, y, z);
}

//  void QMatrix4x4::rotate(float angle, float x, float y, float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x46rotateEffff(
    QMatrix4x4 *self,
    float angle,
    float x,
    float y,
    float z) {
  self->rotate(angle, x, y, z);
}

#if !defined(QT_NO_QUATERNION)
//  void QMatrix4x4::rotate(const QQuaternion &quaternion)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x46rotateERK11QQuaternion(
    QMatrix4x4 *self,
    const QQuaternion *quaternion) {
  self->rotate(*quaternion);
}
#endif  // !defined(QT_NO_QUATERNION)

//  void QMatrix4x4::ortho(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45orthoERK5QRect(
    QMatrix4x4 *self,
    const QRect *rect) {
  self->ortho(*rect);
}

//  void QMatrix4x4::ortho(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45orthoERK6QRectF(
    QMatrix4x4 *self,
    const QRectF *rect) {
  self->ortho(*rect);
}

//  void QMatrix4x4::ortho(float left, float right, float bottom, float top,
//      float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x45orthoEffffff(
    QMatrix4x4 *self,
    float left,
    float right,
    float bottom,
    float top,
    float nearPlane,
    float farPlane) {
  self->ortho(left, right, bottom, top, nearPlane, farPlane);
}

//  void QMatrix4x4::frustum(float left, float right, float bottom, float
//      top, float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x47frustumEffffff(
    QMatrix4x4 *self,
    float left,
    float right,
    float bottom,
    float top,
    float nearPlane,
    float farPlane) {
  self->frustum(left, right, bottom, top, nearPlane, farPlane);
}

//  void QMatrix4x4::perspective(float verticalAngle, float aspectRatio,
//      float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x411perspectiveEffff(
    QMatrix4x4 *self,
    float verticalAngle,
    float aspectRatio,
    float nearPlane,
    float farPlane) {
  self->perspective(verticalAngle, aspectRatio, nearPlane, farPlane);
}

#if !defined(QT_NO_VECTOR3D)
//  void QMatrix4x4::lookAt(const QVector3D &eye, const QVector3D &center,
//      const QVector3D &up)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x46lookAtERK9QVector3DS2_S2_(
    QMatrix4x4 *self,
    const QVector3D *eye,
    const QVector3D *center,
    const QVector3D *up) {
  self->lookAt(*eye, *center, *up);
}
#endif  // !defined(QT_NO_VECTOR3D)

//  void QMatrix4x4::viewport(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x48viewportERK6QRectF(
    QMatrix4x4 *self,
    const QRectF *rect) {
  self->viewport(*rect);
}

//  void QMatrix4x4::viewport(float left, float bottom, float width, float
//      height, float nearPlane, float farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x48viewportEffffff(
    QMatrix4x4 *self,
    float left,
    float bottom,
    float width,
    float height,
    float nearPlane,
    float farPlane) {
  self->viewport(left, bottom, width, height, nearPlane, farPlane);
}

//  void QMatrix4x4::flipCoordinates()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x415flipCoordinatesEv(QMatrix4x4 *self) {
  self->flipCoordinates();
}

//  void QMatrix4x4::copyDataTo(float *values) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QMatrix4x410copyDataToEPf(
    const QMatrix4x4 *self,
    float *values) {
  self->copyDataTo(values);
}

//  QTransform QMatrix4x4::toTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QMatrix4x411toTransformEv(const QMatrix4x4 *self) {
  return new QTransform(self->toTransform());
}

//  QTransform QMatrix4x4::toTransform(float distanceToPlane) const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK10QMatrix4x411toTransformEf(
    const QMatrix4x4 *self,
    float distanceToPlane) {
  return new QTransform(self->toTransform(distanceToPlane));
}

//  QPoint QMatrix4x4::map(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10QMatrix4x43mapERK6QPoint(
    const QMatrix4x4 *self,
    const QPoint *point) {
  return new QPoint(self->map(*point));
}

//  QPointF QMatrix4x4::map(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10QMatrix4x43mapERK7QPointF(
    const QMatrix4x4 *self,
    const QPointF *point) {
  return new QPointF(self->map(*point));
}

#if !defined(QT_NO_VECTOR3D)
//  QVector3D QMatrix4x4::map(const QVector3D &point) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10QMatrix4x43mapERK9QVector3D(
    const QMatrix4x4 *self,
    const QVector3D *point) {
  return new QVector3D(self->map(*point));
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  QVector3D QMatrix4x4::mapVector(const QVector3D &vector) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10QMatrix4x49mapVectorERK9QVector3D(
    const QMatrix4x4 *self,
    const QVector3D *vector) {
  return new QVector3D(self->mapVector(*vector));
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR4D)
//  QVector4D QMatrix4x4::map(const QVector4D &point) const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK10QMatrix4x43mapERK9QVector4D(
    const QMatrix4x4 *self,
    const QVector4D *point) {
  return new QVector4D(self->map(*point));
}
#endif  // !defined(QT_NO_VECTOR4D)

//  QRect QMatrix4x4::mapRect(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK10QMatrix4x47mapRectERK5QRect(
    const QMatrix4x4 *self,
    const QRect *rect) {
  return new QRect(self->mapRect(*rect));
}

//  QRectF QMatrix4x4::mapRect(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10QMatrix4x47mapRectERK6QRectF(
    const QMatrix4x4 *self,
    const QRectF *rect) {
  return new QRectF(self->mapRect(*rect));
}

//  void QMatrix4x4::optimize()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x48optimizeEv(QMatrix4x4 *self) {
  self->optimize();
}

//  QVariant QMatrix4x4::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK10QMatrix4x4cv8QVariantEv(const QMatrix4x4 *self) {
  return new QVariant(self->operator QVariant());
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QMatrix4x4 &m)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK10QMatrix4x4(
    const QDebug *dbg,
    const QMatrix4x4 *m) {
  return new QDebug(operator<<(*dbg, *m));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QMatrix4x4::projectedRotate(float angle, float x, float y, float z,
//      float distanceToPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x415projectedRotateEfffff(
    QMatrix4x4 *self,
    float angle,
    float x,
    float y,
    float z,
    float distanceToPlane) {
  self->projectedRotate(angle, x, y, z, distanceToPlane);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QMatrix4x4::projectedRotate(float angle, float x, float y, float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x415projectedRotateEffff(
    QMatrix4x4 *self,
    float angle,
    float x,
    float y,
    float z) {
  self->projectedRotate(angle, x, y, z);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  Flags QMatrix4x4::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QMatrix4x45flagsEv(const QMatrix4x4 *self) {
  return static_cast<int>(self->flags().toInt());
}

//  QMatrix4x4 QMatrix4x4::orthonormalInverse() const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_ZNK10QMatrix4x418orthonormalInverseEv(
    const QMatrix4x4 *self) {
  return new QMatrix4x4(self->orthonormalInverse());
}

//  void QMatrix4x4::toGenericMatrix_impl(float *dst, int n, int m) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK10QMatrix4x420toGenericMatrix_implEPfii(
    const QMatrix4x4 *self,
    float *dst,
    int n,
    int m) {
  self->toGenericMatrix_impl(dst, n, m);
}

//  QMatrix4x4::~QMatrix4x4()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QMatrix4x4D1Ev(QMatrix4x4 *self) {
  delete self;
}

//  QList<QMatrix4x4>::QList()
extern "C" Q_DECL_EXPORT
QList<QMatrix4x4> *ritual_list_make_QMatrix4x4() {
  return new QList<QMatrix4x4>();
}

//  void QList<QMatrix4x4>::append(const QMatrix4x4 &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QMatrix4x4(
    QList<QMatrix4x4> *self,
    const QMatrix4x4 *element) {
  self->append(*element);
}

//  qsizetype QList<QMatrix4x4>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QMatrix4x4(const QList<QMatrix4x4> *self) {
  return self->size();
}

//  const QMatrix4x4 &QList<QMatrix4x4>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QMatrix4x4 *ritual_list_at_QMatrix4x4(
    const QList<QMatrix4x4> *self,
    long long index) {
  return new QMatrix4x4(self->at(index));
}

//  QList<QMatrix4x4>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QMatrix4x4(QList<QMatrix4x4> *self) {
  delete self;
}

#endif  // !defined(QT_NO_MATRIX4X4)
