//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::PushScriptContext::call(ExecutionEngine *a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime17PushScriptContext4callEPNS_15ExecutionEngineEi(
    QV4::ExecutionEngine *a0,
    int a1) {
  QV4::Runtime::PushScriptContext::call(a0, a1);
}

//  QV4::Runtime::PushScriptContext::~PushScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime17PushScriptContextD1Ev(
    QV4::Runtime::PushScriptContext *self) {
  delete self;
}
