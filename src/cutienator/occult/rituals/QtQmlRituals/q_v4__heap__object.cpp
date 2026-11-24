//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4object_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4property_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::Object::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6Object4initEv(QV4::Heap::Object *self) {
  self->init();
}

//  const VTable *QV4::Heap::Object::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZNK3QV44Heap6Object6vtableEv(
    const QV4::Heap::Object *self) {
  return self->vtable();
}

//  const Value *QV4::Heap::Object::inlinePropertyDataWithOffset(uint
//      indexWithOffset) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV44Heap6Object28inlinePropertyDataWithOffsetEj(
    const QV4::Heap::Object *self,
    uint indexWithOffset) {
  return self->inlinePropertyDataWithOffset(indexWithOffset);
}

//  const Value *QV4::Heap::Object::inlinePropertyData(uint index) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV44Heap6Object18inlinePropertyDataEj(
    const QV4::Heap::Object *self,
    uint index) {
  return self->inlinePropertyData(index);
}

//  void QV4::Heap::Object::setInlinePropertyWithOffset(ExecutionEngine *e,
//      uint indexWithOffset, Value v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6Object27setInlinePropertyWithOffsetEPNS_15ExecutionEngineEjNS_5ValueE(
    QV4::Heap::Object *self,
    QV4::ExecutionEngine *e,
    uint indexWithOffset,
    const QV4::Value *v) {
  self->setInlinePropertyWithOffset(e, indexWithOffset, *v);
}

//  void QV4::Heap::Object::setInlinePropertyWithOffset(ExecutionEngine *e,
//      uint indexWithOffset, Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6Object27setInlinePropertyWithOffsetEPNS_15ExecutionEngineEjPNS0_4BaseE(
    QV4::Heap::Object *self,
    QV4::ExecutionEngine *e,
    uint indexWithOffset,
    QV4::Heap::Base *b) {
  self->setInlinePropertyWithOffset(e, indexWithOffset, b);
}

//  PropertyIndex QV4::Heap::Object::writablePropertyData(uint index)
extern "C" Q_DECL_EXPORT
QV4::PropertyIndex *ritual_ZN3QV44Heap6Object20writablePropertyDataEj(
    QV4::Heap::Object *self,
    uint index) {
  return new QV4::PropertyIndex(self->writablePropertyData(index));
}

//  const Value *QV4::Heap::Object::propertyData(uint index) const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV44Heap6Object12propertyDataEj(
    const QV4::Heap::Object *self,
    uint index) {
  return self->propertyData(index);
}

//  void QV4::Heap::Object::setProperty(ExecutionEngine *e, uint index, Value
//      v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6Object11setPropertyEPNS_15ExecutionEngineEjNS_5ValueE(
    QV4::Heap::Object *self,
    QV4::ExecutionEngine *e,
    uint index,
    const QV4::Value *v) {
  self->setProperty(e, index, *v);
}

//  void QV4::Heap::Object::setProperty(ExecutionEngine *e, uint index,
//      Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap6Object11setPropertyEPNS_15ExecutionEngineEjPNS0_4BaseE(
    QV4::Heap::Object *self,
    QV4::ExecutionEngine *e,
    uint index,
    QV4::Heap::Base *b) {
  self->setProperty(e, index, b);
}

//  Heap::Object *QV4::Heap::Object::prototype() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Object *ritual_ZNK3QV44Heap6Object9prototypeEv(
    const QV4::Heap::Object *self) {
  return self->prototype();
}

//  QV4::Heap::Object as the QV4::Heap::ObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ObjectData *ritual_cast_QV4_Heap_Object_QV4_Heap_ObjectData(
    QV4::Heap::Object *self) {
  return static_cast<QV4::Heap::ObjectData *>(self);
}
