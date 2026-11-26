//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-25: took out the two-argument distanceToPlane,
//  which the header declares and Qt's source never defines, and its row.
//  Kept as it is when the generator runs again.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QDoubleVector3D::QDoubleVector3D()
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3DC1Ev() {
  return new QDoubleVector3D();
}

//  QDoubleVector3D::QDoubleVector3D(double xpos, double ypos, double zpos)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3DC1Eddd(
    double xpos,
    double ypos,
    double zpos) {
  return new QDoubleVector3D(xpos, ypos, zpos);
}

//  QDoubleVector3D::QDoubleVector3D(const QDoubleVector2D &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3DC1ERK15QDoubleVector2D(
    const QDoubleVector2D *vector) {
  return new QDoubleVector3D(*vector);
}

//  QDoubleVector3D::QDoubleVector3D(const QDoubleVector2D &vector, double
//      zpos)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3DC1ERK15QDoubleVector2Dd(
    const QDoubleVector2D *vector,
    double zpos) {
  return new QDoubleVector3D(*vector, zpos);
}

//  bool QDoubleVector3D::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDoubleVector3D6isNullEv(const QDoubleVector3D *self) {
  return self->isNull();
}

//  double QDoubleVector3D::x() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D1xEv(const QDoubleVector3D *self) {
  return self->x();
}

//  double QDoubleVector3D::y() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D1yEv(const QDoubleVector3D *self) {
  return self->y();
}

//  double QDoubleVector3D::z() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D1zEv(const QDoubleVector3D *self) {
  return self->z();
}

//  void QDoubleVector3D::setX(double x)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3D4setXEd(QDoubleVector3D *self, double x) {
  self->setX(x);
}

//  void QDoubleVector3D::setY(double y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3D4setYEd(QDoubleVector3D *self, double y) {
  self->setY(y);
}

//  void QDoubleVector3D::setZ(double z)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3D4setZEd(QDoubleVector3D *self, double z) {
  self->setZ(z);
}

//  double QDoubleVector3D::get(int i) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D3getEi(
    const QDoubleVector3D *self,
    int i) {
  return self->get(i);
}

//  void QDoubleVector3D::set(int i, double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3D3setEid(
    QDoubleVector3D *self,
    int i,
    double value) {
  self->set(i, value);
}

//  double QDoubleVector3D::length() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D6lengthEv(const QDoubleVector3D *self) {
  return self->length();
}

//  double QDoubleVector3D::lengthSquared() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D13lengthSquaredEv(
    const QDoubleVector3D *self) {
  return self->lengthSquared();
}

//  QDoubleVector3D QDoubleVector3D::normalized() const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK15QDoubleVector3D10normalizedEv(
    const QDoubleVector3D *self) {
  return new QDoubleVector3D(self->normalized());
}

//  void QDoubleVector3D::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3D9normalizeEv(QDoubleVector3D *self) {
  self->normalize();
}

//  QDoubleVector3D &QDoubleVector3D::operator+=(const QDoubleVector3D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3DpLERKS_(
    QDoubleVector3D *self,
    const QDoubleVector3D *vector) {
  self->operator+=(*vector);
}

//  QDoubleVector3D &QDoubleVector3D::operator-=(const QDoubleVector3D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3DmIERKS_(
    QDoubleVector3D *self,
    const QDoubleVector3D *vector) {
  self->operator-=(*vector);
}

//  QDoubleVector3D &QDoubleVector3D::operator*=(double factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3DmLEd(QDoubleVector3D *self, double factor) {
  self->operator*=(factor);
}

//  QDoubleVector3D &QDoubleVector3D::operator*=(const QDoubleVector3D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3DmLERKS_(
    QDoubleVector3D *self,
    const QDoubleVector3D *vector) {
  self->operator*=(*vector);
}

//  QDoubleVector3D &QDoubleVector3D::operator/=(double divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3DdVEd(QDoubleVector3D *self, double divisor) {
  self->operator/=(divisor);
}

//  double QDoubleVector3D::dotProduct(const QDoubleVector3D &v1, const
//      QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
double ritual_ZN15QDoubleVector3D10dotProductERKS_S1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return QDoubleVector3D::dotProduct(*v1, *v2);
}

//  QDoubleVector3D QDoubleVector3D::crossProduct(const QDoubleVector3D &v1,
//      const QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3D12crossProductERKS_S1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return new QDoubleVector3D(QDoubleVector3D::crossProduct(*v1, *v2));
}

//  QDoubleVector3D QDoubleVector3D::normal(const QDoubleVector3D &v1, const
//      QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3D6normalERKS_S1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return new QDoubleVector3D(QDoubleVector3D::normal(*v1, *v2));
}

