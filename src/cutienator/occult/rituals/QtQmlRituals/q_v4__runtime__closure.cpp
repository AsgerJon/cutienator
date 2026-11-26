//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  ReturnedValue QV4::Runtime::Closure::call(ExecutionEngine *a0, int a1)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Runtime7Closure4callEPNS_15ExecutionEngineEi(
    QV4::ExecutionEngine *a0,
    int a1) {
  return QV4::Runtime::Closure::call(a0, a1);
}

//  QV4::Runtime::Closure::~Closure()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime7ClosureD1Ev(QV4::Runtime::Closure *self) {
  delete self;
}
