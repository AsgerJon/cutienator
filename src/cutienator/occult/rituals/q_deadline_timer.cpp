//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qdeadlinetimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qdeadlinetimer.h>

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

//  QDeadlineTimer::~QDeadlineTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QDeadlineTimerD1Ev(QDeadlineTimer *self) {
  delete self;
}
