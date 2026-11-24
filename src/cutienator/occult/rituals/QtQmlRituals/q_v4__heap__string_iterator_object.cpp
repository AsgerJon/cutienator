//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringiterator_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::StringIteratorObject::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20StringIteratorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::StringIteratorObject::markObjects(b, stack);
}

//  void QV4::Heap::StringIteratorObject::init(String *str,
//      QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap20StringIteratorObject4initEPNS0_6StringEPNS_15ExecutionEngineE(
    QV4::Heap::StringIteratorObject *self,
    QV4::Heap::String *str,
    QV4::ExecutionEngine *engine) {
  self->init(str, engine);
}

//  QV4::Heap::StringIteratorObject as the
//      QV4::Heap::StringIteratorObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::StringIteratorObjectData *ritual_cast_QV4_Heap_StringIteratorObject_QV4_Heap_StringIteratorObjectData(
    QV4::Heap::StringIteratorObject *self) {
  return static_cast<QV4::Heap::StringIteratorObjectData *>(self);
}
