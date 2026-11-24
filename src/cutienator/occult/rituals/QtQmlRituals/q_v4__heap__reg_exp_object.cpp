//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::RegExpObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12RegExpObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::RegExpObject::markObjects(b, stack);
}

//  QV4::Heap::RegExpObject as the QV4::Heap::RegExpObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpObjectData *ritual_cast_QV4_Heap_RegExpObject_QV4_Heap_RegExpObjectData(
    QV4::Heap::RegExpObject *self) {
  return static_cast<QV4::Heap::RegExpObjectData *>(self);
}
