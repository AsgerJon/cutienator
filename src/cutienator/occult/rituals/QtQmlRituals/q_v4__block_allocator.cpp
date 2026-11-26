//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt does not export 'QV4::BlockAllocator': only its inline functions
//  and its destructor are written. Not written: the constructor (and
//  with it a Cute class), and 'allocate', 'sweep', 'freeAll' and
//  'resetBlackBits', which only Qt's own library defines. The compiler
//  refused the generated file for 'ChunkAllocator', a type Qt declares
//  in QV4 and defines only in its .cpp file: no ritual here names it.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/6.12.0/QtQml/private/qv4mm_p.h>

//  QV4::BlockAllocator::~BlockAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414BlockAllocatorD1Ev(QV4::BlockAllocator *self) {
  delete self;
}

//  size_t QV4::BlockAllocator::binForSlots(size_t nSlots)
extern "C" Q_DECL_EXPORT
size_t ritual_ZN3QV414BlockAllocator11binForSlotsEm(size_t nSlots) {
  return QV4::BlockAllocator::binForSlots(nSlots);
}

//  size_t QV4::BlockAllocator::totalSlots() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV414BlockAllocator10totalSlotsEv(
    const QV4::BlockAllocator *self) {
  return self->totalSlots();
}

//  size_t QV4::BlockAllocator::allocatedMem() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV414BlockAllocator12allocatedMemEv(
    const QV4::BlockAllocator *self) {
  return self->allocatedMem();
}

//  size_t QV4::BlockAllocator::usedMem() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV414BlockAllocator7usedMemEv(
    const QV4::BlockAllocator *self) {
  return self->usedMem();
}
