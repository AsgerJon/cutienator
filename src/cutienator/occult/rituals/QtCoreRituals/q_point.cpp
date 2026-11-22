//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpoint.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpoint.h>

//  QPoint::QPoint()
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN6QPointC1Ev() {
  return new QPoint();
}

//  QPoint::QPoint(int xpos, int ypos)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN6QPointC1Eii(int xpos, int ypos) {
  return new QPoint(xpos, ypos);
}

//  bool QPoint::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QPoint6isNullEv(const QPoint *self) {
  return self->isNull();
}

//  int QPoint::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPoint1xEv(const QPoint *self) {
  return self->x();
}

//  int QPoint::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPoint1yEv(const QPoint *self) {
  return self->y();
}

//  void QPoint::setX(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPoint4setXEi(QPoint *self, int x) {
  self->setX(x);
}

//  void QPoint::setY(int y)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPoint4setYEi(QPoint *self, int y) {
  self->setY(y);
}

//  int QPoint::manhattanLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QPoint15manhattanLengthEv(const QPoint *self) {
  return self->manhattanLength();
}

//  QPoint QPoint::transposed() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK6QPoint10transposedEv(const QPoint *self) {
  return new QPoint(self->transposed());
}

//  QPoint &QPoint::operator+=(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointpLERKS_(QPoint *self, const QPoint *p) {
  self->operator+=(*p);
}

//  QPoint &QPoint::operator-=(const QPoint &p)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointmIERKS_(QPoint *self, const QPoint *p) {
  self->operator-=(*p);
}

//  QPoint &QPoint::operator*=(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointmLEf(QPoint *self, float factor) {
  self->operator*=(factor);
}

//  QPoint &QPoint::operator*=(double factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointmLEd(QPoint *self, double factor) {
  self->operator*=(factor);
}

//  QPoint &QPoint::operator*=(int factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointmLEi(QPoint *self, int factor) {
  self->operator*=(factor);
}

//  QPoint &QPoint::operator/=(qreal divisor)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointdVEd(QPoint *self, qreal divisor) {
  self->operator/=(divisor);
}

//  int QPoint::dotProduct(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
int ritual_ZN6QPoint10dotProductERKS_S1_(
    const QPoint *p1,
    const QPoint *p2) {
  return QPoint::dotProduct(*p1, *p2);
}

//  bool operator==(const QPoint &lhs, const QPoint &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QPointS1_(const QPoint *lhs, const QPoint *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPoint &lhs, const QPoint &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QPointS1_(const QPoint *lhs, const QPoint *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QPoint operator+(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZplRK6QPointS1_(const QPoint *p1, const QPoint *p2) {
  return new QPoint(operator+(*p1, *p2));
}

//  QPoint operator-(const QPoint &p1, const QPoint &p2)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmiRK6QPointS1_(const QPoint *p1, const QPoint *p2) {
  return new QPoint(operator-(*p1, *p2));
}

//  QPoint operator*(const QPoint &p, float factor)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK6QPointf(const QPoint *p, float factor) {
  return new QPoint(operator*(*p, factor));
}

//  QPoint operator*(const QPoint &p, double factor)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK6QPointd(const QPoint *p, double factor) {
  return new QPoint(operator*(*p, factor));
}

//  QPoint operator*(const QPoint &p, int factor)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlRK6QPointi(const QPoint *p, int factor) {
  return new QPoint(operator*(*p, factor));
}

//  QPoint operator*(float factor, const QPoint &p)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmlfRK6QPoint(float factor, const QPoint *p) {
  return new QPoint(operator*(factor, *p));
}

//  QPoint operator*(double factor, const QPoint &p)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmldRK6QPoint(double factor, const QPoint *p) {
  return new QPoint(operator*(factor, *p));
}

//  QPoint operator*(int factor, const QPoint &p)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZmliRK6QPoint(int factor, const QPoint *p) {
  return new QPoint(operator*(factor, *p));
}

//  QPoint operator+(const QPoint &p)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZpsRK6QPoint(const QPoint *p) {
  return new QPoint(operator+(*p));
}

//  QPoint operator-(const QPoint &p)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZngRK6QPoint(const QPoint *p) {
  return new QPoint(operator-(*p));
}

//  QPoint operator/(const QPoint &p, qreal c)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZdvRK6QPointd(const QPoint *p, qreal c) {
  return new QPoint(operator/(*p, c));
}

//  QPointF QPoint::toPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK6QPoint8toPointFEv(const QPoint *self) {
  return new QPointF(self->toPointF());
}

//  QPoint::~QPoint()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QPointD1Ev(QPoint *self) {
  delete self;
}
