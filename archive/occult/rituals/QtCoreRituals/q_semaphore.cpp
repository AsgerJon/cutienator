//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsemaphore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsemaphore.h>
#include <QtCore/qdeadlinetimer.h>

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
