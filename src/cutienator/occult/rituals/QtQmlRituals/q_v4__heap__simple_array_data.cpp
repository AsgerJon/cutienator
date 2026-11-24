//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  uint QV4::Heap::SimpleArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV44Heap15SimpleArrayData11mappedIndexEj(
    const QV4::Heap::SimpleArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}

//  const Value &QV4::Heap::SimpleArrayData::data(uint index) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV44Heap15SimpleArrayData4dataEj(
    const QV4::Heap::SimpleArrayData *self,
    uint index) {
  return new QV4::Value(self->data(index));
}

//  void QV4::Heap::SimpleArrayData::setData(EngineBase *e, uint index, Value
//      newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15SimpleArrayData7setDataEPNS_10EngineBaseEjNS_5ValueE(
    QV4::Heap::SimpleArrayData *self,
    QV4::EngineBase *e,
    uint index,
    const QV4::Value *newVal) {
  self->setData(e, index, *newVal);
}

//  PropertyAttributes QV4::Heap::SimpleArrayData::attributes(uint i) const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZNK3QV44Heap15SimpleArrayData10attributesEj(
    const QV4::Heap::SimpleArrayData *self,
    uint i) {
  return new QV4::PropertyAttributes(self->attributes(i));
}
