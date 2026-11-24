//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arrayiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arrayiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ArrayIteratorObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ArrayIteratorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ArrayIteratorObject::markObjects(b, stack);
}

//  void QV4::Heap::ArrayIteratorObject::init(Object *obj,
//      QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19ArrayIteratorObject4initEPNS0_6ObjectEPNS_15ExecutionEngineE(
    QV4::Heap::ArrayIteratorObject *self,
    QV4::Heap::Object *obj,
    QV4::ExecutionEngine *engine) {
  self->init(obj, engine);
}

//  QV4::Heap::ArrayIteratorObject as the QV4::Heap::ArrayIteratorObjectData
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayIteratorObjectData *ritual_cast_QV4_Heap_ArrayIteratorObject_QV4_Heap_ArrayIteratorObjectData(
    QV4::Heap::ArrayIteratorObject *self) {
  return static_cast<QV4::Heap::ArrayIteratorObjectData *>(self);
}
