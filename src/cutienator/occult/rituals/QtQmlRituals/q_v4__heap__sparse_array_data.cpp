//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::SparseArrayData::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15SparseArrayData7destroyEv(
    QV4::Heap::SparseArrayData *self) {
  self->destroy();
}

//  uint QV4::Heap::SparseArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV44Heap15SparseArrayData11mappedIndexEj(
    const QV4::Heap::SparseArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}

//  PropertyAttributes QV4::Heap::SparseArrayData::attributes(uint i) const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZNK3QV44Heap15SparseArrayData10attributesEj(
    const QV4::Heap::SparseArrayData *self,
    uint i) {
  return new QV4::PropertyAttributes(self->attributes(i));
}
