//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4executableallocator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4executableallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ExecutableAllocator::Allocation::Allocation()
extern "C" Q_DECL_EXPORT
QV4::ExecutableAllocator::Allocation *ritual_ZN3QV419ExecutableAllocator10AllocationC1Ev() {
  return new QV4::ExecutableAllocator::Allocation();
}

//  void QV4::ExecutableAllocator::Allocation::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ExecutableAllocator10Allocation10invalidateEv(
    QV4::ExecutableAllocator::Allocation *self) {
  self->invalidate();
}

//  bool QV4::ExecutableAllocator::Allocation::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV419ExecutableAllocator10Allocation7isValidEv(
    const QV4::ExecutableAllocator::Allocation *self) {
  return self->isValid();
}

//  QV4::ExecutableAllocator::Allocation::~Allocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419ExecutableAllocator10AllocationD1Ev(
    QV4::ExecutableAllocator::Allocation *self) {
  delete self;
}
