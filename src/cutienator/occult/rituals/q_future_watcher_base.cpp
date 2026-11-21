//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfuturewatcher.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfuturewatcher.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QFutureWatcherBase::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QFutureWatcherBase10metaObjectEv(
    const QFutureWatcherBase *self) {
  return self->metaObject();
}

//  QString QFutureWatcherBase::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QFutureWatcherBase2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QFutureWatcherBase::tr(s, c, n));
}

//  int QFutureWatcherBase::progressValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFutureWatcherBase13progressValueEv(
    const QFutureWatcherBase *self) {
  return self->progressValue();
}

//  int QFutureWatcherBase::progressMinimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFutureWatcherBase15progressMinimumEv(
    const QFutureWatcherBase *self) {
  return self->progressMinimum();
}

//  int QFutureWatcherBase::progressMaximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QFutureWatcherBase15progressMaximumEv(
    const QFutureWatcherBase *self) {
  return self->progressMaximum();
}

//  QString QFutureWatcherBase::progressText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18QFutureWatcherBase12progressTextEv(
    const QFutureWatcherBase *self) {
  return new QString(self->progressText());
}

//  bool QFutureWatcherBase::isStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase9isStartedEv(
    const QFutureWatcherBase *self) {
  return self->isStarted();
}

//  bool QFutureWatcherBase::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase10isFinishedEv(
    const QFutureWatcherBase *self) {
  return self->isFinished();
}

//  bool QFutureWatcherBase::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase9isRunningEv(
    const QFutureWatcherBase *self) {
  return self->isRunning();
}

//  bool QFutureWatcherBase::isCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase10isCanceledEv(
    const QFutureWatcherBase *self) {
  return self->isCanceled();
}

//  bool QFutureWatcherBase::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase8isPausedEv(
    const QFutureWatcherBase *self) {
  return self->isPaused();
}

//  bool QFutureWatcherBase::isSuspending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase12isSuspendingEv(
    const QFutureWatcherBase *self) {
  return self->isSuspending();
}

//  bool QFutureWatcherBase::isSuspended() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QFutureWatcherBase11isSuspendedEv(
    const QFutureWatcherBase *self) {
  return self->isSuspended();
}

//  void QFutureWatcherBase::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase15waitForFinishedEv(
    QFutureWatcherBase *self) {
  self->waitForFinished();
}

//  void QFutureWatcherBase::setPendingResultsLimit(int limit)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase22setPendingResultsLimitEi(
    QFutureWatcherBase *self,
    int limit) {
  self->setPendingResultsLimit(limit);
}

//  bool QFutureWatcherBase::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QFutureWatcherBase5eventEP6QEvent(
    QFutureWatcherBase *self,
    QEvent *event) {
  return self->event(event);
}

//  void QFutureWatcherBase::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase6cancelEv(QFutureWatcherBase *self) {
  self->cancel();
}

//  void QFutureWatcherBase::setSuspended(bool suspend)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase12setSuspendedEb(
    QFutureWatcherBase *self,
    bool suspend) {
  self->setSuspended(suspend);
}

//  void QFutureWatcherBase::suspend()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase7suspendEv(QFutureWatcherBase *self) {
  self->suspend();
}

//  void QFutureWatcherBase::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase6resumeEv(QFutureWatcherBase *self) {
  self->resume();
}

//  void QFutureWatcherBase::toggleSuspended()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase15toggleSuspendedEv(
    QFutureWatcherBase *self) {
  self->toggleSuspended();
}

//  void QFutureWatcherBase::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase9setPausedEb(
    QFutureWatcherBase *self,
    bool paused) {
  self->setPaused(paused);
}

//  void QFutureWatcherBase::pause()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase5pauseEv(QFutureWatcherBase *self) {
  self->pause();
}

//  void QFutureWatcherBase::togglePaused()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QFutureWatcherBase12togglePausedEv(
    QFutureWatcherBase *self) {
  self->togglePaused();
}
