//  Written by hand on 2026-11-25 from
//  QtQml/6.12.0/QtQml/private/qv4mm_p.h, Qt 6.12.0, from Qt's source.
//  Kept as it is when the generator runs again.
//  Qt does not export 'QV4::HugeItemAllocator': only its inline
//  functions and its destructor are written. Not written: the
//  constructor (and with it a Cute class), and 'allocate', 'sweep',
//  'freeAll' and 'resetBlackBits', which only Qt's own library defines.
//  The compiler refused the generated file for 'ChunkAllocator', a type
//  Qt declares in QV4 and defines only in its .cpp file: no ritual here
//  names it.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#include <QtQml/6.12.0/QtQml/private/qv4mm_p.h>

//  QV4::HugeItemAllocator::~HugeItemAllocator()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417HugeItemAllocatorD1Ev(QV4::HugeItemAllocator *self) {
  delete self;
}

//  size_t QV4::HugeItemAllocator::usedMem() const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK3QV417HugeItemAllocator7usedMemEv(
    const QV4::HugeItemAllocator *self) {
  return self->usedMem();
}
