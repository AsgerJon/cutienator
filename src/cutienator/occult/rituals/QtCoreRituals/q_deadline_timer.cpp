//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdeadlinetimer.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 3. Kept as it is when the
//  generator runs again.
#include <QtCore/qdeadlinetimer.h>
#include <chrono>

//  QDeadlineTimer::QDeadlineTimer()
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimerC1Ev() {
  return new QDeadlineTimer();
}

//  QDeadlineTimer::QDeadlineTimer(Qt::TimerType type_)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimerC1EN2Qt9TimerTypeE(
    Qt::TimerType type_) {
  return new QDeadlineTimer(type_);
}

//  QDeadlineTimer::QDeadlineTimer(ForeverConstant a0, Qt::TimerType type_)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimerC1ENS_15ForeverConstantEN2Qt9TimerTypeE(
    QDeadlineTimer::ForeverConstant a0,
    Qt::TimerType type_) {
  return new QDeadlineTimer(a0, type_);
}

//  QDeadlineTimer::QDeadlineTimer(qint64 msecs, Qt::TimerType type)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimerC1ExN2Qt9TimerTypeE(
    qint64 msecs,
    Qt::TimerType type) {
  return new QDeadlineTimer(msecs, type);
}

//  void QDeadlineTimer::swap(QDeadlineTimer &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer4swapERS_(
    QDeadlineTimer *self,
    QDeadlineTimer *other) {
  self->swap(*other);
}

//  bool QDeadlineTimer::isForever() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QDeadlineTimer9isForeverEv(const QDeadlineTimer *self) {
  return self->isForever();
}

//  bool QDeadlineTimer::hasExpired() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QDeadlineTimer10hasExpiredEv(const QDeadlineTimer *self) {
  return self->hasExpired();
}

//  Qt::TimerType QDeadlineTimer::timerType() const
extern "C" Q_DECL_EXPORT
Qt::TimerType ritual_ZNK14QDeadlineTimer9timerTypeEv(
    const QDeadlineTimer *self) {
  return self->timerType();
}

//  void QDeadlineTimer::setTimerType(Qt::TimerType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer12setTimerTypeEN2Qt9TimerTypeE(
    QDeadlineTimer *self,
    Qt::TimerType type) {
  self->setTimerType(type);
}

//  qint64 QDeadlineTimer::remainingTime() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QDeadlineTimer13remainingTimeEv(
    const QDeadlineTimer *self) {
  return self->remainingTime();
}

//  qint64 QDeadlineTimer::remainingTimeNSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QDeadlineTimer18remainingTimeNSecsEv(
    const QDeadlineTimer *self) {
  return self->remainingTimeNSecs();
}

//  void QDeadlineTimer::setRemainingTime(qint64 msecs, Qt::TimerType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer16setRemainingTimeExN2Qt9TimerTypeE(
    QDeadlineTimer *self,
    qint64 msecs,
    Qt::TimerType type) {
  self->setRemainingTime(msecs, type);
}

//  void QDeadlineTimer::setPreciseRemainingTime(qint64 secs, qint64 nsecs,
//      Qt::TimerType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer23setPreciseRemainingTimeExxN2Qt9TimerTypeE(
    QDeadlineTimer *self,
    qint64 secs,
    qint64 nsecs,
    Qt::TimerType type) {
  self->setPreciseRemainingTime(secs, nsecs, type);
}

//  qint64 QDeadlineTimer::deadline() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QDeadlineTimer8deadlineEv(const QDeadlineTimer *self) {
  return self->deadline();
}

//  qint64 QDeadlineTimer::deadlineNSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QDeadlineTimer13deadlineNSecsEv(
    const QDeadlineTimer *self) {
  return self->deadlineNSecs();
}

//  void QDeadlineTimer::setDeadline(qint64 msecs, Qt::TimerType timerType)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer11setDeadlineExN2Qt9TimerTypeE(
    QDeadlineTimer *self,
    qint64 msecs,
    Qt::TimerType timerType) {
  self->setDeadline(msecs, timerType);
}

//  void QDeadlineTimer::setPreciseDeadline(qint64 secs, qint64 nsecs,
//      Qt::TimerType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer18setPreciseDeadlineExxN2Qt9TimerTypeE(
    QDeadlineTimer *self,
    qint64 secs,
    qint64 nsecs,
    Qt::TimerType type) {
  self->setPreciseDeadline(secs, nsecs, type);
}

//  QDeadlineTimer QDeadlineTimer::addNSecs(QDeadlineTimer dt, qint64 nsecs)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimer8addNSecsES_x(
    const QDeadlineTimer *dt,
    qint64 nsecs) {
  return new QDeadlineTimer(QDeadlineTimer::addNSecs(*dt, nsecs));
}

