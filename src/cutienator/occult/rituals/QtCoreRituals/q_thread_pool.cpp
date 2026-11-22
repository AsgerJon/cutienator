//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qthreadpool.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qthreadpool.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>

//  const QMetaObject *QThreadPool::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QThreadPool10metaObjectEv(
    const QThreadPool *self) {
  return self->metaObject();
}

//  QString QThreadPool::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QThreadPool2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QThreadPool::tr(s, c, n));
}

//  QThreadPool::QThreadPool(QObject *parent)
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN11QThreadPoolC1EP7QObject(QObject *parent) {
  return new QThreadPool(parent);
}

//  QThreadPool::~QThreadPool()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPoolD1Ev(QThreadPool *self) {
  delete self;
}

//  QThreadPool *QThreadPool::globalInstance()
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN11QThreadPool14globalInstanceEv() {
  return QThreadPool::globalInstance();
}

//  void QThreadPool::start(QRunnable *runnable, int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool5startEP9QRunnablei(
    QThreadPool *self,
    QRunnable *runnable,
    int priority) {
  self->start(runnable, priority);
}

//  bool QThreadPool::tryStart(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool8tryStartEP9QRunnable(
    QThreadPool *self,
    QRunnable *runnable) {
  return self->tryStart(runnable);
}

//  void QThreadPool::startOnReservedThread(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool21startOnReservedThreadEP9QRunnable(
    QThreadPool *self,
    QRunnable *runnable) {
  self->startOnReservedThread(runnable);
}

//  int QThreadPool::expiryTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QThreadPool13expiryTimeoutEv(const QThreadPool *self) {
  return self->expiryTimeout();
}

//  void QThreadPool::setExpiryTimeout(int expiryTimeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool16setExpiryTimeoutEi(
    QThreadPool *self,
    int expiryTimeout) {
  self->setExpiryTimeout(expiryTimeout);
}

//  int QThreadPool::maxThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QThreadPool14maxThreadCountEv(const QThreadPool *self) {
  return self->maxThreadCount();
}

//  void QThreadPool::setMaxThreadCount(int maxThreadCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool17setMaxThreadCountEi(
    QThreadPool *self,
    int maxThreadCount) {
  self->setMaxThreadCount(maxThreadCount);
}

//  int QThreadPool::activeThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QThreadPool17activeThreadCountEv(const QThreadPool *self) {
  return self->activeThreadCount();
}

//  void QThreadPool::setStackSize(uint stackSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool12setStackSizeEj(
    QThreadPool *self,
    uint stackSize) {
  self->setStackSize(stackSize);
}

//  uint QThreadPool::stackSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK11QThreadPool9stackSizeEv(const QThreadPool *self) {
  return self->stackSize();
}

//  void QThreadPool::setThreadPriority(QThread::Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool17setThreadPriorityEN7QThread8PriorityE(
    QThreadPool *self,
    QThread::Priority priority) {
  self->setThreadPriority(priority);
}

//  QThread::Priority QThreadPool::threadPriority() const
extern "C" Q_DECL_EXPORT
QThread::Priority ritual_ZNK11QThreadPool14threadPriorityEv(
    const QThreadPool *self) {
  return self->threadPriority();
}

//  void QThreadPool::reserveThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool13reserveThreadEv(QThreadPool *self) {
  self->reserveThread();
}

//  void QThreadPool::releaseThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool13releaseThreadEv(QThreadPool *self) {
  self->releaseThread();
}

//  void QThreadPool::setServiceLevel(QThread::QualityOfService serviceLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool15setServiceLevelEN7QThread16QualityOfServiceE(
    QThreadPool *self,
    QThread::QualityOfService serviceLevel) {
  self->setServiceLevel(serviceLevel);
}

//  QThread::QualityOfService QThreadPool::serviceLevel() const
extern "C" Q_DECL_EXPORT
QThread::QualityOfService ritual_ZNK11QThreadPool12serviceLevelEv(
    const QThreadPool *self) {
  return self->serviceLevel();
}

//  bool QThreadPool::waitForDone(int msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool11waitForDoneEi(QThreadPool *self, int msecs) {
  return self->waitForDone(msecs);
}

//  bool QThreadPool::waitForDone(QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool11waitForDoneE14QDeadlineTimer(
    QThreadPool *self,
    const QDeadlineTimer *deadline) {
  return self->waitForDone(*deadline);
}

//  void QThreadPool::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QThreadPool5clearEv(QThreadPool *self) {
  self->clear();
}

//  bool QThreadPool::contains(const QThread *thread) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QThreadPool8containsEPK7QThread(
    const QThreadPool *self,
    const QThread *thread) {
  return self->contains(thread);
}

//  bool QThreadPool::tryTake(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QThreadPool7tryTakeEP9QRunnable(
    QThreadPool *self,
    QRunnable *runnable) {
  return self->tryTake(runnable);
}
