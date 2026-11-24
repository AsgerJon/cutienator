//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  QDoubleVector2D::QDoubleVector2D()
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZN15QDoubleVector2DC1Ev() {
  return new QDoubleVector2D();
}

//  QDoubleVector2D::QDoubleVector2D(double xpos, double ypos)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZN15QDoubleVector2DC1Edd(double xpos, double ypos) {
  return new QDoubleVector2D(xpos, ypos);
}

//  QDoubleVector2D::QDoubleVector2D(const QPointF &p)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZN15QDoubleVector2DC1ERK7QPointF(const QPointF *p) {
  return new QDoubleVector2D(*p);
}

//  QDoubleVector2D::QDoubleVector2D(const QDoubleVector3D &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZN15QDoubleVector2DC1ERK15QDoubleVector3D(
    const QDoubleVector3D *vector) {
  return new QDoubleVector2D(*vector);
}

//  double QDoubleVector2D::manhattanLength() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector2D15manhattanLengthEv(
    const QDoubleVector2D *self) {
  return self->manhattanLength();
}

//  bool QDoubleVector2D::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDoubleVector2D6isNullEv(const QDoubleVector2D *self) {
  return self->isNull();
}

//  bool QDoubleVector2D::isFinite() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QDoubleVector2D8isFiniteEv(const QDoubleVector2D *self) {
  return self->isFinite();
}

//  double QDoubleVector2D::x() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector2D1xEv(const QDoubleVector2D *self) {
  return self->x();
}

//  double QDoubleVector2D::y() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector2D1yEv(const QDoubleVector2D *self) {
  return self->y();
}

//  void QDoubleVector2D::setX(double x)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2D4setXEd(QDoubleVector2D *self, double x) {
  self->setX(x);
}

//  void QDoubleVector2D::setY(double y)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2D4setYEd(QDoubleVector2D *self, double y) {
  self->setY(y);
}

//  double QDoubleVector2D::length() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector2D6lengthEv(const QDoubleVector2D *self) {
  return self->length();
}

//  double QDoubleVector2D::lengthSquared() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK15QDoubleVector2D13lengthSquaredEv(
    const QDoubleVector2D *self) {
  return self->lengthSquared();
}

//  QDoubleVector2D QDoubleVector2D::normalized() const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK15QDoubleVector2D10normalizedEv(
    const QDoubleVector2D *self) {
  return new QDoubleVector2D(self->normalized());
}

//  void QDoubleVector2D::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2D9normalizeEv(QDoubleVector2D *self) {
  self->normalize();
}

//  QDoubleVector2D &QDoubleVector2D::operator+=(const QDoubleVector2D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DpLERKS_(
    QDoubleVector2D *self,
    const QDoubleVector2D *vector) {
  self->operator+=(*vector);
}

//  QDoubleVector2D &QDoubleVector2D::operator-=(const QDoubleVector2D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DmIERKS_(
    QDoubleVector2D *self,
    const QDoubleVector2D *vector) {
  self->operator-=(*vector);
}

//  QDoubleVector2D &QDoubleVector2D::operator*=(double factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DmLEd(QDoubleVector2D *self, double factor) {
  self->operator*=(factor);
}

//  QDoubleVector2D &QDoubleVector2D::operator*=(const QDoubleVector2D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DmLERKS_(
    QDoubleVector2D *self,
    const QDoubleVector2D *vector) {
  self->operator*=(*vector);
}

//  QDoubleVector2D &QDoubleVector2D::operator/=(double divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DdVEd(QDoubleVector2D *self, double divisor) {
  self->operator/=(divisor);
}

//  QDoubleVector2D &QDoubleVector2D::operator/=(const QDoubleVector2D
//      &vector)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DdVERKS_(
    QDoubleVector2D *self,
    const QDoubleVector2D *vector) {
  self->operator/=(*vector);
}

//  double QDoubleVector2D::dotProduct(const QDoubleVector2D &v1, const
//      QDoubleVector2D &v2)
extern "C" Q_DECL_EXPORT
double ritual_ZN15QDoubleVector2D10dotProductERKS_S1_(
    const QDoubleVector2D *v1,
    const QDoubleVector2D *v2) {
  return QDoubleVector2D::dotProduct(*v1, *v2);
}

