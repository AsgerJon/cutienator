//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::StringObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12StringObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::StringObject::markObjects(b, stack);
}

//  void QV4::Heap::StringObject::init(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12StringObject4initEb(
    QV4::Heap::StringObject *self,
    bool a0) {
  self->init(a0);
}

//  QV4::Heap::StringObject as the QV4::Heap::StringObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::StringObjectData *ritual_cast_QV4_Heap_StringObject_QV4_Heap_StringObjectData(
    QV4::Heap::StringObject *self) {
  return static_cast<QV4::Heap::StringObjectData *>(self);
}
