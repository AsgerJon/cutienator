//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ResolveElementWrapper::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap21ResolveElementWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ResolveElementWrapper::markObjects(b, stack);
}

//  QV4::Heap::ResolveElementWrapper as the
//      QV4::Heap::ResolveElementWrapperData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ResolveElementWrapperData *ritual_cast_QV4_Heap_ResolveElementWrapper_QV4_Heap_ResolveElementWrapperData(
    QV4::Heap::ResolveElementWrapper *self) {
  return static_cast<QV4::Heap::ResolveElementWrapperData *>(self);
}
