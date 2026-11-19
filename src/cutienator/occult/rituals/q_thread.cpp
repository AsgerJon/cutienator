//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qthread.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qthread.h>
#include <QtCore/qstring.h>
#include <QtCore/qdeadlinetimer.h>

//  const QMetaObject *QThread::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK7QThread10metaObjectEv(const QThread *self) {
  return self->metaObject();
}

//  QString QThread::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN7QThread2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QThread::tr(s, c, n));
}

//  QThread *QThread::currentThread()
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN7QThread13currentThreadEv() {
  return QThread::currentThread();
}

//  bool QThread::isMainThread()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread12isMainThreadEv() {
  return QThread::isMainThread();
}

//  int QThread::idealThreadCount()
extern "C" Q_DECL_EXPORT
int ritual_ZN7QThread16idealThreadCountEv() {
  return QThread::idealThreadCount();
}

//  void QThread::yieldCurrentThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread18yieldCurrentThreadEv() {
  QThread::yieldCurrentThread();
}

//  QThread::QThread(QObject *parent)
extern "C" Q_DECL_EXPORT
QThread *ritual_ZN7QThreadC1EP7QObject(QObject *parent) {
  return new QThread(parent);
}

//  QThread::~QThread()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThreadD1Ev(QThread *self) {
  delete self;
}

//  void QThread::setPriority(Priority priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread11setPriorityENS_8PriorityE(
    QThread *self,
    QThread::Priority priority) {
  self->setPriority(priority);
}

//  Priority QThread::priority() const
extern "C" Q_DECL_EXPORT
QThread::Priority ritual_ZNK7QThread8priorityEv(const QThread *self) {
  return self->priority();
}

//  bool QThread::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread10isFinishedEv(const QThread *self) {
  return self->isFinished();
}

//  bool QThread::isRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread9isRunningEv(const QThread *self) {
  return self->isRunning();
}

//  void QThread::requestInterruption()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread19requestInterruptionEv(QThread *self) {
  self->requestInterruption();
}

//  bool QThread::isInterruptionRequested() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread23isInterruptionRequestedEv(const QThread *self) {
  return self->isInterruptionRequested();
}

//  void QThread::setStackSize(uint stackSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread12setStackSizeEj(QThread *self, uint stackSize) {
  self->setStackSize(stackSize);
}

//  uint QThread::stackSize() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK7QThread9stackSizeEv(const QThread *self) {
  return self->stackSize();
}

//  QAbstractEventDispatcher *QThread::eventDispatcher() const
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZNK7QThread15eventDispatcherEv(
    const QThread *self) {
  return self->eventDispatcher();
}

//  void QThread::setEventDispatcher(QAbstractEventDispatcher
//      *eventDispatcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread18setEventDispatcherEP24QAbstractEventDispatcher(
    QThread *self,
    QAbstractEventDispatcher *eventDispatcher) {
  self->setEventDispatcher(eventDispatcher);
}

//  bool QThread::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread5eventEP6QEvent(QThread *self, QEvent *event) {
  return self->event(event);
}

//  int QThread::loopLevel() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK7QThread9loopLevelEv(const QThread *self) {
  return self->loopLevel();
}

//  bool QThread::isCurrentThread() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK7QThread15isCurrentThreadEv(const QThread *self) {
  return self->isCurrentThread();
}

//  void QThread::setServiceLevel(QualityOfService serviceLevel)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread15setServiceLevelENS_16QualityOfServiceE(
    QThread *self,
    QThread::QualityOfService serviceLevel) {
  self->setServiceLevel(serviceLevel);
}

//  QualityOfService QThread::serviceLevel() const
extern "C" Q_DECL_EXPORT
QThread::QualityOfService ritual_ZNK7QThread12serviceLevelEv(
    const QThread *self) {
  return self->serviceLevel();
}

//  void QThread::start(Priority a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread5startENS_8PriorityE(
    QThread *self,
    QThread::Priority a0) {
  self->start(a0);
}

//  void QThread::terminate()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread9terminateEv(QThread *self) {
  self->terminate();
}

//  void QThread::exit(int retcode)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread4exitEi(QThread *self, int retcode) {
  self->exit(retcode);
}

//  void QThread::quit()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread4quitEv(QThread *self) {
  self->quit();
}

//  bool QThread::wait(QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread4waitE14QDeadlineTimer(
    QThread *self,
    const QDeadlineTimer *deadline) {
  return self->wait(*deadline);
}

//  bool QThread::wait(unsigned long time)
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QThread4waitEm(QThread *self, unsigned long time) {
  return self->wait(time);
}

//  void QThread::sleep(unsigned long a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread5sleepEm(unsigned long a0) {
  QThread::sleep(a0);
}

//  void QThread::msleep(unsigned long a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread6msleepEm(unsigned long a0) {
  QThread::msleep(a0);
}

//  void QThread::usleep(unsigned long a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN7QThread6usleepEm(unsigned long a0) {
  QThread::usleep(a0);
}
