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
//  -----------------------------------------------------------------------

//  QV4::ExecutableAllocator::ChunkOfPages::ChunkOfPages()
extern "C" Q_DECL_EXPORT
QV4::ExecutableAllocator::ChunkOfPages *ritual_ZN3QV419ExecutableAllocator12ChunkOfPagesC1Ev() {
  return new QV4::ExecutableAllocator::ChunkOfPages();
}

//  bool QV4::ExecutableAllocator::ChunkOfPages::contains(Allocation *alloc)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV419ExecutableAllocator12ChunkOfPages8containsEPNS0_10AllocationE(
    const QV4::ExecutableAllocator::ChunkOfPages *self,
    QV4::ExecutableAllocator::Allocation *alloc) {
  return self->contains(alloc);
}
