//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::MemberFunction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14MemberFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::MemberFunction::markObjects(b, stack);
}

//  QV4::Heap::MemberFunction as the QV4::Heap::MemberFunctionData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberFunctionData *ritual_cast_QV4_Heap_MemberFunction_QV4_Heap_MemberFunctionData(
    QV4::Heap::MemberFunction *self) {
  return static_cast<QV4::Heap::MemberFunctionData *>(self);
}
