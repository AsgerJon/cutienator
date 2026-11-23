//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qreadwritelock.h>
#include <QtCore/qdeadlinetimer.h>

//  QBasicReadWriteLock::QBasicReadWriteLock()
extern "C" Q_DECL_EXPORT
QBasicReadWriteLock *ritual_ZN19QBasicReadWriteLockC1Ev() {
  return new QBasicReadWriteLock();
}

//  void QBasicReadWriteLock::lockForRead()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock11lockForReadEv(
    QBasicReadWriteLock *self) {
  self->lockForRead();
}

//  bool QBasicReadWriteLock::tryLockForRead()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock14tryLockForReadEv(
    QBasicReadWriteLock *self) {
  return self->tryLockForRead();
}

//  bool QBasicReadWriteLock::tryLockForRead(QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock14tryLockForReadE14QDeadlineTimer(
    QBasicReadWriteLock *self,
    const QDeadlineTimer *timeout) {
  return self->tryLockForRead(*timeout);
}

//  void QBasicReadWriteLock::lockForWrite()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock12lockForWriteEv(
    QBasicReadWriteLock *self) {
  self->lockForWrite();
}

//  bool QBasicReadWriteLock::tryLockForWrite()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock15tryLockForWriteEv(
    QBasicReadWriteLock *self) {
  return self->tryLockForWrite();
}

//  bool QBasicReadWriteLock::tryLockForWrite(QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock15tryLockForWriteE14QDeadlineTimer(
    QBasicReadWriteLock *self,
    const QDeadlineTimer *timeout) {
  return self->tryLockForWrite(*timeout);
}

//  void QBasicReadWriteLock::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock6unlockEv(QBasicReadWriteLock *self) {
  self->unlock();
}

//  void QBasicReadWriteLock::lock()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock4lockEv(QBasicReadWriteLock *self) {
  self->lock();
}

//  void QBasicReadWriteLock::lock_shared()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock11lock_sharedEv(
    QBasicReadWriteLock *self) {
  self->lock_shared();
}

//  bool QBasicReadWriteLock::try_lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock8try_lockEv(QBasicReadWriteLock *self) {
  return self->try_lock();
}

//  bool QBasicReadWriteLock::try_lock_shared()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock15try_lock_sharedEv(
    QBasicReadWriteLock *self) {
  return self->try_lock_shared();
}

//  void QBasicReadWriteLock::unlock_shared()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock13unlock_sharedEv(
    QBasicReadWriteLock *self) {
  self->unlock_shared();
}

//  bool QBasicReadWriteLock::tryLockForReadInternal(QDeadlineTimer timeout,
//      unsigned int tsanFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock22tryLockForReadInternalE14QDeadlineTimerj(
    QBasicReadWriteLock *self,
    const QDeadlineTimer *timeout,
    unsigned int tsanFlags) {
  return self->tryLockForReadInternal(*timeout, tsanFlags);
}

//  bool QBasicReadWriteLock::tryLockForWriteInternal(QDeadlineTimer timeout,
//      unsigned int tsanFlags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock23tryLockForWriteInternalE14QDeadlineTimerj(
    QBasicReadWriteLock *self,
    const QDeadlineTimer *timeout,
    unsigned int tsanFlags) {
  return self->tryLockForWriteInternal(*timeout, tsanFlags);
}
