//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::CallName::call(ExecutionEngine *a0, int a1,
//      Value *a2, int a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime8CallName4callEPNS_15ExecutionEngineEiPNS_5ValueEi(
    QV4::ExecutionEngine *a0,
    int a1,
    QV4::Value *a2,
    int a3) {
  return QV4::Runtime::CallName::call(a0, a1, a2, a3);
}

//  QV4::Runtime::CallName::~CallName()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime8CallNameD1Ev(QV4::Runtime::CallName *self) {
  delete self;
}
