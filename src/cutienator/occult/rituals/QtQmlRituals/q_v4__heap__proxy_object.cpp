//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4proxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::ProxyObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ProxyObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ProxyObject::markObjects(b, stack);
}

//  QV4::Heap::ProxyObject as the QV4::Heap::ProxyObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyObjectData *ritual_cast_QV4_Heap_ProxyObject_QV4_Heap_ProxyObjectData(
    QV4::Heap::ProxyObject *self) {
  return static_cast<QV4::Heap::ProxyObjectData *>(self);
}
