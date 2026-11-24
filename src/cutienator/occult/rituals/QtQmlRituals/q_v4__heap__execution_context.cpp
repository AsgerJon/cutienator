//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ExecutionContext::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16ExecutionContext11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ExecutionContext::markObjects(b, stack);
}

//  void QV4::Heap::ExecutionContext::init(ContextType t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16ExecutionContext4initENS1_11ContextTypeE(
    QV4::Heap::ExecutionContext *self,
    QV4::Heap::ExecutionContext::ContextType t) {
  self->init(t);
}

//  const VTable *QV4::Heap::ExecutionContext::vtable() const
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZNK3QV44Heap16ExecutionContext6vtableEv(
    const QV4::Heap::ExecutionContext *self) {
  return self->vtable();
}

//  QV4::Heap::ExecutionContext as the QV4::Heap::ExecutionContextData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContextData *ritual_cast_QV4_Heap_ExecutionContext_QV4_Heap_ExecutionContextData(
    QV4::Heap::ExecutionContext *self) {
  return static_cast<QV4::Heap::ExecutionContextData *>(self);
}
