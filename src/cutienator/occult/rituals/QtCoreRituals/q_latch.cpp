//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlatch_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlatch_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QLatch::QLatch(int expected)
extern "C" Q_DECL_EXPORT
QLatch *ritual_ZN6QLatchC1Ei(int expected) {
  return new QLatch(expected);
}

//  int QLatch::pending() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK6QLatch7pendingEv(const QLatch *self) {
  return self->pending();
}

//  void QLatch::countDown(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch9countDownEi(QLatch *self, int n) {
  self->countDown(n);
}

//  bool QLatch::tryWait() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLatch7tryWaitEv(const QLatch *self) {
  return self->tryWait();
}

//  void QLatch::wait()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch4waitEv(QLatch *self) {
  self->wait();
}

//  void QLatch::arriveAndWait(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch13arriveAndWaitEi(QLatch *self, int n) {
  self->arriveAndWait(n);
}

//  int QLatch::max()
extern "C" Q_DECL_EXPORT
int ritual_ZN6QLatch3maxEv() {
  return QLatch::max();
}

//  void QLatch::count_down(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch10count_downEi(QLatch *self, int n) {
  self->count_down(n);
}

//  bool QLatch::try_wait() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QLatch8try_waitEv(const QLatch *self) {
  return self->try_wait();
}

//  void QLatch::arrive_and_wait(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch15arrive_and_waitEi(QLatch *self, int n) {
  self->arrive_and_wait(n);
}

//  void QLatch::waitInternal(int current)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch12waitInternalEi(QLatch *self, int current) {
  self->waitInternal(current);
}

//  void QLatch::wakeUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QLatch6wakeUpEv(QLatch *self) {
  self->wakeUp();
}
