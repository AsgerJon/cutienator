//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::ExecutionContext::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV416ExecutionContext12staticVTableEv() {
  return QV4::ExecutionContext::staticVTable();
}

//  void QV4::ExecutionContext::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV416ExecutionContext10__dataTestEv(
    QV4::ExecutionContext *self) {
  self->__dataTest();
}

//  QV4::Heap::ExecutionContext *QV4::ExecutionContext::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV416ExecutionContext11d_uncheckedEv(
    const QV4::ExecutionContext *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ExecutionContext *QV4::ExecutionContext::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ExecutionContext *ritual_ZNK3QV416ExecutionContext1dEv(
    const QV4::ExecutionContext *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ExecutionContext::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV416ExecutionContext20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ExecutionContext::defaultInternalClass(e);
}

//  CallContext *QV4::ExecutionContext::asCallContext()
extern "C" Q_DECL_EXPORT
QV4::CallContext *ritual_ZN3QV416ExecutionContext13asCallContextEv(
    QV4::ExecutionContext *self) {
  return self->asCallContext();
}

//  const CallContext *QV4::ExecutionContext::asCallContext() const
extern "C" Q_DECL_EXPORT
const QV4::CallContext *ritual_ZNK3QV416ExecutionContext13asCallContextEv(
    const QV4::ExecutionContext *self) {
  return self->asCallContext();
}

//  bool QV4::ExecutionContext::virtualDeleteProperty(Managed *a0,
//      PropertyKey a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV416ExecutionContext21virtualDeletePropertyEPNS_7ManagedENS_11PropertyKeyE(
    QV4::Managed *a0,
    const QV4::PropertyKey *a1) {
  return QV4::ExecutionContext::virtualDeleteProperty(a0, *a1);
}
