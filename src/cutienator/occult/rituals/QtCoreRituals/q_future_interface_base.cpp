//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfutureinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qfutureinterface.h>
#include <QtCore/qexception.h>
#include <QtCore/qstring.h>
#include <QtCore/qresultstore.h>

//  QFutureInterfaceBase::QFutureInterfaceBase(State initialState)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBaseC1ENS_5StateE(
    QFutureInterfaceBase::State initialState) {
  return new QFutureInterfaceBase(initialState);
}

//  QFutureInterfaceBase::QFutureInterfaceBase(const QFutureInterfaceBase
//      &other)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBaseC1ERKS_(
    const QFutureInterfaceBase *other) {
  return new QFutureInterfaceBase(*other);
}

//  QFutureInterfaceBase::~QFutureInterfaceBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBaseD1Ev(QFutureInterfaceBase *self) {
  delete self;
}

//  void QFutureInterfaceBase::reportStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase13reportStartedEv(
    QFutureInterfaceBase *self) {
  self->reportStarted();
}

//  void QFutureInterfaceBase::reportFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase14reportFinishedEv(
    QFutureInterfaceBase *self) {
  self->reportFinished();
}

//  void QFutureInterfaceBase::reportCanceled()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase14reportCanceledEv(
    QFutureInterfaceBase *self) {
  self->reportCanceled();
}

//  void QFutureInterfaceBase::reportException(const QException &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15reportExceptionERK10QException(
    QFutureInterfaceBase *self,
    const QException *e) {
  self->reportException(*e);
}

//  void QFutureInterfaceBase::reportResultsReady(int beginIndex, int
//      endIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase18reportResultsReadyEii(
    QFutureInterfaceBase *self,
    int beginIndex,
    int endIndex) {
  self->reportResultsReady(beginIndex, endIndex);
}

//  void QFutureInterfaceBase::setRunnable(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase11setRunnableEP9QRunnable(
    QFutureInterfaceBase *self,
    QRunnable *runnable) {
  self->setRunnable(runnable);
}

//  void QFutureInterfaceBase::setThreadPool(QThreadPool *pool)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase13setThreadPoolEP11QThreadPool(
    QFutureInterfaceBase *self,
    QThreadPool *pool) {
  self->setThreadPool(pool);
}

//  QThreadPool *QFutureInterfaceBase::threadPool() const
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZNK20QFutureInterfaceBase10threadPoolEv(
    const QFutureInterfaceBase *self) {
  return self->threadPool();
}

//  void QFutureInterfaceBase::setFilterMode(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase13setFilterModeEb(
    QFutureInterfaceBase *self,
    bool enable) {
  self->setFilterMode(enable);
}

//  void QFutureInterfaceBase::setProgressRange(int minimum, int maximum)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase16setProgressRangeEii(
    QFutureInterfaceBase *self,
    int minimum,
    int maximum) {
  self->setProgressRange(minimum, maximum);
}

//  int QFutureInterfaceBase::progressMinimum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QFutureInterfaceBase15progressMinimumEv(
    const QFutureInterfaceBase *self) {
  return self->progressMinimum();
}

//  int QFutureInterfaceBase::progressMaximum() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QFutureInterfaceBase15progressMaximumEv(
    const QFutureInterfaceBase *self) {
  return self->progressMaximum();
}

//  bool QFutureInterfaceBase::isProgressUpdateNeeded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase22isProgressUpdateNeededEv(
    const QFutureInterfaceBase *self) {
  return self->isProgressUpdateNeeded();
}

//  void QFutureInterfaceBase::setProgressValue(int progressValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase16setProgressValueEi(
    QFutureInterfaceBase *self,
    int progressValue) {
  self->setProgressValue(progressValue);
}

//  int QFutureInterfaceBase::progressValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QFutureInterfaceBase13progressValueEv(
    const QFutureInterfaceBase *self) {
  return self->progressValue();
}

//  void QFutureInterfaceBase::setProgressValueAndText(int progressValue,
//      const QString &progressText)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase23setProgressValueAndTextEiRK7QString(
    QFutureInterfaceBase *self,
    int progressValue,
    const QString *progressText) {
  self->setProgressValueAndText(progressValue, *progressText);
}

//  QString QFutureInterfaceBase::progressText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QFutureInterfaceBase12progressTextEv(
    const QFutureInterfaceBase *self) {
  return new QString(self->progressText());
}

//  void QFutureInterfaceBase::setExpectedResultCount(int resultCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase22setExpectedResultCountEi(
    QFutureInterfaceBase *self,
    int resultCount) {
  self->setExpectedResultCount(resultCount);
}

//  int QFutureInterfaceBase::expectedResultCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN20QFutureInterfaceBase19expectedResultCountEv(
    QFutureInterfaceBase *self) {
  return self->expectedResultCount();
}

//  int QFutureInterfaceBase::resultCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QFutureInterfaceBase11resultCountEv(
    const QFutureInterfaceBase *self) {
  return self->resultCount();
}

//  bool QFutureInterfaceBase::queryState(State state) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase10queryStateENS_5StateE(
    const QFutureInterfaceBase *self,
    QFutureInterfaceBase::State state) {
  return self->queryState(state);
}

//  bool QFutureInterfaceBase::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase9isRunningEv(
    const QFutureInterfaceBase *self) {
  return self->isRunning();
}

//  bool QFutureInterfaceBase::isStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase9isStartedEv(
    const QFutureInterfaceBase *self) {
  return self->isStarted();
}

