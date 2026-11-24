//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qwaitcondition.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(thread)
#include <QtCore/qwaitcondition.h>
#include <QtCore/qdeadlinetimer.h>

//  QWaitCondition::QWaitCondition()
extern "C" Q_DECL_EXPORT
QWaitCondition *ritual_ZN14QWaitConditionC1Ev() {
  return new QWaitCondition();
}

//  QWaitCondition::~QWaitCondition()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaitConditionD1Ev(QWaitCondition *self) {
  delete self;
}

//  bool QWaitCondition::wait(QMutex *lockedMutex, QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWaitCondition4waitEP6QMutex14QDeadlineTimer(
    QWaitCondition *self,
    QMutex *lockedMutex,
    const QDeadlineTimer *deadline) {
  return self->wait(lockedMutex, *deadline);
}

//  bool QWaitCondition::wait(QMutex *lockedMutex, unsigned long time)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWaitCondition4waitEP6QMutexm(
    QWaitCondition *self,
    QMutex *lockedMutex,
    unsigned long time) {
  return self->wait(lockedMutex, time);
}

//  bool QWaitCondition::wait(QReadWriteLock *lockedReadWriteLock,
//      QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWaitCondition4waitEP14QReadWriteLock14QDeadlineTimer(
    QWaitCondition *self,
    QReadWriteLock *lockedReadWriteLock,
    const QDeadlineTimer *deadline) {
  return self->wait(lockedReadWriteLock, *deadline);
}

//  bool QWaitCondition::wait(QReadWriteLock *lockedReadWriteLock, unsigned
//      long time)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QWaitCondition4waitEP14QReadWriteLockm(
    QWaitCondition *self,
    QReadWriteLock *lockedReadWriteLock,
    unsigned long time) {
  return self->wait(lockedReadWriteLock, time);
}

//  void QWaitCondition::wakeOne()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaitCondition7wakeOneEv(QWaitCondition *self) {
  self->wakeOne();
}

//  void QWaitCondition::wakeAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaitCondition7wakeAllEv(QWaitCondition *self) {
  self->wakeAll();
}

//  void QWaitCondition::notify_one()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaitCondition10notify_oneEv(QWaitCondition *self) {
  self->notify_one();
}

//  void QWaitCondition::notify_all()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QWaitCondition10notify_allEv(QWaitCondition *self) {
  self->notify_all();
}

#endif  // QT_CONFIG(thread)
