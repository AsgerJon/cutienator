//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediatimerange.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qmediatimerange.h>

//  QMediaTimeRange::Interval::Interval()
extern "C" Q_DECL_EXPORT
QMediaTimeRange::Interval *ritual_ZN15QMediaTimeRange8IntervalC1Ev() {
  return new QMediaTimeRange::Interval();
}

//  QMediaTimeRange::Interval::Interval(qint64 start, qint64 end)
extern "C" Q_DECL_EXPORT
QMediaTimeRange::Interval *ritual_ZN15QMediaTimeRange8IntervalC1Exx(
    qint64 start,
    qint64 end) {
  return new QMediaTimeRange::Interval(start, end);
}

//  qint64 QMediaTimeRange::Interval::start() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QMediaTimeRange8Interval5startEv(
    const QMediaTimeRange::Interval *self) {
  return self->start();
}

//  qint64 QMediaTimeRange::Interval::end() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QMediaTimeRange8Interval3endEv(
    const QMediaTimeRange::Interval *self) {
  return self->end();
}

//  bool QMediaTimeRange::Interval::contains(qint64 time) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMediaTimeRange8Interval8containsEx(
    const QMediaTimeRange::Interval *self,
    qint64 time) {
  return self->contains(time);
}

//  bool QMediaTimeRange::Interval::isNormal() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMediaTimeRange8Interval8isNormalEv(
    const QMediaTimeRange::Interval *self) {
  return self->isNormal();
}

//  Interval QMediaTimeRange::Interval::normalized() const
extern "C" Q_DECL_EXPORT
QMediaTimeRange::Interval *ritual_ZNK15QMediaTimeRange8Interval10normalizedEv(
    const QMediaTimeRange::Interval *self) {
  return new QMediaTimeRange::Interval(self->normalized());
}

//  Interval QMediaTimeRange::Interval::translated(qint64 offset) const
extern "C" Q_DECL_EXPORT
QMediaTimeRange::Interval *ritual_ZNK15QMediaTimeRange8Interval10translatedEx(
    const QMediaTimeRange::Interval *self,
    qint64 offset) {
  return new QMediaTimeRange::Interval(self->translated(offset));
}

//  bool operator==(Interval lhs, Interval rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqN15QMediaTimeRange8IntervalES0_(
    const QMediaTimeRange::Interval *lhs,
    const QMediaTimeRange::Interval *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(Interval lhs, Interval rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneN15QMediaTimeRange8IntervalES0_(
    const QMediaTimeRange::Interval *lhs,
    const QMediaTimeRange::Interval *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QMediaTimeRange::Interval::~Interval()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange8IntervalD1Ev(
    QMediaTimeRange::Interval *self) {
  delete self;
}
