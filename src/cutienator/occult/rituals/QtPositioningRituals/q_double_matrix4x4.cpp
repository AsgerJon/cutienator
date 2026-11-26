//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qdoublematrix4x4_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, rituals for
//  functions the generator leaves out: 2. Kept as it is when the generator
//  runs again.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublematrix4x4_p.h>
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qdebug.h>

//  QDoubleMatrix4x4::QDoubleMatrix4x4()
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZN16QDoubleMatrix4x4C1Ev() {
  return new QDoubleMatrix4x4();
}

//  QDoubleMatrix4x4::QDoubleMatrix4x4(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZN16QDoubleMatrix4x4C1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QDoubleMatrix4x4(a0);
}

//  QDoubleMatrix4x4::QDoubleMatrix4x4(const double *values)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZN16QDoubleMatrix4x4C1EPKd(const double *values) {
  return new QDoubleMatrix4x4(values);
}

//  QDoubleMatrix4x4::QDoubleMatrix4x4(double m11, double m12, double m13,
//      double m14, double m21, double m22, double m23, double m24, double
//      m31, double m32, double m33, double m34, double m41, double m42,
//      double m43, double m44)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZN16QDoubleMatrix4x4C1Edddddddddddddddd(
    double m11,
    double m12,
    double m13,
    double m14,
    double m21,
    double m22,
    double m23,
    double m24,
    double m31,
    double m32,
    double m33,
    double m34,
    double m41,
    double m42,
    double m43,
    double m44) {
  return new QDoubleMatrix4x4(
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

//  QDoubleMatrix4x4::QDoubleMatrix4x4(const double *values, int cols, int
//      rows)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZN16QDoubleMatrix4x4C1EPKdii(
    const double *values,
    int cols,
    int rows) {
  return new QDoubleMatrix4x4(values, cols, rows);
}

//  const double &QDoubleMatrix4x4::operator()(int row, int column) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QDoubleMatrix4x4clEii(
    const QDoubleMatrix4x4 *self,
    int row,
    int column) {
  return self->operator()(row, column);
}

//  bool QDoubleMatrix4x4::isAffine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDoubleMatrix4x48isAffineEv(const QDoubleMatrix4x4 *self) {
  return self->isAffine();
}

//  bool QDoubleMatrix4x4::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDoubleMatrix4x410isIdentityEv(
    const QDoubleMatrix4x4 *self) {
  return self->isIdentity();
}

//  void QDoubleMatrix4x4::setToIdentity()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x413setToIdentityEv(QDoubleMatrix4x4 *self) {
  self->setToIdentity();
}

//  void QDoubleMatrix4x4::fill(double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x44fillEd(
    QDoubleMatrix4x4 *self,
    double value) {
  self->fill(value);
}

//  double QDoubleMatrix4x4::determinant() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK16QDoubleMatrix4x411determinantEv(
    const QDoubleMatrix4x4 *self) {
  return self->determinant();
}

//  QDoubleMatrix4x4 QDoubleMatrix4x4::inverted(bool *invertible) const
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZNK16QDoubleMatrix4x48invertedEPb(
    const QDoubleMatrix4x4 *self,
    bool *invertible) {
  return new QDoubleMatrix4x4(self->inverted(invertible));
}

//  QDoubleMatrix4x4 QDoubleMatrix4x4::transposed() const
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZNK16QDoubleMatrix4x410transposedEv(
    const QDoubleMatrix4x4 *self) {
  return new QDoubleMatrix4x4(self->transposed());
}

//  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator+=(const QDoubleMatrix4x4
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x4pLERKS_(
    QDoubleMatrix4x4 *self,
    const QDoubleMatrix4x4 *other) {
  self->operator+=(*other);
}

//  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator-=(const QDoubleMatrix4x4
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x4mIERKS_(
    QDoubleMatrix4x4 *self,
    const QDoubleMatrix4x4 *other) {
  self->operator-=(*other);
}

//  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator*=(const QDoubleMatrix4x4
//      &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x4mLERKS_(
    QDoubleMatrix4x4 *self,
    const QDoubleMatrix4x4 *other) {
  self->operator*=(*other);
}

//  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator*=(double factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x4mLEd(QDoubleMatrix4x4 *self, double factor) {
  self->operator*=(factor);
}

//  QDoubleMatrix4x4 &QDoubleMatrix4x4::operator/=(double divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x4dVEd(
    QDoubleMatrix4x4 *self,
    double divisor) {
  self->operator/=(divisor);
}

