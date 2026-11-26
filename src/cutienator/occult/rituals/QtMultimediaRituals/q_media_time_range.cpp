//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/qmediatimerange.h, Qt 6.12.0. Changes made here are lost.
#include <QtMultimedia/qmediatimerange.h>
#include <QtCore/QList>
#include <QtMultimedia/QMediaTimeRange>

//  QMediaTimeRange::QMediaTimeRange()
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeC1Ev() {
  return new QMediaTimeRange();
}

//  QMediaTimeRange::QMediaTimeRange(qint64 start, qint64 end)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeC1Exx(qint64 start, qint64 end) {
  return new QMediaTimeRange(start, end);
}

//  QMediaTimeRange::QMediaTimeRange(const Interval &a0)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeC1ERKNS_8IntervalE(
    const QMediaTimeRange::Interval *a0) {
  return new QMediaTimeRange(*a0);
}

//  QMediaTimeRange::QMediaTimeRange(const QMediaTimeRange &range)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeC1ERKS_(
    const QMediaTimeRange *range) {
  return new QMediaTimeRange(*range);
}

//  QMediaTimeRange::~QMediaTimeRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRangeD1Ev(QMediaTimeRange *self) {
  delete self;
}

//  QMediaTimeRange &QMediaTimeRange::operator=(const QMediaTimeRange &a0)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeaSERKS_(
    QMediaTimeRange *self,
    const QMediaTimeRange *a0) {
  return &(self->operator=(*a0));
}

//  QMediaTimeRange::QMediaTimeRange(QMediaTimeRange &&other)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeC1EOS_(QMediaTimeRange *other) {
  return new QMediaTimeRange(std::move(*other));
}

//  QMediaTimeRange &QMediaTimeRange::operator=(QMediaTimeRange &&other)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeaSEOS_(
    QMediaTimeRange *self,
    QMediaTimeRange *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QMediaTimeRange::swap(QMediaTimeRange &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange4swapERS_(
    QMediaTimeRange *self,
    QMediaTimeRange *other) {
  self->swap(*other);
}

//  void QMediaTimeRange::detach()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange6detachEv(QMediaTimeRange *self) {
  self->detach();
}

//  QMediaTimeRange &QMediaTimeRange::operator=(const Interval &a0)
extern "C" Q_DECL_EXPORT
QMediaTimeRange *ritual_ZN15QMediaTimeRangeaSERKNS_8IntervalE(
    QMediaTimeRange *self,
    const QMediaTimeRange::Interval *a0) {
  return &(self->operator=(*a0));
}

//  qint64 QMediaTimeRange::earliestTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QMediaTimeRange12earliestTimeEv(
    const QMediaTimeRange *self) {
  return self->earliestTime();
}

//  qint64 QMediaTimeRange::latestTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QMediaTimeRange10latestTimeEv(
    const QMediaTimeRange *self) {
  return self->latestTime();
}

//  QList<QMediaTimeRange::Interval> QMediaTimeRange::intervals() const
extern "C" Q_DECL_EXPORT
QList<QMediaTimeRange::Interval> *ritual_ZNK15QMediaTimeRange9intervalsEv(
    const QMediaTimeRange *self) {
  return new QList<QMediaTimeRange::Interval>(self->intervals());
}

//  bool QMediaTimeRange::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMediaTimeRange7isEmptyEv(const QMediaTimeRange *self) {
  return self->isEmpty();
}

//  bool QMediaTimeRange::isContinuous() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMediaTimeRange12isContinuousEv(
    const QMediaTimeRange *self) {
  return self->isContinuous();
}

//  bool QMediaTimeRange::contains(qint64 time) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QMediaTimeRange8containsEx(
    const QMediaTimeRange *self,
    qint64 time) {
  return self->contains(time);
}

//  void QMediaTimeRange::addInterval(qint64 start, qint64 end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange11addIntervalExx(
    QMediaTimeRange *self,
    qint64 start,
    qint64 end) {
  self->addInterval(start, end);
}

//  void QMediaTimeRange::addInterval(const Interval &interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange11addIntervalERKNS_8IntervalE(
    QMediaTimeRange *self,
    const QMediaTimeRange::Interval *interval) {
  self->addInterval(*interval);
}

//  void QMediaTimeRange::addTimeRange(const QMediaTimeRange &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange12addTimeRangeERKS_(
    QMediaTimeRange *self,
    const QMediaTimeRange *a0) {
  self->addTimeRange(*a0);
}

//  void QMediaTimeRange::removeInterval(qint64 start, qint64 end)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange14removeIntervalExx(
    QMediaTimeRange *self,
    qint64 start,
    qint64 end) {
  self->removeInterval(start, end);
}

//  void QMediaTimeRange::removeInterval(const Interval &interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange14removeIntervalERKNS_8IntervalE(
    QMediaTimeRange *self,
    const QMediaTimeRange::Interval *interval) {
  self->removeInterval(*interval);
}

//  void QMediaTimeRange::removeTimeRange(const QMediaTimeRange &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange15removeTimeRangeERKS_(
    QMediaTimeRange *self,
    const QMediaTimeRange *a0) {
  self->removeTimeRange(*a0);
}

//  QMediaTimeRange &QMediaTimeRange::operator+=(const QMediaTimeRange &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRangepLERKS_(
    QMediaTimeRange *self,
    const QMediaTimeRange *a0) {
  self->operator+=(*a0);
}

//  QMediaTimeRange &QMediaTimeRange::operator+=(const Interval &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRangepLERKNS_8IntervalE(
    QMediaTimeRange *self,
    const QMediaTimeRange::Interval *a0) {
  self->operator+=(*a0);
}

//  QMediaTimeRange &QMediaTimeRange::operator-=(const QMediaTimeRange &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRangemIERKS_(
    QMediaTimeRange *self,
    const QMediaTimeRange *a0) {
  self->operator-=(*a0);
}

//  QMediaTimeRange &QMediaTimeRange::operator-=(const Interval &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRangemIERKNS_8IntervalE(
    QMediaTimeRange *self,
    const QMediaTimeRange::Interval *a0) {
  self->operator-=(*a0);
}

//  void QMediaTimeRange::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QMediaTimeRange5clearEv(QMediaTimeRange *self) {
  self->clear();
}

//  bool operator==(const QMediaTimeRange &lhs, const QMediaTimeRange &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QMediaTimeRangeS1_(
    const QMediaTimeRange *lhs,
    const QMediaTimeRange *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QMediaTimeRange &lhs, const QMediaTimeRange &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QMediaTimeRangeS1_(
    const QMediaTimeRange *lhs,
    const QMediaTimeRange *rhs) {
  return operator!=(*lhs, *rhs);
}

//  a QList<QMediaTimeRange::Interval> a ritual of QMediaTimeRange gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMediaTimeRange__QList_QMediaTimeRange_Interval(
    QList<QMediaTimeRange::Interval> *self) {
  delete self;
}
