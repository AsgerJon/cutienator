//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::PushCatchContext::call(ExecutionEngine *a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime16PushCatchContext4callEPNS_15ExecutionEngineEii(
    QV4::ExecutionEngine *a0,
    int a1,
    int a2) {
  QV4::Runtime::PushCatchContext::call(a0, a1, a2);
}

//  QV4::Runtime::PushCatchContext::~PushCatchContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime16PushCatchContextD1Ev(
    QV4::Runtime::PushCatchContext *self) {
  delete self;
}
