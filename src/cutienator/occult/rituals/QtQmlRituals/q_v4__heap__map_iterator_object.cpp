//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::MapIteratorObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap17MapIteratorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::MapIteratorObject::markObjects(b, stack);
}

//  void QV4::Heap::MapIteratorObject::init(Object *obj, QV4::ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap17MapIteratorObject4initEPNS0_6ObjectEPNS_15ExecutionEngineE(
    QV4::Heap::MapIteratorObject *self,
    QV4::Heap::Object *obj,
    QV4::ExecutionEngine *engine) {
  self->init(obj, engine);
}

//  QV4::Heap::MapIteratorObject as the QV4::Heap::MapIteratorObjectData it
//      is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::MapIteratorObjectData *ritual_cast_QV4_Heap_MapIteratorObject_QV4_Heap_MapIteratorObjectData(
    QV4::Heap::MapIteratorObject *self) {
  return static_cast<QV4::Heap::MapIteratorObjectData *>(self);
}
