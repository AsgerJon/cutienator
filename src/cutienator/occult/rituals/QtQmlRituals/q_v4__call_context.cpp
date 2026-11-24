//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::CallContext::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV411CallContext12staticVTableEv() {
  return QV4::CallContext::staticVTable();
}

//  void QV4::CallContext::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411CallContext10__dataTestEv(QV4::CallContext *self) {
  self->__dataTest();
}

//  QV4::Heap::CallContext *QV4::CallContext::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV411CallContext11d_uncheckedEv(
    const QV4::CallContext *self) {
  return self->d_unchecked();
}

//  QV4::Heap::CallContext *QV4::CallContext::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContext *ritual_ZNK3QV411CallContext1dEv(
    const QV4::CallContext *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::CallContext::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411CallContext20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::CallContext::defaultInternalClass(e);
}

//  int QV4::CallContext::argc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV411CallContext4argcEv(const QV4::CallContext *self) {
  return self->argc();
}

//  const Value *QV4::CallContext::args() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV411CallContext4argsEv(
    const QV4::CallContext *self) {
  return self->args();
}
