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

//  const QV4::VTable *QV4::SparseArrayData::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415SparseArrayData12staticVTableEv() {
  return QV4::SparseArrayData::staticVTable();
}

//  void QV4::SparseArrayData::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData10__dataTestEv(
    QV4::SparseArrayData *self) {
  self->__dataTest();
}

//  const Data *QV4::SparseArrayData::d() const
extern "C" Q_DECL_EXPORT
const QV4::SparseArrayData::Data *ritual_ZNK3QV415SparseArrayData1dEv(
    const QV4::SparseArrayData *self) {
  return self->d();
}

//  Data *QV4::SparseArrayData::d()
extern "C" Q_DECL_EXPORT
QV4::SparseArrayData::Data *ritual_ZN3QV415SparseArrayData1dEv(
    QV4::SparseArrayData *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::SparseArrayData::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV415SparseArrayData20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::SparseArrayData::defaultInternalClass(e);
}

//  void QV4::SparseArrayData::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::SparseArrayData::virtualDestroy(b);
}

//  SparseArray *QV4::SparseArrayData::sparse() const
extern "C" Q_DECL_EXPORT
QV4::SparseArray *ritual_ZNK3QV415SparseArrayData6sparseEv(
    const QV4::SparseArrayData *self) {
  return self->sparse();
}

//  void QV4::SparseArrayData::setSparse(SparseArray *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData9setSparseEPNS_11SparseArrayE(
    QV4::SparseArrayData *self,
    QV4::SparseArray *s) {
  self->setSparse(s);
}

//  uint QV4::SparseArrayData::allocate(Object *o, bool doubleSlot)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV415SparseArrayData8allocateEPNS_6ObjectEb(
    QV4::Object *o,
    bool doubleSlot) {
  return QV4::SparseArrayData::allocate(o, doubleSlot);
}

//  void QV4::SparseArrayData::free(Heap::ArrayData *d, uint idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData4freeEPNS_4Heap9ArrayDataEj(
    QV4::Heap::ArrayData *d,
    uint idx) {
  QV4::SparseArrayData::free(d, idx);
}

//  uint QV4::SparseArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SparseArrayData11mappedIndexEj(
    const QV4::SparseArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}

//  Heap::ArrayData *QV4::SparseArrayData::reallocate(Object *o, uint n, bool
//      enforceAttributes)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayData *ritual_ZN3QV415SparseArrayData10reallocateEPNS_6ObjectEjb(
    QV4::Object *o,
    uint n,
    bool enforceAttributes) {
  return QV4::SparseArrayData::reallocate(o, n, enforceAttributes);
}

//  ReturnedValue QV4::SparseArrayData::get(const Heap::ArrayData *d, uint
//      index)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415SparseArrayData3getEPKNS_4Heap9ArrayDataEj(
    const QV4::Heap::ArrayData *d,
    uint index) {
  return QV4::SparseArrayData::get(d, index);
}

//  bool QV4::SparseArrayData::put(Object *o, uint index, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415SparseArrayData3putEPNS_6ObjectEjRKNS_5ValueE(
    QV4::Object *o,
    uint index,
    const QV4::Value *value) {
  return QV4::SparseArrayData::put(o, index, *value);
}

//  bool QV4::SparseArrayData::putArray(Object *o, uint index, const Value
//      *values, uint n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415SparseArrayData8putArrayEPNS_6ObjectEjPKNS_5ValueEj(
    QV4::Object *o,
    uint index,
    const QV4::Value *values,
    uint n) {
  return QV4::SparseArrayData::putArray(o, index, values, n);
}

//  bool QV4::SparseArrayData::del(Object *o, uint index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415SparseArrayData3delEPNS_6ObjectEj(
    QV4::Object *o,
    uint index) {
  return QV4::SparseArrayData::del(o, index);
}

//  void QV4::SparseArrayData::setAttribute(Object *o, uint index,
//      PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData12setAttributeEPNS_6ObjectEjNS_18PropertyAttributesE(
    QV4::Object *o,
    uint index,
    const QV4::PropertyAttributes *attrs) {
  QV4::SparseArrayData::setAttribute(o, index, *attrs);
}

//  void QV4::SparseArrayData::push_front(Object *o, const Value *values,
//      uint n)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SparseArrayData10push_frontEPNS_6ObjectEPKNS_5ValueEj(
    QV4::Object *o,
    const QV4::Value *values,
    uint n) {
  QV4::SparseArrayData::push_front(o, values, n);
}

//  ReturnedValue QV4::SparseArrayData::pop_front(Object *o)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415SparseArrayData9pop_frontEPNS_6ObjectE(
    QV4::Object *o) {
  return QV4::SparseArrayData::pop_front(o);
}

//  uint QV4::SparseArrayData::truncate(Object *o, uint newLen)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV415SparseArrayData8truncateEPNS_6ObjectEj(
    QV4::Object *o,
    uint newLen) {
  return QV4::SparseArrayData::truncate(o, newLen);
}

//  uint QV4::SparseArrayData::length(const Heap::ArrayData *d)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV415SparseArrayData6lengthEPKNS_4Heap9ArrayDataE(
    const QV4::Heap::ArrayData *d) {
  return QV4::SparseArrayData::length(d);
}
