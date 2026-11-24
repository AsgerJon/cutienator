//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfixed_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfixed_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QFixed::QFixed(int val, int a1)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixedC1Eii(int val, int a1) {
  return new QFixed(val, a1);
}

//  QFixed::QFixed()
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixedC1Ev() {
  return new QFixed();
}

//  QFixed::QFixed(int i)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixedC1Ei(int i) {
  return new QFixed(i);
}

//  QFixed::QFixed(long i)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixedC1El(long i) {
  return new QFixed(i);
}

//  QFixed::QFixed(long long i)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixedC1Ex(long long i) {
  return new QFixed(i);
}

//  QFixed QFixed::fromReal(qreal r)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixed8fromRealEd(qreal r) {
  return new QFixed(QFixed::fromReal(r));
}

//  QFixed QFixed::fromFixed(int fixed)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixed9fromFixedEi(int fixed) {
  return new QFixed(QFixed::fromFixed(fixed));
}

//  int QFixed::value() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFixed5valueEv(const QFixed *self) {
  return self->value();
}

//  void QFixed::setValue(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixed8setValueEi(QFixed *self, int value) {
  self->setValue(value);
}

//  int QFixed::toInt() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFixed5toIntEv(const QFixed *self) {
  return self->toInt();
}

//  qreal QFixed::toReal() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QFixed6toRealEv(const QFixed *self) {
  return self->toReal();
}

//  int QFixed::truncate() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QFixed8truncateEv(const QFixed *self) {
  return self->truncate();
}

//  QFixed QFixed::round() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixed5roundEv(const QFixed *self) {
  return new QFixed(self->round());
}

//  QFixed QFixed::floor() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixed5floorEv(const QFixed *self) {
  return new QFixed(self->floor());
}

//  QFixed QFixed::ceil() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixed4ceilEv(const QFixed *self) {
  return new QFixed(self->ceil());
}

//  QFixed QFixed::operator+(int i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedplEi(const QFixed *self, int i) {
  return new QFixed(self->operator+(i));
}

//  QFixed QFixed::operator+(uint i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedplEj(const QFixed *self, uint i) {
  return new QFixed(self->operator+(i));
}

//  QFixed QFixed::operator+(QFixed other) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedplES_(const QFixed *self, const QFixed *other) {
  return new QFixed(self->operator+(*other));
}

//  QFixed &QFixed::operator+=(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedpLEi(QFixed *self, int i) {
  self->operator+=(i);
}

//  QFixed &QFixed::operator+=(uint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedpLEj(QFixed *self, uint i) {
  self->operator+=(i);
}

//  QFixed &QFixed::operator+=(QFixed other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedpLES_(QFixed *self, const QFixed *other) {
  self->operator+=(*other);
}

//  QFixed QFixed::operator-(int i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmiEi(const QFixed *self, int i) {
  return new QFixed(self->operator-(i));
}

//  QFixed QFixed::operator-(uint i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmiEj(const QFixed *self, uint i) {
  return new QFixed(self->operator-(i));
}

//  QFixed QFixed::operator-(QFixed other) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmiES_(const QFixed *self, const QFixed *other) {
  return new QFixed(self->operator-(*other));
}

//  QFixed &QFixed::operator-=(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmIEi(QFixed *self, int i) {
  self->operator-=(i);
}

//  QFixed &QFixed::operator-=(uint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmIEj(QFixed *self, uint i) {
  self->operator-=(i);
}

//  QFixed &QFixed::operator-=(QFixed other)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmIES_(QFixed *self, const QFixed *other) {
  self->operator-=(*other);
}

//  QFixed QFixed::operator-() const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedngEv(const QFixed *self) {
  return new QFixed(self->operator-());
}

//  bool operator==(QFixed lhs, QFixed rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zeq6QFixedS_(const QFixed *lhs, const QFixed *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(QFixed lhs, QFixed rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zne6QFixedS_(const QFixed *lhs, const QFixed *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(QFixed lhs, QFixed rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zlt6QFixedS_(const QFixed *lhs, const QFixed *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(QFixed lhs, QFixed rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zgt6QFixedS_(const QFixed *lhs, const QFixed *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(QFixed lhs, QFixed rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zle6QFixedS_(const QFixed *lhs, const QFixed *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(QFixed lhs, QFixed rhs)
extern "C" Q_DECL_EXPORT
bool ritual_Zge6QFixedS_(const QFixed *lhs, const QFixed *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool QFixed::operator!() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QFixedntEv(const QFixed *self) {
  return self->operator!();
}

//  QFixed &QFixed::operator/=(int x)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixeddVEi(QFixed *self, int x) {
  self->operator/=(x);
}

//  QFixed &QFixed::operator/=(QFixed o)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixeddVES_(QFixed *self, const QFixed *o) {
  self->operator/=(*o);
}

//  QFixed QFixed::operator/(int d) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixeddvEi(const QFixed *self, int d) {
  return new QFixed(self->operator/(d));
}

//  QFixed QFixed::operator/(QFixed b) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixeddvES_(const QFixed *self, const QFixed *b) {
  return new QFixed(self->operator/(*b));
}

//  QFixed QFixed::operator>>(int d) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedrsEi(const QFixed *self, int d) {
  return new QFixed(self->operator>>(d));
}

//  QFixed &QFixed::operator*=(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmLEi(QFixed *self, int i) {
  self->operator*=(i);
}

//  QFixed &QFixed::operator*=(uint i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmLEj(QFixed *self, uint i) {
  self->operator*=(i);
}

//  QFixed &QFixed::operator*=(QFixed o)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmLES_(QFixed *self, const QFixed *o) {
  self->operator*=(*o);
}

//  QFixed QFixed::operator*(int i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmlEi(const QFixed *self, int i) {
  return new QFixed(self->operator*(i));
}

//  QFixed QFixed::operator*(uint i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmlEj(const QFixed *self, uint i) {
  return new QFixed(self->operator*(i));
}

//  QFixed QFixed::operator*(QFixed o) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmlES_(const QFixed *self, const QFixed *o) {
  return new QFixed(self->operator*(*o));
}

//  QFixed::QFixed(qreal i)
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZN6QFixedC1Ed(qreal i) {
  return new QFixed(i);
}

//  QFixed QFixed::operator+(qreal i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedplEd(const QFixed *self, qreal i) {
  return new QFixed(self->operator+(i));
}

//  QFixed &QFixed::operator+=(qreal i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedpLEd(QFixed *self, qreal i) {
  self->operator+=(i);
}

//  QFixed QFixed::operator-(qreal i) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmiEd(const QFixed *self, qreal i) {
  return new QFixed(self->operator-(i));
}

//  QFixed &QFixed::operator-=(qreal i)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmIEd(QFixed *self, qreal i) {
  self->operator-=(i);
}

//  QFixed &QFixed::operator/=(qreal r)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixeddVEd(QFixed *self, qreal r) {
  self->operator/=(r);
}

//  QFixed QFixed::operator/(qreal d) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixeddvEd(const QFixed *self, qreal d) {
  return new QFixed(self->operator/(d));
}

//  QFixed &QFixed::operator*=(qreal d)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedmLEd(QFixed *self, qreal d) {
  self->operator*=(d);
}

//  QFixed QFixed::operator*(qreal d) const
extern "C" Q_DECL_EXPORT
QFixed *ritual_ZNK6QFixedmlEd(const QFixed *self, qreal d) {
  return new QFixed(self->operator*(d));
}

//  QFixed::~QFixed()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QFixedD1Ev(QFixed *self) {
  delete self;
}
