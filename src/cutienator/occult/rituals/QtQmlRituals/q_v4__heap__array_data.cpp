//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraydata_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraydata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4property_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4global_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arraydata_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraydata.cpp, line 52, as _ZN3QV44Heap9ArrayData11markObjectsEPNS0_4BaseEPNS_9MarkStackE
namespace QV4 {
inline void Heap::ArrayData::markObjects(Heap::Base *base, MarkStack *stack)
{
    ArrayData *a = static_cast<ArrayData *>(base);
    a->values.mark(stack);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ArrayData::markObjects(Heap::Base *base, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9ArrayData11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *base,
    QV4::MarkStack *stack) {
  QV4::Heap::ArrayData::markObjects(base, stack);
}

//  bool QV4::Heap::ArrayData::isSparse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap9ArrayData8isSparseEv(
    const QV4::Heap::ArrayData *self) {
  return self->isSparse();
}

//  const ArrayVTable *QV4::Heap::ArrayData::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::ArrayVTable *ritual_ZNK3QV44Heap9ArrayData6vtableEv(
    const QV4::Heap::ArrayData *self) {
  return self->vtable();
}

//  ReturnedValue QV4::Heap::ArrayData::get(uint i) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV44Heap9ArrayData3getEj(
    const QV4::Heap::ArrayData *self,
    uint i) {
  return self->get(i);
}

//  bool QV4::Heap::ArrayData::getProperty(uint index, Property *p,
//      PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV44Heap9ArrayData11getPropertyEjPNS_8PropertyEPNS_18PropertyAttributesE(
    QV4::Heap::ArrayData *self,
    uint index,
    QV4::Property *p,
    QV4::PropertyAttributes *attrs) {
  return self->getProperty(index, p, attrs);
}

//  void QV4::Heap::ArrayData::setProperty(EngineBase *e, uint index, const
//      Property *p)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9ArrayData11setPropertyEPNS_10EngineBaseEjPKNS_8PropertyE(
    QV4::Heap::ArrayData *self,
    QV4::EngineBase *e,
    uint index,
    const QV4::Property *p) {
  self->setProperty(e, index, p);
}

//  PropertyIndex QV4::Heap::ArrayData::getValueOrSetter(uint index,
//      PropertyAttributes *attrs)
extern "C" Q_DECL_EXPORT
QV4::PropertyIndex *ritual_ZN3QV44Heap9ArrayData16getValueOrSetterEjPNS_18PropertyAttributesE(
    QV4::Heap::ArrayData *self,
    uint index,
    QV4::PropertyAttributes *attrs) {
  return new QV4::PropertyIndex(self->getValueOrSetter(index, attrs));
}

//  PropertyAttributes QV4::Heap::ArrayData::attributes(uint i) const
extern "C" Q_DECL_EXPORT
QV4::PropertyAttributes *ritual_ZNK3QV44Heap9ArrayData10attributesEj(
    const QV4::Heap::ArrayData *self,
    uint i) {
  return new QV4::PropertyAttributes(self->attributes(i));
}

//  bool QV4::Heap::ArrayData::isEmpty(uint i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap9ArrayData7isEmptyEj(
    const QV4::Heap::ArrayData *self,
    uint i) {
  return self->isEmpty(i);
}

//  uint QV4::Heap::ArrayData::length() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV44Heap9ArrayData6lengthEv(
    const QV4::Heap::ArrayData *self) {
  return self->length();
}

//  void QV4::Heap::ArrayData::setArrayData(EngineBase *e, uint index, Value
//      newVal)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9ArrayData12setArrayDataEPNS_10EngineBaseEjNS_5ValueE(
    QV4::Heap::ArrayData *self,
    QV4::EngineBase *e,
    uint index,
    const QV4::Value *newVal) {
  self->setArrayData(e, index, *newVal);
}

//  uint QV4::Heap::ArrayData::mappedIndex(uint index) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK3QV44Heap9ArrayData11mappedIndexEj(
    const QV4::Heap::ArrayData *self,
    uint index) {
  return self->mappedIndex(index);
}

//  QV4::Heap::ArrayData as the QV4::Heap::ArrayDataData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayDataData *ritual_cast_QV4_Heap_ArrayData_QV4_Heap_ArrayDataData(
    QV4::Heap::ArrayData *self) {
  return static_cast<QV4::Heap::ArrayDataData *>(self);
}
