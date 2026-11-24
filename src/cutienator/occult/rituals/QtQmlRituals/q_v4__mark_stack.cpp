//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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

//  Heap::Base *QV4::MarkStack::pop()
extern "C" Q_DECL_EXPORT
QV4::Heap::Base *ritual_ZN3QV49MarkStack3popEv(QV4::MarkStack *self) {
  return self->pop();
}
