//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::BoundFunction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13BoundFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::BoundFunction::markObjects(b, stack);
}

//  QV4::Heap::BoundFunction as the QV4::Heap::BoundFunctionData it is built
//      on
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundFunctionData *ritual_cast_QV4_Heap_BoundFunction_QV4_Heap_BoundFunctionData(
    QV4::Heap::BoundFunction *self) {
  return static_cast<QV4::Heap::BoundFunctionData *>(self);
}
