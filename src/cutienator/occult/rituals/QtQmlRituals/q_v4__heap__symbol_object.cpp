//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4symbol_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::SymbolObject::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12SymbolObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::SymbolObject::markObjects(b, stack);
}

//  QV4::Heap::SymbolObject as the QV4::Heap::SymbolObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::SymbolObjectData *ritual_cast_QV4_Heap_SymbolObject_QV4_Heap_SymbolObjectData(
    QV4::Heap::SymbolObject *self) {
  return static_cast<QV4::Heap::SymbolObjectData *>(self);
}
