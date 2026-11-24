//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::QQmlContextWrapper::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap18QQmlContextWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QQmlContextWrapper::markObjects(b, stack);
}

//  QV4::Heap::QQmlContextWrapper as the QV4::Heap::QQmlContextWrapperData it
//      is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapperData *ritual_cast_QV4_Heap_QQmlContextWrapper_QV4_Heap_QQmlContextWrapperData(
    QV4::Heap::QQmlContextWrapper *self) {
  return static_cast<QV4::Heap::QQmlContextWrapperData *>(self);
}
