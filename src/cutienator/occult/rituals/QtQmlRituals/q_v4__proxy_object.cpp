//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4proxy_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4proxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ProxyObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ProxyObject10__dataTestEv(QV4::ProxyObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ProxyObject *QV4::ProxyObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyObject *ritual_ZNK3QV411ProxyObject11d_uncheckedEv(
    const QV4::ProxyObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ProxyObject *QV4::ProxyObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ProxyObject *ritual_ZNK3QV411ProxyObject1dEv(
    const QV4::ProxyObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ProxyObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411ProxyObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ProxyObject::defaultInternalClass(e);
}
