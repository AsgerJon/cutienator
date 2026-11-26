//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmargins.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmargins.h>
#include <QtCore/QMargins>

//  QMargins::QMargins()
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZN8QMarginsC1Ev() {
  return new QMargins();
}

//  QMargins::QMargins(int left, int top, int right, int bottom)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZN8QMarginsC1Eiiii(
    int left,
    int top,
    int right,
    int bottom) {
  return new QMargins(left, top, right, bottom);
}

//  bool QMargins::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QMargins6isNullEv(const QMargins *self) {
  return self->isNull();
}

//  int QMargins::left() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins4leftEv(const QMargins *self) {
  return self->left();
}

//  int QMargins::top() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins3topEv(const QMargins *self) {
  return self->top();
}

//  int QMargins::right() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins5rightEv(const QMargins *self) {
  return self->right();
}

//  int QMargins::bottom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QMargins6bottomEv(const QMargins *self) {
  return self->bottom();
}

//  void QMargins::setLeft(int left)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins7setLeftEi(QMargins *self, int left) {
  self->setLeft(left);
}

//  void QMargins::setTop(int top)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins6setTopEi(QMargins *self, int top) {
  self->setTop(top);
}

//  void QMargins::setRight(int right)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins8setRightEi(QMargins *self, int right) {
  self->setRight(right);
}

//  void QMargins::setBottom(int bottom)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMargins9setBottomEi(QMargins *self, int bottom) {
  self->setBottom(bottom);
}

//  QMargins &QMargins::operator+=(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginspLERKS_(QMargins *self, const QMargins *margins) {
  self->operator+=(*margins);
}

//  QMargins &QMargins::operator-=(const QMargins &margins)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsmIERKS_(QMargins *self, const QMargins *margins) {
  self->operator-=(*margins);
}

//  QMargins &QMargins::operator+=(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginspLEi(QMargins *self, int a0) {
  self->operator+=(a0);
}

//  QMargins &QMargins::operator-=(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsmIEi(QMargins *self, int a0) {
  self->operator-=(a0);
}

//  QMargins &QMargins::operator*=(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsmLEi(QMargins *self, int a0) {
  self->operator*=(a0);
}

//  QMargins &QMargins::operator/=(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsdVEi(QMargins *self, int a0) {
  self->operator/=(a0);
}

//  QMargins &QMargins::operator*=(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsmLEd(QMargins *self, qreal a0) {
  self->operator*=(a0);
}

//  QMargins &QMargins::operator/=(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsdVEd(QMargins *self, qreal a0) {
  self->operator/=(a0);
}

//  QMarginsF QMargins::toMarginsF() const
extern "C" Q_DECL_EXPORT
QMarginsF *ritual_ZNK8QMargins10toMarginsFEv(const QMargins *self) {
  return new QMarginsF(self->toMarginsF());
}

//  QMargins operator+(const QMargins &m1, const QMargins &m2)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZplRK8QMarginsS1_(const QMargins *m1, const QMargins *m2) {
  return new QMargins(operator+(*m1, *m2));
}

//  QMargins operator-(const QMargins &m1, const QMargins &m2)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZmiRK8QMarginsS1_(const QMargins *m1, const QMargins *m2) {
  return new QMargins(operator-(*m1, *m2));
}

//  QMargins operator+(const QMargins &lhs, int rhs)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZplRK8QMarginsi(const QMargins *lhs, int rhs) {
  return new QMargins(operator+(*lhs, rhs));
}

//  QMargins operator+(int lhs, const QMargins &rhs)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZpliRK8QMargins(int lhs, const QMargins *rhs) {
  return new QMargins(operator+(lhs, *rhs));
}

//  QMargins operator-(const QMargins &lhs, int rhs)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZmiRK8QMarginsi(const QMargins *lhs, int rhs) {
  return new QMargins(operator-(*lhs, rhs));
}

//  QMargins operator*(const QMargins &margins, int factor)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZmlRK8QMarginsi(const QMargins *margins, int factor) {
  return new QMargins(operator*(*margins, factor));
}

//  QMargins operator*(int factor, const QMargins &margins)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZmliRK8QMargins(int factor, const QMargins *margins) {
  return new QMargins(operator*(factor, *margins));
}

//  QMargins operator*(const QMargins &margins, qreal factor)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZmlRK8QMarginsd(const QMargins *margins, qreal factor) {
  return new QMargins(operator*(*margins, factor));
}

//  QMargins operator*(qreal factor, const QMargins &margins)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZmldRK8QMargins(qreal factor, const QMargins *margins) {
  return new QMargins(operator*(factor, *margins));
}

//  QMargins operator/(const QMargins &margins, int divisor)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZdvRK8QMarginsi(const QMargins *margins, int divisor) {
  return new QMargins(operator/(*margins, divisor));
}

//  QMargins operator/(const QMargins &margins, qreal divisor)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZdvRK8QMarginsd(const QMargins *margins, qreal divisor) {
  return new QMargins(operator/(*margins, divisor));
}

//  QMargins operator|(const QMargins &m1, const QMargins &m2)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZorRK8QMarginsS1_(const QMargins *m1, const QMargins *m2) {
  return new QMargins(operator|(*m1, *m2));
}

//  QMargins::QMargins(Representation left, Representation top,
//      Representation right, Representation bottom)
extern "C" Q_DECL_EXPORT
QMargins *ritual_ZN8QMarginsC1EN9QtPrivate16QCheckedIntegers11QCheckedIntIiNS1_13SafeCheckImplIiEENS1_18AssertReportPolicyEEES6_S6_S6_(
    const QMargins::Representation *left,
    const QMargins::Representation *top,
    const QMargins::Representation *right,
    const QMargins::Representation *bottom) {
  return new QMargins(*left, *top, *right, *bottom);
}

//  bool operator==(const QMargins &lhs, const QMargins &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK8QMarginsS1_(const QMargins *lhs, const QMargins *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMargins &lhs, const QMargins &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK8QMarginsS1_(const QMargins *lhs, const QMargins *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QMargins::~QMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QMarginsD1Ev(QMargins *self) {
  delete self;
}
