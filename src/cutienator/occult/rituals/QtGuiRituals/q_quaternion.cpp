//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qquaternion.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 1. Kept as it is when the
//  generator runs again.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_QUATERNION)
#include <QtGui/qquaternion.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtGui/QMatrix3x3>

//  QQuaternion::QQuaternion()
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternionC1Ev() {
  return new QQuaternion();
}

//  QQuaternion::QQuaternion(Qt::Initialization a0)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternionC1EN2Qt14InitializationE(
    Qt::Initialization a0) {
  return new QQuaternion(a0);
}

//  QQuaternion::QQuaternion(float scalar, float xpos, float ypos, float
//      zpos)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternionC1Effff(
    float scalar,
    float xpos,
    float ypos,
    float zpos) {
  return new QQuaternion(scalar, xpos, ypos, zpos);
}

#if !defined(QT_NO_VECTOR3D)
//  QQuaternion::QQuaternion(float scalar, const QVector3D &vector)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternionC1EfRK9QVector3D(
    float scalar,
    const QVector3D *vector) {
  return new QQuaternion(scalar, *vector);
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR4D)
//  QQuaternion::QQuaternion(const QVector4D &vector)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternionC1ERK9QVector4D(const QVector4D *vector) {
  return new QQuaternion(*vector);
}
#endif  // !defined(QT_NO_VECTOR4D)

//  bool QQuaternion::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuaternion6isNullEv(const QQuaternion *self) {
  return self->isNull();
}

//  bool QQuaternion::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QQuaternion10isIdentityEv(const QQuaternion *self) {
  return self->isIdentity();
}

#if !defined(QT_NO_VECTOR3D)
//  QVector3D QQuaternion::vector() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QQuaternion6vectorEv(const QQuaternion *self) {
  return new QVector3D(self->vector());
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  void QQuaternion::setVector(const QVector3D &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion9setVectorERK9QVector3D(
    QQuaternion *self,
    const QVector3D *vector) {
  self->setVector(*vector);
}
#endif  // !defined(QT_NO_VECTOR3D)

//  void QQuaternion::setVector(float x, float y, float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion9setVectorEfff(
    QQuaternion *self,
    float x,
    float y,
    float z) {
  self->setVector(x, y, z);
}

//  float QQuaternion::x() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuaternion1xEv(const QQuaternion *self) {
  return self->x();
}

//  float QQuaternion::y() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuaternion1yEv(const QQuaternion *self) {
  return self->y();
}

//  float QQuaternion::z() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuaternion1zEv(const QQuaternion *self) {
  return self->z();
}

//  float QQuaternion::scalar() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuaternion6scalarEv(const QQuaternion *self) {
  return self->scalar();
}

//  void QQuaternion::setX(float x)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion4setXEf(QQuaternion *self, float x) {
  self->setX(x);
}

//  void QQuaternion::setY(float y)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion4setYEf(QQuaternion *self, float y) {
  self->setY(y);
}

//  void QQuaternion::setZ(float z)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion4setZEf(QQuaternion *self, float z) {
  self->setZ(z);
}

//  void QQuaternion::setScalar(float scalar)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion9setScalarEf(QQuaternion *self, float scalar) {
  self->setScalar(scalar);
}

//  float QQuaternion::dotProduct(const QQuaternion &q1, const QQuaternion
//      &q2)
extern "C" Q_DECL_EXPORT
float ritual_ZN11QQuaternion10dotProductERKS_S1_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return QQuaternion::dotProduct(*q1, *q2);
}

//  float QQuaternion::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuaternion6lengthEv(const QQuaternion *self) {
  return self->length();
}

//  float QQuaternion::lengthSquared() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK11QQuaternion13lengthSquaredEv(const QQuaternion *self) {
  return self->lengthSquared();
}

//  QQuaternion QQuaternion::normalized() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK11QQuaternion10normalizedEv(const QQuaternion *self) {
  return new QQuaternion(self->normalized());
}

//  void QQuaternion::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternion9normalizeEv(QQuaternion *self) {
  self->normalize();
}

//  QQuaternion QQuaternion::inverted() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK11QQuaternion8invertedEv(const QQuaternion *self) {
  return new QQuaternion(self->inverted());
}

//  QQuaternion QQuaternion::conjugated() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK11QQuaternion10conjugatedEv(const QQuaternion *self) {
  return new QQuaternion(self->conjugated());
}

//  QVector3D QQuaternion::rotatedVector(const QVector3D &vector) const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QQuaternion13rotatedVectorERK9QVector3D(
    const QQuaternion *self,
    const QVector3D *vector) {
  return new QVector3D(self->rotatedVector(*vector));
}

//  QQuaternion &QQuaternion::operator+=(const QQuaternion &quaternion)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternionpLERKS_(
    QQuaternion *self,
    const QQuaternion *quaternion) {
  self->operator+=(*quaternion);
}

//  QQuaternion &QQuaternion::operator-=(const QQuaternion &quaternion)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternionmIERKS_(
    QQuaternion *self,
    const QQuaternion *quaternion) {
  self->operator-=(*quaternion);
}

