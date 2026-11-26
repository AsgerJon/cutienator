//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsemaphore.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 3. Kept as it is when the
//  generator runs again.
#include <QtCore/qsemaphore.h>
#include <QtCore/qdeadlinetimer.h>
#include <chrono>

//  QSemaphore::QSemaphore(int n)
extern "C" Q_DECL_EXPORT
QSemaphore *ritual_ZN10QSemaphoreC1Ei(int n) {
  return new QSemaphore(n);
}

//  QSemaphore::~QSemaphore()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSemaphoreD1Ev(QSemaphore *self) {
  delete self;
}

//  void QSemaphore::acquire(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSemaphore7acquireEi(QSemaphore *self, int n) {
  self->acquire(n);
}

//  bool QSemaphore::tryAcquire(int n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore10tryAcquireEi(QSemaphore *self, int n) {
  return self->tryAcquire(n);
}

//  bool QSemaphore::tryAcquire(int n, int timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore10tryAcquireEii(
    QSemaphore *self,
    int n,
    int timeout) {
  return self->tryAcquire(n, timeout);
}

//  bool QSemaphore::tryAcquire(int n, QDeadlineTimer timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore10tryAcquireEi14QDeadlineTimer(
    QSemaphore *self,
    int n,
    const QDeadlineTimer *timeout) {
  return self->tryAcquire(n, *timeout);
}

//  void QSemaphore::release(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QSemaphore7releaseEi(QSemaphore *self, int n) {
  self->release(n);
}

//  int QSemaphore::available() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QSemaphore9availableEv(const QSemaphore *self) {
  return self->available();
}

//  bool QSemaphore::try_acquire()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore11try_acquireEv(QSemaphore *self) {
  return self->try_acquire();
}

//  bool QSemaphore::tryAcquire(int n, std::chrono::milliseconds timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore10tryAcquireIlSt5ratioILl1ELl1000EEEEbiNSt6chrono8durationIT_T0_EE(
    QSemaphore *self,
    int n,
    long long timeout) {
  return self->tryAcquire(n, std::chrono::milliseconds(timeout));
}

//  bool QSemaphore::try_acquire_for(const std::chrono::milliseconds
//      &timeout)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore15try_acquire_forIlSt5ratioILl1ELl1000EEEEbRKNSt6chrono8durationIT_T0_EE(
    QSemaphore *self,
    long long timeout) {
  return self->try_acquire_for(std::chrono::milliseconds(timeout));
}

//  bool QSemaphore::try_acquire_until(const
//      std::chrono::steady_clock::time_point &tp)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QSemaphore17try_acquire_untilINSt6chrono3_V212steady_clockENS1_8durationIlSt5ratioILl1ELl1000000000EEEEEEbRKNS1_10time_pointIT_T0_EE(
    QSemaphore *self,
    long long nanoseconds) {
  return self->try_acquire_until(
      std::chrono::steady_clock::time_point(
          std::chrono::nanoseconds(nanoseconds)));
}