//  bool QDoubleMatrix4x4::operator==(const QDoubleMatrix4x4 &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDoubleMatrix4x4eqERKS_(
    const QDoubleMatrix4x4 *self,
    const QDoubleMatrix4x4 *other) {
  return self->operator==(*other);
}

//  bool QDoubleMatrix4x4::operator!=(const QDoubleMatrix4x4 &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QDoubleMatrix4x4neERKS_(
    const QDoubleMatrix4x4 *self,
    const QDoubleMatrix4x4 *other) {
  return self->operator!=(*other);
}

//  QDoubleMatrix4x4 operator+(const QDoubleMatrix4x4 &m1, const
//      QDoubleMatrix4x4 &m2)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZplRK16QDoubleMatrix4x4S1_(
    const QDoubleMatrix4x4 *m1,
    const QDoubleMatrix4x4 *m2) {
  return new QDoubleMatrix4x4(operator+(*m1, *m2));
}

//  QDoubleMatrix4x4 operator-(const QDoubleMatrix4x4 &m1, const
//      QDoubleMatrix4x4 &m2)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZmiRK16QDoubleMatrix4x4S1_(
    const QDoubleMatrix4x4 *m1,
    const QDoubleMatrix4x4 *m2) {
  return new QDoubleMatrix4x4(operator-(*m1, *m2));
}

//  QDoubleMatrix4x4 operator*(const QDoubleMatrix4x4 &m1, const
//      QDoubleMatrix4x4 &m2)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZmlRK16QDoubleMatrix4x4S1_(
    const QDoubleMatrix4x4 *m1,
    const QDoubleMatrix4x4 *m2) {
  return new QDoubleMatrix4x4(operator*(*m1, *m2));
}

//  QDoubleVector3D operator*(const QDoubleMatrix4x4 &matrix, const
//      QDoubleVector3D &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZmlRK16QDoubleMatrix4x4RK15QDoubleVector3D(
    const QDoubleMatrix4x4 *matrix,
    const QDoubleVector3D *vector) {
  return new QDoubleVector3D(operator*(*matrix, *vector));
}

//  QDoubleVector3D operator*(const QDoubleVector3D &vector, const
//      QDoubleMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZmlRK15QDoubleVector3DRK16QDoubleMatrix4x4(
    const QDoubleVector3D *vector,
    const QDoubleMatrix4x4 *matrix) {
  return new QDoubleVector3D(operator*(*vector, *matrix));
}

//  QPoint operator*(const QPoint &point, const QDoubleMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK6QPointRK16QDoubleMatrix4x4(
    const QPoint *point,
    const QDoubleMatrix4x4 *matrix) {
  return new QPoint(operator*(*point, *matrix));
}

//  QPointF operator*(const QPointF &point, const QDoubleMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmlRK7QPointFRK16QDoubleMatrix4x4(
    const QPointF *point,
    const QDoubleMatrix4x4 *matrix) {
  return new QPointF(operator*(*point, *matrix));
}

//  QDoubleMatrix4x4 operator-(const QDoubleMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZngRK16QDoubleMatrix4x4(
    const QDoubleMatrix4x4 *matrix) {
  return new QDoubleMatrix4x4(operator-(*matrix));
}

//  QPoint operator*(const QDoubleMatrix4x4 &matrix, const QPoint &point)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK16QDoubleMatrix4x4RK6QPoint(
    const QDoubleMatrix4x4 *matrix,
    const QPoint *point) {
  return new QPoint(operator*(*matrix, *point));
}

//  QPointF operator*(const QDoubleMatrix4x4 &matrix, const QPointF &point)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZmlRK16QDoubleMatrix4x4RK7QPointF(
    const QDoubleMatrix4x4 *matrix,
    const QPointF *point) {
  return new QPointF(operator*(*matrix, *point));
}

//  QDoubleMatrix4x4 operator*(double factor, const QDoubleMatrix4x4 &matrix)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZmldRK16QDoubleMatrix4x4(
    double factor,
    const QDoubleMatrix4x4 *matrix) {
  return new QDoubleMatrix4x4(operator*(factor, *matrix));
}

//  QDoubleMatrix4x4 operator*(const QDoubleMatrix4x4 &matrix, double factor)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZmlRK16QDoubleMatrix4x4d(
    const QDoubleMatrix4x4 *matrix,
    double factor) {
  return new QDoubleMatrix4x4(operator*(*matrix, factor));
}

//  QDoubleMatrix4x4 operator/(const QDoubleMatrix4x4 &matrix, double
//      divisor)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZdvRK16QDoubleMatrix4x4d(
    const QDoubleMatrix4x4 *matrix,
    double divisor) {
  return new QDoubleMatrix4x4(operator/(*matrix, divisor));
}