//  bool QFutureInterfaceBase::isCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase10isCanceledEv(
    const QFutureInterfaceBase *self) {
  return self->isCanceled();
}

//  bool QFutureInterfaceBase::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase10isFinishedEv(
    const QFutureInterfaceBase *self) {
  return self->isFinished();
}

//  bool QFutureInterfaceBase::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase8isPausedEv(
    const QFutureInterfaceBase *self) {
  return self->isPaused();
}

//  void QFutureInterfaceBase::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase9setPausedEb(
    QFutureInterfaceBase *self,
    bool paused) {
  self->setPaused(paused);
}

//  void QFutureInterfaceBase::togglePaused()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase12togglePausedEv(
    QFutureInterfaceBase *self) {
  self->togglePaused();
}

//  bool QFutureInterfaceBase::isSuspending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase12isSuspendingEv(
    const QFutureInterfaceBase *self) {
  return self->isSuspending();
}

//  bool QFutureInterfaceBase::isSuspended() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase11isSuspendedEv(
    const QFutureInterfaceBase *self) {
  return self->isSuspended();
}

//  bool QFutureInterfaceBase::isThrottled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase11isThrottledEv(
    const QFutureInterfaceBase *self) {
  return self->isThrottled();
}

//  bool QFutureInterfaceBase::isResultReadyAt(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase15isResultReadyAtEi(
    const QFutureInterfaceBase *self,
    int index) {
  return self->isResultReadyAt(index);
}

//  bool QFutureInterfaceBase::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase7isValidEv(
    const QFutureInterfaceBase *self) {
  return self->isValid();
}

//  int QFutureInterfaceBase::loadState() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QFutureInterfaceBase9loadStateEv(
    const QFutureInterfaceBase *self) {
  return self->loadState();
}

//  void QFutureInterfaceBase::cancel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase6cancelEv(QFutureInterfaceBase *self) {
  self->cancel();
}

//  void QFutureInterfaceBase::cancelAndFinish()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15cancelAndFinishEv(
    QFutureInterfaceBase *self) {
  self->cancelAndFinish();
}

//  void QFutureInterfaceBase::cancelChain()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase11cancelChainEv(
    QFutureInterfaceBase *self) {
  self->cancelChain();
}

//  void QFutureInterfaceBase::setAddResultsIfCanceledEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase30setAddResultsIfCanceledEnabledEb(
    QFutureInterfaceBase *self,
    bool enable) {
  self->setAddResultsIfCanceledEnabled(enable);
}

//  bool QFutureInterfaceBase::isAddResultsIfCanceledEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase29isAddResultsIfCanceledEnabledEv(
    const QFutureInterfaceBase *self) {
  return self->isAddResultsIfCanceledEnabled();
}

//  void QFutureInterfaceBase::setSuspended(bool suspend)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase12setSuspendedEb(
    QFutureInterfaceBase *self,
    bool suspend) {
  self->setSuspended(suspend);
}

//  void QFutureInterfaceBase::toggleSuspended()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15toggleSuspendedEv(
    QFutureInterfaceBase *self) {
  self->toggleSuspended();
}

//  void QFutureInterfaceBase::reportSuspended() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QFutureInterfaceBase15reportSuspendedEv(
    const QFutureInterfaceBase *self) {
  self->reportSuspended();
}

//  void QFutureInterfaceBase::setThrottled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase12setThrottledEb(
    QFutureInterfaceBase *self,
    bool enable) {
  self->setThrottled(enable);
}

//  void QFutureInterfaceBase::waitForFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15waitForFinishedEv(
    QFutureInterfaceBase *self) {
  self->waitForFinished();
}

//  bool QFutureInterfaceBase::waitForNextResult()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QFutureInterfaceBase17waitForNextResultEv(
    QFutureInterfaceBase *self) {
  return self->waitForNextResult();
}

//  void QFutureInterfaceBase::waitForResult(int resultIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase13waitForResultEi(
    QFutureInterfaceBase *self,
    int resultIndex) {
  self->waitForResult(resultIndex);
}

//  void QFutureInterfaceBase::waitForResume()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase13waitForResumeEv(
    QFutureInterfaceBase *self) {
  self->waitForResume();
}

//  void QFutureInterfaceBase::suspendIfRequested()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase18suspendIfRequestedEv(
    QFutureInterfaceBase *self) {
  self->suspendIfRequested();
}

//  bool QFutureInterfaceBase::hasException() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase12hasExceptionEv(
    const QFutureInterfaceBase *self) {
  return self->hasException();
}

//  const QtPrivate::ResultStoreBase &QFutureInterfaceBase::resultStoreBase()
//      const
extern "C" Q_DECL_EXPORT
QtPrivate::ResultStoreBase *ritual_ZNK20QFutureInterfaceBase15resultStoreBaseEv(
    const QFutureInterfaceBase *self) {
  return new QtPrivate::ResultStoreBase(self->resultStoreBase());
}

//  bool QFutureInterfaceBase::operator==(const QFutureInterfaceBase &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBaseeqERKS_(
    const QFutureInterfaceBase *self,
    const QFutureInterfaceBase *other) {
  return self->operator==(*other);
}

//  bool QFutureInterfaceBase::operator!=(const QFutureInterfaceBase &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBaseneERKS_(
    const QFutureInterfaceBase *self,
    const QFutureInterfaceBase *other) {
  return self->operator!=(*other);
}

//  bool QFutureInterfaceBase::isChainCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase15isChainCanceledEv(
    const QFutureInterfaceBase *self) {
  return self->isChainCanceled();
}