//  QQuaternion &QQuaternion::operator*=(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternionmLEf(QQuaternion *self, float factor) {
  self->operator*=(factor);
}

//  QQuaternion &QQuaternion::operator*=(const QQuaternion &quaternion)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternionmLERKS_(
    QQuaternion *self,
    const QQuaternion *quaternion) {
  self->operator*=(*quaternion);
}

//  QQuaternion &QQuaternion::operator/=(float divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaterniondVEf(QQuaternion *self, float divisor) {
  self->operator/=(divisor);
}

//  bool operator==(const QQuaternion &q1, const QQuaternion &q2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QQuaternionS1_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return operator==(*q1, *q2);
}

//  bool operator!=(const QQuaternion &q1, const QQuaternion &q2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QQuaternionS1_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return operator!=(*q1, *q2);
}

//  QQuaternion operator+(const QQuaternion &q1, const QQuaternion &q2)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZplRK11QQuaternionS1_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return new QQuaternion(operator+(*q1, *q2));
}

//  QQuaternion operator-(const QQuaternion &q1, const QQuaternion &q2)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZmiRK11QQuaternionS1_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return new QQuaternion(operator-(*q1, *q2));
}

//  QQuaternion operator*(float factor, const QQuaternion &quaternion)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZmlfRK11QQuaternion(
    float factor,
    const QQuaternion *quaternion) {
  return new QQuaternion(operator*(factor, *quaternion));
}

//  QQuaternion operator*(const QQuaternion &quaternion, float factor)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZmlRK11QQuaternionf(
    const QQuaternion *quaternion,
    float factor) {
  return new QQuaternion(operator*(*quaternion, factor));
}

//  QQuaternion operator*(const QQuaternion &q1, const QQuaternion &q2)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZmlRK11QQuaternionS1_(
    const QQuaternion *q1,
    const QQuaternion *q2) {
  return new QQuaternion(operator*(*q1, *q2));
}

//  QQuaternion operator-(const QQuaternion &quaternion)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZngRK11QQuaternion(const QQuaternion *quaternion) {
  return new QQuaternion(operator-(*quaternion));
}

//  QQuaternion operator/(const QQuaternion &quaternion, float divisor)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZdvRK11QQuaternionf(
    const QQuaternion *quaternion,
    float divisor) {
  return new QQuaternion(operator/(*quaternion, divisor));
}

#if !defined(QT_NO_VECTOR4D)
//  QVector4D QQuaternion::toVector4D() const
extern "C" Q_DECL_EXPORT
QVector4D *ritual_ZNK11QQuaternion10toVector4DEv(const QQuaternion *self) {
  return new QVector4D(self->toVector4D());
}
#endif  // !defined(QT_NO_VECTOR4D)

//  QVariant QQuaternion::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QQuaternioncv8QVariantEv(const QQuaternion *self) {
  return new QVariant(self->operator QVariant());
}

#if !defined(QT_NO_VECTOR3D)
//  void QQuaternion::getAxisAndAngle(QVector3D *axis, float *angle) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQuaternion15getAxisAndAngleEP9QVector3DPf(
    const QQuaternion *self,
    QVector3D *axis,
    float *angle) {
  self->getAxisAndAngle(axis, angle);
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  QQuaternion QQuaternion::fromAxisAndAngle(const QVector3D &axis, float
//      angle)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion16fromAxisAndAngleERK9QVector3Df(
    const QVector3D *axis,
    float angle) {
  return new QQuaternion(QQuaternion::fromAxisAndAngle(*axis, angle));
}
#endif  // !defined(QT_NO_VECTOR3D)

//  void QQuaternion::getAxisAndAngle(float *x, float *y, float *z, float
//      *angle) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQuaternion15getAxisAndAngleEPfS0_S0_S0_(
    const QQuaternion *self,
    float *x,
    float *y,
    float *z,
    float *angle) {
  self->getAxisAndAngle(x, y, z, angle);
}

//  QQuaternion QQuaternion::fromAxisAndAngle(float x, float y, float z,
//      float angle)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion16fromAxisAndAngleEffff(
    float x,
    float y,
    float z,
    float angle) {
  return new QQuaternion(QQuaternion::fromAxisAndAngle(x, y, z, angle));
}

#if !defined(QT_NO_VECTOR3D)
//  QVector3D QQuaternion::toEulerAngles() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK11QQuaternion13toEulerAnglesEv(
    const QQuaternion *self) {
  return new QVector3D(self->toEulerAngles());
}
#endif  // !defined(QT_NO_VECTOR3D)

//  void QQuaternion::getEulerAngles(float *pitch, float *yaw, float *roll)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQuaternion14getEulerAnglesEPfS0_S0_(
    const QQuaternion *self,
    float *pitch,
    float *yaw,
    float *roll) {
  self->getEulerAngles(pitch, yaw, roll);
}

//  QQuaternion QQuaternion::fromEulerAngles(float pitch, float yaw, float
//      roll)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion15fromEulerAnglesEfff(
    float pitch,
    float yaw,
    float roll) {
  return new QQuaternion(QQuaternion::fromEulerAngles(pitch, yaw, roll));
}

