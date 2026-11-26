//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::TailCall::call(JSTypesStackFrame *a0,
//      ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime8TailCall4callEPNS_17JSTypesStackFrameEPNS_15ExecutionEngineE(
    QV4::JSTypesStackFrame *a0,
    QV4::ExecutionEngine *engine) {
  return QV4::Runtime::TailCall::call(a0, engine);
}

//  QV4::Runtime::TailCall::~TailCall()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime8TailCallD1Ev(QV4::Runtime::TailCall *self) {
  delete self;
}
