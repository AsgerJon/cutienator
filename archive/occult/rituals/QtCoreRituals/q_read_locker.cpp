//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qreadwritelock.h>

//  QReadLocker::QReadLocker(QReadWriteLock *readWriteLock)
extern "C" Q_DECL_EXPORT
QReadLocker *ritual_ZN11QReadLockerC1EP14QReadWriteLock(
    QReadWriteLock *readWriteLock) {
  return new QReadLocker(readWriteLock);
}

//  QReadLocker::~QReadLocker()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QReadLockerD1Ev(QReadLocker *self) {
  delete self;
}

//  void QReadLocker::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QReadLocker6unlockEv(QReadLocker *self) {
  self->unlock();
}

//  void QReadLocker::relock()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QReadLocker6relockEv(QReadLocker *self) {
  self->relock();
}

//  QReadWriteLock *QReadLocker::readWriteLock() const
extern "C" Q_DECL_EXPORT
QReadWriteLock *ritual_ZNK11QReadLocker13readWriteLockEv(
    const QReadLocker *self) {
  return self->readWriteLock();
}
