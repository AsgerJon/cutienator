//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::QmlContext::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10QmlContext11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QmlContext::markObjects(b, stack);
}

//  QQmlContextWrapper *QV4::Heap::QmlContext::qml()
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapper *ritual_ZN3QV44Heap10QmlContext3qmlEv(
    QV4::Heap::QmlContext *self) {
  return self->qml();
}

//  QV4::Heap::QmlContext as the QV4::Heap::QmlContextData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContextData *ritual_cast_QV4_Heap_QmlContext_QV4_Heap_QmlContextData(
    QV4::Heap::QmlContext *self) {
  return static_cast<QV4::Heap::QmlContextData *>(self);
}
