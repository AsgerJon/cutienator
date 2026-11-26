//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::PopScriptContext::call(ExecutionEngine *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime16PopScriptContext4callEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *a0) {
  QV4::Runtime::PopScriptContext::call(a0);
}

//  QV4::Runtime::PopScriptContext::~PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime16PopScriptContextD1Ev(
    QV4::Runtime::PopScriptContext *self) {
  delete self;
}
