//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qreadwritelock.h, Qt 6.12.0. Edited by hand on 2026-11-25: added
//  by hand, rituals for functions the generator leaves out: 2. Kept as it is
//  when the generator runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(thread)
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

//  bool QBasicReadWriteLock::contendedTryLockForRead(QDeadlineTimer timeout,
//      void *dd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock23contendedTryLockForReadE14QDeadlineTimerPv(
    QBasicReadWriteLock *self,
    const QDeadlineTimer *timeout,
    void *dd) {
  return self->contendedTryLockForRead(*timeout, dd);
}

//  bool QBasicReadWriteLock::contendedTryLockForWrite(QDeadlineTimer
//      timeout, void *dd)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock24contendedTryLockForWriteE14QDeadlineTimerPv(
    QBasicReadWriteLock *self,
    const QDeadlineTimer *timeout,
    void *dd) {
  return self->contendedTryLockForWrite(*timeout, dd);
}

//  void QBasicReadWriteLock::contendedUnlock(void *dd)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QBasicReadWriteLock15contendedUnlockEPv(
    QBasicReadWriteLock *self,
    void *dd) {
  self->contendedUnlock(dd);
}

//  quintptr QBasicReadWriteLock::describeLockInternal(void *dd)
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN19QBasicReadWriteLock20describeLockInternalEPv(void *dd) {
  return QBasicReadWriteLock::describeLockInternal(dd);
}

//  uint QBasicReadWriteLock::describeLockForTSan(QReadWriteLockPrivate *d,
//      uint flags)
extern "C" Q_DECL_EXPORT
uint ritual_ZN19QBasicReadWriteLock19describeLockForTSanEP21QReadWriteLockPrivatej(
    QReadWriteLockPrivate *d,
    uint flags) {
  return QBasicReadWriteLock::describeLockForTSan(d, flags);
}

//  QBasicReadWriteLock::QBasicReadWriteLock(QReadWriteLockPrivate *d)
extern "C" Q_DECL_EXPORT
QBasicReadWriteLock *ritual_ZN19QBasicReadWriteLockC1EP21QReadWriteLockPrivate(
    QReadWriteLockPrivate *d) {
  return new QBasicReadWriteLock(d);
}

//  bool QBasicReadWriteLock::fastTryLockForRead(QReadWriteLockPrivate *&d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock18fastTryLockForReadERP21QReadWriteLockPrivate(
    QBasicReadWriteLock *self,
    QReadWriteLockPrivate **d) {
  return self->fastTryLockForRead(*d);
}

//  bool QBasicReadWriteLock::fastTryLockForWrite(QReadWriteLockPrivate *&d)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QBasicReadWriteLock19fastTryLockForWriteERP21QReadWriteLockPrivate(
    QBasicReadWriteLock *self,
    QReadWriteLockPrivate **d) {
  return self->fastTryLockForWrite(*d);
}

#endif  // QT_CONFIG(thread)
