//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qelapsedtimer.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qelapsedtimer.h>

//  QElapsedTimer::QElapsedTimer()
extern "C" Q_DECL_EXPORT
QElapsedTimer *ritual_ZN13QElapsedTimerC1Ev() {
  return new QElapsedTimer();
}

//  ClockType QElapsedTimer::clockType()
extern "C" Q_DECL_EXPORT
QElapsedTimer::ClockType ritual_ZN13QElapsedTimer9clockTypeEv() {
  return QElapsedTimer::clockType();
}

//  bool QElapsedTimer::isMonotonic()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QElapsedTimer11isMonotonicEv() {
  return QElapsedTimer::isMonotonic();
}

//  void QElapsedTimer::start()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QElapsedTimer5startEv(QElapsedTimer *self) {
  self->start();
}

//  qint64 QElapsedTimer::restart()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN13QElapsedTimer7restartEv(QElapsedTimer *self) {
  return self->restart();
}

//  void QElapsedTimer::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QElapsedTimer10invalidateEv(QElapsedTimer *self) {
  self->invalidate();
}

//  bool QElapsedTimer::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QElapsedTimer7isValidEv(const QElapsedTimer *self) {
  return self->isValid();
}

//  qint64 QElapsedTimer::nsecsElapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QElapsedTimer12nsecsElapsedEv(const QElapsedTimer *self) {
  return self->nsecsElapsed();
}

//  qint64 QElapsedTimer::elapsed() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QElapsedTimer7elapsedEv(const QElapsedTimer *self) {
  return self->elapsed();
}

//  bool QElapsedTimer::hasExpired(qint64 timeout) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QElapsedTimer10hasExpiredEx(
    const QElapsedTimer *self,
    qint64 timeout) {
  return self->hasExpired(timeout);
}

//  qint64 QElapsedTimer::msecsSinceReference() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QElapsedTimer19msecsSinceReferenceEv(
    const QElapsedTimer *self) {
  return self->msecsSinceReference();
}

//  qint64 QElapsedTimer::msecsTo(const QElapsedTimer &other) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QElapsedTimer7msecsToERKS_(
    const QElapsedTimer *self,
    const QElapsedTimer *other) {
  return self->msecsTo(*other);
}

//  qint64 QElapsedTimer::secsTo(const QElapsedTimer &other) const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK13QElapsedTimer6secsToERKS_(
    const QElapsedTimer *self,
    const QElapsedTimer *other) {
  return self->secsTo(*other);
}

//  bool operator<(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK13QElapsedTimerS1_(
    const QElapsedTimer *lhs,
    const QElapsedTimer *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator==(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK13QElapsedTimerS1_(
    const QElapsedTimer *lhs,
    const QElapsedTimer *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK13QElapsedTimerS1_(
    const QElapsedTimer *lhs,
    const QElapsedTimer *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator>(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK13QElapsedTimerS1_(
    const QElapsedTimer *lhs,
    const QElapsedTimer *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK13QElapsedTimerS1_(
    const QElapsedTimer *lhs,
    const QElapsedTimer *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QElapsedTimer &lhs, const QElapsedTimer &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK13QElapsedTimerS1_(
    const QElapsedTimer *lhs,
    const QElapsedTimer *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QElapsedTimer::~QElapsedTimer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QElapsedTimerD1Ev(QElapsedTimer *self) {
  delete self;
}
