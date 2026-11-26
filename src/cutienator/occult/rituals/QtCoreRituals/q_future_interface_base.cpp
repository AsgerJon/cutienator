//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qfutureinterface.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(future)
#if QT_CONFIG(future)
#include <QtCore/qfutureinterface.h>
#include <QtCore/qexception.h>
#include <QtCore/qstring.h>
#include <QtCore/qresultstore.h>
#include <QtCore/qvariant.h>
#include <functional>
#include <QtCore/QFutureInterfaceBase>
#include <QtCore/QVariant>
#include <QtCore/qfuture.h>

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

//  QFutureInterfaceBase::QFutureInterfaceBase(QFutureInterfaceBase &&other)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBaseC1EOS_(
    QFutureInterfaceBase *other) {
  return new QFutureInterfaceBase(std::move(*other));
}

//  QFutureInterfaceBase &QFutureInterfaceBase::operator=(const
//      QFutureInterfaceBase &other)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBaseaSERKS_(
    QFutureInterfaceBase *self,
    const QFutureInterfaceBase *other) {
  return &(self->operator=(*other));
}

//  QFutureInterfaceBase
//      &QFutureInterfaceBase::operator=(QFutureInterfaceBase &&other)
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBaseaSEOS_(
    QFutureInterfaceBase *self,
    QFutureInterfaceBase *other) {
  return &(self->operator=(std::move(*other)));
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

#if !defined(QT_NO_EXCEPTIONS)
//  void QFutureInterfaceBase::reportException(const QException &e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15reportExceptionERK10QException(
    QFutureInterfaceBase *self,
    const QException *e) {
  self->reportException(*e);
}
#endif  // !defined(QT_NO_EXCEPTIONS)

#if !defined(QT_NO_EXCEPTIONS)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  void QFutureInterfaceBase::reportException(std::exception_ptr e)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15reportExceptionENSt15__exception_ptr13exception_ptrE(
    QFutureInterfaceBase *self,
    const std::exception_ptr *e) {
  self->reportException(*e);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_EXCEPTIONS)

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

#if QT_DEPRECATED_SINCE(6, 0)
//  bool QFutureInterfaceBase::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase8isPausedEv(
    const QFutureInterfaceBase *self) {
  return self->isPaused();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QFutureInterfaceBase::setPaused(bool paused)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase9setPausedEb(
    QFutureInterfaceBase *self,
    bool paused) {
  self->setPaused(paused);
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

#if QT_DEPRECATED_SINCE(6, 0)
//  void QFutureInterfaceBase::togglePaused()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase12togglePausedEv(
    QFutureInterfaceBase *self) {
  self->togglePaused();
}
#endif  // QT_DEPRECATED_SINCE(6, 0)

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

//  QMutex &QFutureInterfaceBase::mutex() const
extern "C" Q_DECL_EXPORT
QMutex *ritual_ZNK20QFutureInterfaceBase5mutexEv(
    const QFutureInterfaceBase *self) {
  return &(self->mutex());
}

//  bool QFutureInterfaceBase::hasException() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase12hasExceptionEv(
    const QFutureInterfaceBase *self) {
  return self->hasException();
}

//  QtPrivate::ExceptionStore &QFutureInterfaceBase::exceptionStore()
extern "C" Q_DECL_EXPORT
QtPrivate::ExceptionStore *ritual_ZN20QFutureInterfaceBase14exceptionStoreEv(
    QFutureInterfaceBase *self) {
  return &(self->exceptionStore());
}

//  QtPrivate::ResultStoreBase &QFutureInterfaceBase::resultStoreBase()
extern "C" Q_DECL_EXPORT
QtPrivate::ResultStoreBase *ritual_ZN20QFutureInterfaceBase15resultStoreBaseEv(
    QFutureInterfaceBase *self) {
  return &(self->resultStoreBase());
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

//  void QFutureInterfaceBase::swap(QFutureInterfaceBase &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase4swapERS_(
    QFutureInterfaceBase *self,
    QFutureInterfaceBase *other) {
  self->swap(*other);
}

//  bool QFutureInterfaceBase::isChainCanceled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase15isChainCanceledEv(
    const QFutureInterfaceBase *self) {
  return self->isChainCanceled();
}

//  bool QFutureInterfaceBase::refT() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase4refTEv(
    const QFutureInterfaceBase *self) {
  return self->refT();
}

//  bool QFutureInterfaceBase::derefT() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase6derefTEv(
    const QFutureInterfaceBase *self) {
  return self->derefT();
}

