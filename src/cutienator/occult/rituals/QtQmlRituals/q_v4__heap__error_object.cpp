//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ErrorObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ErrorObject::markObjects(b, stack);
}

//  void QV4::Heap::ErrorObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject7destroyEv(
    QV4::Heap::ErrorObject *self) {
  self->destroy();
}

//  QV4::Heap::ErrorObject as the QV4::Heap::ErrorObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorObjectData *ritual_cast_QV4_Heap_ErrorObject_QV4_Heap_ErrorObjectData(
    QV4::Heap::ErrorObject *self) {
  return static_cast<QV4::Heap::ErrorObjectData *>(self);
}
