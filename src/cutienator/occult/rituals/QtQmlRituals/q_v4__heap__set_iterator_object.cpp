//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4setiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4setiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::SetIteratorObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap17SetIteratorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::SetIteratorObject::markObjects(b, stack);
}

//  void QV4::Heap::SetIteratorObject::init(Object *obj, QV4::ExecutionEngine
//      *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap17SetIteratorObject4initEPNS0_6ObjectEPNS_15ExecutionEngineE(
    QV4::Heap::SetIteratorObject *self,
    QV4::Heap::Object *obj,
    QV4::ExecutionEngine *engine) {
  self->init(obj, engine);
}

//  QV4::Heap::SetIteratorObject as the QV4::Heap::SetIteratorObjectData it
//      is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::SetIteratorObjectData *ritual_cast_QV4_Heap_SetIteratorObject_QV4_Heap_SetIteratorObjectData(
    QV4::Heap::SetIteratorObject *self) {
  return static_cast<QV4::Heap::SetIteratorObjectData *>(self);
}