//  QDoubleVector3D QDoubleVector3D::normal(const QDoubleVector3D &v1, const
//      QDoubleVector3D &v2, const QDoubleVector3D &v3)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZN15QDoubleVector3D6normalERKS_S1_S1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2,
    const QDoubleVector3D *v3) {
  return new QDoubleVector3D(QDoubleVector3D::normal(*v1, *v2, *v3));
}

//  double QDoubleVector3D::distanceToPlane(const QDoubleVector3D &plane1,
//      const QDoubleVector3D &plane2, const QDoubleVector3D &plane3) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D15distanceToPlaneERKS_S1_S1_(
    const QDoubleVector3D *self,
    const QDoubleVector3D *plane1,
    const QDoubleVector3D *plane2,
    const QDoubleVector3D *plane3) {
  return self->distanceToPlane(*plane1, *plane2, *plane3);
}

//  double QDoubleVector3D::distanceToLine(const QDoubleVector3D &point,
//      const QDoubleVector3D &direction) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector3D14distanceToLineERKS_S1_(
    const QDoubleVector3D *self,
    const QDoubleVector3D *point,
    const QDoubleVector3D *direction) {
  return self->distanceToLine(*point, *direction);
}

//  bool operator==(const QDoubleVector3D &v1, const QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QDoubleVector3DS1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return operator==(*v1, *v2);
}

//  bool operator!=(const QDoubleVector3D &v1, const QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QDoubleVector3DS1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return operator!=(*v1, *v2);
}

//  const QDoubleVector3D operator+(const QDoubleVector3D &v1, const
//      QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZplRK15QDoubleVector3DS1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return new QDoubleVector3D(operator+(*v1, *v2));
}

//  const QDoubleVector3D operator-(const QDoubleVector3D &v1, const
//      QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZmiRK15QDoubleVector3DS1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return new QDoubleVector3D(operator-(*v1, *v2));
}

//  const QDoubleVector3D operator*(double factor, const QDoubleVector3D
//      &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZmldRK15QDoubleVector3D(
    double factor,
    const QDoubleVector3D *vector) {
  return new QDoubleVector3D(operator*(factor, *vector));
}

//  const QDoubleVector3D operator*(const QDoubleVector3D &vector, double
//      factor)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZmlRK15QDoubleVector3Dd(
    const QDoubleVector3D *vector,
    double factor) {
  return new QDoubleVector3D(operator*(*vector, factor));
}

//  const QDoubleVector3D operator*(const QDoubleVector3D &v1, const
//      QDoubleVector3D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZmlRK15QDoubleVector3DS1_(
    const QDoubleVector3D *v1,
    const QDoubleVector3D *v2) {
  return new QDoubleVector3D(operator*(*v1, *v2));
}

//  const QDoubleVector3D operator-(const QDoubleVector3D &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZngRK15QDoubleVector3D(
    const QDoubleVector3D *vector) {
  return new QDoubleVector3D(operator-(*vector));
}

//  const QDoubleVector3D operator/(const QDoubleVector3D &vector, double
//      divisor)
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZdvRK15QDoubleVector3Dd(
    const QDoubleVector3D *vector,
    double divisor) {
  return new QDoubleVector3D(operator/(*vector, divisor));
}

//  QDoubleVector2D QDoubleVector3D::toVector2D() const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK15QDoubleVector3D10toVector2DEv(
    const QDoubleVector3D *self) {
  return new QDoubleVector2D(self->toVector2D());
}

//  QDoubleVector3D::~QDoubleVector3D()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector3DD1Ev(QDoubleVector3D *self) {
  delete self;
}

//  QList<QDoubleVector3D>::QList()
extern "C" Q_DECL_EXPORT
QList<QDoubleVector3D> *ritual_list_make_QDoubleVector3D() {
  return new QList<QDoubleVector3D>();
}

//  void QList<QDoubleVector3D>::append(const QDoubleVector3D &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDoubleVector3D(
    QList<QDoubleVector3D> *self,
    const QDoubleVector3D *element) {
  self->append(*element);
}

//  qsizetype QList<QDoubleVector3D>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDoubleVector3D(
    const QList<QDoubleVector3D> *self) {
  return self->size();
}

//  const QDoubleVector3D &QList<QDoubleVector3D>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_list_at_QDoubleVector3D(
    const QList<QDoubleVector3D> *self,
    long long index) {
  return new QDoubleVector3D(self->at(index));
}

//  QList<QDoubleVector3D>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDoubleVector3D(QList<QDoubleVector3D> *self) {
  delete self;
}
