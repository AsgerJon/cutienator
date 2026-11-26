//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::PushCallContext::call(JSTypesStackFrame *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime15PushCallContext4callEPNS_17JSTypesStackFrameE(
    QV4::JSTypesStackFrame *a0) {
  QV4::Runtime::PushCallContext::call(a0);
}

//  QV4::Runtime::PushCallContext::~PushCallContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime15PushCallContextD1Ev(
    QV4::Runtime::PushCallContext *self) {
  delete self;
}
