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

//  const QV4::VTable *QV4::ArrayData::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV49ArrayData12staticVTableEv() {
  return QV4::ArrayData::staticVTable();
}

//  void QV4::ArrayData::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayData10__dataTestEv(QV4::ArrayData *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayData *QV4::ArrayData::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayData *ritual_ZNK3QV49ArrayData11d_uncheckedEv(
    const QV4::ArrayData *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayData *QV4::ArrayData::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayData *ritual_ZNK3QV49ArrayData1dEv(
    const QV4::ArrayData *self) {
  return self->d();
}

//  uint QV4::ArrayData::alloc() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV49ArrayData5allocEv(const QV4::ArrayData *self) {
  return self->alloc();
}

//  void QV4::ArrayData::setAlloc(uint a)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayData8setAllocEj(QV4::ArrayData *self, uint a) {
  self->setAlloc(a);
}

//  void QV4::ArrayData::setType(Type t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayData7setTypeENS_4Heap9ArrayData4TypeE(
    QV4::ArrayData *self,
    QV4::ArrayData::Type t) {
  self->setType(t);
}

//  PropertyAttributes *QV4::ArrayData::attrs() const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZNK3QV49ArrayData5attrsEv(
    const QV4::ArrayData *self) {
  return self->attrs();
}

//  void QV4::ArrayData::setAttrs(PropertyAttributes *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayData8setAttrsEPNS_18PropertyAttributesE(
    QV4::ArrayData *self,
    QV4::PropertyAttributes *a) {
  self->setAttrs(a);
}

//  const Value *QV4::ArrayData::arrayData() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV49ArrayData9arrayDataEv(
    const QV4::ArrayData *self) {
  return self->arrayData();
}

//  void QV4::ArrayData::setArrayData(EngineBase *e, uint index, Value
//      newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayData12setArrayDataEPNS_10EngineBaseEjNS_5ValueE(
    QV4::ArrayData *self,
    QV4::EngineBase *e,
    uint index,
    const QV4::Value *newVal) {
  self->setArrayData(e, index, *newVal);
}

//  const ArrayVTable *QV4::ArrayData::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::ArrayVTable *ritual_ZNK3QV49ArrayData6vtableEv(
    const QV4::ArrayData *self) {
  return self->vtable();
}

//  bool QV4::ArrayData::isSparse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49ArrayData8isSparseEv(const QV4::ArrayData *self) {
  return self->isSparse();
}

//  uint QV4::ArrayData::length() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV49ArrayData6lengthEv(const QV4::ArrayData *self) {
  return self->length();
}

//  bool QV4::ArrayData::hasAttributes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49ArrayData13hasAttributesEv(const QV4::ArrayData *self) {
  return self->hasAttributes();
}

//  PropertyAttributes QV4::ArrayData::attributes(uint i) const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZNK3QV49ArrayData10attributesEj(
    const QV4::ArrayData *self,
    uint i) {
  return new QV4::PropertyAttributes(self->attributes(i));
}

//  bool QV4::ArrayData::isEmpty(uint i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49ArrayData7isEmptyEj(const QV4::ArrayData *self, uint i) {
  return self->isEmpty(i);
}

//  ReturnedValue QV4::ArrayData::get(uint i) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV49ArrayData3getEj(
    const QV4::ArrayData *self,
    uint i) {
  return self->get(i);
}

//  void QV4::ArrayData::realloc(Object *o, Type newType, uint alloc, bool
//      enforceAttributes)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayData7reallocEPNS_6ObjectENS_4Heap9ArrayData4TypeEjb(
    QV4::Object *o,
    QV4::ArrayData::Type newType,
    uint alloc,
    bool enforceAttributes) {
  QV4::ArrayData::realloc(o, newType, alloc, enforceAttributes);
}
