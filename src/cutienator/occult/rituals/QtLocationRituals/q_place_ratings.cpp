//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/qplaceratings.h, Qt 6.12.0. Changes made here are lost.
#include <QtLocation/qplaceratings.h>

//  QPlaceRatings::QPlaceRatings()
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_ZN13QPlaceRatingsC1Ev() {
  return new QPlaceRatings();
}

//  QPlaceRatings::QPlaceRatings(const QPlaceRatings &other)
extern "C" Q_DECL_EXPORT
QPlaceRatings *ritual_ZN13QPlaceRatingsC1ERKS_(const QPlaceRatings *other) {
  return new QPlaceRatings(*other);
}

//  QPlaceRatings::~QPlaceRatings()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceRatingsD1Ev(QPlaceRatings *self) {
  delete self;
}

//  bool operator==(const QPlaceRatings &lhs, const QPlaceRatings &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QPlaceRatingsS1_(
    const QPlaceRatings *lhs,
    const QPlaceRatings *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QPlaceRatings &lhs, const QPlaceRatings &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QPlaceRatingsS1_(
    const QPlaceRatings *lhs,
    const QPlaceRatings *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qreal QPlaceRatings::average() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPlaceRatings7averageEv(const QPlaceRatings *self) {
  return self->average();
}

//  void QPlaceRatings::setAverage(qreal average)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceRatings10setAverageEd(
    QPlaceRatings *self,
    qreal average) {
  self->setAverage(average);
}

//  int QPlaceRatings::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QPlaceRatings5countEv(const QPlaceRatings *self) {
  return self->count();
}

//  void QPlaceRatings::setCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceRatings8setCountEi(QPlaceRatings *self, int count) {
  self->setCount(count);
}

//  qreal QPlaceRatings::maximum() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK13QPlaceRatings7maximumEv(const QPlaceRatings *self) {
  return self->maximum();
}

//  void QPlaceRatings::setMaximum(qreal max)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QPlaceRatings10setMaximumEd(QPlaceRatings *self, qreal max) {
  self->setMaximum(max);
}

//  bool QPlaceRatings::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlaceRatings7isEmptyEv(const QPlaceRatings *self) {
  return self->isEmpty();
}

//  bool QPlaceRatings::isEqual(const QPlaceRatings &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QPlaceRatings7isEqualERKS_(
    const QPlaceRatings *self,
    const QPlaceRatings *other) {
  return self->isEqual(*other);
}
