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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 179, as _ZN3QV419ExecutableAllocator4freeEPNS0_10AllocationE
namespace QV4 {
inline void ExecutableAllocator::free(Allocation *allocation)
{
    QMutexLocker locker(&mutex);

    Q_ASSERT(allocation);

    allocation->free = true;

    QMap<quintptr, ChunkOfPages*>::Iterator it = chunks.lowerBound(allocation->addr);
    if (it != chunks.begin())
        --it;
    Q_ASSERT(it != chunks.end());
    ChunkOfPages *chunk = *it;
    Q_ASSERT(chunk->contains(allocation));

    bool merged = allocation->mergeNext(this);
    merged |= allocation->mergePrevious(this);
    if (!merged)
        freeAllocations.insert(allocation->size, allocation);

    allocation = nullptr;

    if (!chunk->firstAllocation->next) {
        freeAllocations.remove(chunk->firstAllocation->size, chunk->firstAllocation);
        chunks.erase(it);
        delete chunk;
        return;
    }
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 23, as _ZNK3QV419ExecutableAllocator10Allocation11memoryStartEv
namespace QV4 {
inline void *ExecutableAllocator::Allocation::memoryStart() const
{
    return reinterpret_cast<void*>(addr);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 13, as _ZNK3QV419ExecutableAllocator10Allocation21exceptionHandlerStartEv
namespace QV4 {
inline void *ExecutableAllocator::Allocation::exceptionHandlerStart() const
{
    return reinterpret_cast<void*>(addr);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4executableallocator.cpp, line 41, as _ZN3QV419ExecutableAllocator10Allocation5splitEm
namespace QV4 {
inline ExecutableAllocator::Allocation *ExecutableAllocator::Allocation::split(size_t dividingSize)
{
    Allocation *remainder = new Allocation;
    if (next)
        next->prev = remainder;

    remainder->next = next;
    next = remainder;

    remainder->prev = this;

    remainder->size = size - dividingSize;
    remainder->free = free;
    remainder->addr = addr + dividingSize;
    size = dividingSize;

    return remainder;
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
//  -----------------------------------------------------------------------

//  QV4::ExecutableAllocator::Allocation::Allocation()
extern "C" Q_DECL_EXPORT
QV4::ExecutableAllocator::Allocation *ritual_ZN3QV419ExecutableAllocator10AllocationC1Ev() {
  return new QV4::ExecutableAllocator::Allocation();
}

//  void *QV4::ExecutableAllocator::Allocation::memoryStart() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK3QV419ExecutableAllocator10Allocation11memoryStartEv(
    const QV4::ExecutableAllocator::Allocation *self) {
  return self->memoryStart();
}

//  size_t QV4::ExecutableAllocator::Allocation::memorySize() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV419ExecutableAllocator10Allocation10memorySizeEv(
    const QV4::ExecutableAllocator::Allocation *self) {
  return self->memorySize();
}

//  void *QV4::ExecutableAllocator::Allocation::exceptionHandlerStart() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK3QV419ExecutableAllocator10Allocation21exceptionHandlerStartEv(
    const QV4::ExecutableAllocator::Allocation *self) {
  return self->exceptionHandlerStart();
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

//  Allocation *QV4::ExecutableAllocator::Allocation::split(size_t
//      dividingSize)
extern "C" Q_DECL_EXPORT
QV4::ExecutableAllocator::Allocation *ritual_ZN3QV419ExecutableAllocator10Allocation5splitEm(
    QV4::ExecutableAllocator::Allocation *self,
    size_t dividingSize) {
  return self->split(dividingSize);
}

//  bool QV4::ExecutableAllocator::Allocation::mergeNext(ExecutableAllocator
//      *allocator)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV419ExecutableAllocator10Allocation9mergeNextEPS0_(
    QV4::ExecutableAllocator::Allocation *self,
    QV4::ExecutableAllocator *allocator) {
  return self->mergeNext(allocator);
}

//  bool
//      QV4::ExecutableAllocator::Allocation::mergePrevious(ExecutableAllocat
//      or *allocator)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV419ExecutableAllocator10Allocation13mergePreviousEPS0_(
    QV4::ExecutableAllocator::Allocation *self,
    QV4::ExecutableAllocator *allocator) {
  return self->mergePrevious(allocator);
}
