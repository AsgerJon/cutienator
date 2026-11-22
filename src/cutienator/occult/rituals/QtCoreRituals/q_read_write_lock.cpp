//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qreadwritelock.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qreadwritelock.h>

//  QReadWriteLock::QReadWriteLock(RecursionMode recursionMode)
extern "C" Q_DECL_EXPORT
QReadWriteLock *ritual_ZN14QReadWriteLockC1ENS_13RecursionModeE(
    QReadWriteLock::RecursionMode recursionMode) {
  return new QReadWriteLock(recursionMode);
}

//  QReadWriteLock::~QReadWriteLock()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QReadWriteLockD1Ev(QReadWriteLock *self) {
  delete self;
}

//  bool QReadWriteLock::tryLockForRead(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QReadWriteLock14tryLockForReadEi(
    QReadWriteLock *self,
    int timeout) {
  return self->tryLockForRead(timeout);
}

//  bool QReadWriteLock::tryLockForWrite(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QReadWriteLock15tryLockForWriteEi(
    QReadWriteLock *self,
    int timeout) {
  return self->tryLockForWrite(timeout);
}
