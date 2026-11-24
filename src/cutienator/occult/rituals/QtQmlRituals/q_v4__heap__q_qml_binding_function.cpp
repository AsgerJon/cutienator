//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::QQmlBindingFunction::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap19QQmlBindingFunction11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QQmlBindingFunction::markObjects(b, stack);
}

//  QV4::Heap::QQmlBindingFunction as the QV4::Heap::QQmlBindingFunctionData
//      it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlBindingFunctionData *ritual_cast_QV4_Heap_QQmlBindingFunction_QV4_Heap_QQmlBindingFunctionData(
    QV4::Heap::QQmlBindingFunction *self) {
  return static_cast<QV4::Heap::QQmlBindingFunctionData *>(self);
}
