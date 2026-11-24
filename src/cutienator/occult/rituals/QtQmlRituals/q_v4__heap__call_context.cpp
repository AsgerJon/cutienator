//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::CallContext::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::CallContext::markObjects(b, stack);
}

//  void QV4::Heap::CallContext::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext4initEv(QV4::Heap::CallContext *self) {
  self->init();
}

//  int QV4::Heap::CallContext::argc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap11CallContext4argcEv(
    const QV4::Heap::CallContext *self) {
  return self->argc();
}

//  const Value *QV4::Heap::CallContext::args() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV44Heap11CallContext4argsEv(
    const QV4::Heap::CallContext *self) {
  return self->args();
}

//  QV4::Heap::CallContext as the QV4::Heap::CallContextData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContextData *ritual_cast_QV4_Heap_CallContext_QV4_Heap_CallContextData(
    QV4::Heap::CallContext *self) {
  return static_cast<QV4::Heap::CallContextData *>(self);
}
