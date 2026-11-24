//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mmdefs_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  HeapItem *QV4::Chunk::realBase()
extern "C" Q_DECL_EXPORT
QV4::HeapItem *ritual_ZN3QV45Chunk8realBaseEv(QV4::Chunk *self) {
  return self->realBase();
}

//  HeapItem *QV4::Chunk::first()
extern "C" Q_DECL_EXPORT
QV4::HeapItem *ritual_ZN3QV45Chunk5firstEv(QV4::Chunk *self) {
  return self->first();
}

//  quintptr QV4::Chunk::bitForIndex(size_t index)
extern "C" Q_DECL_EXPORT
quintptr ritual_ZN3QV45Chunk11bitForIndexEm(size_t index) {
  return QV4::Chunk::bitForIndex(index);
}

//  void QV4::Chunk::setBit(quintptr *bitmap, size_t index)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45Chunk6setBitEPym(quintptr *bitmap, size_t index) {
  QV4::Chunk::setBit(bitmap, index);
}

//  void QV4::Chunk::clearBit(quintptr *bitmap, size_t index)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45Chunk8clearBitEPym(quintptr *bitmap, size_t index) {
  QV4::Chunk::clearBit(bitmap, index);
}

//  bool QV4::Chunk::testBit(quintptr *bitmap, size_t index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV45Chunk7testBitEPym(quintptr *bitmap, size_t index) {
  return QV4::Chunk::testBit(bitmap, index);
}

//  void QV4::Chunk::setBits(quintptr *bitmap, size_t index, size_t nBits)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45Chunk7setBitsEPymm(
    quintptr *bitmap,
    size_t index,
    size_t nBits) {
  QV4::Chunk::setBits(bitmap, index, nBits);
}

//  bool QV4::Chunk::hasNonZeroBit(quintptr *bitmap)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV45Chunk13hasNonZeroBitEPy(quintptr *bitmap) {
  return QV4::Chunk::hasNonZeroBit(bitmap);
}

//  uint QV4::Chunk::lowestNonZeroBit(quintptr *bitmap)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV45Chunk16lowestNonZeroBitEPy(quintptr *bitmap) {
  return QV4::Chunk::lowestNonZeroBit(bitmap);
}

//  uint QV4::Chunk::nFreeSlots() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV45Chunk10nFreeSlotsEv(const QV4::Chunk *self) {
  return self->nFreeSlots();
}

//  uint QV4::Chunk::nUsedSlots() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV45Chunk10nUsedSlotsEv(const QV4::Chunk *self) {
  return self->nUsedSlots();
}

//  QV4::Chunk::~Chunk()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45ChunkD1Ev(QV4::Chunk *self) {
  delete self;
}