//  QDeadlineTimer QDeadlineTimer::current(Qt::TimerType timerType)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimer7currentEN2Qt9TimerTypeE(
    Qt::TimerType timerType) {
  return new QDeadlineTimer(QDeadlineTimer::current(timerType));
}

//  QDeadlineTimer operator+(QDeadlineTimer dt, qint64 msecs)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_Zpl14QDeadlineTimerx(
    const QDeadlineTimer *dt,
    qint64 msecs) {
  return new QDeadlineTimer(operator+(*dt, msecs));
}

//  QDeadlineTimer operator+(qint64 msecs, QDeadlineTimer dt)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_Zplx14QDeadlineTimer(
    qint64 msecs,
    const QDeadlineTimer *dt) {
  return new QDeadlineTimer(operator+(msecs, *dt));
}

//  QDeadlineTimer operator-(QDeadlineTimer dt, qint64 msecs)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_Zmi14QDeadlineTimerx(
    const QDeadlineTimer *dt,
    qint64 msecs) {
  return new QDeadlineTimer(operator-(*dt, msecs));
}

//  qint64 operator-(QDeadlineTimer dt1, QDeadlineTimer dt2)
extern "C" Q_DECL_EXPORT
qint64 ritual_Zmi14QDeadlineTimerS_(
    const QDeadlineTimer *dt1,
    const QDeadlineTimer *dt2) {
  return operator-(*dt1, *dt2);
}

//  QDeadlineTimer &QDeadlineTimer::operator+=(qint64 msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimerpLEx(QDeadlineTimer *self, qint64 msecs) {
  self->operator+=(msecs);
}

//  QDeadlineTimer &QDeadlineTimer::operator-=(qint64 msecs)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimermIEx(QDeadlineTimer *self, qint64 msecs) {
  self->operator-=(msecs);
}

//  std::chrono::nanoseconds QDeadlineTimer::remainingTimeAsDuration() const
extern "C" Q_DECL_EXPORT
long long ritual_ZNK14QDeadlineTimer23remainingTimeAsDurationEv(
    const QDeadlineTimer *self) {
  return static_cast<long long>(self->remainingTimeAsDuration().count());
}

//  bool operator==(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK14QDeadlineTimerS1_(
    const QDeadlineTimer *lhs,
    const QDeadlineTimer *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK14QDeadlineTimerS1_(
    const QDeadlineTimer *lhs,
    const QDeadlineTimer *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK14QDeadlineTimerS1_(
    const QDeadlineTimer *lhs,
    const QDeadlineTimer *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK14QDeadlineTimerS1_(
    const QDeadlineTimer *lhs,
    const QDeadlineTimer *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK14QDeadlineTimerS1_(
    const QDeadlineTimer *lhs,
    const QDeadlineTimer *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QDeadlineTimer &lhs, const QDeadlineTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK14QDeadlineTimerS1_(
    const QDeadlineTimer *lhs,
    const QDeadlineTimer *rhs) {
  return operator>=(*lhs, *rhs);
}

//  qint64 QDeadlineTimer::rawRemainingTimeNSecs() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK14QDeadlineTimer21rawRemainingTimeNSecsEv(
    const QDeadlineTimer *self) {
  return self->rawRemainingTimeNSecs();
}

//  QDeadlineTimer::~QDeadlineTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimerD1Ev(QDeadlineTimer *self) {
  delete self;
}

//  QDeadlineTimer::QDeadlineTimer<long, std::ratio<1l, 1000l> >(
//      std::chrono::duration<long, std::ratio<1l, 1000l> > remaining,
//      Qt::TimerType type_)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimerC2IlSt5ratioILl1ELl1000EEEENSt6chrono8durationIT_T0_EEN2Qt9TimerTypeE(
    long long remaining,
    Qt::TimerType type_) {
  return new QDeadlineTimer(std::chrono::milliseconds(remaining), type_);
}

//  QDeadlineTimer &QDeadlineTimer::operator=<long, std::ratio<1l, 1000l> >(
//      std::chrono::duration<long, std::ratio<1l, 1000l> > remaining)
extern "C" Q_DECL_EXPORT
QDeadlineTimer *ritual_ZN14QDeadlineTimeraSIlSt5ratioILl1ELl1000EEEERS_NSt6chrono8durationIT_T0_EE(
    QDeadlineTimer *self,
    long long remaining) {
  return &(*self = std::chrono::milliseconds(remaining));
}

//  void QDeadlineTimer::setRemainingTime<long, std::ratio<1l, 1000l> >(
//      std::chrono::duration<long, std::ratio<1l, 1000l> > remaining,
//      Qt::TimerType type_)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimer16setRemainingTimeIlSt5ratioILl1ELl1000EEEEvNSt6chrono8durationIT_T0_EEN2Qt9TimerTypeE(
    QDeadlineTimer *self,
    long long remaining,
    Qt::TimerType type_) {
  self->setRemainingTime(std::chrono::milliseconds(remaining), type_);
}
