//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdeadlinetimer.h>

//  QV4::MarkStack::MarkStack(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::MarkStack *ritual_ZN3QV49MarkStackC1EPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *engine) {
  return new QV4::MarkStack(engine);
}

//  QV4::MarkStack::~MarkStack()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MarkStackD1Ev(QV4::MarkStack *self) {
  delete self;
}

//  void QV4::MarkStack::push(Heap::Base *m)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MarkStack4pushEPNS_4Heap4BaseE(
    QV4::MarkStack *self,
    QV4::Heap::Base *m) {
  self->push(m);
}

//  bool QV4::MarkStack::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49MarkStack7isEmptyEv(const QV4::MarkStack *self) {
  return self->isEmpty();
}

//  qptrdiff QV4::MarkStack::remainingBeforeSoftLimit() const
extern "C" Q_DECL_EXPORT
qptrdiff ritual_ZNK3QV49MarkStack24remainingBeforeSoftLimitEv(
    const QV4::MarkStack *self) {
  return self->remainingBeforeSoftLimit();
}

//  ExecutionEngine *QV4::MarkStack::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK3QV49MarkStack6engineEv(
    const QV4::MarkStack *self) {
  return self->engine();
}

//  void QV4::MarkStack::drain()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MarkStack5drainEv(QV4::MarkStack *self) {
  self->drain();
}

//  DrainState QV4::MarkStack::drain(QDeadlineTimer deadline)
extern "C" Q_DECL_EXPORT
QV4::MarkStack::DrainState ritual_ZN3QV49MarkStack5drainE14QDeadlineTimer(
    QV4::MarkStack *self,
    const QDeadlineTimer *deadline) {
  return self->drain(*deadline);
}

//  void QV4::MarkStack::setSoftLimit(size_t size)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MarkStack12setSoftLimitEm(
    QV4::MarkStack *self,
    size_t size) {
  self->setSoftLimit(size);
}

//  Heap::Base *QV4::MarkStack::pop()
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZN3QV49MarkStack3popEv(QV4::MarkStack *self) {
  return self->pop();
}
