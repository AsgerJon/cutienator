//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmutex.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(thread) || defined(Q_QDOC)
#include <QtCore/qmutex.h>
#include <QtCore/qdeadlinetimer.h>

//  QRecursiveMutex::QRecursiveMutex()
extern "C" Q_DECL_EXPORT
QRecursiveMutex *ritual_ZN15QRecursiveMutexC1Ev() {
  return new QRecursiveMutex();
}

//  QRecursiveMutex::~QRecursiveMutex()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRecursiveMutexD1Ev(QRecursiveMutex *self) {
  delete self;
}

//  void QRecursiveMutex::lock()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRecursiveMutex4lockEv(QRecursiveMutex *self) {
  self->lock();
}

//  bool QRecursiveMutex::tryLock(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QRecursiveMutex7tryLockEi(
    QRecursiveMutex *self,
    int timeout) {
  return self->tryLock(timeout);
}

//  bool QRecursiveMutex::tryLock(QDeadlineTimer timer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QRecursiveMutex7tryLockE14QDeadlineTimer(
    QRecursiveMutex *self,
    const QDeadlineTimer *timer) {
  return self->tryLock(*timer);
}

//  void QRecursiveMutex::unlock()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QRecursiveMutex6unlockEv(QRecursiveMutex *self) {
  self->unlock();
}

//  bool QRecursiveMutex::try_lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QRecursiveMutex8try_lockEv(QRecursiveMutex *self) {
  return self->try_lock();
}

#endif  // QT_CONFIG(thread) || defined(Q_QDOC)
