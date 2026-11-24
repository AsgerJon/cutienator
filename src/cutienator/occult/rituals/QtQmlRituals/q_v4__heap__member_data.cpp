//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4memberdata_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4memberdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::MemberData::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10MemberData11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::MemberData::markObjects(b, stack);
}

//  QV4::Heap::MemberData as the QV4::Heap::MemberDataData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberDataData *ritual_cast_QV4_Heap_MemberData_QV4_Heap_MemberDataData(
    QV4::Heap::MemberData *self) {
  return static_cast<QV4::Heap::MemberDataData *>(self);
}