//  QMatrix3x3 QQuaternion::toRotationMatrix() const
extern "C" Q_DECL_EXPORT
QMatrix3x3 *ritual_ZNK11QQuaternion16toRotationMatrixEv(
    const QQuaternion *self) {
  return new QMatrix3x3(self->toRotationMatrix());
}

//  QQuaternion QQuaternion::fromRotationMatrix(const QMatrix3x3 &rot3x3)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion18fromRotationMatrixERK14QGenericMatrixILi3ELi3EfE(
    const QMatrix3x3 *rot3x3) {
  return new QQuaternion(QQuaternion::fromRotationMatrix(*rot3x3));
}

//  Axes QQuaternion::toAxes() const
extern "C" Q_DECL_EXPORT
QQuaternion::Axes *ritual_ZNK11QQuaternion6toAxesEv(
    const QQuaternion *self) {
  return new QQuaternion::Axes(self->toAxes());
}

//  QQuaternion QQuaternion::fromAxes(Axes axes)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion8fromAxesENS_4AxesE(
    const QQuaternion::Axes *axes) {
  return new QQuaternion(QQuaternion::fromAxes(*axes));
}

#if !defined(QT_NO_VECTOR3D)
//  void QQuaternion::getAxes(QVector3D *xAxis, QVector3D *yAxis, QVector3D
//      *zAxis) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QQuaternion7getAxesEP9QVector3DS1_S1_(
    const QQuaternion *self,
    QVector3D *xAxis,
    QVector3D *yAxis,
    QVector3D *zAxis) {
  self->getAxes(xAxis, yAxis, zAxis);
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  QQuaternion QQuaternion::fromAxes(const QVector3D &xAxis, const QVector3D
//      &yAxis, const QVector3D &zAxis)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion8fromAxesERK9QVector3DS2_S2_(
    const QVector3D *xAxis,
    const QVector3D *yAxis,
    const QVector3D *zAxis) {
  return new QQuaternion(QQuaternion::fromAxes(*xAxis, *yAxis, *zAxis));
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  QQuaternion QQuaternion::fromDirection(const QVector3D &direction, const
//      QVector3D &up)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion13fromDirectionERK9QVector3DS2_(
    const QVector3D *direction,
    const QVector3D *up) {
  return new QQuaternion(QQuaternion::fromDirection(*direction, *up));
}
#endif  // !defined(QT_NO_VECTOR3D)

#if !defined(QT_NO_VECTOR3D)
//  QQuaternion QQuaternion::rotationTo(const QVector3D &from, const
//      QVector3D &to)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion10rotationToERK9QVector3DS2_(
    const QVector3D *from,
    const QVector3D *to) {
  return new QQuaternion(QQuaternion::rotationTo(*from, *to));
}
#endif  // !defined(QT_NO_VECTOR3D)

//  QQuaternion QQuaternion::slerp(const QQuaternion &q1, const QQuaternion
//      &q2, float t)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion5slerpERKS_S1_f(
    const QQuaternion *q1,
    const QQuaternion *q2,
    float t) {
  return new QQuaternion(QQuaternion::slerp(*q1, *q2, t));
}

//  QQuaternion QQuaternion::nlerp(const QQuaternion &q1, const QQuaternion
//      &q2, float t)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion5nlerpERKS_S1_f(
    const QQuaternion *q1,
    const QQuaternion *q2,
    float t) {
  return new QQuaternion(QQuaternion::nlerp(*q1, *q2, t));
}

//  QQuaternion::~QQuaternion()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QQuaternionD1Ev(QQuaternion *self) {
  delete self;
}

//  QList<QQuaternion>::QList()
extern "C" Q_DECL_EXPORT
QList<QQuaternion> *ritual_list_make_QQuaternion() {
  return new QList<QQuaternion>();
}

//  void QList<QQuaternion>::append(const QQuaternion &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QQuaternion(
    QList<QQuaternion> *self,
    const QQuaternion *element) {
  self->append(*element);
}

//  qsizetype QList<QQuaternion>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QQuaternion(const QList<QQuaternion> *self) {
  return self->size();
}

//  const QQuaternion &QList<QQuaternion>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_list_at_QQuaternion(
    const QList<QQuaternion> *self,
    long long index) {
  return new QQuaternion(self->at(index));
}

//  QList<QQuaternion>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QQuaternion(QList<QQuaternion> *self) {
  delete self;
}

//  a QMatrix3x3 a ritual of QQuaternion gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQuaternion__QMatrix3x3(QMatrix3x3 *self) {
  delete self;
}

//  static QQuaternion QQuaternion::fromEulerAngles(
//      QQuaternion::EulerAngles<float> angles)
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZN11QQuaternion15fromEulerAnglesENS_11EulerAnglesIfEE(
    const QQuaternion::EulerAngles<float> *angles) {
  return new QQuaternion(QQuaternion::fromEulerAngles(*angles));
}

#endif  // !defined(QT_NO_QUATERNION)