//  void QDoubleMatrix4x4::scale(const QDoubleVector3D &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45scaleERK15QDoubleVector3D(
    QDoubleMatrix4x4 *self,
    const QDoubleVector3D *vector) {
  self->scale(*vector);
}

//  void QDoubleMatrix4x4::translate(const QDoubleVector3D &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x49translateERK15QDoubleVector3D(
    QDoubleMatrix4x4 *self,
    const QDoubleVector3D *vector) {
  self->translate(*vector);
}

//  void QDoubleMatrix4x4::rotate(double angle, const QDoubleVector3D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x46rotateEdRK15QDoubleVector3D(
    QDoubleMatrix4x4 *self,
    double angle,
    const QDoubleVector3D *vector) {
  self->rotate(angle, *vector);
}

//  void QDoubleMatrix4x4::scale(double x, double y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45scaleEdd(
    QDoubleMatrix4x4 *self,
    double x,
    double y) {
  self->scale(x, y);
}

//  void QDoubleMatrix4x4::scale(double x, double y, double z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45scaleEddd(
    QDoubleMatrix4x4 *self,
    double x,
    double y,
    double z) {
  self->scale(x, y, z);
}

//  void QDoubleMatrix4x4::scale(double factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45scaleEd(
    QDoubleMatrix4x4 *self,
    double factor) {
  self->scale(factor);
}

//  void QDoubleMatrix4x4::translate(double x, double y)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x49translateEdd(
    QDoubleMatrix4x4 *self,
    double x,
    double y) {
  self->translate(x, y);
}

//  void QDoubleMatrix4x4::translate(double x, double y, double z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x49translateEddd(
    QDoubleMatrix4x4 *self,
    double x,
    double y,
    double z) {
  self->translate(x, y, z);
}

//  void QDoubleMatrix4x4::rotate(double angle, double x, double y, double z)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x46rotateEdddd(
    QDoubleMatrix4x4 *self,
    double angle,
    double x,
    double y,
    double z) {
  self->rotate(angle, x, y, z);
}

//  void QDoubleMatrix4x4::ortho(const QRect &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45orthoERK5QRect(
    QDoubleMatrix4x4 *self,
    const QRect *rect) {
  self->ortho(*rect);
}

//  void QDoubleMatrix4x4::ortho(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45orthoERK6QRectF(
    QDoubleMatrix4x4 *self,
    const QRectF *rect) {
  self->ortho(*rect);
}

//  void QDoubleMatrix4x4::ortho(double left, double right, double bottom,
//      double top, double nearPlane, double farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x45orthoEdddddd(
    QDoubleMatrix4x4 *self,
    double left,
    double right,
    double bottom,
    double top,
    double nearPlane,
    double farPlane) {
  self->ortho(left, right, bottom, top, nearPlane, farPlane);
}

//  void QDoubleMatrix4x4::frustum(double left, double right, double bottom,
//      double top, double nearPlane, double farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x47frustumEdddddd(
    QDoubleMatrix4x4 *self,
    double left,
    double right,
    double bottom,
    double top,
    double nearPlane,
    double farPlane) {
  self->frustum(left, right, bottom, top, nearPlane, farPlane);
}

//  void QDoubleMatrix4x4::perspective(double verticalAngle, double
//      aspectRatio, double nearPlane, double farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x411perspectiveEdddd(
    QDoubleMatrix4x4 *self,
    double verticalAngle,
    double aspectRatio,
    double nearPlane,
    double farPlane) {
  self->perspective(verticalAngle, aspectRatio, nearPlane, farPlane);
}

//  void QDoubleMatrix4x4::lookAt(const QDoubleVector3D &eye, const
//      QDoubleVector3D &center, const QDoubleVector3D &up)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x46lookAtERK15QDoubleVector3DS2_S2_(
    QDoubleMatrix4x4 *self,
    const QDoubleVector3D *eye,
    const QDoubleVector3D *center,
    const QDoubleVector3D *up) {
  self->lookAt(*eye, *center, *up);
}

//  void QDoubleMatrix4x4::viewport(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x48viewportERK6QRectF(
    QDoubleMatrix4x4 *self,
    const QRectF *rect) {
  self->viewport(*rect);
}

//  void QDoubleMatrix4x4::viewport(double left, double bottom, double width,
//      double height, double nearPlane, double farPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x48viewportEdddddd(
    QDoubleMatrix4x4 *self,
    double left,
    double bottom,
    double width,
    double height,
    double nearPlane,
    double farPlane) {
  self->viewport(left, bottom, width, height, nearPlane, farPlane);
}