//  void QFutureInterfaceBase::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase5resetEv(QFutureInterfaceBase *self) {
  self->reset();
}

//  void QFutureInterfaceBase::rethrowPossibleException()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase24rethrowPossibleExceptionEv(
    QFutureInterfaceBase *self) {
  self->rethrowPossibleException();
}

//  void QFutureInterfaceBase::setContinuation(std::function<void (const
//      QFutureInterfaceBase &)> func, void *continuationFutureData,
//      ContinuationType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15setContinuationESt8functionIFvRKS_EEPvNS_16ContinuationTypeE(
    QFutureInterfaceBase *self,
    const std::function<void (const QFutureInterfaceBase &)> *func,
    void *continuationFutureData,
    QFutureInterfaceBase::ContinuationType type) {
  self->setContinuation(*func, continuationFutureData, type);
}

//  void QFutureInterfaceBase::setContinuation(const QObject *context,
//      std::function<void ()> func, const QVariant &continuationFuture,
//      ContinuationType type)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase15setContinuationEPK7QObjectSt8functionIFvvEERK8QVariantNS_16ContinuationTypeE(
    QFutureInterfaceBase *self,
    const QObject *context,
    const std::function<void ()> *func,
    const QVariant *continuationFuture,
    QFutureInterfaceBase::ContinuationType type) {
  self->setContinuation(context, *func, *continuationFuture, type);
}

//  void QFutureInterfaceBase::cleanContinuation()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase17cleanContinuationEv(
    QFutureInterfaceBase *self) {
  self->cleanContinuation();
}

//  void QFutureInterfaceBase::runContinuation() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QFutureInterfaceBase15runContinuationEv(
    const QFutureInterfaceBase *self) {
  self->runContinuation();
}

//  void QFutureInterfaceBase::setLaunchAsync(bool value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase14setLaunchAsyncEb(
    QFutureInterfaceBase *self,
    bool value) {
  self->setLaunchAsync(value);
}

//  bool QFutureInterfaceBase::launchAsync() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase11launchAsyncEv(
    const QFutureInterfaceBase *self) {
  return self->launchAsync();
}

//  bool QFutureInterfaceBase::isRunningOrPending() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QFutureInterfaceBase18isRunningOrPendingEv(
    const QFutureInterfaceBase *self) {
  return self->isRunningOrPending();
}

//  void QFutureInterfaceBase::cancel(CancelMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase6cancelENS_10CancelModeE(
    QFutureInterfaceBase *self,
    QFutureInterfaceBase::CancelMode mode) {
  self->cancel(mode);
}

//  void QFutureInterfaceBase::cancelChain(CancelMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QFutureInterfaceBase11cancelChainENS_10CancelModeE(
    QFutureInterfaceBase *self,
    QFutureInterfaceBase::CancelMode mode) {
  self->cancelChain(mode);
}

//  static QFutureInterfaceBase QFutureInterfaceBase::get(
//      const QFuture<T> &future) [T = void]
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBase3getIvEES_RK7QFutureIT_E(
    const QFuture<void> *future) {
  return new QFutureInterfaceBase(
      QFutureInterfaceBase::get<void>(*future));
}

//  static QFutureInterfaceBase QFutureInterfaceBase::get(
//      const QFuture<T> &future) [T = int]
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBase3getIiEES_RK7QFutureIT_E(
    const QFuture<int> *future) {
  return new QFutureInterfaceBase(
      QFutureInterfaceBase::get<int>(*future));
}

//  static QFutureInterfaceBase QFutureInterfaceBase::get(
//      const QFuture<T> &future) [T = double]
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBase3getIdEES_RK7QFutureIT_E(
    const QFuture<double> *future) {
  return new QFutureInterfaceBase(
      QFutureInterfaceBase::get<double>(*future));
}

//  static QFutureInterfaceBase QFutureInterfaceBase::get(
//      const QFuture<T> &future) [T = bool]
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBase3getIbEES_RK7QFutureIT_E(
    const QFuture<bool> *future) {
  return new QFutureInterfaceBase(
      QFutureInterfaceBase::get<bool>(*future));
}

//  static QFutureInterfaceBase QFutureInterfaceBase::get(
//      const QFuture<T> &future) [T = QString]
extern "C" Q_DECL_EXPORT
QFutureInterfaceBase *ritual_ZN20QFutureInterfaceBase3getI7QStringEES_RK7QFutureIT_E(
    const QFuture<QString> *future) {
  return new QFutureInterfaceBase(
      QFutureInterfaceBase::get<QString>(*future));
}

#endif  // QT_CONFIG(future)
#endif  // QT_CONFIG(future)