//  bool operator==(const QDoubleVector2D &v1, const QDoubleVector2D &v2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QDoubleVector2DS1_(
    const QDoubleVector2D *v1,
    const QDoubleVector2D *v2) {
  return operator==(*v1, *v2);
}

//  bool operator!=(const QDoubleVector2D &v1, const QDoubleVector2D &v2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QDoubleVector2DS1_(
    const QDoubleVector2D *v1,
    const QDoubleVector2D *v2) {
  return operator!=(*v1, *v2);
}

//  const QDoubleVector2D operator+(const QDoubleVector2D &v1, const
//      QDoubleVector2D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZplRK15QDoubleVector2DS1_(
    const QDoubleVector2D *v1,
    const QDoubleVector2D *v2) {
  return new QDoubleVector2D(operator+(*v1, *v2));
}

//  const QDoubleVector2D operator-(const QDoubleVector2D &v1, const
//      QDoubleVector2D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZmiRK15QDoubleVector2DS1_(
    const QDoubleVector2D *v1,
    const QDoubleVector2D *v2) {
  return new QDoubleVector2D(operator-(*v1, *v2));
}

//  const QDoubleVector2D operator*(double factor, const QDoubleVector2D
//      &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZmldRK15QDoubleVector2D(
    double factor,
    const QDoubleVector2D *vector) {
  return new QDoubleVector2D(operator*(factor, *vector));
}

//  const QDoubleVector2D operator*(const QDoubleVector2D &vector, double
//      factor)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZmlRK15QDoubleVector2Dd(
    const QDoubleVector2D *vector,
    double factor) {
  return new QDoubleVector2D(operator*(*vector, factor));
}

//  const QDoubleVector2D operator*(const QDoubleVector2D &v1, const
//      QDoubleVector2D &v2)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZmlRK15QDoubleVector2DS1_(
    const QDoubleVector2D *v1,
    const QDoubleVector2D *v2) {
  return new QDoubleVector2D(operator*(*v1, *v2));
}

//  const QDoubleVector2D operator-(const QDoubleVector2D &vector)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZngRK15QDoubleVector2D(
    const QDoubleVector2D *vector) {
  return new QDoubleVector2D(operator-(*vector));
}

//  const QDoubleVector2D operator/(const QDoubleVector2D &vector, double
//      divisor)
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZdvRK15QDoubleVector2Dd(
    const QDoubleVector2D *vector,
    double divisor) {
  return new QDoubleVector2D(operator/(*vector, divisor));
}

//  QDoubleVector3D QDoubleVector2D::toVector3D() const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK15QDoubleVector2D10toVector3DEv(
    const QDoubleVector2D *self) {
  return new QDoubleVector3D(self->toVector3D());
}

//  QPointF QDoubleVector2D::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK15QDoubleVector2D8toPointFEv(
    const QDoubleVector2D *self) {
  return new QPointF(self->toPointF());
}

//  QDoubleVector2D::~QDoubleVector2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QDoubleVector2DD1Ev(QDoubleVector2D *self) {
  delete self;
}

//  QList<QDoubleVector2D>::QList()
extern "C" Q_DECL_EXPORT
QList<QDoubleVector2D> *ritual_list_make_QDoubleVector2D() {
  return new QList<QDoubleVector2D>();
}

//  void QList<QDoubleVector2D>::append(const QDoubleVector2D &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QDoubleVector2D(
    QList<QDoubleVector2D> *self,
    const QDoubleVector2D *element) {
  self->append(*element);
}

//  qsizetype QList<QDoubleVector2D>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QDoubleVector2D(
    const QList<QDoubleVector2D> *self) {
  return self->size();
}

//  const QDoubleVector2D &QList<QDoubleVector2D>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_list_at_QDoubleVector2D(
    const QList<QDoubleVector2D> *self,
    long long index) {
  return new QDoubleVector2D(self->at(index));
}

//  QList<QDoubleVector2D>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QDoubleVector2D(QList<QDoubleVector2D> *self) {
  delete self;
}
