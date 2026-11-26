//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, rituals for functions the generator leaves
//  out: 1. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::SimpleArrayData::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415SimpleArrayData12staticVTableEv() {
  return QV4::SimpleArrayData::staticVTable();
}

//  void QV4::SimpleArrayData::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SimpleArrayData10__dataTestEv(
    QV4::SimpleArrayData *self) {
  self->__dataTest();
}

//  const Data *QV4::SimpleArrayData::d() const
extern "C" Q_DECL_EXPORT
const QV4::SimpleArrayData::Data *ritual_ZNK3QV415SimpleArrayData1dEv(
    const QV4::SimpleArrayData *self) {
  return self->d();
}

//  Data *QV4::SimpleArrayData::d()
extern "C" Q_DECL_EXPORT
QV4::SimpleArrayData::Data *ritual_ZN3QV415SimpleArrayData1dEv(
    QV4::SimpleArrayData *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::SimpleArrayData::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV415SimpleArrayData20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::SimpleArrayData::defaultInternalClass(e);
}

//  uint QV4::SimpleArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SimpleArrayData11mappedIndexEj(
    const QV4::SimpleArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}

//  Value QV4::SimpleArrayData::data(uint index) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV415SimpleArrayData4dataEj(
    const QV4::SimpleArrayData *self,
    uint index) {
  return new QV4::Value(self->data(index));
}

//  uint QV4::SimpleArrayData::len() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV415SimpleArrayData3lenEv(
    const QV4::SimpleArrayData *self) {
  return self->len();
}

//  Heap::ArrayData *QV4::SimpleArrayData::reallocate(Object *o, uint n, bool
//      enforceAttributes)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayData *ritual_ZN3QV415SimpleArrayData10reallocateEPNS_6ObjectEjb(
    QV4::Object *o,
    uint n,
    bool enforceAttributes) {
  return QV4::SimpleArrayData::reallocate(o, n, enforceAttributes);
}

//  ReturnedValue QV4::SimpleArrayData::get(const Heap::ArrayData *d, uint
//      index)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415SimpleArrayData3getEPKNS_4Heap9ArrayDataEj(
    const QV4::Heap::ArrayData *d,
    uint index) {
  return QV4::SimpleArrayData::get(d, index);
}

//  bool QV4::SimpleArrayData::put(Object *o, uint index, const Value &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415SimpleArrayData3putEPNS_6ObjectEjRKNS_5ValueE(
    QV4::Object *o,
    uint index,
    const QV4::Value *value) {
  return QV4::SimpleArrayData::put(o, index, *value);
}

//  bool QV4::SimpleArrayData::putArray(Object *o, uint index, const Value
//      *values, uint n)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415SimpleArrayData8putArrayEPNS_6ObjectEjPKNS_5ValueEj(
    QV4::Object *o,
    uint index,
    const QV4::Value *values,
    uint n) {
  return QV4::SimpleArrayData::putArray(o, index, values, n);
}

//  bool QV4::SimpleArrayData::del(Object *o, uint index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415SimpleArrayData3delEPNS_6ObjectEj(
    QV4::Object *o,
    uint index) {
  return QV4::SimpleArrayData::del(o, index);
}

//  void QV4::SimpleArrayData::setAttribute(Object *o, uint index,
//      PropertyAttributes attrs)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SimpleArrayData12setAttributeEPNS_6ObjectEjNS_18PropertyAttributesE(
    QV4::Object *o,
    uint index,
    const QV4::PropertyAttributes *attrs) {
  QV4::SimpleArrayData::setAttribute(o, index, *attrs);
}

//  void QV4::SimpleArrayData::push_front(Object *o, const Value *values,
//      uint n)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415SimpleArrayData10push_frontEPNS_6ObjectEPKNS_5ValueEj(
    QV4::Object *o,
    const QV4::Value *values,
    uint n) {
  QV4::SimpleArrayData::push_front(o, values, n);
}

//  ReturnedValue QV4::SimpleArrayData::pop_front(Object *o)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415SimpleArrayData9pop_frontEPNS_6ObjectE(
    QV4::Object *o) {
  return QV4::SimpleArrayData::pop_front(o);
}

//  uint QV4::SimpleArrayData::truncate(Object *o, uint newLen)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV415SimpleArrayData8truncateEPNS_6ObjectEj(
    QV4::Object *o,
    uint newLen) {
  return QV4::SimpleArrayData::truncate(o, newLen);
}

//  uint QV4::SimpleArrayData::length(const Heap::ArrayData *d)
extern "C" Q_DECL_EXPORT
uint ritual_ZN3QV415SimpleArrayData6lengthEPKNS_4Heap9ArrayDataE(
    const QV4::Heap::ArrayData *d) {
  return QV4::SimpleArrayData::length(d);
}

//  uint &QV4::SimpleArrayData::len()
extern "C" Q_DECL_EXPORT
uint *ritual_ZN3QV415SimpleArrayData3lenEv(
    QV4::SimpleArrayData *self) {
  return &(self->len());
}
