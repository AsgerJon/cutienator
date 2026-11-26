//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmutex.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by hand,
//  instances of templates of the class: 1. Kept as it is when the generator
//  runs again.
#include <QtCore/qglobal.h>
#if QT_CONFIG(thread) || defined(Q_QDOC)
#include <QtCore/qmutex.h>
#include <QtCore/qdeadlinetimer.h>
#include <chrono>

//  QMutex::QMutex()
extern "C" Q_DECL_EXPORT
QMutex *ritual_ZN6QMutexC1Ev() {
  return new QMutex();
}

//  QMutex::~QMutex()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QMutexD1Ev(QMutex *self) {
  delete self;
}

//  bool QMutex::try_lock()
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMutex8try_lockEv(QMutex *self) {
  return self->try_lock();
}

//  bool QMutex::tryLock(int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMutex7tryLockEi(QMutex *self, int timeout) {
  return self->tryLock(timeout);
}

//  bool QMutex::tryLock(QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMutex7tryLockE14QDeadlineTimer(
    QMutex *self,
    const QDeadlineTimer *timeout) {
  return self->tryLock(*timeout);
}

//  bool QMutex::try_lock_for<long, std::ratio<1,
//      1000>>(std::chrono::duration<long, std::ratio<1, 1000>> duration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QMutex12try_lock_forIlSt5ratioILl1ELl1000EEEEbNSt6chrono8durationIT_T0_EE(
    QMutex *self,
    long long duration) {
  return self->try_lock_for(std::chrono::milliseconds(duration));
}

#endif  // QT_CONFIG(thread) || defined(Q_QDOC)
