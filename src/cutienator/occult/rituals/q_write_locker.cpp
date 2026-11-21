//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qreadwritelock.h>

//  QWriteLocker::QWriteLocker(QReadWriteLock *readWriteLock)
extern "C" Q_DECL_EXPORT
QWriteLocker *ritual_ZN12QWriteLockerC1EP14QReadWriteLock(
    QReadWriteLock *readWriteLock) {
  return new QWriteLocker(readWriteLock);
}

//  QWriteLocker::~QWriteLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWriteLockerD1Ev(QWriteLocker *self) {
  delete self;
}

//  void QWriteLocker::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWriteLocker6unlockEv(QWriteLocker *self) {
  self->unlock();
}

//  void QWriteLocker::relock()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWriteLocker6relockEv(QWriteLocker *self) {
  self->relock();
}

//  QReadWriteLock *QWriteLocker::readWriteLock() const
extern "C" Q_DECL_EXPORT
QReadWriteLock *ritual_ZNK12QWriteLocker13readWriteLockEv(
    const QWriteLocker *self) {
  return self->readWriteLock();
}
