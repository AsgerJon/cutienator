//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4executableallocator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4executableallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QV4::ExecutableAllocator::freeAllocationCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV419ExecutableAllocator19freeAllocationCountEv(
    const QV4::ExecutableAllocator *self) {
  return self->freeAllocationCount();
}

//  int QV4::ExecutableAllocator::chunkCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV419ExecutableAllocator10chunkCountEv(
    const QV4::ExecutableAllocator *self) {
  return self->chunkCount();
}
