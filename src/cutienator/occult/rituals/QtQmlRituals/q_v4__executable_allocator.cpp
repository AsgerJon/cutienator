//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4executableallocator_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4executableallocator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4executableallocator_p.h>
#include <QtQml/private/qv4functiontable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 80, as _ZN3QV419ExecutableAllocator10Allocation13mergePreviousEPS0_
namespace QV4 {
inline bool ExecutableAllocator::Allocation::mergePrevious(ExecutableAllocator *allocator)
{
    Q_ASSERT(free);
    if (!prev || !prev->free)
        return false;

    allocator->freeAllocations.remove(size, this);
    allocator->freeAllocations.remove(prev->size, prev);

    prev->size += size;
    if (next)
        next->prev = prev;
    prev->next = next;

    allocator->freeAllocations.insert(prev->size, prev);

    delete this;
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 60, as _ZN3QV419ExecutableAllocator10Allocation9mergeNextEPS0_
namespace QV4 {
inline bool ExecutableAllocator::Allocation::mergeNext(ExecutableAllocator *allocator)
{
    Q_ASSERT(free);
    if (!next || !next->free)
        return false;

    allocator->freeAllocations.remove(size, this);
    allocator->freeAllocations.remove(next->size, next);

    size += next->size;
    Allocation *newNext = next->next;
    delete next;
    next = newNext;
    if (next)
        next->prev = this;

    allocator->freeAllocations.insert(size, this);
    return true;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 113, as _ZNK3QV419ExecutableAllocator12ChunkOfPages8containsEPNS0_10AllocationE
namespace QV4 {
inline bool ExecutableAllocator::ChunkOfPages::contains(Allocation *alloc) const
{
    Allocation *it = firstAllocation;
    while (it) {
        if (it == alloc)
            return true;
        it = it->next;
    }
    return false;
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 124, as _ZN3QV419ExecutableAllocatorC1Ev
namespace QV4 {
inline ExecutableAllocator::ExecutableAllocator()
    = default;
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 209, as _ZNK3QV419ExecutableAllocator18chunkForAllocationEPNS0_10AllocationE
namespace QV4 {
inline ExecutableAllocator::ChunkOfPages *ExecutableAllocator::chunkForAllocation(Allocation *allocation) const
{
    QMutexLocker locker(&mutex);

    QMap<quintptr, ChunkOfPages*>::ConstIterator it = chunks.lowerBound(allocation->addr);
    if (it != chunks.begin())
        --it;
    if (it == chunks.end())
        return nullptr;
    return *it;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  QV4::ExecutableAllocator::ExecutableAllocator()
extern "C" Q_DECL_EXPORT
QV4::ExecutableAllocator *ritual_ZN3QV419ExecutableAllocatorC1Ev() {
  return new QV4::ExecutableAllocator();
}

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

//  ChunkOfPages *QV4::ExecutableAllocator::chunkForAllocation(Allocation
//      *allocation) const
extern "C" Q_DECL_EXPORT
QV4::ExecutableAllocator::ChunkOfPages *ritual_ZNK3QV419ExecutableAllocator18chunkForAllocationEPNS0_10AllocationE(
    const QV4::ExecutableAllocator *self,
    QV4::ExecutableAllocator::Allocation *allocation) {
  return self->chunkForAllocation(allocation);
}