//  void QDoubleMatrix4x4::flipCoordinates()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x415flipCoordinatesEv(QDoubleMatrix4x4 *self) {
  self->flipCoordinates();
}

//  void QDoubleMatrix4x4::copyDataTo(double *values) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QDoubleMatrix4x410copyDataToEPd(
    const QDoubleMatrix4x4 *self,
    double *values) {
  self->copyDataTo(values);
}

//  QPoint QDoubleMatrix4x4::map(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QDoubleMatrix4x43mapERK6QPoint(
    const QDoubleMatrix4x4 *self,
    const QPoint *point) {
  return new QPoint(self->map(*point));
}

//  QPointF QDoubleMatrix4x4::map(const QPointF &point) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK16QDoubleMatrix4x43mapERK7QPointF(
    const QDoubleMatrix4x4 *self,
    const QPointF *point) {
  return new QPointF(self->map(*point));
}

//  QDoubleVector3D QDoubleMatrix4x4::map(const QDoubleVector3D &point) const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK16QDoubleMatrix4x43mapERK15QDoubleVector3D(
    const QDoubleMatrix4x4 *self,
    const QDoubleVector3D *point) {
  return new QDoubleVector3D(self->map(*point));
}

//  QDoubleVector3D QDoubleMatrix4x4::mapVector(const QDoubleVector3D
//      &vector) const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK16QDoubleMatrix4x49mapVectorERK15QDoubleVector3D(
    const QDoubleMatrix4x4 *self,
    const QDoubleVector3D *vector) {
  return new QDoubleVector3D(self->mapVector(*vector));
}

//  QRect QDoubleMatrix4x4::mapRect(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QDoubleMatrix4x47mapRectERK5QRect(
    const QDoubleMatrix4x4 *self,
    const QRect *rect) {
  return new QRect(self->mapRect(*rect));
}

//  QRectF QDoubleMatrix4x4::mapRect(const QRectF &rect) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QDoubleMatrix4x47mapRectERK6QRectF(
    const QDoubleMatrix4x4 *self,
    const QRectF *rect) {
  return new QRectF(self->mapRect(*rect));
}

//  const double *QDoubleMatrix4x4::data() const
extern "C" Q_DECL_EXPORT
const double *ritual_ZNK16QDoubleMatrix4x44dataEv(
    const QDoubleMatrix4x4 *self) {
  return self->data();
}

//  const double *QDoubleMatrix4x4::constData() const
extern "C" Q_DECL_EXPORT
const double *ritual_ZNK16QDoubleMatrix4x49constDataEv(
    const QDoubleMatrix4x4 *self) {
  return self->constData();
}

//  void QDoubleMatrix4x4::optimize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x48optimizeEv(QDoubleMatrix4x4 *self) {
  self->optimize();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug dbg, const QDoubleMatrix4x4 &m)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK16QDoubleMatrix4x4(
    const QDebug *dbg,
    const QDoubleMatrix4x4 *m) {
  return new QDebug(operator<<(*dbg, *m));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QDoubleMatrix4x4::QDoubleMatrix4x4(int a0)
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZN16QDoubleMatrix4x4C1Ei(int a0) {
  return new QDoubleMatrix4x4(a0);
}

//  QDoubleMatrix4x4 QDoubleMatrix4x4::orthonormalInverse() const
extern "C" Q_DECL_EXPORT
QDoubleMatrix4x4 *ritual_ZNK16QDoubleMatrix4x418orthonormalInverseEv(
    const QDoubleMatrix4x4 *self) {
  return new QDoubleMatrix4x4(self->orthonormalInverse());
}

//  void QDoubleMatrix4x4::projectedRotate(double angle, double x, double y,
//      double z, double distanceToPlane)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x415projectedRotateEddddd(
    QDoubleMatrix4x4 *self,
    double angle,
    double x,
    double y,
    double z,
    double distanceToPlane) {
  self->projectedRotate(angle, x, y, z, distanceToPlane);
}

//  QDoubleMatrix4x4::~QDoubleMatrix4x4()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDoubleMatrix4x4D1Ev(QDoubleMatrix4x4 *self) {
  delete self;
}

//  double &QDoubleMatrix4x4::operator()(int row, int column)
extern "C" Q_DECL_EXPORT
double *ritual_ZN16QDoubleMatrix4x4clEii(
    QDoubleMatrix4x4 *self,
    int row,
    int column) {
  return &((*self)(row, column));
}

//  double *QDoubleMatrix4x4::data()
extern "C" Q_DECL_EXPORT
double *ritual_ZN16QDoubleMatrix4x44dataEv(
    QDoubleMatrix4x4 *self) {
  return self->data();
}
