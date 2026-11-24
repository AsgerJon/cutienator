//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mm_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::HugeItemAllocator::HugeChunk::~HugeChunk()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417HugeItemAllocator9HugeChunkD1Ev(
    QV4::HugeItemAllocator::HugeChunk *self) {
  delete self;
}
