//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmutex.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmutex.h>
#include <QtCore/qdeadlinetimer.h>

//  QBasicMutex::QBasicMutex()
extern "C" Q_DECL_EXPORT
QBasicMutex *ritual_ZN11QBasicMutexC1Ev() {
  return new QBasicMutex();
}

//  void QBasicMutex::lock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicMutex4lockEv(QBasicMutex *self) {
  self->lock();
}

//  void QBasicMutex::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicMutex6unlockEv(QBasicMutex *self) {
  self->unlock();
}

//  bool QBasicMutex::tryLock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBasicMutex7tryLockEv(QBasicMutex *self) {
  return self->tryLock();
}

//  bool QBasicMutex::try_lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBasicMutex8try_lockEv(QBasicMutex *self) {
  return self->try_lock();
}

//  bool QBasicMutex::fastTryLock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBasicMutex11fastTryLockEv(QBasicMutex *self) {
  return self->fastTryLock();
}

//  void QBasicMutex::lockInternal()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicMutex12lockInternalEv(QBasicMutex *self) {
  self->lockInternal();
}

//  bool QBasicMutex::lockInternal(QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBasicMutex12lockInternalE14QDeadlineTimer(
    QBasicMutex *self,
    const QDeadlineTimer *timeout) {
  return self->lockInternal(*timeout);
}

//  bool QBasicMutex::lockInternal(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QBasicMutex12lockInternalEi(QBasicMutex *self, int timeout) {
  return self->lockInternal(timeout);
}

//  void QBasicMutex::unlockInternal()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QBasicMutex14unlockInternalEv(QBasicMutex *self) {
  self->unlockInternal();
}
