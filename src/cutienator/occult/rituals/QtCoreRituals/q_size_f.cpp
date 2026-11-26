//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsize.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  rituals for functions the generator leaves out: 2. Kept as it is when the
//  generator runs again.
#include <QtCore/qsize.h>
#include <QtCore/qmargins.h>

//  QSizeF::QSizeF()
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN6QSizeFC1Ev() {
  return new QSizeF();
}

//  QSizeF::QSizeF(const QSize &sz)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN6QSizeFC1ERK5QSize(const QSize *sz) {
  return new QSizeF(*sz);
}

//  QSizeF::QSizeF(qreal w, qreal h)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZN6QSizeFC1Edd(qreal w, qreal h) {
  return new QSizeF(w, h);
}

//  bool QSizeF::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QSizeF6isNullEv(const QSizeF *self) {
  return self->isNull();
}

//  bool QSizeF::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QSizeF7isEmptyEv(const QSizeF *self) {
  return self->isEmpty();
}

//  bool QSizeF::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QSizeF7isValidEv(const QSizeF *self) {
  return self->isValid();
}

//  qreal QSizeF::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QSizeF5widthEv(const QSizeF *self) {
  return self->width();
}

//  qreal QSizeF::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK6QSizeF6heightEv(const QSizeF *self) {
  return self->height();
}

//  void QSizeF::setWidth(qreal w)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeF8setWidthEd(QSizeF *self, qreal w) {
  self->setWidth(w);
}

//  void QSizeF::setHeight(qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeF9setHeightEd(QSizeF *self, qreal h) {
  self->setHeight(h);
}

//  void QSizeF::transpose()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeF9transposeEv(QSizeF *self) {
  self->transpose();
}

//  QSizeF QSizeF::transposed() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF10transposedEv(const QSizeF *self) {
  return new QSizeF(self->transposed());
}

//  void QSizeF::scale(qreal w, qreal h, Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeF5scaleEddN2Qt15AspectRatioModeE(
    QSizeF *self,
    qreal w,
    qreal h,
    Qt::AspectRatioMode mode) {
  self->scale(w, h, mode);
}

//  void QSizeF::scale(const QSizeF &s, Qt::AspectRatioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeF5scaleERKS_N2Qt15AspectRatioModeE(
    QSizeF *self,
    const QSizeF *s,
    Qt::AspectRatioMode mode) {
  self->scale(*s, mode);
}

//  QSizeF QSizeF::scaled(qreal w, qreal h, Qt::AspectRatioMode mode) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF6scaledEddN2Qt15AspectRatioModeE(
    const QSizeF *self,
    qreal w,
    qreal h,
    Qt::AspectRatioMode mode) {
  return new QSizeF(self->scaled(w, h, mode));
}

//  QSizeF QSizeF::scaled(const QSizeF &s, Qt::AspectRatioMode mode) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF6scaledERKS_N2Qt15AspectRatioModeE(
    const QSizeF *self,
    const QSizeF *s,
    Qt::AspectRatioMode mode) {
  return new QSizeF(self->scaled(*s, mode));
}

//  QSizeF QSizeF::expandedTo(const QSizeF &a0) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF10expandedToERKS_(
    const QSizeF *self,
    const QSizeF *a0) {
  return new QSizeF(self->expandedTo(*a0));
}

//  QSizeF QSizeF::boundedTo(const QSizeF &a0) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF9boundedToERKS_(
    const QSizeF *self,
    const QSizeF *a0) {
  return new QSizeF(self->boundedTo(*a0));
}

//  QSizeF QSizeF::grownBy(QMarginsF m) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF7grownByE9QMarginsF(
    const QSizeF *self,
    const QMarginsF *m) {
  return new QSizeF(self->grownBy(*m));
}

//  QSizeF QSizeF::shrunkBy(QMarginsF m) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK6QSizeF8shrunkByE9QMarginsF(
    const QSizeF *self,
    const QMarginsF *m) {
  return new QSizeF(self->shrunkBy(*m));
}

//  QSizeF &QSizeF::operator+=(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeFpLERKS_(QSizeF *self, const QSizeF *a0) {
  self->operator+=(*a0);
}

//  QSizeF &QSizeF::operator-=(const QSizeF &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeFmIERKS_(QSizeF *self, const QSizeF *a0) {
  self->operator-=(*a0);
}

//  QSizeF &QSizeF::operator*=(qreal c)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeFmLEd(QSizeF *self, qreal c) {
  self->operator*=(c);
}

//  QSizeF &QSizeF::operator/=(qreal c)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeFdVEd(QSizeF *self, qreal c) {
  self->operator/=(c);
}

//  bool operator==(const QSizeF &lhs, const QSizeF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QSizeFS1_(const QSizeF *lhs, const QSizeF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSizeF &lhs, const QSizeF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QSizeFS1_(const QSizeF *lhs, const QSizeF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QSizeF &lhs, const QSize &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK6QSizeFRK5QSize(const QSizeF *lhs, const QSize *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSizeF &lhs, const QSize &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK6QSizeFRK5QSize(const QSizeF *lhs, const QSize *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator==(const QSize &lhs, const QSizeF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK5QSizeRK6QSizeF(const QSize *lhs, const QSizeF *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QSize &lhs, const QSizeF &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK5QSizeRK6QSizeF(const QSize *lhs, const QSizeF *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QSizeF operator+(const QSizeF &s1, const QSizeF &s2)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZplRK6QSizeFS1_(const QSizeF *s1, const QSizeF *s2) {
  return new QSizeF(operator+(*s1, *s2));
}

//  QSizeF operator-(const QSizeF &s1, const QSizeF &s2)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZmiRK6QSizeFS1_(const QSizeF *s1, const QSizeF *s2) {
  return new QSizeF(operator-(*s1, *s2));
}

//  QSizeF operator*(const QSizeF &s, qreal c)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZmlRK6QSizeFd(const QSizeF *s, qreal c) {
  return new QSizeF(operator*(*s, c));
}

//  QSizeF operator*(qreal c, const QSizeF &s)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZmldRK6QSizeF(qreal c, const QSizeF *s) {
  return new QSizeF(operator*(c, *s));
}

//  QSizeF operator/(const QSizeF &s, qreal c)
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZdvRK6QSizeFd(const QSizeF *s, qreal c) {
  return new QSizeF(operator/(*s, c));
}

//  QSize QSizeF::toSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK6QSizeF6toSizeEv(const QSizeF *self) {
  return new QSize(self->toSize());
}

//  QSizeF::~QSizeF()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QSizeFD1Ev(QSizeF *self) {
  delete self;
}

//  qreal &QSizeF::rwidth()
extern "C" Q_DECL_EXPORT
qreal *ritual_ZN6QSizeF6rwidthEv(
    QSizeF *self) {
  return &(self->rwidth());
}

//  qreal &QSizeF::rheight()
extern "C" Q_DECL_EXPORT
qreal *ritual_ZN6QSizeF7rheightEv(
    QSizeF *self) {
  return &(self->rheight());
}
