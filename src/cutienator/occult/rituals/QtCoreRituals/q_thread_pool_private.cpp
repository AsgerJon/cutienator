//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qthreadpool_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/qthreadpool.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qthreadpool_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>

//  QThreadPool *QThreadPoolPrivate::q_func()
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN18QThreadPoolPrivate6q_funcEv(
    QThreadPoolPrivate *self) {
  return self->q_func();
}

//  const QThreadPool *QThreadPoolPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QThreadPool *ritual_ZNK18QThreadPoolPrivate6q_funcEv(
    const QThreadPoolPrivate *self) {
  return self->q_func();
}

//  QThreadPoolPrivate::QThreadPoolPrivate()
extern "C" Q_DECL_EXPORT
QThreadPoolPrivate *ritual_ZN18QThreadPoolPrivateC1Ev() {
  return new QThreadPoolPrivate();
}

//  bool QThreadPoolPrivate::tryStart(QRunnable *task)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QThreadPoolPrivate8tryStartEP9QRunnable(
    QThreadPoolPrivate *self,
    QRunnable *task) {
  return self->tryStart(task);
}

//  void QThreadPoolPrivate::enqueueTask(QRunnable *task, int priority)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadPoolPrivate11enqueueTaskEP9QRunnablei(
    QThreadPoolPrivate *self,
    QRunnable *task,
    int priority) {
  self->enqueueTask(task, priority);
}

//  int QThreadPoolPrivate::activeThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QThreadPoolPrivate17activeThreadCountEv(
    const QThreadPoolPrivate *self) {
  return self->activeThreadCount();
}

//  void QThreadPoolPrivate::tryToStartMoreThreads()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadPoolPrivate21tryToStartMoreThreadsEv(
    QThreadPoolPrivate *self) {
  self->tryToStartMoreThreads();
}

//  bool QThreadPoolPrivate::areAllThreadsActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QThreadPoolPrivate19areAllThreadsActiveEv(
    const QThreadPoolPrivate *self) {
  return self->areAllThreadsActive();
}

//  bool QThreadPoolPrivate::tooManyThreadsActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QThreadPoolPrivate20tooManyThreadsActiveEv(
    const QThreadPoolPrivate *self) {
  return self->tooManyThreadsActive();
}

//  int QThreadPoolPrivate::maxThreadCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QThreadPoolPrivate14maxThreadCountEv(
    const QThreadPoolPrivate *self) {
  return self->maxThreadCount();
}

//  void QThreadPoolPrivate::startThread(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadPoolPrivate11startThreadEP9QRunnable(
    QThreadPoolPrivate *self,
    QRunnable *runnable) {
  self->startThread(runnable);
}

//  void QThreadPoolPrivate::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadPoolPrivate5resetEv(QThreadPoolPrivate *self) {
  self->reset();
}

//  bool QThreadPoolPrivate::waitForDone(const QDeadlineTimer &timer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QThreadPoolPrivate11waitForDoneERK14QDeadlineTimer(
    QThreadPoolPrivate *self,
    const QDeadlineTimer *timer) {
  return self->waitForDone(*timer);
}

//  void QThreadPoolPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadPoolPrivate5clearEv(QThreadPoolPrivate *self) {
  self->clear();
}

//  void QThreadPoolPrivate::stealAndRunRunnable(QRunnable *runnable)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QThreadPoolPrivate19stealAndRunRunnableEP9QRunnable(
    QThreadPoolPrivate *self,
    QRunnable *runnable) {
  self->stealAndRunRunnable(runnable);
}
