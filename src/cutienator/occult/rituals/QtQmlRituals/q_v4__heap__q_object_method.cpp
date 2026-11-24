//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::QObjectMethod::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13QObjectMethod11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QObjectMethod::markObjects(b, stack);
}

//  void QV4::Heap::QObjectMethod::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13QObjectMethod7destroyEv(
    QV4::Heap::QObjectMethod *self) {
  self->destroy();
}

//  QV4::Heap::QObjectMethod as the QV4::Heap::QObjectMethodData it is built
//      on
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectMethodData *ritual_cast_QV4_Heap_QObjectMethod_QV4_Heap_QObjectMethodData(
    QV4::Heap::QObjectMethod *self) {
  return static_cast<QV4::Heap::QObjectMethodData *>(self);
}
